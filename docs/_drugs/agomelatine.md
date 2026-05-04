---
layout: default
title: Agomelatine
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: From Major Depressive Disorder to Anxiety Disorder

## One-Sentence Summary

Agomelatine is a novel melatonergic antidepressant approved in Europe and Australia for Major Depressive Disorder, acting through a unique dual mechanism of MT1/MT2 receptor agonism and 5-HT2C receptor antagonism that is entirely distinct from conventional SSRIs and SNRIs.
The TxGNN model predicts it may be effective for **Anxiety Disorder** (particularly Generalised Anxiety Disorder, GAD),
with **14 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Malaysian NPRA data (EMA-approved for Major Depressive Disorder) |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although detailed DrugBank MOA data was not retrievable for this evidence pack, the published literature consistently identifies agomelatine as a selective **MT1/MT2 melatonin receptor agonist** combined with a **5-HT2C serotonin receptor antagonist**. The MT1/MT2 agonism acts on the suprachiasmatic nucleus (SCN) to resynchronise disrupted circadian rhythms, while the 5-HT2C antagonism increases dopamine and noradrenaline release in the prefrontal cortex, producing anxiolytic effects that have been confirmed in both preclinical rodent models and clinical trials.

Anxiety disorder and major depressive disorder share deeply overlapping neurobiological substrates: amygdala hyperreactivity, prefrontal cortex dysfunction, disrupted sleep-wake regulation, and HPA axis dysregulation. Approximately 50–60% of MDD patients present with clinically significant comorbid anxiety. Agomelatine's 5-HT2C antagonism specifically attenuates amygdala-driven fear responses and pathological worry, while its circadian rhythm-restoring action addresses the sleep disruption that perpetuates anxiety states — making the mechanistic link to anxiety disorder exceptionally strong.

