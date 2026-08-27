---
layout: default
title: Bupropion
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Bupropion
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

Using **txgnn-pipeline** background knowledge is not directly applicable here (this is a report-writing task, not a pipeline/training operation), so I'm proceeding directly with report generation per the v5 prompt template, using only the data present in the Evidence Pack.

A few data-handling notes before the report:
- `original_moa` and `original_indications` are both empty/`[Data Gap]` in this pack. Bupropion's original indications (Major Depressive Disorder, Smoking Cessation) are well-established public pharmacological facts (not fabricated), but the **NPRA-specific approved indication text is not available** in this pack (DG001) — this is flagged explicitly rather than invented.
- `taiwan_regulatory.licenses` contains 2 entries but every field is an empty string — so no per-license table is presented; this is stated plainly instead of showing a blank table.
- Bupropion is not an antineoplastic drug → the Cytotoxicity section is omitted per the rules.
- All `safety` fields are `[Data Gap]` or empty → fallback safety text is used, with DG001 (Blocking) flagged.

---

# Bupropion: From Depression to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Bupropion is a norepinephrine–dopamine reuptake inhibitor (NDRI) originally used to treat depression and to support smoking cessation.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> with **8 clinical trials** (including one completed Phase 3 RCT) and **19 publications** (including a Cochrane systematic review) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression / Smoking cessation (well-established public indications; NPRA-specific approved indication text is not available in this data pack — see Data Gap DG001) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap (DG002) for this pack. Based on known pharmacology, however, bupropion is a norepinephrine–dopamine reuptake inhibitor (NDRI) that lacks serotonergic activity, distinguishing it from most other antidepressants. It is marketed in the class of atypical antidepressants and, separately, as a smoking-cessation aid, and its efficacy in depression is well established.

Mechanistically, this dopamine/norepinephrine reuptake-inhibition profile is directly relevant to ADHD, whose core pathology is understood to involve prefrontal cortical dopaminergic and noradrenergic hypofunction. This is the same neurochemical target engaged by first-line ADHD stimulants and by atomoxetine (a selective norepinephrine reuptake inhibitor), giving bupropion a plausible, class-consistent rationale as a non-stimulant ADHD option.

This mechanistic plausibility is reinforced by substantial real-world and trial evidence: bupropion has already been studied off-label in ADHD across multiple populations (adults, adolescents, and patients with comorbid substance-use disorders), and is discussed as a nonstimulant alternative in several systematic reviews and network meta-analyses, including a Cochrane review dedicated specifically to bupropion in adult ADHD. Its effect size is generally described as smaller than stimulants but superior to placebo, consistent with a genuine but modest treatment effect rather than a spurious knowledge-graph association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | Multicenter, randomized, double-blind, placebo-controlled, flexible-dose (300–450 mg/day) trial of extended-release bupropion for adult ADHD — direct efficacy/safety evidence |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | Treatment of adult ADHD in patients on methadone maintenance |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Post-marketing confirmatory trial of bupropion for ADHD in adolescents with comorbid substance use disorder |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | N/A | Completed | 32 | Open-label study of bupropion SR for adult ADHD with recent/current substance use disorder |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | N/A | Completed | 32 | Early trial evaluating cocaine abuse and comorbid Attention Deficit Disorder |
| [NCT03326128](https://clinicaltrials.gov/study/NCT03326128) | Phase 2 | Terminated | 12 | High-dose bupropion pilot for smoking cessation — not an ADHD efficacy trial, low relevance |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Withdrawn (0 enrolled); explored bupropion/naltrexone effects on craving and inhibitory control in stimulant-use disorder with/without ADHD |
| [NCT00330434](https://clinicaltrials.gov/study/NCT00330434) | N/A | Withdrawn | 0 | Withdrawn; pharmacokinetic/CYP2B6 metabolism study, not an ADHD efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Cochrane systematic review specifically evaluating bupropion for adult ADHD |
| [27813651](https://pubmed.ncbi.nlm.nih.gov/27813651/) | 2017 | Review | J Child Adolesc Psychopharmacol | Systematic review of bupropion use for ADHD in children and adolescents |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Review | Health Psychology Research | Review of bupropion's pharmacokinetics/dynamics and mechanisms across depression, ADHD, and smoking cessation |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Review (Network Meta-analysis) | The Lancet Psychiatry | Comparative efficacy/tolerability network meta-analysis of ADHD medications across age groups |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Review (Network Meta-analysis) | PLoS ONE | Systematic review and NMA of pharmacologic treatments for adult ADHD |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Review | Expert Rev Neurother | Review of current nonstimulant medications for adult ADHD |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Review (Bayesian NMA) | J Psychiatric Research | Bayesian network meta-analysis of monoamine reuptake inhibitors (incl. bupropion) in ADHD |
| [26693882](https://pubmed.ncbi.nlm.nih.gov/26693882/) | 2016 | Review | Expert Rev Neurother | Systematic review of alternative pharmacological strategies for adult ADHD |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Current Pharmaceutical Design | Review of ADHD psychopharmacology, listing bupropion among common treatment options |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Review | American Family Physician | Clinical review of ADHD diagnosis and treatment in adults |

---

## Malaysia Market Information

Bupropion is registered in Malaysia with NPRA (**market status: Marketed, 2 total registrations**). However, this data pack does not contain the individual license numbers, product names, dosage forms, or approved indication text for these registrations — retrieving the NPRA product label (DG001) is required to complete this section.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug–drug interaction data were not available in this evidence pack (flagged as DG001, a **Blocking** data gap — this must be resolved before any safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The predicted indication is supported by strong, direct evidence: one completed Phase 3 RCT, several additional completed trials across relevant populations, and a Cochrane systematic review dedicated specifically to bupropion in adult ADHD, together with multiple network meta-analyses situating bupropion among recognized nonstimulant ADHD options (Evidence Level L1).
- Despite this efficacy evidence, safety data (warnings, contraindications, DDI) is entirely missing from this pack, and NPRA-specific label content is also unavailable — both are prerequisites before any clinical or regulatory pathway can be pursued.

**To proceed, the following is needed:**
- TFDA/NPRA product label — warnings and contraindications (DG001, Blocking)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Malaysia-specific license details and approved indication text for the 2 registered products
- Formal drug–drug interaction (DDI) review, particularly for CYP2B6 substrates and seizure-threshold–lowering agents given bupropion's known class risk

---

*Note: Nine additional TxGNN-predicted indications for bupropion were reviewed in this evidence pack (rank 2–10). Rank 2 ("ADHD, inattentive type") is a clinical subtype of the primary indication above and inherits the same mechanistic rationale (L3, Research Question). Ranks 3–10 (e.g., faciodigitogenital syndrome, chondromyxoid fibroma, hypervitaminosis) had no supporting clinical trials or literature and were assessed as likely knowledge-graph embedding noise (L5, Hold) — they are not carried forward in this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

