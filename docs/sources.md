---
layout: default
title: Data Sources
parent: Sumber
nav_order: 1
description: "Data sources used in MyTxGNN drug repurposing predictions"
permalink: /sources/
---

# Data Sources
{: .fs-9 }

Databases and sources used in this project
{: .fs-6 .fw-300 }

---

## Data Source Overview

| Data Type | Source | Usage |
|-----------|--------|-------|
| AI Predictions | TxGNN | Drug-disease association prediction |
| Clinical Trials | ClinicalTrials.gov | Clinical evidence validation |
| Literature | PubMed | Research evidence validation |
| Drug Information | DrugBank | Pharmacology and mechanism data |
| Malaysia Approval | NPRA | Local market information |
| Drug Interactions | DDInter, GtoPdb | DDI information |

---

## TxGNN Model

### Overview

TxGNN is a drug repurposing prediction model developed by Professor Marinka Zitnik's team at Harvard Medical School.

### Publication

- **Title**: A foundation model for clinician-centered drug repurposing
- **Journal**: Nature Medicine (2023)
- **DOI**: [10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

### Data Scale

| Item | Count |
|------|-------|
| Nodes | 17,080 |
| Drugs | 4,465 |
| Diseases | 2,870 |
| Known Drug-Disease Relationships | 14,573 |

### Data Download

- [node.csv](https://dataverse.harvard.edu/api/access/datafile/7144482) - Node data
- [kg.csv](https://dataverse.harvard.edu/api/access/datafile/7144484) - Knowledge graph

---

## ClinicalTrials.gov

### Overview

The world's largest clinical trial registry, maintained by the U.S. National Institutes of Health (NIH).

### Website

[https://clinicaltrials.gov/](https://clinicaltrials.gov/)

### Usage

- Search drug name + disease name via API
- Collect trial ID, phase, status, enrollment, etc.

### Collected Fields

| Field | Description |
|-------|-------------|
| NCT Number | Unique trial identifier |
| Phase | Trial phase (Phase 1-4) |
| Status | Trial status |
| Enrollment | Number of participants |
| Conditions | Studied diseases |
| Interventions | Interventions (drugs) |

---

## PubMed

### Overview

Biomedical literature database maintained by the U.S. National Library of Medicine (NLM).

### Website

[https://pubmed.ncbi.nlm.nih.gov/](https://pubmed.ncbi.nlm.nih.gov/)

### Usage

- Search via E-utilities API
- Drug name + disease name as keywords

### Collected Fields

| Field | Description |
|-------|-------------|
| PMID | PubMed unique identifier |
| Title | Article title |
| Year | Publication year |
| Journal | Journal name |
| Abstract | Abstract content |
| Publication Type | Literature type |

---

## DrugBank

### Overview

Comprehensive drug database maintained by OMx Personal Health Analytics (Canada).

### Website

[https://go.drugbank.com/](https://go.drugbank.com/)

### Collected Fields

| Field | Description |
|-------|-------------|
| DrugBank ID | Drug unique identifier |
| Name | Drug name |
| Mechanism of Action | Mechanism of action |
| Pharmacodynamics | Pharmacodynamics |
| Indication | Approved indications |

---

## Malaysia NPRA

### Overview

National Pharmaceutical Regulatory Agency (NPRA) of Malaysia, responsible for drug registration management.

### Data Source

[data.gov.my - Pharmaceutical Products](https://data.gov.my/data-catalogue/pharmaceutical_products)

### Collected Fields

| Field | Description |
|-------|-------------|
| Registration Number | Drug registration number |
| Product Name | Product name |
| Active Ingredients | Active ingredients |
| Dosage Form | Dosage form |
| Registration Status | Active/Cancelled |

---

## Drug-Drug Interactions (DDI)

### DDInter 2.0

- **Website**: [https://ddinter2.scbdd.com/](https://ddinter2.scbdd.com/)
- **Scale**: 302,516 DDI records, 2,310 drugs
- **Usage**: Drug-drug interaction information

### Guide to PHARMACOLOGY (GtoPdb)

- **Website**: [https://www.guidetopharmacology.org/](https://www.guidetopharmacology.org/)
- **Maintained by**: IUPHAR/BPS
- **Usage**: Approved drug interactions

### Data Scale

| Source | DDI Count | Update Date |
|--------|-----------|-------------|
| DDInter | 222,391 records | 2026-02 |
| GtoPdb | 4,636 records | 2026-02 |

---

## Data Update Frequency

| Data Type | Update Frequency |
|-----------|-----------------|
| TxGNN Predictions | On model version update |
| Clinical Trials | On report generation |
| PubMed Literature | On report generation |
| NPRA Registry | Weekly |
| DDI Data | Quarterly recommended |

---

## Licensing and Citation

Please cite original data sources when using this project's data.

### TxGNN Citation

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

### This Project Citation

```bibtex
@misc{mytxgnn2026,
  title={MyTxGNN: Malaysia Drug Repurposing Prediction Platform},
  url={https://mytxgnn.yao.care},
  year={2026}
}
```

---

## NPRA Data Attribution

NPRA pharmaceutical product data is licensed under CC BY 4.0 by the Government of Malaysia via data.gov.my.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
All data is provided for research purposes only. While we strive for accuracy, users should verify critical information from primary sources.
</div>
