---
layout: default
title: Benserazide Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 0
---

# Benserazide Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Benserazide Hydrochloride: Drug Repurposing Evaluation Report

## One-Sentence Summary

Benserazide hydrochloride is a peripheral DOPA decarboxylase inhibitor, commonly used in combination with levodopa for the treatment of Parkinson's disease. The TxGNN model **has not generated any predicted new indications** for this compound, and the evidence pack contains significant data gaps across multiple categories, preventing a meaningful repurposing assessment at this time.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (combination with levodopa) |
| Predicted New Indication | — (No prediction generated) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No studies; no model prediction available) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for benserazide hydrochloride. The `predicted_indications` array is empty, meaning the model did not identify any repurposing candidates that met the scoring threshold.

Benserazide is a peripheral aromatic L-amino acid decarboxylase (AADC) inhibitor. It does not cross the blood–brain barrier and acts by blocking the peripheral conversion of levodopa to dopamine, thereby increasing the bioavailability of levodopa in the central nervous system. It is always used as a combination product (levodopa/benserazide, marketed as Madopar®) and has limited standalone pharmacological activity.

The absence of a prediction may be attributable to several factors: (1) benserazide functions primarily as a pharmacokinetic enhancer rather than a direct therapeutic agent, making its standalone repurposing potential limited; (2) the DrugBank ID was not resolved (`drugbank_id: null`), which may have prevented proper mapping into the TxGNN knowledge graph; and (3) the mechanism of action data was not available in the evidence pack, further limiting the model's ability to draw mechanistic associations.

## Clinical Trial Evidence

Currently no predicted indication was generated, therefore no targeted clinical trial search was performed.

## Literature Evidence

Currently no predicted indication was generated, therefore no targeted literature search was performed.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *(Not available)* | *(Not available)* | *(Not available)* | *(Not available)* |

> **Note:** Three registrations were identified in the NPRA database, but the detailed license information (authorization number, product name, dosage form, and approved indication text) was not populated in the evidence pack. This represents a data gap that should be remediated by querying the NPRA database directly.

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, and drug–drug interactions) are currently unavailable in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No repurposing candidates were predicted by TxGNN for benserazide hydrochloride. Additionally, critical data gaps exist across DrugBank mapping, mechanism of action, regulatory license details, and safety information, making any repurposing assessment premature.

**To proceed, the following is needed:**
- **Resolve DrugBank ID mapping** — Query DrugBank for "benserazide" (DB00190) to enable proper knowledge graph integration
- **Populate NPRA license details** — Retrieve full registration records (authorization numbers, product names, dosage forms, approved indications) from the NPRA database
- **Obtain mechanism of action data** — Retrieve MOA from DrugBank to support mechanistic reasoning
- **Obtain safety data** — Download and parse the package insert (PIL) for key warnings, contraindications, and drug interactions
- **Re-run TxGNN prediction** — Once the DrugBank ID is resolved and the drug is properly mapped into the knowledge graph, re-execute the prediction pipeline to determine if any repurposing candidates emerge
- **Consider combination context** — Since benserazide is almost exclusively used in combination with levodopa, evaluate whether the prediction model should assess the levodopa/benserazide combination rather than benserazide alone

---

*This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

