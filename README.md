# MyTxGNN - Malaysia: Penggunaan Semula Ubat

> 本專案由 **藥提醒科技有限公司**（[yao.care](https://www.yao.care)）開發與維運。
> MyTxGNN 站台：<https://mytxgnn.yao.care/>｜產品總覽：<https://www.yao.care/medical/txgnn/>

[![Website](https://img.shields.io/badge/Website-mytxgnn.yao.care-blue)](https://mytxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ramalan penggunaan semula ubat untuk ubat yang diluluskan NPRA (Malaysia) menggunakan model TxGNN.

## Penafian

- Keputusan projek ini hanya untuk tujuan penyelidikan dan tidak merupakan nasihat perubatan.
- Calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum penggunaan.

## Gambaran keseluruhan projek

### Statistik laporan

| Item | Bilangan |
|------|------|
| **Laporan ubat** | 606 |
| **Jumlah ramalan** | 18,287,982 |
| **Ubat unik** | 1,000 |
| **Petunjuk unik** | 17,041 |
| **Data DDI** | 302,516 |
| **Data DFI** | 857 |
| **Data DHI** | 35 |
| **Data DDSI** | 8,359 |
| **Sumber FHIR** | 508 MK / 3,832 CUD |

### Taburan tahap bukti

| Tahap bukti | Bilangan laporan | Penerangan |
|---------|-------|------|
| **L1** | 0 | Pelbagai RCT Fasa 3 |
| **L2** | 0 | RCT tunggal atau pelbagai Fasa 2 |
| **L3** | 0 | Kajian pemerhatian |
| **L4** | 0 | Kajian praklinikal / mekanistik |
| **L5** | 508 | Ramalan pengkomputeran sahaja |

### Mengikut sumber

| Sumber | Ramalan |
|------|------|
| DL | 18,284,150 |
| KG + DL | 3,301 |
| KG | 531 |

### Mengikut keyakinan

| Keyakinan | Ramalan |
|------|------|
| very_high | 2,433 |
| high | 999,893 |
| medium | 2,378,077 |
| low | 14,907,579 |

---

## Kaedah ramalan

| Kaedah | Kelajuan | Ketepatan | Keperluan |
|------|------|--------|----------|
| Graf pengetahuan | Cepat (saat) | Lebih rendah | Tiada keperluan khas |
| Pembelajaran mendalam | Perlahan (jam) | Lebih tinggi | Conda + PyTorch + DGL |

### Kaedah graf pengetahuan

```bash
uv run python scripts/run_kg_prediction.py
```

| Metrik | Nilai |
|------|------|
| NPRA Jumlah ubat | 13,554 |
| Dipetakan ke DrugBank | 9,326 (68.8%) |
| Calon penggunaan semula | 3,832 |

### Kaedah pembelajaran mendalam

```bash
conda activate txgnn
PYTHONPATH=src python -m mytxgnn.predict.txgnn_model
```

| Metrik | Nilai |
|------|------|
| Jumlah ramalan DL | 1,981,986 |
| Ubat unik | 1,000 |
| Petunjuk unik | 17,041 |

### Tafsiran skor

Skor TxGNN mewakili keyakinan model dalam pasangan ubat-penyakit, julat 0 hingga 1.

| Ambang | Makna |
|-----|------|
| >= 0.9 | Keyakinan sangat tinggi |
| >= 0.7 | Keyakinan tinggi |
| >= 0.5 | Keyakinan sederhana |

#### Taburan skor

| Ambang | Maksud |
|-----|------|
| ≥ 0.9999 | Keyakinan sangat tinggi, ramalan paling yakin model |
| ≥ 0.99 | Keyakinan sangat tinggi, patut diutamakan untuk pengesahan |
| ≥ 0.9 | Keyakinan tinggi |
| ≥ 0.5 | Keyakinan sederhana (sempadan keputusan sigmoid) |

#### Definisi tahap bukti

| Tahap | Definisi | Kepentingan klinikal |
|-----|------|---------|
| L1 | RCT fasa 3 atau ulasan sistematik | Boleh menyokong penggunaan klinikal |
| L2 | RCT fasa 2 | Boleh dipertimbangkan untuk penggunaan |
| L3 | Fasa 1 atau kajian pemerhatian | Memerlukan penilaian lanjut |
| L4 | Laporan kes atau penyelidikan praklinikal | Belum disyorkan |
| L5 | Ramalan pengkomputeran sahaja, tiada bukti klinikal | Memerlukan penyelidikan lanjut |

#### Peringatan penting

1. **Skor tinggi tidak menjamin keberkesanan klinikal: skor TxGNN adalah ramalan berasaskan graf pengetahuan yang memerlukan pengesahan ujian klinikal.**
2. **Skor rendah tidak bermakna tidak berkesan: model mungkin tidak mempelajari perkaitan tertentu.**
3. **Disyorkan untuk digunakan dengan saluran paip pengesahan: gunakan alat projek ini untuk menyemak ujian klinikal, kesusasteraan dan bukti lain.**

### Saluran paip pengesahan

```mermaid
flowchart TD
    A["Keputusan ramalan TxGNN"] --> B
    subgraph B["Step 1: DrugBundle Collector"]
        B1["Tahap ubat: NPRA, DDI, DrugBank"]
        B2["Tahap petunjuk: ClinicalTrials, PubMed, ICTRP"]
    end
    B --> |"drug_bundle.json"| C
    subgraph C["Step 2: Evidence Pack Generator"]
        C1["Pemindahan data programatik (100%)"]
        C2["+ LLM Analisis (L1-L5)"]
    end
    C --> |"drug_evidence_pack.json/md"| D
    subgraph D["Step 3: Notes Writer"]
        D1["drug_pharmacist_notes.md"]
        D2["drug_sponsor_notes.md"]
    end
```

---

## Mula pantas

### Langkah 1: Muat turun data

| Fail | Muat turun |
|------|------|
| NPRA Data | [Sumber data](https://storage.data.gov.my/healthcare/pharmaceutical_products.csv) |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) |

### Langkah 2: Pasang kebergantungan

```bash
uv sync
```

### Langkah 3: Proses data ubat

```bash
uv run python scripts/process_fda_data.py
```

### Langkah 4: Sediakan data perbendaharaan kata

```bash
uv run python scripts/prepare_external_data.py
```

### Langkah 5: Jalankan ramalan graf pengetahuan

```bash
uv run python scripts/run_kg_prediction.py
```

### Langkah 6: Sediakan persekitaran pembelajaran mendalam

```bash
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb
```

### Langkah 7: Jalankan ramalan pembelajaran mendalam

```bash
conda activate txgnn
PYTHONPATH=src python -m mytxgnn.predict.txgnn_model
```

---

## Sumber

### TxGNN Teras

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine, 2024
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org)

### Sumber data

| Kategori | Data | Sumber | Nota |
|------|------|------|------|
| **Data ubat** | NPRA | [NPRA](https://storage.data.gov.my/healthcare/pharmaceutical_products.csv) | Malaysia |
| **Graf pengetahuan** | TxGNN KG | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 diseases, 7,957 drugs |
| **Pangkalan data ubat** | DrugBank | [DrugBank](https://go.drugbank.com/) | Pemetaan ramuan ubat |
| **Interaksi ubat** | DDInter 2.0 | [DDInter](https://ddinter2.scbdd.com/) | Pasangan DDI |
| **Interaksi ubat** | Guide to PHARMACOLOGY | [IUPHAR/BPS](https://www.guidetopharmacology.org/) | Interaksi ubat yang diluluskan |
| **Percubaan klinikal** | ClinicalTrials.gov | [CT.gov API v2](https://clinicaltrials.gov/data-api/api) | Pendaftaran percubaan klinikal |
| **Percubaan klinikal** | WHO ICTRP | [ICTRP API](https://apps.who.int/trialsearch/api/v1/search) | Platform percubaan klinikal antarabangsa |
| **Sastera** | PubMed | [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) | Carian sastera perubatan |
| **Pemetaan nama** | RxNorm | [RxNav API](https://rxnav.nlm.nih.gov/REST) | Penyeragaman nama ubat |
| **Pemetaan nama** | PubChem | [PUG-REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Sinonim bahan kimia |
| **Pemetaan nama** | ChEMBL | [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data) | Pangkalan data bioaktiviti |
| **Piawaian** | FHIR R4 | [HL7 FHIR](http://hl7.org/fhir/) | MedicationKnowledge, ClinicalUseDefinition |
| **Piawaian** | SMART on FHIR | [SMART Health IT](https://smarthealthit.org/) | Integrasi EHR, OAuth 2.0 + PKCE |

### Muat turun model

| Fail | Muat turun | Nota |
|------|------|------|
| Model pra-latih | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | model_ckpt.zip |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | Data nod |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | Data graf pengetahuan |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | Data tepi (DL) |

## Pengenalan projek

### Struktur direktori

```
MyTxGNN/
├── README.md
├── CLAUDE.md
├── pyproject.toml
│
├── config/
│   └── fields.yaml
│
├── data/
│   ├── kg.csv
│   ├── node.csv
│   ├── edges.csv
│   ├── raw/
│   ├── external/
│   ├── processed/
│   │   ├── drug_mapping.csv
│   │   ├── repurposing_candidates.csv
│   │   ├── txgnn_dl_predictions.csv.gz
│   │   └── integration_stats.json
│   ├── bundles/
│   └── collected/
│
├── src/mytxgnn/
│   ├── data/
│   │   └── loader.py
│   ├── mapping/
│   │   ├── normalizer.py
│   │   ├── drugbank_mapper.py
│   │   └── disease_mapper.py
│   ├── predict/
│   │   ├── repurposing.py
│   │   └── txgnn_model.py
│   ├── collectors/
│   └── paths.py
│
├── scripts/
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   └── integrate_predictions.py
│
├── docs/
│   ├── _drugs/
│   ├── fhir/
│   │   ├── MedicationKnowledge/
│   │   └── ClinicalUseDefinition/
│   └── smart/
│
├── model_ckpt/
└── tests/
```

**Petunjuk**: 🔵 Pembangunan projek | 🟢 Data tempatan | 🟡 Data TxGNN | 🟠 Saluran paip pengesahan

### Aliran data

```mermaid
flowchart TD
    FDA["NPRA Data"] --> proc["process_fda_data.py"]
    TxGNN["TxGNN Data"] --> prep["prepare_external_data.py"]

    proc --> json["my_fda_drugs.json"]
    prep --> ext["data/external/"]

    json --> norm["normalizer.py"]
    ext --> norm

    norm --> drug_map["drug_mapping.csv"]
    drug_map --> ind_map["indication_mapping.csv"]

    ind_map --> KG["Graf pengetahuan"]
    ind_map --> DL["Pembelajaran mendalam"]

    KG --> kg_out["repurposing_candidates.csv"]
    DL --> dl_out["txgnn_dl_predictions.csv"]
```

---

## Petikan

Jika anda menggunakan set data atau perisian ini, sila petik:

```bibtex
@software{mytxgnn2026,
  author       = {Yao.Care},
  title        = {MyTxGNN: Drug Repurposing Validation Reports for Malaysia NPRA Drugs},
  year         = 2026,
  publisher    = {GitHub},
  url          = {https://github.com/yao-care/MyTxGNN}
}
```

Petik juga artikel asal TxGNN:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

<!-- txgnn-ops:start -->
## 維運：資料還原與許可證更新

### 完整還原

git 只放程式碼與網站頁面；許可證原始資料、證據包、藥師報告原稿、預測結果放在本 repo 的 Release。

```bash
git clone https://github.com/yao-care/mytxgnn.git && cd mytxgnn
uv sync                                  # Python 相依套件
bash scripts/restore_data.sh             # 取最新的 data-* Release，還原 data/（含校驗）
bash scripts/restore_data.sh --with-kg   # 另加共用知識圖譜與預測模型（只有重跑預測才需要）
```

需要 [GitHub CLI](https://cli.github.com/)（`gh auth login`）與 [uv](https://docs.astral.sh/uv/)。

### 改頁工具鏈

事實層、checker、許可證狀態計算等放在 `tools/txgnn/.claude/`，是母 repo `yao-care/txgnn` 的 `.claude/` 複本（版本見 `tools/txgnn/VERSION`）。
規則要改請改母 repo，再用 `python3 .claude/sync_site_tools.py MyTxGNN` 同步過來，不要直接改這裡的複本。
在本 repo 單獨使用時，先組工作目錄：

```bash
WS=$(bash scripts/txgnn_ws.sh)
cd "$WS"
python3 .claude/dump_license_facts_20261021.py MyTxGNN       # 依證據包算市場狀態（checker 要用）
python3 .claude/checker_trend.py --no-append MyTxGNN           # 全部藥物頁 checker，必須「非 0 0」
```

### 許可證排程更新（GitHub Actions）

`.github/workflows/license-refresh.yml` 每週一 UTC 03:17 自動執行，也可以在 Actions 頁手動觸發（可選只試跑）：

1. 從 Release 還原 `data/`（`scripts/restore_data.sh`）
2. 從主管機關下載最新許可證資料（`scripts/license_adapter.py`），檢查筆數與格式
3. 更新證據包的許可證狀態 → 重算市場狀態 → 同步許可證表 → 事實層改頁 → checker 全量必須 0 → 衍生檔 → gate
4. 全部通過才推上 `main` 並觸發部署；更新後的 `data/` 另存成新的 `data-YYYYMMDD` Release

以下情況一律不推、自動開 issue（label `license-refresh`）：下載失敗或格式改變、狀態變動超過兩成、
改到的藥物頁超過 min(200, 5%)、checker／gate／h1 沒過、有人工查核紀錄的頁會被改到。全程不使用 AI。
<!-- txgnn-ops:end -->
