---
layout: default
title: Trifarotene
parent: 僅模型預測 (L5)
nav_order: 669
evidence_level: L5
indication_count: 2
---

# Trifarotene
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

# Trifarotene: From Unspecified Original Indication to Elevated Plasma Zinc

## One-Sentence Summary

Trifarotene (DrugBank DB12808) is marketed in Malaysia, but its original approved indication and mechanism of action are not yet recorded in this evidence pack. The TxGNN model assigns a **99.40%** score to "Zinc, Elevated Plasma" as a candidate new indication, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic assessment flags it as likely graph-structure noise rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available records |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trifarotene is not currently available in this evidence pack, and no original indication text was returned from the Malaysia registry record on file, so a direct pharmacological bridge between the original and predicted indications cannot be established from the data provided.

The evidence pack's own mechanistic assessment is explicitly skeptical of this prediction: there is no known mechanism linking RAR-γ agonism (trifarotene's known pharmacological class) to plasma zinc concentration regulation. "Elevated plasma zinc" is a laboratory parameter rather than a disease entity, and high-scoring TxGNN predictions for this type of node are commonly attributable to knowledge-graph co-occurrence noise rather than an interpretable pharmacological pathway.

Given the absence of both mechanistic plausibility and corroborating evidence, this prediction should be treated as a low-confidence model output rather than a repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Malaysia registry (NPRA) records 1 active license for this product, but the detailed fields (license number, product name, dosage form, approved indication text) were not returned in this evidence pack and cannot be reported without fabrication.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication lacks any clinical trial or literature support, and the mechanistic rationale itself indicates the prediction is likely a knowledge-graph artifact rather than a biologically plausible signal (L5, decision stage S0).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (blocking gap, DG001) — required before any S1 safety screening can begin
- Mechanism of action data from DrugBank (DG002) — needed to properly evaluate mechanistic plausibility
- Complete license record details (product name, dosage form, approved indication text) for the Malaysia registration
- If pursuing further, re-evaluate the second-ranked candidate (pyogenic arthritis-pyoderma gangrenosum-acne syndrome, score 99.32%), which currently has no evidence or rationale assessment completed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

