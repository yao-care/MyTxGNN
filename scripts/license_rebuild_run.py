"""依成分重建許可證的整套流程（2026-11-05，用戶核准；給 .github/workflows/license-rebuild.yml 用，全程不用 AI）。
做法比照 ZaTxGNN 的同名腳本；NPRA（data.gov.my）現行註冊與撤銷清單，重建前重新下載（--skip-download 用 Release 裡的檔）。

步驟：
1. 重建前先跑一次 checker 當基準（既存的非 M 類錯誤與許可證無關，不在這次處理）。
2. scripts/rebuild_licenses_by_ingredient.py：依成分重建 data/bundles 的許可證紀錄。
3. 事實層（dump_license_facts）→ 許可證表狀態格（license_table_sync.apply，用語取 .claude/license_labels/<站>.json）、獸用列刪除 →
   概覽表狀態列、張數列（sync_market_rows）→ 刪掉跟新事實矛盾的句子（.claude/delete_license_sentences.py，
   人工核對清單 scripts/license_sentence_fixes.json）→ lastmod（正文有變才換日期）。
5. 停損（任一條不過就把 docs 還原、exit 非 0，workflow 開 issue）：
   - checker：任何 M 類（市場狀態）錯誤，或出現基準以外的新錯誤
   - gate（scripts/check_seo_docs.py）沒過；改到的頁 h1 不是恰好 1 個
   - 改到的頁數超過 --max-pages（預設 min(200, 5%)；這次一次性重建由 request 檔指定）
結果寫 .license_rebuild/（summary.md、rebuild.tsv、rebuild.excluded.tsv、deletions.tsv、pages.diff）。
用法（repo 根目錄）：python3 scripts/license_rebuild_run.py --ws <工作目錄> [--max-pages N] [--skip-download]
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = (ROOT / "tools/txgnn/SITE").read_text(encoding="utf-8").strip()
OUT = ROOT / ".license_rebuild"
PY = sys.executable


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def run(cmd, cwd=ROOT, check=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(map(str, cmd))} 失敗：{(r.stderr or r.stdout)[-1500:]}")
    return r


def checker(ws):
    out = run([PY, ".claude/checker_trend.py", "--no-append", SITE], cwd=ws, check=False).stdout
    det = re.search(r"明細 (\S+)", out)
    if not det:
        raise RuntimeError("checker 沒有輸出明細：" + out[-500:])
    res = {}
    for l in (ws / det.group(1)).read_text(encoding="utf-8").split("\n")[1:]:
        c = l.split("\t")
        if len(c) == 4 and c[3]:
            res[c[1]] = set(c[3].split(","))
    return res, out.strip().split("\n")[0]


def changed_pages():
    s = run(["git", "status", "--porcelain", "--", "docs/_drugs"]).stdout
    return sorted(l[3:].strip() for l in s.split("\n") if l.strip().endswith(".md"))


SEP = re.compile(r"^\|[\s:|-]+\|\s*$")


def refill_empty_tables(pages, lts):
    """獸用列刪完只剩表頭的許可證表：證據包有人用許可就依序列前 5 張（許可證號、品名、劑型；表頭以外的欄位寫「Ikke angivet」），
    沒有（只有獸用許可）就整張表拿掉。表頭第一欄是許可證號欄（nummer／tilladelse／MA…）才處理。"""
    nfill = nrm = 0
    for stem in pages:
        pg = ROOT / "docs/_drugs" / f"{stem}.md"
        bf = ROOT / "data/bundles" / stem.replace("-", "_") / "drug_bundle.json"
        if not pg.exists() or not bf.exists():
            continue
        recs = lts.reg_block(json.loads(bf.read_text(encoding="utf-8"))).get("records") or []
        lines = pg.read_text(encoding="utf-8").split("\n")
        out, i, ch = [], 0, False
        while i < len(lines):
            l = lines[i]
            if l.startswith("|") and i + 1 < len(lines) and SEP.match(lines[i + 1]) and not (i + 2 < len(lines) and lines[i + 2].startswith("|")) \
                    and re.search(r"nummer|tilladelse|godkendelse|licen|^\s*MA\b", l.split("|")[1] if l.count("|") > 1 else "", re.I):
                ncol = l.count("|") - 1
                if recs:
                    out += [l, lines[i + 1]]
                    for r in recs[:5]:
                        df = (r.get("dosage_form") or "").strip()
                        cells = [r.get("license_id") or "", r.get("brand_name_zh") or "", df[:1].upper() + df[1:]] + ["Ikke angivet"] * max(0, ncol - 3)
                        out.append("| " + " | ".join(cells[:ncol]) + " |")
                    nfill += 1
                else:
                    nrm += 1
                    if out and not out[-1].strip() and i + 2 < len(lines) and not lines[i + 2].strip():
                        i += 1  # 拿掉表後不留連續空行
                i += 2
                ch = True
                continue
            out.append(l)
            i += 1
        if ch:
            pg.write_text("\n".join(out), encoding="utf-8")
    return nfill, nrm


def main(argv):
    ws = Path(argv[argv.index("--ws") + 1])
    OUT.mkdir(exist_ok=True)
    S = []
    md = lambda: (OUT / "summary.md").write_text("\n".join(S) + "\n", encoding="utf-8")  # noqa: E731

    def stop(code, msg):
        S.insert(0, f"## {SITE} 依成分重建許可證：{msg}\n")
        run(["git", "diff", "--", "docs"], check=False)
        (OUT / "pages.diff").write_text(run(["git", "diff", "--", "docs"], check=False).stdout, encoding="utf-8")
        if code:
            run(["git", "checkout", "--", "docs", "snapshots"], check=False)  # 快照跟頁面一起還原（2026-11-12）
        md()
        print("\n".join(S))
        sys.exit(code)

    if changed_pages():
        stop(4, "工作目錄已有未提交的藥物頁改動，中止")
    # 1. 基準 checker
    run([PY, ".claude/dump_license_facts_20261021.py", SITE], cwd=ws)
    base, base_line = checker(ws)
    pre_p = sum(1 for c in base.values() if any(not x.startswith("M") for x in c))
    pre_m = sum(1 for c in base.values() if any(x.startswith("M") for x in c))
    S.append(f"- 重建前 checker：{base_line}（M 類＝市場狀態矛盾 {pre_m} 頁，本次要清掉；其他類 {pre_p} 頁是既存問題，與許可證無關，本次不處理）")
    lts = _load("lts", ws / ".claude/license_table_sync_20261029.py")
    lf = ws / ".claude/license_labels" / f"{SITE}.json"
    labels = json.loads(lf.read_text(encoding="utf-8")) if lf.exists() else lts.learn(SITE)  # 用重建前的事實學
    # 2. 重建證據包
    dl = ["--skip-download"] if "--skip-download" in argv else []  # NPRA 現行註冊與撤銷清單：重建前重新下載
    r = run([PY, "scripts/rebuild_licenses_by_ingredient.py", *dl, "--report", str(OUT / "rebuild.tsv")], check=False)
    if r.returncode != 0:
        stop(2, "許可清單下載或重建失敗：" + (r.stderr or r.stdout)[-300:])
    S.append("- 重建：" + r.stdout.strip().split("\n")[-1])
    # 4. 事實層、概覽表、許可證表、刪句、lastmod
    run([PY, ".claude/dump_license_facts_20261021.py", SITE], cwd=ws)
    tch, uns = lts.apply(SITE, labels)
    dropped = lts.drop_excluded_rows(SITE)  # 許可證表裡的獸用許可列（veterinary_records）刪除
    tch += dropped
    nfill, nrm = refill_empty_tables(sorted({d[0] for d in dropped}), lts)
    S.append(f"- 獸用許可列刪除 {len(dropped)} 列；刪完只剩表頭的許可證表：{nfill} 張改列人用許可（程式產生），{nrm} 張（只有獸用許可）拿掉")
    S.append(f"- 許可證表狀態格改 {len(tch)} 格" + (f"（本站沒有寫法、未改 {len(uns)} 格）" if uns else ""))
    rows = lts.sync_market_rows(SITE)
    S.append(f"- 概覽表狀態／張數列改 {sum(len(v) for v in rows.values())} 格（{len(rows)} 頁）")
    # 2026-11-12 本站查核機制：刪句前先存一份頁面，刪完把刪掉的子句轉成查核紀錄（docs/_data/drug_reviews.json），
    # 再重套紀錄、重建許可證快照（gate 的查核紀錄、許可證項目檢查）
    import shutil
    before = OUT / "pages_before_delete"
    shutil.rmtree(before, ignore_errors=True)
    shutil.copytree(ROOT / "docs/_drugs", before)
    r = run([PY, ".claude/delete_license_sentences.py", SITE, "--log", str(OUT / "deletions.tsv")], cwd=ws)
    S.append("- 矛盾句：" + r.stdout.strip().split("\n")[-1])
    today_rec = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    # 2026-11-12：轉紀錄前先用新事實重建快照（reviews_from_edits 的紀錄說明讀快照的張數；舊順序會寫進舊張數）。
    # 套完紀錄後下面還會再建一次，確保最後的快照跟頁面一致。
    r = run([PY, "scripts/build_license_snapshot.py", "--ws", str(ws), "--no-rewrite"], check=False)
    if r.returncode != 0:
        stop(4, "許可證快照重建失敗（轉紀錄前）：" + (r.stdout + r.stderr)[-300:])
    r = run([PY, "scripts/reviews_from_edits.py", "--dirs", str(before), str(ROOT / "docs/_drugs"),
             "--date", today_rec, "--commit", "license-rebuild " + os.environ.get("GITHUB_RUN_ID", "local"), "--write"], check=False)
    S.append("- 查核紀錄：" + (r.stdout.strip().split("\n") or [""])[0])
    if r.returncode != 0:
        stop(4, "刪句轉查核紀錄失敗：" + (r.stdout + r.stderr)[-300:])
    r = run([PY, "scripts/apply_drug_reviews.py"], check=False)
    S.append("- " + (r.stdout.strip().split("\n") or [""])[-1])
    if r.returncode != 0:
        stop(4, "查核紀錄套用有問題：" + (r.stdout + r.stderr)[-300:])
    r = run([PY, "scripts/build_license_snapshot.py", "--ws", str(ws)], check=False)
    S.append("- " + (r.stdout.strip().split("\n") or [""])[-1])
    if r.returncode != 0:
        stop(4, "許可證快照重建失敗：" + (r.stdout + r.stderr)[-300:])
    shutil.rmtree(before, ignore_errors=True)
    lr = _load("lr", ws / ".claude/license_refresh_20261029.py")
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    n_body = lr.fix_lastmod(SITE, today)
    pages = changed_pages()
    S.append(f"- 藥物頁改 {len(pages)} 頁（正文有變 {n_body} 頁，last_modified_at 換成 {today}）")
    # 5. 停損
    after, after_line = checker(ws)
    S.append(f"- 重建後 checker：{after_line}")
    bad = {p: sorted(x for x in c - base.get(p, set()) if not x.startswith("M")) for p, c in after.items()
           if any(not x.startswith("M") for x in c - base.get(p, set()))}
    m_bad = {p: sorted(x for x in c if x.startswith("M")) for p, c in after.items() if any(x.startswith("M") for x in c)}
    if bad or m_bad:
        S.append("\n### checker 新增錯誤\n\n" + "\n".join(f"- `{p}`：{', '.join(bad.get(p) or m_bad.get(p))}" for p in sorted(set(bad) | set(m_bad))))
        stop(4, "checker 出現基準以外的新錯誤（或 M 類錯誤），頁面已還原")
    g = run([PY, "scripts/check_seo_docs.py"], check=False)
    if g.returncode != 0:
        S.append("- gate 輸出：" + (g.stdout + g.stderr)[-800:])
        stop(4, "gate（check_seo_docs.py）沒過，頁面已還原")
    lc = _load("lc", ws / ".claude/launch_commit_20261028.py")
    h1bad = [p for p in pages if lc.h1_count((ROOT / p).read_text(encoding="utf-8")) != 1]
    if h1bad:
        S.append("- h1 不是 1 個：" + ", ".join(h1bad[:20]))
        stop(4, f"{len(h1bad)} 頁 h1 不是恰好 1 個，頁面已還原")
    total = len(list((ROOT / "docs/_drugs").glob("*.md")))
    limit = min(200, max(1, int(total * 0.05)))
    if "--max-pages" in argv:
        limit = int(argv[argv.index("--max-pages") + 1])
    if len(pages) > limit:
        stop(3, f"改到 {len(pages)} 頁，超過停損 {limit} 頁，頁面已還原")
    n_del = max(0, len((OUT / "deletions.tsv").read_text(encoding="utf-8").strip().split("\n")) - 1)
    stop(0, f"可以 merge：改 {len(pages)} 頁、刪句 {n_del} 句，checker 無新增錯誤、gate 通過")


if __name__ == "__main__":
    main(sys.argv[1:])
