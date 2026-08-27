---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 5
---

# Insulin Human
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

# Insulin Human: From Diabetes Mellitus to Diabetic Ketoacidosis

## One-Sentence Summary

> Insulin Human is the foundational glucose-lowering therapy for diabetes mellitus, and TxGNN's top-ranked prediction for this drug is **Diabetic Ketoacidosis (DKA)** — a life-threatening acute complication of diabetes that insulin already treats as first-line, guideline-endorsed therapy.
> This should be read as a confirmatory signal reinforcing an already-approved use rather than a genuine repositioning into a new disease area.
> Evidence support is substantial in volume — **50 clinical trials** and **17 publications** were retrieved — though most trials study adjunctive interventions (fluids, closed-loop devices, other agents) rather than insulin itself as a novel variable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (insulin replacement therapy) — TFDA/NPRA label-specific indication text not captured in current data pull |
| Predicted New Indication | Diabetic Ketoacidosis (DKA) |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 22 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, DrugBank-sourced mechanism-of-action data is not available for Insulin Human in this evidence pack (flagged as a High-severity data gap). However, insulin's pharmacology is textbook-level established knowledge: it activates the insulin receptor (INSR)/PI3K-AKT signaling cascade, which suppresses lipolysis and ketogenesis, promotes peripheral GLUT4-mediated glucose uptake, and inhibits hepatic gluconeogenesis.

DKA is a medical emergency caused by absolute or relative insulin deficiency (classically in type 1 diabetes, but increasingly recognized in ketosis-prone type 2 diabetes). Because insulin corrects the exact metabolic defect underlying DKA — halting free fatty acid release and ketone production while normalizing glucose — it is already the cornerstone of every major DKA management guideline. The repurposing rationale supplied with this evidence pack states this directly: the mechanistic link is to insulin's **original, FDA/label-recognized mechanism**, not a cross-target repositioning.

