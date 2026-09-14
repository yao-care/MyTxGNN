---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

> Travoprost (DB00287) is a prostaglandin F2α analog whose established use is lowering intraocular pressure in glaucoma and ocular hypertension — though this specific regulatory dataset does not carry a populated indication text, so that original-use statement is based on public drug knowledge rather than the supplied license records. TxGNN's top-ranked prediction for this drug is **Visceral Calciphylaxis**, but this candidate currently has **zero clinical trials** and **zero supporting publications** — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the supplied NPRA license records (all `approved_indication_text` fields are blank); publicly known as glaucoma / ocular hypertension (prostaglandin F2α / FP-receptor agonist) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on public information, travoprost is a topical prostaglandin F2α analog / FP-receptor agonist used to increase uveoscleral outflow and reduce intraocular pressure.

For this specific candidate, however, the evidence pack itself is explicit that no mechanistic bridge exists: visceral calciphylaxis is a small-vessel calcifying vasculopathy, and the pack notes "no known connection" between that pathology and travoprost's FP-receptor/IOP-lowering pathway. The prediction is therefore a pure statistical signal from TxGNN (rank 6, score ≈1.0) unsupported by any biological rationale, clinical trial, or literature — consistent with its L5/Hold classification.

It is worth noting that a lower-ranked candidate in the same pack, *vascular disease* (rank 5), has a more plausible — if still indirect — mechanistic thread: travoprost's well-documented ocular hyperemia (vasodilatory) side effect and 20 associated publications, though none of that literature studies systemic vascular disease directly. That candidate reached evidence level L4/S1 ("Research Question") and may warrant separate follow-up outside the scope of this report's primary candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Travoprost holds 4 active NPRA registrations ("已上市" / Marketed), but the supplied dataset does not include populated license numbers, product names, dosage forms, or indication texts for any of the 4 entries — this level of detail was not captured in the current data pull and would need to be sourced directly from the NPRA product registry before market-facing use.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/NPRA package-insert warnings and contraindications are flagged as a **Blocking**-severity data gap in this evidence pack — see "To proceed" below — and no drug interaction records were found for travoprost in this query.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (visceral calciphylaxis) is supported only by an extremely high TxGNN score, with no clinical trials, no literature, and no established mechanistic link — the evidence pack's own rationale confirms this. Combined with a Blocking-severity safety data gap that prevents even a preliminary S1 safety screen, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Detailed mechanism of action data from DrugBank — currently a High-severity data gap (DG002)
- Any preclinical or mechanistic studies linking FP-receptor agonism to vascular/soft-tissue calcification pathways, if this candidate is to be reconsidered
- Complete license/product detail (number, product name, dosage form, indication text) for the 4 existing Malaysia registrations
- If pursuing an alternative direction, consider prioritizing the *vascular disease* candidate (L4, 20 supporting publications) for a dedicated evaluation instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

