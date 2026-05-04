---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From Hyperprolactinemia to Schizophrenia (Negative Symptoms)

## One-Sentence Summary

Bromocriptine is a dopamine D2/D3 receptor agonist, originally used for hyperprolactinemia, Parkinson's disease, and type 2 diabetes management.
The TxGNN model predicts it may be effective for **Schizophrenia** (specifically negative symptoms),
with **3 clinical trials** and **20 publications** currently supporting this direction, making it the most evidence-rich prediction among 10 candidates.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinemia, Parkinson's disease, acromegaly, type 2 diabetes (regulatory details pending) |
| Predicted New Indication | Schizophrenia (Rank 9 of 10; featured due to strongest evidence base) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 (observational studies & clinical investigations) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

> **Note on Prediction Ranking**: TxGNN ranked schizophrenia 9th out of 10 predictions. The top 8 predictions (ranks 1–8) are ultra-rare genetic/developmental disorders with **L5 evidence** (model prediction only, no clinical studies) and **no identifiable mechanistic link**. Schizophrenia is featured here because it is the only prediction with clinical trial and literature evidence. A summary of all 10 predictions is provided below.

### All TxGNN Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------|-------------|----------------|--------|-------------|----------------|
| 1 | Congenital disorder of glycosylation with defective fucosylation | 99.83% | L5 | 0 | 0 | Hold |
| 2 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.83% | L5 | 0 | 0 | Hold |
| 3 | Retinal dystrophy with or without extraocular anomalies | 99.82% | L5 | 0 | 15 | Hold |
| 4 | Atypical glycine encephalopathy | 99.82% | L5 | 0 | 0 | Hold |
| 5 | Myopia 26, X-linked, female-limited | 99.81% | L5 | 0 | 0 | Hold |
| 6 | Hydranencephaly | 99.80% | L5 | 0 | 1 | Hold |
| 7 | Myopia X-linked | 99.78% | L5 | 0 | 0 | Hold |
| 8 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.78% | L5 | 0 | 0 | Hold |
| **9** | **Schizophrenia** | **99.73%** | **L3** | **3** | **20** | **Research Question** |
| 10 | Syndromic myopia | 99.73% | L5 | 0 | 0 | Hold |

> **Interpretation**: Ranks 1–8 likely reflect TxGNN knowledge graph topology bias — rare disease nodes with low degree centrality can receive inflated scores without genuine biological rationale. Rank 9 (schizophrenia) and rank 3 (retinal dystrophy) are the only predictions with literature support.

---

## Why is This Prediction Reasonable?

