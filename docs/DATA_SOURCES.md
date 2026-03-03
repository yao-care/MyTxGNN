---
layout: default
title: Data Sources
nav_order: 5
description: "Data sources used in MyTxGNN drug repurposing predictions"
permalink: /DATA_SOURCES/
---

# Data Sources

MyTxGNN integrates multiple authoritative data sources for comprehensive drug repurposing predictions.

---

## Primary Data Sources

### TxGNN Knowledge Graph

| Attribute | Value |
|-----------|-------|
| **Source** | [Harvard Zitnik Lab](https://zitniklab.hms.harvard.edu/projects/TxGNN/) |
| **Publication** | Nature Medicine (2023) |
| **Nodes** | 17,080 (drugs, diseases, genes, proteins) |
| **Use** | AI prediction model |

The TxGNN knowledge graph forms the foundation of our predictions, integrating relationships from multiple biomedical databases.

### Malaysia NPRA Drug Registry

| Attribute | Value |
|-----------|-------|
| **Source** | [data.gov.my](https://data.gov.my/data-catalogue/pharmaceutical_products) |
| **Agency** | National Pharmaceutical Regulatory Agency (NPRA) |
| **Records** | 27,938 pharmaceutical products |
| **License** | CC BY 4.0 |
| **Update Frequency** | Daily |

**Fields Used:**
- Registration number (reg_no)
- Product name
- Active ingredients
- Registration status
- Holder information

### DrugBank

| Attribute | Value |
|-----------|-------|
| **Source** | [DrugBank Online](https://go.drugbank.com/) |
| **Version** | Latest available |
| **Drugs Mapped** | 508 |
| **Use** | Drug standardization, mechanism data |

**Fields Used:**
- DrugBank ID
- Drug name standardization
- Mechanism of action
- Known indications

---

## Evidence Collection Sources

### ClinicalTrials.gov

| Attribute | Value |
|-----------|-------|
| **Source** | [ClinicalTrials.gov](https://clinicaltrials.gov/) |
| **Operated By** | U.S. National Library of Medicine |
| **Use** | Clinical trial evidence |
| **API** | ClinicalTrials.gov API v2 |

**Fields Collected:**
- NCT ID (trial identifier)
- Trial phase
- Study status
- Enrollment count
- Start/completion dates
- Sponsor information

### PubMed

| Attribute | Value |
|-----------|-------|
| **Source** | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) |
| **Operated By** | NCBI |
| **Use** | Literature evidence |
| **API** | E-utilities API |

**Fields Collected:**
- PMID
- Article title
- Publication year
- Journal name
- Abstract

### WHO ICTRP

| Attribute | Value |
|-----------|-------|
| **Source** | [WHO ICTRP](https://trialsearch.who.int/) |
| **Operated By** | World Health Organization |
| **Use** | International clinical trials |
| **Coverage** | Southeast Asia registries (TCTR, etc.) |

---

## Data Processing Pipeline

```
NPRA Data → DrugBank Mapping → TxGNN Prediction → Evidence Collection → Report Generation
```

### Step 1: NPRA Data Processing

1. Download pharmaceutical products dataset from data.gov.my
2. Filter for active registrations (PRODUCT APPROVED)
3. Extract and normalize active ingredients
4. Parse ingredient names and dosage information

### Step 2: DrugBank Mapping

1. Normalize drug names (remove salts, standardize spelling)
2. Match to DrugBank IDs using fuzzy matching
3. Validate mappings against DrugBank database
4. **Mapping Rate**: ~73% of unique ingredients

### Step 3: TxGNN Prediction

1. Load TxGNN model and knowledge graph
2. Run knowledge graph inference for drug-disease pairs
3. Run deep learning model for confidence scores
4. Filter and rank predictions

### Step 4: Evidence Collection

1. Query ClinicalTrials.gov for each drug-disease pair
2. Search PubMed for relevant literature
3. Check ICTRP for regional trials
4. Aggregate and format evidence

---

## Data Quality Measures

### Validation Checks

- Drug name normalization accuracy
- DrugBank ID verification
- Clinical trial ID format validation
- PubMed ID existence check

### Coverage Statistics

| Metric | Value |
|--------|-------|
| NPRA products processed | 27,938 |
| Unique ingredients | ~2,500 |
| DrugBank mapped | 508 (73.87% of matchable) |
| KG predictions | 41,560 |
| DL predictions (score ≥0.7) | 176,021 |

---

## Data Update Schedule

| Data Source | Update Frequency |
|-------------|------------------|
| NPRA Registry | Weekly |
| DrugBank | Monthly |
| ClinicalTrials.gov | On-demand |
| PubMed | On-demand |

---

## Terms of Use

### NPRA Data
- Licensed under CC BY 4.0 by Malaysia Government
- Attribution required

### DrugBank Data
- Used under academic license
- Attribution required

### Clinical Trial Data
- Public domain (ClinicalTrials.gov)
- No restrictions

### PubMed Data
- NCBI Disclaimer applies
- No restrictions on article metadata

---

## Citation Requirements

When using MyTxGNN data, please cite:

1. **TxGNN Model**: Huang et al., Nature Medicine (2023)
2. **NPRA Data**: data.gov.my with CC BY 4.0 attribution
3. **DrugBank**: DrugBank Online with appropriate license citation

---

<div class="disclaimer">
<strong>Data Disclaimer</strong><br>
Data is provided for research purposes only. While we strive for accuracy, users should verify critical information from primary sources. Data may be subject to change without notice.
</div>
