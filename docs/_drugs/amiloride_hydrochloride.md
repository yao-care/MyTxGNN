---
layout: default
title: Amiloride Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 0
---

# Amiloride Hydrochloride
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

# Amiloride Hydrochloride: Evaluation Pending — Insufficient TxGNN Prediction Data

## One-Sentence Summary

Amiloride Hydrochloride is a potassium-sparing diuretic used to treat hypertension and oedema, often prescribed in combination with thiazide diuretics to prevent drug-induced hypokalaemia.
At this stage, **no TxGNN repurposing predictions are available** for this compound, and critical data gaps in mechanism of action, safety information, and regulatory product details prevent a full evaluation from being completed.
**2 market authorizations** are registered in Malaysia confirming its commercial availability, but additional data collection is required before any repurposing analysis can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, oedema, thiazide-induced hypokalaemia prevention |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | — |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing predictions are currently available for Amiloride Hydrochloride. As a result, this section cannot present a mechanistic rationale linking an original indication to a new therapeutic target.

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Amiloride Hydrochloride belongs to the potassium-sparing diuretic class. It is understood to act on the distal nephron to reduce sodium reabsorption while preserving potassium excretion. Its efficacy in managing hypertension and fluid overload conditions has been established in clinical practice, and it is frequently co-formulated with hydrochlorothiazide.

Without TxGNN prediction output and with the current gaps in MOA, safety, and regulatory product detail, a structured mechanistic bridge to any candidate repurposing indication cannot be constructed at this time. Once the data gaps are remediated and the TxGNN pipeline is re-run, this section will be updated with a full mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication is available for evidence search.

---

## Literature Evidence

Currently no related literature available — no predicted indication is available for evidence search.

---

## Malaysia Market Information

Product-level registration details (product name, dosage form, manufacturer, approved indication) are absent from the current dataset for both authorizations. The table below reflects what is currently available:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| (Not provided) | (Not provided) | (Not provided) | (Not provided) |
| (Not provided) | (Not provided) | (Not provided) | (Not provided) |

> **Note:** 2 authorizations are confirmed as registered under "AMILORIDE HYDROCHLORIDE" in Malaysia. Full product details must be retrieved from the NPRA product search portal to complete this section.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety warnings, contraindications, and drug interaction data are currently unavailable (marked as data gaps in this Evidence Pack). Downloading and parsing the NPRA-registered product SmPC/PI is required before any safety screening can be conducted.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions have been generated for this drug, and four critical data dimensions — mechanism of action, safety warnings, contraindications, and full regulatory product details — are incomplete, making it impossible to conduct a meaningful repurposing evaluation at this time.

**To proceed, the following is needed:**

- **NPRA Package Insert**: Download and parse the SmPC/PI PDF from the NPRA portal to obtain approved indication text, safety warnings (Blocking severity — DG001), and contraindications for both registered products
- **DrugBank MOA**: Query the DrugBank API using the INN "amiloride" to retrieve the pharmacological mechanism of action and drug classification (High severity — DG002)
- **Regulatory Product Details**: Retrieve authorization number, product name, dosage form, and manufacturer for both registered licenses to complete the Malaysia market profile
- **TxGNN Re-run**: Once drug-level data is complete, re-run the TxGNN prediction pipeline to generate repurposing candidates and trigger evidence collection (ClinicalTrials.gov, PubMed)
- **DDI Screening**: Re-query drug interaction databases after DrugBank ID is confirmed to complete the safety profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

