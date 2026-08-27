---
layout: default
title: Chlordiazepoxide
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Chlordiazepoxide
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

# Chlordiazepoxide: From Anxiety to Insomnia

## One-Sentence Summary

Chlordiazepoxide is the original benzodiazepine, classically used to treat anxiety disorders and alcohol withdrawal.
The TxGNN model predicts it may also be effective for **Insomnia**,
with **1 low-relevance clinical trial** and **6 publications** (mostly reviews) currently associated with this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorders (established benzodiazepine indication; TFDA/NPRA approved-indication text is not available in the current dataset — see Data Gap DG001) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Research Question (Hold pending further evidence) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record (Data Gap DG002). Based on known pharmacological information, chlordiazepoxide is a benzodiazepine — the first one ever brought to market — and acts as a positive allosteric modulator of the GABA-A receptor, enhancing chloride channel response to GABA. Its efficacy in anxiety disorders has been well established for over 60 years, and this same sedative mechanism is mechanistically applicable to sleep induction and maintenance.

The predicted new indication (insomnia) and the drug's classic use (anxiety) rely on the same GABA-A-mediated sedative-anxiolytic pathway, so the pharmacological rationale is sound. However, the evidence pack itself notes an important caveat: sedation and anxiolysis overlap heavily in benzodiazepines, making it difficult to distinguish "anxiety treatment with secondary sleep improvement" from "primary insomnia treatment." Most available literature centers on chlordiazepoxide's anxiolytic and alcohol-withdrawal roles rather than dedicated insomnia trials, so the insomnia signal should currently be treated as a mechanistically plausible but clinically unconfirmed hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109030](https://clinicaltrials.gov/study/NCT01109030) | Phase 2/3 | Completed | 50 | Trial of Pioglitazone as an adjunct to Citalopram for moderate-to-severe depression. **Relevance flagged as low (Grade C)** — the evidence pack itself notes this appears to be a knowledge-graph mismatch with no substantive link to chlordiazepoxide or insomnia. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4628683](https://pubmed.ncbi.nlm.nih.gov/4628683/) | 1972 | RCT | Current Therapeutic Research | Clinical evaluation of chlordiazepoxide vs. molindone efficacy in anxious outpatients (abstract not available). |
| [30680986](https://pubmed.ncbi.nlm.nih.gov/30680986/) | 2019 | Cohort | Medicinski Glasnik | Cross-sectional study of potentially inappropriate medications (Beers criteria) among elderly patients in Iran; benzodiazepines including chlordiazepoxide are implicated. |
| [14085195](https://pubmed.ncbi.nlm.nih.gov/14085195/) | 1963 | Cohort | Acta Psychiatrica Scandinavica | Early treatment series of anxiety neuroses and psychosomatic syndromes using a Librium metabolite (abstract not available). |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Review of anxiolytic drug pharmacokinetics, noting anxiolytics as the most prescribed psychoactive drug class. |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of benzodiazepine pharmacodynamic changes in the elderly, relevant to hypnotic use in this population. |
| [6111745](https://pubmed.ncbi.nlm.nih.gov/6111745/) | 1981 | Review | The Medical Letter on Drugs and Therapeutics | General reference review on choice among benzodiazepines. |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not yet available in this evidence pack — see Data Gap DG001.)

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence level is L3 — supported only by review-level and cohort literature plus one clinical trial that the evidence pack itself flags as a likely database mismatch (Grade C relevance). No study directly tests chlordiazepoxide for insomnia as a primary endpoint; the signal rests on mechanistic extrapolation from its anxiolytic/sedative action rather than dedicated clinical evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently blocking (DG001)
- DrugBank mechanism-of-action data to formally support the mechanistic rationale (DG002)
- Malaysia market license details (product name, dosage form, approved indication text) — current record has 1 registration but no populated license fields
- Dedicated clinical trials or comparative studies evaluating chlordiazepoxide specifically for insomnia (as opposed to anxiety or alcohol withdrawal)
- Drug-drug interaction data, given chlordiazepoxide's CNS-depressant profile and relevance to a sleep-related indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