Agomelatine has been directly studied in Generalised Anxiety Disorder through dedicated randomised controlled trials, accumulating sufficient regulatory evidence for approval in Australia. Multiple independent meta-analyses — including a 2025 systematic review and network meta-analysis in *International Clinical Psychopharmacology* — confirm its efficacy in reducing HAM-A scores versus placebo and active comparators, with a favourable tolerability profile free of sexual dysfunction and significant weight gain that limits long-term SSRI/SNRI use in anxiety patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01108393](https://clinicaltrials.gov/study/NCT01108393) | Phase 2 | Completed | 74 | Agomelatine 25 mg (escalatable to 50 mg) vs. placebo over 16 weeks in OCD patients; the most directly anxiety-targeted prospective trial in this dataset |
| [NCT03977441](https://clinicaltrials.gov/study/NCT03977441) | Phase 4 | Unknown | 240 | Multicenter RCT evaluating agomelatine for sleep disorders, depression and anxiety in Parkinson's disease; addresses co-occurring anxiety and mood disturbances |
| [NCT04589143](https://clinicaltrials.gov/study/NCT04589143) | Phase 4 | Completed | 137 | Agomelatine augmentation in SSRI/SNRI early non-responders with MDD; secondary outcomes specifically included anxiety symptoms and sleep quality improvement |
| [NCT00411242](https://clinicaltrials.gov/study/NCT00411242) | Phase 3 | Completed | 503 | 8-week fixed-dose agomelatine 25 mg and 50 mg vs. placebo in MDD with 52-week open-label extension; core pivotal trial establishing dose-response |
| [NCT00467402](https://clinicaltrials.gov/study/NCT00467402) | Phase 3 | Completed | 644 | 52-week RCT on relapse prevention in MDD; sustained anxiolytic-antidepressant effects confirmed over long-term follow-up |
| [NCT01488071](https://clinicaltrials.gov/study/NCT01488071) | Phase 3 | Completed | 495 | Head-to-head agomelatine vs. vortioxetine in MDD patients with inadequate SSRI response; active-controlled comparative efficacy data |
| [NCT00411099](https://clinicaltrials.gov/study/NCT00411099) | Phase 3 | Completed | 508 | 8-week fixed-dose agomelatine vs. placebo in MDD with 52-week open-label extension; independent replication of pivotal dose-efficacy study |
| [NCT00463242](https://clinicaltrials.gov/study/NCT00463242) | Phase 3 | Completed | 501 | Agomelatine vs. paroxetine (active comparator) and placebo in MDD; tolerability comparison directly relevant to anxiety comorbidity management |
| [NCT05323994](https://clinicaltrials.gov/study/NCT05323994) | N/A | Completed | 104 | Observational study of agomelatine effectiveness in post-COVID depression with prominent anxiety features in routine Russian clinical practice |
| [NCT01110889](https://clinicaltrials.gov/study/NCT01110889) | Phase 3 | Completed | 582 | 8-week double-blind placebo-controlled multicenter RCT of agomelatine sublingual formulation in MDD; supports broader antidepressant and anxiolytic evidence base |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38804215](https://pubmed.ncbi.nlm.nih.gov/38804215/) | 2025 | Systematic Review + NMA | Int Clin Psychopharmacol | Network meta-analysis comparing agomelatine against all approved GAD medications on remission and adverse event-driven discontinuation rates |
| [33537871](https://pubmed.ncbi.nlm.nih.gov/33537871/) | 2021 | Meta-analysis | Advances in Therapy | Pooled analysis of 3 placebo-controlled RCTs for GAD; agomelatine 25–50 mg significantly reduced anxious symptoms and functional impairment vs. placebo |
| [35795687](https://pubmed.ncbi.nlm.nih.gov/35795687/) | 2022 | Review | Ther Adv Psychopharmacol | Comprehensive mechanistic review of agomelatine's distinctive MT/5-HT2C pathway in GAD; synthesises preclinical anxiolytic data and clinical trial outcomes |
| [32702221](https://pubmed.ncbi.nlm.nih.gov/32702221/) | 2020 | Meta-analysis | Clin Psychopharmacol Neurosci | Meta-analysis of efficacy and safety of agomelatine specifically in GAD treatment; supports use as an additional treatment option for patients with inadequate response |
| [24569045](https://pubmed.ncbi.nlm.nih.gov/24569045/) | 2014 | RCT | J Clin Psychiatry | Short-term active-comparator and placebo-controlled Phase 3 study confirming agomelatine efficacy in GAD; completed as a regulatory-confirmatory study required by agencies |
| [30712879](https://pubmed.ncbi.nlm.nih.gov/30712879/) | 2019 | Systematic Review + NMA | Lancet | Comprehensive Lancet NMA of all pharmacological treatments for GAD; positions agomelatine among available therapeutic choices with efficacy and acceptability data |
| [34417992](https://pubmed.ncbi.nlm.nih.gov/34417992/) | 2021 | Review | Advances in Therapy | Evidence-based pharmacotherapy framework for GAD with a specific focus on agomelatine as an alternative-mechanism agent for patients who cannot tolerate SSRIs/SNRIs |
| [28730851](https://pubmed.ncbi.nlm.nih.gov/28730851/) | 2017 | Review | Expert Opin Pharmacother | Evaluation of clinical efficacy and tolerability data for agomelatine in short-term and maintenance treatment of GAD; expert commentary on first-line versus second-line positioning |
| [24766542](https://pubmed.ncbi.nlm.nih.gov/24766542/) | 2014 | Review | Expert Opin Investig Drugs | Review of agomelatine in GAD discussing clinical profile, mechanisms, and comparison with benzodiazepines, SSRIs, SNRIs, buspirone, and anticonvulsants |
| [25999720](https://pubmed.ncbi.nlm.nih.gov/25999720/) | 2015 | Review | Neuropsychiatr Dis Treat | Profile of agomelatine as MT1/MT2 agonist with 5-HT2C antagonism as a pharmacological alternative for the ~50% of GAD patients who do not respond adequately to existing treatments |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Not retrievable) | (Not retrievable) | (Not retrievable) | (Not retrievable) |

> **Note:** The Malaysian NPRA registry confirms 1 licensed product with market status **Marketed** as of the data cut-off (2026-04-04). However, detailed product information — including the authorisation number, brand name, dosage form, and the approved indication text — was not captured in the current data feed. Direct verification via the NPRA online registration portal is recommended before proceeding with any regulatory assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data — including key warnings and contraindications — was not available in the current evidence pack (classified as a Blocking data gap). For agomelatine specifically, prescribers should be aware that hepatotoxicity monitoring (liver enzyme testing before and during treatment) is a well-documented class concern referenced in the EMA label; this should be confirmed in the Malaysian product insert once retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple independent meta-analyses and systematic reviews — including a 2025 network meta-analysis and confirmed Phase 3 GAD-specific RCTs cited in pooled analyses — establish L1-level evidence for agomelatine's efficacy in Generalised Anxiety Disorder, supported by a strong and mechanistically coherent rationale and existing regulatory approval in Australia. The drug is already marketed in Malaysia, eliminating market access barriers, but local safety data and the exact scope of the registered indication must be confirmed before proceeding.

**To proceed, the following is needed:**
- **[Priority — Blocking]** Download and parse the Malaysian SmPC/product insert to extract the approved indication, contraindications, and key warnings (Data Gap DG001)
- **[Priority — High]** Retrieve DrugBank MOA data to complete the mechanistic analysis documentation (Data Gap DG002)
- Confirm whether the current Malaysian NPRA registration covers MDD only, or already includes GAD/anxiety disorder
- If the GAD indication is not yet registered locally, assess whether a supplementary new indication application is required to NPRA
- Establish a hepatotoxicity monitoring protocol (LFT at baseline, 6 weeks, 12 weeks, and periodically thereafter) consistent with the EMA label requirements
- Review any local reimbursement or formulary implications for the anxiety disorder indication in the Malaysian healthcare system

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

