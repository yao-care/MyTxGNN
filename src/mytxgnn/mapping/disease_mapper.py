"""疾病映射模組 - Malaysia 版本

將馬來語（Bahasa Malaysia）和常見英文變體映射至 TxGNN 疾病本體
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 馬來語 / 英文變體 → 標準英文疾病名稱
# 目標：150-200 個疾病詞條
DISEASE_DICT = {
    # === 心血管系統 (Sistem Kardiovaskular) ===
    "tekanan darah tinggi": "hypertension",
    "hipertensi": "hypertension",
    "high blood pressure": "hypertension",
    "tekanan darah rendah": "hypotension",
    "hipotensi": "hypotension",
    "low blood pressure": "hypotension",
    "penyakit jantung": "heart disease",
    "sakit jantung": "heart disease",
    "heart disease": "heart disease",
    "serangan jantung": "myocardial infarction",
    "infarksi miokardium": "myocardial infarction",
    "heart attack": "myocardial infarction",
    "angina": "angina",
    "sakit dada": "angina",
    "chest pain": "angina",
    "aritmia": "arrhythmia",
    "denyutan jantung tidak teratur": "arrhythmia",
    "irregular heartbeat": "arrhythmia",
    "kegagalan jantung": "heart failure",
    "heart failure": "heart failure",
    "strok": "stroke",
    "angin ahmar": "stroke",
    "stroke": "stroke",
    "aterosklerosis": "atherosclerosis",
    "atherosclerosis": "atherosclerosis",
    "kolesterol tinggi": "hypercholesterolemia",
    "high cholesterol": "hypercholesterolemia",
    "hiperlipidemia": "hyperlipidemia",
    "trombosis": "thrombosis",
    "thrombosis": "thrombosis",
    "embolisme pulmonari": "pulmonary embolism",
    "pulmonary embolism": "pulmonary embolism",

    # === sistem Pernafasan (呼吸系統) ===
    "asma": "asthma",
    "asthma": "asthma",
    "lelah": "asthma",
    "bronkitis": "bronchitis",
    "bronchitis": "bronchitis",
    "radang paru-paru": "pneumonia",
    "pneumonia": "pneumonia",
    "jangkitan paru-paru": "lung infection",
    "lung infection": "lung infection",
    "tuberkulosis": "tuberculosis",
    "tb": "tuberculosis",
    "tuberculosis": "tuberculosis",
    "penyakit paru-paru obstruktif kronik": "chronic obstructive pulmonary disease",
    "copd": "chronic obstructive pulmonary disease",
    "emfisema": "emphysema",
    "emphysema": "emphysema",
    "fibrosis paru-paru": "pulmonary fibrosis",
    "pulmonary fibrosis": "pulmonary fibrosis",
    "batuk": "cough",
    "cough": "cough",
    "selesema": "common cold",
    "selsema": "common cold",
    "common cold": "common cold",
    "influenza": "influenza",
    "flu": "influenza",

    # === Sistem Pencernaan (消化系統) ===
    "gastritis": "gastritis",
    "radang perut": "gastritis",
    "ulser perut": "gastric ulcer",
    "ulser gastrik": "gastric ulcer",
    "gastric ulcer": "gastric ulcer",
    "peptic ulcer": "peptic ulcer",
    "refluks asid": "gastroesophageal reflux disease",
    "gerd": "gastroesophageal reflux disease",
    "acid reflux": "gastroesophageal reflux disease",
    "cirit-birit": "diarrhea",
    "diarrhea": "diarrhea",
    "sembelit": "constipation",
    "constipation": "constipation",
    "sindrom usus rengsa": "irritable bowel syndrome",
    "ibs": "irritable bowel syndrome",
    "irritable bowel syndrome": "irritable bowel syndrome",
    "hepatitis": "hepatitis",
    "radang hati": "hepatitis",
    "sirosis": "cirrhosis",
    "cirrhosis": "cirrhosis",
    "penyakit hati berlemak": "fatty liver disease",
    "fatty liver": "fatty liver disease",
    "batu hempedu": "gallstones",
    "gallstones": "gallstones",
    "pankreatitis": "pancreatitis",
    "pancreatitis": "pancreatitis",
    "buasir": "hemorrhoids",
    "hemorrhoids": "hemorrhoids",
    "piles": "hemorrhoids",
    "loya": "nausea",
    "nausea": "nausea",
    "muntah": "vomiting",
    "vomiting": "vomiting",

    # === Sistem Saraf (神經系統) ===
    "sakit kepala": "headache",
    "headache": "headache",
    "migrain": "migraine",
    "migraine": "migraine",
    "epilepsi": "epilepsy",
    "sawan": "epilepsy",
    "epilepsy": "epilepsy",
    "seizure": "seizure",
    "penyakit parkinson": "parkinson disease",
    "parkinson": "parkinson disease",
    "penyakit alzheimer": "alzheimer disease",
    "alzheimer": "alzheimer disease",
    "demensia": "dementia",
    "dementia": "dementia",
    "neuropati": "neuropathy",
    "neuropathy": "neuropathy",
    "sklerosis berbilang": "multiple sclerosis",
    "multiple sclerosis": "multiple sclerosis",
    "meningitis": "meningitis",
    "radang selaput otak": "meningitis",
    "vertigo": "vertigo",
    "pening": "dizziness",
    "dizziness": "dizziness",

    # === Kesihatan Mental (精神疾病) ===
    "kemurungan": "depression",
    "depresi": "depression",
    "depression": "depression",
    "kebimbangan": "anxiety disorder",
    "gangguan kecemasan": "anxiety disorder",
    "anxiety": "anxiety disorder",
    "skizofrenia": "schizophrenia",
    "schizophrenia": "schizophrenia",
    "gangguan bipolar": "bipolar disorder",
    "bipolar": "bipolar disorder",
    "insomnia": "insomnia",
    "susah tidur": "insomnia",
    "gangguan tidur": "sleep disorder",
    "sleep disorder": "sleep disorder",
    "gangguan panik": "panic disorder",
    "panic attack": "panic disorder",
    "ptsd": "post-traumatic stress disorder",
    "gangguan tekanan selepas trauma": "post-traumatic stress disorder",
    "ocd": "obsessive-compulsive disorder",
    "gangguan obsesif-kompulsif": "obsessive-compulsive disorder",

    # === Sistem Endokrin (內分泌系統) ===
    "kencing manis": "diabetes mellitus",
    "diabetes": "diabetes mellitus",
    "diabetes mellitus": "diabetes mellitus",
    "diabetis": "diabetes mellitus",
    "hipertiroidisme": "hyperthyroidism",
    "hyperthyroidism": "hyperthyroidism",
    "hipotiroidisme": "hypothyroidism",
    "hypothyroidism": "hypothyroidism",
    "goiter": "goiter",
    "kelenjar tiroid membesar": "goiter",
    "sindrom cushing": "cushing syndrome",
    "cushing syndrome": "cushing syndrome",
    "penyakit addison": "addison disease",
    "addison disease": "addison disease",
    "obesiti": "obesity",
    "kegemukan": "obesity",
    "obesity": "obesity",
    "gout": "gout",
    "asam urat": "gout",
    "osteoporosis": "osteoporosis",
    "tulang rapuh": "osteoporosis",

    # === Sistem Muskuloskeletal (肌肉骨骼系統) ===
    "artritis": "arthritis",
    "sakit sendi": "arthritis",
    "arthritis": "arthritis",
    "artritis reumatoid": "rheumatoid arthritis",
    "rheumatoid arthritis": "rheumatoid arthritis",
    "osteoartritis": "osteoarthritis",
    "osteoarthritis": "osteoarthritis",
    "sakit belakang": "back pain",
    "back pain": "back pain",
    "sakit pinggang": "lower back pain",
    "lower back pain": "lower back pain",
    "fibromialgia": "fibromyalgia",
    "fibromyalgia": "fibromyalgia",
    "kekejangan otot": "muscle spasm",
    "muscle spasm": "muscle spasm",
    "tendinitis": "tendinitis",
    "tendonitis": "tendinitis",
    "bursitis": "bursitis",
    "lupus": "systemic lupus erythematosus",
    "sle": "systemic lupus erythematosus",

    # === Penyakit Kulit (皮膚疾病) ===
    "ekzema": "eczema",
    "eczema": "eczema",
    "dermatitis": "dermatitis",
    "psoriasis": "psoriasis",
    "jerawat": "acne",
    "acne": "acne",
    "gatal-gatal": "pruritus",
    "pruritus": "pruritus",
    "itching": "pruritus",
    "urtikaria": "urticaria",
    "urticaria": "urticaria",
    "hives": "urticaria",
    "jangkitan kulat": "fungal infection",
    "fungal infection": "fungal infection",
    "kurap": "ringworm",
    "ringworm": "ringworm",
    "kudis": "scabies",
    "scabies": "scabies",
    "herpes": "herpes",
    "kayap": "herpes zoster",
    "shingles": "herpes zoster",
    "vitiligo": "vitiligo",
    "melasma": "melasma",
    "rosacea": "rosacea",

    # === Sistem Kencing (泌尿系統) ===
    "jangkitan saluran kencing": "urinary tract infection",
    "uti": "urinary tract infection",
    "urinary tract infection": "urinary tract infection",
    "batu karang": "kidney stones",
    "batu buah pinggang": "kidney stones",
    "kidney stones": "kidney stones",
    "kegagalan buah pinggang": "kidney failure",
    "renal failure": "kidney failure",
    "nefritis": "nephritis",
    "nephritis": "nephritis",
    "inkontinens": "urinary incontinence",
    "urinary incontinence": "urinary incontinence",
    "pembesaran prostat": "benign prostatic hyperplasia",
    "bph": "benign prostatic hyperplasia",
    "prostatitis": "prostatitis",
    "sistitis": "cystitis",
    "cystitis": "cystitis",

    # === Mata (眼科) ===
    "konjunktivitis": "conjunctivitis",
    "mata merah": "conjunctivitis",
    "pink eye": "conjunctivitis",
    "glaukoma": "glaucoma",
    "glaucoma": "glaucoma",
    "katarak": "cataract",
    "cataract": "cataract",
    "mata kering": "dry eye syndrome",
    "dry eye": "dry eye syndrome",
    "degenerasi makula": "macular degeneration",
    "macular degeneration": "macular degeneration",
    "retinopati diabetik": "diabetic retinopathy",
    "diabetic retinopathy": "diabetic retinopathy",

    # === Telinga, Hidung, Tekak (耳鼻喉) ===
    "jangkitan telinga": "ear infection",
    "otitis media": "otitis media",
    "ear infection": "ear infection",
    "sinusitis": "sinusitis",
    "sinus": "sinusitis",
    "faringitis": "pharyngitis",
    "sakit tekak": "pharyngitis",
    "sore throat": "pharyngitis",
    "tonsilitis": "tonsillitis",
    "radang tonsil": "tonsillitis",
    "tinnitus": "tinnitus",
    "bunyi telinga": "tinnitus",
    "kehilangan pendengaran": "hearing loss",
    "hearing loss": "hearing loss",
    "pekak": "deafness",

    # === Jangkitan (感染症) ===
    "jangkitan bakteria": "bacterial infection",
    "bacterial infection": "bacterial infection",
    "jangkitan virus": "viral infection",
    "viral infection": "viral infection",
    "demam denggi": "dengue fever",
    "dengue": "dengue fever",
    "malaria": "malaria",
    "taifoid": "typhoid fever",
    "typhoid": "typhoid fever",
    "covid-19": "covid-19",
    "coronavirus": "covid-19",
    "hiv": "hiv infection",
    "aids": "acquired immunodeficiency syndrome",
    "hepatitis b": "hepatitis b",
    "hepatitis c": "hepatitis c",
    "jangkitan helicobacter pylori": "helicobacter pylori infection",
    "h. pylori": "helicobacter pylori infection",
    "sepsis": "sepsis",
    "jangkitan darah": "sepsis",

    # === Alahan (過敏) ===
    "alahan": "allergy",
    "alergi": "allergy",
    "allergy": "allergy",
    "rinitis alahan": "allergic rhinitis",
    "allergic rhinitis": "allergic rhinitis",
    "hay fever": "allergic rhinitis",
    "alahan makanan": "food allergy",
    "food allergy": "food allergy",
    "alahan ubat": "drug allergy",
    "drug allergy": "drug allergy",
    "anafilaksis": "anaphylaxis",
    "anaphylaxis": "anaphylaxis",
    "dermatitis atopik": "atopic dermatitis",
    "atopic dermatitis": "atopic dermatitis",

    # === Kesihatan Wanita (婦科) ===
    "haid tidak teratur": "menstrual disorder",
    "menstrual disorder": "menstrual disorder",
    "senggugut": "dysmenorrhea",
    "sakit haid": "dysmenorrhea",
    "menstrual cramps": "dysmenorrhea",
    "sindrom pramenstruasi": "premenstrual syndrome",
    "pms": "premenstrual syndrome",
    "menopaus": "menopause",
    "menopause": "menopause",
    "endometriosis": "endometriosis",
    "sista ovari": "ovarian cyst",
    "ovarian cyst": "ovarian cyst",
    "fibroid rahim": "uterine fibroids",
    "uterine fibroids": "uterine fibroids",
    "jangkitan yis": "yeast infection",
    "candidiasis": "candidiasis",
    "vaginitis": "vaginitis",
    "sindrom ovari polikistik": "polycystic ovary syndrome",
    "pcos": "polycystic ovary syndrome",

    # === Kanser / Tumor (腫瘤/癌症) ===
    "kanser": "cancer",
    "barah": "cancer",
    "cancer": "cancer",
    "tumor": "tumor",
    "ketumbuhan": "tumor",
    "kanser paru-paru": "lung cancer",
    "lung cancer": "lung cancer",
    "kanser payudara": "breast cancer",
    "breast cancer": "breast cancer",
    "kanser kolon": "colorectal cancer",
    "kanser usus besar": "colorectal cancer",
    "colon cancer": "colorectal cancer",
    "kanser prostat": "prostate cancer",
    "prostate cancer": "prostate cancer",
    "kanser hati": "liver cancer",
    "liver cancer": "liver cancer",
    "kanser perut": "stomach cancer",
    "gastric cancer": "stomach cancer",
    "leukemia": "leukemia",
    "kanser darah": "leukemia",
    "limfoma": "lymphoma",
    "lymphoma": "lymphoma",
    "melanoma": "melanoma",
    "kanser kulit": "skin cancer",
    "skin cancer": "skin cancer",
    "kanser otak": "brain cancer",
    "brain tumor": "brain cancer",
    "kanser pankreas": "pancreatic cancer",
    "pancreatic cancer": "pancreatic cancer",
    "kanser tiroid": "thyroid cancer",
    "thyroid cancer": "thyroid cancer",
    "kanser serviks": "cervical cancer",
    "cervical cancer": "cervical cancer",
    "kanser ovari": "ovarian cancer",
    "ovarian cancer": "ovarian cancer",

    # === Gejala Umum (一般症狀) ===
    "demam": "fever",
    "fever": "fever",
    "sakit": "pain",
    "kesakitan": "pain",
    "pain": "pain",
    "keradangan": "inflammation",
    "radang": "inflammation",
    "inflammation": "inflammation",
    "bengkak": "swelling",
    "edema": "edema",
    "swelling": "edema",
    "keletihan": "fatigue",
    "penat": "fatigue",
    "fatigue": "fatigue",
    "lemah": "weakness",
    "weakness": "weakness",
    "anemia": "anemia",
    "kurang darah": "anemia",
    "dehidrasi": "dehydration",
    "dehydration": "dehydration",
    "hilang selera makan": "loss of appetite",
    "loss of appetite": "loss of appetite",
    "penurunan berat badan": "weight loss",
    "weight loss": "weight loss",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:
                index[kw] = (disease_id, disease_name)

    return index


def translate_term(term: str) -> List[str]:
    """將馬來語/英文變體翻譯為標準英文關鍵詞"""
    keywords = []
    term_lower = term.lower().strip()

    for local_term, en_term in DISEASE_DICT.items():
        if local_term in term_lower:
            keywords.append(en_term.upper())

    return keywords


def map_term_to_disease(
    term: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將詞彙映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為標準英文關鍵詞
    keywords = translate_term(term)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]


# Alias for backward compatibility
translate_indication = translate_term
map_indication_to_disease = map_term_to_disease


def extract_indications(indication_str: str) -> List[str]:
    """從適應症文字提取個別適應症

    Note: 馬來西亞資料沒有適應症欄位，此函數主要用於未來擴展
    """
    if not indication_str:
        return []

    text = indication_str.strip()
    # 使用句號、分號、逗號分割
    parts = re.split(r"[。；;,]", text)

    indications = []
    for part in parts:
        part = part.strip()
        if part and len(part) >= 2:
            indications.append(part)

    return indications


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "indication",
    license_field: str = "reg_no",
    brand_field: str = "product",
) -> pd.DataFrame:
    """將藥品適應症映射到 TxGNN 疾病

    Note: 馬來西亞資料沒有適應症欄位，此函數返回空 DataFrame
    """
    if indication_field not in fda_df.columns:
        # 馬來西亞資料沒有適應症欄位
        return pd.DataFrame(columns=[
            "license_id", "brand_name", "original_indication",
            "extracted_indication", "disease_id", "disease_name", "confidence"
        ])

    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []
    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        indications = extract_indications(str(indication_str))

        for ind in indications:
            matches = map_term_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": str(indication_str)[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": str(indication_str)[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    if len(mapping_df) == 0:
        return {
            "total_indications": 0,
            "mapped_indications": 0,
            "mapping_rate": 0,
            "unique_indications": 0,
            "unique_diseases": 0,
        }

    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }


def get_disease_dict_stats() -> dict:
    """計算 DISEASE_DICT 統計"""
    unique_english = set(DISEASE_DICT.values())

    # 按類別統計
    categories = {
        "cardiovascular": ["hypertension", "heart", "stroke", "arrhythmia", "thrombosis"],
        "respiratory": ["asthma", "bronchitis", "pneumonia", "tuberculosis", "copd"],
        "digestive": ["gastritis", "ulcer", "hepatitis", "cirrhosis", "diarrhea"],
        "neurological": ["headache", "migraine", "epilepsy", "parkinson", "alzheimer"],
        "mental": ["depression", "anxiety", "schizophrenia", "bipolar", "insomnia"],
        "endocrine": ["diabetes", "thyroid", "obesity", "gout"],
        "musculoskeletal": ["arthritis", "osteoporosis", "back pain", "fibromyalgia"],
        "dermatological": ["eczema", "psoriasis", "acne", "urticaria"],
        "urological": ["urinary", "kidney", "prostate", "cystitis"],
        "ophthalmological": ["glaucoma", "cataract", "conjunctivitis"],
        "ent": ["otitis", "sinusitis", "pharyngitis", "tinnitus"],
        "infectious": ["infection", "dengue", "malaria", "typhoid", "covid"],
        "allergic": ["allergy", "allergic", "anaphylaxis"],
        "gynecological": ["menstrual", "menopause", "endometriosis", "ovarian"],
        "oncological": ["cancer", "tumor", "leukemia", "lymphoma", "melanoma"],
    }

    return {
        "total_entries": len(DISEASE_DICT),
        "unique_english_terms": len(unique_english),
        "categories": len(categories),
    }
