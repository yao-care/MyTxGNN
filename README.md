# MyTxGNN - Ramalan Penggunaan Semula Ubat di Malaysia

[![Website](https://img.shields.io/badge/Website-mytxgnn.yao.care-blue)](https://mytxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FHIR R4](https://img.shields.io/badge/FHIR-R4-orange)](https://mytxgnn.yao.care/fhir/metadata)

Ramalan penggunaan semula ubat untuk produk farmaseutikal yang diluluskan NPRA di Malaysia menggunakan graf pengetahuan TxGNN.

## Notis Penting

- **Untuk Penyelidikan Sahaja**: Keputusan adalah untuk rujukan penyelidikan dan bukan nasihat perubatan
- **Pengesahan Klinikal Diperlukan**: Calon penggunaan semula ubat memerlukan ujian klinikal sebelum aplikasi
- **Rujuk Profesional Kesihatan**: Sentiasa dapatkan nasihat perubatan profesional untuk keputusan rawatan

## Gambaran Keseluruhan Projek

### Statistik Ramalan

| Metrik | Jumlah |
|--------|--------|
| **Ubat Dianalisis** | 508 |
| **Ramalan KG** | 41,560 |
| **Ramalan DL** | 9,968,985 |
| **Keyakinan Tinggi (≥0.7)** | 176,021 |
| **Penyakit Unik** | 17,041 |

### Sumber Data

| Sumber | Penerangan | Rekod |
|--------|------------|-------|
| **Pendaftaran NPRA** | Produk farmaseutikal Malaysia melalui [data.gov.my](https://data.gov.my/data-catalogue/pharmaceutical_products) | 27,938 |
| **TxGNN** | Graf pengetahuan Harvard ([Nature Medicine 2023](https://doi.org/10.1038/s41591-023-02233-x)) | 17,080 nod |
| **DrugBank** | Penstandardan dan pemetaan ubat | 508 dipadankan |

### Ubat Teratas mengikut Jumlah Ramalan

| Kedudukan | Ubat | ID DrugBank | Ramalan KG |
|-----------|------|-------------|------------|
| 1 | Prednisolone | DB00860 | 3,650 |
| 2 | Betamethasone | DB00443 | 3,198 |
| 3 | Fusidic Acid | DB02703 | 3,008 |
| 4 | Hydrocortisone Acetate | DB14539 | 2,880 |
| 5 | Hydrocortisone | DB00741 | 2,780 |
| 6 | Dexamethasone | DB01234 | 2,736 |
| 7 | Ketoconazole | DB01026 | 759 |
| 8 | Ofloxacin | DB01165 | 690 |
| 9 | Triamcinolone | DB00620 | 645 |
| 10 | Mometasone Furoate | DB14512 | 640 |

---

## Kaedah Ramalan

TxGNN menyediakan dua pendekatan ramalan:

| Kaedah | Kelajuan | Ketepatan | Keperluan | Hasil |
|--------|----------|-----------|-----------|-------|
| Graf Pengetahuan | Cepat (saat) | Rendah | Tiada keperluan khas | `repurposing_candidates.csv` |
| Pembelajaran Mendalam | Lambat (jam) | Tinggi | Conda + PyTorch + DGL | `txgnn_checkpoint.csv` |

**Perbezaan Utama**: Kaedah graf pengetahuan menanyakan hubungan ubat-penyakit sedia ada; kaedah pembelajaran mendalam menggunakan inferens rangkaian neural untuk meramalkan hubungan berpotensi dengan skor keyakinan.

### Kaedah Graf Pengetahuan

```bash
uv run python scripts/run_kg_prediction.py
```

**Output**: `data/processed/repurposing_candidates.csv`

| Metrik | Nilai |
|--------|-------|
| Produk NPRA | 27,938 |
| Bahan Unik | ~2,500 |
| Dipetakan DrugBank | 508 (73.87%) |
| Ramalan KG | 41,560 |
| Penyakit Unik | 940 |

### Kaedah Pembelajaran Mendalam

```bash
# Memerlukan persekitaran conda dengan PyTorch + DGL
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

**Output**: `data/processed/txgnn_checkpoint.csv`

| Metrik | Nilai |
|--------|-------|
| Jumlah Ramalan | 9,968,985 |
| Ubat | 585 |
| Penyakit | 17,041 |
| Keyakinan Tinggi (≥0.7) | 176,021 |
| Keyakinan Sangat Tinggi (≥0.9) | ~50,000 |

### Tafsiran Skor TxGNN

| Julat Skor | Maksud | Tindakan Disyorkan |
|------------|--------|-------------------|
| ≥ 0.95 | Keyakinan sangat tinggi | Keutamaan untuk penyiasatan |
| 0.90 - 0.95 | Keyakinan tinggi | Patut disiasat |
| 0.70 - 0.90 | Keyakinan sederhana-tinggi | Pertimbangkan dengan berhati-hati |
| 0.50 - 0.70 | Keyakinan sederhana | Penerokaan sahaja |
| < 0.50 | Keyakinan rendah | Memerlukan rasional kukuh |

---

## Mula Pantas

### Langkah 1: Muat Turun Data

| Fail | Pautan Muat Turun | Lokasi | Tujuan |
|------|-------------------|--------|--------|
| Data NPRA | [data.gov.my](https://data.gov.my/data-catalogue/pharmaceutical_products) | `data/raw/` | Pendaftaran ubat Malaysia |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | `data/node.csv` | Data nod TxGNN |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | `data/kg.csv` | Graf pengetahuan TxGNN |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | `data/edges.csv` | Data tepi (untuk DL) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | `model_ckpt/` | Model pra-latih (untuk DL) |

### Langkah 2: Pasang Kebergantungan

```bash
# Pasang kebergantungan asas
uv sync

# Jalankan ujian
uv run pytest tests/
```

### Langkah 3: Proses Data NPRA

```bash
uv run python scripts/process_fda_data.py
```

Ini menghasilkan `data/raw/my_fda_drugs.json`.

### Langkah 4: Sediakan Data Kosa Kata

```bash
uv run python scripts/prepare_external_data.py
```

Ini menghasilkan fail dalam `data/external/`:
- `drugbank_vocab.csv` - Kosa kata DrugBank
- `disease_vocab.csv` - Kosa kata penyakit
- `drug_disease_relations.csv` - Hubungan ubat-penyakit

### Langkah 5: Jalankan Ramalan Graf Pengetahuan

```bash
uv run python scripts/run_kg_prediction.py
```

### Langkah 6: Sediakan Persekitaran Pembelajaran Mendalam (Pilihan)

```bash
# Cipta persekitaran conda
conda create -n txgnn python=3.11 -y
conda activate txgnn

# Pasang PyTorch
pip install torch==2.2.2 torchvision==0.17.2

# Pasang DGL
pip install dgl==1.1.3

# Pasang TxGNN
pip install git+https://github.com/mims-harvard/TxGNN.git

# Pasang kebergantungan lain
pip install pandas tqdm pyyaml pydantic ogb

# Sahkan pemasangan
python -c "import torch; import dgl; import txgnn; print('Pemasangan berjaya!')"
```

### Langkah 7: Jalankan Ramalan Pembelajaran Mendalam (Pilihan)

```bash
# Ekstrak fail model
unzip -n model_ckpt.zip

# Jalankan ramalan
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

---

## API FHIR R4

Akses data ubat melalui API FHIR R4:

| Endpoint | Penerangan |
|----------|------------|
| `/fhir/metadata` | Penyata keupayaan |
| `/fhir/MedicationKnowledge/{id}` | Maklumat ubat |
| `/fhir/ClinicalUseDefinition/{ubat}-{indikasi}` | Data ramalan |

**Contoh**:
```bash
curl https://mytxgnn.yao.care/fhir/MedicationKnowledge/db00860.json
```

---

## Struktur Projek

```
MyTxGNN/
├── README.md                    # Dokumentasi projek
├── CLAUDE.md                    # Panduan pembantu AI (SOP)
├── pyproject.toml               # Konfigurasi pakej Python
│
├── data/                        # Direktori data
│   ├── kg.csv                   # 🟡 Graf pengetahuan TxGNN
│   ├── node.csv                 # 🟡 Data nod TxGNN
│   ├── raw/
│   │   └── my_fda_drugs.json    # 🟢 Data ubat NPRA
│   ├── external/                # 🔵 Dijana oleh prepare_external_data.py
│   │   ├── drugbank_vocab.csv
│   │   ├── disease_vocab.csv
│   │   └── drug_disease_relations.csv
│   └── processed/
│       ├── drugbank_mapping.csv        # 🔵 Pemetaan Ubat→DrugBank
│       ├── repurposing_candidates.csv  # 🔵 Hasil kaedah KG
│       └── txgnn_checkpoint.csv        # 🔵 Hasil kaedah DL
│
├── docs/                        # Laman dokumentasi Jekyll
│   ├── _config.yml
│   ├── _drugs/                  # 508 halaman laporan ubat
│   ├── fhir/                    # Sumber FHIR
│   └── ...
│
├── src/txgnn/                   # Kod teras
│   ├── data/loader.py           # Pemuat data NPRA
│   ├── mapping/
│   │   ├── normalizer.py        # Penstandardan nama ubat
│   │   ├── drugbank_mapper.py   # Pemetaan ID DrugBank
│   │   └── disease_mapper.py    # Pemetaan penyakit
│   ├── predict/
│   │   ├── repurposing.py       # Kaedah KG
│   │   └── txgnn_model.py       # Kaedah DL
│   └── collectors/              # Pengumpul bukti
│       ├── npra.py              # Pengumpul NPRA
│       ├── clinicaltrials.py    # ClinicalTrials.gov
│       └── pubmed.py            # PubMed
│
├── scripts/                     # Skrip pelaksanaan
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   ├── run_txgnn_prediction.py
│   └── generate_fhir_resources.py
│
└── tests/                       # Suite ujian
```

**Petunjuk**: 🔵 Kod projek | 🟢 Data Malaysia | 🟡 Data TxGNN

---

## Sumber Berkaitan

- [Kertas TxGNN](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine 2023
- [GitHub TxGNN](https://github.com/mims-harvard/TxGNN)
- [Penjelajah TxGNN](http://txgnn.org) - Pertanyaan ramalan interaktif
- [NPRA Malaysia](https://www.npra.gov.my/) - Agensi Regulatori Farmaseutikal Kebangsaan
- [data.gov.my](https://data.gov.my/) - Portal Data Terbuka Malaysia

---

## Petikan

Jika anda menggunakan dataset atau perisian ini, sila petik:

```bibtex
@misc{mytxgnn2026,
  title={MyTxGNN: Ramalan Penggunaan Semula Ubat untuk Ubat Diluluskan NPRA di Malaysia},
  url={https://mytxgnn.yao.care},
  year={2026}
}
```

Dan petik kertas TxGNN asal:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## Lesen

Lesen MIT - Lihat [LICENSE](LICENSE) untuk butiran.

## Penghargaan

- [Harvard Zitnik Lab](https://zitniklab.hms.harvard.edu/) untuk TxGNN
- [NPRA Malaysia](https://www.npra.gov.my/) untuk data pendaftaran farmaseutikal
- [data.gov.my](https://data.gov.my/) untuk akses data terbuka
