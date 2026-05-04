---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: From Spasticity to Nicotine Dependence

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist originally used for the treatment of spasticity associated with conditions such as multiple sclerosis and spinal cord injuries. The TxGNN model predicts it may be effective for **Nicotine Dependence** (Rank 2, Evidence Level L2) and **Attention Deficit-Hyperactivity Disorder** (Rank 1, Evidence Level L5), with **3 clinical trials** and **20 publications** supporting the nicotine dependence direction, while the ADHD prediction currently relies on model inference with only indirect literature support.

---

## Quick Overview

### Prediction 1: Attention Deficit-Hyperactivity Disorder (ADHD)

| Item | Content |
|------|------|
| Original Indication | Spasticity (approved indication text not available in current dataset) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 — Model prediction only, no direct clinical studies |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

### Prediction 2: Nicotine Dependence

| Item | Content |
|------|------|
| Original Indication | Spasticity (approved indication text not available in current dataset) |
| Predicted New Indication | Nicotine Dependence |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L2 — 1 completed Phase 2 RCT |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

### Mechanism of Action

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, baclofen is a selective GABA-B (gamma-aminobutyric acid type B) receptor agonist. It acts by binding to GABA-B receptors in the spinal cord and brain, inhibiting excitatory neurotransmitter release and reducing monosynaptic and polysynaptic reflexes. Its original approval is for the management of spasticity resulting from multiple sclerosis, spinal cord injuries, and other spinal cord diseases.

### Nicotine Dependence — Mechanistic Rationale (Moderate to Strong)

The GABA-B receptor plays a critical role in modulating the mesolimbic dopamine reward pathway. Activation of GABA-B receptors by baclofen inhibits dopamine neuronal firing in the ventral tegmental area (VTA), thereby attenuating the rewarding and reinforcing effects of nicotine. Multiple preclinical studies (PMID 24553576, 18682277, 19250803) have directly demonstrated that baclofen reduces nicotine conditioned place preference, discriminative stimulus effects, and drug-induced reinstatement of nicotine-seeking behaviour. This mechanism is consistent with baclofen's extensively studied role in alcohol use disorder, where it has already received approval in France. The GABAergic hypothesis of nicotine dependence provides a plausible pharmacological bridge from baclofen's known receptor activity to smoking cessation.

### ADHD — Mechanistic Rationale (Weak)

The core pathophysiology of ADHD involves dysregulation of the dopamine and norepinephrine pathways, whereas baclofen acts primarily on the GABAergic system. While there is theoretical interest in the role of GABA in impulse control circuits (PMID 24062084), and baclofen has been studied in Tourette syndrome (which is frequently comorbid with ADHD), there is no direct pharmacological link between GABA-B agonism and the attention/executive function deficits central to ADHD. The retrieved literature primarily mentions ADHD as a comorbidity within studies of other neuropsychiatric conditions (e.g., Tourette syndrome, autism spectrum disorders), rather than as a direct treatment target for baclofen.

---

## Clinical Trial Evidence

### Prediction 1: ADHD

Currently no related clinical trials registered.

### Prediction 2: Nicotine Dependence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Examined baclofen's effects on brain responses and behaviour in cigarette smokers using perfusion fMRI and dopaminergic gene association approach. Investigated whether baclofen reduces appetitive cue-sensitive neural responses and smoking behaviour. Most important completed evidence source. |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Evaluated baclofen's efficacy in reducing smoking urge, withdrawal, and reinforcement in moderate-to-heavy smokers. Terminated but enrolled 41 participants; partial data may be available. Termination reason is a key consideration. |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Directly tested the GABAergic hypothesis of nicotine dependence in a randomized, placebo-controlled design. Terminated early after enrolling only 6 participants — insufficient to draw efficacy conclusions. Termination cause (recruitment difficulty vs. safety concern) requires investigation. |

---

## Literature Evidence

### Prediction 1: ADHD

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Reviewed treatment of tics in Tourette syndrome (comorbid with ADHD); baclofen not a primary focus for ADHD itself |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurol | Enrolled 450 patients with tics/Tourette syndrome treated with baclofen/botulinum toxin; ADHD mentioned as comorbidity |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clin Neuropharmacol | Mood stabilizers in ASD children; ADHD discussed as comorbid condition, baclofen not directly studied for ADHD |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | Emerging treatments in Tourette syndrome; ADHD as comorbidity, baclofen discussed for tics only |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical | Psychopharmacology | α2A-adrenergic agonist (guanfacine) in ventral hippocampus reduces impulsive decision-making; GABA role in impulsivity mentioned peripherally |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | Tourette syndrome management; baclofen listed among newer agents for tics, ADHD addressed as comorbidity |

