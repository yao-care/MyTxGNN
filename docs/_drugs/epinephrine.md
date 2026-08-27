---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 4
---

# Epinephrine
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

# Epinephrine: From Anaphylaxis and Emergency Use to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine already holds approved emergency-use indications, including anaphylaxis (per the evidence pack's repurposing rationale; formal NPRA license indication text is a data gap in this dataset). The TxGNN model predicts it may also be effective for **Obstructive Lung Disease**, with **50 clinical trials** and **20 publications** currently associated with this direction — though only a small subset directly test epinephrine itself, mostly in pediatric acute bronchospasm/bronchiolitis rather than chronic COPD maintenance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current NPRA license data (Blocking Data Gap DG001); evidence pack references approved use in anaphylaxis and other emergency indications |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate is not available (High-severity Data Gap DG002). Based on the mechanistic rationale captured in the evidence pack itself, epinephrine's **β2-adrenergic agonism produces bronchodilation**, while its **α1-adrenergic agonism reduces mucosal/airway edema** — mechanisms that already underpin its standard emergency use in croup, bronchiolitis, and acute airway obstruction.

The evidence pack notes that epinephrine already carries approved indications for anaphylaxis and related emergencies. Obstructive lung disease — as represented in the collected evidence, largely acute bronchospasm, bronchiolitis, and croup-related airway obstruction in infants/children — shares overlapping emergency pathophysiology with anaphylaxis: both involve rapid catecholamine-mediated reversal of airway compromise.

However, the evidence base is uneven. Most trials returned under this disease label test **other drug classes** (corticosteroids, benralizumab, magnesium sulfate) in the same disease area rather than epinephrine itself, and none directly address chronic COPD or asthma maintenance therapy. Only a handful of trials — mostly Phase 1–4 studies of inhaled epinephrine (E004/HFA-MDI) or nebulized/IM epinephrine in pediatric bronchiolitis and acute asthma exacerbation — directly test the drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | Pharmacokinetics/safety of Epinephrine Inhalation Aerosol USP (E004, HFA-MDI) in healthy adults |
| [NCT01737892](https://clinicaltrials.gov/study/NCT01737892) | Phase 1/2 | Terminated | 21 | PK study of E004 using deuterium-labeled epinephrine-d3 to distinguish drug from endogenous epinephrine |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Randomized, double-blind, placebo-controlled, crossover single-dose study of E004 in children 4–11 with asthma |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Compared systemic drug exposure: Primatene Mist (inhaled) vs. IM epinephrine injection vs. ProAir HFA (inhaled) in healthy adults |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | IM epinephrine as adjunct to inhaled β2-agonist bronchodilators for severe pediatric asthma exacerbation |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Nebulized adrenaline + oral betamethasone vs. standard care for acute bronchiolitis in the ED |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | Unknown | 100 | Epinephrine, dexamethasone, and hypertonic saline combinations in children with bronchiolitis |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | RCT comparing epinephrine vs. albuterol nebulization for bronchiolitis |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | Unknown | 500 | Optimal inhalation treatment (racemic epinephrine as one comparator) for infants 0–12 months with acute bronchiolitis |
| [NCT00435994](https://clinicaltrials.gov/study/NCT00435994) | N/A | Completed | 59 | Compared aerosol medications (including epinephrine) for airway obstruction in infants with lower respiratory infection |

*40 additional trials in the dataset were graded as low-relevance (different drug classes) or ungraded/pending and are omitted here for focus.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34593615](https://pubmed.ncbi.nlm.nih.gov/34593615/) | 2022 | Systematic Review | Thorax | Guidelines generally recommend against epinephrine in acute asthma except for anaphylaxis/angioedema, though IM epinephrine plus nebulized β2-agonist is used in many prehospital severe-asthma protocols |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of bronchodilators, including epinephrine, for acute bronchiolitis; overall effectiveness remains uncertain |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Review | Cochrane Database Syst Rev | Earlier Cochrane review of epinephrine for bronchiolitis; modest short-term benefit noted in mild-moderate cases |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Reviews role of racemic epinephrine, corticosteroids, hypertonic saline, and high-flow oxygen in pediatric bronchiolitis |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Nebulized adrenaline provides temporary symptomatic benefit in croup and acute bronchiolitis |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clin Evid | Overview of bronchiolitis, the most common lower respiratory tract infection in infants |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Pharmacology Study | Clin Pharmacol Ther | Directly compares bronchodilator effects of terbutaline and epinephrine in obstructive lung disease |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort (mechanistic) | Scand J Clin Lab Invest | Elevated plasma noradrenaline in chronic obstructive lung disease patients, inversely correlated with arterial oxygen saturation |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clin Evid | Earlier review edition on management of infant bronchiolitis |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review | J Allergy Clin Immunol | Overview of childhood asthma pathophysiology and airway hyperresponsiveness mechanisms |

---

## Malaysia Market Information

NPRA registration confirms **marketed status** with **11 active licenses** for epinephrine in Malaysia. Detailed license-level data (authorization numbers, product names, dosage forms, and approved indication text) was not returned in this data pull — this is tracked as Blocking Data Gap **DG001** and needs to be remediated by downloading and parsing the product inserts from the NPRA website before this candidate can proceed to safety evaluation (S1).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L2, anchored by a completed Phase 3 crossover trial of inhaled epinephrine (E004) in pediatric asthma plus multiple systematic/Cochrane reviews, but the supporting evidence predominantly covers **acute pediatric bronchospasm and bronchiolitis**, not chronic COPD/asthma maintenance — a mismatch with the broad "obstructive lung disease" label that warrants clinical scoping before advancing further.

**To proceed, the following is needed:**
- NPRA product insert warnings/contraindications (Blocking Data Gap DG001)
- Mechanism of action confirmation from DrugBank (High Data Gap DG002)
- Clarification of the target population/route (acute pediatric bronchiolitis vs. adult chronic obstructive disease) before defining a specific repurposing claim
- Malaysia license-level detail (product names, dosage forms, approved indication text) currently missing from the registry pull

---

## Other Candidate Indications in This Evidence Pack

This evidence pack (`TW-DB00668-multi`) contains three additional TxGNN-predicted indications for epinephrine, summarized here for completeness rather than as full reports:

| Disease | TxGNN Score | Evidence Level | Decision | Note |
|---------|------------|-----------------|----------|------|
| Food-dependent exercise-induced anaphylaxis | 99.57% | L3 | Proceed with Guardrails | Extension of epinephrine's existing anaphylaxis indication to a specific trigger subtype (physical exertion + food); 20 supporting publications but no dedicated clinical trials |
| Rienhoff syndrome | 99.57% | L5 | Hold | No clinical trials or literature identified; a rare TGFBR2-related connective tissue disorder with no known mechanistic link to adrenergic agonism — likely a knowledge-graph false positive |
| Respiratory malformation | 99.56% | L4 | Hold | Evidence mismatch: retrieved literature concerns croup/upper-airway obstruction, not structural malformation, and most trials are irrelevant noise; requires manual disease-label review before further scoring |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

