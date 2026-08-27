---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 7
---

# Felodipine
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

# Felodipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

> Felodipine is a dihydropyridine calcium channel blocker whose repurposing rationale in this evidence pack identifies it as an established antihypertensive agent. The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5)**, but this direction is currently supported by **zero clinical trials and zero publications**, and the evidence pack's own rationale flags the score as possible knowledge-graph noise rather than a disease-specific signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from drug class per evidence pack rationale text; formal TFDA/NPRA label indication text not on file) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for felodipine in this evidence pack. Based on known information within the pack, felodipine is referenced repeatedly across other candidate rationales as "an established antihypertensive" and a dihydropyridine calcium channel blocker (CCB) that works by blocking calcium influx into vascular smooth muscle, producing vasodilation and blood pressure reduction.

For this specific candidate, however, the mechanistic link is weak. WHO Group 5 pulmonary hypertension is defined precisely by its unclear or multifactorial mechanism, and there is no established pharmacological rationale connecting dihydropyridine CCB activity to this category of disease. The evidence pack's own rationale states this directly: the TxGNN score likely reflects the broad connectivity of "hypertension"-related nodes in the knowledge graph rather than a disease-specific mechanistic relationship.

No clinical trials or literature were retrieved for felodipine against this exact indication (see query_log entries 3–5, all zero results), reinforcing that this is a model-generated hypothesis without empirical support at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Felodipine has 5 product registrations on file with NPRA (market status: Marketed), but the evidence pack does not include license numbers, product names, dosage forms, or approved-indication text for these registrations — this data needs to be retrieved from NPRA directly.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: retrieval of TFDA/NPRA label warnings and contraindications is flagged in this evidence pack as a Blocking data gap (DG001) — the drug cannot proceed to a S1 safety review until this is resolved.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has L5 evidence (model prediction only) with no supporting clinical trials or literature, and the pack's own mechanistic rationale characterizes the high TxGNN score as likely reflecting generic "hypertension" node connectivity rather than a genuine signal for this specific, mechanistically-undefined disease category.

**To proceed, the following is needed:**
- Felodipine mechanism of action data (DG002)
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review)
- Disease-specific clinical or preclinical evidence connecting dihydropyridine CCBs to WHO Group 5 pulmonary hypertension
- NPRA license details (numbers, product names, approved indication text) currently missing from the registry extract

*For reference: this same evidence pack contains other felodipine candidates with substantially stronger support — notably Prinzmetal angina (L2, 8 literature sources including 3 RCTs, "Proceed with Guardrails") — which may warrant a separate evaluation report given the mechanistic plausibility (CCB-mediated coronary vasospasm relief) and existing clinical evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

