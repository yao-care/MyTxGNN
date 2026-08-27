---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 517
evidence_level: L5
indication_count: 5
---

# Olanzapine
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

# Olanzapine: From Schizophrenia/Bipolar Disorder to Major Depressive Disorder

## One-Sentence Summary

Olanzapine is a second-generation (atypical) antipsychotic originally approved for schizophrenia and bipolar I disorder. The TxGNN pipeline ranks **Major Depressive Disorder** as its top repurposing candidate, but this overlaps substantially with an already-established use (olanzapine/fluoxetine combination for treatment-resistant depression), supported by **~50 clinical trials** and **17 publications** in the evidence pack. Note: the evidence pack itself flags a data-quality problem — two lower-ranked "predictions" (schizophrenia, bipolar disorder) are in fact olanzapine's own original approved indications, not genuine new candidates, so this ranking should be treated cautiously pending upstream data correction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (TFDA license `approved_indication_text` fields are empty for all 5 sampled licenses, and `original_indications` is an empty array — see Data Gap DG001/DG002). Based on the evidence pack's own analyst notes, olanzapine's original approved indications are schizophrenia and bipolar I disorder. |
| Predicted New Indication | Major Depressive Disorder |
| TxGNN Prediction Score | 0% (reported as 0.0 — this appears anomalous for a rank-1 candidate; treat as a data-quality flag, not a true near-zero score) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs: NCT00035321, NCT00958568, among others) |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 34 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, olanzapine is a multi-receptor-targeted antipsychotic (MARTA) with antagonism at dopamine D2, serotonin 5-HT2A/5-HT2C, and other monoamine receptors — receptor activity that overlaps mechanistically with several antidepressant and antipsychotic-augmentation strategies used in mood disorders.

Olanzapine's approved indications (schizophrenia, bipolar I disorder — including bipolar depression via the olanzapine/fluoxetine combination, OFC/Symbyax) already sit within the same mood/psychotic-spectrum disease space as major depressive disorder. This is why the literature evidence below is dominated by augmentation and combination-therapy studies rather than novel monotherapy trials.

Importantly, this candidate is **not a mechanistically novel hypothesis** — OFC is already an approved, guideline-referenced treatment for treatment-resistant depression, and olanzapine augmentation of antidepressants is a well-documented, commonly used off-label strategy. The "prediction" here largely reflects consolidation of existing clinical practice rather than a new signal, which should temper enthusiasm despite the L1 evidence level.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00958568](https://clinicaltrials.gov/study/NCT00958568) | Phase 3 | Completed | 892 | Long-term OFC vs. fluoxetine alone for relapse prevention in treatment-resistant depression |
| [NCT00035321](https://clinicaltrials.gov/study/NCT00035321) | Phase 3 | Completed | 600 | Olanzapine + fluoxetine combination for treatment-resistant depression without psychotic features |
| [NCT00510146](https://clinicaltrials.gov/study/NCT00510146) | Phase 3 | Completed | 514 | Olanzapine vs. placebo in bipolar I disorder, depressed |
| [NCT00056472](https://clinicaltrials.gov/study/NCT00056472) | Phase 3 | Completed | 259 | SSRI + antipsychotic combination for psychotic depression |
| [NCT00402324](https://clinicaltrials.gov/study/NCT00402324) | Phase 4 | Completed | 202 | Divalproex + olanzapine for mixed-episode bipolar I disorder |
| [NCT00618748](https://clinicaltrials.gov/study/NCT00618748) | Phase 3 | Completed | 101 | Long-term olanzapine in bipolar I disorder, depressed |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Olanzapine vs. risperidone as SSRI add-on in treatment-resistant depression |
| [NCT05814640](https://clinicaltrials.gov/study/NCT05814640) | Phase 1/2 | Recruiting | 520 | STAR-AD: pragmatic trial of antidepressant strategies in depressed children/adolescents |
| [NCT00520507](https://clinicaltrials.gov/study/NCT00520507) | Phase 4 | Completed | 27 | Sleep architecture and cognitive changes in olanzapine-treated depressed patients |
| [NCT00273624](https://clinicaltrials.gov/study/NCT00273624) | Phase 3 | Withdrawn | 0 | Olanzapine augmentation vs. placebo in major depression (trial did not proceed) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38360024](https://pubmed.ncbi.nlm.nih.gov/38360024/) | 2024 | Network meta-analysis | The Lancet Psychiatry | Comparative efficacy/safety of pharmacological treatments for psychotic depression |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatric Clinics of North America | Antidepressants and atypical antipsychotics for treatment-resistant depression |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic review/meta-analysis | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (incl. olanzapine) in MDD |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Network meta-analysis | Medicine | Comparative efficacy/safety of 4 atypical antipsychotics as MDD augmentation |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | American Journal of Psychiatry | How antipsychotics fit into the treatment-resistant depression landscape |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic review/meta-analysis | Journal of Psychopharmacology | Augmentation/combination treatments for early-stage treatment-resistant depression |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Network meta-analysis | Journal of Affective Disorders | Augmentation strategies for treatment-resistant major depression |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Review | Journal of Psychopharmacology | Antidepressants + SGAs vs. esketamine vs. lithium for major depression |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Antipsychotics (incl. olanzapine) as antidepressants |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane systematic review | Cochrane Database of Systematic Reviews | Second-generation antipsychotics for major depressive disorder and dysthymia |

## Malaysia Market Information

Olanzapine is marketed in Malaysia with **34 total registrations**, but this evidence pack does not contain per-license detail — all 5 sampled license records have empty `license_number`, `product_name_zh`, `dosage_form`, `manufacturer`, and `approved_indication_text` fields. A detailed authorization table cannot be produced until this NPRA license data is populated.

## Safety Considerations

Please refer to the package insert for safety information. (This evidence pack's `key_warnings`, `contraindications`, and DDI fields are all data gaps — notably DG001, marked **Blocking**, meaning no safety pre-screening can currently be performed for this candidate.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (DG001 — TFDA warnings/contraindications) prevents any safety pre-screening (S0 stage) of this candidate. Additionally, the prediction pipeline itself flags a data-integrity issue in this batch: two other ranked "predictions" (schizophrenia, bipolar disorder) are actually olanzapine's own original approved indications rather than novel candidates, and the rank-1 MDD prediction score (0.0) is anomalous — both cast doubt on whether this ranking reflects a genuine repurposing signal versus consolidation of already-known clinical use (OFC for treatment-resistant depression).

**To proceed, the following is needed:**
- TFDA/NPRA package insert — warnings, contraindications (DG001, Blocking)
- Confirmed mechanism of action from DrugBank (DG002)
- Correction of the upstream `original_indications` field so genuinely novel candidates can be distinguished from already-approved uses
- Re-validation of the TxGNN scoring pipeline to resolve the anomalous 0.0 prediction score
- Populated NPRA license-level data (product name, dosage form, approved indication text) for the 34 registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

