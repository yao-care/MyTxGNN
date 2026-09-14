---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab (DrugBank DB14004) is an anti-IL-23p19 monoclonal antibody whose approved use targets IL-23-driven inflammatory skin disease (plaque psoriasis); Malaysia-specific indication text was not populated in this evidence pack. The TxGNN model predicts possible activity in **Severe Nonproliferative Diabetic Retinopathy**, but this direction currently has **zero clinical trials** and **zero publications** — it is a pure knowledge-graph inference with no direct supporting study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in the Malaysia (NPRA) license record provided; tildrakizumab's known global indication is moderate-to-severe plaque psoriasis |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is not available from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on the drug class and the mechanistic notes attached to this candidate set, tildrakizumab is a monoclonal antibody that binds the p19 subunit of IL-23, blocking downstream Th17 cell differentiation and IL-17A secretion — the pathway underlying its proven efficacy in plaque psoriasis.

The link to diabetic retinopathy is indirect and cross-species: published models suggest IL-17A, acting through retinal Müller cells, contributes to retinal ganglion cell injury, and that the IL-17A/RORγt axis drives retinal inflammation and microvascular degeneration in diabetic animal models. This candidate (severe nonproliferative diabetic retinopathy) is a TxGNN extrapolation of the broader diabetic-retinopathy prediction to a more specific disease stage — the mechanistic strength is identical to the general DR prediction, but no data exists for this severity stratum specifically.

Whether a systemically administered anti-IL-23 antibody achieves meaningful penetration into retinal tissue, and whether suppressing IL-17A is protective or harmful in this context, is unresolved — some literature reports a neuroprotective role for IL-17A, meaning the mechanistic rationale is directionally plausible but unproven and not without controversy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

NPRA records confirm 1 active registration for this product, but the license number, product name, dosage form, manufacturer, and approved-indication text fields were not populated in this evidence extract, so authorization details cannot be tabulated here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications for this drug (including this top-ranked candidate) sit at decision stage S0 with Evidence Level L5 — model prediction only. Searches across ClinicalTrials.gov, ICTRP, and PubMed returned zero results for tildrakizumab in any of the four predicted diabetic/ophthalmic/bone indications, so there is no clinical or preclinical signal to act on yet.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap — required before any safety pre-screen)
- Confirmed mechanism-of-action data via DrugBank API (currently a High-severity gap)
- Preclinical studies directly linking the IL-23/Th17/IL-17A axis to diabetic retinopathy progression (not just general retinal inflammation models)
- Completed Malaysia license details (product name, dosage form, approved indication text) to establish the true original-indication baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

