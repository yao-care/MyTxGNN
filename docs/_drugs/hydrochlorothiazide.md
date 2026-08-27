---
layout: default
title: Hydrochlorothiazide
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 5
---

# Hydrochlorothiazide
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

# Hydrochlorothiazide: From Hypertension to Congestive Heart Failure

## One-Sentence Summary

Hydrochlorothiazide (HCTZ) is a thiazide diuretic long used for hypertension and fluid retention. Within this evidence pack, the only candidate indication with a completed evidence review is **Congestive Heart Failure** — specifically as an add-on to loop diuretics for diuretic-resistant decompensated heart failure — supported by **1 completed Phase 3 RCT (CLOROTIC trial, n=232)** and **8 relevant publications**, including a 2025 post-hoc analysis. (Note: the other four candidates returned by TxGNN — "hypertension" / "hypertensive disorder" — largely restate HCTZ's already-known original use and carry no completed scoring, so they are not treated as genuine repurposing signals here.)

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and edema (thiazide diuretic — official NPRA label indication text was not returned in this dataset) |
| Predicted New Indication | Congestive Heart Failure (as loop-diuretic adjunct in diuretic resistance) |
| TxGNN Prediction Score | 0.00% (score field returned 0.0 for all candidates in this data pull — likely a pipeline/data-quality issue, not a true confidence score) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 61 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, hydrochlorothiazide is a thiazide-type diuretic that inhibits the Na⁺/Cl⁻ cotransporter in the distal convoluted tubule, reducing sodium and water reabsorption and lowering circulating volume — the basis for its established efficacy in hypertension.

Heart failure and hypertension share overlapping pathophysiology (volume overload and RAAS activation), and thiazides already have a recognized secondary role in HF management: when loop diuretics (e.g., furosemide) are used long-term, the distal nephron compensates with increased sodium reabsorption ("distal nephron rebound"), producing diuretic resistance. Adding HCTZ blocks this compensatory pathway, producing **sequential nephron blockade** and restoring diuretic response. This mechanism is directly supported by the CLOROTIC trial, giving the prediction a plausible and clinically-grounded rationale — though it should be understood as a **specific adjunct-therapy niche** (diuretic-resistant acute decompensated HF) rather than a broad new primary indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01647932](https://clinicaltrials.gov/study/NCT01647932) | Phase 3 | Completed | 232 | CLOROTIC trial: RCT directly testing loop diuretic + thiazide (HCTZ) vs. loop diuretic alone in decompensated heart failure; graded "A" relevance — the pivotal trial for this indication |
| [NCT00690521](https://clinicaltrials.gov/study/NCT00690521) | NA | Completed | 8 | Compared HCTZ vs. metolazone, both combined with furosemide, for diuresis in congestive heart failure patients |
| [NCT03006796](https://clinicaltrials.gov/study/NCT03006796) | N/A | Completed | 94 | Observational study of azilsartan/chlorthalidone vs. irbesartan/HCTZ in hypertension with obesity; HCTZ present as comparator-arm component (graded "B") |
| [NCT03553810](https://clinicaltrials.gov/study/NCT03553810) | Phase 2 | Completed | 80 | ARNi effect on ventricular remodeling in hypertensive LVH — population is pre-HF hypertrophy rather than HF itself (graded "C") |
| [NCT04465123](https://clinicaltrials.gov/study/NCT04465123) | Phase 3 | Unknown | 100 | Furosemide + sequential nephron blockade (thiazide/spironolactone class) vs. furosemide alone in diuretic-resistant acute HF (graded "C" — HCTZ not confirmed as the specific agent used) |
| [NCT06273397](https://clinicaltrials.gov/study/NCT06273397) | NA | Not yet recruiting | 1050 | Acetazolamide or metolazone in acute heart failure — related mechanism class, not a direct HCTZ trial (graded "C") |
| [NCT02185417](https://clinicaltrials.gov/study/NCT02185417) | Phase 3 | Completed | 20,723 | VA Diuretic Comparison Project: chlorthalidone vs. HCTZ for cardiovascular outcomes in older hypertensive patients (large-scale background safety/effectiveness data) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36423214](https://pubmed.ncbi.nlm.nih.gov/36423214/) | 2023 | RCT (CLOROTIC trial) | European Heart Journal | Adding HCTZ to IV furosemide safely improves diuretic response in acute heart failure |
| [40856000](https://pubmed.ncbi.nlm.nih.gov/40856000/) | 2025 | RCT post-hoc analysis | European Journal of Heart Failure | Post-hoc analysis of CLOROTIC: HCTZ improves weight loss/decongestion even in patients with diuretic resistance |
| [38645830](https://pubmed.ncbi.nlm.nih.gov/38645830/) | 2024 | RCT insights/review | Cardiology Research | Reviews recent RCTs on upfront acetazolamide and HCTZ combined with loop diuretics in acute decompensated HF |
| [38204501](https://pubmed.ncbi.nlm.nih.gov/38204501/) | 2024 | Narrative Review | The Canadian Journal of Hospital Pharmacy | Reviews diuretic strategies, including thiazide add-on, for acute decompensated heart failure |
| [21896142](https://pubmed.ncbi.nlm.nih.gov/21896142/) | 2011 | Review | Journal of Clinical Hypertension | Pharmacokinetic/pharmacodynamic comparison of thiazide and loop diuretics relevant to combination use |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC: Heart Failure | Describes the pathophysiological transition from hypertension to heart failure, supporting mechanistic overlap |
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review (guideline update) | ESC Heart Failure | 2024 update on heart failure management |
| [6761370](https://pubmed.ncbi.nlm.nih.gov/6761370/) | 1982 | Controlled trial | Journal of Clinical Pharmacology | Early controlled trial of slow-release furosemide plus HCTZ in congestive cardiac failure |

## Malaysia Market Information

Individual authorization-level details (license numbers, product names, dosage forms, approved indication text) were not returned in this dataset — all 5 sampled license records had blank fields. NPRA records confirm **61 total registrations** and an overall market status of **✓ Marketed**, but product-level verification requires a direct NPRA database query.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were all flagged as data gaps in this evidence pack (DG001, severity: Blocking) — this is the primary reason a full safety assessment (S1) cannot currently be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale and clinical evidence (CLOROTIC trial, L2) support HCTZ as an adjunct in diuretic-resistant decompensated heart failure, but this is a narrow, already partially-recognized clinical niche rather than a novel repurposing opportunity — and a **Blocking**-severity data gap (missing NPRA label warnings/contraindications) prevents completion of the mandatory S1 safety screen.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (resolves DG001, blocking)
- Confirmed mechanism of action documentation (resolves DG002)
- Drug interaction data specific to combination diuretic use (loop diuretics, potassium-sparing agents) in HF populations
- Clarification of the TxGNN scoring pipeline, since all five candidate indications returned a 0.0 score
- Product-level NPRA registration data (license numbers, approved indication text) to confirm current Malaysia labeling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

