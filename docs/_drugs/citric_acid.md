---
layout: default
title: Citric Acid
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 8
---

# Citric Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Citric Acid: From Multi-Purpose Excipient Use to Stomach Disease

## One-Sentence Summary

Citric acid (DrugBank DB04272) is a weak organic acid used broadly across pharmaceutical formulations as an excipient, acidulant, and mineral-supplement component; no single original therapeutic indication is recorded in this evidence pack. The TxGNN model predicts it may be effective for **Stomach Disease**, with **29 clinical trials** and **20 publications** retrieved during the search — but on review, none of these directly test citric acid as a treatment for the condition, and the supporting evidence remains largely indirect (metabolomic/mechanistic).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack — citric acid is generally used as a pharmaceutical excipient/acidulant rather than for a defined indication (all NPRA license indication fields returned empty) |
| Predicted New Indication | Stomach Disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 27 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA: Data Gap). Citric acid is an endogenous intermediate of the tricarboxylic acid (TCA) cycle and is widely used pharmaceutically as an acidifying agent, chelator, and excipient (e.g., in calcium/magnesium citrate salts, effervescent formulations, and as a flavor/taste-masking agent). No established pharmacological mechanism links it to direct treatment of gastrointestinal disease.

Reviewing the retrieved evidence, citric acid's appearances in the "stomach disease" literature are mostly as a **diagnostic reagent** (e.g., citric acid test meals used to improve accuracy of the ¹³C-urea breath test for *H. pylori*) or as a **natural constituent of gastric juice**, rather than as a therapeutic intervention. Of the 29 retrieved clinical trials, none use citric acid itself as the investigational treatment for stomach disease — several instead study *calcium citrate* (a different compound/salt form) for hypoparathyroidism or post-gastric-bypass calcium supplementation, which is mechanistically distinct.

