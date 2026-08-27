---
layout: default
title: Carboprost Tromethamine
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Carboprost Tromethamine
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

# Carboprost Tromethamine: From Unspecified Approved Indication to Atypical Coarctation of Aorta

## One-Sentence Summary

Carboprost tromethamine is an already-marketed injectable (3 registered licenses), but the full text of its approved indication has not yet been captured in this evidence pack. The TxGNN model predicts a possible link to **Atypical Coarctation of Aorta**, scoring **99.99%**, but this ranking is currently supported by **zero clinical trials and zero publications** — and the evidence pack's own rationale flags this as a likely false-positive association rather than a genuine treatment signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not yet extracted — all 3 license records have blank indication text (see Data Gaps) |
| Predicted New Indication | Atypical Coarctation of Aorta |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for carboprost tromethamine is not yet available (MOA remains a documented data gap). Based on general pharmacological knowledge, carboprost tromethamine is a PGF2α (prostaglandin F2-alpha) analog whose primary pharmacological action is uterine smooth-muscle contraction, consistent with its class as a uterotonic agent used in obstetric bleeding-control contexts.

The TxGNN model assigns a very high score (99.99%) to a link between this drug and "atypical coarctation of aorta," but this condition is a **structural congenital cardiovascular malformation** — an anatomical defect that is not reversible by pharmacological intervention. There is no mechanistic pathway connecting a uterotonic prostaglandin analog to correction of aortic structural anomalies, and no clinical trial or literature evidence supports this link.

The evidence pack's own repurposing rationale explicitly characterizes this as a likely artifact of knowledge-graph node proximity rather than a genuine causal treatment relationship. This prediction should therefore be treated as evidence-free and mechanistically unsupported, not as a promising repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The evidence pack confirms 3 registered licenses and an overall "已上市 (Marketed)" status, but license-level details (authorization number, product name, dosage form, approved indication text) are all currently blank in the source data and cannot be reported.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction (atypical coarctation of aorta) targets a non-drug-treatable structural anomaly, has no supporting clinical or literature evidence, and is flagged by the evidence pack itself as a likely spurious association. Combined with missing MOA and safety data, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Drug label warnings/contraindications from official Malaysia/Taiwan regulatory source (currently Blocking gap, DG001)
- Mechanism of action data via DrugBank (currently High-severity gap, DG002)
- Complete license-level regulatory data (authorization numbers, product names, approved indication text)
- If pursuing repurposing directions for this drug, consider re-evaluating **rank 10 (primary hereditary glaucoma)** instead — it has a class-level mechanistic rationale (PGF2α/FP-receptor agonist class shared with approved glaucoma drugs) despite a lower TxGNN score, making it a more biologically grounded candidate than the current top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

