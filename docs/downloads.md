---
layout: default
title: Muat Turun
parent: Sumber
nav_order: 2
description: "Download MyTxGNN drug repurposing prediction data"
permalink: /downloads/
---

# Downloads

Download MyTxGNN prediction data for your research.

---

## Available Datasets

### Candidate Pairs (not predictions)

| File | Description | Format | Size |
|------|-------------|--------|------|
| `repurposing_candidates.csv` | Drug–disease candidate pairs before filtering; includes known uses and is not a list of predictions | CSV | ~4.7 MB |

**Columns:**
- `license_id`: NPRA registration number
- `brand_name`: Product name
- `ingredient`: Active ingredient
- `drugbank_id`: DrugBank identifier
- `disease_name`: Candidate disease
- `disease_id`: Disease identifier
- `source`: Source
- `is_new`: New indication flag

**Statistics:**
- 41,560 candidate pairs
- 508 unique drugs
- 940 unique diseases

---

### DrugBank Mapping

| File | Description | Format | Size |
|------|-------------|--------|------|
| `drugbank_mapping.csv` | Drug ID mappings | CSV | ~1.8 MB |

**Columns:**
- `ingredient`: Normalized ingredient name
- `drugbank_id`: DrugBank identifier
- `match_score`: Mapping confidence

---

### Deep Learning Predictions

| File | Description | Format | Size |
|------|-------------|--------|------|
| `txgnn_checkpoint.csv` | DL model predictions | CSV | ~756 MB |

**Columns:**
- `drugbank_id`: DrugBank identifier
- `drug_name`: Drug name
- `disease_name`: Predicted indication
- `txgnn_score`: Confidence score (0-1)

**Statistics:**
- 9,968,985 total predictions
- {{ site.data.site_stats.indications }} listed on the site (score ≥ 0.99, up to 10 per drug, known uses excluded)
- 585 unique drugs
- 17,041 unique diseases

---

## How to Download

### Via GitHub

All data files are available in the project repository:

```bash
git clone https://github.com/yao-care/MyTxGNN.git
cd MyTxGNN/data/processed
```

### Direct Links

- [Candidate Pairs (unfiltered)](https://github.com/yao-care/MyTxGNN/blob/main/data/processed/repurposing_candidates.csv)
- [DrugBank Mapping](https://github.com/yao-care/MyTxGNN/blob/main/data/processed/drugbank_mapping.csv)

---

## FHIR Resources

FHIR R4 formatted resources are also available:

| Resource Type | Count | Location |
|---------------|-------|----------|
| MedicationKnowledge | 508 | `/fhir/MedicationKnowledge/` |
| ClinicalUseDefinition | 41,560 | `/fhir/ClinicalUseDefinition/` |

Access via:
```
GET /fhir/MedicationKnowledge/{drugbank_id}.json
GET /fhir/ClinicalUseDefinition/{drug}-{indication}.json
```

---

## Data Dictionary

### Prediction Score Interpretation

The site only lists predictions with a score of 0.99 or higher (up to the top 10 per drug, known uses excluded). The score ranks candidates inside the model; it is not a probability of clinical efficacy.

### Disease Naming Convention

Disease names follow the TxGNN knowledge graph ontology, which is derived from:
- MONDO Disease Ontology
- Disease Ontology (DO)
- Human Phenotype Ontology (HPO)

---

## Usage Examples

### Python

```python
import pandas as pd

# Load candidate pairs (unfiltered, includes known uses)
kg = pd.read_csv('repurposing_candidates.csv')

# Filter for a specific drug
metformin = kg[kg['ingredient'] == 'METFORMIN']

# Get high-score DL predictions
dl = pd.read_csv('txgnn_checkpoint.csv')
high_conf = dl[dl['txgnn_score'] >= 0.99]  # site threshold
```

### R

```r
library(readr)

# Load candidate pairs (unfiltered, includes known uses)
kg <- read_csv('repurposing_candidates.csv')

# Filter by drug
prednisolone <- kg %>% filter(ingredient == 'PREDNISOLONE')

# Summary statistics
kg %>% group_by(disease_name) %>% summarise(n = n()) %>% arrange(desc(n))
```

---

## Terms of Use

By downloading this data, you agree to:

1. **Attribution**: Cite MyTxGNN and TxGNN (Huang et al., 2024) in publications
2. **Research Use**: Data is provided for research purposes
3. **No Clinical Decisions**: Do not use predictions for clinical decisions without validation
4. **Compliance**: Follow applicable data protection regulations

---

## Citation

When using this data, please cite:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Prediction data is provided for research purposes only. Predictions have not been clinically validated and should not be used for medical decisions.
</div>
