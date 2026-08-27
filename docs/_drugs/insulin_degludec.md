---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Insulin Degludec: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Insulin degludec is a marketed ultra-long-acting basal insulin analogue used for diabetes mellitus management.
> The TxGNN model's top prediction is **Type 1 Diabetes Mellitus**, supported by **50 clinical trials** and **20 publications** —
> however, this is not a novel repurposing signal but a confirmation of the drug's existing approved use, since insulin replacement is the drug's core mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (exact NPRA-approved indication text was not captured in the source registry data; original_indications field is empty) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data was not available for this candidate (`original_moa` = Data Gap in the source pack), but the evidence pack's own repurposing rationale supplies the relevant pharmacology: insulin degludec is an **ultra-long-acting basal insulin analogue** that works by directly replacing endogenous insulin to control blood glucose. This is a class-level mechanism shared by all basal insulin products.

Importantly, the evidence pack itself flags that this "prediction" is not a genuine old-drug-new-use signal. Type 1 diabetes mellitus is insulin degludec's core, already-approved on-label indication — the drug exists specifically to treat insulin-deficient states, of which T1DM is the prototypical example. The very high TxGNN score (99.44%) and the volume of Phase 3 evidence therefore reflect **real, well-established pharmacology rather than a newly discovered therapeutic link**. In other words, TxGNN has correctly reconstructed known drug-disease pharmacology, which is a useful validation of the model's accuracy but not an actionable repurposing opportunity in the traditional sense.

For contrast, among the other TxGNN-ranked candidates for this drug, most (autoimmune oophoritis, opsismodysplasia, focal stiff limb syndrome, classic stiff person syndrome) are rated L5/Hold with no supporting evidence — likely knowledge-graph co-occurrence artifacts (e.g., shared autoimmune/GAD65 biology with T1DM) rather than treatable mechanistic links. One candidate, thiamine-responsive dysfunction syndrome (TRMA), is rated L4/Research Question, reflecting a plausible indirect rationale: TRMA's diabetes component often requires insulin therapy as a comorbid treatment, not a primary cure.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN™ Young 1: multinational RCT of insulin degludec vs. insulin detemir in children/adolescents with T1DM on basal-bolus regimen |
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2: double-blind crossover trial comparing degludec vs. glargine safety/efficacy |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | Completed | 834 | Faster-acting insulin aspart vs. NovoRapid, both combined with degludec, in children/adolescents with T1DM |
| [NCT01773798](https://clinicaltrials.gov/study/NCT01773798) | Phase 1 | Completed | 33 | PK/PD characterization of insulin degludec/aspart 15 in T1DM subjects |
| [NCT03938740](https://clinicaltrials.gov/study/NCT03938740) | Phase 2 | Completed | 61 | Exploratory comparison of insulin dosing algorithms (HDV-lispro vs. degludec) for optimum basal dosing in T1DM |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A | Completed | 1262 | Non-interventional real-world safety/effectiveness study of degludec (Tresiba®) in T1DM and T2DM |
| [NCT01984372](https://clinicaltrials.gov/study/NCT01984372) | N/A | Completed | 6163 | Large-scale post-marketing surveillance of long-term Tresiba® safety/effectiveness in insulin-requiring diabetes |
| [NCT00982228](https://clinicaltrials.gov/study/NCT00982228) | Phase 3 | Completed | 629 | BEGIN™: BB T1 LONG — degludec vs. glargine, both with insulin aspart, in T1DM (with long-term extension) |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | Completed | 258 | BEYOND: durability of glycemic control with basal insulin/GLP-1RA or SGLT-2i combinations vs. basal-bolus regimen |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | Completed | 153 | Head-to-head comparison of investigational GZR101 vs. insulin degludec/aspart |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily degludec in basal-bolus regimen for T1DM |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs. detemir (both + aspart) non-inferiority trial in pregnant women with T1DM |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: once-weekly insulin efsitora alfa vs. once-daily degludec, non-inferiority trial in T1DM adults |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Management of T1DM in pregnancy, including basal insulin strategy and technology updates |
| [36106652](https://pubmed.ncbi.nlm.nih.gov/36106652/) | 2023 | Review | Diabetes Obes Metab | Rationale/design of the ONWARDS 1-6 phase 3a program for once-weekly insulin icodec vs. degludec comparators |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Review | Clin Therap | Systematic review/meta-analysis: efficacy and tolerability of degludec vs. other long-acting basal insulins in T1D/T2D |
| [38679838](https://pubmed.ncbi.nlm.nih.gov/38679838/) | 2024 | Review | Diabetes Obes Metab | Design/rationale of the QWINT phase 3 program for once-weekly insulin efsitora alfa |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Review | Endocrinol Nutr | Degludec as ultra-long-acting basal insulin: advances in clinical research for T1D/T2D |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vasc Health Risk Manag | Insulin degludec/aspart combination for treatment of T1D and T2D |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Current status of degludec in T1D and T2D based on randomized and observational trials |

---

## Malaysia Market Information

Insulin degludec holds **5 active registrations** with NPRA and is currently marketed (已上市) in Malaysia. Detailed license numbers, product names, dosage forms, and approved-indication text were not captured in this evidence pack (all license record fields returned empty), so a per-license table cannot be produced from the available data.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack; DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is extremely strong (L1: multiple completed Phase 3 RCTs, including large trials like SWITCH 2 and BEGIN™ Young 1), but it supports insulin degludec's **existing, already-approved use** in type 1 diabetes rather than a new indication — this is model validation, not a repurposing discovery. The "guardrail" here is regulatory/administrative: confirming the drug's Malaysia-registered label already covers T1DM, not generating new clinical evidence.

**To proceed, the following is needed:**
- NPRA license detail (indication text, product names, dosage forms) to confirm T1DM is already on-label in Malaysia
- Package insert data for warnings, contraindications, and drug interactions (currently unavailable)
- Formal confirmation of drug MOA from DrugBank/product labeling
- If genuine repurposing candidates are of interest, the thiamine-responsive dysfunction syndrome (TRMA) candidate (L4, Research Question) warrants a literature-based mechanistic review, while the remaining candidates (autoimmune oophoritis, opsismodysplasia, focal/classic stiff person syndrome) currently lack any supporting evidence and should remain on Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

