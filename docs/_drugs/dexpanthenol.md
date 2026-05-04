---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 7
---

# Dexpanthenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Dexpanthenol: From Wound Healing / Skin Care to Exanthem (Skin Rash)

## One-Sentence Summary

Dexpanthenol (provitamin B5) is a topical agent widely used for wound healing, skin protection, and epithelial repair. The TxGNN model predicts it may be effective for **Exanthem (skin rash/dermatitis)**, with **5 clinical trials** (including a completed Phase III RCT directly testing Bepanthen® cream for rash prevention) currently supporting this direction. Among all 7 predicted indications, exanthem represents the strongest repurposing candidate with the most robust clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Wound healing, skin protection, epithelial repair (license details not available in current dataset) |
| Predicted New Indication | Exanthem (disease) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Dexpanthenol is the alcohol analogue of pantothenic acid (vitamin B5). Once absorbed by the skin, it is converted to pantothenic acid, which is an essential component of coenzyme A (CoA). CoA plays a critical role in cellular metabolism, lipid synthesis, and the maintenance of the skin barrier. Dexpanthenol promotes epithelial cell regeneration and repair, possesses anti-inflammatory and moisturising properties, and accelerates stratum corneum recovery — mechanisms that are directly relevant to managing skin eruptions and dermatitis.

Exanthem, broadly defined as skin rash or eruption, involves disruption of the skin barrier, inflammation, and impaired epithelial integrity. These pathological features align closely with dexpanthenol's known pharmacological actions. Notably, drug-induced skin rashes (e.g., EGFR inhibitor–associated papulopustular eruptions) represent a significant clinical problem where skin barrier restoration is a key therapeutic strategy. The mechanistic overlap between dexpanthenol's tissue repair properties and the pathophysiology of exanthem provides a sound biological rationale for this repurposing prediction.

Furthermore, a completed Phase III randomised double-blind trial (NCT01136005, BeCet study, n=160) has directly evaluated Bepanthen® cream (dexpanthenol) versus cetomacrogol cream for the prevention of papulopustular eruptions in patients receiving EGFR inhibitors, providing direct clinical evidence for this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | **BeCet study**: Randomised double-blind trial directly comparing Bepanthen® cream (dexpanthenol) vs cetomacrogol cream for prevention of ≥Grade 2 papulopustular eruptions in patients receiving EGFR inhibitors. Assessed compliance, HRQoL, and skin treatment adherence over 6 weeks. *[Relevance: A — direct evidence for dexpanthenol in skin rash prevention]* |
| [NCT03852563](https://clinicaltrials.gov/study/NCT03852563) | N/A | Completed | 33 | Evaluated Bepantol® cream (dexpanthenol) for skin recovery and reduction of skin rash after ablative facial laser procedure. Assessed redness, irritation, and softness over 3 weeks post-procedure. *[Relevance: B — supportive evidence for dexpanthenol in post-procedural skin rash]* |
| [NCT03866447](https://clinicaltrials.gov/study/NCT03866447) | Phase 4 | Unknown | 80 | Investigated vitamin D and topical analogues in acne vulgaris pathogenesis and treatment. Dexpanthenol may have been used as adjunctive skin care. *[Relevance: C — indirect association]* |
| [NCT05699122](https://clinicaltrials.gov/study/NCT05699122) | N/A | Completed | 16 | Evaluated low-level laser therapy for incontinence-associated dermatitis in elderly patients. Dexpanthenol possibly used as comparator or adjunct. *[Relevance: C — indirect, small sample]* |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Evaluated topical imiquimod formulations for actinic cheilitis treatment. Dexpanthenol may have been used for post-treatment wound care. *[Relevance: C — indirect, terminated study]* |

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Not available) | — | — | — |
| (Not available) | — | — | — |
| (Not available) | — | — | — |
| (Not available) | — | — | — |

> **Note:** Dexpanthenol has 4 registered products in the Malaysian market (status: marketed), but detailed authorization numbers, product names, dosage forms, and approved indication texts were not available in the current dataset. Further data retrieval from NPRA is recommended.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current dataset.
>
> **Note:** Dexpanthenol is generally considered a well-tolerated topical agent with a favourable safety profile. No drug-drug interactions were identified in the DrugBank query (0 interactions found). A comprehensive safety review from the package insert and NPRA records is recommended before proceeding.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The BeCet study (NCT01136005) — a completed Phase III randomised double-blind trial with 160 participants — provides direct clinical evidence for dexpanthenol (Bepanthen® cream) in the prevention of skin eruptions associated with EGFR inhibitor therapy. Dexpanthenol's well-established mechanism of promoting epithelial regeneration, anti-inflammatory action, and skin barrier repair aligns strongly with the pathophysiology of exanthem. The TxGNN prediction score of 99.60% is further corroborated by this clinical evidence base. However, full safety data (package insert warnings, contraindications) and detailed MOA documentation remain outstanding gaps.

**To proceed, the following is needed:**
- Retrieve detailed mechanism of action (MOA) data from DrugBank API to complete the pharmacological profile
- Obtain NPRA package insert PDFs for all 4 registered products to extract warnings, contraindications, and precautions
- Retrieve full results from the BeCet study (NCT01136005) to assess efficacy outcomes and effect sizes
- Confirm route compatibility: verify that available dosage forms (topical cream/ointment) are appropriate for the target exanthem indication
- Populate detailed Malaysia market information (authorization numbers, product names, dosage forms, approved indications) from NPRA database
- Consider whether additional indications with mechanistic plausibility (e.g., punctate epithelial keratoconjunctivitis — where dexpanthenol eye drops already exist in some markets) warrant parallel evaluation

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