**Important caveat for reviewers:** the TxGNN score for this candidate is 0.00%, and all five of the drug's top-ranked "predicted indications" (diabetic ketoacidosis, type 2 diabetes, type 1 diabetes, diabetes mellitus, and IDDM 1) are simply diabetes and its acute complication — i.e., insulin's own core disease category, not a novel indication outside its known label. This pattern suggests the prediction pipeline surfaced Insulin Human's existing indication space rather than a genuine drug-repurposing candidate, and should be flagged to the modeling team as a possible self-match artifact rather than advanced as a discovery.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06007508](https://clinicaltrials.gov/study/NCT06007508) | Phase 2 | Terminated | 8 | Early administration of insulin glargine in DKA; directly tests insulin timing in DKA but stopped early with small sample |
| [NCT04233034](https://clinicaltrials.gov/study/NCT04233034) | Phase 3 | Completed | 113 | Hybrid closed-loop therapy + verapamil for β-cell preservation in new-onset type 1 diabetes (CLVer); insulin is background therapy |
| [NCT01365793](https://clinicaltrials.gov/study/NCT01365793) | Phase 3 | Completed | 1,389 | Compared four IV fluid rehydration protocols for pediatric DKA and cerebral injury outcomes |
| [NCT04196140](https://clinicaltrials.gov/study/NCT04196140) | N/A | Completed | 240 | Omnipod Horizon automated glucose control system safety/effectiveness in type 1 diabetes |
| [NCT06541535](https://clinicaltrials.gov/study/NCT06541535) | Phase 4 | Not yet recruiting | 300 | Saline vs. Ringer Lactate fluid resuscitation in severe DKA, insulin therapy as background standard of care |
| [NCT07167693](https://clinicaltrials.gov/study/NCT07167693) | Phase 1/2 | Recruiting | 60 | Arginine hydrochloride to reduce DKA duration in ketosis-prone type 2 diabetes |
| [NCT00426413](https://clinicaltrials.gov/study/NCT00426413) | N/A | Completed | 44 | Ketosis-prone diabetes in African-Americans; insulin signaling, proteomics, and outcomes |
| [NCT06599203](https://clinicaltrials.gov/study/NCT06599203) | N/A | Not yet recruiting | 130 | Prognostic factors and treatment response monitoring in children with DKA |
| [NCT02130180](https://clinicaltrials.gov/study/NCT02130180) | N/A | Unknown | 108 | Optic nerve sheath ultrasound as a marker for cerebral edema in DKA |
| [NCT06032325](https://clinicaltrials.gov/study/NCT06032325) | N/A | Unknown | 48 | NGAL and KIM-1 as biomarkers of acute kidney injury in children with DKA |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36479786](https://pubmed.ncbi.nlm.nih.gov/36479786/) | 2023 | RCT | Diabetes, Obesity & Metabolism | Early insulin glargine + continuous IV insulin infusion improved DKA management outcomes vs. IV infusion alone |
| [28364357](https://pubmed.ncbi.nlm.nih.gov/28364357/) | 2017 | Review | Current Diabetes Reports | Comparative review of DKA/HHS treatment protocols between UK and USA |
| [34590174](https://pubmed.ncbi.nlm.nih.gov/34590174/) | 2021 | Review/Guideline | Diabetologia | ADA/EASD consensus report on management of type 1 diabetes in adults, including insulin therapy |
| [27097605](https://pubmed.ncbi.nlm.nih.gov/27097605/) | 2017 | Review | Current Diabetes Reviews | Review of euglycemic DKA, its causes including recent insulin use, and diagnostic criteria |
| [35389497](https://pubmed.ncbi.nlm.nih.gov/35389497/) | 2022 | Cohort | JAMA Network Open | Hospital-wide implementation of subcutaneous insulin protocol for DKA reduced ICU need |
| [31704689](https://pubmed.ncbi.nlm.nih.gov/31704689/) | 2020 | Retrospective Cohort | Diabetes Care | Clinical outcomes in isolated vs. combined DKA and hyperosmolar hyperglycemic state |
| [40407548](https://pubmed.ncbi.nlm.nih.gov/40407548/) | 2025 | Evidence Map | Medical Sciences (Basel) | Evidence and gap map identifying low-quality-evidence areas in DKA therapeutic management |
| [38444312](https://pubmed.ncbi.nlm.nih.gov/38444312/) | 2024 | Post-hoc Analysis | Diabetes Technology & Therapeutics | DKA at type 1 diabetes onset and long-term glycemic outcomes with closed-loop insulin delivery |
| [26086329](https://pubmed.ncbi.nlm.nih.gov/26086329/) | 2015 | Review | Journal of Clinical Endocrinology & Metabolism | SGLT2 inhibitors may predispose to ketoacidosis; FDA warning context relevant to insulin co-therapy |
| [28003053](https://pubmed.ncbi.nlm.nih.gov/28003053/) | 2016 | Clinical Review | Clinical Therapeutics | SGLT2 inhibitor-associated DKA: prevention and diagnosis recommendations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The clinical trial and literature volume (50 trials, 17 publications) confirms insulin's well-established, guideline-level role in DKA management — but this is validation of an existing, already-approved use rather than a novel repurposing discovery, since DKA and the other top TxGNN-ranked "predicted indications" all fall within insulin's own known diabetes indication space.
- Two blocking/high-severity data gaps remain: TFDA/NPRA package-insert warnings and contraindications (blocking safety review), and a formally sourced mechanism-of-action record (high priority for mechanistic documentation).

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — required before any S1 safety assessment can proceed
- DrugBank-sourced mechanism-of-action confirmation
- Malaysia-specific license/product register details (license number, product name, dosage form, approved indication text), which were not populated in this data pull despite 22 total registrations on file
- A pipeline-level review of whether a drug's own core indication category should be excluded from its "repurposing candidate" outputs, to avoid self-match artifacts like this one recurring across other TxGNN candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