The high TxGNN score most likely reflects strong co-occurrence of citric acid with gastrointestinal-related metabolites and conditions within the knowledge graph (a statistical/embedding association), rather than a validated pharmacological or clinical signal. This should be treated as a hypothesis-generating prediction only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03812380](https://clinicaltrials.gov/study/NCT03812380) | Phase 3 | Terminated | 62 | Effervescent calcium magnesium citrate studied to avert PPI-related complications (fracture, hypomagnesemia, CKD) — tests a citrate salt combination, not citric acid alone |
| [NCT03425747](https://clinicaltrials.gov/study/NCT03425747) | Phase 4 | Completed | 26 | Calcium citrate vs calcium carbonate for chronic hypoparathyroidism — compares calcium salt forms, not citric acid's GI effect |
| [NCT02830789](https://clinicaltrials.gov/study/NCT02830789) | N/A | Completed | 38 | Calcium citrate vs calcium carbonate for secondary hyperparathyroidism after Roux-en-Y gastric bypass |
| [NCT04095975](https://clinicaltrials.gov/study/NCT04095975) | Phase 4 | Completed | 31 | Baking soda vs LithoLyte for raising urinary citrate/pH to reduce kidney stone risk — urinary, not gastric, application |
| [NCT06826443](https://clinicaltrials.gov/study/NCT06826443) | Phase 3 | Not yet recruiting | 100 | Mosapride vs metoclopramide for enteral feeding intolerance in ICU patients — unrelated to citric acid (grade C: not relevant) |
| [NCT02180334](https://clinicaltrials.gov/study/NCT02180334) | Phase 4 | Completed | 12 | Mosapride + DPP-4 inhibitor combination effect on incretin hormones — unrelated to citric acid (grade C: not relevant) |
| [NCT07122284](https://clinicaltrials.gov/study/NCT07122284) | N/A | Completed | 42 | Gut microbiota/metabolomic profiling in H. pylori + SIBO patients — observational, not a citric acid intervention (grade C: not relevant) |
| [NCT03320538](https://clinicaltrials.gov/study/NCT03320538) | N/A | Completed | 360 | Efficacy of a TCM herbal decoction (Hou Gu Mi Xi) for peptic ulcer disease — unrelated to citric acid |
| [NCT06760065](https://clinicaltrials.gov/study/NCT06760065) | Phase 3 | Not yet recruiting | 316 | Keverprazan-amoxicillin dual therapy vs quadruple therapy for H. pylori rescue treatment — unrelated to citric acid |
| [NCT05196945](https://clinicaltrials.gov/study/NCT05196945) | Phase 4 | Unknown | 316 | Vonoprazan + amoxicillin for first-line H. pylori eradication — unrelated to citric acid |

*Note: None of the 29 retrieved trials tested citric acid itself as an interventional treatment for stomach disease. The above are the most topically adjacent (citrate salts, gastric/GI conditions) but do not directly support the predicted indication.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Preclinical (rat) | J Pharm Pharmacol | MX1 (a bismuth–citric acid complex salt of roxatidine metabolite) showed gastroprotective effect against stress-induced ulcers in rats — the most mechanistically direct citric acid–stomach evidence found |
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Cohort | Gut and Liver | Citric acid test meal improves diagnostic accuracy of the ¹³C-urea breath test for H. pylori in Asian populations — diagnostic, not therapeutic use |
| [6027230](https://pubmed.ncbi.nlm.nih.gov/6027230/) | 1967 | Cohort | Gastroenterology | Measured lactic, pyruvic, citric, and uric acid content of human gastric juice — descriptive physiology, not an intervention study |
| [9604442](https://pubmed.ncbi.nlm.nih.gov/9604442/) | 1998 | Review | Br Med Bull | Reviews urea breath test methodology, which relies on a citric acid test meal to standardize gastric emptying |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | General review of diet/nutrition in peptic ulcer disease; does not focus on citric acid specifically |
| [38959111](https://pubmed.ncbi.nlm.nih.gov/38959111/) | 2024 | Not classified | Cell Reports | Metabolic subtyping of gastric cancer highlights TCA cycle (citric acid cycle) activity as a prognostic feature — mechanistic association only |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Not classified | Metabolomics | Elevated serum citric acid (with L-carnitine) observed before gastric cancer onset in a Korean cohort — biomarker association, not treatment |
| [37477784](https://pubmed.ncbi.nlm.nih.gov/37477784/) | 2024 | Not classified | Clin Transl Oncol | Reviews energy metabolism (including TCA cycle) as a therapeutic target class in gastric cancer — conceptual, not citric-acid-specific |
| [26088916](https://pubmed.ncbi.nlm.nih.gov/26088916/) | 2015 | Not classified | Appl Biochem Biotechnol | LC/MS metabolomic analysis of gastric cancer identifying metabolic biomarkers — citric acid appears only as a background metabolite |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | Reviews physiology/metabolism of H. pylori in the human stomach — general background, not citric acid–specific |

## Malaysia Market Information

Malaysia NPRA records show **27 registered licenses** with market status "✓ Marketed," but the evidence pack did not capture license numbers, product names, dosage forms, manufacturers, or approved indication text for any individual registration (all fields returned empty). Detailed product-level registration data needs to be re-queried from NPRA before it can be included in this report.

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data were retrieved — DG001 flags TFDA/NPRA label warnings as a Blocking data gap that must be resolved before safety screening can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (mechanistic/preclinical only) with no clinical trial directly testing citric acid for stomach disease; the available literature and trials relate mainly to citrate salts (calcium/magnesium citrate) or to citric acid's diagnostic/excipient roles, not therapeutic use. A Blocking data gap (missing label warnings/contraindications) also prevents any safety screening (S1) at this stage.

**To proceed, the following is needed:**
- Resolve DG001: obtain NPRA label warnings and contraindications for citric acid products
- Resolve DG002: obtain a defined mechanism of action from DrugBank or primary literature
- Confirm the drug's actual original/approved indication(s) via complete NPRA license records (current records returned empty)
- Identify or commission a clinical study testing citric acid itself (not calcium/magnesium citrate salts) as an intervention for a specific stomach disease subtype
- Re-evaluate TxGNN evidence level once direct interventional data becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

