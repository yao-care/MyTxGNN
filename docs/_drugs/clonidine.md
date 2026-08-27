---
layout: default
title: Clonidine
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Clonidine
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

# Clonidine: From Hypertension to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Clonidine is a centrally-acting α2-adrenergic agonist, classically used to treat hypertension. The TxGNN model predicts it may also be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)** — an indication already supported by **17 clinical trials** (including four completed Phase 3 RCTs) and **19 publications**, and already approved elsewhere as Kapvay/CLONICEL (clonidine extended-release). A closely related model output, "ADHD, inattentive type," scored almost identically but has no independent evidence — it is a DSM subtype of the same disease entity and should be read as inheriting the ADHD evidence below, not as a separate data gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (established pharmacological indication; the Malaysia NPRA registration record exists but its label text was not captured in this data pack — see note in Safety Considerations) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.9996% (model rank 25; the "inattentive type" subtype entry scored 99.9997%, model rank 22) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clonidine is a centrally-acting α2A-adrenergic receptor agonist. α2A-agonism strengthens prefrontal cortex signal transmission by reducing noradrenergic tone at postsynaptic α2A receptors — this is not a speculative mechanism but the actual FDA-approved mechanism behind Kapvay (clonidine extended-release), approved in 2010 as monotherapy or adjunctive therapy for ADHD. In other words, this is not an exploratory repurposing signal; it reflects an indication already established for the same molecule under a different brand/formulation.

The two top-ranked TxGNN outputs — "attention deficit-hyperactivity disorder" and "attention deficit hyperactivity disorder, inattentive type" — are the same underlying disease entity. The inattentive subtype is a DSM-5 clinical descriptor of ADHD rather than a biologically distinct condition, and approved clonidine ER labeling does not differentiate by subtype. The inattentive-type node therefore has no independent trial or literature evidence in this pack; its supporting evidence should be read as inherited from the general ADHD entry below.

Detailed formal MOA annotation (e.g., DrugBank structured data) is flagged as a data gap in this evidence pack. Based on the mechanistic rationale captured from the evidence itself, clonidine's α2A-agonist activity is pharmacologically consistent with its established, FDA-approved role in ADHD management alongside stimulants and other non-stimulants (atomoxetine, guanfacine).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00641329](https://clinicaltrials.gov/study/NCT00641329) | Phase 3 | Completed | 198 | CLONICEL (clonidine HCl sustained release) as add-on to psychostimulant therapy vs. psychostimulant alone in children/adolescents with ADHD |
| [NCT00031395](https://clinicaltrials.gov/study/NCT00031395) | Phase 3 | Completed | 122 | CAT trial — classic controlled study of clonidine alone or combined with methylphenidate in children 7–12 with ADHD |
| [NCT00556959](https://clinicaltrials.gov/study/NCT00556959) | Phase 3 | Completed | 236 | Dose-response evaluation of CLONICEL vs. placebo in children/adolescents with ADHD |
| [NCT00723190](https://clinicaltrials.gov/study/NCT00723190) | Phase 3 | Completed | 303 | 12-month open-label chronic exposure safety study of CLONICEL, as monotherapy or combined with stimulants |
| [NCT01439126](https://clinicaltrials.gov/study/NCT01439126) | Phase 4 | Completed | 135 | Randomized-withdrawal study confirming long-term efficacy and safety of KAPVAY (clonidine ER) in children/adolescents with ADHD |
| [NCT07044609](https://clinicaltrials.gov/study/NCT07044609) | Phase 4 | Not yet recruiting | 162 | Placebo-controlled trial of clonidine ER (Onyda XR) in children 6–12 with ADHD and comorbid oppositional defiant disorder |
| [NCT00414921](https://clinicaltrials.gov/study/NCT00414921) | Phase 2 | Completed | 30 | Preschool (ages 4–6) supplement study of clonidine and methylphenidate, alone or combined, for ADHD |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic SMART-design trial comparing stimulants and alpha-2 agonists (incl. clonidine) for ADHD in youth with autism spectrum disorder |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Unknown | 32 | Clonidine's effect on night-time sleep and day-time aggression in children with Tourette's syndrome and comorbid ADHD |
| [NCT06910605](https://clinicaltrials.gov/study/NCT06910605) | N/A | Recruiting | 26 | Driving-simulation study examining medication holidays in adults with ADHD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Network Meta-analysis | The Lancet Psychiatry | Comparative efficacy/tolerability of ADHD medications across children, adolescents, and adults |
| [37166701](https://pubmed.ncbi.nlm.nih.gov/37166701/) | 2023 | Systematic Review | CNS Drugs | Non-stimulant medications (including clonidine) for adult ADHD, as monotherapy or adjunct to stimulants |
| [39760346](https://pubmed.ncbi.nlm.nih.gov/39760346/) | 2025 | Systematic Review | Pediatric Annals | Non-stimulant ADHD medications as alternatives for patients who cannot tolerate or don't respond to stimulants |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Network Meta-analysis | The Lancet Psychiatry | Comparative cardiovascular safety of ADHD medications — hemodynamic and ECG effects across children, adolescents, adults |
| [28391425](https://pubmed.ncbi.nlm.nih.gov/28391425/) | 2017 | Systematic Review | Paediatric Drugs | Safety, tolerability, and efficacy of drugs (including clonidine) for behavioral insomnia in children with ADHD |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Current Pharmaceutical Design | Psychopharmacology of ADHD — effects and side effects of major drug classes |
| [24259638](https://pubmed.ncbi.nlm.nih.gov/24259638/) | 2014 | Review | The Annals of Pharmacotherapy | Pathophysiology, etiology, and treatment overview of ADHD |
| [28700715](https://pubmed.ncbi.nlm.nih.gov/28700715/) | 2017 | Network Meta-analysis | PLoS ONE | Efficacy and safety of pharmacological, psychological, and CAM interventions for ADHD in children/adolescents |
| [38506810](https://pubmed.ncbi.nlm.nih.gov/38506810/) | 2024 | Cohort | JAMA Network Open | Association between specific ADHD medications and work disability / mental health outcomes |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Cohort | Psychiatry Investigation | Efficacy and safety of clonidine adhesive patch in Tourette syndrome patients with comorbid ADHD |

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack's NPRA-sourced warnings, contraindications, and drug-interaction data are flagged as blocking data gaps (not yet retrieved), so no drug-specific safety statements can be made from the current dataset — this must be resolved before an S1 safety pre-screen can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ADHD indication is backed by L1-level evidence — four completed Phase 3 RCTs plus a completed Phase 4 randomized-withdrawal trial — and reflects a mechanism (α2A-agonism) already approved for this exact use in other markets (Kapvay/CLONICEL). However, this candidate's basic regulatory and safety data (NPRA label warnings, contraindications, formal MOA record) are currently blocking gaps, so guardrails are required before any clinical or regulatory action.

**To proceed, the following is needed:**
- Retrieve NPRA label PDF for this Malaysia registration (license number, product name, approved indication text, dosage form) — currently blank in the dataset
- Retrieve package insert warnings/contraindications and DDI data (currently "[Data Gap]" / not found)
- Confirm formal MOA/DrugBank record for α2A-adrenergic mechanism documentation
- Clarify route/formulation availability in Malaysia against the extended-release formulation used in the pivotal ADHD trials (immediate-release vs. ER may not be interchangeable for this indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

