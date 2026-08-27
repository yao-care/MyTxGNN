---
layout: default
title: Choline Salicylate
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Choline Salicylate
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

# Choline Salicylate: A Low-Confidence TxGNN Signal for Prinzmetal Angina

## One-Sentence Summary

> This evidence pack does not include verified original-indication data for Choline salicylate.
> The TxGNN model's top-ranked prediction is **Prinzmetal Angina**, but this is supported by
> **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale explicitly states there is no known pharmacological basis for the link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not disclosed in this evidence pack (no license indication text or original indication data available) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Choline salicylate is not available in this evidence pack. Based on rationale notes attached to other candidate indications in the same pack, Choline salicylate is a **non-acetylated salicylate**, pharmacologically related to NSAIDs (COX inhibition, analgesic/anti-inflammatory activity).

For Prinzmetal angina specifically, however, the model's own rationale is negative: Prinzmetal angina is caused by **coronary artery vasospasm**, and salicylates have no established vascular smooth-muscle antispasmodic or vasodilatory effect. The evidence pack states directly:

> "無明確機轉支持——Prinzmetal angina 為冠狀動脈痙攣所致，水楊酸鹽無已知血管平滑肌解痙作用，TxGNN 高分推測為知識圖譜間接關聯，缺乏臨床或機轉證據。"

In plain terms: the high TxGNN similarity score most likely reflects an indirect knowledge-graph association rather than a genuine pharmacological relationship. No clinical or mechanistic evidence in this pack supports the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The evidence pack confirms Choline salicylate is marketed in Malaysia under **5 registrations**, but no license-level details (registration number, product name, dosage form, approved indication text) were captured in this data pull — all license fields are blank.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: the accompanying data-gap log flags NPRA label warnings/contraindications (DG001) as a **Blocking** gap — this evidence pack cannot currently support a Stage 1 safety screen for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are zero supporting clinical trials or publications for the Prinzmetal angina prediction, and the mechanistic rationale generated alongside the prediction itself concludes there is no known pharmacological basis for it — the high TxGNN score appears to be a knowledge-graph artifact rather than a genuine signal.

**To proceed, the following is needed:**
- NPRA package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- DrugBank-sourced mechanism of action data (DG002)
- Original indication and license text for Choline salicylate (currently entirely missing from this pack)
- If further repurposing work on this drug is pursued, note that **rheumatoid arthritis** (rank 2 in this same evidence pack, TxGNN score 99.82%) carries a stronger evidence base — Evidence Level L3, decision stage S2, 4 supporting publications, and a mechanistically coherent rationale (NSAID-class anti-inflammatory action) — and may be a more productive candidate to evaluate next than Prinzmetal angina.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

