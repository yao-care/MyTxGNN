---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 5
---

# Aripiprazole
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

# Aripiprazole: From Schizophrenia / Bipolar Disorder to Autism Spectrum Disorder

## One-Sentence Summary

Aripiprazole is a third-generation atypical antipsychotic with a unique "dopamine system stabilizer" profile (D2/D3 partial agonist, 5-HT1A partial agonist, 5-HT2A antagonist), established globally for schizophrenia and bipolar disorder. The TxGNN model's top actionable prediction is **Autism** (irritability associated with autism spectrum disorder), backed by **multiple completed Phase 3 double-blind RCTs** and **20+ publications**, including FDA approval for this indication in children aged 6–17. Note: The highest-ranked model output was "autism susceptibility 1" (a genetic susceptibility locus), for which no clinical evidence exists and a Hold decision applies; the clinically actionable prediction is autism proper (Rank 2, Evidence Level L1).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia, Bipolar Disorder (established global approvals; Malaysia-specific indication text unavailable in current dataset) |
| Predicted New Indication | Autism (Irritability Associated with Autism Spectrum Disorder) |
| TxGNN Prediction Score | N/A (score field returned 0.00% — likely not computed in this model run) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 26 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aripiprazole functions as a dopamine system stabilizer through its partial agonism at D2 and D3 dopamine receptors and 5-HT1A serotonin receptors, combined with antagonism at 5-HT2A receptors. In brain regions where dopamine is pathologically elevated (e.g., the mesolimbic system during agitation or aggression), aripiprazole acts as a functional brake; in regions with insufficient dopaminergic tone (e.g., the prefrontal cortex), it provides partial support. Crucially, this mechanism is distinct from full D2 blockade: aripiprazole carries a markedly lower burden of extrapyramidal symptoms, metabolic disturbance, and sedation — properties that make it particularly suitable for long-term use in pediatric populations.

In autism spectrum disorder (ASD), the behavioral symptoms most disruptive to daily functioning — including irritability, explosive aggression, self-injurious behavior, and severe tantrums — are linked to dysregulation of dopaminergic and serotonergic circuits. The 5-HT1A partial agonist component of aripiprazole provides anxiolytic effects that may help stabilize emotional dysregulation; D2/D3 partial agonism blunts dopamine-driven impulsivity. Animal models have additionally shown that dopamine-stabilizing agents can improve repetitive behavior patterns and social behavioral deficits relevant to ASD.

