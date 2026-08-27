---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Unspecified Approved Indication to Schizophrenia

## One-Sentence Summary

Haloperidol is a marketed drug in Malaysia (3 NPRA registrations), but its officially recorded original indication text is currently a data gap in this evidence pack. The TxGNN model's top prediction is **Schizophrenia** (score 99.96%), supported by **50 clinical trials** and **20 publications** — however, the model's own rationale notes this is very likely confirmation of Haloperidol's *existing* standard-of-care antipsychotic use rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source registry data (data gap — see DG001/DG002); Haloperidol is clinically established as a first-generation antipsychotic |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `drug.original_moa` field. However, the evidence pack's own repurposing rationale supplies the relevant pharmacology: Haloperidol is a first-generation (typical) antipsychotic whose mechanism is central dopamine D2 receptor antagonism — a textbook-standard mechanism for treating schizophrenia.

Importantly, the evidence pack explicitly flags that this is **not a strict case of drug repurposing**: Schizophrenia is Haloperidol's long-established, real-world approved indication, and the blank `original_indications` field reflects a data-extraction gap rather than the absence of that indication. In other words, the TxGNN model has correctly re-identified Haloperidol's known primary use — which is a useful sanity check on model validity, but should not be presented to stakeholders as a novel repurposing opportunity.

