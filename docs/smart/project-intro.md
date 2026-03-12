---
layout: default
title: Project Introduction
parent: SMART on FHIR
nav_order: 7
description: "Introduction to MyTxGNN project for international audience"
permalink: /smart/project-intro/
---

# MyTxGNN Project Introduction

<p class="key-answer" data-question="What is MyTxGNN?">
<strong>MyTxGNN</strong> is a drug repurposing prediction platform for Malaysia, built on Harvard's TxGNN model published in Nature Medicine. It provides AI-powered predictions for potential new therapeutic uses of NPRA-approved drugs.
</p>

---

## Project Overview

| Metric | Value |
|--------|-------|
| **Drugs Analyzed** | 508 |
| **KG Predictions** | 41,560 |
| **DL Predictions** | 9,968,985 |
| **High Confidence (≥0.7)** | 176,021 |
| **Unique Diseases** | 17,041 |

---

## Key Features

### 1. Dual Prediction Methods

- **Knowledge Graph (KG)**: Fast queries based on existing drug-disease relationships
- **Deep Learning (DL)**: Neural network-based predictions with confidence scores

### 2. FHIR R4 API

Access predictions programmatically using the FHIR R4 standard:

```bash
curl https://mytxgnn.yao.care/fhir/MedicationKnowledge/db00860.json
```

### 3. Evidence Levels

Each prediction is assigned an evidence level (L1-L5) based on supporting clinical evidence.

### 4. Malaysia Focus

Focused on drugs registered with Malaysia's National Pharmaceutical Regulatory Agency (NPRA), ensuring relevance to local healthcare needs.

---

## Data Sources

| Source | Description | Records |
|--------|-------------|---------|
| **NPRA Registration** | Malaysia pharmaceutical products via [data.gov.my](https://data.gov.my/) | 27,938 |
| **TxGNN** | Harvard knowledge graph ([Nature Medicine 2023](https://doi.org/10.1038/s41591-023-02233-x)) | 17,080 nodes |
| **DrugBank** | Drug standardization and mapping | 508 matched |

---

## Technology Stack

- **Backend**: Python, TxGNN, DGL (Deep Graph Library)
- **Frontend**: Jekyll, GitHub Pages
- **Standards**: FHIR R4, SMART on FHIR, CDS Hooks
- **Data**: TxGNN Knowledge Graph, DrugBank, NPRA

---

## Use Cases

### Research

- Identify drug repurposing candidates for rare diseases
- Explore drug-disease relationships in the knowledge graph
- Access prediction data via API for downstream analysis

### Clinical Decision Support

- Integrate with EHR systems via SMART on FHIR
- Receive alerts for potential new indications
- Access evidence summaries for repurposing candidates

### Education

- Learn about drug repurposing methodologies
- Understand knowledge graph approaches
- Explore FHIR/SMART standards implementation

---

## Team

MyTxGNN is developed and maintained by the yao.care research team, building on the foundational work of Harvard's Zitnik Lab.

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

## Related Resources

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine 2023
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org) - Interactive prediction queries
- [NPRA Malaysia](https://www.npra.gov.my/) - National Pharmaceutical Regulatory Agency

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This platform is for <strong>research purposes only</strong> and does not constitute medical advice. Drug repurposing predictions require clinical validation before application.
<br><br>
<small>Last updated: 2026-03-03 | MyTxGNN Research Team</small>
</div>
