---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carfilzomib: From Multiple Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib is a second-generation proteasome inhibitor from the same drug class approved for relapsed/refractory multiple myeloma. The TxGNN model predicts potential activity against **Melanoma** (and several related rare subtypes), but current support is limited to **5 preclinical/in vitro publications** — no clinical trials exist for any of the predicted melanoma indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Myeloma (based on known drug classification; Malaysia label indication text was not retrievable from this evidence pack — see Data Gaps) |
| Predicted New Indication | Melanoma |
| TxGNN Prediction Score | 99.03% (melanoma); related melanoma subtype predictions score up to 99.37% (CMM7) |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for carfilzomib is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological classification, carfilzomib is an irreversible second-generation proteasome inhibitor: it blocks the 26S proteasome, preventing degradation of pro-apoptotic regulators and disrupting NF-κB pathway activation. This mechanism underlies its efficacy in multiple myeloma, a malignancy that is highly dependent on proteasome function for plasma cell survival.

The predicted new indication, melanoma, is mechanistically distinct (solid tumor vs. hematologic malignancy), but preclinical work suggests the same proteasome/NF-κB axis is relevant in melanoma cell biology. In vitro data show carfilzomib (alone or combined with bortezomib) induces apoptosis in B16-F1 melanoma cells via caspase 3/8/9/12 activation, and related mechanistic studies (E3-ligase cIAP2 regulation, NF-κB-driven heparanase expression, BET-protein degradation) support a plausible — though not yet clinically tested — role for proteasome inhibition in melanoma.

TxGNN additionally surfaced four rare melanoma subtypes (CMM7, pediatric leptomeningeal melanoma, epithelioid uveal melanoma, vulvar melanoma) with even higher prediction scores than generic melanoma, but **none of these subtypes have any supporting clinical trial or literature evidence** — they represent pure knowledge-graph extrapolation and are separately scored L5/Hold. Several also carry specific mechanistic concerns (e.g., limited CNS/blood-brain-barrier penetration for the pediatric leptomeningeal case, differing driver mutations for uveal and vulvar/mucosal subtypes), so they should not be treated as validated leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for melanoma or any of the predicted subtypes: CMM7, pediatric leptomeningeal melanoma, epithelioid uveal melanoma, vulvar melanoma).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro/Preclinical | Biology | Carfilzomib + bortezomib induced apoptosis in B16-F1 melanoma cells via caspase 3/8/9/12 activation |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico (molecular docking/simulation) | J Biomol Struct Dyn | Docking/dynamics screening of clinical drugs across 10 cancer types (incl. melanoma) against 18 kinase targets |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | In vitro/Mechanistic | Mol Cancer Res | ZFAND2A (AIRAP) regulates melanoma cell survival via E3-ligase cIAP2, implicating proteotoxic-stress pathways relevant to proteasome inhibition |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | In vitro/Preclinical (PROTAC) | Leukemia | BET-targeting PROTACs active in preclinical multiple myeloma models — myeloma-context evidence supporting the shared proteasomal-degradation pathway, not direct melanoma data |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | In vitro/Preclinical | Matrix Biology | Bortezomib and carfilzomib activate NF-κB, triggering heparanase expression in myeloma cells — myeloma-context evidence, not direct melanoma data |

---

## Malaysia Market Information

Malaysia (NPRA) records show carfilzomib as marketed with **2 active registrations**. However, this evidence pack did not return product-level details (license number, product name, dosage form, or approved indication text) for either registration — these fields are blank in the source data and are not fabricated here.

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent (proteasome inhibitor class, oncology indication).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (second-generation proteasome inhibitor) |
| Myelosuppression Risk | Moderate–High (thrombocytopenia and lymphopenia are class-recognized effects of proteasome inhibitors); specific incidence data not available in this evidence pack |
| Emetogenicity Classification | Low to Moderate (proteasome inhibitor class) |
| Monitoring Items | CBC with differential, renal function, electrolytes, cardiac/pulmonary status (proteasome inhibitor class carries a cardiotoxicity signal) |
| Handling Protection | Cytotoxic/hazardous drug handling precautions apply; institution-specific NPRA handling requirements were not available in this evidence pack |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were flagged as data gaps in this evidence pack; the DDI query returned no records.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for melanoma (and all four related subtype predictions) is limited entirely to in vitro, mechanistic, and in silico studies — there are zero clinical trials or patient-level data. This is compounded by a Blocking-severity data gap on Malaysia label warnings/contraindications, which prevents even an initial safety assessment.

**To proceed, the following is needed:**
- TFDA/NPRA package insert — warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action / drug classification from DrugBank (DG002)
- Malaysia label original indication text and full registration details (currently blank in source data)
- In vivo/animal efficacy data or early-phase clinical evidence in melanoma before advancing beyond the current preclinical hypothesis
- Completed DDI screening (currently not_found, 0 records)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

