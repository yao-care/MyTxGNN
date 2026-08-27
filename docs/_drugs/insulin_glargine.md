---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 5
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Diabetic Ketoacidosis

## One-Sentence Summary

Insulin Glargine (DrugBank DB00047) is a long-acting basal insulin analogue approved for the management of Type 1 and Type 2 diabetes mellitus. The TxGNN model predicts it may also be effective for **Diabetic Ketoacidosis (DKA)** — specifically as an early adjunct to standard IV insulin therapy — with **26 clinical trials** and **20 publications** currently addressing this use, though most individual studies are small or terminated.

*Note: The evidence pack returned four additional "predicted" indications (Type 2 DM, Type 1 DM, diabetes mellitus, IDDM 1) that the source data itself flags as data-pipeline errors — these are the drug's existing approved indications, not novel repurposing candidates, and are excluded from this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1 and Type 2) — basal insulin replacement therapy |
| Predicted New Indication | Diabetic Ketoacidosis (DKA) |
| TxGNN Prediction Score | 0.00% (raw score field returned 0.0 — likely a data-pipeline gap, not a true model confidence value) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity data gap). Based on known pharmacology, insulin glargine is a long-acting basal insulin analogue; its efficacy in diabetes mellitus is well established, and its blood-glucose-lowering and lipolysis-suppressing effects mechanistically extend to DKA management.

Diabetic ketoacidosis is fundamentally an insulin-deficiency crisis: hyperglycemia and unchecked free-fatty-acid release drive ketone body formation and acidosis. Because insulin glargine's core action — correcting hyperglycemia and inhibiting free fatty acid release — is identical to its original indication, this is not a novel mechanistic hypothesis but a **same-mechanism extension of use**: adding early long-acting basal insulin to standard short-acting IV insulin during the acute phase of DKA, rather than waiting until acidosis resolves to start subcutaneous transition therapy. This gives the prediction high biological plausibility, and is directly reflected in a two-decade string of clinical trials testing exactly this strategy (e.g., NCT00179127, 2004–2012; NCT02548494, 2015–2019; NCT06007508, 2022–2023).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930044](https://clinicaltrials.gov/study/NCT02930044) | NA | Completed | 18 | Early SC glargine + standard of care vs. standard of care alone in ED patients with DKA; assessed duration of IV insulin infusion |
| [NCT05219942](https://clinicaltrials.gov/study/NCT05219942) | NA | Unknown | 52 | Long-acting glargine + low-dose regular insulin infusion vs. infusion alone in DKA patients with renal impairment |
| [NCT06007508](https://clinicaltrials.gov/study/NCT06007508) | Phase 2 | Terminated | 8 | Early administration of glargine in DKA; small terminated trial, insufficient statistical power |
| [NCT00179127](https://clinicaltrials.gov/study/NCT00179127) | NA | Completed | 75 | Early glargine addition during moderate-to-severe pediatric DKA to accelerate acidosis correction and reduce ICU time |
| [NCT00732524](https://clinicaltrials.gov/study/NCT00732524) | Phase 4 | Completed | 80 | Sulfonylurea + glargine as ED discharge therapy to prevent impending DKA in unstable Type 2 diabetes |
| [NCT00590044](https://clinicaltrials.gov/study/NCT00590044) | Phase 4 | Completed | 74 | Multicenter RCT comparing insulin analogs vs. human insulins during IV-to-SC transition in DKA |
| [NCT03107208](https://clinicaltrials.gov/study/NCT03107208) | Phase 4 | Completed | 61 | Early glargine vs. glargine after full DKA resolution in children; assessed prevention of rebound hyperglycemia |
| [NCT02006342](https://clinicaltrials.gov/study/NCT02006342) | NA | Completed | 40 | Pilot study: SC glargine + IV insulin vs. IV insulin alone on time to anion-gap closure and ICU admission in ED DKA |
| [NCT04567225](https://clinicaltrials.gov/study/NCT04567225) | Phase 4 | Terminated | 39 | Early basal insulin administration in adult DKA management |
| [NCT02548494](https://clinicaltrials.gov/study/NCT02548494) | NA | Terminated | 17 | Double-blind RCT of early long-acting glargine during pediatric Type 1 DKA management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27861474](https://pubmed.ncbi.nlm.nih.gov/27861474/) | 2016 | Systematic Review + Meta-analysis | Gaceta médica de México | SC glargine coadministration from onset of DKA management may reduce rebound hyperglycemia and improve time to resolution vs. IV insulin alone |
| [41208563](https://pubmed.ncbi.nlm.nih.gov/41208563/) | 2026 | Systematic Review + Meta-analysis (RCTs) | Diabetes, Obesity & Metabolism | Evaluates effectiveness/safety of early SC basal insulin + IV infusion vs. IV infusion alone for DKA |
| [41296041](https://pubmed.ncbi.nlm.nih.gov/41296041/) | 2025 | GRADE Systematic Review + Meta-analysis | European Journal of Pediatrics | Early vs. late initiation of long-acting basal insulin during IV insulin in pediatric DKA (PROSPERO-registered) |
| [40840711](https://pubmed.ncbi.nlm.nih.gov/40840711/) | 2025 | Randomized Clinical Trial | Endocrine Practice | Early glargine U100 vs. U300 alongside IV insulin in adult T1DM DKA management |
| [40623843](https://pubmed.ncbi.nlm.nih.gov/40623843/) | 2025 | Double-blind RCT | Archives of Disease in Childhood | Early glargine supplementation during acute pediatric DKA management — efficacy and safety |
| [33655870](https://pubmed.ncbi.nlm.nih.gov/33655870/) | 2021 | RCT/Cohort | Current Diabetes Reviews | Early glargine use in DKA was safe and associated with a trend toward faster resolution |
| [37139251](https://pubmed.ncbi.nlm.nih.gov/37139251/) | 2023 | Cohort (pediatric evaluation) | J Pediatr Pharmacol Ther | Early SC glargine may accelerate ketoacidosis resolution in pediatric DKA vs. standard-timing administration |
| [36479786](https://pubmed.ncbi.nlm.nih.gov/36479786/) | 2023 | RCT (Cohort effectiveness/safety) | Diabetes, Obesity & Metabolism | Early glargine + continuous IV insulin infusion vs. IV infusion alone in DKA management |
| [39308229](https://pubmed.ncbi.nlm.nih.gov/39308229/) | 2025 | Cohort (operational effectiveness) | Academic Emergency Medicine | SQuID II protocol expands SC insulin DKA management to sicker patients on regular medical floors |
| [39054791](https://pubmed.ncbi.nlm.nih.gov/39054791/) | 2025 | Review | Annals of Pharmacotherapy | Summarizes studies on SC insulin regimens (including glargine) for DKA management in adults and pediatrics |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The repurposing hypothesis has high mechanistic plausibility (same drug, same glucose/ketone-lowering action, extended to earlier use in the same disease continuum), and is backed by one systematic review + meta-analysis plus multiple RCTs/cohorts spanning two decades. However, individual trials are consistently small (n=8–80), several were terminated early, and no single large confirmatory Phase 3 RCT exists — hence L2 rather than L1 evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, precautions, and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Detailed mechanism of action documentation from DrugBank (currently a High-severity data gap)
- A larger, adequately powered confirmatory RCT specifically in the DKA population (existing trials are underpowered or terminated)
- Malaysia-specific regulatory review of whether early basal insulin use in DKA falls within, or requires an extension of, the current approved label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

