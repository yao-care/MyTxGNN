---
layout: default
title: Ravulizumab
parent: Low Evidence (L4-L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Ravulizumab
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Ravulizumab: From Complement-Mediated Disease to Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

Ravulizumab is a long-acting terminal complement C5 inhibitor, with its established global indications covering complement/thrombotic microangiopathy-related diseases (PNH, aHUS, gMG, NMOSD). The TxGNN model's top prediction is **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but this direction — along with all 9 other candidates in this evidence pack — has **zero clinical trials and zero literature support**, and the model's own generated rationale explicitly flags it as a likely graph-clustering artifact rather than a genuine mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the current Malaysia regulatory data pull; based on annotations in this evidence pack, Ravulizumab's known global indications are complement-mediated diseases (PNH, aHUS, gMG, NMOSD) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured record (`original_moa`: Data Gap). However, annotations embedded elsewhere in this evidence pack indicate Ravulizumab is a long-acting terminal complement C5 inhibitor (same mechanistic class as eculizumab), blocking cleavage of C5 into C5a/C5b and preventing formation of the membrane attack complex (MAC). Its established indications are complement-mediated diseases and thrombotic microangiopathies.

The model's top-ranked candidate — congenital neutropenia due to G6PC3 deficiency — has no known pathophysiological connection to this mechanism: it arises from a glucose-6-phosphatase defect causing endoplasmic reticulum stress and impaired neutrophil maturation, not complement activation. The evidence pack's own rationale for this candidate explicitly states the high TxGNN score is most likely driven by clustering of "rare hematologic/immune genetic disease" nodes in the knowledge graph rather than a true biological link. This pattern repeats across all 10 ranked candidates in this pack (congenital neutropenia subtypes, platelet disorders, megaloblastic anemia, etc.) — each rationale independently concludes there is no plausible mechanistic bridge to C5 inhibition. The one partial exception is rank 3, primary hyperoxaluria, where the rationale notes a speculative, indirect route (oxalate nephropathy can trigger downstream thrombotic microangiopathy, which is sometimes treated off-label with complement inhibitors) — but this targets a complication, not the disease's underlying enzymatic defect (AGXT/GRHPR/HOGA1), and has no direct supporting evidence either.

Overall, this candidate set reads as a case where TxGNN's high confidence scores are not well corroborated by mechanistic plausibility, and none are backed by real-world clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The NPRA record confirms 1 registration is on file with market status ✓ Marketed. License number, product name, dosage form, and approved indication text were not captured in this data pull.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings` and `contraindications` are flagged as Blocking data gaps — DG001 — in this evidence pack, meaning a formal S1 safety screen cannot proceed until the TFDA package insert is obtained.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are L5 (model prediction only) with no supporting clinical trials or literature, and 9 of 10 candidates' own mechanistic rationale explicitly finds no plausible link to Ravulizumab's C5-inhibition MOA. Combined with a Blocking data gap on safety warnings/contraindications (DG001), there is currently no basis to advance any of these candidates past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — resolves DG001, required before any S1 safety evaluation
- Confirmed DrugBank MOA record — resolves DG002
- If pursuing the primary hyperoxaluria (rank 3) direction specifically: case-level or registry evidence on complement inhibitor use in oxalate-nephropathy-associated TMA, since this is currently a downstream-complication hypothesis rather than a primary-indication hypothesis
- Complete Malaysia regulatory license details (product name, dosage form, approved indication text) for the existing registration
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

