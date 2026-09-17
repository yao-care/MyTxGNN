---
layout: default
title: Salbutamol
parent: High Evidence (L1-L2)
nav_order: 607
evidence_level: L2
indication_count: 10
---

# Salbutamol
{: .fs-9 }

Tahap bukti: **L2** | Indikasi diramal: **10** 
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

# Salbutamol: From Bronchodilator Therapy (Asthma/COPD) to Bronchitis

## One-Sentence Summary

> Salbutamol is a short-acting β2-adrenergic agonist (SABA) bronchodilator, globally established for relieving bronchospasm in asthma and COPD.
> Among 10 TxGNN-predicted new indications for this drug, **Bronchitis** stands out as the most credibly supported candidate,
> with **evidence level L2** drawn from dozens of salbutamol/albuterol clinical trials in bronchitis/bronchiolitis populations, though dedicated peer-reviewed literature specific to this indication is currently absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma and COPD (bronchospasm relief) — established SABA class use; Malaysia label text not extracted in current dataset |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (Marketed) |
| Number of Registrations | 67 |
| Recommended Decision | Proceed with Guardrails |

**Note:** This Evidence Pack bundles 10 TxGNN-predicted indications for Salbutamol. The top-ranked prediction by raw model score, *papillary conjunctivitis*, is explicitly flagged in the pack's own rationale as likely model noise (no supporting evidence, Hold). Bronchitis was selected as the headline candidate for this report because it has the strongest combination of TxGNN score, mechanistic plausibility, and trial-level evidence among the true "new indication" candidates. See the full ranking below.

### Full Prediction Ranking (for context)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Papillary conjunctivitis | 99.996% | L5 | Hold (model noise) |
| 2 | Nasal cavity disease | 99.994% | L4 | Hold |
| 3 | Pharyngitis | 99.994% | L4 | Hold |
| **4** | **Bronchitis** | **99.99%** | **L2** | **Proceed with Guardrails** |
| 5 | Acute laryngopharyngitis | 99.991% | L5 | Hold |
| 6 | Anaphylaxis | 99.96% | L3 | Research Question |
| 7 | Common cold | 99.95% | L3 | Research Question |
| 8 | Atopic conjunctivitis | 99.95% | L4 | Hold |
| 9 | Anorectal stricture | 99.94% | L5 | Hold |
| 10 | Obstructive lung disease | 99.94% | L1 | Proceed with Guardrails (largely overlaps original indication, not a novel use) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Salbutamol is not available in this dataset (DrugBank query pending). Based on well-established pharmacological knowledge, Salbutamol is a short-acting β2-adrenergic receptor agonist (SABA) that relaxes bronchial smooth muscle, and its efficacy in relieving reversible airway obstruction in asthma and COPD is well proven.

Bronchitis frequently presents with airway inflammation accompanied by reversible bronchospasm and airflow obstruction, particularly in acute and pediatric (bronchiolitis-associated) presentations. Because Salbutamol's core mechanism directly targets bronchial smooth muscle relaxation, its extension to bronchitis represents a mechanistically coherent, low-novelty repurposing case — largely reflecting existing off-label/supportive-care practice rather than a genuinely new pharmacological hypothesis.

The clinical trial evidence base (below) consists mainly of salbutamol/albuterol used in bronchiolitis and bronchodilator-responsiveness studies rather than trials formally labeled "bronchitis," so while mechanistic plausibility is high, indication-specific confirmatory evidence remains indirect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02233985](https://clinicaltrials.gov/study/NCT02233985) | Phase 4 | Completed | 64 | RCT of nebulized salbutamol + 3% hypertonic saline vs. standard care in acute bronchiolitis; direct salbutamol efficacy test |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | Completed | 17 | Acute bronchodilator responsiveness (albuterol + tiotropium) in obliterative bronchiolitis post-HSCT |
| [NCT01054170](https://clinicaltrials.gov/study/NCT01054170) | Phase 2 | Completed | 52 | Airway structural changes by CT in COPD/bronchiolitis-related obstruction |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | RCT comparing epinephrine vs. albuterol in bronchiolitis |
| [NCT02760719](https://clinicaltrials.gov/study/NCT02760719) | Phase 2 | Terminated | 100 | Nebulized 3% hypertonic saline with salbutamol vs. standard care in hospitalized children with acute bronchiolitis |
| [NCT01065272](https://clinicaltrials.gov/study/NCT01065272) | Phase 1 | Completed | 200 | Oral dexamethasone + nebulized salbutamol (Ventolin) in viral bronchiolitis |
| [NCT00696540](https://clinicaltrials.gov/study/NCT00696540) | Phase 2 | Unknown | 74 | Salbutamol nebulized in hypertonic vs. normal saline diluent for bronchiolitis during RSV epidemic |
| [NCT01238445](https://clinicaltrials.gov/study/NCT01238445) | N/A | Completed | 29 | Assessing clinical response to albuterol in bronchiolitis |
| [NCT03900494](https://clinicaltrials.gov/study/NCT03900494) | N/A | Completed | 80 | Comparison of valved holding chambers for bronchodilator (primarily salbutamol) delivery in acute wheezing/bronchitis |
| [NCT00798616](https://clinicaltrials.gov/study/NCT00798616) | N/A | Withdrawn | 0 | Steroid benefit in bronchiolitis patients responsive to albuterol |

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Salbutamol currently holds **67 active registrations** with NPRA (Malaysia), and the drug is confirmed as marketed (Marketed). Detailed license-level data (registration numbers, product names, dosage forms, approved indication text) was not returned in the current data extraction and requires a follow-up NPRA registry query.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications, and DDI data, are currently unextracted — see "To proceed" below; this is flagged as a Blocking gap for safety review.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bronchitis involves reversible bronchospasm that is mechanistically consistent with Salbutamol's established SABA action, and this is supported by numerous completed bronchodilator-responsiveness and bronchiolitis trials (evidence level L2). However, no indication-specific published literature exists, and safety documentation for formal review is currently missing.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap — required before any S1 safety evaluation)
- DrugBank-sourced mechanism of action confirmation
- Malaysia-specific license and approved-indication text (currently blank in registry extract)
- Indication-specific (bronchitis, not solely bronchiolitis) peer-reviewed literature search
- Formal drug-drug interaction (DDI) review, given current query returned no results
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

