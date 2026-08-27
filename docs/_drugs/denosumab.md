---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 2
---

# Denosumab
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a RANKL-targeting monoclonal antibody originally used for osteoporosis and the prevention of skeletal-related events (e.g., in bone metastases). The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, but this is currently a **pure model prediction (score 99.63%) with no supporting clinical trials or literature** identified to date.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis / skeletal-related events (globally known use — local license text not available in this data pack) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, denosumab is a fully human monoclonal antibody that inhibits RANKL (RANK ligand), thereby blocking osteoclast formation and activity; its efficacy in osteoporosis and prevention of skeletal-related events is well established and widely approved.

The link between denosumab and diabetic retinopathy rests on the RANK/RANKL/OPG signaling axis, which has been studied observationally as a biomarker pathway in diabetic vascular complications — elevated serum osteoprotegerin (OPG) has been associated with microvascular disease including retinopathy in some cohort studies. This is a **correlative biomarker association**, not an established causal or interventional mechanism, and the original indication (bone metabolism) and the predicted indication (retinal microvascular disease) are mechanistically distant beyond this shared signaling pathway.

Critically, this rationale applies to the broader category "diabetic retinopathy" (a related, lower-ranked prediction with score 99.23%, which has one real-world cohort/meta-analysis publication and one cross-sectional study, though relevance to this specific indication is still unverified). For the specific predicted indication reported here — **severe nonproliferative diabetic retinopathy** — there is no direct clinical trial or literature evidence at all; the prediction is derived purely from the TxGNN knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for severe nonproliferative diabetic retinopathy is supported only by a TxGNN knowledge-graph score (L5) with zero clinical trials or literature directly addressing this indication. In addition, a **blocking data gap** exists on local (NPRA) label warnings/contraindications, which prevents even a preliminary safety (S1) assessment.

**To proceed, the following is needed:**
- NPRA-approved package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- Verified mechanism-of-action documentation from DrugBank or equivalent (DG002)
- Targeted literature/clinical trial search for RANKL inhibition and retinal microvascular outcomes, ideally interventional rather than biomarker-association studies
- Further evaluation of the related broader indication "diabetic retinopathy" (TxGNN score 99.23%), whose existing real-world cohort data has not yet been assessed for relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

