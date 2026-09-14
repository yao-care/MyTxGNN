---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 597
evidence_level: L5
indication_count: 5
---

# Risperidone
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

Using the drug-repurposing evaluation report template supplied in the prompt (no additional skill needed — this is direct document generation from a fully-specified format).

A few observations from the Evidence Pack worth flagging before the report itself: `drug.original_indications` is empty and `original_moa` is a data gap, but risperidone's approved uses (schizophrenia, bipolar I disorder mania, irritability associated with autistic disorder) and its D2/5-HT2A antagonist mechanism are directly stated inside the evidence pack's own trial summaries and `repurposing_rationale.mechanistic_link` fields — I used those rather than inventing anything. Also, ranks 2–5 ("autism", "schizophrenia", "bipolar disorder", "manic bipolar affective disorder") are **not** new repurposing candidates — the pack's own rationale text says so explicitly (TxGNN score 0.0 = re-identified known label). The only actual novel candidate is rank 1, "autism susceptibility 1," a genetic-susceptibility ontology term, not a clinical diagnosis. The report below is built around that distinction.

---

# Risperidone: From Schizophrenia and Bipolar Disorder to Autism Susceptibility 1

## One-Sentence Summary

Risperidone is a well-established atypical antipsychotic (5-HT2A/D2 receptor antagonist) already approved for schizophrenia, bipolar I disorder manic episodes, and irritability associated with autistic disorder. The TxGNN model's top novel candidate is **Autism Susceptibility 1** — a genetic susceptibility locus rather than a clinical diagnosis — currently supported by only **1 clinical trial** (a pharmacogenomics study, not an efficacy trial) and **3 publications**. The model's other four ranked outputs (autism, schizophrenia, bipolar disorder, manic bipolar affective disorder) are risperidone's existing approved indications, not new predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, Bipolar I Disorder (manic/mixed episodes), Irritability associated with Autistic Disorder — established uses referenced throughout the evidence pack's own trial summaries; formal NPRA license indication text is not yet populated in this pack |
| Predicted New Indication | Autism susceptibility 1 (a genetic susceptibility locus, not a treatable clinical phenotype) |
| TxGNN Prediction Score | 0% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 25 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The evidence pack's `drug.original_moa` field is currently a data gap, but the mechanistic rationale embedded in the evidence itself is consistent: risperidone is a benzisoxazole derivative combining potent serotonin 5-HT2A and dopamine D2 receptor antagonism. This dual blockade underlies its established efficacy across positive/negative psychotic symptoms (schizophrenia), manic episodes (bipolar I disorder), and behavioral irritability/aggression in autism spectrum disorder — all documented in the trial summaries collected under ranks 2–5 of this pack.

"Autism susceptibility 1," however, is a different kind of entity: it is a genetic/GWAS susceptibility locus in the underlying knowledge graph, not a diagnosable condition a drug can be prescribed against. It is distinct from — though graph-adjacent to — the already-approved "irritability associated with autistic disorder" indication. The single supporting trial (NCT00584701) is itself a pharmacogenomics study examining genetic modifiers of treatment response, not a trial designed to test risperidone's efficacy against this susceptibility marker. The three supporting publications are similarly pharmacogenomic association/cohort studies (CYP2D6/UGT1A1/NRXN3 polymorphisms and side-effect outcomes such as prolactin elevation and weight gain), not efficacy evidence for the susceptibility entity itself.

Mechanistically, D2/5-HT2A blockade plausibly explains risperidone's benefit for the *behavioral* symptoms of autism spectrum disorder (already an approved use) — but a receptor antagonist does not "treat" a genetic susceptibility locus. This candidate should be read as the model surfacing a graph-adjacency artifact (pharmacogenomic literature clustering near an autism-susceptibility node) rather than a genuine efficacy hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00584701](https://clinicaltrials.gov/study/NCT00584701) | Phase 2/3 | Completed | 49 | Pharmacogenomics in Autism Treatment — examined genetic susceptibility/environmental interaction in autism; risperidone used as the studied agent for behavioral difficulties, but study endpoint was pharmacogenomic, not efficacy against a susceptibility marker (relevance grade C: study design targets pharmacogenomics, not this entity as a treatment endpoint) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955115](https://pubmed.ncbi.nlm.nih.gov/29955115/) | 2018 | Pharmacogenomic Cohort | The Pharmacogenomics Journal | UGT1A1 polymorphisms associated with prolactin response in risperidone-treated children/adolescents with ASD (n=84) |
| [23799528](https://pubmed.ncbi.nlm.nih.gov/23799528/) | 2013 | Pharmacogenomic Association | Translational Psychiatry | Energy-balance gene variants (FTO, MC4R, LEP, CNR1, FAAH) moderate antipsychotic-induced weight gain in RUPP Autism Network risperidone trials (n=225) |
| [23306218](https://pubmed.ncbi.nlm.nih.gov/23306218/) | 2013 | Pharmacogenomic Association | Progress in Neuro-Psychopharmacology & Biological Psychiatry | NRXN3 polymorphisms associated with schizophrenia and risperidone-induced weight gain in Chinese Han population |

---

## Malaysia Market Information

Detailed authorization records (license number, product name, dosage form, approved-indication text) are not yet populated in this evidence pack for any of the 25 registrations. NPRA confirms risperidone's market status as **已上市 (Marketed)** with **25 active registrations**; license-level detail needs to be pulled from source before this table can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all unpopulated in this evidence pack (flagged as Blocking data gap DG001 — TFDA/NPRA label warnings/contraindications). Separately, the clinical-trial evidence collected across ranks 2–5 of this pack repeatedly documents prolactin elevation, weight gain/metabolic effects, and extrapyramidal symptoms as recurring signals for risperidone — these should inform the eventual safety review once formal label data is obtained, but are not a substitute for it.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only genuinely novel candidate in this pack — Autism Susceptibility 1 — is a genetic-susceptibility ontology entity, not a clinical diagnosis, and is supported solely by pharmacogenomic side-effect studies (Evidence Level L3, Decision Stage S1, "Research Question"), not efficacy evidence. This does not meet the bar to advance past S1. Separately, ranks 2–5 (autism/irritability, schizophrenia, bipolar disorder, manic bipolar affective disorder) are not repurposing opportunities at all — they are risperidone's existing, long-approved indications, correctly reflected by a TxGNN score of 0.0 (known label, not a new prediction).

**To proceed, the following is needed:**
- TFDA/NPRA package-insert warnings and contraindications (DG001, Blocking — currently prevents any S1 safety screen)
- Confirmed DrugBank MOA record (DG002)
- License-level product/indication text for the 25 Malaysia registrations
- A pipeline-level check on why already-approved indications are being surfaced as "predicted new indications" — likely an artifact of candidate-ontology granularity (e.g., "bipolar disorder" vs. "manic bipolar affective disorder" as separate nodes) that should be deduplicated against `original_indications` before scoring
- If Autism Susceptibility 1 is to be pursued further, non-pharmacogenomic efficacy evidence specific to genetically-defined ASD subpopulations would be needed — none currently exists in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

