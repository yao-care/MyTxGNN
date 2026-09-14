---
layout: default
title: Tiotropium
parent: 僅模型預測 (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Tiotropium
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

Using the drug-repurposing report template directly on the supplied Evidence Pack. One important note before the report: `predicted_indications[0]` ("obstructive lung disease") is TxGNN's top hit, but its own `repurposing_rationale` states this is the **umbrella term already covering tiotropium's approved COPD/asthma use** — i.e., not a genuine new-use signal. I've built the report per the template (which anchors on `predicted_indications[0]`) but flagged this prominently so the report isn't misleading.

---

# Tiotropium: From Chronic Obstructive Pulmonary Disease to Obstructive Lung Disease

## One-Sentence Summary

> Tiotropium is a long-acting muscarinic antagonist (LAMA) bronchodilator established for chronic obstructive pulmonary disease (COPD) and, as add-on therapy, severe persistent asthma.
> The TxGNN model's top-ranked prediction is **Obstructive Lung Disease**, supported by **50 clinical trials** and **20 publications** — however, this term is the disease-category umbrella that already includes tiotropium's approved indications, so it should be read as a confirmatory signal rather than a genuinely novel repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the TFDA/NPRA license extract (approved-indication text is blank for all 3 registrations); based on established pharmacology, tiotropium is indicated for maintenance treatment of COPD and as add-on controller therapy in severe persistent asthma |
| Predicted New Indication | Obstructive Lung Disease *(umbrella term — not a novel indication; see caveat below)* |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails *(model-derived label — see Conclusion for a corrected recommendation)* |

---

## Why is This Prediction Reasonable?

`drug.original_moa` is marked as a data gap in this Evidence Pack, so the mechanism below is drawn from the `repurposing_rationale` fields attached to individual predictions rather than a dedicated MOA record: Tiotropium is a long-acting muscarinic receptor antagonist (LAMA) that selectively blocks M3 receptors on airway smooth muscle, producing sustained bronchodilation. This is the well-established mechanistic basis for its role in COPD and asthma management.

**Important caveat**: the rationale text supplied for this top-ranked prediction explicitly states that "obstructive lung disease" is a superordinate concept covering COPD and asthma — i.e., the disease tiotropium is *already* indicated for — and is "not a novel prediction." The same applies to rank 5 in this Evidence Pack, "chronic obstructive pulmonary disease" itself (L1, included seemingly as a baseline/sanity-check entry). Both score extremely high (>99.8%) precisely because the model is correctly recovering a known drug–disease link, not surfacing new therapeutic potential.

Among the remaining candidates, only rank 4 ("COPD, severe early onset") represents a plausible but underpowered incremental extension — same LAMA mechanism, but no trial has specifically enrolled or stratified this early-onset severe phenotype. Ranks 2, 3, and 6–10 (respiratory malformation, Rienhoff syndrome, hyperlucent lung, compensatory emphysema, interstitial emphysema, tracheal stenosis, and a CD8α-deficiency immune disorder) are structural, genetic, or immunologic conditions with no mechanistic link to M3-receptor antagonism; their own rationale text flags them as likely drug-name co-occurrence noise rather than real signal, and 6 of the 7 have zero supporting trials or literature (L5).

---

## Clinical Trial Evidence

*(from `predicted_indications[0]` — "obstructive lung disease")*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | Completed | 453 | Placebo-controlled trial of tiotropium Respimat 5 mcg/day as add-on controller therapy over 48 weeks in severe persistent asthma |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | Completed | 457 | 24-week multicenter trial of tiotropium 18 mcg HandiHaler + PRN albuterol vs. placebo + PRN albuterol in maintenance-naïve COPD |
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Phase 3 | Completed | 5993 | UPLIFT-scale trial assessing whether daily tiotropium reduces the rate of lung-function decline in COPD |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Phase 3 | Completed | 914 | SAFE study — one-year effect of tiotropium 18 mcg on trough FEV1 change in COPD, stratified by smoking status |
| [NCT01911364](https://clinicaltrials.gov/study/NCT01911364) | Phase 3 | Completed | 3686 | 52-week trial comparing triple therapy (beclometasone+formoterol+glycopyrronium) vs. tiotropium and vs. tiotropium+beclometasone/formoterol in severe COPD |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | Completed | 872 | 24-week comparison of GSK573719/GW642444 vs. GSK573719 vs. tiotropium in COPD |
| [NCT02173769](https://clinicaltrials.gov/study/NCT02173769) | N/A | Completed | 1845 | Real-world assessment of physical functioning changes with tiotropium+olodaterol combination therapy in COPD |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | Completed | 17 | Acute bronchodilator responsiveness to tiotropium and albuterol in obliterative bronchiolitis after hematopoietic stem cell transplant |
| [NCT00662740](https://clinicaltrials.gov/study/NCT00662740) | Phase 3 | Terminated | 220 | 1-year comparison of tiotropium+salmeterol combination regimens vs. single-agent therapies in COPD |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Phase 4 | Terminated | 80 | Intermittent tiotropium+salbutamol vs. fluticasone+salbutamol vs. salbutamol alone for episode-free days in early-childhood wheezing |

---

## Literature Evidence

*(from `predicted_indications[0]` — "obstructive lung disease")*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | The New England Journal of Medicine | Long-term tiotropium use improves lung function and slows decline in mild/moderate, early-stage COPD |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Update of tiotropium vs. placebo efficacy/safety evidence across trial formats including the Respimat soft-mist inhaler |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Update comparing tiotropium against ipratropium bromide in stable COPD |
| [29206658](https://pubmed.ncbi.nlm.nih.gov/29206658/) | 2018 | Review | Current Opinion in Pulmonary Medicine | Review of lung-function trajectories in COPD and the role of pharmacologic intervention in early disease phases |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Mechanistic profile of tiotropium as a slow-dissociating, kinetically M3/M1-selective antimuscarinic bronchodilator |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Cohort/Comparative | The Annals of Pharmacotherapy | Review of efficacy/safety data on concomitant ipratropium plus tiotropium use in COPD |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Current Medical Research and Opinion | Evidence review of tiotropium+olodaterol fixed-dose combination per GOLD 2020 recommendations for exacerbation reduction |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Review of tiotropium's clinical development history as LAMA monotherapy for GOLD groups B, C, and D |
| [22562275](https://pubmed.ncbi.nlm.nih.gov/22562275/) | 2012 | Study (unclassified) | Pneumonologia i Alergologia Polska | Effects of formoterol, formoterol+tiotropium, formoterol+ICS, and tiotropium on lung function, exercise tolerance, and morning activities in COPD |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Study (unclassified) | Drugs | Pharmacologic and clinical profile of tiotropium bromide as a once-daily anticholinergic bronchodilator in COPD |

---

## Malaysia Market Information

The evidence pack confirms **3 active registrations** for tiotropium with market status "Marketed," but product-level fields (authorization number, product name, dosage form, and approved-indication text) are blank in the current data extract and cannot be populated without re-querying the source registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Underlying data: `key_warnings`, `contraindications`, and the DDI query all returned no usable content in this Evidence Pack — DDI query status: not found, 0 interactions recorded.)*

---

## Conclusion and Next Steps

**Decision: Hold — Not a Novel Repurposing Candidate (as top-ranked)**

**Rationale:**
- The Evidence Pack's own rationale for the #1-ranked prediction ("obstructive lung disease") states it is a superordinate concept already encompassing tiotropium's approved COPD/asthma indications — the L1 evidence level reflects confirmation of existing use, not a new therapeutic signal, so it should not be advanced through a repurposing pathway.
- Of the remaining candidates, only rank 4 ("COPD, severe early onset," L3, "Research Question") is mechanistically plausible but lacks phenotype-specific trial data; all others (respiratory malformation, Rienhoff syndrome, hyperlucent lung, compensatory emphysema, interstitial emphysema, tracheal stenosis, and CD8α-deficiency susceptibility) are structural/genetic/immunologic conditions with no mechanistic rationale and, in 6 of 7 cases, zero supporting trials or literature (L5) — recommendation Hold on all.

**To proceed, the following is needed:**
- TFDA/NPRA package-insert warnings and contraindications (flagged as a **Blocking** data gap — required before any Stage 1 safety screen can proceed)
- Formal mechanism-of-action record for tiotropium (High-severity data gap; the mechanism cited above was reconstructed from prediction-level rationale text, not a dedicated MOA source)
- If pursuing rank 4 ("COPD, severe early onset") further: literature/trial search specifically targeting early-onset severe COPD phenotypes rather than general COPD populations
- Complete product-level Malaysia registration data (brand names, dosage forms, approved-indication text) currently missing from the license extract
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

