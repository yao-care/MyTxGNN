---
layout: default
title: Pantothenic Acid
parent: 僅模型預測 (L5)
nav_order: 533
evidence_level: L5
indication_count: 9
---

# Pantothenic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pantothenic Acid: From Nutritional Supplementation (Vitamin B5) to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (Vitamin B5, DrugBank DB01783) is generally used as a nutritional/vitamin supplement; the Evidence Pack does not contain a specific registered indication text for it in Malaysia. The TxGNN model predicts it may be effective for **Congenital Prothrombin Deficiency**, but only **1 clinical trial** and **0 publications** are currently linked to this specific indication, and that single trial is topically unrelated to the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registry data provided (all `approved_indication_text` fields are empty); pantothenic acid is generally classified as a Vitamin B5 nutritional supplement |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged in the Evidence Pack as a High-severity data gap). Based on known information, pantothenic acid is a precursor of coenzyme A (CoA) and is generally used as a nutritional/vitamin supplement rather than for a specific disease indication in this dataset.

No mechanistic pathway connecting pantothenic acid to congenital prothrombin deficiency (an inherited coagulation factor disorder) has been identified. The single clinical trial retrieved as "evidence" for this prediction actually studied a multi-ingredient dietary supplement (L-arginine, Pycnogenol, vitamin K2, alpha-lipoic acid, and B-vitamins) on endothelial function in patients with hypertension and hyperhomocysteinemia — a completely different population and endpoint. The evidence pack's own review of this trial explicitly flags it as a topical mismatch, and characterizes the overall pairing as a high-scoring but likely **false-positive** TxGNN prediction with no substantive supporting evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | NA | Completed | 25 | Randomized, double-blind, placebo-controlled crossover study of a multi-ingredient dietary supplement (L-arginine, Pycnogenol, vitamin K2, alpha-lipoic acid, B-vitamins) on endothelial function in volunteers with mild-to-moderate hypertension and hyperhomocysteinemia — not a study of pantothenic acid alone, and not related to congenital prothrombin deficiency |

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The Evidence Pack confirms pantothenic acid is marketed in Malaysia with 18 total registrations, but the underlying license records returned in this pack contain no populated fields (license number, product name, dosage form, manufacturer, and indication text are all blank). Product-level registration detail is not available from this data pull.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only indication-specific evidence retrieved (a single completed trial) is topically unrelated to congenital prothrombin deficiency, no supporting literature exists, and no mechanistic rationale links pantothenic acid to this disease. This is an L5, model-prediction-only candidate that the evidence itself suggests is a likely false positive.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank
- Product-level Malaysia registration detail (license numbers, indications, dosage forms)
- If repurposing interest continues, consider re-scoping evaluation toward **folic acid deficiency anemia** (rank 4 in this pack), which currently has stronger supporting evidence (Evidence Level L3, 4 clinical trials, 4 publications) than the top-ranked candidate above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

