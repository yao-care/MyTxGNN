---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 5
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy to Epilepsy with Generalized Tonic-Clonic Seizures

> **Data note**: This evidence pack does not contain a captured original-indication text (license records are blank; `original_indications` is empty; MOA is flagged `[Data Gap]`). The "Epilepsy" starting point above reflects Carbamazepine's well-established pharmacological classification as a first-line antiepileptic, not a value extracted from the Malaysia regulatory record in this pack.

## One-Sentence Summary

Carbamazepine is a classic antiepileptic (dibenzazepine-class sodium-channel blocker), long used for epilepsy, trigeminal neuralgia, and bipolar disorder. The TxGNN model's top prediction is **Epilepsy with Generalized Tonic-Clonic Seizures**, supported by **7 clinical trials** and **20 publications** — but the TxGNN score is **0.00%**, and this "predicted" indication is a clinical subtype of the disease Carbamazepine is already used to treat, not a genuinely novel target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (license text blank); by established classification, Carbamazepine is a classic antiepileptic |
| Predicted New Indication | Epilepsy with generalized tonic-clonic seizures |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002, High severity). Based on known pharmacological classification, Carbamazepine is a dibenzazepine-class anticonvulsant that acts primarily via voltage-gated sodium channel blockade to reduce neuronal excitability, and its efficacy across seizure types — including generalized tonic-clonic seizures — has been established for decades.

The relationship between the "original" and "predicted new" indication here is not repurposing in the usual sense: epilepsy with generalized tonic-clonic seizures is a clinical subtype of epilepsy, the disease area Carbamazepine already treats as first-line therapy. This is corroborated by the clinical trial evidence below, where Carbamazepine (CR) consistently appears as the **active comparator/reference arm** in monotherapy trials of newer AEDs (lacosamide, levetiracetam), rather than as an investigational agent being tested for a new disease.

Combined with a TxGNN score of 0.00%, this strongly suggests the knowledge graph is re-identifying an already-known drug-disease relationship rather than surfacing a genuine repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01243177](https://clinicaltrials.gov/study/NCT01243177) | Phase 3 | Completed | 888 | Lacosamide vs. Carbamazepine-CR monotherapy, non-inferiority design, 6-month seizure freedom endpoint in newly diagnosed partial-onset/GTC seizures |
| [NCT01465997](https://clinicaltrials.gov/study/NCT01465997) | Phase 3 | Completed | 551 | Long-term safety follow-up comparing Lacosamide to Carbamazepine-CR monotherapy in partial-onset/GTC seizures |
| [NCT00150735](https://clinicaltrials.gov/study/NCT00150735) | Phase 3 | Completed | 580 | Levetiracetam vs. Carbamazepine monotherapy (up to 121 weeks) in newly diagnosed epilepsy with partial or GTC seizures |
| [NCT02208492](https://clinicaltrials.gov/study/NCT02208492) | Phase 4 | Completed | 75 | Cognitive function effects: Levetiracetam vs. Carbamazepine monotherapy in pediatric partial seizure |
| [NCT04836559](https://clinicaltrials.gov/study/NCT04836559) | Phase 2 | Completed | 110 | JNJ-40411813 adjunctive therapy in focal-onset seizures with suboptimal response to levetiracetam/brivaracetam (Carbamazepine as background AED context) |
| [NCT07443241](https://clinicaltrials.gov/study/NCT07443241) | N/A | Completed | 779 | Retrospective analysis of sex-specific differences in status epilepticus etiology, treatment, outcome |
| [NCT00208520](https://clinicaltrials.gov/study/NCT00208520) | N/A | Unknown | 60 | SLICE study: second-line AED choice after inadequate response to valproate in partial/tonic-clonic seizures |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1298221](https://pubmed.ncbi.nlm.nih.gov/1298221/) | 1992 | RCT | The New England Journal of Medicine | VA Cooperative Study 264: Valproate vs. Carbamazepine for complex partial and secondarily generalized tonic-clonic seizures |
| [3121296](https://pubmed.ncbi.nlm.nih.gov/3121296/) | 1987 | Clinical synthesis | Epilepsia | Reviews VA Epilepsy Cooperative Study findings establishing Carbamazepine as drug of choice for partial/secondarily GTC seizures |
| [29602083](https://pubmed.ncbi.nlm.nih.gov/29602083/) | 2018 | Review | Epilepsy & Behavior | Evidence-based guide to AED selection for GTCS, evaluating regulatory data across 8 approved agents |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Current role of Carbamazepine and Oxcarbazepine in epilepsy management given newer AED options |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Review | Continuum (Minneapolis, Minn.) | Comprehensive review of AED pharmacology, indications, and clinical use, including Carbamazepine |
| [19445769](https://pubmed.ncbi.nlm.nih.gov/19445769/) | 2009 | Review | BMJ Clinical Evidence | Epilepsy treatment overview and evidence summary |
| [29020805](https://pubmed.ncbi.nlm.nih.gov/29020805/) | 2018 | Review | The Annals of Pharmacotherapy | Pharmacology, efficacy, safety, and drug interactions of IV Carbamazepine (Carnexiv) for seizures in adults |
| [10530693](https://pubmed.ncbi.nlm.nih.gov/10530693/) | 1999 | Review | Epilepsia | Discusses Carbamazepine's established first-line role and limitations (toxicity, autoinduction, drug interactions) |
| [24370318](https://pubmed.ncbi.nlm.nih.gov/24370318/) | 2014 | Observational | Seizure | Evaluates Carbamazepine efficacy specifically for GTCS in idiopathic generalized epilepsy |
| [37872695](https://pubmed.ncbi.nlm.nih.gov/37872695/) | 2024 | Observational | Epilepsia | Electroclinical features and prognostic patterns of epilepsy with GTC seizures alone (large cohort) |

## Malaysia Market Information

The evidence pack records 8 total NPRA registrations and a "Marketed" status, but the individual license records (authorization number, product name, dosage form, manufacturer, approved indication text) are all blank in this pack — this is a data completeness gap, not an absence of registrations. License-level detail needs to be re-extracted from the source before it can be reported.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps in this pack — notably DG001, "TFDA warnings/contraindications," is marked **Blocking** severity because it prevents entry into the S1 safety initial review.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- DG001 is a **Blocking** data gap — without warnings/contraindications data, this candidate cannot pass S1 safety review regardless of efficacy evidence.
- The top-ranked "predicted new indication" (epilepsy with GTCS) overlaps with Carbamazepine's already-established primary indication rather than representing a novel disease area, and the TxGNN score itself is 0.00% — there is no real predictive signal here, only re-identification of a known relationship.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) to clear the blocking safety gap
- DrugBank mechanism-of-action detail (DG002)
- Malaysia license-level detail (authorization numbers, product names, approved indication text) — currently blank despite 8 registrations
- A re-check of whether "epilepsy with GTCS" should be deprioritized as a non-novel candidate, in favor of examining lower-ranked but more clinically distinct predictions (e.g., glossopharyngeal neuralgia, rank 4) that represent genuine off-label extensions rather than restatements of the primary indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

