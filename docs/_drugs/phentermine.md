---
layout: default
title: Phentermine
parent: 僅模型預測 (L5)
nav_order: 543
evidence_level: L5
indication_count: 4
---

# Phentermine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Phentermine: From Weight Management to Hypervitaminosis

## One-Sentence Summary

> Phentermine is internationally known as a short-term appetite suppressant/CNS stimulant used in obesity management, though the formal original-indication text is not available in the current registry extract.
> The TxGNN model's top prediction is **Hypervitaminosis**, but this is a pure knowledge-graph signal with **zero clinical trials** and **zero publications** supporting it, and the model's own mechanistic rationale finds no pharmacological plausibility for the link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in registry extract (all `approved_indication_text` fields empty); internationally documented as a short-term appetite suppressant for obesity |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only) |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for phentermine in this evidence pack (`original_moa: [Data Gap]`), and the registry's approved-indication text is also empty for all three registered products. Based on general pharmacological knowledge, phentermine acts primarily as a noradrenergic/sympathomimetic appetite suppressant.

For the top-ranked prediction, hypervitaminosis, the evidence pack's own rationale explicitly states there is **no known pharmacological or pathophysiological link** between phentermine's mechanism and vitamin-excess states — the high TxGNN score (0.9957) most likely reflects graph-node proximity rather than a real biological relationship, and no clinical or literature evidence corroborates it.

This weak plausibility is consistent across the other three ranked candidates in this pack: rank 2 (proximal 16p11.2 microdeletion syndrome) has no known mechanistic connection to sympathomimetic activity; rank 3 (obsolete hypertelorism) is flagged in the underlying ontology as an **obsolete term**, indicating a data-quality artifact rather than a genuine indication; and rank 4 (frontorhiny) is an ultra-rare KAT6B-related craniofacial disorder with no plausible link. None of the four candidates in this pack should be treated as a credible repurposing hypothesis without independent mechanistic review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The registry confirms phentermine is marketed in Malaysia under **3 active registrations**, but the extract does not include license numbers, product names, dosage forms, or indication text for any of them (all fields returned empty). Detailed product-level data needs to be re-pulled from the source registry before this table can be populated.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on an L5 TxGNN score with no clinical, literature, or mechanistic corroboration — and the pack's own rationale text argues against biological plausibility for the top-ranked indication (hypervitaminosis) and flags one candidate (obsolete hypertelorism) as a likely ontology artifact. In addition, a **Blocking** data gap on TFDA/NPRA label warnings and contraindications (DG001) means this candidate cannot even enter the S1 safety pre-screen.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — Blocking gap, required before any safety screening
- DrugBank-sourced mechanism of action (MOA) for phentermine
- Complete product-level registry data (license numbers, dosage forms, approved indication text) for the 3 Malaysia registrations
- Independent pharmacological/ontology review of all four predicted indications before allocating further evidence-search effort, given the low a priori plausibility already flagged in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

