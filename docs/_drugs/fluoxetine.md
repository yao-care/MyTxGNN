---
layout: default
title: Fluoxetine
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# Fluoxetine: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

> Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) widely used as an antidepressant. The TxGNN model's top-ranked prediction links it to **Obsessive-Compulsive Disorder (OCD)**, supported by **31 clinical trials** and **20 publications** — though this evidence largely confirms an indication fluoxetine already holds internationally rather than a genuinely novel repurposing hypothesis (see caveat below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Malaysia dataset (all `approved_indication_text` fields are blank). Fluoxetine is broadly known as an antidepressant (SSRI class); Malaysia-specific label text is unverified — see Data Gap DG001. |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (Data Gap DG002). Based on the evidence pack's own rationale, fluoxetine is a selective serotonin reuptake inhibitor (SSRI) that blocks presynaptic serotonin reuptake, raising serotonin concentration in the prefrontal cortex–striatum–thalamus circuit — the core pharmacological pathway underlying OCD pharmacotherapy.

**Important caveat**: the evidence pack itself notes that OCD is *"an existing approved indication for fluoxetine, not a new drug-repurposing hypothesis"* (fluoxetine has held OCD approval in most major markets for decades, alongside major depressive disorder). The very large trial/literature base here therefore reflects mature, established clinical use rather than an emerging signal — this should be read as **evidence consolidation**, not discovery.

A more genuinely incremental signal in this evidence pack is **dysthymic disorder / persistent depressive disorder** (rank 10, L2), which shares fluoxetine's serotonergic mechanism with major depression but is a distinct chronic-course diagnosis, and is backed by two placebo-controlled RCTs (PMID 15653941, PMID 9160652) specifically in this population — worth flagging alongside the top-ranked OCD result.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Efficacy of ERP and SSRIs (and predictors of response) for OCD in a Chinese population — Grade A, directly relevant |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomized open trial comparing group CBT vs. fluoxetine for OCD — Grade A, direct head-to-head evidence |
| [NCT00592852](https://clinicaltrials.gov/study/NCT00592852) | Phase 4 | Terminated | 13 | Pilot study of fluoxetine for OCD in children/adolescents with comorbid bipolar disorder — Grade A, terminated early but direct |
| [NCT00245635](https://clinicaltrials.gov/study/NCT00245635) | Phase 4 | Completed | 43 | Fluoxetine in pediatric body dysmorphic disorder (OCD-spectrum) — Grade B |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Clinical/neuroimaging predictors of treatment response in OCD — Grade B |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Completed | 54 | Double-blind augmentation strategies (fluoxetine + quetiapine / + clomipramine) for OCD non-responders |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT augmentation of SRI treatment in pediatric OCD partial responders |
| [NCT00758966](https://clinicaltrials.gov/study/NCT00758966) | Phase 2 | Terminated | 8 | Naltrexone SR ± fluoxetine for OCD, proof-of-concept |
| [NCT04899687](https://clinicaltrials.gov/study/NCT04899687) | Phase 2 | Recruiting | 60 | Fluoxetine + dextromethorphan open-label crossover pilot in OCD and related disorders |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | N/A | Completed | 144 | Adaptive pharmacotherapy strategies (incl. fluoxetine) for pediatric OCD in public health context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32242450](https://pubmed.ncbi.nlm.nih.gov/32242450/) | 2020 | Review (Tier 1) | Nordic J Psychiatry | Systematic review/meta-analysis of fluoxetine in acute treatment of pediatric OCD |
| [8263222](https://pubmed.ncbi.nlm.nih.gov/8263222/) | 1993 | RCT (Tier 1) | J Behav Ther Exp Psychiatry | Meta-analysis: clomipramine, fluoxetine, and behavior therapy all effective for OCD |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Review (Tier 2) | Compr Psychiatry | Long-term safety/tolerability of off-label high-dose SSRIs in OCD |
| [2140372](https://pubmed.ncbi.nlm.nih.gov/2140372/) | 1990 | Cohort (Tier 2) | J Clin Psychopharmacol | Retrospective comparison of clomipramine vs. fluoxetine efficacy/side effects in OCD |
| [11437015](https://pubmed.ncbi.nlm.nih.gov/11437015/) | 2001 | RCT | J Am Acad Child Adolesc Psychiatry | 13-week double-blind placebo-controlled trial of fluoxetine in pediatric OCD |
| [9286186](https://pubmed.ncbi.nlm.nih.gov/9286186/) | 1997 | RCT | Am J Psychiatry | Placebo-controlled trial of fluoxetine vs. phenelzine for OCD |
| [31638682](https://pubmed.ncbi.nlm.nih.gov/31638682/) | 2019 | RCT | JAMA | RCT of fluoxetine for obsessive-compulsive behaviors in children/adolescents with ASD |
| [3894437](https://pubmed.ncbi.nlm.nih.gov/3894437/) | 1985 | Cohort | J Clin Psychopharmacol | Early single-blind trial establishing fluoxetine's effect on OCD symptoms |
| [1429485](https://pubmed.ncbi.nlm.nih.gov/1429485/) | 1992 | Review | J Clin Psychiatry | Review of serotonergic antidepressants' efficacy in OCD, including fluoxetine |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacol Bull | Mono/polypharmacotherapy of OCD; fluoxetine among approved SRIs |

---

## Malaysia Market Information

NPRA records confirm **7 active registrations** for fluoxetine in Malaysia (market status: ✓ Marketed). However, license-level details (authorization number, product name, dosage form, and approved indication text) are not populated in the current dataset — this is a data gap, not a confirmed absence of registration detail.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note**: Package insert warnings/contraindications (Data Gap DG001) are marked as **Blocking** in the source data — this specifically prevents the candidate from entering the S1 safety pre-assessment stage. Drug interaction (DDI) lookup also returned no results.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The OCD signal is backed by L1-tier evidence (a Phase 4 RCT and multiple supporting trials/reviews), but this largely reflects fluoxetine's already-established indication rather than new repurposing evidence, and a **Blocking** data gap (missing TFDA/NPRA package insert) currently prevents formal safety pre-assessment (S1).

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — Blocking gap, required before any safety assessment
- DrugBank-sourced mechanism of action confirmation
- Malaysia-specific license details (product name, dosage form, approved indication text) to verify whether OCD is already a registered indication locally
- If pursuing a genuinely incremental signal, consider evaluating dysthymic disorder (rank 10, L2, two supporting placebo-controlled RCTs) as a parallel candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

