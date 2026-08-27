---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Ocrelizumab is an anti-CD20 monoclonal antibody used to deplete CD20-positive B lymphocytes, with multiple sclerosis noted as its established indication.
> The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
> but currently **no clinical trials and no published literature** support this specific prediction — the signal is based on model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (per mechanistic rationale notes; NPRA license indication text is currently blank — data gap) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Malaysia Market Status | Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ocrelizumab's mechanism of action is anti-CD20 monoclonal antibody binding, which depletes CD20-positive B lymphocytes. This mechanism underlies its established use in multiple sclerosis, where B-cell-mediated autoimmune activity contributes to disease progression.

HER2-positive breast carcinoma biology, in contrast, is driven by HER2/neu receptor overexpression and downstream tyrosine kinase signaling — a pathway with no direct biological connection to B-cell depletion. There is no established pharmacological link between clearing CD20+ B cells and controlling HER2-driven tumor growth.

Given this, the high TxGNN score (99.89%) most likely reflects indirect node proximity within the knowledge graph (e.g., shared immune/oncology-adjacent nodes) rather than a genuine mechanistic relationship. This is consistent with the complete absence of supporting clinical trials or literature for this specific drug-disease pair.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

License detail fields (registration number, product name, dosage form, approved indication text) are currently blank in the data pack. Only the aggregate market status is confirmed: Marketed, with 1 registration on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: package insert warnings/contraindications retrieval is a blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature currently support ocrelizumab's use in HER2-positive breast carcinoma, and the underlying mechanism (CD20+ B-cell depletion) has no established biological link to HER2-driven tumor signaling. The high TxGNN score appears to reflect graph-structural proximity rather than genuine pharmacological relevance, and this candidate is additionally blocked from safety review (S1) by a missing package insert data gap.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action documentation (DG002)
- Confirmed original approved indication text from license data (currently blank)
- Any future clinical or literature evidence establishing a mechanistic link between B-cell depletion and HER2-positive breast carcinoma, should it emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

