#!/usr/bin/env python3
"""把藥物頁正文的刪改轉成查核紀錄（docs/_data/drug_reviews.json 的 action: correct）（2026-11-12 建，本站查核機制）。

為什麼要有這支：
  2026-10-31 與 2026-11-05～06 依成分重建許可證後，正文裡跟新事實矛盾的句子是直接刪掉（只刪矛盾子句）的，
  頁面上看不出改過什麼，下次 scripts/sync_notes_to_docs.py 依 notes 重寫整頁時也會被蓋回去。
  用戶 2026-11-12 決定：這些刪改轉成查核紀錄（頁面上顯示 Review correction 框與 Review Log），以後的刪句也一樣。
  兩種用法共用同一套抽取規則：
    --git：依 git 提交前後的頁面轉（歷史的刪改，COMMITS 列出的提交）
    --dirs：依改寫前後兩個目錄轉（scripts/license_rebuild_run.py 刪句後呼叫）

抽取規則（只看正文）：
  - 去掉 front matter、查核框、程式區塊標記；表格、SHOW 句、NONE_LINE（程式產生的許可證文字）不算正文。
  - 正文切成段落、段落再切成行與句子，依序比對；有變的連續句子＝一筆（claim＝原句、replacement＝新句）。
  - 整句被刪（replacement 會是空的）：claim 往前（沒有前句就往後）多帶一句，replacement＝那一句，讓錨點在頁面上找得到；
    整段被刪：claim＝那一段、replacement 空、anchor＝前一段（頁面上要唯一）。
  - 同一處前後改過多次（例 10-31 刪了一半、11-05 再刪），依時間合併成一筆：claim＝最早的原句、replacement＝最後的版本。
理由（note 是頁面上顯示的英文、finding 是內部紀錄）：
  - scripts/license_sentence_fixes.json 的人工清單有這句（sentence／cut 落在 claim 裡）→ finding＝該筆 reason。
  - 其他依被刪文字分類（台灣模板殘留、單方／複方、全部註銷／停產、張數、產品描述），note 附快照裡目前的申請數與有效數。
狀態：
  - 頁面上找得到 replacement（或整段刪除時的 anchor）→ 照常顯示框。
  - 找不到、而且頁面在之後被 AI 重產過報告（REGEN_COMMITS）→ status: resolved_by_regeneration（紀錄保留、不顯示框）。
  - 其他找不到的 → 不寫入，列在輸出，交人工判斷。

用法（repo 根目錄）：
  python3 scripts/reviews_from_edits.py --git [--write]            # 歷史的 12 次刪改（COMMITS）
  python3 scripts/reviews_from_edits.py --dirs 前目錄 後目錄 --date YYYY-MM-DD --commit 說明 [--write]
沒有 --write 只列出結果，不寫檔。寫入後跑 python3 scripts/apply_drug_reviews.py。
"""
from __future__ import annotations

import difflib
import gzip
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "_data" / "drug_reviews.json"
FIXES = ROOT / "scripts" / "license_sentence_fixes.json"
sys.path.insert(0, str(ROOT / "src"))
from mytxgnn.regulatory import site as C  # noqa: E402

