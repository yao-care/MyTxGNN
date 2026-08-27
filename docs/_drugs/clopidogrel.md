---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 8
---

# Clopidogrel
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

# Clopidogrel: From Antiplatelet Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

> Clopidogrel is a P2Y12 receptor antagonist used as an antiplatelet agent; its specific TFDA-approved indication text was not captured in this evidence pack.
> The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
> but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests on model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack — all TFDA licence indication texts were blank (structured extraction still pending) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 23 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data (DrugBank) was not available in this pack. Based on the mechanistic rationale accompanying the TxGNN prediction, clopidogrel is a P2Y12 receptor antagonist that inhibits platelet activation and aggregation — its established pharmacology is antiplatelet/antithrombotic action.

Migraine pathophysiology, particularly the aura component, involves cortical spreading depression and hypotheses around vascular endothelial and platelet activation. On this basis, there is a theoretical rationale for antiplatelet agents to influence attack frequency (e.g., prior observational interest in antiplatelet therapy for PFO-associated migraine). However, this link is indirect and non-causal — the evidence pack's own rationale explicitly notes it is "a theoretical inference without direct mechanistic evidence" specific to the brainstem-aura subtype.

Given the high TxGNN score (99.44%) but complete absence of clinical trial or literature support, the mechanistic plausibility should be treated as a hypothesis-generating signal only, not as validated pharmacological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Clopidogrel is registered in Malaysia with 23 total licences and an active ("已上市") market status. However, licence-level details (registration number, product name, dosage form, approved indication text) were not populated in this evidence pack extract and require follow-up retrieval from the NPRA source.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(A blocking data gap — TFDA label warnings/contraindications not yet retrieved — prevents a full safety assessment; see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 8 TxGNN-predicted indications for clopidogrel (including the top-ranked migraine with brainstem aura, score 99.44%) are Evidence Level L5 with zero supporting clinical trials or literature — the signal is model-prediction-only. In addition, a **blocking** data gap on TFDA label warnings/contraindications (DG001) prevents any safety pre-assessment (S1 stage), so no repurposing decision can proceed regardless of prediction strength.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA package insert (warnings, contraindications) — DG001, blocking
- Retrieve structured DrugBank MOA data — DG002
- Populate licence-level product/indication details for the 23 Malaysia registrations (currently all blank)
- Re-run clinical trial / literature searches periodically — current searches (as of 2026-03-27) returned zero hits across all 8 predicted indications
- If pursuing further, prioritize rheumatoid arthritis (rank 7) for mechanistic follow-up, as its rationale (platelet involvement in synovial inflammation) is comparatively stronger than the other candidates, despite currently having no trial or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

