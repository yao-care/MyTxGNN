---
layout: default
title: Clomipramine
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Clomipramine
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

# Clomipramine: From Depression to Anxiety Disorder

## One-Sentence Summary

Clomipramine is a tricyclic antidepressant (TCA) with potent serotonin reuptake inhibition, historically established for depression and obsessive-compulsive disorder (OCD).
The TxGNN model's top-ranked prediction is **Anxiety Disorder**, but the supporting evidence in this pack is dominated by OCD trials that appear to be mislabeled under this node, with **19 clinical trials** and **20 publications** retrieved — most only indirectly relevant.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from NPRA license data (all fields blank in this pack); based on the literature retrieved, Clomipramine's established original indications are **depression** and **obsessive-compulsive disorder (OCD)** |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this evidence pack (data gap DG002). Based on the literature retrieved here (e.g., PMID 2178909), Clomipramine is a tricyclic antidepressant that is a particularly strong inhibitor of serotonin (5-HT) reuptake, with weaker noradrenergic effects — the pharmacological basis for its established use in depression and OCD.

Anxiety disorders, depression, and OCD share overlapping serotonergic pathophysiology, so a mechanistic link to anxiety is plausible. Older literature (1980s–1990s RCTs, largely predating ClinicalTrials.gov registration) does support Clomipramine's efficacy specifically in **panic disorder and agoraphobia** — see the separate "agoraphobia" prediction node in this pack, which carries more directly relevant RCT evidence.

However, for the "anxiety disorder" node specifically, the retrieved clinical trials are dominated by OCD studies (troriluzole augmentation, quetiapine augmentation, rTMS, pediatric OCD strategies) rather than trials in anxiety disorder itself — several evidence items explicitly flag this as a labeling/mapping issue rather than true topical relevance. The prediction is mechanistically credible, but the current evidence bundle does not yet distinguish which anxiety subtype (panic disorder vs. generalized anxiety disorder) is actually supported.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Troriluzole as adjunct in OCD patients with inadequate response to SSRI/clomipramine/venlafaxine — not a clomipramine efficacy trial |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Completed | 44 | Quetiapine augmentation of SSRI/clomipramine in severe OCD |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Open-label comparison of clomipramine augmentation vs. quetiapine augmentation of SSRIs in SSRI-refractory OCD |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Predicts medication response comparing clomipramine vs. escitalopram (or duloxetine) in OCD |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Completed | 54 | Double-blind augmentation strategies in OCD non-responders; one arm is fluoxetine + clomipramine |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT added to SRI treatment (including clomipramine class) in pediatric OCD partial responders |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Unknown | 76 | Direct clomipramine trial: IV vs. oral pulse-loading followed by maintenance therapy in OCD |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Pharmacovigilance study of psychopharmacological treatment (incl. TCAs) in gerontopsychiatric inpatients |
| [NCT02431845](https://clinicaltrials.gov/study/NCT02431845) | N/A | Recruiting | 200 | Pharmaco(epi)genetic/proteomic/microbiomic study of SSRI response in OCD |
| [NCT04708834](https://clinicaltrials.gov/study/NCT04708834) | Phase 3 | Terminated | 772 | Long-term safety of troriluzole adjunctive therapy in OCD |

**Note:** None of these trials directly evaluate Clomipramine for "anxiety disorder" as a primary endpoint — most are OCD trials in which clomipramine appears as a comparator, prior treatment, or augmentation partner.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Network meta-analysis of pharmacological treatments for panic disorder in adults |
| [3887445](https://pubmed.ncbi.nlm.nih.gov/3887445/) | 1985 | RCT | Psychiatry Research | 12-week double-blind trial: clomipramine vs. imipramine in OCD, both showed modest symptom reduction |
| [9786103](https://pubmed.ncbi.nlm.nih.gov/9786103/) | 1998 | RCT | J Clin Pharm Ther | Double-blind, placebo-controlled trial of clomipramine + nortriptyline combination in OCD |
| [1474179](https://pubmed.ncbi.nlm.nih.gov/1474179/) | 1992 | RCT/Cohort | J Clin Psychopharmacol | Compares clomipramine, clonazepam, and clonidine against control in OCD |
| [1933762](https://pubmed.ncbi.nlm.nih.gov/1933762/) | 1991 | RCT | Can J Psychiatry | IV clomipramine used successfully in a treatment-resistant OCD case after oral therapy failed |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week placebo-controlled comparison of paroxetine, clomipramine, and cognitive therapy in panic disorder |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | Systematic Review/Meta-analysis | J Am Acad Child Adolesc Psychiatry | Meta-analysis of early treatment response to SSRIs vs. clomipramine in pediatric OCD |
| [8263222](https://pubmed.ncbi.nlm.nih.gov/8263222/) | 1993 | Meta-analysis | J Behav Ther Exp Psychiatry | Meta-analysis of clomipramine, fluoxetine, and behavior therapy for OCD |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Review | Drugs | Overview of clomipramine's pharmacology and therapeutic use in OCD and panic disorder |
| [7795952](https://pubmed.ncbi.nlm.nih.gov/7795952/) | 1995 | Review | J Child Adolesc Psychiatr Nurs | Review of clomipramine's serotonergic mechanism and side-effect profile in pediatric OCD |

## Malaysia Market Information

NPRA records show **2 active registrations** for Clomipramine, but individual license details (license number, product name, dosage form, approved indication text) were not returned in this data pull — all fields came back blank. These need to be retrieved directly from the NPRA product registration database (QUEST3+) before market-status claims can be finalized.

## Safety Considerations

Please refer to the package insert for safety information. (Note: the underlying data gap — missing TFDA/NPRA package-insert warnings and contraindications — is flagged as **Blocking severity** in this evidence pack, meaning a formal safety pre-assessment (S1) cannot yet be completed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two issues block advancement: (1) the package-insert warnings/contraindications data gap (DG001) is explicitly rated Blocking, preventing the S1 safety pre-assessment required before any Go/Proceed recommendation; (2) the clinical evidence attached to "anxiety disorder" is largely mislabeled OCD-trial data rather than trials in anxiety disorder itself, so the true evidence level for this specific indication is weaker than the L2 rating suggests until the subtype is clarified. Separately, this evidence pack also reveals that the model's high-scoring OCD and depression predictions (ranks 2 and 9) are not novel repurposing candidates — they are Clomipramine's already-approved original indications — so they should not be treated as new opportunities.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/NPRA package insert for warnings, contraindications, and drug interactions (remediation for DG001)
- Query DrugBank for confirmed mechanism-of-action data (remediation for DG002)
- Obtain full NPRA license details (license number, product name, dosage form, approved indication text) for the 2 registered products
- Re-run evidence collection for "anxiety disorder" with disambiguation between panic disorder/agoraphobia and generalized anxiety disorder, excluding trials whose primary condition is OCD
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