SNAP = ROOT / "snapshots" / f"{C.CODE}_licenses.json.gz"
# 歷史的許可證刪改與期間內的 AI 重產提交：本站的清單在 site.py（COMMITS、REGEN_COMMITS）
COMMITS = C.COMMITS
REGEN_COMMITS = C.REGEN_COMMITS
SOURCES = C.SOURCES
SENT = C.SENT
BLOCK_RE = re.compile(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", re.S)


# ---------- 抽取 ----------
def body(t):
    t = t.replace("\r\n", "\n")
    if t.startswith("---"):
        e = t.find("\n---", 3)
        t = t[e + 4:] if e >= 0 else t
    t = BLOCK_RE.sub("", t)
    return re.sub(r"<!-- licenses:(begin|end) -->", "", t)


def is_prose(p):
    s = p.strip()
    return bool(s) and not s.startswith("|") and not s.startswith("{:") and not s.startswith("<!--") and not s.startswith("#") \
        and not any(rx.match(s) for rx in C.PROGRAM_LINES)


def paras(t):
    """正文段落：空行分段；段落裡的標題行（# 開頭，例：清單後直接接「## Disclaimer」）也斷開，標題本身不算正文"""
    out = []
    for blk in re.split(r"\n[ \t]*\n", t):
        cur = []
        for ln in blk.split("\n"):
            if ln.startswith("#"):
                if cur:
                    out.append("\n".join(cur))
                cur = []
                continue
            cur.append(ln)
        if cur:
            out.append("\n".join(cur))
    return [p.strip("\n") for p in out if is_prose(p)]


def spans(p):
    out, i = [], 0
    for m in SENT.finditer(p):
        if m.start() > i:
            out.append((i, m.start()))
        i = m.end()
    if i < len(p):
        out.append((i, len(p)))
    return out


def in_para(a, b):
    """段落 a→b 有變的句子群 → [[(claim, replacement), …]]：每群由小到大的候選（往前後多帶相同的句子），
    claim 是 a 的子字串、replacement 是 b 的子字串；定稿時取第一個在頁面上唯一的候選"""
    sa, sb = spans(a), spans(b)
    ta, tb = [a[x:y] for x, y in sa], [b[x:y] for x, y in sb]
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        cands = []
        for k1 in range(0, 4):
            for k2 in range(0, 4):
                x1, x2, y1, y2 = i1 - k1, i2 + k2, j1 - k1, j2 + k2
                if x1 < 0 or y1 < 0 or x2 > len(ta) or y2 > len(tb) or y2 == y1 or x2 == x1:
                    continue  # replacement 不能空（錨點）；claim 也不能空（純插入的句子要多帶相鄰句才能定位，例 Za 補回句）
                # claim 前後的分隔（空白或換行）要跟 replacement 前後的一樣，套用後才不會把兩行併成一行（例 My atropine：
                # 整句刪掉時往後帶下一行當錨點，claim 前是空白、replacement 前是換行）；不一樣的候選排到後面
                sep = lambda s, sp, i: s[sp[i - 1][1] if i > 0 else 0:sp[i][0] if i < len(sp) else len(s)]
                bad = sep(a, sa, x1) != sep(b, sb, y1) or sep(a, sa, x2) != sep(b, sb, y2)
                cands.append((k1 + k2 + (10 if bad else 0), (a[sa[x1][0]:sa[x2 - 1][1]] if x2 > x1 else "", b[sb[y1][0]:sb[y2 - 1][1]])))
        if not cands:
            continue  # 段落只剩這句又整句刪：由段落層級處理
        cands = [c for _, c in sorted(cands, key=lambda x: x[0])]
        whole = [(f"\n{c}\n", f"\n{r}\n") for c, r in cands if c == a and r == b]  # 整段＝這幾句：前後帶換行，跟段落中間的同一句區分
        out.append(cands + whole)
    return out


def changes(before, after):
    """兩版頁面 → [(claim, replacement, anchor)]"""
    pa, pb = paras(body(before)), paras(body(after))
    out = []
    def deleted(i, j1):
        """整段刪掉：錨點候選＝新版前後各三段（定稿時取第一個在頁面上唯一的）"""
        near = [pb[j] for j in (j1 - 1, j1, j1 - 2, j1 + 1, j1 - 3, j1 + 2) if 0 <= j < len(pb)]
        out.append([(pa[i], "", x) for x in near] or [(pa[i], "", "")])

    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, pa, pb, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        if op == "insert":
            # 只有新增不是更正；但「刪句後補回部分內容」（例 Za d5c6364b6：只刪矛盾子句、其餘補回）要併回先前的整段刪除紀錄
            for j in range(j1, j2):
                out.append([("", pb[j], "", "insert")])
            continue
        # 段落配對：所有（原段落, 新段落）組合算相似度（新段落的字都在原段落裡也算高分），從最高分開始配、保持先後順序；
        # 配上的做段內比對，配不上的原段落是整段刪除。不把多段接成一筆（段落之間常隔著表格，接起來在頁面上不相連）。
        # 不用「依序各挑最像的」：會把被刪的段落錯配到後面那段的新版（2026-11-12 Za arginine）
        def score(x, y):
            r = difflib.SequenceMatcher(None, x, y, autojunk=False).ratio()
            wb, wa = re.findall(r"\w+", y.lower()), set(re.findall(r"\w+", x.lower()))
            if y.strip() and (y.strip() in x or (len(wb) >= 2 and set(wb) <= wa)):
                r = max(r, 0.6 + 0.4 * r)  # 刪掉大半只剩一句（例 atropine「Five examples:」）
            return r
        cand = sorted(((score(pa[i], pb[k]), i, k) for i in range(i1, i2) for k in range(j1, j2)), reverse=True)
        pairs = {}
        for s, i, k in cand:
            if s < 0.5 or i in pairs or k in pairs.values():
                continue
            if any((i2_ < i) != (k2_ < k) for i2_, k2_ in pairs.items()):
                continue  # 保持先後順序
            pairs[i] = k
        for i in range(i1, i2):
            if i in pairs:
                for cands in in_para(pa[i], pb[pairs[i]]):
                    out.append([(c, r, "") for c, r in cands])
            else:
                deleted(i, min([k for ii, k in pairs.items() if ii > i] or [j2]))
        for k in range(j1, j2):
            if k not in pairs.values():
                out.append([("", pb[k], "", "insert")])  # 新段落（可能是補回的內容）
    return out


# ---------- 理由 ----------
def load_fixes():
    if not FIXES.exists():
        return {}
    return json.loads(FIXES.read_text(encoding="utf-8"))


def snap_facts():
    if not SNAP.exists():
        return {}
    return {k: v.get("facts") or {} for k, v in json.loads(gzip.open(SNAP).read().decode("utf-8"))["drugs"].items()}


def removed_text(claim, repl):
    """claim 裡被刪掉的字：以詞為單位比對（不分大小寫、不計標點），避免逐字比對把「dan p」「alaysia」這種半個詞當成刪除"""
    wa, wb = claim.split(), repl.split()
    key = lambda w: re.sub(r"[^\w]", "", w.lower())
    sm = difflib.SequenceMatcher(None, [key(w) for w in wa], [key(w) for w in wb], autojunk=False)
    return " ".join(" ".join(wa[i1:i2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op in ("delete", "replace"))


def classify(rm):
    for kind, rx in C.CLASSIFY:
        if rx.search(rm):
            return kind
    return "generic"


def note_for(kind, date, fc):
    return C.note_for(kind, date, fc)


def manual_reason(fixes, stem, claim):
    for it in fixes.get(stem) or []:
        kp = it.get("keep")
        if kp is True or (isinstance(kp, str) and kp.strip() == (it.get("sentence") or "").strip()):
            continue  # 人工判定整句保留（沒有刪任何字）的項目不當理由
        s = (it.get("sentence") or "").strip()
        cuts = it.get("cut") or []
        cuts = [x.strip(" ,;") for x in (cuts if isinstance(cuts, list) else [cuts])]
        if (s and s in claim) or any(len(c) > 6 and c in claim for c in cuts):
            return it.get("reason") or ""
    return ""


# ---------- 合併與狀態 ----------
def compose(recs, cands, meta):
    """同一處前後改過多次 → 合併成一筆（claim＝最早原句、replacement＝最新版）。回傳是否已併入既有紀錄。
    合併用最小的候選比對；合併後候選只剩合併結果（再往外帶句子的候選要依新頁面重算，這裡不做）"""
    if len(cands[0]) == 4:  # 新增段落：補回先前整段刪掉的部分內容 → 那筆的 replacement 改成補回的文字
        added = cands[0][1]
        wa = set(re.findall(r"\w+", added.lower()))
        for r in recs:
            c0, r0, a0 = r["cands"][0]
            wc = set(re.findall(r"\w+", c0.lower())) if c0 else set()
            if not r0 and c0 and wa and len(wa & wc) >= 0.8 * len(wa):  # 補回時可能小改幾個字：八成以上的詞出現在原句就算
                r["cands"] = [(c0, added, "")]
                r["_meta"].append(meta)
                return True
        return True  # 其他單純新增不轉紀錄
    claim, repl, anchor = cands[0]
    for r in recs:
        old = r["cands"][0][1]
        if old and claim and claim in old:
            new = [(c0, old.replace(claim, repl, 1), a0 or anchor) for c0, r0, a0 in r["cands"] if r0 == old] or \
                  [(r["cands"][0][0], old.replace(claim, repl, 1), anchor)]
        elif old and claim and old in claim:
            new = [(c.replace(old, r["cands"][0][0], 1), rp, a) for c, rp, a in cands if old in c]
        else:
            continue
        r["cands"] = new
        r["_meta"].append(meta)
        return True
    return False


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout


def show(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def commit_date(h):
    return git("log", "-1", "--format=%cs", h).strip()


def regen_pages():
    out = set()
    for h in REGEN_COMMITS:
        out |= {Path(f).name for f in git("diff", "--name-only", f"{h}^", h, "--", "docs/_drugs").split()}
    return out


def build(pairs):
    """pairs：[(檔名, 前文, 後文, 日期, 提交)]，依時間排序 → {檔名: [紀錄草稿]}"""
    by = {}
    for fname, before, after, date, commit in pairs:
        recs = by.setdefault(fname, [])
        for cands in changes(before, after):
            meta = {"date": date, "commit": commit}
            if not compose(recs, cands, meta):
                recs.append({"cands": cands, "_meta": [meta]})
    return by


def pick(cands, cur_body):
    """候選裡第一個能在目前頁面上唯一定位的：replacement（整段刪除時是 anchor）在頁面上剛好出現一次；
    或頁面上又是原句（claim 剛好出現一次，套用時會再更正）。都不行回 None"""
    for c, r, a in cands:
        loc = r or a
        if c == r or not c.strip():
            continue
        if loc and cur_body.count(loc) == 1:
            return c, r, a, "located"
    for c, r, a in cands:
        if c.strip() and c != r and cur_body.count(c) == 1 and (r or a):
            return c, r, a, "claim_on_page"
    return None


def finalize(by, current, regen, fixes, facts, existing_ids):
    """草稿 → 正式紀錄；回傳 (紀錄, 無法定位的草稿)"""
    out, lost = [], []
    for fname, recs in sorted(by.items()):
        stem = fname[:-3]
        cur = current(fname)
        if cur is None or 'http-equiv="refresh"' in cur[:3000]:
            continue
        cur_body = body(cur)
        n = 0
        for r in recs:
            got = pick(r["cands"], cur_body)
            if got is None:
                c0, r0, a0 = r["cands"][0]
                if c0 == r0 or not c0.strip():
                    continue
                if fname in regen:
                    got = (c0, r0, a0, "regen")
                else:
                    lost.append((fname, {"claim": c0, "replacement": r0}))
                    continue
            r = dict(r, claim=got[0], replacement=got[1], anchor=got[2], how=got[3])
            n += 1
            first, last = r["_meta"][0], r["_meta"][-1]
            rm = removed_text(r["claim"], r["replacement"])
            reason = manual_reason(fixes, stem, r["claim"])
            kind = (C.reason_kind(reason) if reason and hasattr(C, "reason_kind") else None) or classify(rm)
            rec = {
                "id": f"{C.CODE}-lic-{first['date'].replace('-', '')}-{stem}-{n}",
                "drug": stem, "file": fname, "action": "correct",
                "claim": r["claim"], "replacement": r["replacement"],
                "note": note_for(kind, last["date"], facts.get(stem)),
                "finding": reason or f"依成分重建許可證後，正文跟新事實矛盾的子句由刪句工具刪除（分類：{kind}）",
                "sources": [dict(s, accessed=last["date"]) for s in SOURCES],
                "checked": last["date"],
                "summary": C.SUMMARY.format(text=" ".join((rm.strip(" ,;.、。\n-") or r["claim"]).split())[:140]),
                "method": ("2026-11-12 由 git 提交前後的頁面轉入查核紀錄（scripts/reviews_from_edits.py）；原本的刪改：" +
                           "、".join(f"{m['commit']}（{m['date']}）" for m in r["_meta"])),
            }
            if not r["replacement"]:
                rec["anchor"] = r["anchor"]
            if r["how"] == "regen":
                rec["status"] = "resolved_by_regeneration"
                rec["resolved_on"] = "2026-11-12"
                rec["resolved_note"] = C.REGEN_NOTE
            if rec["id"] in existing_ids:
                continue
            out.append(rec)
    return out, lost


def write(new):
    doc = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else {"_doc": DOC, "schema_version": 1, "records": []}
    have = {r["id"] for r in doc["records"]}
    doc["records"] += [r for r in new if r["id"] not in have]
    DATA.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


DOC = ("藥物頁人工查核紀錄（單一真實來源；2026-11-12 建，核心流程比照 TwTxGNN docs/_data/drug_reviews.json，欄位相同）。"
       "每筆＝一次查核：drug／file／claim（頁面原句）／replacement（更正後）／note（頁面上顯示的本站語言說明）／finding（內部查證結論）／"
       "sources（網址＋查閱日）／checked（查核日）／action（correct 更正｜annotate 加註｜rereview 待重審｜section 附來源段落｜"
       "rereview_result 重審結果｜header_level｜description_level）。由 scripts/apply_drug_reviews.py 套到 docs/_drugs/*.md；"
       "改寫頁面的程式結尾都會重套，scripts/check_seo_docs.py 第 17 項擋未套用的紀錄。原則：基本事實照主管機關資料更正；"
       "模型預測原文不刪不改寫，只加註；證據等級與決策只在重審結果為降級、升級或撤回時更新。"
       "2026-10-31、11-05～06 依成分重建許可證後直接刪掉的矛盾子句，2026-11-12 由 scripts/reviews_from_edits.py 依 git 前後版本轉入"
       "（id 以 <站碼>-lic- 開頭）；報告在 11 月經 AI 重產、原句已不在頁面的標 status=resolved_by_regeneration。"
       "同 id 重發時前版存進 history（retired、reason），不覆蓋丟棄。")


def main(argv):
    fixes, facts = load_fixes(), snap_facts()
    existing = {r["id"] for r in json.loads(DATA.read_text(encoding="utf-8"))["records"]} if DATA.exists() else set()
    if "--git" in argv:
        pairs = []
        for h in COMMITS:
            d = commit_date(h)
            for f in git("diff", "--name-only", f"{h}^", h, "--", "docs/_drugs").split():
                b, a = show(f"{h}^", f), show(h, f)
                if b and a:
                    pairs.append((Path(f).name, b, a, d, h))
        by = build(pairs)
        current = lambda fn: (ROOT / "docs/_drugs" / fn).read_text(encoding="utf-8") if (ROOT / "docs/_drugs" / fn).exists() else None
        recs, lost = finalize(by, current, regen_pages(), fixes, facts, existing)
    elif "--dirs" in argv:
        i = argv.index("--dirs")
        bd, ad = Path(argv[i + 1]), Path(argv[i + 2])
        d = argv[argv.index("--date") + 1]
        c = argv[argv.index("--commit") + 1] if "--commit" in argv else "license-rebuild"
        pairs = [(f.name, f.read_text(encoding="utf-8"), (ad / f.name).read_text(encoding="utf-8"), d, c)
                 for f in sorted(bd.glob("*.md")) if (ad / f.name).exists()]
        by = build(pairs)
        current = lambda fn: (ad / fn).read_text(encoding="utf-8") if (ad / fn).exists() else None
        recs, lost = finalize(by, current, set(), fixes, facts, existing)
    else:
        sys.exit(__doc__)
    act = sum(1 for r in recs if not r.get("status"))
    print(f"紀錄 {len(recs)} 筆（顯示框 {act}、報告重產後已無此錯誤 {len(recs) - act}），{len({r['file'] for r in recs})} 頁；"
          f"無法定位 {len(lost)} 筆")
    for fn, r in lost[:30]:
        print(f"  ? {fn}：{r['claim'][:90]!r} → {r['replacement'][:60]!r}")
    if "--write" in argv:
        write(recs)
        print(f"已寫入 {DATA.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
