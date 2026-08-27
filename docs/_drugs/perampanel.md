---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Perampanel is a selective, non-competitive AMPA-receptor antagonist marketed as an antiepileptic drug (AED) for focal-onset and primary generalized tonic-clonic seizures. The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a visually/photosensitivity-triggered reflex epilepsy), with a **99.92% prediction score**, but currently only **3 clinical trials** and **20 publications** exist — none of them specific to visual epilepsy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (focal-onset seizures ± secondary generalization; primary generalized tonic-clonic seizures) — inferred from drug class across the pack's literature; Malaysia-specific approved indication text was not captured in this data pull |
| Predicted New Indication | Visual Epilepsy (photosensitive / visually-induced seizures) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a flagged data gap (DG002). However, the clinical literature captured in this pack consistently and independently identifies perampanel as a first-in-class, selective, non-competitive AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) receptor antagonist, approved as adjunctive/monotherapy for focal-onset seizures and primary generalized tonic-clonic seizures.

Visual epilepsy is a form of reflex epilepsy in which seizures are triggered by visual stimuli (e.g., photosensitivity), reflecting transient cortical hyperexcitability in visual/occipital cortex. Since perampanel's original indication (epilepsy generally) already covers seizure disorders driven by excessive glutamatergic/AMPA-mediated excitation, the mechanistic leap to a specific reflex-epilepsy subtype is biologically plausible — broad-spectrum suppression of cortical hyperexcitability could, in principle, blunt stimulus-triggered discharges regardless of the trigger modality.

That said, this remains a mechanism-only inference. None of the 3 associated clinical trials or 20 publications study visual epilepsy specifically — they are general-population epilepsy PK/safety/EEG studies. A related reflex-epilepsy analog (audiogenic seizures, rank 7 in this candidate set) has direct preclinical validation in the DBA/2 mouse model, which lends indirect plausibility to the broader "reflex epilepsy" mechanistic class, but no such preclinical or clinical work exists yet for the visual trigger specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Tolerability, safety, and pharmacokinetics of perampanel (E2007) in patients with refractory partial or generalized seizures — general epilepsy population, not visual-epilepsy specific |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Effects of perampanel on cognition and EEG in patients with refractory partial-onset seizures — non-disease-specific |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Effects of perampanel on neurophysiology tests (EEG, SEP, BAEP, and visual evoked potential/VEP) in healthy volunteers — closest visual-modality link, but not a visual-epilepsy efficacy trial |

*None of these trials specifically enroll or evaluate visual/photosensitive epilepsy patients.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review & Meta-analysis | Seizure | Efficacy and safety of perampanel across RCTs for focal-onset and primary generalized tonic-clonic seizures |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review / Network Meta-analysis | Journal of Neurology | Compares ASM efficacy/safety (incl. perampanel) for idiopathic generalized epilepsies |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES guideline update on efficacy/tolerability of newer AEDs for new-onset epilepsy |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review (clinical trial + real-world evidence) | Epilepsy & Behavior | Perampanel monotherapy for focal-onset and generalized tonic-clonic seizures |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review & Meta-analysis | Brain & Development | Efficacy, tolerability, and safety of perampanel in children/adolescents with epilepsy |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review (drug development history) | Expert Opinion on Drug Discovery | History of perampanel's discovery and development as an AMPA-receptor antagonist AED |
| [41043235](https://pubmed.ncbi.nlm.nih.gov/41043235/) | 2025 | Prospective multicenter study | Epilepsy & Behavior | Perampanel effects on seizure control and sleep quality in people with epilepsy |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Cohort study | Annals of Clinical and Translational Neurology | Efficacy of perampanel in pediatric epilepsy with known/presumed genetic etiology |
| [27935018](https://pubmed.ncbi.nlm.nih.gov/27935018/) | 2017 | Cohort study | Developmental Medicine & Child Neurology | Tolerability and efficacy of perampanel in children with refractory epilepsy |
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Cohort study | The Medical Journal of Malaysia | Efficacy and safety of adjunctive perampanel in epilepsy patients (Malaysia-based cohort) |

*All 20 literature results describe perampanel's use in general epilepsy populations; none specifically address visual/photosensitive epilepsy as a distinct trigger subtype.*

---

## Malaysia Market Information

NPRA registry confirms **3 active registrations** for perampanel (market status: Marketed). However, the detailed license fields (registration number, product name, dosage form, manufacturer, approved indication text) were not returned in this data pull and require a direct NPRA lookup to populate.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DDI query returned no results). Note: the absence of TFDA/NPRA label warnings and contraindications is flagged as a **Blocking** data gap (DG001) — this must be resolved before any S1 safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.92%) and the AMPA-antagonist mechanism is biologically plausible for a reflex-epilepsy subtype, but evidence level is L4 (mechanism/analogy only) — none of the 3 trials or 20 publications specifically study visual epilepsy, and the safety data needed for even a preliminary S1 review is currently blocked (DG001).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, blocking)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Disease-specific preclinical evidence (e.g., a photosensitive/visual-trigger seizure model, analogous to the audiogenic-seizure DBA/2 mouse data available for a related candidate)
- Completed Malaysia license details (product name, dosage form, approved indication text) for regulatory cross-check
- A populated DDI dataset (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

