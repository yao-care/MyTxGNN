---
layout: default
title: Fluvoxamine
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
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

# Fluvoxamine: From Obsessive-Compulsive Disorder to Broader Anxiety-Spectrum Disorders

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) whose original indication text is missing from the source records, though the evidence pack's own literature repeatedly documents it as an already-approved treatment for **obsessive-compulsive disorder (OCD)**. TxGNN's top-ranked prediction is, in fact, OCD itself — the model's own rationale flags this as likely a duplicate of an existing approved use rather than a genuine new indication. The more credible repurposing signals in this pack are **anxiety disorder** and **agoraphobia** (ranks 6–7), each supported by multiple placebo-controlled RCTs (L2 evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured data (TFDA/NPRA license indication text and DrugBank `original_indications` are both empty). Literature within this pack consistently documents fluvoxamine as an already-marketed SSRI for OCD. |
| Predicted New Indication | Obsessive-Compulsive Disorder *(⚠ see caveat below — likely not a genuinely new indication)* |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

**⚠ Data-quality caveat:** The rank-1 prediction (OCD) has an *empty* `clinical_trials` evidence array despite an L1 evidence label, and the model's own rationale states this "is one of fluvoxamine's already-approved indications, not strictly a new use; the empty `original_indications` field is likely a data gap." Ranks 6 (**anxiety disorder**, L2, S2/S3, Proceed with Guardrails) and 7 (**agoraphobia**, L2, S2, Proceed with Guardrails) are supported by multiple double-blind placebo-controlled RCTs and represent more credible repurposing candidates than rank 1.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (DrugBank MOA field: data gap). Based on well-established pharmacology reflected throughout the literature in this evidence pack, fluvoxamine is a selective serotonin reuptake inhibitor (SSRI). Serotonergic dysregulation is a core pathophysiological hypothesis for OCD, and SSRIs including fluvoxamine are established first-line pharmacotherapy for OCD — this is documented directly in the pack (e.g., PMID 9184625: "the mainstay of pharmacologic treatment of OCD is a 10- to 12-week trial of a potent SRI... one of the most thoroughly studied of these SRIs is fluvoxamine").

Because the `original_indications` field is empty and TFDA/NPRA license indication text was not captured, the pipeline appears to have ranked OCD as the top "predicted new indication," when in fact the evidence base shows OCD is fluvoxamine's long-standing approved use (multiple post-marketing and Phase 3/4 trials, e.g. NCT01933919, NCT02022709). This is a data-completeness issue upstream (DG001/DG002), not a repurposing signal, and should be corrected before this candidate is used to justify a "new indication" claim.

The genuinely more informative signal in this pack is the shared serotonergic mechanism extending fluvoxamine's efficacy from OCD to other anxiety-spectrum disorders — social anxiety disorder, panic disorder, generalized anxiety disorder, and agoraphobia — all supported by direct, fluvoxamine-specific double-blind RCTs (e.g., PMID 8927663, PMID 7726307, PMID 9754844, PMID 16573847). This is mechanistically coherent (same serotonergic pathway, overlapping DSM anxiety-spectrum classification) and is where the stronger repurposing case exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (predicted_indications[0].evidence.clinical_trials is empty for obsessive-compulsive disorder; note that multiple fluvoxamine/OCD trials such as [NCT01933919](https://clinicaltrials.gov/study/NCT01933919) and [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) do appear under the "anxiety disorder" prediction entry in this evidence pack, suggesting a possible disease-tagging inconsistency upstream).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | RCT/Meta-analysis | Journal of Psychiatric Research | Network meta-analysis of pharmacological vs. psychological treatment (alone and combined) for pediatric/adolescent OCD, including SRIs such as fluvoxamine. |
| [19198698](https://pubmed.ncbi.nlm.nih.gov/19198698/) | 2008 | RCT | Drugs of Today | Three 12-week double-blind, multicenter, placebo-controlled trials of controlled-release fluvoxamine in OCD and social phobia demonstrating efficacy. |
| [9184625](https://pubmed.ncbi.nlm.nih.gov/9184625/) | 1997 | Review | The Journal of Clinical Psychiatry | Comprehensive review establishing fluvoxamine's anti-obsessional efficacy from double-blind, placebo-controlled trials; one of the most thoroughly studied SRIs for OCD. |
| [40143130](https://pubmed.ncbi.nlm.nih.gov/40143130/) | 2025 | Review (overview of systematic reviews) | Pharmaceuticals (Basel) | Synthesizes systematic reviews/meta-analyses on fluvoxamine efficacy across GAD, social anxiety disorder, panic disorder, and OCD. |
| [27318812](https://pubmed.ncbi.nlm.nih.gov/27318812/) | 2016 | Systematic Review/Network Meta-analysis | The Lancet Psychiatry | Compares direct and indirect efficacy of all major pharmacological and psychotherapeutic OCD interventions in a single analysis. |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Review | Comprehensive Psychiatry | Long-term safety and tolerability of off-label high-dose SRIs (including fluvoxamine) in OCD treatment. |
| [31040685](https://pubmed.ncbi.nlm.nih.gov/31040685/) | 2019 | Association rule mining study | Neuropsychiatric Disease and Treatment | Predicts fluvoxamine treatment response in an Iranian OCD cohort using association rule mining; notes 40–60% of patients do not respond adequately to SRIs. |
| [34880926](https://pubmed.ncbi.nlm.nih.gov/34880926/) | 2021 | Statistical/cohort analysis | Clinical Practice and Epidemiology in Mental Health | Bayesian ordinal quantile regression modeling of fluvoxamine response in OCD patients. |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Clinical evidence review | BMJ Clinical Evidence | General epidemiology and treatment-options summary for OCD (prevalence ~1–2.7% depending on age group). |
| [1806635](https://pubmed.ncbi.nlm.nih.gov/1806635/) | 1991 | Review | International Clinical Psychopharmacology | Early narrative review of OCD as a neuropsychiatric syndrome and its historical treatment approaches. |

---

## Malaysia Market Information

NPRA records show **6 registered product licenses** for fluvoxamine (market status: ✓ Marketed), but the license number, product name, dosage form, manufacturer, and approved-indication text fields were not populated in this evidence pack (data gap) — full label detail should be pulled directly from NPRA/product package inserts before this data is used for regulatory or clinical decisions.

---

## Safety Considerations

Please refer to the package insert for safety information. All structured safety fields in this evidence pack (key warnings, contraindications, drug-drug interactions) are marked as data gaps — notably, **DG001 (TFDA/NPRA package insert warnings/contraindications) is flagged as Blocking**, meaning this candidate cannot yet complete an initial S1 safety assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The underlying serotonergic mechanism is well supported for fluvoxamine across the OCD/anxiety-disorder spectrum, and multiple direct RCTs support use in anxiety disorder and agoraphobia (L2 evidence, ranks 6–7).
- However, the rank-1 "predicted new indication" (OCD) appears to duplicate an already-approved use due to an upstream data gap (empty `original_indications` field), and a Blocking safety data gap (DG001) prevents a complete initial safety review — guardrails, not a full Go, are appropriate at this stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert PDF (warnings, contraindications, DDI) to resolve DG001 (Blocking)
- DrugBank mechanism-of-action data to resolve DG002 and strengthen the mechanistic-link analysis
- Reconciliation of the empty `original_indications` field so OCD is correctly classified as an existing approved use rather than a "new" prediction
- Completed license detail (product name, dosage form, indication text) for the 6 Malaysia registrations
- If pursuing repurposing specifically, prioritize confirmatory review of the anxiety disorder / agoraphobia candidates (ranks 6–7), which carry the stronger direct-evidence case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

