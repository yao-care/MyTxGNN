---
layout: default
title: Spironolactone
parent: Low Evidence (L4-L5)
nav_order: 627
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **2** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Spironolactone: From Marketed Indication (Not Specified) to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a mineralocorticoid receptor antagonist marketed in Malaysia (1 registration on file), though the specific approved indication text is not captured in the current evidence pack. The TxGNN model predicts potential effectiveness for **Hypotrichosis Simplex of the Scalp**, a rare genetic hair-loss disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence level L5, model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available registration data |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is flagged as a data gap in this evidence pack. However, the prediction rationale supplied alongside the candidate indicates spironolactone acts as a mineralocorticoid receptor antagonist with notable anti-androgenic activity (androgen receptor blockade, inhibition of steroidogenesis), and is widely used off-label for androgenetic alopecia (female pattern hair loss).

That established anti-androgen use is the likely source of TxGNN's high score — but it does not transfer cleanly to the two predicted indications here. Hypotrichosis simplex of the scalp is a rare autosomal dominant disorder primarily linked to *APCDD1* and *CDH3* mutations, with a follicular developmental defect that has no direct connection to androgen signaling. Similarly, congenital hypotrichosis with milia-like features is associated with desmosomal gene mutations (e.g., *DSC2*, *DSG4*) affecting keratinocyte/follicle structure, not androgen-driven hair suppression.

In both cases, the evidence pack's own rationale flags this as a likely **semantic clustering artifact** — the knowledge graph groups these diseases under a shared "hypotrichosis/alopecia" label rather than through a validated, mechanism-specific pathway. This is a high-risk mechanistic extrapolation, not a well-grounded pharmacological hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Malaysia market status for spironolactone is confirmed as marketed, with 1 registration on file. License number, product name, dosage form, and approved indication text are not available in the current evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap — DG001 — which independently prevents this candidate from entering the S1 safety review stage regardless of indication-level evidence.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by TxGNN's model score (L5, decision stage S0) with zero clinical trials or literature, and the mechanistic link is judged weak — the high score likely reflects disease-label clustering ("hypotrichosis") rather than a validated pathway connecting spironolactone's anti-mineralocorticoid/anti-androgen activity to these genetically-driven follicular disorders.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to clear the Blocking data gap (DG001) before any safety review can begin
- Confirmed original indication text and mechanism of action (DG002)
- Preclinical or case-level evidence linking androgen/mineralocorticoid pathways to *APCDD1*/*CDH3*- or desmosome-related follicular pathology
- Any case reports of spironolactone use in genetic hypotrichosis syndromes to test the mechanistic hypothesis before further investment
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

