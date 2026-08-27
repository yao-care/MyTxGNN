---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline-class antibiotic, and detailed original indication text from Malaysia's regulatory data was not available in this evidence pack.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
but currently **no clinical trials and no published literature** support this specific direction — this is a pure model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA license text (Doxycycline is generally used for bacterial infections) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 32 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Doxycycline is a tetracycline-class broad-spectrum antibiotic, its efficacy in treating bacterial infections has been proven, and it is separately known to have anti-matrix-metalloproteinase (MMP) and anti-inflammatory properties.

For this specific predicted indication — punctate epithelial keratoconjunctivitis — no clinical trial or literature evidence was retrieved. The only mechanistic rationale available is indirect: Doxycycline's known MMP-inhibitory and anti-inflammatory effects are already used clinically in other ocular surface diseases (e.g., ocular rosacea, meibomian gland dysfunction), which suggests a plausible but unverified pathway for punctate epithelial keratoconjunctivitis.

This remains a pure model-level (TxGNN) prediction. Targeted literature searches and a preliminary safety assessment are needed before this candidate can advance beyond the hypothesis stage.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-level (model prediction only) candidate with zero supporting clinical trials or literature, and safety data (warnings, contraindications, DDI) is entirely unavailable — including a Blocking-severity data gap on TFDA/NPRA label warnings. There is not enough evidence to proceed to safety review.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap — required before any S1 safety screening)
- DrugBank mechanism of action (MOA) data
- Targeted literature/preclinical search specifically on doxycycline in punctate epithelial keratoconjunctivitis or related ocular surface disease
- Malaysia license-level detail (product name, dosage form, approved indication text) — not available in current evidence pack despite 32 registered licenses

---
**Supplementary note:** This evidence pack contains other TxGNN-predicted indications for Doxycycline with substantially stronger evidence than the top-ranked candidate above — notably **trachoma** (rank 2, L2/S3, "Proceed with Guardrails", 20 literature citations including RCTs and a Cochrane review) and **post-infectious syndrome** (rank 6, includes a completed Phase 4 RCT — the Qure Study — directly testing doxycycline for Q-fever fatigue syndrome). If the goal is to identify the most actionable repurposing candidate rather than strictly the top TxGNN score, trachoma is worth a separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

