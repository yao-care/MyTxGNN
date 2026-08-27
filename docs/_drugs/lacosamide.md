---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy (Partial-Onset Seizures) to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is a third-generation antiepileptic drug (AED) whose approved use is for partial-onset (focal) seizures. The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, but the current evidence base — 1 clinical trial and 14 publications retrieved — predominantly addresses **bipolar depression**, not the manic phase specifically, so the disease-direction match needs confirmation before this can be treated as strong support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial-onset (focal) seizures (adjunctive/monotherapy); *Malaysia-specific approved indication text unavailable — NPRA license records for this pull are empty* |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lacosamide (`original_moa` is a data gap). Based on information surfaced within the literature evidence itself, Lacosamide selectively enhances the slow inactivation of voltage-gated sodium channels, producing extended stabilisation of neuronal cell membranes (PMID 28845834) — the same general mechanism by which other AEDs (valproate, lamotrigine, carbamazepine) act as mood stabilisers in bipolar disorder. This gives a class-level precedent for repurposing an AED into psychiatric indications.

However, the disease-direction match is imprecise: the predicted indication is specifically "manic" bipolar disorder, but nearly all supporting evidence (the ongoing Phase 3 trial, the retrospective cohort study, and the open-label pilot) targets **bipolar depression**, not mania. One retrospective study did report improvement in both depressive and manic symptoms in an open-label setting, so a mechanistic link to mood stabilisation broadly is plausible, but indication-specific (manic-phase) evidence is currently thin.

**Note:** Among the 10 TxGNN-predicted indications in this evidence pack, rank 5 ("migraine disorder") has substantially stronger supporting evidence (Evidence Level L1, 6 clinical trials including 3 completed Phase 2/3 RCTs directly testing lacosamide) than this rank-1 candidate. If evaluating which candidate to prioritize for investment, migraine disorder warrants separate review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Evaluates lacosamide as augmentation to first-/second-line treatment for moderate-to-severe major depressive episodes in Bipolar Disorder Types I and II (randomized, double-blind, parallel-group); tests depressive-episode efficacy, not the manic phase specifically. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide vs. other antiepileptics in bipolar disorder patients without epilepsy — direct comparative clinical evidence. |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week open-label pilot assessing efficacy/safety of lacosamide for bipolar depression. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Clinical stabilisation of mood disorder comorbid with PTSD and fronto-temporal epilepsy using lacosamide; describes sodium-channel slow-inactivation mechanism. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report (adverse event) | Indian J Psychol Med | Lacosamide-precipitated neutropenia in a patient with bipolar disorder and comorbid epilepsy. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case report | Cureus | Bipolar I patient with multiple comorbidities including seizure-like activity; contextual case, not a treatment efficacy study. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | Review of therapeutic drug monitoring for AEDs; notes AEDs are also used for bipolar disorder management generally. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chem Neurosci | Review of CRMP2 druggability, relevant to the sodium-channel/CRMP2 mechanism shared across AED mood applications. |

---

## Malaysia Market Information

NPRA records confirm Lacosamide is marketed in Malaysia with **4 active licenses**, but the detailed license fields (authorization number, product name, dosage form, approved indication text) were all returned empty in this data pull — this is a data gap, not an absence of registration.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data were retrievable in this pull — TFDA/NPRA label data is flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence Level L3 with only a single, small (n=40), still-recruiting Phase 3 trial and no completed RCTs specific to the manic phase is insufficient to progress. The strongest existing evidence targets bipolar *depression*, not the *manic* episodes named by this predicted indication — the disease-direction match itself needs confirmation. Additionally, TFDA/NPRA safety label data (warnings/contraindications) is a Blocking gap, which prevents any S1 safety pre-screen.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings and contraindications) — Blocking gap (DG001)
- DrugBank-sourced mechanism of action data — High-priority gap (DG002)
- Confirmation of indication direction: manic-phase-specific evidence, vs. the depression-phase evidence currently available
- Results from NCT07412132 upon completion (expected 2027-01)
- Complete NPRA license detail (product names, dosage forms, approved indication text) for the 4 registered licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

