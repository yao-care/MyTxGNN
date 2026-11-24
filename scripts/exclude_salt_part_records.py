"""證據包排除「本藥只是另一個藥的鹽類／共晶／溶劑合物／配位基部分」的 NPRA 登記（2026-11-24 第三輪，用戶決定；全程不用 AI）。

背景：原收集器（src/mytxgnn/collectors/npra.py 的 _search_drugs）依頁名子字串比對 product／active_ingredient／generic_name，
所以 arginine 頁收進 COVERSYL 5MG（PERINDOPRIL ARGININE；成分是 perindopril，arginine 只是鹽類），程式表還列成 Bahan tunggal；
同類還有 potassium_chloride 收進 Glucosamine Sulfate Potassium Chloride（成分是 glucosamine sulfate，KCl 是複鹽的穩定劑）等。
這些登記的有效成分不是本藥，不屬於本藥的市場事實。

規則（下表 SALT_PART，每筆附依據；只列這幾類，不放寬到一般的子字串誤收）：
- 某登記 active_ingredient 的每個成分（「名稱[劑量]」）裡，含本藥名稱（整字）的成分都符合表上的「另一個藥」寫法，
  而且沒有任何一個成分本身就是本藥（同 scripts/rebuild_licenses_by_ingredient.py 的成分主體比法，或去掉鹽類／水合物／藥典字樣後只剩本藥）
  → 從 npra.records 移到 npra.excluded_records（原紀錄照存，加 excluded_reason、excluded_basis、excluded＝日期），不刪資料。
- 同一個證據包又在 records 裡出現同一號碼（例如之後重新收集）時，重跑會再排除；排除過的號碼不會被
  rebuild_licenses_by_ingredient.py 補回（它跳過 excluded_records 的號碼）。
- 只動證據包；狀態列、張數列、程式表、快照由之後的 license_refresh／build_license_snapshot 依新證據包重算。
2026-11-24 同日第三輪續做（用戶決定「逐站修對照並重算」）：同一支程式另處理「本藥名稱只是另一個藥名的一部分」的子字串誤收
（OTHER 表，每筆附依據；例 glycine 收進 Glycine max（大豆）、ofloxacin 收進 ciprofloxacin／levofloxacin／marbofloxacin、citalopram 收進 escitalopram、
omeprazole 收進 esomeprazole、desonide 收進 budesonide）：登記的 active_ingredient／generic_name／product 正規化後，拿掉表上「另一個藥」的寫法，
若已找不到本藥名稱（原收集器比的子字串），而且表上寫法至少出現一次、沒有任何成分本身就是本藥 → 排除（excluded_reason 註明）。
另 RECORD_MISMATCH：NPRA 某欄位錯植的個別登記（附理由）。本藥的鹽類、酯類、拼法變體（lignocaine、frusemide、aciclovir…）不在表上，照收。
每週排程（.github/workflows/license-refresh.yml）在 merge_duplicate_bundles.py 之後、license_refresh 之前跑；重新收集證據包之後也要再跑。
用法（repo 根目錄）：python3 scripts/exclude_salt_part_records.py [--dry-run] [--report out.tsv]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
sys.path.insert(0, str(ROOT / "scripts"))
import rebuild_licenses_by_ingredient as rb  # noqa: E402

TODAY = "2026-11-24"
# 證據包名 → [(本藥名稱在成分裡的寫法, 另一個藥的成分寫法（正規化後的 regex）, 依據)]
SALT_PART = {
    "arginine": [("arginine", r"\bperindopril arginine\b",
                  "perindopril arginine 是 perindopril 的 L-arginine 鹽（ACE 抑制劑 COVERSYL／Triveram 等），有效成分是 perindopril")],
    "potassium_chloride": [("potassium chloride", r"\bglucosamine (sulfate|sulphate) potassium chloride\b",
                            "glucosamine sulfate potassium chloride 是 glucosamine sulfate 以氯化鉀穩定的複鹽，有效成分是 glucosamine")],
    "sodium_chloride": [("sodium chloride", r"\bglucosamine (sulfate|sulphate) sodium chloride\b",
                         "glucosamine sulfate sodium chloride 是 glucosamine sulfate 以氯化鈉穩定的複鹽，有效成分是 glucosamine")],
    "potassium_acetate": [("potassium acetate", r"\bhydroxymatairesinol potassium acetate\b",
                           "7-hydroxymatairesinol potassium acetate 是木酚素 7-hydroxymatairesinol 的鉀鹽／醋酸鉀錯合物，有效成分是 7-hydroxymatairesinol")],
    "mannitol": [("mannitol", r"\bdapagliflozin mannitol\b",
                  "dapagliflozin mannitol 是 dapagliflozin 與甘露醇的共晶（Dapamac），有效成分是 dapagliflozin")],
    "propylene_glycol": [("propylene glycol", r"\bdasatinib (s )?propylene glycol\b",
                          "dasatinib (S)-propylene glycol 是 dasatinib 的丙二醇溶劑合物，有效成分是 dasatinib")],
    "polyethylene_glycol": [("polyethylene glycol", r"\bmethoxy polyethylene glycol epoetin beta\b",
                             "methoxy polyethylene glycol-epoetin beta 是 PEG 化的 epoetin beta（MIRCERA），有效成分是 epoetin beta")],
    "sodium_phosphate": [("sodium phosphate", r"\b(betamethasone|dexamethasone|prednisolone|riboflavin( 5)?) (di)?sodium phosphate\b",
                          "betamethasone／dexamethasone／prednisolone／riboflavin sodium phosphate 是該藥的磷酸鈉酯鹽，有效成分是該藥")],
    "zinc": [("zinc", r"\bbacitracin zinc\b", "bacitracin zinc 是 bacitracin 的鋅鹽（外用抗生素），有效成分是 bacitracin")],
    "methionine": [("methionine", r"^(zinc methionine|methionine bound zinc complex)\b",
                    "zinc methionine 是鋅的甲硫胺酸螯合物（鋅補充劑），有效成分是鋅；甲硫胺酸只是配位基")],
}
# 證據包名 → [(另一個藥的寫法（正規化後的 regex）, 依據)]：拿掉這些寫法後找不到本藥名稱就排除（見檔頭）
OTHER = {
    "acetic_acid": [(r"aminoacetic acid", "aminoacetic acid 是 glycine（胺基乙酸），不是醋酸")],
    "alanine": [(r"\w*phenylalanine", "phenylalanine／α-ketophenylalanine 是另一個胺基酸（或其酮酸類似物），不是 alanine")],
    "phenylalanine": [(r"keto ?phenylalanine", "α-ketophenylalanine calcium 是 phenylalanine 的酮酸類似物（Ketosteril），不是 phenylalanine")],
    "isoleucine": [(r"keto ?isoleucine", "α-ketoisoleucine calcium 是 isoleucine 的酮酸類似物（Ketosteril），不是 isoleucine")],
    "valine": [(r"keto ?valine", "α-ketovaline calcium 是 valine 的酮酸類似物（Ketosteril），不是 valine")],
    "aprepitant": [(r"fosaprepitant", "fosaprepitant 是另一個 INN（aprepitant 的前驅藥，注射劑）")],
    "atracurium_besylate": [(r"cisatracurium", "cisatracurium 是另一個 INN（atracurium 的單一異構物）")],
    "benzoic_acid": [(r"para ?amino ?benzoic acid|aminobenzoic acid|\bpaba\b", "para-aminobenzoic acid（PABA）是另一個化合物"),
                     (r"2 hydroxybenzoic acid", "2-hydroxybenzoic acid 是 salicylic acid")],
    "camphor": [(r"antrodia camphorat\w*|antrodia cinnamomea", "Antrodia camphorata／cinnamomea 是牛樟芝（真菌），不是樟腦"),
                (r"(cortex |folium )?cinnamomum camphora( oil)?", "Cinnamomum camphora 是樟樹（植物）萃取物，不是樟腦成分"),
                (r"borneo camphor", "Borneo camphor 是龍腦（borneol），不是樟腦"),
                (r"camphor monobromide", "monobromated camphor 是樟腦的溴化衍生物，另一個化合物")],
    "citalopram": [(r"escitalopram", "escitalopram 是另一個 INN（citalopram 的 S-鏡像異構物）")],
    "daunorubicin": [(r"idarubicin( hcl| hydrochloride)?( 4)? ?demethoxy ?daunorubicin|demethoxy ?daunorubicin|idarubicin", "idarubicin（4-demethoxydaunorubicin）是另一個 INN")],
    "desonide": [(r"budesonide", "budesonide 是另一個糖皮質素（名稱含 desonide 字串）")],
    "epinephrine": [(r"norepinephrine", "norepinephrine（noradrenaline）是另一個藥")],
    "ergometrine": [(r"methylergometrine", "methylergometrine 是另一個 INN")],
    "ethanol": [(r"phenoxyethanol|\w*ethanolamine", "phenoxyethanol（防腐劑）、triethanolamine 等是另一個化合物，不是乙醇")],
    "filgrastim": [(r"pegfilgrastim", "pegfilgrastim 是另一個 INN（PEG 化 filgrastim）")],
    "flurbiprofen": [(r"esflurbiprofen", "esflurbiprofen 是另一個 INN（flurbiprofen 的 S-鏡像異構物）")],
    "folic_acid": [(r"\d* ?methyl ?tetrahydrofolic acid|tetrahydrofolic acid", "5-methyltetrahydrofolic acid（L-methylfolate）是另一個化合物")],
    "glycerin": [(r"nitroglycerin|glyceryl trinitrate", "nitroglycerin（glyceryl trinitrate）是另一個藥")],
    "nitroglycerin": [],
    "glycine": [(r"(semen )?glycine (hispida )?(max|soja)\w*", "Glycine max／Glycine soja 是大豆的學名（植物），不是胺基酸 glycine"),
                (r"trimethylglycine", "trimethylglycine 是 betaine，另一個化合物")],
    "guaiacol": [(r"glyceryl guaiacolate|guaiacol glyceryl ether|guaiacol glycerol ether", "glyceryl guaiacolate 是 guaifenesin，另一個藥")],
    "iron": [(r"spironolactone", "spironolactone 名稱含「iron」字串，不是鐵劑")],
    "ketoprofen": [(r"dexketoprofen", "dexketoprofen 是另一個 INN（ketoprofen 的 S-鏡像異構物）")],
    "lansoprazole": [(r"dexlansoprazole", "dexlansoprazole 是另一個 INN（lansoprazole 的 R-鏡像異構物）")],
    "ofloxacin": [(r"\b(?!ofloxacin\b)\w+ofloxacin\w*", "ciprofloxacin、levofloxacin、enrofloxacin、marbofloxacin、danofloxacin 等是另一個 fluoroquinolone（名稱含 ofloxacin 字串）")],
    "omeprazole": [(r"esomeprazole", "esomeprazole 是另一個 INN（omeprazole 的 S-鏡像異構物）")],
    "phenol": [(r"mycophenol\w*", "mycophenolate／mycophenolic acid 是另一個藥"),
               (r"\b(?!phenols?\b)\w+phenols?\b", "propofol（2,6-diisopropylphenol）、植物多酚等是另一個化合物，不是酚（phenol）")],
    "prednisolone": [(r"methylprednisolone", "methylprednisolone 是另一個 INN")],
    "prednisolone_acetate": [(r"methylprednisolone", "methylprednisolone 是另一個 INN")],
    "progesterone": [(r"medroxyprogesterone|hydroxyprogesterone", "medroxyprogesterone／hydroxyprogesterone 是另一個黃體素類藥")],
    "resorcinol": [(r"hexylresorcinol", "hexylresorcinol 是另一個藥（喉片）")],
    "salicylic_acid": [(r"acetyl ?salicylic acid", "acetylsalicylic acid 是 aspirin，另一個藥"),
                       (r"\d* ?amino ?salicylic acid", "5-aminosalicylic acid 是 mesalazine，另一個藥")],
    "serine": [(r"cycloserine", "cycloserine 是抗結核藥，另一個藥"),
               (r"phosphatidyl ?serine", "phosphatidylserine 是磷脂，不是胺基酸 serine")],
    "sodium_citrate": [(r"ferric sodium citrate", "ferric sodium citrate 是鐵劑，另一個化合物")],
    "streptomycin": [(r"dihydrostreptomycin", "dihydrostreptomycin 是另一個 INN（獸用）")],
    "trastuzumab": [(r"trastuzumab (deruxtecan|emtansine)", "trastuzumab deruxtecan（Enhertu）／emtansine（Kadcyla）是另一個 INN（抗體藥物複合體）")],
    "tretinoin": [(r"isotretinoin", "isotretinoin 是另一個 INN")],
    "turoctocog_alfa": [(r"turoctocog alfa pegol", "turoctocog alfa pegol（Esperoct）是另一個 INN")],
    "uracil": [(r"\b(?!uracil\b)\w+uracil\w*", "fluorouracil、propylthiouracil 等是另一個藥（名稱含 uracil 字串）")],
    "vitamin_a": [(r"pro ?vitamin a\b", "provitamin A 是 beta-carotene，不是維生素 A")],
    "methionine": [(r"\w*selenomethionine|selenium methionine", "selenomethionine 是硒補充劑（甲硫胺酸的硒類似物），另一個化合物"),
                   (r"s adenosyl l? ?methionine|ademetionine", "S-adenosyl-L-methionine（ademetionine，SAMe）是另一個 INN"),
                   (r"\w*hydroxy ?methionine", "α-hydroxymethionine calcium 是甲硫胺酸的羥基類似物（Ketosteril），另一個化合物"),
                   (r"zinc (mono)?methionine|methionine bound zinc", "zinc methionine 是鋅的甲硫胺酸螯合物（鋅補充劑）")],
    "acyclovir": [(r"valaciclovir|valacyclovir", "valaciclovir 是另一個 INN（aciclovir 的前驅藥）")],
}
# 個別登記：NPRA 欄位錯植（號碼 → (不屬於的證據包, 依據)）
RECORD_MISMATCH = {
    "MAL09102936AZ": (("budesonide", "desonide"), "RESICALM Tablets 1mg 的成分是 RISPERIDONE；NPRA generic_name 欄錯植「Budesonide 100 mcg/dose Nasal Spray」"),
}
NOISE = re.compile(r"\b(" + rb.SALT + r"|ph eur|pheur|eur|ph|usp|bp|ip|jp|ep|b p|u s p|heptahydrate|\d+h2o|\d+)\b")


def rid(r):
    return str(r.get("reg_no") or "").strip()


def is_self(page, comps):
    """有成分本身就是本藥（主體比法同 rebuild_licenses_by_ingredient；或去掉鹽類／水合物／藥典字樣後只剩本藥名稱）"""
    terms, salt_named = rb.terms_for(page)
    full = rb.norm(page.replace("_", " "))
    for c in comps:
        if rb.base(c, keep_salt=salt_named) in terms:
            return True
        if re.search(r"\b" + re.escape(full) + r"\b", c):
            rest = " ".join(NOISE.sub(" ", re.sub(r"\b" + re.escape(full) + r"\b", " ", c)).split())
            if not rest:
                return True
    return False


def salt_part(page, r):
    """(依據, 符合的成分) 或 None"""
    comps = rb.components(r.get("active_ingredient"))
    if not comps or is_self(page, comps):
        return None
    for name, rx, basis in SALT_PART.get(page, []):
        hits = [c for c in comps if re.search(r"\b" + re.escape(name) + r"\b", c)]
        if hits and all(re.search(rx, c) for c in hits):
            return basis, hits
    return None


def _text(r):
    return rb.norm(" ".join(str(r.get(k) or "") for k in ("active_ingredient", "generic_name", "product")))


def other_drug(page, r):
    """(依據, 符合的寫法) 或 None：拿掉 OTHER 表的寫法後找不到本藥名稱（原收集器的子字串）"""
    for no, (pages, why) in RECORD_MISMATCH.items():
        if rid(r) == no and page in pages:
            return why, [no]
    pats = OTHER.get(page) or []
    if not pats:
        return None
    comps = rb.components(r.get("active_ingredient"))
    if is_self(page, comps):
        return None
    txt, hit, why = _text(r), [], []
    for rx, basis in pats:
        m = [x.group(0) for x in re.finditer(rx, txt)]
        if m:
            hit += m
            why.append(basis)
            txt = re.sub(rx, " ", txt)
    if not hit:
        return None
    full = rb.norm(page.replace("_", " "))
    terms, _ = rb.terms_for(page)
    if full in txt or any(re.search(r"\b" + re.escape(x) + r"\b", txt) for x in terms):
        return None
    return "；".join(dict.fromkeys(why)), list(dict.fromkeys(hit))


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    out, n = [], 0
    for page in sorted(set(SALT_PART) | set(OTHER) | {p for ps, _ in RECORD_MISMATCH.values() for p in ps}):
        f = BUNDLES / page / "drug_bundle.json"
        if not f.exists():
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("npra") or {}
        recs = reg.get("records") or []
        exc = reg.get("excluded_records") or []
        have_exc = {rid(x) for x in exc}
        keep, move = [], []
        for r in recs:
            hit = salt_part(page, r)
            kind = "本藥只是另一個藥的鹽類／共晶／溶劑合物／配位基部分（成分："
            if not hit:
                hit = other_drug(page, r)
                kind = "本藥名稱只是另一個藥名的一部分，或登記欄位錯植（"
            if hit:
                move.append(r)
                out.append(f"{page}\t{rid(r)}\t{r.get('product')}\t{'; '.join(hit[1])}\t{hit[0]}")
                if rid(r) not in have_exc:
                    exc.append(dict(r, excluded_reason=kind + "; ".join(hit[1]) + "）",
                                    excluded_basis=hit[0], excluded=TODAY))
                    have_exc.add(rid(r))
            else:
                keep.append(r)
        if move:
            n += len(move)
            print(f"{page}\t{len(recs)} → {len(keep)}\t排除 {len(move)}")
            if not dry:
                reg.update(records=keep, excluded_records=exc, found=bool(keep))
                b["npra"] = reg
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\treg_no\tproduct\tcomponents\tbasis\n" + "\n".join(out) + "\n", encoding="utf-8")
    print(f"共排除 {n} 筆{'（試跑）' if dry else ''}")


if __name__ == "__main__":
    main(sys.argv[1:])
