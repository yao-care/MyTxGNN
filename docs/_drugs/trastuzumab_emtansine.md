---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 664
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Normal Breast-like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate approved for HER2-positive breast cancer. TxGNN's top-ranked prediction for this drug is **Normal Breast-like Subtype of Breast Carcinoma**, but this direction is currently supported by only **1 clinical trial (indirect relevance)** and **0 publications**. This evidence pack also contains three related breast-cancer-subtype predictions with substantially stronger evidence (see "Related Predictions" below), which should be considered alongside the top-ranked candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (confirmed via clinical trial descriptions in evidence pack; NPRA indication text not retrieved — see data gap) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

### Related TxGNN Predictions for This Drug

This evidence pack contains four related breast-cancer-subtype predictions for trastuzumab emtansine. Since scores are nearly identical, evidence strength — not TxGNN rank — should drive triage:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Normal breast-like subtype of breast carcinoma | 99.82% | L4 | Hold |
| 2 | Progesterone-receptor positive breast cancer | 99.82% | L3 | Research Question |
| 3 | Progesterone-receptor negative breast cancer | 99.82% | **L1** | **Proceed with Guardrails** |
| 4 | Breast tumor, luminal A or B | 99.81% | L2 | Research Question |

**Note:** Rank 3 (PR-negative breast cancer) has the strongest evidence (2 pivotal Phase 3 trials: EMILIA/NCT00829166, MARIANNE/NCT01120184), but its own rationale flags that this is effectively a biomarker subgroup of the *already-approved* HER2-positive breast cancer indication, not a genuinely new indication. Rank 1, the subject of this report, is the weakest and most mechanistically uncertain of the four.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trastuzumab emtansine was not retrieved in this evidence pack (Data Gap). Based on information available in the accompanying clinical trial records, trastuzumab emtansine is an antibody-drug conjugate combining trastuzumab (an anti-HER2 monoclonal antibody) with the cytotoxic microtubule inhibitor DM1/mertansine (referred to as "Trastuzumab-Mcc-DM1" in earlier trials such as NCT00679211 and NCT00829166). Its efficacy is well established in HER2-positive breast cancer, where HER2 overexpression drives receptor-mediated internalization and intracellular release of the cytotoxic payload.

"Normal breast-like" is a PAM50 intrinsic molecular subtype defined by gene-expression profiling resembling normal breast tissue; it is not defined by HER2 overexpression, and per the model's own rationale, no literature currently supports that this subtype responds specifically to T-DM1.

Mechanistically, this weakens the case for extending T-DM1 to the normal-like subtype: T-DM1's activity depends on HER2 target expression, and this subtype's biological definition does not entail HER2 positivity. The single supporting trial in this pack (NCT06348134) was graded "C" relevance — it studies anti-HER2 therapy broadly in a HER2-positive Nigerian cohort, not the normal-like subtype specifically.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Evaluates efficacy/safety of optimal neoadjuvant-to-adjuvant anti-HER2 therapy in Nigerian women with HER2+ breast cancer; does not specifically target the normal-like subtype (Grade C relevance). |

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Detailed NPRA registration records (license numbers, product names, dosage forms, indication text) were not retrieved in this evidence pack for any of the 6 registered licenses — this is a blocking data gap (DG001). Only the aggregate status is confirmed: **6 licenses registered, market status ✓ Marketed**.

## Cytotoxicity

Trastuzumab emtansine is an antineoplastic agent (approved for breast cancer; antibody-drug conjugate class).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-targeted antibody-drug conjugate delivering the cytotoxic maytansinoid payload DM1/mertansine) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As an antibody-drug conjugate with a cytotoxic payload, handling should follow institutional cytotoxic/hazardous drug protocols; refer to the package insert for specifics |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (normal breast-like subtype) has only one indirectly relevant Phase 2 trial and no supporting literature, and its own mechanistic rationale notes the subtype is not HER2-defined, weakening the biological case for T-DM1 activity there.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently blocking (DG001)
- Detailed mechanism-of-action data (DG002)
- Complete NPRA license records (product names, dosage forms, approved indication text) for the 6 registered products
- Literature or trial evidence specifically evaluating T-DM1 in PAM50 normal-like breast cancer
- Separately, consider evaluating Rank 3 (PR-negative breast cancer, L1 evidence) as a distinct, better-supported candidate — while noting it may represent a subgroup of the existing approved indication rather than a novel use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