> **Note:** None of the retrieved literature directly investigates baclofen as a treatment for ADHD. All references mention ADHD as a comorbid condition within studies of Tourette syndrome, autism, or impulse control.

### Prediction 2: Nicotine Dependence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Clinical/RCT | Neuropsychopharmacology | Double-blind, placebo-controlled RCT of baclofen for concurrent alcohol and nicotine dependence — direct clinical evidence |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Preclinical | Psychopharmacology | Baclofen attenuated nicotine rewarding properties and withdrawal manifestations in rodents |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Preclinical | Eur Neuropsychopharmacol | Baclofen prevented drug-induced reinstatement of nicotine-seeking behaviour and nicotine place preference in rodents |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Preclinical | Neurosci Lett | Baclofen reduced conditioned rewarding and discriminative stimulus effects of nicotine in rats at high doses |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Preclinical | Prog Neuropsychopharmacol Biol Psychiatry | Baclofen prevented nicotine withdrawal-related α4β2 nicotinic receptor density changes in mice |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B receptors as therapeutic targets for substance use disorders, including nicotine; PAMs may offer better side-effect profile |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Review of current and emerging tobacco cessation pharmacotherapies; baclofen discussed as emerging candidate |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opin Emerg Drugs | Emerging drugs for tobacco dependence; baclofen included among GABAergic candidates |
| [17338593](https://pubmed.ncbi.nlm.nih.gov/17338593/) | 2007 | Review | CNS Drugs | Pharmacotherapy of dual substance abuse; baclofen reviewed for combined alcohol–nicotine dependence treatment |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review | Int Rev Neurobiol | Drug repurposing for alcohol use disorder; baclofen listed among approved medications in France, mechanism applicable to nicotine |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details unavailable) | — | — | — |
| (Details unavailable) | — | — | — |
| (Details unavailable) | — | — | — |
| (Details unavailable) | — | — | — |
| (Details unavailable) | — | — | — |

> **Note:** 6 registrations are recorded in the Malaysian market (status: Marketed), but detailed license information (authorization numbers, product names, dosage forms, approved indications) was not available in the current dataset. Please consult the NPRA database for complete registration details.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack. As baclofen is a centrally acting agent, clinicians should be aware of common class effects including sedation, drowsiness, dizziness, weakness, and the risk of withdrawal seizures upon abrupt discontinuation.

---

## Conclusion and Next Steps

### Prediction 1: ADHD

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.32%), but there is no direct clinical or preclinical evidence supporting baclofen for ADHD treatment. All retrieved literature only tangentially mentions ADHD as a comorbidity in Tourette syndrome or autism studies. The mechanistic link between GABA-B agonism and ADHD's core dopaminergic/noradrenergic pathology is extremely weak. This prediction does not warrant further development at this time.

**To proceed, the following would be needed:**
- Direct preclinical studies demonstrating baclofen's effect on ADHD-relevant behavioural endpoints (sustained attention, hyperactivity, impulsivity)
- Mechanistic studies linking GABA-B modulation to prefrontal dopamine/norepinephrine signalling relevant to ADHD
- At least one pilot clinical trial specifically targeting ADHD symptoms

---

### Prediction 2: Nicotine Dependence

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial (NCT01821560, n=44) directly examined baclofen's effects on brain and behavioural responses in smokers, providing the strongest available clinical evidence. A solid body of preclinical research (≥4 animal studies) consistently demonstrates that baclofen attenuates nicotine reward, withdrawal, and relapse. The GABAergic hypothesis of nicotine dependence is mechanistically coherent and supported by baclofen's established efficacy in alcohol use disorder (approved in France). However, two of three clinical trials were terminated, and definitive efficacy data from Phase 3 trials is lacking.

**To proceed, the following is needed:**
- Obtain and review published results from NCT01821560 (completed trial) to confirm efficacy signal
- Investigate termination reasons for NCT01228994 and NCT00257894 (recruitment vs. safety)
- Detailed mechanism of action data (MOA) from DrugBank
- NPRA package insert review for key warnings and contraindications
- Safety monitoring plan, particularly for sedation and CNS depression in combination with other substances
- Consideration of a Phase 2b/3 dose-finding trial if efficacy signal is confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

