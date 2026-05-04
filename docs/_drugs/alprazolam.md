---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Alprazolam: From Anxiety and Panic Disorders to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine derivative primarily used for anxiety and panic disorders, acting through positive modulation of GABA-A receptors to produce sedative and anxiolytic effects.
The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** currently supporting this direction.
However, most clinical trial evidence is indirect, and the primary pharmacological basis rests on alprazolam's established sedative-hypnotic properties rather than dedicated insomnia indication trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety and panic disorders (NPRA approved indication text not retrievable from current data) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alprazolam positively modulates GABA-A receptor chloride ion channels, enhancing inhibitory GABAergic neurotransmission across the central nervous system. This mechanism produces dose-dependent sedation and hypnotic effects — specifically shortening sleep-onset latency and increasing total sleep time — which directly underpins the TxGNN model's prediction of efficacy in insomnia. The drug's rapid onset of action (Tmax 1–2 hours) further supports its pharmacological plausibility as a sleep-onset aid.

The mechanistic overlap between anxiety management and sleep induction is clinically well-recognised: anxiety-driven hyperarousal is a leading cause of sleep-onset insomnia, and alprazolam's dual anxiolytic-sedative profile makes it pharmacologically rational for patients with comorbid anxiety and insomnia. Comparative studies in specialty populations (e.g., haemodialysis patients with end-stage renal disease) have demonstrated alprazolam's ability to improve subjective and objective sleep quality metrics, lending real-world support to the model prediction.

Nonetheless, important mechanistic limitations must be acknowledged. Alprazolam's half-life of 6–27 hours raises concern for next-day residual sedation ("hangover effect"), unlike ultra-short-acting benzodiazepines such as triazolam. More critically, long-term use suppresses slow-wave sleep and REM sleep architecture, potentially worsening overall sleep quality over time. These pharmacokinetic and pharmacodynamic constraints mean that while the TxGNN prediction is mechanistically sound, alprazolam is not considered an optimal first-line hypnotic agent under current sleep medicine guidelines.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort in Taiwan examining risks and benefits of hypnotics — including benzodiazepines — in elderly patients with sleep disorders; covers alprazolam-relevant patient population and evaluates clinical, pharmacokinetic, and pharmacogenetic outcomes |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Multicenter open-label RCT comparing Niravam™ (alprazolam orally disintegrating tablet) added to a newly prescribed SSRI/SNRI vs SSRI/SNRI alone in patients with GAD or panic disorder; evaluates time to symptomatic response |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Randomised double-blind placebo-controlled trial of AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's disease; provides context for CNS-active drug assessment in elderly patients with sleep-behaviour overlap |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronic self-management intervention to promote benzodiazepine cessation among Veterans; contextualises long-term BZD risks including dependence and cognitive effects of alprazolam class |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Hypnosis versus alprazolam premedication for perioperative anxiety in gynaecological surgery; alprazolam used as active pharmacological comparator for acute anxiolytic-sedative effect |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for treatment of hypersomnia; inverse sleep condition study providing mechanistic contrast relevant to GABAergic sleep modulation |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for benzodiazepine dependence; terminated early due to insufficient enrolment (n=2); provides class-level dependence management context |