For comparison, the pack's rank-8 candidate ("psychotic disorder," L1 evidence) shows the same pattern — D2 antagonism directly supports acute psychosis management and is standard clinical practice, not a new finding. By contrast, ranks 3–7, 9, and 10 (e.g., congenital disorders of glycosylation, retinal dystrophy, hydranencephaly, X-linked myopia, Charcot-Marie-Tooth disease) have **no clinical trials, no literature, and no plausible mechanistic link** — the evidence pack itself labels these as likely false-positive artifacts of the knowledge-graph embedding space (L5, Hold). Only rank 2 (schizophreniform disorder, L3, "Research Question") represents a genuinely exploratory signal worth monitoring.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01052389](https://clinicaltrials.gov/study/NCT01052389) | Phase 4 | Completed | 300 | GiSAS trial — aripiprazole, olanzapine, and haloperidol compared over 12 months in schizophrenia outpatients |
| [NCT00203775](https://clinicaltrials.gov/study/NCT00203775) | N/A | Terminated | N/A | Risperidone vs haloperidol for aggression/hostility in psychotic inmates |
| [NCT00485901](https://clinicaltrials.gov/study/NCT00485901) | Phase 3 | Completed | 50 | IM olanzapine vs IM haloperidol in acutely agitated schizophrenia patients |
| [NCT00455234](https://clinicaltrials.gov/study/NCT00455234) | Phase 3 | Completed | 300 | IM olanzapine vs IM haloperidol + promethazine for rapid tranquilization |
| [NCT00249119](https://clinicaltrials.gov/study/NCT00249119) | Phase 3 | Completed | 1579 | Risperidone vs fixed 10mg haloperidol in chronic schizophrenia |
| [NCT00191555](https://clinicaltrials.gov/study/NCT00191555) | Phase 4 | Completed | 360 | Long-term olanzapine vs haloperidol in stabilized schizophrenia patients |
| [NCT00866645](https://clinicaltrials.gov/study/NCT00866645) | Phase 2/3 | Completed | 240 | IM levosulpiride vs IM haloperidol for agitation in Chinese schizophrenia patients |
| [NCT00631722](https://clinicaltrials.gov/study/NCT00631722) | N/A | Completed | 80 | Quetiapine vs haloperidol for agitated symptoms in acute schizophrenia |
| [NCT01164059](https://clinicaltrials.gov/study/NCT01164059) | Phase 4 | Completed | 149 | Newer antipsychotics vs low-dose haloperidol/flupentixol in schizophrenia |
| [NCT00723606](https://clinicaltrials.gov/study/NCT00723606) | Phase 3 | Completed | 376 | IM ziprasidone vs IM haloperidol for agitation in schizophrenia (China registration study) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11777998](https://pubmed.ncbi.nlm.nih.gov/11777998/) | 2002 | RCT | The New England Journal of Medicine | Long-term comparison of risperidone vs haloperidol for relapse prevention in schizophrenia/schizoaffective disorder |
| [31006114](https://pubmed.ncbi.nlm.nih.gov/31006114/) | 2019 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of haloperidol discontinuation in stable schizophrenia patients |
| [18254045](https://pubmed.ncbi.nlm.nih.gov/18254045/) | 2008 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Haloperidol vs chlorpromazine — benchmark antipsychotic comparison |
| [11552769](https://pubmed.ncbi.nlm.nih.gov/11552769/) | 2001 | Pooled analysis | International Clinical Psychopharmacology | Combined analysis of 12 double-blind trials, risperidone vs haloperidol and other antipsychotics |
| [15342619](https://pubmed.ncbi.nlm.nih.gov/15342619/) | 2004 | RCT | Journal of Clinical Pharmacology | IM haloperidol/lorazepam effects on QT interval in schizophrenia |
| [27516021](https://pubmed.ncbi.nlm.nih.gov/27516021/) | 2016 | Cohort | Romanian Journal of Morphology and Embryology | Clinical/biological outcomes of prolonged haloperidol treatment |
| [33472389](https://pubmed.ncbi.nlm.nih.gov/33472389/) | 2021 | Comparative study | The American Journal of Psychiatry | Clozapine vs olanzapine vs haloperidol for violence in schizophrenia with conduct disorder |
| [10200746](https://pubmed.ncbi.nlm.nih.gov/10200746/) | 1999 | Study | The American Journal of Psychiatry | Sexual disturbances during clozapine vs haloperidol treatment |
| [35887056](https://pubmed.ncbi.nlm.nih.gov/35887056/) | 2022 | Preclinical | International Journal of Molecular Sciences | Haloperidol/olanzapine effects on hippocampal cell proliferation (animal model) |
| [37635268](https://pubmed.ncbi.nlm.nih.gov/37635268/) | 2023 | Preclinical | International Journal of Developmental Neuroscience | Haloperidol effects on neurotrophic factors/epigenetics in ketamine-induced schizophrenia model |

---

## Malaysia Market Information

NPRA records confirm 3 active registrations (market status: Marketed), but the individual license number, product name, dosage form, and approved indication text fields were not populated in this data pull — a data extraction gap, not an absence of registration. Re-querying the NPRA product database is needed to complete this table.

---

## Safety Considerations

Please refer to the package insert for safety information. **Note:** the TFDA/NPRA label warnings and contraindications (DG001) and drug interaction data are currently unavailable and are flagged as a *Blocking* data gap — this must be resolved before any safety-stage (S1) evaluation can be completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The rank-1 prediction (schizophrenia) is supported by extensive Phase 3/4 RCT and systematic-review evidence (L1), but this largely reconfirms Haloperidol's already-established use rather than identifying a novel repurposing opportunity — so its practical value here is as a model-validity check, not a new candidate to advance. A blocking data gap (missing TFDA/NPRA label warnings and contraindications) prevents completion of the safety initial screen for any indication, including this one.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/NPRA package insert (warnings, contraindications) — Blocking gap DG001
- Obtain DrugBank MOA data to formally document mechanism (currently drug-level gap DG002)
- Re-query NPRA for complete per-license product name, dosage form, and approved indication text
- Clarify with regulatory/clinical staff whether schizophrenia should be treated as a "confirmation" case rather than a repurposing candidate before further investment
- Ranks 3, 5, 6, 7, 9, 10 (L5, no trials/literature, no mechanistic plausibility) should be deprioritized as likely false positives; rank 2 (schizophreniform disorder, L3) may warrant lightweight monitoring only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

