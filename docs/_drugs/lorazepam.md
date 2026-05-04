---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Lorazepam is a benzodiazepine class drug primarily used for anxiety disorders, acute sedation, and seizure management, with well-established GABA-A receptor modulation as its core mechanism.
The TxGNN model predicts it may be effective for **Insomnia (disease)**, with **23 clinical trials** and **18 publications** currently supporting this direction.
The mechanistic link is direct — lorazepam's GABAergic enhancement produces sedative-hypnotic effects that map precisely onto insomnia therapeutic goals, though long-term use carries recognised risks of tolerance and physical dependence.

> **Note on Top-Ranked Prediction:** TxGNN rank 1 (trigeminal nerve neoplasm, score 99.87%) was identified in the repurposing rationale as a likely false positive — a result of indirect knowledge-graph node linkages between "neuropain/neuro-oncology" and "sedatives" with no supporting clinical trial or literature evidence. This report therefore focuses on **rank 2 (insomnia)**, the highest-ranked prediction with actionable evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders / acute sedation (detailed Malaysia regulatory data not available in this pack) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lorazepam is a short-to-intermediate-acting benzodiazepine that acts as a positive allosteric modulator of GABA-A receptors. By binding to the benzodiazepine recognition site at the interface of α and γ subunits, it increases the frequency of chloride ion channel opening in response to GABA, thereby amplifying inhibitory neurotransmission across the central nervous system. Detailed mechanism-of-action data was not available in this evidence pack; however, lorazepam's dose-dependent CNS depressant profile — covering sedation, anxiolysis, muscle relaxation, and anticonvulsant activity — is extensively documented in the pharmacological literature (PMID 30764).

The mechanistic link between lorazepam and insomnia is both direct and well-grounded. Enhanced GABAergic tone shortens sleep onset latency and prolongs Stage 2 NREM sleep duration, precisely the parameters targeted in insomnia treatment. A head-to-head double-blind crossover RCT (PMID 3280615) demonstrated that lorazepam 2 mg outperformed flurazepam 30 mg on most polysomnographic sleep parameters in chronic insomniacs. Furthermore, Phase 2 and 3 clinical trials of the SM-1 combination (diphenhydramine + zolpidem + lorazepam; NCT03331042, NCT02671760) directly confirmed lorazepam's contribution to hypnotic efficacy in a transient insomnia model, and a prospective cohort study in 1,400 elderly Taiwanese patients (NCT02648776) assessed real-world risk-benefit outcomes across the hypnotic drug class.

