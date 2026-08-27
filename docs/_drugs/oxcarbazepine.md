---
layout: default
title: Oxcarbazepine
parent: 僅模型預測 (L5)
nav_order: 525
evidence_level: L5
indication_count: 10
---

# Oxcarbazepine
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

# Oxcarbazepine: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

> Oxcarbazepine is a widely used antiepileptic drug (AED), originally approved for partial-onset seizures.
> The TxGNN model's top-ranked prediction highlights **Visual Epilepsy** (a reflex epilepsy subtype triggered by visual stimuli),
> currently supported by **1 clinical trial** and **19 publications**, though none specifically designed for this subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial-onset seizures (epilepsy)* |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

*\*Malaysia (NPRA) license text was not captured in this data extract (see Malaysia Market Information below); this original indication is drawn from the clinical-trial/literature evidence in this pack, which consistently documents partial-onset seizures as oxcarbazepine's core approved indication (see rank 9, "partial epilepsy" candidate).*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not retrieved from DrugBank for this pack (Data Gap DG002). However, the accompanying literature evidence consistently describes oxcarbazepine (via its active metabolite, the 10-monohydroxy derivative, MHD) as a voltage-gated sodium channel blocker that limits high-frequency neuronal firing — the same mechanism underlying its approved use in partial-onset seizures (PMID [8156978](https://pubmed.ncbi.nlm.nih.gov/8156978/)).

Visual epilepsy is a reflex epilepsy subtype in which seizures are triggered by visual stimuli (e.g., flickering light, patterns), driven by localized cortical hyperexcitability rather than a distinct disease mechanism. Because reflex epilepsies sit within the broader epilepsy spectrum, a broad-spectrum sodium-channel blocker with proven efficacy across focal seizure types is mechanistically plausible for this subtype as well.

That said, this is a **class-level extension** of an already-approved mechanism rather than a novel pharmacological hypothesis. As the evidence pack itself notes, no prospective trial has specifically enrolled or evaluated visually-triggered/reflex epilepsy patients — the supporting Phase 4 trial and literature address antiepileptic drugs (including oxcarbazepine) in focal epilepsy broadly, not this subtype specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | "Liceo Study" — observational assessment of new AEDs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, tiagabine, topiramate) as first-choice bitherapy in focal epilepsy; not designed specifically for visually-induced/reflex seizures (relevance grade B). |

---

## Literature Evidence

*Note: No retrieved literature specifically addresses visual/photosensitive epilepsy. The entries below reflect general oxcarbazepine/epilepsy evidence supporting the broader mechanistic class.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | RCT | CNS Neurosci Ther | Multicenter, open-label, randomized comparison of oxcarbazepine vs. levetiracetam monotherapy in newly diagnosed focal epilepsy (China). |
| [27845825](https://pubmed.ncbi.nlm.nih.gov/27845825/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Withdrawn Cochrane review on oxcarbazepine add-on therapy for drug-resistant partial epilepsy. |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Review | JAMA | Overview of antiseizure medications for adults with epilepsy, including oxcarbazepine's role. |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Current role of carbamazepine and oxcarbazepine in epilepsy management amid newer AEDs. |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Review | Continuum (Minneap Minn) | Comprehensive review of antiepileptic drugs including pharmacokinetics and modes of use. |
| [19445769](https://pubmed.ncbi.nlm.nih.gov/19445769/) | 2009 | Review | BMJ Clin Evid | General epilepsy treatment evidence review. |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Review (update) | Continuum (Minneap Minn) | 2025 update on antiseizure medications, covering pharmacokinetics and indications. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Update on pharmacotherapy for trigeminal neuralgia; discusses carbamazepine/oxcarbazepine efficacy and dose-limiting toxicity. |
| [37092337](https://pubmed.ncbi.nlm.nih.gov/37092337/) | 2023 | Review | Pharmacogenomics | Pharmacogenomic variability in oxcarbazepine efficacy/safety across populations. |
| [16450324](https://pubmed.ncbi.nlm.nih.gov/16450324/) | 2006 | Review | Rev Neurol | Review and update on oxcarbazepine mechanism of action, efficacy, safety, and clinical use. |

---

## Malaysia Market Information

Malaysia (NPRA) registry data confirms **2 active marketing authorizations** for oxcarbazepine (market status: Marketed). However, the per-license fields (authorization number, product name, dosage form, and approved indication text) were not populated in this data extract — no license record contained a non-empty entry. Retrieving the full NPRA license detail is needed to complete this table.

---

## Safety Considerations

Formal Malaysia/TFDA safety data (key warnings, contraindications, DDI) was not retrieved for this pack (Data Gap DG001; DDI query returned no results). Please refer to the package insert for authoritative safety information.

For context, the literature evidence in this pack repeatedly flags two class-recognized safety signals for oxcarbazepine, relevant to future safety review:
- **Hyponatremia**, reported as one of the most common adverse effects, particularly with longer treatment duration (PMID [35629976](https://pubmed.ncbi.nlm.nih.gov/35629976/), [33576502](https://pubmed.ncbi.nlm.nih.gov/33576502/), [27333872](https://pubmed.ncbi.nlm.nih.gov/27333872/)).
- **HLA-associated cutaneous adverse reactions** (DRESS, maculopapular eruption), with genetic risk alleles (e.g., HLA-A*31:01, HLA-B*15:02, HLA-B*40:02) reported in Asian populations (PMID [29610167](https://pubmed.ncbi.nlm.nih.gov/29610167/), [30599396](https://pubmed.ncbi.nlm.nih.gov/30599396/), [27666425](https://pubmed.ncbi.nlm.nih.gov/27666425/)) — potentially relevant given Malaysia's population genetics.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Oxcarbazepine's core mechanism (sodium channel blockade) and its established efficacy in partial-onset seizures provide reasonable mechanistic support for a class-level extension to visual/reflex epilepsy. However, all supporting evidence is at the general-AED/general-epilepsy level (L3) — no clinical trial or case series has specifically evaluated visually-triggered seizures, so this remains a plausible but unconfirmed hypothesis rather than a validated indication.

**To proceed, the following is needed:**
- Subtype-specific clinical evidence (case series or trial) for visually-induced/reflex epilepsy
- TFDA/NPRA package insert data — warnings, contraindications, DDI (Data Gap DG001)
- Confirmed mechanism-of-action data from DrugBank (Data Gap DG002)
- Complete Malaysia NPRA license details (product name, dosage form, indication text) for the 2 registered authorizations
- Pharmacogenomic screening consideration (HLA-A*31:01/B*15:02) given Malaysia's population diversity

*Note: Among the other TxGNN-predicted candidates in this pack, "partial epilepsy" (rank 9) is not a novel repurposing target — it is oxcarbazepine's already-approved core indication, supported by L1 evidence (multiple completed Phase 3 RCTs). The remaining candidates (restless legs syndrome, eating/audiogenic/orgasm-induced/thinking/startle/micturition-induced seizures, status epilepticus) scored L4–L5 with "Hold" recommendations due to sparse or preclinical-only evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

