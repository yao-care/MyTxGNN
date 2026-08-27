---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Etoricoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Etoricoxib: From Inflammatory Pain Conditions to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor NSAID, generally used for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, acute gout and other inflammatory pain conditions (exact NPRA-approved indication text is not available in the current data extract).
The TxGNN model predicts it may be effective for **Migraine Disorder**, but this is currently a **pure model prediction with 0 clinical trials and 0 publications** directly supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from source data (NPRA license indication text is empty; see Data Gap DG001/DG002) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 79 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, etoricoxib is a selective cyclooxygenase-2 (COX-2) inhibitor that reduces prostaglandin synthesis, and it is marketed for inflammatory and pain-related conditions. This is class-level, not drug-specific, background information — it is not extracted from the NPRA license data in this Evidence Pack, which currently contains no indication text.

NSAID/COX-2 inhibition is a recognized pharmacological class effect in acute migraine treatment, since prostaglandin-mediated neurovascular inflammation contributes to migraine pathophysiology. This is the basis for the TxGNN model's high similarity score (99.90%) between etoricoxib and migraine disorder.

However, this mechanistic link is purely inferred from knowledge-graph pharmacological-class similarity — there is **no etoricoxib-specific clinical trial or publication** supporting its use in migraine. Among the model's other predictions for related headache conditions, only "headache disorder" (rank 9) and "trigeminal autonomic cephalalgia" (rank 10) are backed by actual case-level literature (indomethacin-responsive headache syndromes where etoricoxib was used as an indomethacin substitute), and even that evidence does not extend to migraine disorder specifically. The top-ranked prediction in this pack — migraine disorder — has zero direct evidence and should be read as the weakest-supported of the migraine-related candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA package insert warnings and contraindications are flagged as a Blocking data gap (DG001) — this data must be obtained before any safety pre-assessment (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but evidence level is L5 — a pure TxGNN model prediction with no supporting clinical trials or literature specific to etoricoxib in migraine. There is no basis to advance this candidate beyond a research hypothesis at this stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank (DG002)
- Etoricoxib-specific migraine trial or publication search, or a formal literature review of NSAID/COX-2 inhibitors in migraine treatment
- If pursuing headache-spectrum indications instead, consider re-scoring "headache disorder" and "trigeminal autonomic cephalalgia" (ranks 9–10), which have case-level literature support that migraine disorder itself lacks
- Original (approved) indication text from NPRA licensing data, currently blank in the source extract
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

