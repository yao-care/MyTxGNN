#!/usr/bin/env python3
"""DDI／GtoPdb 資料來源數字：.github/ddi-versions.json 的 site_data → docs/_data/ddi_sources.json（2026-11-05）。

頁面上 DDInter 與 Guide to PHARMACOLOGY（GtoPdb）的版本、筆數、Ligand 數一律用 Liquid 讀
site.data.ddi_sources（數字用 display 裡的千分位字串），不要手寫。site_data 是本站 Release 資料檔實算的值
（重算方式見 site_data.note）；改了 site_data 就跑這支，重寫資料檔與 Liquid 進不去的 front matter 位置（SPOTS）。

用法：python3 scripts/sync_ddi_sources.py          # 重寫
      python3 scripts/sync_ddi_sources.py --check  # 只檢查，不一致就非零（check_seo_docs.py 也會呼叫 problems()）
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSIONS = ROOT / ".github" / "ddi-versions.json"
OUT = ROOT / "docs" / "_data" / "ddi_sources.json"

KEYS = ["ddinter_rows", "ddinter_unique_pairs", "ddinter_drug_names",
        "gtopdb_version", "gtopdb_published", "gtopdb_drug_target_records", "gtopdb_ligands", "gtopdb_release"]

# Liquid 進不去的地方（front matter）：(檔案, 正規式, site_data 欄位)；正規式第 1 組是要換掉的數字
SPOTS = [
]


def expected():
    sd = json.loads(VERSIONS.read_text(encoding="utf-8")).get("site_data", {})
    missing = [k for k in KEYS if k not in sd]
    if missing:
        raise SystemExit(f"{VERSIONS.relative_to(ROOT)} 的 site_data 缺 {missing}")
    data = {"_note": "由 scripts/sync_ddi_sources.py 依 .github/ddi-versions.json 的 site_data 產生，勿手改。"}
    data.update({k: sd[k] for k in KEYS})
    data["display"] = {k: f"{sd[k]:,}" for k in KEYS if isinstance(sd[k], int)}
    data["display"]["gtopdb_published_month"] = sd["gtopdb_published"][:7]
    return data


def render(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


_SKIP_DIRS = {"_site", "vendor", "node_modules", ".jekyll-cache", "_drugs", "_news", "data", "fhir", ".bundle"}
_CTX = re.compile(r"DDInter(?!act)|\bDDI\b|GtoPdb|PHARMACOLOGY|[Ll]igand")
_GTOP_CTX = re.compile(r"GtoPdb|PHARMACOLOGY|[Ll]igand")
_VER = re.compile(r"(?<![\d.])(20\d\d\.\d+(?:\.\d+)?)(?![\d.]?\d)")
_ANYNUM = re.compile(r"(?<![\d,.])(\d{1,3}(?:,\d{3})+)(?![\d,]?\d)")


def hardcode_problems(data):
    """頁面正文（front matter 以外）在提到 DDInter／DDI／GtoPdb 的行（含後 3 行，涵蓋 HTML 表格分行的 <td>）
    不得手寫 site_data 的數字；提到 GtoPdb 的行（含後 3 行）不得手寫任何千分位數字或 GtoPdb 版本號（YYYY.N）。
    要用 {{ site.data.ddi_sources.display.<欄位> }}、{{ site.data.ddi_sources.gtopdb_version }}。"""
    nums = {data["display"][k] for k in data["display"] if k != "gtopdb_published_month"}
    num_re = re.compile(r"(?<![\d,.])(" + "|".join(re.escape(n) for n in sorted(nums, key=len, reverse=True)) + r")(?![\d,]?\d)")
    out = []
    docs = ROOT / "docs"
    for f in sorted(docs.rglob("*")):
        if f.suffix not in (".md", ".html") or not f.is_file() or set(f.relative_to(docs).parts[:-1]) & _SKIP_DIRS:
            continue
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        start = 0
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    start = i + 1
                    break
        bad = set()
        for i in range(start, len(lines)):
            if not _CTX.search(lines[i]):
                continue
            gtop = bool(_GTOP_CTX.search(lines[i]))
            for j in range(i, min(i + 4, len(lines))):
                for m in num_re.finditer(lines[j]):
                    bad.add((j + 1, m.group(1)))
                if gtop:
                    for m in list(_VER.finditer(lines[j])) + list(_ANYNUM.finditer(lines[j])):
                        bad.add((j + 1, m.group(1)))
        out += [f"docs/{f.relative_to(docs)}:{n} 手寫了 {v}（改用 site.data.ddi_sources 的 Liquid）" for n, v in sorted(bad)]
    return out


def problems():
    out = []
    data = expected()
    out += hardcode_problems(data)
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != render(data):
        out.append(f"{OUT.relative_to(ROOT)} 與 .github/ddi-versions.json 的 site_data 不一致（跑 scripts/sync_ddi_sources.py）")
    for rel, pattern, key in SPOTS:
        m = re.search(pattern, (ROOT / rel).read_text(encoding="utf-8"))
        want = data["display"].get(key, str(data[key]))
        if not m:
            out.append(f"{rel}：找不到 {key} 的位置（{pattern}），改了文字就要一起改 scripts/sync_ddi_sources.py 的 SPOTS")
        elif m.group(1) != want:
            out.append(f"{rel}：{key} 寫 {m.group(1)}，site_data 是 {want}（跑 scripts/sync_ddi_sources.py）")
    return out


def main():
    if "--check" in sys.argv:
        p = problems()
        for e in p:
            print("✗", e)
        sys.exit(1 if p else 0)
    data = expected()
    OUT.write_text(render(data), encoding="utf-8")
    print(f"✓ {OUT.relative_to(ROOT)}")
    for rel, pattern, key in SPOTS:
        path = ROOT / rel
        raw = path.read_bytes().decode("utf-8")
        want = data["display"].get(key, str(data[key]))
        m = re.search(pattern, raw)
        if not m:
            raise SystemExit(f"{rel}：找不到 {key} 的位置（{pattern}）")
        if m.group(1) != want:
            raw = raw[:m.start(1)] + want + raw[m.end(1):]
            path.write_bytes(raw.encode("utf-8"))
            print(f"✓ {rel}：{key} → {want}")
    p = problems()
    if p:
        raise SystemExit("\n".join(p))


if __name__ == "__main__":
    main()
