---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 2
---

# Carbetocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Carbetocin: From Postpartum Hemorrhage Prevention to Isotretinoin-like Syndrome

## One-Sentence Summary

Carbetocin is a long-acting oxytocin receptor agonist known clinically for preventing postpartum hemorrhage and uterine atony. The TxGNN model predicts it may be effective for **isotretinoin-like syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags this as a likely model-noise candidate rather than a credible repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postpartum hemorrhage / uterine atony prevention (from known drug background; official Malaysia label indication text is not available in this dataset) |
| Predicted New Indication | Isotretinoin-like syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is a data gap). Based on known information, carbetocin is a long-acting oxytocin receptor agonist whose efficacy in preventing postpartum hemorrhage and uterine atony is well established. No mechanistic pathway connects oxytocin receptor agonism to "isotretinoin-like syndrome" — this is not a standard disease term, and even under the closest plausible interpretation (retinoic acid embryopathy-type fetal malformation syndrome), there is no known pharmacological link to oxytocin signaling.

The evidence pack's own rationale explicitly characterizes this as a **pure score-driven artifact (score 0.991, rank 11018)** with no mechanistic or literature support, and flags it as a likely knowledge-graph noise candidate. A second top-ranked prediction for this drug, Goodman syndrome (score 99.06%), carries the identical profile — zero trials, zero literature, no plausible mechanistic link, evidence level L5, recommendation Hold — suggesting a systemic issue with disease-node mapping for this drug rather than two independent genuine signals.

Given the missing MOA data and the complete absence of corroborating evidence, this prediction should not be treated as a credible repurposing hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Malaysia (NPRA) records show carbetocin has **2 active registrations**, but detailed authorization data (license numbers, product names, dosage forms, approved indication text) is not available in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both top-ranked TxGNN predictions for carbetocin (isotretinoin-like syndrome, Goodman syndrome) lack any mechanistic rationale, clinical trial evidence, or literature support, and the source data itself assesses these as likely model noise rather than genuine repurposing signals. Original MOA and safety label data are also missing, blocking progression to safety evaluation (S1).

**To proceed, the following is needed:**
- Mechanism of action data (DG002, High severity) to enable any mechanistic-relevance check
- TFDA/NPRA label warnings and contraindications (DG001, Blocking) required before any S1 safety evaluation
- Malaysia license detail fields (license number, product name, dosage form, approved indication text) currently empty in the registry extract
- Clarification/validation of the disease terms "isotretinoin-like syndrome" and "Goodman syndrome" as mapped in the knowledge graph, since neither is a standard indication and both may reflect node mislabeling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

