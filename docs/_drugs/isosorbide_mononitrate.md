---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina Pectoris to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate is an organic nitrate (NO donor) established for angina pectoris prophylaxis. The TxGNN model's top-ranked prediction for this drug is **Hypertrichosis (disease)**, but this prediction is currently supported by **zero clinical trials and zero publications** — it is a model-score-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (prophylaxis) — general pharmacological knowledge; Malaysia-specific label indication text not yet captured in registry data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% (rank 174 among all predictions) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not yet available for this drug (flagged as a High-severity data gap). Based on general pharmacology, isosorbide mononitrate is an NO donor that acts through the NO–cGMP–sGC pathway to produce vasodilation, an effect well established in its use for angina pectoris.

For hypertrichosis specifically, no mechanistic hypothesis connects this vasodilatory pathway to hair follicle biology. The evidence pack's own rationale for this candidate states explicitly: *"無機轉假說支持，亦無任何臨床試驗或文獻證據，純屬模型預測分數"* ("no mechanistic hypothesis, and no clinical trial or literature evidence — purely a model prediction score"). Note that a related candidate in the same batch (rank 5, alopecia) drew a loose analogy to minoxidil's follicular blood-flow effect, but even that link was labeled speculative and unsupported by direct evidence — it does not extend to hypertrichosis.

Given the complete absence of supporting evidence, this candidate should be treated as an unvalidated model output rather than a substantiated repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The product is registered in Malaysia (market status: Marketed, 1 registration on file), but structured details — authorization number, product name, dosage form, and approved indication text — have not yet been extracted from source documents.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available; the missing TFDA label warnings/contraindications data is flagged as a Blocking gap that must be resolved before any safety assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hypertrichosis) has an L5 evidence level — a TxGNN score with no mechanistic hypothesis, no clinical trials, and no literature support. There is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF for warnings and contraindications (Blocking gap, DG001)
- Official MOA data via DrugBank (High-priority gap, DG002)
- A mechanistic rationale (preclinical or literature) specifically linking NO-donor activity to hair follicle/hypertrichosis biology, if this candidate is to be pursued further
- Malaysia license record details (product name, dosage form, approved indication text)

**Note:** Within the same evidence pack, a lower-ranked candidate — **pulmonary arterial hypertension** (rank 10, L3, decision stage S1, "Research Question") — has a stronger mechanistic rationale (NO–cGMP–sGC pathway is a validated PAH drug target) and 6 supporting publications. This may warrant separate evaluation as it is better substantiated than the top-ranked hit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

