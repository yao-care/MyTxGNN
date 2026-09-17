---
layout: default
title: Tolvaptan
parent: Low Evidence (L4-L5)
nav_order: 656
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From an Unspecified Approved Indication to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

> Tolvaptan is already marketed in Malaysia (6 registrations), but the source data pack does not specify its original approved indication text or mechanism of action.
> The TxGNN model's top prediction is **Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)** — a genetically distinct ADPKD subtype —
> with **0 disease-specific clinical trials** but **20 supporting publications**, several of which describe landmark Phase 3 RCTs of tolvaptan in the broader ADPKD population.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the current data extract (no `original_indications` recorded; all license `approved_indication_text` fields are blank) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (see caveat below) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tolvaptan is flagged as a data gap in this pack (DG002). However, the supporting literature and trial records included in the evidence itself consistently describe tolvaptan as a **vasopressin V2-receptor (V2R) antagonist** (e.g., PMID 35134221, PMID 37150675, and trial NCT01850940). V2R antagonism reduces intracellular cAMP signaling in renal tubular epithelium, a pathway implicated in cyst formation and growth.

"Polycystic kidney disease 3" refers to a genetically distinct but mechanistically related ADPKD subtype (non-PKD1/PKD2, e.g., GANAB/DNAJB11-associated disease), sharing the ciliopathy-driven cystogenesis pathway seen in classic ADPKD. Since tolvaptan already has demonstrated efficacy in slowing cyst growth and renal function decline in ADPKD generally — per PMID 40726372, it "remains the only FDA-approved therapy targeting disease progression" in ADPKD — the mechanistic rationale for extending its use to the PKD3 subtype is biologically plausible.

**Important caveat**: none of the literature retrieved for this specific predicted indication explicitly isolates the PKD3 (non-PKD1/PKD2) genetic subgroup — the cited RCTs and reviews study ADPKD broadly. The prediction's strength therefore rests on mechanistic extrapolation from the general ADPKD evidence base, not on subtype-specific trial data.

## Clinical Trial Evidence

Currently no clinical trials are registered directly under this specific predicted indication label ("polycystic kidney disease 3 with or without polycystic liver disease").

*Context note: the broader diagnosis category "polycystic kidney disease" (rank 5 in this pack) has 40 associated trials, including two completed Phase 3 RCTs (NCT00428948, NCT02160145) — see Literature Evidence below for the corresponding publications.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (TEMPO 3:4) | The New England Journal of Medicine | Vasopressin V2-receptor antagonism with tolvaptan slowed kidney growth and functional decline in ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (REPRISE) | The New England Journal of Medicine | Tolvaptan efficacy/safety confirmed in later-stage ADPKD patients |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review/Meta-analysis | Nefrologia | Confirms efficacy and characterizes safety profile of tolvaptan across ADPKD trials |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Evaluates disease-modifying agents, including tolvaptan, for ADPKD progression |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement/Guideline | Nephrology, Dialysis, Transplantation | ERA Working Group consensus on tolvaptan use in ADPKD, informed by the TEMPO 3:4 trial |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD epidemiology, genetics, and treatment |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annual Review of Pathology | Advances in understanding and treating polycystic liver disease, the hepatic component of PKD3 |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Review | International Journal of Molecular Sciences | Cystogenesis pathophysiology and treatment advances in ADPKD |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Discusses tolvaptan's role in slowing renal deterioration and cyst growth in combined kidney/liver disease |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Confirms tolvaptan as the only FDA-approved disease-modifying ADPKD therapy; surveys emerging alternatives |

## Malaysia Market Information

Tolvaptan holds 6 active registrations in Malaysia (market status: Marketed), but the underlying dataset for this run did not capture license-level detail — authorization numbers, product names, dosage forms, and approved indication text are all blank in the source extract. This should be re-pulled from NPRA before proceeding further.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic and literature-based efficacy signal for tolvaptan in ADPKD-spectrum disease is strong (two completed Phase 3 RCTs referenced in the literature), but this evidence pack is missing the drug's TFDA/NPRA warnings and contraindications (DG001, flagged Blocking) and its mechanism-of-action confirmation (DG002, flagged High) — both required before an initial safety screen (S1) can begin.

**To proceed, the following is needed:**
- TFDA/NPRA package insert with warnings, precautions, and contraindications (DG001)
- DrugBank-confirmed mechanism of action (DG002)
- Malaysia license-level detail (authorization numbers, product names, dosage forms, approved indication text) for the 6 existing registrations
- Confirmation of whether the PKD3 (non-PKD1/PKD2) genetic subtype has been specifically studied, or whether the evidence base only supports general ADPKD
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

