---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 5
---

# Tadalafil
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

# Tadalafil: From Established PDE5-Inhibitor Uses to Premature Ejaculation as a New Indication

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor already marketed in Malaysia (23 NPRA registrations) whose best-known uses — erectile dysfunction, pulmonary arterial hypertension, and benign prostatic hyperplasia — are picked up by the TxGNN model with the strongest evidence (L1, dozens of completed Phase 3 trials each), confirming the model is recovering **known, already-approved pharmacology** rather than flagging something new. The one genuinely novel repurposing signal in this pack is **Premature Ejaculation**, supported by **6 clinical trials** and **20 publications**, mostly evaluating tadalafil in combination with SSRIs (dapoxetine/paroxetine) rather than as monotherapy. A fifth candidate, psychologic dyspareunia, has only 2 small/indirect publications and no clinical trials, and should be put on hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction (Tadalafil's globally established original approval; Malaysia-specific NPRA label wording is not available in this evidence pack) |
| Predicted New Indication (headline) | 5 candidates evaluated — see breakdown below; genuine novel signal is **Premature Ejaculation** |
| TxGNN Prediction Score | Recorded as 0.0 for all 5 candidates in this pack — score field appears unpopulated/not meaningful for differentiation; ranking below uses evidence level and clinical relevance instead |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 23 |
| Recommended Decision | Mixed — see per-indication table below |

### Per-Indication Breakdown

| Rank | Disease | Evidence Level | Decision Stage | Recommendation |
|------|---------|-----------------|-----------------|-----------------|
| 1 | Erectile Dysfunction | L1 | S3 | Proceed with Guardrails *(already an approved use elsewhere — confirmatory signal)* |
| 2 | Premature Ejaculation | L2 | S2 | Research Question *(genuine new-indication candidate)* |
| 3 | Psychologic Dyspareunia | L4 | S0 | Hold *(insufficient, indirect evidence)* |
| 4 | Pulmonary Hypertension | L1 | S3 | Proceed with Guardrails *(already approved as Adcirca elsewhere — confirmatory signal)* |
| 5 | Benign Prostatic Hyperplasia | L1 | S3 | Proceed with Guardrails *(already approved elsewhere — confirmatory signal)* |

---

## Why is This Prediction Reasonable?

Tadalafil is a selective phosphodiesterase type-5 (PDE5) inhibitor. It blocks the breakdown of cGMP, which relaxes vascular and other smooth muscle. This single mechanism explains all five predictions in this pack, though it applies to each with very different strength:

**Erectile dysfunction, pulmonary hypertension, and benign prostatic hyperplasia** are not new pharmacology for tadalafil — they are its existing, globally approved indications (branded as Cialis for ED/BPH and Adcirca for PAH). PDE5 inhibition relaxes corpus cavernosum smooth muscle (ED), pulmonary vascular smooth muscle (PAH), and prostate/bladder-neck smooth muscle while improving pelvic blood flow (BPH). The evidence pack itself labels these three as "已核准適應症（非老藥新用）" — approved indications, not true drug repurposing. Their appearance here mainly validates that the model correctly recovers tadalafil's real pharmacology; on their own they don't represent an actionable *new* opportunity unless the specific indication is missing from the current Malaysia NPRA label (which cannot be confirmed from this pack — see Data Gaps below).

**Premature ejaculation (PE)** is the more interesting candidate. The mechanistic story is indirect: PDE5 inhibition prolongs erectile rigidity and may improve sexual confidence, which can secondarily delay ejaculatory latency, but the bulk of supportive evidence comes from tadalafil used **in combination with SSRIs** (dapoxetine, paroxetine, fluoxetine) that act on serotonin reuptake — the primary PE mechanism. Tadalafil monotherapy data for PE exists but is less robust than the combination data.

**Psychologic dyspareunia** relies on an extrapolated mechanism (increased genital blood flow/engorgement improving arousal-related intercourse pain) supported only by a systematic review of an unrelated condition (unconsummated marriage) and one small, uncontrolled study in diabetic women with genital arousal disorder — not psychogenic dyspareunia itself. This is a much weaker, purely theoretical link.

---

## Clinical Trial Evidence

### Erectile Dysfunction (top 10 of 50 retrieved)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00547287](https://clinicaltrials.gov/study/NCT00547287) | Phase 3 | Completed | 2760 | Multinational preference study, sildenafil vs. tadalafil switching |
| [NCT01937871](https://clinicaltrials.gov/study/NCT01937871) | Phase 3 | Completed | 909 | Once-daily tadalafil for ED + BPH-LUTS signs/symptoms |
| [NCT01122264](https://clinicaltrials.gov/study/NCT01122264) | Phase 4 | Completed | 770 | Once-daily vs. on-demand tadalafil vs. on-demand sildenafil, treatment adherence |
| [NCT00547599](https://clinicaltrials.gov/study/NCT00547599) | Phase 4 | Completed | 659 | Effect of ED-related distress on tadalafil treatment response |
| [NCT02224846](https://clinicaltrials.gov/study/NCT02224846) | Phase 4 | Completed | 635 | Postmarketing surveillance, tadalafil 2.5/5 mg once daily in Chinese men |
| [NCT00547417](https://clinicaltrials.gov/study/NCT00547417) | Phase 3 | Completed | 1933 | On-demand tadalafil efficacy/safety across diverse populations incl. diabetes, depression *(graded A)* |
| [NCT00734604](https://clinicaltrials.gov/study/NCT00734604) | Phase 3 | Completed | 378 | Psychosocial outcomes: once-daily tadalafil vs. as-needed PDE5i |
| [NCT00422734](https://clinicaltrials.gov/study/NCT00422734) | Phase 3 | Completed | 342 | Tadalafil 5 mg daily vs. placebo, sexual quality of life |
| [NCT00547183](https://clinicaltrials.gov/study/NCT00547183) | Phase 3 | Completed | 298 | Tadalafil 2.5/5 mg once daily in men with diabetes and ED |
| [NCT06805513](https://clinicaltrials.gov/study/NCT06805513) | Phase 3 | Recruiting | 2250 | Actual-use trial for prescription-to-OTC switch of tadalafil 5 mg *(graded B)* |

### Premature Ejaculation (all 6 retrieved)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01063855](https://clinicaltrials.gov/study/NCT01063855) | Phase 3 | Completed | 495 | RCT, dapoxetine vs. placebo in men with PE + ED already on a PDE5i (incl. tadalafil) *(graded A)* |
| [NCT03177746](https://clinicaltrials.gov/study/NCT03177746) | Phase 4 | Unknown | 40 | Safety of dapoxetine/tadalafil 30/20 mg combination for PE + ED *(graded B)* |
| [NCT04361305](https://clinicaltrials.gov/study/NCT04361305) | Phase 3 | Unknown | 150 | Multicenter efficacy/safety of dapoxetine + tadalafil for PE with concomitant ED *(graded B)* |
| [NCT05052879](https://clinicaltrials.gov/study/NCT05052879) | Phase 3 | Not yet recruiting | 232 | Combination product for both ED and PE *(graded C — no results yet)* |
| [NCT04703127](https://clinicaltrials.gov/study/NCT04703127) | Phase 3 | Unknown | 60 | On-demand dapoxetine+tadalafil vs. dapoxetine+lidocaine spray for lifelong PE non-responders |
| [NCT05749354](https://clinicaltrials.gov/study/NCT05749354) | NA | Unknown | 159 | TCM ("Liver Meridian") study touching on male impotence, tangential to PE |

### Psychologic Dyspareunia

Currently no related clinical trials registered.

### Pulmonary Hypertension (top 10 of 50 retrieved)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01178073](https://clinicaltrials.gov/study/NCT01178073) | Phase 3 | Completed | 610 | AMBITION trial — first-line ambrisentan+tadalafil combination vs. monotherapy in PAH *(graded A)* |
| [NCT01066845](https://clinicaltrials.gov/study/NCT01066845) | Phase 4 | Completed | 1809 | Long-term safety/effectiveness of Adcirca (tadalafil) in Japanese PAH patients *(graded A)* |
| [NCT03904693](https://clinicaltrials.gov/study/NCT03904693) | Phase 3 | Completed | 187 | Macitentan+tadalafil monotherapies vs. fixed-dose combination in PAH |
| [NCT02558231](https://clinicaltrials.gov/study/NCT02558231) | Phase 3 | Completed | 247 | Initial triple (macitentan+tadalafil+selexipag) vs. dual oral therapy in newly diagnosed PAH |
| [NCT00549302](https://clinicaltrials.gov/study/NCT00549302) | Phase 3 | Completed | 357 | Long-term safety/efficacy extension study of tadalafil in PAH |
| [NCT02891850](https://clinicaltrials.gov/study/NCT02891850) | Phase 4 | Completed | 225 | Riociguat as replacement for PDE5i therapy in PAH not at treatment goal |
| [NCT01824290](https://clinicaltrials.gov/study/NCT01824290) | Phase 3 | Completed | 35 | Double-blind efficacy/safety of tadalafil in pediatric PAH *(graded B)* |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | Ambrisentan+tadalafil in PAH associated with systemic sclerosis |
| [NCT01305252](https://clinicaltrials.gov/study/NCT01305252) | Phase 4 | Completed | 21 | Upfront dual therapy (inhaled treprostinil + tadalafil) in treatment-naïve PAH |
| [NCT05937854](https://clinicaltrials.gov/study/NCT05937854) | Phase 2 | Recruiting | 126 | Tadalafil for respiratory symptoms in COPD complicated by pulmonary hypertension |

### Benign Prostatic Hyperplasia (top 10 of 38 retrieved)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00384930](https://clinicaltrials.gov/study/NCT00384930) | Phase 2/3 | Completed | 1058 | Multinational dose-response study of once-daily tadalafil for BPH signs/symptoms *(graded A)* |
| [NCT01139762](https://clinicaltrials.gov/study/NCT01139762) | Phase 3 | Completed | 696 | Tadalafil co-administered with finasteride for LUTS + prostatic enlargement |
| [NCT04947631](https://clinicaltrials.gov/study/NCT04947631) | Phase 3 | Completed | 667 | Dutasteride+tadalafil (DKF-313) combination for BPH |
| [NCT00861757](https://clinicaltrials.gov/study/NCT00861757) | Phase 3 | Completed | 612 | Placebo- and tamsulosin-controlled study of tadalafil once daily in Asian men with BPH |
| [NCT01460342](https://clinicaltrials.gov/study/NCT01460342) | Phase 3 | Completed | 610 | Once-daily tadalafil for 12 weeks in Asian men with BPH |
| [NCT00855582](https://clinicaltrials.gov/study/NCT00855582) | Phase 3 | Completed | 606 | Tadalafil 2.5/5 mg for concurrent ED and BPH signs/symptoms |
| [NCT00970632](https://clinicaltrials.gov/study/NCT00970632) | Phase 3 | Completed | 511 | Global multicenter study of once-daily tadalafil for BPH |
| [NCT00848081](https://clinicaltrials.gov/study/NCT00848081) | Phase 3 | Completed | 318 | Tadalafil added to concomitant alpha1-blocker therapy for BPH *(graded A)* |
| [NCT00827242](https://clinicaltrials.gov/study/NCT00827242) | Phase 3 | Completed | 325 | Multinational placebo-controlled study of daily tadalafil for BPH |
| [NCT06466369](https://clinicaltrials.gov/study/NCT06466369) | Phase 3 | Completed | 306 | Once-daily tadalafil, anti-inflammatory/antiproliferative/relaxant effects in ED+BPH *(graded A)* |

---

## Literature Evidence

### Erectile Dysfunction (top 10 of 20 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28741090](https://pubmed.ncbi.nlm.nih.gov/28741090/) | 2017 | Systematic Review | Int Urol Nephrol | Direct comparison of tadalafil vs. sildenafil for ED |
| [21711956](https://pubmed.ncbi.nlm.nih.gov/21711956/) | 2011 | Review | BMJ Clinical Evidence | ED overview: prevalence, risk factors, treatment options |
| [39532245](https://pubmed.ncbi.nlm.nih.gov/39532245/) | 2025 | Cohort | Am J Med | Tadalafil/sildenafil effects on mortality, cardiovascular disease, dementia |
| [28882778](https://pubmed.ncbi.nlm.nih.gov/28882778/) | 2018 | Systematic Review/Meta-analysis | Urology | Tadalafil daily vs. on-demand for ED |
| [29341503](https://pubmed.ncbi.nlm.nih.gov/29341503/) | 2018 | Systematic Review/Meta-analysis | Lower Urin Tract Symptoms | Tadalafil 5 mg once daily for LUTS and ED |
| [28628914](https://pubmed.ncbi.nlm.nih.gov/28628914/) | 2017 | Systematic Review/Meta-analysis | Urol Int | Once-a-day vs. on-demand tadalafil efficacy/safety |
| [20856843](https://pubmed.ncbi.nlm.nih.gov/20856843/) | 2010 | Review | Drug Des Devel Ther | Once-daily tadalafil: compliance and efficacy |
| [17183346](https://pubmed.ncbi.nlm.nih.gov/17183346/) | 2007 | Review | Int J Impot Res | Do vardenafil/tadalafil have advantages over sildenafil? |
| [15709885](https://pubmed.ncbi.nlm.nih.gov/15709885/) | 2005 | Review | Expert Opin Pharmacother | Comparison of sildenafil, vardenafil, tadalafil trials |
| [12435622](https://pubmed.ncbi.nlm.nih.gov/12435622/) | 2002 | Review | Eur J Med Res | Comparative efficacy/side effects of PDE5 inhibitors |

### Premature Ejaculation (top 10 of 20 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38481411](https://pubmed.ncbi.nlm.nih.gov/38481411/) | 2024 | RCT | Arab J Urol | Head-to-head: tadalafil alone vs. dapoxetine alone vs. combination for PE |
| [18362486](https://pubmed.ncbi.nlm.nih.gov/18362486/) | 2008 | RCT | Urol Int | Tadalafil + fluoxetine, randomized double-blind placebo-controlled |
| [26981497](https://pubmed.ncbi.nlm.nih.gov/26981497/) | 2016 | RCT | Nephrourol Mon | Tadalafil + paroxetine vs. paroxetine alone for PE |
| [34773634](https://pubmed.ncbi.nlm.nih.gov/34773634/) | 2021 | RCT | Urol J | Dapoxetine/tadalafil vs. paroxetine/tadalafil combination therapies |
| [30544399](https://pubmed.ncbi.nlm.nih.gov/30544399/) | 2018 | Bayesian Network Meta-analysis | Medicine | PDE5 inhibitors vs. SSRIs for PE — comparative efficacy/safety |
| [37203851](https://pubmed.ncbi.nlm.nih.gov/37203851/) | 2023 | Retrospective Cohort | Eur Rev Med Pharmacol Sci | Daily paroxetine/tadalafil combination in PE + ED |
| [25768099](https://pubmed.ncbi.nlm.nih.gov/25768099/) | 2015 | Systematic Review (HTA) | Health Technol Assess | Interventions to treat PE, short report |
| [20189712](https://pubmed.ncbi.nlm.nih.gov/20189712/) | 2010 | Guideline | Eur Urol | EAU guidelines on ED and PE |
| [39034106](https://pubmed.ncbi.nlm.nih.gov/39034106/) | 2024 | Scoping Review | Sex Med Rev | Neurotransmitter systems in lifelong PE |
| [29527702](https://pubmed.ncbi.nlm.nih.gov/29527702/) | 2018 | RCT (placebo-controlled) | Andrologia | Daily tadalafil 5 mg monotherapy for PE |

### Psychologic Dyspareunia (both retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37952223](https://pubmed.ncbi.nlm.nih.gov/37952223/) | 2023 | Systematic Review | J Sex Med | Unconsummated marriage: etiology and management (indirect relevance) |
| [22612985](https://pubmed.ncbi.nlm.nih.gov/22612985/) | 2012 | Small uncontrolled study | J Sex Med | Tadalafil 5 mg daily in type 1 diabetic women with genital arousal disorder |

### Pulmonary Hypertension (top 10 of 18 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26308684](https://pubmed.ncbi.nlm.nih.gov/26308684/) | 2015 | RCT | N Engl J Med | AMBITION trial: initial ambrisentan+tadalafil in PAH |
| [38267108](https://pubmed.ncbi.nlm.nih.gov/38267108/) | 2024 | RCT | J Am Coll Cardiol | Macitentan/tadalafil single-tablet combination for PAH |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Diagnosis and treatment of PAH |
| [19470885](https://pubmed.ncbi.nlm.nih.gov/19470885/) | 2009 | Pivotal trial | Circulation | Original tadalafil therapy trial for PAH |
| [38939948](https://pubmed.ncbi.nlm.nih.gov/38939948/) | 2024 | Phase 3 RCT | Circulation | Tadalafil for combined post-/pre-capillary PH in HFpEF |
| [34593120](https://pubmed.ncbi.nlm.nih.gov/34593120/) | 2021 | Trial report | J Am Coll Cardiol | Three- vs. two-drug therapy in newly diagnosed PAH |
| [39316293](https://pubmed.ncbi.nlm.nih.gov/39316293/) | 2024 | Real-world evidence | Adv Ther | Macitentan+tadalafil in incident/prevalent PAH (OPUS/OrPHeUS) |
| [33472458](https://pubmed.ncbi.nlm.nih.gov/33472458/) | 2021 | Review | Expert Rev Respir Med | Lessons from upfront ambrisentan+tadalafil combination |
| [23129569](https://pubmed.ncbi.nlm.nih.gov/23129569/) | 2013 | Review | Ther Adv Respir Dis | Tadalafil as monotherapy and in combination regimens for PAH |
| [40934467](https://pubmed.ncbi.nlm.nih.gov/40934467/) | 2025 | Review | Cardiol Rev | Mechanisms, evidence, and emerging perspectives for tadalafil in PH |

### Benign Prostatic Hyperplasia (top 10 of 19 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30901259](https://pubmed.ncbi.nlm.nih.gov/30901259/) | 2019 | Review | Expert Opin Pharmacother | Tadalafil for treatment of BPH — mechanism and clinical data |
| [31625449](https://pubmed.ncbi.nlm.nih.gov/31625449/) | 2019 | Meta-analysis | Am J Mens Health | Tadalafil + tamsulosin vs. tadalafil alone in BPH+ED |
| [34712682](https://pubmed.ncbi.nlm.nih.gov/34712682/) | 2021 | Evidence-based Analysis (13 studies) | Front Med | 12-week tadalafil 5 mg monotherapy for LUTS/BPH |
| [24459652](https://pubmed.ncbi.nlm.nih.gov/24459652/) | 2013 | Systematic Review | World J Mens Health | LUTS/BPH and BPH+ED in Asian men, focus on tadalafil |
| [23816815](https://pubmed.ncbi.nlm.nih.gov/23816815/) | 2013 | Meta-analysis | Urol Int | Efficacy/safety of tadalafil monotherapy for LUTS/BPH |
| [26425140](https://pubmed.ncbi.nlm.nih.gov/26425140/) | 2015 | Review | Ther Adv Urol | Tadalafil for LUTS/BPH in Asian men, mechanism update |
| [21284024](https://pubmed.ncbi.nlm.nih.gov/21284024/) | 2011 | Review | Neurourol Urodyn | Pathophysiology/mechanism of tadalafil for LUTS/BPH |
| [39287476](https://pubmed.ncbi.nlm.nih.gov/39287476/) | 2024 | Cohort | J Intern Med | Tadalafil use and lower incidence of type 2 diabetes in men with BPH |
| [25083163](https://pubmed.ncbi.nlm.nih.gov/25083163/) | 2014 | Review | Ther Adv Urol | Tadalafil for BPH with and without ED |
| [23018613](https://pubmed.ncbi.nlm.nih.gov/23018613/) | 2012 | Review | Drugs Aging | Tadalafil in signs/symptoms of BPH with or without ED |

---

## Malaysia Market Information

Tadalafil is confirmed as **already marketed in Malaysia** with **23 NPRA registrations**. However, this evidence pack does not contain the underlying license-level detail (registration numbers, product names, dosage forms, manufacturers, or approved indication text) — all license fields in the source data are empty. This is a listed Blocking data gap (see Conclusion) and needs to be pulled directly from the NPRA product registry before a market-position or label-gap analysis can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction data were available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Mixed — Proceed with Guardrails (ED / PAH / BPH, confirmatory) · Research Question (Premature Ejaculation) · Hold (Psychologic Dyspareunia)**

**Rationale:**
- ED, PAH, and BPH each have L1 evidence (multiple completed Phase 3 RCTs, including pivotal trials like AMBITION for PAH), but the evidence pack itself flags these as already-approved uses elsewhere rather than novel repurposing — their value here is confirming model validity and checking whether the Malaysia label already covers them.
- Premature ejaculation has L2 evidence (one large completed Phase 3 RCT plus supportive combination-therapy literature) but the mechanistic case rests mainly on tadalafil-plus-SSRI combinations rather than tadalafil monotherapy, so it merits further research before any label or clinical guidance decision.
- Psychologic dyspareunia has only L4, indirect evidence (no clinical trials, 2 tangential publications) and should not proceed further without new, disease-specific data.

**To proceed, the following is needed:**
- Malaysia NPRA package insert / label text (Blocking gap — currently blocks the safety (S1) review stage entirely; this must be resolved before any of the five candidates can move forward on safety grounds)
- Formal DrugBank/labeled MOA reference to replace the currently inferred mechanistic narrative
- License-level NPRA registration detail (product names, dosage forms, current approved indications) to determine whether ED/PAH/BPH indications are already on the Malaysia label or represent a genuine label-expansion opportunity
- For premature ejaculation: dedicated tadalafil-monotherapy trial data (separate from SSRI-combination trials) to strengthen the causal case
- Drug-drug interaction data (current query returned no results) before any clinical recommendation, especially given known nitrate/alpha-blocker interaction concerns for PDE5 inhibitors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

