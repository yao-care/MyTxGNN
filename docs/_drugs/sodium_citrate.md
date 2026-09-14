---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 5
---

# Sodium Citrate
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

# Sodium Citrate: From Existing Marketed Use to Pharyngitis

## One-Sentence Summary

Sodium Citrate (DrugBank DB09154) is an already-marketed drug in Malaysia with 36 active registrations, though its originally approved indication text is not available in the current data extract. The TxGNN model's top-ranked prediction is **Pharyngitis**, but after review, none of the 6 retrieved clinical trials or 1 retrieved publication actually studied sodium citrate for this indication — they are keyword coincidences on "citrate."

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — all license `approved_indication_text` fields in the current extract are blank |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 36 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for sodium citrate is not available in this evidence pack, and no original approved indication text could be extracted from the Malaysia registration records (all licence indication fields were blank in this data pull).

More importantly, the evidence review for this specific prediction found **no genuine mechanistic or clinical link** between sodium citrate and pharyngitis. The repurposing rationale explicitly states that all six retrieved trials and the one retrieved publication are keyword-coincidence matches on "citrate" — a COVID-19 outpatient multi-drug platform trial, a nebulized *fentanyl citrate* trial, two unrelated anaesthesia/airway comparison studies, a lithium-containing mouthwash trial, and a Ga-67 *citrate* thyroid scintigraphy case report. None involve administering sodium citrate to treat pharyngitis, so the mechanistic basis for this candidate is currently absent.

For context, two other ranked candidates in this pack — Rhinitis (rank 2, evidence level L3) and Gastroesophageal Reflux Disease (rank 4, evidence level L4) — show more plausible mechanistic stories (calcium chelation affecting nasal mucosa/olfaction; citrate's established antacid/alkalinizing use) and were both scored "Research Question" rather than "Hold." These may be better candidates for further evaluation than the top-ranked Pharyngitis prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04518410](https://clinicaltrials.gov/study/NCT04518410) | Phase 2/3 | Completed | 4044 | COVID-19 outpatient multi-drug platform trial; not related to sodium citrate or pharyngitis (relevance grade C) |
| [NCT05165992](https://clinicaltrials.gov/study/NCT05165992) | Phase 3 | Unknown | 200 | Nebulized **fentanyl citrate** for COVID-19 respiratory/throat symptoms; different drug (relevance pending, keyword match only) |
| [NCT03812718](https://clinicaltrials.gov/study/NCT03812718) | N/A | Recruiting | 160 | Airway device comparison during laparoscopic cholecystectomy anaesthesia; no drug-indication link (relevance pending) |
| [NCT06251050](https://clinicaltrials.gov/study/NCT06251050) | Phase 1/2 | Completed | 175 | Lithium-containing mouthwash for radiotherapy-induced oral mucositis/dysgeusia; not sodium citrate (relevance grade C) |
| [NCT03107832](https://clinicaltrials.gov/study/NCT03107832) | N/A | Completed | 40 | Sedation method comparison in laparoscopic cholecystectomy; unrelated to pharyngitis (relevance pending) |
| [NCT04642638](https://clinicaltrials.gov/study/NCT04642638) | Phase 2/3 | Terminated | 1307 | INO-4800 DNA COVID-19 vaccine trial; unrelated (relevance pending) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11181329](https://pubmed.ncbi.nlm.nih.gov/11181329/) | 2001 | Case report | Revista española de medicina nuclear | Ga-67 **citrate** scintigraphy used to diagnose subacute thyroiditis; a radioactive imaging tracer, not the drug sodium citrate, and unrelated to pharyngitis |

## Malaysia Market Information

Registration-level details (authorization number, product name, dosage form, approved indication text) are not populated in the current data extract — all 5 sampled license records returned blank fields. The regulatory database confirms **36 total active registrations** for sodium citrate in Malaysia with market status "Marketed," but the underlying license detail needs to be re-pulled from the NPRA source to populate this table.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were returned in this evidence pack (DDI query status: not found), and the drug label/warning extraction (DG001) is flagged as a **Blocking** data gap that currently prevents a full safety pre-assessment (S1) for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Pharyngitis) has no supporting mechanistic rationale, and every retrieved trial and publication is an incidental "citrate" keyword match rather than genuine evidence for this indication — evidence level L5 (model prediction only).

**To proceed, the following is needed:**
- Product label warnings/contraindications (DG001, Blocking — required before any S1 safety assessment)
- Verified mechanism of action data (DG002)
- Complete license-level registration data (authorization numbers, indication text) for Malaysia
- Consider re-scoping the evaluation toward Rhinitis (rank 2, L3, "Research Question") or Gastroesophageal Reflux Disease (rank 4, L4, "Research Question"), which show materially stronger mechanistic and evidentiary support than the top-ranked Pharyngitis candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