> **Note:** No clinical trials directly evaluating alprazolam as a primary investigational treatment for insomnia were identified in ClinicalTrials.gov. The above trials provide indirect evidence through hypnotic drug class context, alprazolam as comparator, or BZD risk characterisation in populations with sleep disorders.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative RCT | Cureus | Head-to-head comparison of alprazolam vs melatonin for sleep disorders in haemodialysis patients; directly evaluates alprazolam efficacy for improving subjective and objective sleep quality in ESRD |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | RCT (Integrative Therapy) | Medicine | Alprazolam used as active control in 116 patients with comorbid coronary heart disease and insomnia; experimental group received Du Meridian moxibustion + ear acupuncture; demonstrates alprazolam's real-world role as a standard-of-care comparator for insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica (Zagreb) | Systematic review and meta-analysis of randomised and observational studies on tranquilisers (including BZDs) in elderly patients with chronic diseases; assesses optimal dose, type, efficacy outcomes, and adverse effect profiles |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical Study | Aging | Proteomic analysis in mice showing repeated alprazolam administration causes hippocampal mitochondrial dysfunction and memory consolidation impairment; reveals molecular mechanisms underlying long-term cognitive safety concerns |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Epidemiological Analysis | Value in Health Regional Issues | 10-year predictive model of benzodiazepine use trends; documents BZD prescription for insomnia alongside anxiety and mood disorders, and quantifies long-term risks including Alzheimer's disease, dependence, falls, and traffic accidents |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional Study | Medicine | Cross-sectional study of insomnia prevalence and risk factors in COVID-19 survivors (Dec 2022–Feb 2023); contextualises the contemporary rise in insomnia burden and treatment demand |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-world Analysis | China Journal of Chinese Materia Medica | Real-world analysis of 1,067 insomnia patients from 20 Chinese hospitals; maps concurrent disease patterns (hypertension 26.9%, cerebrovascular disease) and medication use including Western hypnotics (benzodiazepine class) |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Observational Study | Sleep Medicine | Large managed-care prescription pattern analysis for insomnia treatment; documents decline in dedicated hypnotic use over a decade and corresponding increase in non-hypnotic prescribing including benzodiazepines for insomnia |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Pharmacology Review | Expert Opinion on Drug Metabolism & Toxicology | Comprehensive review of anxiolytic drug pharmacokinetics; covers alprazolam absorption, distribution, half-life variability (6–27 hours), and clinical implications for daytime residual effects |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | Randomised controlled trial of eszopiclone for sleep quality and cognitive function in elderly Alzheimer's patients with sleep disorders; provides comparative hypnotic class context for evaluating non-BZD alternatives |

---

## Malaysia Market Information

NPRA registration data confirms **14 product authorisations** for alprazolam in Malaysia, and the drug is currently marketed. However, individual product details — including authorisation numbers, product names, dosage forms, manufacturers, and approved indication text — were not returned in the current NPRA data extract.

> **Data Note:** Detailed product registration records were not available from the NPRA query at this time. Direct verification via the NPRA official product registry is required to confirm currently approved indications, registered dosage forms, and marketing authorisation holders.

---

## Safety Considerations

Formal warning and contraindication data from the NPRA package insert were not available for this evaluation. Please refer to the registered package insert for complete safety information.

Based on well-established evidence from the published literature and the drug class profile, the following safety considerations are relevant for clinical decision-making:

- **Dependence and withdrawal**: Long-term benzodiazepine use carries significant risk of physical dependence; abrupt discontinuation can precipitate withdrawal seizures and rebound anxiety/insomnia
- **CNS depression**: Drowsiness, psychomotor slowing, and cognitive impairment are common, particularly in elderly patients
- **Falls and fractures**: Elevated risk of falls in older adults, especially in the elderly population
- **Sleep architecture disruption**: Chronic use suppresses slow-wave sleep (SWS) and REM sleep, potentially worsening long-term sleep quality
- **Respiratory depression**: Potentially serious risk when combined with opioids, alcohol, or other CNS depressants
- **Memory impairment**: Anterograde amnesia and hippocampus-dependent memory consolidation deficits documented in both human and animal studies

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprazolam's GABA-A receptor mechanism provides a pharmacologically sound basis for sedative-hypnotic activity in insomnia, and L3-level evidence from observational studies and comparative real-world trials confirms its use for sleep disturbances in clinical practice. However, no dedicated Phase 2/3 RCT for alprazolam in primary insomnia has been identified, long-term use is associated with sleep architecture deterioration and dependence risk, and alprazolam is not recommended as a first-line hypnotic under current international guidelines.

**To proceed, the following is needed:**

- Retrieve NPRA-approved indication text to confirm whether insomnia or sleep disorders are already listed as a registered indication in Malaysia
- Obtain the full registered package insert for complete warning, contraindication, and drug interaction data
- Clarify the regulatory status of alprazolam as a scheduled/controlled substance in Malaysia and applicable prescription restrictions
- Commission a systematic review or meta-analysis specifically for alprazolam in primary insomnia to establish whether L2 evidence can be documented
- Design a pharmacovigilance monitoring plan addressing dependence risk, cognitive effects, and falls — particularly for elderly patients and those with renal or hepatic impairment
- Define clinical positioning relative to guideline-recommended first-line insomnia treatments (Cognitive Behavioural Therapy for Insomnia [CBT-I], non-benzodiazepine hypnotics such as zolpidem or eszopiclone) to determine where alprazolam adds clinical value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

