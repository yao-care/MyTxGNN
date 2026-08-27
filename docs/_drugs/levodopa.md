---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 5
---

# Levodopa
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

Using the drug-repurposing evaluation report prompt (v5) rules already supplied, here is the report generated directly from the Evidence Pack.

---

# Levodopa: From Parkinson's Disease to Parkinsonian Disorder

## One-Sentence Summary

Levodopa is the long-standing gold-standard dopamine-replacement therapy for idiopathic **Parkinson's disease** (confirmed within this evidence pack itself as candidate rank 4, "non-repurposing / original indication"). The TxGNN model's top-ranked prediction broadens this to the wider diagnostic category of **Parkinsonian Disorder**, which is currently supported by **50 clinical trials** and **20 publications**, though several of the underlying diseases in this umbrella term (e.g. atypical/vascular parkinsonism) are clinically known to respond poorly to Levodopa.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (idiopathic) — NPRA license text was not returned for this query; confirmed instead via the evidence pack's own rank-4 candidate, which states Parkinson's disease is Levodopa's original core indication |
| Predicted New Indication | Parkinsonian Disorder |
| TxGNN Prediction Score | 0.00%* |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 15 |
| Recommended Decision | Proceed with Guardrails |

\* *Data quality note: the raw TxGNN score field returned 0.0 for all five candidate diseases in this evidence pack (ranks 1–5). This is very likely an export/serialization issue rather than a true model confidence of zero, since candidates are still meaningfully differentiated by rank (1–5) and by evidence volume. Rank order, not the raw score, should be used to interpret model confidence until this is resolved.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Levodopa was not returned by the DrugBank query in this evidence pack (flagged as data gap DG002). However, the evidence pack's own repurposing rationale for the original-indication candidate (rank 4, Parkinson disease) does provide the relevant mechanism: **Levodopa is a dopamine precursor that crosses the blood–brain barrier and is converted to dopamine by AADC, directly replenishing the nigrostriatal dopamine deficiency that underlies parkinsonism.** This is the best-established drug mechanism in movement-disorder neurology, supported by decades of Phase 3 RCTs and clinical use.

"Parkinsonian Disorder" (rank 1) is not a distinct new disease so much as a **broader diagnostic umbrella** that contains idiopathic Parkinson's disease plus related but mechanistically heterogeneous syndromes (e.g. multiple system atrophy, vascular parkinsonism, progressive supranuclear palsy). The rationale attached to this candidate explicitly notes: *"與『Parkinson disease』為同一機轉核心（多巴胺前驅物補充治療），但此標籤較廣泛，可能涵蓋部分對 Levodopa 反應不一的巴金森症候群… 核心特發性巴金森病證據充分，但廣義 parkinsonian disorder 需注意亞型異質性。"* In plain terms: the mechanistic logic is sound for the classic idiopathic-PD subset, but the broader label pools in atypical parkinsonism subtypes that are clinically recognized to have a poor or transient Levodopa response. This heterogeneity is the central caveat for this prediction, not a reason to reject it outright — hence the "Proceed with Guardrails" stance rather than a clean "Go."

