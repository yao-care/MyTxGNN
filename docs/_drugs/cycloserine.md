---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 7
---

# Cycloserine
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

# Cycloserine: From Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line anti-tuberculosis agent that inhibits alanine racemase/D-alanine ligase and also acts as a partial agonist at the NMDA receptor glycine site. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on knowledge-graph similarity rather than direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (second-line anti-TB agent) — no formal TFDA indication text was extracted in this evidence pack |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.95% (graph rank 1184) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned by DrugBank in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes captured alongside the prediction, cycloserine inhibits alanine racemase and D-alanine ligase — enzymes bacteria use for cell-wall synthesis — which underlies its anti-tuberculosis effect. It also has a secondary, off-target action as a partial agonist at the NMDA receptor's glycine site, a property more commonly discussed in its CNS toxicity profile than in any therapeutic context.

Tuberculosis and IBS are unrelated conditions with no shared organ system or established pharmacological link. The theoretical bridge TxGNN may be drawing on is the gut-brain axis, where NMDA/glutamate receptor signaling has some role in visceral hypersensitivity and gut motility regulation. However, this is a mechanistic hypothesis only — no direct study has examined cycloserine's effect on intestinal motility or visceral pain, and the connection should be treated as speculative graph-embedding similarity rather than a validated pharmacological rationale.

Given cycloserine's well-documented CNS toxicity (seizures, psychiatric symptoms) at doses used for TB treatment, any exploration of this indication would need to address a fundamentally different risk-benefit calculus than its current use in a serious infectious disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

A registration record exists (1 license on file), but product name, dosage form, manufacturer, and approved indication text were not populated in this evidence pack — these fields need to be re-extracted from the source registry before market details can be reported.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: warning and contraindication data for cycloserine were not available from TFDA in this evidence pack — this is flagged as a Blocking gap and must be resolved before any clinical safety assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's graph-embedding score (L5) with no clinical trials, no literature, and no mechanistic study directly linking cycloserine to IBS. Combined with a Blocking gap on TFDA warnings/contraindications, there is not yet enough information to move this candidate past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to close the Blocking safety gap
- DrugBank-confirmed mechanism of action to validate the gut-brain axis hypothesis
- Preclinical or mechanistic studies on cycloserine's effect on gut motility/visceral sensitivity
- Reassessment of risk-benefit given cycloserine's known CNS toxicity profile relative to IBS as a non-life-threatening condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

