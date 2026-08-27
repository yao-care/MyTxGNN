---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 5
---

# Citalopram
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

# Citalopram: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) originally used for depression. The TxGNN model predicts it may also be effective for **Obsessive-Compulsive Disorder (OCD)**, with **30 clinical trials** and **16 publications** currently supporting this direction — though most of the trial-level evidence is for escitalopram (citalopram's S-enantiomer) rather than citalopram itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (SSRI class; specific NPRA-approved indication text not extracted in the current data pull) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 27 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action (MOA) data for citalopram is not available in the evidence pack. Based on known information, citalopram is a selective serotonin reuptake inhibitor (SSRI) — this classification is confirmed directly in the evidence pack's repurposing rationale. Its efficacy in depression, the established SSRI indication, is well proven, and mechanistically SSRIs are already recognized as first-line pharmacotherapy for OCD, since OCD pathophysiology is strongly linked to serotonergic dysregulation.

This is not a purely speculative model association: SSRIs already appear in most clinical treatment guidelines for OCD, and citalopram-specific studies (see Literature Evidence below) support this class effect directly, giving the prediction real clinical grounding beyond the TxGNN score alone.

**Caveat:** Four other TxGNN-predicted indications for citalopram in this same batch — paranoid, schizotypal, schizoid, and histrionic personality disorder — share an identical prediction score (99.68%). This strongly suggests a model artifact (clustering on the "personality disorder" disease category) rather than independent, disease-specific signals. All four carry a **Hold** recommendation and are excluded from further evidence review here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | Unknown | 40 | Escitalopram in adolescents with OCD — efficacy, safety, and effects on executive function/brain activation |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | ERP vs SSRIs vs combination for OCD; predictors of treatment response in a Chinese population |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Escitalopram for OCD — efficacy and optimal treatment dose |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Conventional (20mg) vs high-dose (40mg) escitalopram in OCD, randomized double-blind multicenter trial |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study of escitalopram safety/effectiveness for OCD symptoms |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label high-dose (up to 50mg) escitalopram for OCD, tolerability and efficacy |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Completed | 12 | fMRI study of citalopram's effect on restricted repetitive behaviors in autism spectrum disorder |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | Citalopram vs placebo for repetitive behavior in children with autism |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT augmentation of SRI treatment in pediatric OCD partial responders |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Naturalistic follow-up of clinical/neurocognitive/neuroimaging predictors of OCD treatment response |

*Note: most directly relevant OCD trials above use escitalopram (citalopram's active S-enantiomer), not citalopram itself; NCT00609531 and NCT00086645 use citalopram but for autism-related repetitive behavior rather than OCD.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | RCT | European Psychiatry | Citalopram vs citalopram+clomipramine in treatment-resistant OCD, 90-day open-label trial |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | RCT | International Clinical Psychopharmacology | Reviews citalopram's effectiveness for OCD alongside its role in OCD neurobiology research |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label study | Psychiatry and Clinical Neurosciences | Citalopram in children/adolescents with OCD — 8-week efficacy/tolerability report |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Review/Meta-analysis | Journal of Psychiatric Research | Network meta-analysis comparing pharmacological and psychological treatments for pediatric OCD |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Review | Comprehensive Psychiatry | Safety/tolerability of off-label high-dose SRIs (including SSRIs) in OCD |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Systematic Review | Expert Opinion on Pharmacotherapy | Efficacy/tolerability of pharmacotherapy for obsessive-compulsive personality disorder |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Antidepressant efficacy/tolerability/suicidality in children and adolescents, covering OCD |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clinical Evidence | Overview of OCD epidemiology and treatment evidence |
| [19454066](https://pubmed.ncbi.nlm.nih.gov/19454066/) | 2007 | Review | BMJ Clinical Evidence | Earlier overview of OCD epidemiology and treatment evidence |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World Journal of Biological Psychiatry | OCD's shift from rare disorder to serotonin-linked, SSRI-responsive condition |

---

## Malaysia Market Information

Citalopram is currently marketed in Malaysia with **27 active registrations**. License-level detail (registration numbers, product names, dosage forms, approved indication text) was not returned in the current NPRA data extraction and requires a follow-up data pull before it can be reported here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Citalopram's SSRI mechanism directly supports OCD treatment, and this is reinforced by multiple Phase 2–4 trials (mostly escitalopram) and citalopram-specific RCT/open-label evidence in the literature. However, the drug-level safety data (warnings, contraindications) needed for a formal safety assessment is currently a **blocking data gap**, so guardrails are required before this proceeds further.

**To proceed, the following is needed:**
- Official product label warnings and contraindications for citalopram (currently blocking, marked Severity: Blocking in the evidence pack)
- Detailed mechanism-of-action (MOA) documentation from DrugBank
- License-level Malaysia market data (registration numbers, product names, approved indication text)
- Clarification on whether the escitalopram-based trial evidence should be treated as directly applicable to citalopram or only as supportive class-effect evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

