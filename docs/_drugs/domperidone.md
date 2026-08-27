---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Domperidone: From Unspecified Original Indication to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is marketed in Malaysia under 17 registrations, but the evidence pack does not yet contain its original approved indication text or mechanism of action.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis**, with a prediction score of **99.08%**, but currently **no clinical trials and no literature** support this direction — this is a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

*(Original Indication and license details are omitted — the evidence pack's license records and `original_indications` field contain no data for this field.)*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for domperidone in this evidence pack, and no original indication text was retrieved from the Malaysia license records. As a result, no mechanistic or indication-similarity rationale can be constructed from source data at this time.

The prediction rests solely on the TxGNN knowledge-graph model's score (99.08%, rank 11,766), with no corroborating clinical trial or literature evidence yet identified. Until MOA and original indication data are retrieved, the biological plausibility of this repurposing signal cannot be independently assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has zero supporting clinical trials or literature (L5, model prediction only), and a Blocking data gap remains on TFDA warnings/contraindications, which prevents any safety pre-screening. There is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (resolve Blocking data gap DG001)
- Mechanism of action data from DrugBank (resolve data gap DG002)
- Original approved indication text from Malaysia license records
- Ongoing monitoring for new clinical trials or publications on domperidone in nephrogenic syndrome of inappropriate antidiuresis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

