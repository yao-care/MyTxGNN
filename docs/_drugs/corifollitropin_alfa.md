---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 8
---

# Corifollitropin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Corifollitropin Alfa: From an Unregistered Original Indication to Gastroduodenitis

## One-Sentence Summary

> Corifollitropin alfa is a long-acting recombinant FSH analog; its original approved indication is not recorded in the current Malaysia (NPRA) registration data, though its known pharmacology targets ovarian granulosa-cell FSH receptors to drive follicular development.
> The TxGNN model predicts a possible association with **Gastroduodenitis**, but **0 clinical trials** and **0 publications** currently support this direction, and the model's own mechanistic rationale flags it as a likely graph-noise artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current NPRA license data; MOA description suggests ovarian stimulation for assisted reproduction |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Corifollitropin alfa is a long-acting recombinant FSH analog that acts on ovarian granulosa-cell FSH receptors to stimulate follicular development — a mechanism referenced in the evidence pack's rationale, though a formal, structured mechanism-of-action record is not currently available for this drug.

There is no known pharmacological or pathway overlap between FSH receptor signaling and gastroduodenitis (a gastric/duodenal mucosal inflammatory condition). FSH receptor expression in gastrointestinal tissue has no established biological significance, and the model's own annotation for this candidate explicitly states the link lacks a reasonable biological basis, attributing the prediction to knowledge-graph co-morbidity or node-proximity noise rather than a genuine mechanistic signal.

The other seven candidates in this batch show the same pattern: several (migraine, migraine with brainstem aura, pulmonary hypertension) have rationale text suggesting the drug's known pharmacodynamics (acute hormonal fluctuation, OHSS-related fluid shifts) would plausibly *worsen* rather than treat the predicted condition — i.e., mechanistically inverse to the hypothesis. None of the eight candidates currently have supporting clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Two NPRA registrations exist for this drug (market status: ✓ Marketed), but license number, product name, dosage form, and approved indication text are not populated in the current dataset. This detail cannot be reported until the underlying registration record is retrieved.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA labeled warnings and contraindications are flagged as a Blocking data gap (DG001) — until resolved, this candidate cannot proceed to the S1 safety pre-screen.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or literature. The mechanistic rationale itself assesses the FSH-receptor-to-gastroduodenitis link as biologically implausible and likely a knowledge-graph noise artifact, and a Blocking data gap (missing TFDA safety data) independently prevents entry into safety pre-screening.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data — warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action record (DG002, High)
- Confirmed original approved indication(s) for this drug in the Malaysia registry
- Independent biological plausibility review before allocating further evidence-collection resources to this candidate, given the model's own rationale casts doubt on the signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