Bromocriptine is an ergot-derived dopamine D2/D3 receptor agonist and partial serotonin 5-HT2C agonist. Its primary therapeutic mechanism involves stimulation of dopamine D2 receptors in the tuberoinfundibular pathway (suppressing prolactin secretion), the nigrostriatal pathway (improving motor symptoms in Parkinson's disease), and peripheral metabolic regulation (improving insulin sensitivity in type 2 diabetes).

The relationship between bromocriptine and schizophrenia is pharmacologically complex and somewhat paradoxical. The dopamine hypothesis of schizophrenia posits that **mesolimbic D2 overactivity** drives positive symptoms (hallucinations, delusions) — which is why all approved antipsychotics are D2 **antagonists**. However, **mesocortical dopamine hypoactivity** is believed to underlie negative symptoms (apathy, social withdrawal, cognitive deficits), which remain poorly addressed by current treatments. A low-dose D2 agonist could, in theory, preferentially stimulate presynaptic autoreceptors — paradoxically reducing dopamine release in the mesolimbic pathway while augmenting mesocortical transmission. Multiple clinical studies from the 1980s–1990s explored this "low-dose agonist" strategy with bromocriptine adjunctive to neuroleptics, with some evidence of improvement in negative symptoms (BPRS total scores improved ~29% in one study). More recent clinical interest focuses on bromocriptine's role in managing antipsychotic-induced metabolic and endocrine side effects (hyperprolactinemia, prediabetes, weight gain), which are prevalent in schizophrenia patients.

That said, **the safety concern is significant**: bromocriptine can exacerbate or even induce psychotic symptoms. One published case report describes bromocriptine-induced schizophrenia in a previously non-psychotic patient. This dual-edged pharmacology — potentially helping negative symptoms while risking positive symptom exacerbation — makes this a legitimate research question rather than a straightforward repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03575000](https://clinicaltrials.gov/study/NCT03575000) | Phase 4 | Not yet recruiting | 15 | Open-label pilot evaluating bromocriptine as adjunct to antipsychotics for managing APD-associated prediabetes/insulin resistance in schizophrenia patients. Focuses on metabolic side effect management rather than psychiatric symptom treatment. |
| [NCT00315081](https://clinicaltrials.gov/study/NCT00315081) | Phase 3 | Unknown | 20 | Bromocriptine for symptomatic risperidone-induced hyperprolactinemia in schizophrenic patients. Addresses a known indication (hyperprolactinemia) in a specific population. Endocrinological outcomes assessed. |
| [NCT04181385](https://clinicaltrials.gov/study/NCT04181385) | Phase 2/3 | Unknown | 15 | Assessment of lipid response to acute olanzapine in healthy adults. Bromocriptine investigated as potential metabolic protective agent. Indirectly relevant — healthy volunteers, not schizophrenia patients. |

> **Trial Evidence Summary**: All three trials address bromocriptine's role in managing **metabolic/endocrine side effects** of antipsychotic medications, not direct treatment of schizophrenia symptoms. No trial evaluates bromocriptine as a primary or adjunctive treatment for positive or negative symptoms of schizophrenia. Sample sizes are small (15–20 participants), and two trials have unknown completion status.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6574535](https://pubmed.ncbi.nlm.nih.gov/6574535/) | 1983 | Open-label trial | Psychiatry Research | Bromocriptine (1.25–40 mg) in 10 chronic schizophrenic patients; assessed symptomatology, sleep patterns, and prolactin response. One of the earliest clinical investigations. |
| [2643996](https://pubmed.ncbi.nlm.nih.gov/2643996/) | 1989 | RCT (vs placebo) | Biological Psychiatry | Low-dose bromocriptine (2.5 mg/day) added to haloperidol: 29% BPRS improvement at 24h (vs 14% placebo, p<0.10). Acute improvement correlated negatively with plasma levels. |
| [1679383](https://pubmed.ncbi.nlm.nih.gov/1679383/) | 1991 | Clinical study | Comprehensive Psychiatry | Bromocriptine for "negative" schizophrenia — explores dopamine agonist strategy based on mesocortical hypoactivity hypothesis. Open clinical trials of D2 agonist + neuroleptic combination. |
| [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/) | 1993 | Case report | J Natl Med Assoc | **Bromocriptine-induced schizophrenia**: 53-year-old male developed schizophrenia 4 days after starting low-dose bromocriptine for macroprolactinoma. Resolved 5 days after discontinuation. Supports dopamine hypothesis. |
| [8561400](https://pubmed.ncbi.nlm.nih.gov/8561400/) | 1995 | Clinical study | Ann Médico-Psychol | Neuroleptic–bromocriptine combination in 12 schizophrenic patients: 29% mean improvement in PANSS total score after 1 month. Suggests adjunctive utility. |
| [18480682](https://pubmed.ncbi.nlm.nih.gov/18480682/) | 2008 | RCT (crossover) | J Clin Psychopharmacol | Randomized crossover comparing herbal medicine vs bromocriptine for risperidone-induced hyperprolactinemia. Bromocriptine used as active comparator for prolactin-lowering. |
| [21157697](https://pubmed.ncbi.nlm.nih.gov/21157697/) | 2011 | Clinical observation | Pharmacopsychiatry | Disorganized schizophrenia did NOT deteriorate with dopamine agonists (cabergoline and bromocriptine) used for ablactation. Reassuring safety signal in stable patients. |
| [26573387](https://pubmed.ncbi.nlm.nih.gov/26573387/) | 2016 | Case report | Nordic J Psychiatry | Bromocriptine mitigated paliperidone-induced metabolic/neurohormonal side effects AND improved negative symptoms in early-onset schizophrenia. Notable dual benefit. |
| [31688399](https://pubmed.ncbi.nlm.nih.gov/31688399/) | 2019 | Systematic review & meta-analysis | J Clin Psychopharmacol | Prodopaminergic drugs for negative symptoms of schizophrenia — systematic review of RCTs. Addresses the broader therapeutic strategy that bromocriptine represents. |
| [33571431](https://pubmed.ncbi.nlm.nih.gov/33571431/) | 2021 | Basic science | Cell | Cryo-EM structural insights into D1R and D2R signaling complexes. D2R identified as principal therapeutic target for schizophrenia; provides structural basis for understanding bromocriptine–D2R interaction. |

> **Literature Summary**: The evidence spans nearly 4 decades (1983–2024) and includes 2 small RCTs, multiple open-label trials, case reports, and systematic reviews. Key themes: (1) low-dose bromocriptine adjunctive to neuroleptics may improve negative symptoms (~29% BPRS improvement); (2) bromocriptine can induce or exacerbate psychosis; (3) most recent clinical interest focuses on managing antipsychotic metabolic/endocrine side effects. No large-scale definitive RCT exists for bromocriptine as a direct schizophrenia treatment.

---

## Notable Secondary Finding: Retinal Dystrophy (Rank 3)

While most top-ranked predictions lack evidence, rank 3 (retinal dystrophy) includes one highly relevant publication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/) | 2024 | Pre-clinical / Drug repurposing | Nature Communications | Combination treatment (tamsulosin + metoprolol + **bromocriptine**) demonstrated mutation-agnostic efficacy in pre-clinical retinopathy models by suppressing intracellular cAMP and Ca²⁺ via GPCR modulation. Direct drug repurposing evidence for bromocriptine in inherited retinal disease. |

> This finding suggests an emerging research direction, though evidence remains pre-clinical (L4). The remaining 14 publications retrieved for this indication are tangentially related (covering extraocular anomalies, congenital ptosis, orbital pathology) and do not specifically address bromocriptine for retinal dystrophy.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Registration details pending) | — | — | — |
| (Registration details pending) | — | — | — |

> Bromocriptine has **2 registered products** in Malaysia with market status **"Marketed"**. Specific registration numbers, product names, dosage forms, and approved indications were not available in the current data extract. Please consult the NPRA database for complete registration details.

---

## Safety Considerations

> Please refer to the package insert for safety information.

**Known pharmacological safety concerns relevant to this repurposing evaluation:**

- **Psychosis risk**: Bromocriptine, as a dopamine D2 agonist, carries an inherent risk of inducing or exacerbating psychotic symptoms. At least one published case report documents bromocriptine-induced schizophrenia (PMID: 8120934). This is a critical concern for any schizophrenia-related repurposing.
- **Detailed warnings, contraindications, and drug interaction data** were not available in the current evidence pack (classified as Blocking data gap DG001). Completion of safety profile review via NPRA package insert analysis is required before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bromocriptine has a well-documented pharmacological interaction with dopamine pathways relevant to schizophrenia, and a modest body of clinical literature (L3) supports its potential to improve negative symptoms when used adjunctively at low doses. However, the fundamental paradox — a D2 agonist for a disease treated by D2 antagonists — poses significant safety concerns, including the risk of psychotic exacerbation. The clinical trials identified focus on managing antipsychotic side effects (hyperprolactinemia, metabolic syndrome), not on treating core schizophrenia symptoms. The remaining 9 TxGNN predictions involve ultra-rare genetic disorders with no mechanistic rationale or clinical evidence, likely reflecting knowledge graph topology bias rather than genuine biological signals.

**To proceed, the following is needed:**
- Complete safety profile review (NPRA package insert warnings, contraindications, DDI — currently a Blocking data gap)
- DrugBank ID confirmation and detailed MOA documentation
- Systematic review of all published adjunctive bromocriptine trials in schizophrenia, with focus on dose-response relationship and negative symptom outcomes
- Assessment of whether modern atypical antipsychotics (with lower D2 occupancy) create a safer context for adjunctive D2 agonist therapy
- For the retinal dystrophy prediction (rank 3): monitoring of clinical translation from the 2024 Nature Communications pre-clinical findings
- Validation of TxGNN model predictions for rare disease indications (ranks 1–8) — recommend flagging as likely false positives due to low-degree node bias

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