This prediction is not speculative: aripiprazole received FDA approval in 2009 specifically for irritability associated with autistic disorder in children and adolescents aged 6–17 years, based on pivotal multicenter Phase 3 RCTs. The transition from a schizophrenia/bipolar disorder drug to ASD behavioral management is mechanistically coherent and clinically validated, making it one of the best-supported drug repurposing stories in pediatric psychiatry. The key clinical question for Malaysia is therefore not whether the evidence is sufficient, but whether this specific indication is currently registered among the 26 existing product licenses.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00332241](https://clinicaltrials.gov/study/NCT00332241) | Phase 3 | Completed | 98 | Multicenter double-blind RCT: aripiprazole flexible dose vs. placebo in children and adolescents with autistic disorder — one of the two FDA pivotal trials underpinning the 2009 approval for ASD irritability |
| [NCT00337571](https://clinicaltrials.gov/study/NCT00337571) | Phase 3 | Completed | 218 | Multicenter double-blind RCT: three fixed doses of aripiprazole (5/10/15 mg) vs. placebo in children and adolescents with autistic disorder — the companion FDA pivotal trial |
| [NCT00198107](https://clinicaltrials.gov/study/NCT00198107) | Phase 3 | Completed | 81 | Assessed aripiprazole and D-cycloserine in autism in children; directly evaluated aripiprazole as monotherapy for ASD-associated symptoms, considered a foundational approval-support trial |
| [NCT01227668](https://clinicaltrials.gov/study/NCT01227668) | Phase 4 | Completed | 215 | Long-term maintenance RCT: patients stabilized on aripiprazole were randomized to continue or switch to placebo; assessed time to relapse of irritability in pediatric autistic disorder |
| [NCT00365859](https://clinicaltrials.gov/study/NCT00365859) | Phase 3 | Completed | 330 | 52-week multicenter open-label extension providing long-term safety and tolerability data for aripiprazole in children and adolescents with autistic disorder; largest long-term safety dataset for this population |
| [NCT03487770](https://clinicaltrials.gov/study/NCT03487770) | Phase 3 | Completed | 111 | Multicenter double-blind RCT: aripiprazole oral solution (2–15 mg) vs. placebo over 8 weeks in children and adolescents with autistic disorder; assessed steady-state pharmacokinetics alongside efficacy |
| [NCT01617447](https://clinicaltrials.gov/study/NCT01617447) | Phase 3 | Completed | 92 | Short-term (8-week) oral aripiprazole efficacy and safety study in pediatric autistic disorder in Japan; provides Asia-specific clinical data |
| [NCT01617460](https://clinicaltrials.gov/study/NCT01617460) | Phase 3 | Completed | 86 | Long-term safety and efficacy extension of the short-term Japan study (NCT01617447) in pediatric autistic disorder; supports sustained use data in Asian populations |
| [NCT03179787](https://clinicaltrials.gov/study/NCT03179787) | Phase N/A | Completed | 528 | Post-marketing surveillance study in Japan evaluating real-world safety and effectiveness of aripiprazole in autism patients; the largest real-world dataset from an Asian market |
| [NCT01028820](https://clinicaltrials.gov/study/NCT01028820) | Phase 4 | Completed | 13 | 8-week fMRI neuroimaging study exploring brain activation patterns during aripiprazole treatment in ASD; provides mechanistic imaging evidence supporting the D2/serotonin pathway hypothesis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35101925](https://pubmed.ncbi.nlm.nih.gov/35101925/) | 2023 | Overview of Systematic Reviews | BMJ Evidence-Based Medicine | Synthesized multiple systematic reviews on risperidone and aripiprazole for children with ASD; aripiprazole showed significant, clinically meaningful reduction in irritability with a more favorable metabolic profile than risperidone |
| [35470032](https://pubmed.ncbi.nlm.nih.gov/35470032/) | 2023 | Systematic Review + Meta-analysis | JAACAP | First meta-analysis assessing a broad range of pharmacological interventions for emotional dysregulation and irritability in ASD; aripiprazole demonstrated statistically significant superiority over placebo in reducing irritability subscale scores |
| [38263251](https://pubmed.ncbi.nlm.nih.gov/38263251/) | 2024 | Systematic Review + Network Meta-analysis | Molecular Autism | Comprehensive NMA of pharmacological and non-pharmacological interventions for ASD irritability with GRADE assessment; aripiprazole ranked as one of the most effective pharmacological options with moderate-to-high quality evidence |
| [35246237](https://pubmed.ncbi.nlm.nih.gov/35246237/) | 2022 | Systematic Review + Network Meta-analysis | Molecular Autism | NMA investigating pharmacological and dietary-supplement treatments for ASD; confirmed aripiprazole efficacy for associated irritability and agitation symptoms across multiple study designs |
| [33857522](https://pubmed.ncbi.nlm.nih.gov/33857522/) | 2021 | Systematic Review | Progress in Neuro-Psychopharmacology & Biological Psychiatry | Comprehensive systematic review of pediatric psychopharmacology in ASD (Part I); detailed reconstruction of the aripiprazole evidence base from open-label to Phase 3 pivotal trials |
| [41004875](https://pubmed.ncbi.nlm.nih.gov/41004875/) | 2025 | RCT | Brain & Development | Head-to-head randomized controlled trial comparing risperidone vs. aripiprazole for reducing irritability severity in children with ASD; both effective, with aripiprazole offering a potentially superior metabolic safety profile |
| [39690490](https://pubmed.ncbi.nlm.nih.gov/39690490/) | 2025 | Network Meta-analysis | Journal of Psychopharmacology | Updated NMA comparing pharmacotherapies for agitation in ASD and intellectual disabilities in both children and adults; aripiprazole identified as an efficacious first-line pharmacological option across age groups |
| [36625807](https://pubmed.ncbi.nlm.nih.gov/36625807/) | 2023 | Narrative Review | JAMA | High-impact clinical review of ASD published in JAMA; explicitly notes aripiprazole as one of only two FDA-approved medications for ASD-associated irritability, reinforcing its guideline-level clinical positioning |
| [20643378](https://pubmed.ncbi.nlm.nih.gov/20643378/) | 2010 | Narrative Review | Neurotherapeutics | Foundational early review specifically examining aripiprazole in autism spectrum disorders and fragile X syndrome; summarized preclinical rationale and early clinical evidence that preceded the FDA approval pathway |
| [27388494](https://pubmed.ncbi.nlm.nih.gov/27388494/) | 2016 | Expert Review | Expert Review of Neurotherapeutics | Expert clinical review of aripiprazole for irritability and aggression in children and adolescents with ASD; affirms clinical positioning, dosing guidance (2–15 mg/day), and safety monitoring considerations post-FDA approval |

---

## Malaysia Market Information

Aripiprazole has **26 product registrations** confirmed in the Malaysia NPRA database with active market status. However, detailed product-level information — including individual authorization numbers, product names, dosage forms, and approved indication texts — was not captured in the current data extraction. The table below reflects this gap.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| Pending | (26 products registered in NPRA) | Pending | Pending — requires NPRA portal review |

> The key unresolved question for this repurposing evaluation is whether any of the 26 currently registered products in Malaysia carry an approved indication for irritability associated with autism spectrum disorder. If not, the existing L1 evidence base constitutes a strong foundation for an indication extension application.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Package insert warnings, contraindications, and drug-drug interaction data were flagged as data gaps (DG001, DG002) in this evidence pack. Before advancing to clinical planning, these must be retrieved directly from the NPRA official website and the corresponding package insert PDFs. Key areas to review include: neuroleptic malignant syndrome risk, tardive dyskinesia, impulse control disorders (a class-effect concern with D2 partial agonists), metabolic monitoring in pediatric populations, and use in elderly patients with dementia-related psychosis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aripiprazole has L1-level clinical evidence — including multiple completed Phase 3 double-blind RCTs and an FDA approval — for irritability associated with autism spectrum disorder in children aged 6–17. The mechanistic rationale is well-established, the pediatric safety profile is extensively characterized, and Asia-specific data (Japan post-marketing, n=528) further supports applicability to the Malaysian clinical context. The evidence base is sufficient to proceed; the remaining work is primarily regulatory and implementation-focused.

**Additional Supported Indications (Ranks 3–5):**
The evidence pack also identifies schizophrenia (Rank 3, L1) and bipolar disorder / manic bipolar affective disorder (Ranks 4–5, L1) as high-evidence predictions — both are globally established aripiprazole indications and likely already registered among the 26 Malaysia licenses.

**To proceed, the following is needed:**

- **Regulatory review**: Retrieve and verify the approved indication text for all 26 NPRA-registered aripiprazole products — confirm whether ASD irritability is currently approved or requires an indication extension
- **Safety data retrieval**: Download and parse package insert PDFs from the NPRA website to populate the key warnings and contraindication fields (Data Gap DG001)
- **MOA documentation**: Query the DrugBank API to formally document the mechanism of action for regulatory submissions (Data Gap DG002)
- **Pediatric risk management plan**: Develop monitoring protocols covering: body weight and BMI (at baseline, 4 weeks, 8 weeks, then quarterly), fasting glucose and lipid panel, extrapyramidal symptom assessment (e.g., AIMS scale), and sedation monitoring — all critical for the pediatric target population
- **Dose confirmation**: Confirm the pediatric dose range registered or to be registered in Malaysia (globally approved range: 2–15 mg/day for ASD irritability)
- **Asia-Pacific comparator review**: Cross-reference with Japanese and Taiwanese regulatory approvals for ASD irritability to support any Malaysia indication extension application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

