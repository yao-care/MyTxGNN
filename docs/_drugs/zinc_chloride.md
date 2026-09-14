---
layout: default
title: Zinc Chloride
parent: 僅模型預測 (L5)
nav_order: 697
evidence_level: L5
indication_count: 3
---

# Zinc Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Zinc Chloride: From Unspecified Original Indication to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Zinc Chloride (DrugBank DB14533) is marketed in Taiwan under 3 existing licenses, but its originally approved indication and mechanism of action are not currently documented in available data. The TxGNN model predicts potential efficacy for **Severe Nonproliferative Diabetic Retinopathy**, with a very high prediction score (99.34%) but **no supporting clinical trials or literature** — this is a pure model-driven prediction at the earliest evidence stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (no approved indication text on file) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Taiwan Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Zinc Chloride is not currently available. Based on general pharmacological knowledge, zinc functions as a cofactor for numerous metalloenzymes and plays a role in oxidative stress regulation — both of which are theoretically relevant to the pathophysiology of diabetic retinopathy. However, this theoretical link has not been substantiated by any animal or human studies specific to zinc chloride and severe NPDR.

The TxGNN model assigned this indication its highest-ranked prediction score, but the complete absence of clinical trials or published literature means the mechanistic rationale remains speculative. This candidate should be treated as a hypothesis-generating signal rather than an evidence-supported repurposing opportunity at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Zinc Chloride currently holds 3 marketed licenses in Taiwan (市場狀態: 已上市); however, structured details such as license numbers, product names, dosage forms, and approved indication text are not yet available in the evidence pack and require retrieval from TFDA records.

---

## Safety Considerations

Please refer to the package insert for safety information. Warning, contraindication, and drug-interaction data have not yet been retrieved from the TFDA product label (flagged as a blocking data gap — DG001).

---

## Additional Predicted Indications (Lower Priority, for Context)

Two other candidates from the same prediction set carry different evidence profiles worth noting for future prioritization:

| Rank | Indication | TxGNN Score | Evidence Level | Notes |
|------|-----------|-------------|-----------------|-------|
| 2 | Sjögren Syndrome | 99.18% | L5 | No trials/literature; mucosal-repair analogy only |
| 3 | Dry Eye Syndrome | 99.18% | L2 | 2 completed trials (NCT02951910 Phase 4, NCT01541891 Phase 2) involving zinc-containing ophthalmic formulations, though not zinc chloride alone |

Rank 3 (dry eye syndrome) has meaningfully stronger evidence than the top-ranked indication and may warrant separate evaluation if this drug's repurposing pathway is pursued further.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (severe NPDR) is supported only by a TxGNN model score with zero corroborating clinical trials or literature (L5). Additionally, a blocking data gap exists on TFDA label warnings/contraindications, preventing even a preliminary safety assessment (S1).

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — required before any safety-stage review
- Mechanism of action (MOA) data from DrugBank or primary literature
- Complete license/registration details (license numbers, approved indication text, dosage forms) for the 3 Taiwan marketing authorizations
- If pursuing the dry eye syndrome signal (Rank 3) instead, formulation-level confirmation that zinc chloride (not complex zinc-hyaluronate formulations) drives the observed clinical effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

