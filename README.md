# MyTxGNN - Malaysia Drug Repurposing Predictions

[![Website](https://img.shields.io/badge/Website-mytxgnn.yao.care-blue)](https://mytxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FHIR R4](https://img.shields.io/badge/FHIR-R4-orange)](https://mytxgnn.yao.care/fhir/metadata)

Drug repurposing predictions for NPRA-approved pharmaceuticals in Malaysia using TxGNN knowledge graph.

## Important Notice

- **Research Use Only**: Results are for research reference and do not constitute medical advice
- **Clinical Validation Required**: Drug repurposing candidates require clinical trials before application
- **Consult Healthcare Professionals**: Always seek professional medical advice for treatment decisions

## Project Overview

### Prediction Statistics

| Metric | Count |
|--------|-------|
| **Drugs Analyzed** | 508 |
| **KG Predictions** | 41,560 |
| **DL Predictions** | 9,968,985 |
| **High Confidence (≥0.7)** | 176,021 |
| **Unique Diseases** | 17,041 |

### Data Sources

| Source | Description | Records |
|--------|-------------|---------|
| **NPRA Registry** | Malaysia pharmaceutical products via [data.gov.my](https://data.gov.my/data-catalogue/pharmaceutical_products) | 27,938 |
| **TxGNN** | Harvard knowledge graph ([Nature Medicine 2023](https://doi.org/10.1038/s41591-023-02233-x)) | 17,080 nodes |
| **DrugBank** | Drug standardization and mapping | 508 matched |

### Top Drugs by Prediction Count

| Rank | Drug | DrugBank ID | KG Predictions |
|------|------|-------------|----------------|
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

## Prediction Methods

TxGNN provides two prediction approaches:

| Method | Speed | Precision | Requirements | Results |
|--------|-------|-----------|--------------|---------|
| Knowledge Graph | Fast (seconds) | Lower | No special requirements | `repurposing_candidates.csv` |
| Deep Learning | Slow (hours) | Higher | Conda + PyTorch + DGL | `txgnn_checkpoint.csv` |

**Key Difference**: Knowledge graph method queries existing drug-disease relationships; deep learning method uses neural network inference to predict potential relationships with confidence scores.

### Knowledge Graph Method

```bash
uv run python scripts/run_kg_prediction.py
```

**Output**: `data/processed/repurposing_candidates.csv`

| Metric | Value |
|--------|-------|
| NPRA Products | 27,938 |
| Unique Ingredients | ~2,500 |
| DrugBank Mapped | 508 (73.87%) |
| KG Predictions | 41,560 |
| Unique Diseases | 940 |

### Deep Learning Method

```bash
# Requires conda environment with PyTorch + DGL
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

**Output**: `data/processed/txgnn_checkpoint.csv`

| Metric | Value |
|--------|-------|
| Total Predictions | 9,968,985 |
| Drugs | 585 |
| Diseases | 17,041 |
| High Confidence (≥0.7) | 176,021 |
| Very High Confidence (≥0.9) | ~50,000 |

### TxGNN Score Interpretation

| Score Range | Meaning | Recommended Action |
|-------------|---------|-------------------|
| ≥ 0.95 | Very high confidence | Priority for investigation |
| 0.90 - 0.95 | High confidence | Worth investigating |
| 0.70 - 0.90 | Moderate-high confidence | Consider with caution |
| 0.50 - 0.70 | Moderate confidence | Exploratory only |
| < 0.50 | Low confidence | Requires strong rationale |

---

## Quick Start

### Step 1: Download Data

| File | Download Link | Location | Purpose |
|------|---------------|----------|---------|
| NPRA Data | [data.gov.my](https://data.gov.my/data-catalogue/pharmaceutical_products) | `data/raw/` | Malaysia drug registry |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | `data/node.csv` | TxGNN node data |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | `data/kg.csv` | TxGNN knowledge graph |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | `data/edges.csv` | Edge data (for DL) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | `model_ckpt/` | Pre-trained model (for DL) |

### Step 2: Install Dependencies

```bash
# Install basic dependencies
uv sync

# Run tests
uv run pytest tests/
```

### Step 3: Process NPRA Data

```bash
uv run python scripts/process_fda_data.py
```

This generates `data/raw/my_fda_drugs.json`.

### Step 4: Prepare Vocabulary Data

```bash
uv run python scripts/prepare_external_data.py
```

This generates files in `data/external/`:
- `drugbank_vocab.csv` - DrugBank vocabulary
- `disease_vocab.csv` - Disease vocabulary
- `drug_disease_relations.csv` - Drug-disease relationships

### Step 5: Run Knowledge Graph Prediction

```bash
uv run python scripts/run_kg_prediction.py
```

### Step 6: Set Up Deep Learning Environment (Optional)

```bash
# Create conda environment
conda create -n txgnn python=3.11 -y
conda activate txgnn

# Install PyTorch
pip install torch==2.2.2 torchvision==0.17.2

# Install DGL
pip install dgl==1.1.3

# Install TxGNN
pip install git+https://github.com/mims-harvard/TxGNN.git

# Install other dependencies
pip install pandas tqdm pyyaml pydantic ogb

# Verify installation
python -c "import torch; import dgl; import txgnn; print('Installation successful!')"
```

### Step 7: Run Deep Learning Prediction (Optional)

```bash
# Extract model files
unzip -n model_ckpt.zip

# Run prediction
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

---

## FHIR R4 API

Access drug data via FHIR R4 API:

| Endpoint | Description |
|----------|-------------|
| `/fhir/metadata` | Capability statement |
| `/fhir/MedicationKnowledge/{id}` | Drug information |
| `/fhir/ClinicalUseDefinition/{drug}-{indication}` | Prediction data |

**Example**:
```bash
curl https://mytxgnn.yao.care/fhir/MedicationKnowledge/db00860.json
```

---

## Project Structure

```
MyTxGNN/
├── README.md                    # Project documentation
├── CLAUDE.md                    # AI assistant guide (SOP)
├── pyproject.toml               # Python package config
│
├── data/                        # Data directory
│   ├── kg.csv                   # 🟡 TxGNN knowledge graph
│   ├── node.csv                 # 🟡 TxGNN node data
│   ├── raw/
│   │   └── my_fda_drugs.json    # 🟢 NPRA drug data
│   ├── external/                # 🔵 Generated by prepare_external_data.py
│   │   ├── drugbank_vocab.csv
│   │   ├── disease_vocab.csv
│   │   └── drug_disease_relations.csv
│   └── processed/
│       ├── drugbank_mapping.csv        # 🔵 Drug→DrugBank mapping
│       ├── repurposing_candidates.csv  # 🔵 KG method results
│       └── txgnn_checkpoint.csv        # 🔵 DL method results
│
├── docs/                        # Jekyll documentation site
│   ├── _config.yml
│   ├── _drugs/                  # 508 drug report pages
│   ├── fhir/                    # FHIR resources
│   └── ...
│
├── src/txgnn/                   # Core code
│   ├── data/loader.py           # NPRA data loader
│   ├── mapping/
│   │   ├── normalizer.py        # Drug name standardization
│   │   ├── drugbank_mapper.py   # DrugBank ID mapping
│   │   └── disease_mapper.py    # Disease mapping
│   ├── predict/
│   │   ├── repurposing.py       # KG method
│   │   └── txgnn_model.py       # DL method
│   └── collectors/              # Evidence collectors
│       ├── npra.py              # NPRA collector
│       ├── clinicaltrials.py    # ClinicalTrials.gov
│       └── pubmed.py            # PubMed
│
├── scripts/                     # Execution scripts
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   ├── run_txgnn_prediction.py
│   └── generate_fhir_resources.py
│
└── tests/                       # Test suite
```

**Legend**: 🔵 Project code | 🟢 Malaysia data | 🟡 TxGNN data

---

## Related Resources

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine 2023
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org) - Interactive prediction query
- [NPRA Malaysia](https://www.npra.gov.my/) - National Pharmaceutical Regulatory Agency
- [data.gov.my](https://data.gov.my/) - Malaysia Open Data Portal

---

## Citation

If you use this dataset or software, please cite:

```bibtex
@misc{mytxgnn2026,
  title={MyTxGNN: Drug Repurposing Predictions for NPRA-Approved Drugs in Malaysia},
  url={https://mytxgnn.yao.care},
  year={2026}
}
```

And cite the original TxGNN paper:

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

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgments

- [Harvard Zitnik Lab](https://zitniklab.hms.harvard.edu/) for TxGNN
- [NPRA Malaysia](https://www.npra.gov.my/) for pharmaceutical registry data
- [data.gov.my](https://data.gov.my/) for open data access
