---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Finasteride: From Androgenetic Alopecia/BPH to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5α-reductase inhibitor conventionally used for benign prostatic hyperplasia and androgenetic alopecia (male pattern hair loss); this evidence pack does not contain the specific NPRA-approved indication text. The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital disorder of excessive hair growth — but this pairing currently has **0 clinical trials and 0 publications**, and the drug's own mechanistic direction (DHT suppression → less hair growth) runs opposite to what this disease would require.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied NPRA license records (all indication-text fields are blank); Finasteride is generally known as a 5α-reductase inhibitor for BPH and androgenetic alopecia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% (rank 207 of full candidate list) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, Finasteride inhibits 5α-reductase type II, lowering dihydrotestosterone (DHT) — a mechanism that **reduces** androgen-dependent hair growth, which is why it is used for male pattern hair loss and BPH.

Ambras type hypertrichosis is a congenital, non-androgen-dependent condition of generalized excess hair growth, most often linked to chromosome 8q rearrangements near the *TRPS1* locus, not to androgen/DHT signaling. The evidence pack's own mechanistic analysis is explicit that there is no plausible biological connection here, and that the direction is actually inverted: Finasteride suppresses hair growth, while Ambras hypertrichosis is a disease of excess hair growth. No clinical trials, ICTRP records, or PubMed literature support this pairing.

The related rank-2 candidate, "hypertrichosis (disease)" (score 99.99%, rank 248), has some retrieved evidence (1 clinical trial, 4 literature items), but the trial is graded relevance "C" — it studies topical treatments for androgenetic alopecia (hair *loss*), not hypertrichosis, and none of the four literature items involve Finasteride directly. Taken together, this strongly suggests the TxGNN score reflects proximity in a "hair-related disease" embedding space rather than a genuine pharmacological relationship. This candidate should be treated as low-confidence pending further mechanistic or clinical justification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Finasteride is marketed in Malaysia with 8 total NPRA registrations (market status: 已上市/Marketed). However, this evidence pack does not include populated license-level details (license number, product name, dosage form, or approved-indication text) — those fields were returned blank by the data source and would need to be re-pulled from NPRA records before they can be reported.

## Safety Considerations

Please refer to the package insert for safety information. (Note: retrieval of NPRA label warnings/contraindications is flagged as a **Blocking** data gap — DG001 — and must be resolved before any safety-stage review can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis universalis congenita) has no clinical or literature support (L5, decision stage S0), and the evidence pack's own mechanistic rationale indicates the drug's effect runs in the opposite direction from what this disease would need. Separately, a Blocking data gap (missing NPRA label warnings/contraindications) prevents any safety-stage evaluation from proceeding regardless of indication.

**To proceed, the following is needed:**
- NPRA product label (PDF) with warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action data from DrugBank (DG002, High)
- If a hair-growth-related repurposing hypothesis is still of interest, re-evaluate the rank-2 candidate ("hypertrichosis (disease)") with trials/literature that actually involve Finasteride, rather than the current androgenetic-alopecia trial of only tangential relevance
- Populated NPRA license-level data (product names, dosage forms, approved indication text) for the 8 existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

