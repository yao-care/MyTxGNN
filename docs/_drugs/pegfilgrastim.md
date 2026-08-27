---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
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

# Pegfilgrastim: From Febrile Neutropenia Prophylaxis to Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a PEGylated G-CSF analog, generally used to reduce the risk of infection (febrile neutropenia) in patients receiving myelosuppressive chemotherapy. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but currently **no clinical trials and no literature** support this direction — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of chemotherapy-induced febrile neutropenia (general drug knowledge; Malaysia-specific label indication text is not available in this evidence pack) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for pegfilgrastim in this evidence pack. Based on known pharmacology, pegfilgrastim is a PEGylated granulocyte colony-stimulating factor (G-CSF) analog that stimulates proliferation and differentiation of bone marrow granulocyte precursors and mobilizes neutrophils, and its efficacy in preventing chemotherapy-induced neutropenia is well established.

The proposed link to diabetic retinopathy is indirect and speculative. Diabetic retinopathy's core pathology is chronic hyperglycemia-driven retinal microvascular injury, with ischemia-induced VEGF elevation driving neovascularization. There is no known direct pharmacological overlap with G-CSF signaling. G-CSF is known to mobilize endothelial progenitor cells (EPCs), which offers a theoretical, indirect connection to vascular repair/neovascularization in ischemic tissue — but the direction of this effect (protective vs. potentially worsening neovascularization) is unclear, and this link is not a validated mechanism.

Because the original MOA data field itself is a data gap and no clinical or literature evidence exists, this prediction should be treated as a TxGNN model score only (>0.99), not as a mechanistically or clinically substantiated hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Malaysia has 4 registered pegfilgrastim products (market status: Marketed), but detailed license information (registration number, product name, dosage form, approved indication text) is not available in the current evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (severe nonproliferative diabetic retinopathy) has no supporting clinical trials or literature, and the proposed mechanistic link (G-CSF-mediated endothelial progenitor cell mobilization) is speculative with uncertain directionality. This is an L5, model-score-only prediction and does not meet the threshold for further evaluation.

**To proceed, the following is needed:**
- Original mechanism of action (MOA) data for pegfilgrastim (currently a data gap)
- TFDA/NPRA label warnings and contraindications (currently a data gap, flagged as Blocking)
- Detailed Malaysia license information (product names, dosage forms, approved indication text)
- Preclinical or mechanistic studies specifically linking G-CSF pathway activity to diabetic retinopathy progression or regression, to justify moving beyond model prediction alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

