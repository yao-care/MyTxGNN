---
layout: default
title: Amorolfine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 0
---

# Amorolfine Hydrochloride
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

# Amorolfine Hydrochloride: Antifungal Agent — No Repurposing Predictions Generated

---

## One-Sentence Summary

Amorolfine Hydrochloride is a morpholine-class antifungal agent, used topically for the treatment of onychomycosis (fungal nail infections).
The TxGNN model did not generate any new repurposing predictions for this drug in the current analysis run.
Without a target indication, no evidence evaluation can be performed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infections) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No repurposing prediction was generated for amorolfine hydrochloride in this run, so there is no mechanistic link to evaluate at this time.

Based on established pharmacology, amorolfine is a morpholine-class antifungal that inhibits two key enzymes in the ergosterol biosynthesis pathway — Δ14-reductase and Δ7-8-isomerase — leading to accumulation of abnormal sterols (primarily ignosterol) that disrupt fungal cell membrane integrity. This mechanism is highly specific to the fungal ergosterol pathway and has limited counterparts in mammalian biology, which may reduce cross-disease repurposing potential compared to systemic or receptor-modulating agents.

Detailed mechanism of action data was not returned from the DrugBank query in this Evidence Pack (DrugBank ID not mapped). A full pharmacological profile retrieval is recommended to determine whether any secondary mechanisms (e.g., anti-biofilm activity, anti-inflammatory effects) could support repurposing into non-fungal indications.

---

## Malaysia Market Information

Two product registrations are recorded with Malaysia's NPRA for amorolfine hydrochloride. However, the detailed registration records — including authorization number, product name, dosage form, and approved indication text — were not available in the current data extract.

For the complete and up-to-date product listing, please consult the NPRA Product Registration Search portal directly (https://www.npra.gov.my).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for amorolfine hydrochloride, making it impossible to evaluate evidence for a new indication. Additionally, critical data fields — including MOA, safety warnings, contraindications, and detailed registration records — are missing, preventing a meaningful safety or mechanistic assessment.

**To proceed, the following is needed:**
- Re-run the TxGNN prediction pipeline to confirm whether amorolfine hydrochloride appears as a candidate for any indication (check drug name normalisation and DrugBank ID mapping)
- Retrieve the correct DrugBank ID to populate MOA, toxicity, and drug interaction data
- Download and parse the NPRA/TFDA package insert PDF to populate key warnings and contraindications (currently blocking S1 safety assessment)
- Confirm detailed NPRA registration records (product names, dosage forms, approved indications) for the 2 registered products
- Verify whether the two NPRA registrations correspond to the same formulation (e.g., 5% nail lacquer — Loceryl) or distinct products, as this affects indication scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