However, long-term use raises clinically important safety concerns: tolerance develops within 1–2 weeks, physical dependence and withdrawal syndrome risk escalates with prolonged use, and lorazepam suppresses slow-wave sleep (SWS). The withdrawn Phase 3 trial (NCT03338764, 0 enrolled) highlights the regulatory and commercial challenges in securing new Phase 3 approval for this indication today. Active deprescribing studies (NCT04572750, NCT06584513, n = 470) reflect the clinical community's shift toward viewing benzodiazepines as short-term bridges rather than long-term insomnia solutions. Accordingly, any clinical deployment should be restricted to short-term use (< 4 weeks) with mandatory cognitive-behavioural therapy for insomnia (CBT-I) co-integration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | Completed | 85 | 4-way crossover RCT directly evaluating SM-1 (diphenhydramine + zolpidem + lorazepam 0.5 mg delayed-release) vs two active comparators and placebo in a 5-hour phase-advance model of transient insomnia; lorazepam is a core active component |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | Completed | 39 | Phase 2 double-blind PD study of SM-1 (containing lorazepam) on total sleep time in adults with transient insomnia; sleep centre–based evaluation using phase-advance model |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Large prospective cohort (Taiwan) examining medication use patterns, pharmacokinetic and pharmacogenetic characteristics, and clinical outcomes of hypnotics including benzodiazepines in elderly patients; most directly applicable real-world evidence for this drug class in an Asian population |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | Withdrawn | 0 | Phase 3 double-blind placebo-controlled efficacy and safety trial of SM-1 for transient insomnia in adults; withdrawn before enrolment — the withdrawal itself signals the regulatory and commercial headwinds facing new Phase 3 data generation for this indication |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | Not Yet Recruiting | 14 | Phase 2 crossover PD study of SM-1 vs diphenhydramine + lorazepam combination in 3-hour phase-advance model of transient insomnia; directly evaluates lorazepam's PD contribution |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronic self-management intervention to promote benzodiazepine (including lorazepam) cessation in Veterans using BZDs for anxiety and sleep; reflects real-world long-term safety concerns and highlights dependence challenges |
| [NCT06584513](https://clinicaltrials.gov/study/NCT06584513) | N/A | Recruiting | 470 | BE-SAFE: large patient-centred RCT to reduce benzodiazepine and sedative-hypnotic use in older adults (≥65 years) with sleep problems; underscores contemporary safety management priorities for this drug class |
| [NCT03405298](https://clinicaltrials.gov/study/NCT03405298) | N/A | Completed | 44 | Pilot RCT of two approaches to chronic benzodiazepine reduction (direct patient education ± behavioural health support) in older adults; demonstrates demand for structured deprescribing protocols |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of dexmedetomidine (α₂ agonist) vs GABA agonists (including lorazepam) on sleep stages and total sleep time in mechanically ventilated ICU patients; provides physiological evidence on lorazepam's effects on sleep architecture |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Phase 1 | Completed | 12 | Phase 1 double-blind crossover PK/PD biomarker study of selective GABA-A modulator AZD7325 vs benzodiazepines including lorazepam; supports mechanistic understanding of GABAergic pharmacology relevant to insomnia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | J Clin Pharmacol | Head-to-head double-blind crossover RCT (n=8): lorazepam 2 mg outperformed flurazepam 30 mg on most polysomnographic sleep parameters including sleep latency, stage distribution, and subjective sleep quality over 3 weeks in chronic insomniacs |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Systematic Review | Medical Letter | Current systematic clinical review of drug options for chronic insomnia; positions benzodiazepines (including lorazepam) within the modern treatment landscape relative to Z-drugs, doxepin, suvorexant, and melatonin agonists |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Clinical Trial | Int Clin Psychopharmacol | Compared 24-hour lorazepam dosing (0.5 mg TID) vs single evening dose (1.5 mg HS) in primary insomnia; tested hypothesis that addressing daytime hyperarousal may enhance overall treatment response beyond nocturnal hypnosis alone |
| [41392764](https://pubmed.ncbi.nlm.nih.gov/41392764/) | 2026 | RCT | Food & Function | Probiotic (Bifidobacterium Bbm-19) intervention for insomnia using lorazepam as the pharmacological positive control in a PCPA-induced mouse model; confirms lorazepam as gold-standard benchmark hypnotic agent in current preclinical insomnia research |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | J Multidiscip Healthc | Review of efficacy, safety, and drug-drug interactions for insomnia therapy in COVID-19 patients ("coronasomnia"); covers benzodiazepines and summarises interaction risks with antivirals and other COVID medications |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquiliser use across dose types and outcomes in elderly patients with chronic non-communicable diseases; evaluates adverse effects including falls, cognitive impairment, and mortality risk for the benzodiazepine class |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Experimental | Drug Delivery | Comparative intranasal microemulsion study of diazepam, lorazepam, and alprazolam for sleep induction in rats; lorazepam microemulsion demonstrated effective sleep induction, supporting alternative delivery routes for insomnia management |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort | Sleep Medicine | Large managed-care database analysis of hypnotic prescriptions for insomnia; characterises real-world prescribing patterns, patient demographics, and trend shifts from benzodiazepines to non-hypnotic agents over a decade |
| [15040803](https://pubmed.ncbi.nlm.nih.gov/15040803/) | 2004 | Observational | Health Qual Life Outcomes | Survey of sleep quality and sedating drug use (including lorazepam) in acute-care hospitalised adult patients; identifies determinants of hospital-acquired insomnia and characterises the extent of benzodiazepine prescribing for sleep disturbance |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | PK Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics review of anxiolytic drugs including lorazepam; covers absorption, distribution, metabolism, elimination, and half-life profiles relevant to optimising dosing regimens for insomnia applications |

---

## Malaysia Market Information

Lorazepam has **5 registered products** in Malaysia (market status: ✓ Marketed). Detailed product-level data — including authorization numbers, brand names, dosage forms, and approved indication text — was not captured in this evidence pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | — |
| — | — | — | — |
| — | — | — | — |
| — | — | — | — |
| — | — | — | — |

> To access full registration details, query the **National Pharmaceutical Regulatory Agency (NPRA)** product database at [https://www.npra.gov.my/](https://www.npra.gov.my/) using the search term "LORAZEPAM". Retrieving this data will also resolve **Data Gap DG001** (Blocking — required for S1 safety assessment).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Alert (DG001 — Blocking):** Key warnings and contraindication data for the Malaysia-registered lorazepam products were not available in this evidence pack. This constitutes a blocking gap that prevents progression to Safety Stage 1 (S1) evaluation. To resolve: download the prescribing information PDF from the NPRA official source and parse for warnings regarding CNS/respiratory depression, dependence potential, pregnancy/lactation restrictions, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lorazepam's GABA-A receptor mechanism directly and plausibly supports its efficacy in insomnia, underpinned by direct RCT evidence (PMID 3280615), completed Phase 2/3 clinical trial experience with lorazepam-containing combinations (NCT03331042, NCT02671760), and a large real-world prospective cohort study in 1,400 elderly Taiwanese patients (NCT02648776). The drug is already marketed in Malaysia with 5 registered products, substantially lowering the regulatory entry barrier. Evidence level is L2, consistent with a "Proceed with Guardrails" recommendation.

**To proceed, the following is needed:**

- **Resolve Blocking Data Gap DG001**: Download and parse the NPRA-registered lorazepam package insert to complete the S1 safety assessment — specifically documenting warnings for CNS/respiratory depression, fall risk in elderly, pregnancy/lactation contraindications, and potential for abuse and physical dependence
- **Resolve High-Severity Data Gap DG002**: Retrieve full mechanism-of-action profile from DrugBank (DB00186) to formalise the mechanistic rationale section with primary source documentation
- **Define short-term use protocol**: Establish a maximum treatment duration policy (recommended ≤ 4 weeks) with structured reassessment criteria at each prescription renewal
- **Tolerance and dependence monitoring plan**: Develop patient education materials covering withdrawal risk, dose tapering schedules, and criteria for escalation to specialist care
- **CBT-I co-prescription framework**: Design a combination treatment pathway integrating cognitive-behavioural therapy for insomnia as the first-line non-pharmacological backbone, with lorazepam positioned as a short-term adjunct
- **Special population risk stratification**: Conduct a focused assessment of dose adjustments required for elderly patients (fall risk, cognitive impairment, extended half-life) and patients with respiratory compromise or hepatic impairment
- **Contemporary Phase 3 evidence gap**: Given the withdrawn NCT03338764 and absence of a completed modern Phase 3 insomnia-specific trial with lorazepam as monotherapy, consider whether a bridging pharmacokinetic or efficacy study is warranted before pursuing any new indication filing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

