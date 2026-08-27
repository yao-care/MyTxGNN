---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Major Depressive Disorder to Endogenous Depression

## One-Sentence Summary

> Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally approved for major depressive disorder (MDD) and generalized anxiety disorder.
> The TxGNN model's top-ranked prediction is **Endogenous Depression** (an older diagnostic term for the melancholic/biological subtype of MDD), with a **99.94% prediction score**,
> though only **2 low-quality clinical trials** (both terminated/withdrawn) and **20 publications** are directly tagged to this specific disease label — most of the underlying evidence actually comes from duloxetine's already-established MDD efficacy data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (stated in the evidence pack's repurposing rationale; NPRA license text fields were not populated in this evidence pack) |
| Predicted New Indication | Endogenous Depression |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (based on aggregate MDD evidence base; trial evidence specific to this legacy label is weak — see below) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data (e.g., DrugBank MOA text) is flagged as a data gap in this evidence pack. However, the repurposing rationale notes included alongside the predictions state that duloxetine is a **serotonin-norepinephrine reuptake inhibitor (SNRI)**, inhibiting reuptake of both serotonin (5-HT) and norepinephrine (NE) — the mechanism underlying its established efficacy in MDD and generalized anxiety disorder.

"Endogenous depression" is an older classification term describing depression with prominent biological/melancholic features, generally considered a subtype within the MDD spectrum rather than a distinct disease entity. Because of this overlap, the very high TxGNN score (99.94%) most likely reflects the model recognizing an already-proven drug-disease relationship (duloxetine ↔ MDD) rather than uncovering a genuinely novel therapeutic hypothesis. This is corroborated by the evidence pack's own rationale for the "major depressive disorder" and "unipolar depression" predictions, which explicitly note these are "not a repurposing hypothesis but known efficacy."

The practical implication: pharmacologically, applying duloxetine to patients diagnosed under the "endogenous depression" label is well supported by the broader MDD evidence base, but the clinical trials and literature specifically indexed under this exact disease term are sparse and low quality (see below), so this should be treated as a labeling/terminology nuance rather than a new indication requiring separate clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03634527](https://clinicaltrials.gov/study/NCT03634527) | N/A | Terminated | 15 | Study of auricular point acupressure for chemotherapy-induced peripheral neuropathy (CIPN); duloxetine mentioned only as the reference drug (0.72-point pain improvement vs. placebo in a cited RCT), not as the study intervention. Low relevance (Grade C) — terminated, n=15. |
| [NCT03068247](https://clinicaltrials.gov/study/NCT03068247) | Phase 3 | Withdrawn | 0 | Intended to study neurobiological mechanisms of treatment response in MDD; withdrawn before enrollment, no usable data (Grade C). |

Both trials indexed against the "endogenous depression" label are low relevance — neither provides direct efficacy evidence for duloxetine in this indication. Stronger supporting evidence exists under the related "major depressive disorder" prediction (see query_log), including large completed Phase 3/4 RCTs.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20831742](https://pubmed.ncbi.nlm.nih.gov/20831742/) | 2011 | Review (Tier 1) | Acta Psychiatrica Scandinavica | Systematic review of duloxetine and venlafaxine short-term antidepressant efficacy/tolerability in major depression, including unpublished data. |
| [15811202](https://pubmed.ncbi.nlm.nih.gov/15811202/) | 2005 | RCT (Tier 1) | Current Medical Research and Opinion | Efficacy, safety and tolerability of duloxetine 60 mg once daily in major depression. |
| [38838790](https://pubmed.ncbi.nlm.nih.gov/38838790/) | 2024 | RCT (Tier 2) | Journal of Affective Disorders | Cognitive improvement in late-life depression treated with vortioxetine and duloxetine; age at first onset affects outcomes. |
| [27400882](https://pubmed.ncbi.nlm.nih.gov/27400882/) | 2016 | Cohort (Tier 2) | Human Psychopharmacology | Open-label naturalistic study of duloxetine effectiveness and plasma level prediction in elderly MDD patients. |
| [17612852](https://pubmed.ncbi.nlm.nih.gov/17612852/) | 2007 | N/A | Annals of Clinical Psychiatry | Review of duloxetine pharmacology and therapeutic use in depression and other psychiatric disorders. |
| [15583519](https://pubmed.ncbi.nlm.nih.gov/15583519/) | 2004 | N/A | Journal of Psychiatric Practice | General review of duloxetine. |
| [17503986](https://pubmed.ncbi.nlm.nih.gov/17503986/) | 2007 | N/A | The Journal of Clinical Psychiatry | Open-label trial of duloxetine in dysthymia and "double depression." |
| [20931154](https://pubmed.ncbi.nlm.nih.gov/20931154/) | 2010 | N/A | La Clinica Terapeutica | Duloxetine vs. venlafaxine in the acute treatment of unipolar and bipolar depression. |
| [16148429](https://pubmed.ncbi.nlm.nih.gov/16148429/) | 2005 | N/A | American Journal of Therapeutics | Role of venlafaxine/duloxetine in depression treatment with somatic pain symptoms; pharmacokinetics discussion. |
| [14682027](https://pubmed.ncbi.nlm.nih.gov/14682027/) | 2003 | N/A | Journal of Psychosocial Nursing and Mental Health Services | Physical symptoms comorbid with depression and role of duloxetine. |

(10 of 20 available publications shown, prioritized by RCT/Review classification tier; remaining entries were classified as "pending" in the evidence pack and are general duloxetine/depression literature.)

---

## Malaysia Market Information

The evidence pack records **18 total registrations** with market status **✓ Marketed**, but the individual license records (registration number, product name, dosage form, manufacturer, approved indication text) were returned as empty fields for all 5 sampled entries — no usable per-license detail is currently available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Duloxetine's SNRI mechanism and broad MDD evidence base make its use in "endogenous depression" (a melancholic/biological MDD subtype) pharmacologically reasonable and low novel-risk, since this is largely an established use under a legacy diagnostic label rather than a genuinely new indication. However, trial/literature evidence specifically tagged to this exact disease term is weak, and key safety/regulatory data are missing, so guardrails (clinical oversight, safety monitoring) are warranted rather than an unconditional Go.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (flagged as Blocking data gap, DG001)
- DrugBank-sourced mechanism of action detail (flagged as High-severity data gap, DG002)
- Confirmation of how "endogenous depression" maps to current diagnostic criteria (e.g., DSM-5 MDD with melancholic features) to clarify whether this is a labeling nuance or a distinct clinical population
- Populated Malaysia license/registration details (product names, dosage forms, approved indication text) to verify current marketed formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