For context, three other TxGNN-predicted candidates in this pack (juvenile-onset Parkinson disease 19A, early-onset parkinsonism-intellectual disability syndrome, atypical juvenile parkinsonism) scored far lower on evidence (L3–L5) and are not the focus of this report, since rank 1 is the designated primary candidate under the reporting rules.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001928](https://clinicaltrials.gov/study/NCT00001928) | N/A | Completed | 25 | "Intravenous Levodopa in Parkinsonism" — direct test of IV levodopa as dopamine replacement in Parkinsonian patients. |
| [NCT00562198](https://clinicaltrials.gov/study/NCT00562198) | Phase 2 | Terminated | 16 | Crossover study comparing Levodopa/Carbidopa vs. Stalevo on striatal ¹¹C-raclopride binding in PD patients with wearing-off symptoms — direct Levodopa pharmacodynamics. |
| [NCT03881371](https://clinicaltrials.gov/study/NCT03881371) | Phase 3 | Completed | 307 | Safinamide add-on vs. placebo in Chinese PD patients on stable-dose Levodopa with motor fluctuations. |
| [NCT02240030](https://clinicaltrials.gov/study/NCT02240030) | Phase 3 | Completed | 351 | CVT-301 (Levodopa Inhalation Powder) vs. placebo for OFF episodes in PD patients with motor fluctuations. |
| [NCT00466167](https://clinicaltrials.gov/study/NCT00466167) | Phase 3 | Completed | 517 | Pramipexole ER vs. placebo vs. IR in Levodopa-treated advanced PD patients with motor fluctuations. |
| [NCT00368108](https://clinicaltrials.gov/study/NCT00368108) | Phase 3 | Completed | 752 | E2007 vs. placebo in Levodopa-treated PD patients with motor fluctuations. |
| [NCT01283594](https://clinicaltrials.gov/study/NCT01283594) | Phase 2/3 | Completed | 420 | SYN115 as adjunctive therapy in Levodopa-treated PD subjects with end-of-dose wearing off. |
| [NCT00199407](https://clinicaltrials.gov/study/NCT00199407) | Phase 3 | Completed | 230 | Istradefylline (KW-6002) 20 mg/day for reducing OFF time in advanced PD patients treated with Levodopa. |
| [NCT06596876](https://clinicaltrials.gov/study/NCT06596876) | Phase 3 | Recruiting | 450 | HRG2010 vs. sustained-release carbidopa-levodopa in PD patients with motor fluctuations. |
| [NCT00143026](https://clinicaltrials.gov/study/NCT00143026) | Phase 4 | Completed | 184 | Carbidopa/Levodopa/Entacapone vs. quality of life (PDQ-8) in PD patients with minimal motor fluctuations. |

*Note: most of these trials evaluate an add-on/comparator drug against a stable Levodopa background rather than Levodopa itself as the primary intervention; NCT00001928 and NCT00562198 are the two trials that test Levodopa directly (Grade A relevance in the source evidence pack).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25449210](https://pubmed.ncbi.nlm.nih.gov/25449210/) | 2015 | Review | Movement Disorders | Comprehensive review of Levodopa pharmacokinetics and pharmacodynamics in PD treatment. |
| [41219370](https://pubmed.ncbi.nlm.nih.gov/41219370/) | 2025 | Cohort | Scientific Reports | Postmortem study (n=63) on Levodopa exposure and nigral neuroinflammation across PD, MSA, and PSP. |
| [30361296](https://pubmed.ncbi.nlm.nih.gov/30361296/) | 2019 | Cohort | J Neurol Neurosurg Psychiatry | REIN-PD trial: behavioural/trait changes in PD patients switched from dopamine agonist to Levodopa. |
| [11723148](https://pubmed.ncbi.nlm.nih.gov/11723148/) | 2001 | Cohort | J Gerontol A Biol Sci Med Sci | Effect of Levodopa therapy on orthostatic and postprandial hypotension in elderly Parkinsonian patients. |
| [31272925](https://pubmed.ncbi.nlm.nih.gov/31272925/) | 2019 | Review | Parkinsonism & Related Disorders | Juvenile parkinsonism differential diagnosis, genetics, and Levodopa-responsive subtypes. |
| [28229895](https://pubmed.ncbi.nlm.nih.gov/28229895/) | 2017 | Review | The Lancet Neurology | Update on impulse control disorders and Levodopa-induced dyskinesias in PD. |
| [6435991](https://pubmed.ncbi.nlm.nih.gov/6435991/) | 1984 | Review | Drugs | Historical overview establishing Levodopa as the most effective single drug in Parkinson's disease. |
| [812004](https://pubmed.ncbi.nlm.nih.gov/812004/) | 1975 | Cohort | Neurology | Classic study of on-off response with oral vs. IV Levodopa administration in Parkinsonian patients. |
| [12429201](https://pubmed.ncbi.nlm.nih.gov/12429201/) | 2002 | Preclinical | Experimental Neurology | Quetiapine attenuates Levodopa-induced motor complications in rodent/primate parkinsonian models. |
| [35986227](https://pubmed.ncbi.nlm.nih.gov/35986227/) | 2023 | Review | Cerebellum | Diagnostic criteria for multiple system atrophy — relevant to differentiating atypical parkinsonism within the broader "parkinsonian disorder" label. |

---

## Malaysia Market Information

NPRA records show Levodopa has **15 active marketing authorizations** in Malaysia (market status: Marketed). However, the license-level fields returned for this query — authorization number, product name, dosage form, and approved indication text — were all empty in the current data pull, so an item-level authorization table cannot be presented. This should be treated as an open data gap requiring a fresh NPRA query before regulatory sign-off.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields in this evidence pack — key warnings, contraindications, and drug–drug interactions — were returned as data gaps or empty; DG001 flags this as a Blocking gap for the S1 safety pre-screen.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong for the core idiopathic-PD subset of "parkinsonian disorder," and the evidence level is L1 (multiple completed Phase 3 RCTs in Levodopa-treated Parkinsonian populations), consistent with the source scoring. However, the predicted indication is a broader diagnostic umbrella that includes atypical parkinsonism subtypes (MSA, vascular parkinsonism, PSP) with clinically recognized poor Levodopa response, and the drug-level safety/MOA data needed for a full S1 safety screen is currently missing (DG001, blocking; DG002, high).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001 — blocking for S1 safety screen)
- Confirmed Levodopa mechanism-of-action record via DrugBank API (DG002)
- Complete NPRA license-level detail (authorization numbers, product names, approved indication text) for the 15 registered products
- Subtype-stratified evidence review to separate idiopathic-PD response data from atypical-parkinsonism response data before applying this prediction across the full "parkinsonian disorder" umbrella
- Clarification/re-pull of the TxGNN score field, which returned 0.0 for all five candidates in this dataset and should not currently be relied on as a confidence metric
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

