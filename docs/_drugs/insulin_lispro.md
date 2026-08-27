---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

> Insulin lispro is a rapid-acting insulin analog used for glycemic control in diabetes mellitus.
> The TxGNN model predicts a possible link to **Autoimmune Oophoritis**, but currently **no clinical trials** and **no literature** support this specific pairing, and the model's own rationale flags the association as likely driven by semantic proximity rather than a real biological mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in current data extract (drug is a known insulin therapy for diabetes mellitus; TFDA-specific label text is a data gap — see below) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for insulin lispro in this evidence pack. Based on known information, insulin lispro is a rapid-acting insulin analog used to control blood glucose in diabetes mellitus, acting via the insulin receptor to regulate glucose uptake and metabolism.

Autoimmune oophoritis is an autoimmune condition causing premature ovarian failure. It has no established direct mechanistic connection to insulin signaling. According to the evidence pack's own rationale, the high TxGNN score most likely reflects semantic clustering around "autoimmune" disease nodes in the knowledge graph — for example, autoimmune oophoritis can co-occur with Type 1 diabetes as part of autoimmune polyglandular syndrome (APS) — rather than a causal pharmacological relationship. There is no specific biological pathway connecting insulin signaling to autoimmune destruction of ovarian tissue.

Given this, the prediction should be treated as a knowledge-graph association signal rather than a mechanistically grounded repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

3 registrations are on file and the product's market status is Marketed, but the current data extract does not include license numbers, product names, dosage forms, manufacturers, or approved-indication text for these registrations — this information will need to be pulled directly from source records before market details can be reported.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications are marked as a Blocking data gap — DG001 — meaning this candidate cannot yet enter the S1 safety pre-assessment stage until that data is retrieved.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no supporting clinical trials or literature, sits at evidence level L5 (model prediction only), and the mechanistic rationale itself indicates the association is likely a knowledge-graph artifact rather than a genuine pharmacological link.

**To proceed, the following is needed:**
- Insulin lispro's mechanism of action (MOA) data (DG002)
- TFDA/NPRA package insert warnings and contraindications, required to clear the S1 safety pre-assessment gate (DG001, Blocking)
- Complete license/product details (product name, dosage form, manufacturer, approved indication text) for the 3 existing registrations
- Any preclinical or mechanistic study specifically linking insulin signaling to autoimmune oophoritis, to validate or refute the current TxGNN association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

