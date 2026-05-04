---
layout: default
title: Bortezomib Monohydrate
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 0
---

# Bortezomib Monohydrate
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

# Bortezomib: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bortezomib is a proteasome inhibitor originally approved for the treatment of multiple myeloma and mantle cell lymphoma. The current Evidence Pack contains **no TxGNN predicted indications**, and critical data gaps exist in regulatory details, mechanism of action, and safety information. This report serves as a **baseline assessment** pending data supplementation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma, mantle cell lymphoma (registry details unavailable in current dataset) |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions or supporting studies in this pack) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the Evidence Pack does not contain any TxGNN-predicted new indications for Bortezomib. Therefore, mechanistic plausibility analysis cannot be performed at this time.

Based on established medical knowledge, Bortezomib (brand name: Velcade) is a reversible inhibitor of the 26S proteasome. It blocks the ubiquitin-proteasome pathway, leading to accumulation of pro-apoptotic proteins, cell cycle arrest, and apoptosis preferentially in malignant cells. This mechanism has been validated in multiple myeloma and mantle cell lymphoma.

The proteasome inhibition pathway has theoretical relevance to other conditions involving NF-κB signalling, protein homeostasis, or immune dysregulation. However, without specific TxGNN predictions in this Evidence Pack, no candidate indications can be evaluated. The `predicted_indications` array is empty, and this report should be revisited once predictions are generated.

---

## Clinical Trial Evidence

Currently no predicted indication is available to query clinical trial evidence against.

---

## Literature Evidence

Currently no predicted indication is available to query literature evidence against.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Not provided) | (Not provided) | (Not provided) | (Not provided) |

> **Note:** The NPRA query returned 1 registration record, but the licence details (authorization number, product name, dosage form, approved indication text) are all empty in the current dataset. Data supplementation from the NPRA database is required.

---

## Cytotoxicity

Bortezomib is an antineoplastic agent (proteasome inhibitor class). This section is applicable.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Proteasome inhibitor) |
| Myelosuppression Risk | **High** — Thrombocytopenia is the dose-limiting toxicity (cyclical pattern, nadir ~Day 11, recovery by Day 21); neutropenia is also common |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelet count (before each dose), liver function (AST/ALT/bilirubin), renal function (CrCl), blood glucose, signs of peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations; use appropriate PPE during reconstitution and administration |

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> The current Evidence Pack does not contain key warnings, contraindications, or drug interaction data for Bortezomib (all flagged as Data Gaps). The following are well-established safety concerns based on published prescribing information and should be confirmed with the local package insert:
>
> - **Peripheral neuropathy** (dose-limiting; requires dose modification)
> - **Thrombocytopenia** (cyclical; monitor platelet counts)
> - **Hypotension**, including orthostatic hypotension
> - **Cardiac disorders** (acute heart failure, QT prolongation)
> - **Pulmonary toxicity** (rare but serious)
> - **Hepatotoxicity**
> - **Tumour lysis syndrome**
> - **Herpes zoster reactivation** (antiviral prophylaxis recommended)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is incomplete — there are no TxGNN-predicted indications to evaluate, and critical data fields (DrugBank ID, MOA, regulatory licence details, safety warnings) are missing. A meaningful repurposing assessment cannot be conducted until these gaps are resolved.

**To proceed, the following is needed:**

1. **DrugBank ID mapping** — Bortezomib should map to DrugBank ID `DB00188`; re-run the DrugBank mapper with the corrected INN ("bortezomib" without "monohydrate" suffix)
2. **TxGNN prediction execution** — Run the KG and/or DL prediction pipeline for Bortezomib to generate candidate indications
3. **NPRA licence detail enrichment** — Retrieve full registration data (authorization number, product name, dosage form, approved indication text) from the NPRA database
4. **Safety data collection** — Download and parse the local package insert to populate key warnings, contraindications, and drug interactions
5. **MOA data retrieval** — Query DrugBank API for detailed mechanism of action (proteasome inhibition pathway, pharmacodynamics)
6. **Evidence collection** — Once predicted indications are available, run ClinicalTrials.gov, PubMed, and ICTRP collectors for supporting evidence

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

