---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Advanced Prostate Cancer to Hypertrichosis

> **Note on data provenance**: The evidence pack's `original_indications` field and TFDA/NPRA license `approved_indication_text` fields are both empty (data gap DG001, Blocking). "Advanced Prostate Cancer" below reflects Degarelix's publicly known global indication (GnRH receptor antagonist, marketed as Firmagon), not data confirmed within this evidence pack.

## One-Sentence Summary

Degarelix is a GnRH (gonadotropin-releasing hormone) receptor antagonist, publicly known for use in advanced prostate cancer — though the evidence pack itself carries no confirmed original indication or MOA data (Blocking gap). The TxGNN model's top-ranked prediction is **Hypertrichosis**, but **no clinical trials or literature currently support this direction**, and the model's own rationale flags the mechanistic link as speculative.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in source data (publicly known: advanced prostate cancer) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (Blocking/High-severity data gaps DG001, DG002). Based on general pharmacological knowledge, Degarelix is a GnRH receptor antagonist that suppresses the hypothalamic-pituitary-gonadal axis, lowering testosterone and estrogen levels — a mechanism used therapeutically in advanced prostate cancer.

The pack's own repurposing rationale for this top-ranked candidate is skeptical rather than supportive: it notes that hypertrichosis broadly refers to non-androgen-dependent, generalized excess hair growth, whereas Degarelix's action is specifically androgen/estrogen suppression. The rationale explicitly states this connection is "weak" and "speculative" (機轉與雄性素軸關聯薄弱，屬推測性連結). In other words, the high TxGNN score does not correspond to a well-supported biological hypothesis for this particular indication.

Worth flagging: within the same evidence pack, rank 9 ("central precocious puberty 1") has a substantially stronger, direct mechanistic rationale — Degarelix's GnRH-antagonism directly targets the GnRH-dependent pathology of central precocious puberty — but scores lower and is marked "Research Question" rather than the top prediction. This suggests the rank-1 candidate (hypertrichosis) reflects knowledge-graph embedding similarity more than a validated pharmacological hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Degarelix is registered under 2 active licenses ("已上市" / Marketed status), but the evidence pack contains no populated license numbers, product names, dosage forms, manufacturers, or approved indication text for either entry — these fields are all blank in the source data and require direct NPRA lookup to complete.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidate has L5 evidence (model prediction only, no clinical trials or literature), and the evidence pack's own mechanistic rationale characterizes the drug-disease link as speculative and weak. There is no empirical or strong mechanistic basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data — key warnings, contraindications, DDI (Blocking gap, DG001)
- Confirmed mechanism of action and original approved indication (High gap, DG002)
- NPRA license details (license numbers, approved indication text, dosage forms) for the 2 registered products
- If pursuing further repurposing analysis, consider re-scoping toward rank 9 (central precocious puberty), which has a stronger direct mechanistic rationale despite its lower TxGNN score and current "Research Question" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

