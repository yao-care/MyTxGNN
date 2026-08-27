---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 5
---

# Cimetidine
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

# Cimetidine: From Peptic Ulcer Disease to Hyperinsulinism

## One-Sentence Summary

Cimetidine is a histamine H2-receptor antagonist historically used for peptic ulcer disease and gastric acid hypersecretion. The TxGNN model's top-ranked prediction is **Hyperinsulinism**, but the only linked clinical trial (a knee arthroplasty study) is pharmacologically unrelated and **0 supporting publications** exist — indicating this top-ranked signal is most likely a data-pairing artifact rather than genuine evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / gastric acid hypersecretion (H2-receptor antagonist; not captured in NPRA license text, inferred from in-pack pharmacology literature) |
| Predicted New Indication | Hyperinsulinism |
| TxGNN Prediction Score | 0% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 21 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Cimetidine is not available (data gap). Based on known information, Cimetidine is a histamine H2-receptor antagonist whose efficacy in gastric acid-related disorders is well established, as confirmed repeatedly within this evidence pack's own literature (e.g., PMID 342231, 620911).

For the top-ranked candidate, **hyperinsulinism**, the evidence review itself found no identifiable pharmacological link. The single associated clinical trial (NCT05685693) concerns robot-assisted knee arthroplasty and has no relevance to insulin secretion or H2-receptor blockade; the pack's own relevance assessment grades it "C" and its rationale explicitly labels this pairing a likely **data-mismatch/noise** artifact. No literature supports this indication.

Looking at the other candidates in this pack for context: gastric ulcer (rank 3, L1) and esophagitis (rank 2, L2) are both acid-related conditions mechanistically consistent with H2-blockade, but the pack's own rationale notes these largely reconfirm Cimetidine's already-known, established pharmacology rather than reveal a genuinely new indication. Systemic mastocytosis (rank 4, L4) is the most plausible candidate for a distinct secondary use — symptom control of histamine-driven gastric hypersecretion — but remains at an early "Research Question" stage. None of this supports the rank-1 hyperinsulinism prediction specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05685693](https://clinicaltrials.gov/study/NCT05685693) | N/A | Active, not recruiting | 150 | Robot-assisted (ROSA®) vs. conventional knee arthroplasty outcomes; **no pharmacological connection to hyperinsulinism or Cimetidine's mechanism** — flagged by evidence review as a likely mismatched/noise pairing (relevance grade C) |

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA records 21 total registrations for Cimetidine, but license-level details (registration numbers, product names, dosage forms, approved indication text) were not populated in this evidence pack and could not be extracted.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: NPRA label warnings/contraindications are flagged in this evidence pack as a **Blocking** data gap, preventing formal safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (hyperinsulinism) has no mechanistic rationale, no supporting literature, and its only linked trial is unrelated — evidence level L5, decision stage S0. Combined with a **Blocking** data gap on NPRA label warnings/contraindications and a **High**-severity gap on mechanism of action, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Re-verify the hyperinsulinism–Cimetidine pairing against the source knowledge graph for a possible mapping/labeling error
- Obtain NPRA product label (warnings, contraindications) — currently a Blocking gap (DG001)
- Obtain DrugBank mechanism of action data — currently a High-severity gap (DG002)
- If pursuing a genuine repurposing signal from this pack, evaluate **systemic mastocytosis** instead (L4, Research Question stage) as the more mechanistically distinct candidate, pending further clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

