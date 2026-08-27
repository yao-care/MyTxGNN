---
layout: default
title: Gliclazide
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 5
---

# Gliclazide
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

# Gliclazide: From Type 2 Diabetes Mellitus to Type 2 Diabetes Mellitus (No Valid New-Indication Signal)

## One-Sentence Summary

Gliclazide is a second-generation sulfonylurea already approved and marketed for type 2 diabetes mellitus (T2DM). All five "predicted indications" returned by TxGNN for this candidate are variants of the same disease (T2DM / diabetes mellitus) with a **TxGNN score of 0.0**, indicating this is not a genuine repurposing signal but a data artifact caused by a missing `original_indications` field upstream. **35 clinical trials and 20 publications** were retrieved, but they support gliclazide's existing, already-approved indication — not a new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (based on well-established pharmacology; NPRA license indication text not captured in this data pull) |
| Predicted "New" Indication | Type 2 Diabetes Mellitus (duplicate of original indication — see rationale below) |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 (evidence quality is high, but it substantiates the *existing* indication, not a repurposing hypothesis) |
| Malaysia Market Status | ✓ Marketed (NPRA) |
| Number of Registrations | 36 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) record is not available in DrugBank for this candidate (flagged as a High-severity data gap, DG002). Based on known pharmacology captured in the evidence pack's own repurposing rationale: gliclazide is a second-generation sulfonylurea that acts directly on the SUR1/Kir6.2 (K_ATP) channel of pancreatic β-cells. Channel closure triggers membrane depolarization, opens voltage-gated calcium channels, and stimulates insulin secretion — this is gliclazide's **original, already-approved** glucose-lowering mechanism, not a newly discovered pathway.

All five ranked "predicted indications" in this evidence pack are "type 2 diabetes mellitus" or "diabetes mellitus" at different granularities. This is not a repurposing hypothesis: it is the drug's own indication reappearing because the upstream `drug.original_indications` field is empty, so the deduplication step that should exclude already-known indications from the repurposing candidate list did not fire. The `txgnn.score = 0.0` across all five ranks corroborates this — TxGNN did not actually assign confidence to these as novel drug–disease edges.

**Conclusion: there is no scientifically meaningful "old drug, new use" hypothesis to evaluate here.** The correct action is a data-pipeline fix, not a clinical evaluation.

---

## Clinical Trial Evidence

*(Evidence below documents gliclazide's performance in its existing indication, T2DM — not a new indication.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01709305](https://clinicaltrials.gov/study/NCT01709305) | Phase 4 | Completed | 5,570 | Large multicenter Chinese RCT comparing gliclazide, glimepiride, repaglinide, or acarbose as third-line add-on to sitagliptin+metformin in T2DM |
| [NCT00102388](https://clinicaltrials.gov/study/NCT00102388) | Phase 3 | Completed | 1,092 | Vildagliptin vs. gliclazide in drug-naive T2DM patients — direct efficacy/safety comparison |
| [NCT01758380](https://clinicaltrials.gov/study/NCT01758380) | Phase 4 | Completed | 557 | Double-blind, double-dummy RCT comparing vildagliptin vs. gliclazide as dual therapy with metformin during Ramadan fasting |
| [NCT01420692](https://clinicaltrials.gov/study/NCT01420692) | N/A | Completed | 64 | Insulin detemir vs. gliclazide-MR added to lifestyle modification + metformin — effects on endothelial function |
| [NCT00738088](https://clinicaltrials.gov/study/NCT00738088) | Phase 4 | Terminated | 14 | Mechanistic study of sulfonylurea glycemic response and T2DM pathophysiology |
| [NCT02092597](https://clinicaltrials.gov/study/NCT02092597) | Phase 4 | Completed | 42 | Safety evaluation of incretin-based therapies on cardiovascular, GI, and renal systems |
| [NCT01195259](https://clinicaltrials.gov/study/NCT01195259) | N/A | Completed | 1 | ADOPT/RECORD malignancy AE meta-analysis (metformin vs. rosiglitazone) — not directly related to gliclazide; likely a database linkage artifact |
| [NCT06704802](https://clinicaltrials.gov/study/NCT06704802) | N/A | Completed | 678 | Observational cohort assessing an education program combined with gliclazide MR on HbA1c in uncontrolled T2DM |
| [NCT02475499](https://clinicaltrials.gov/study/NCT02475499) | N/A | Completed | 886,172 | Pharmacoepidemiologic study of incretin-based drugs and pancreatic cancer risk, using sulfonylureas as comparator |
| [NCT03246828](https://clinicaltrials.gov/study/NCT03246828) | N/A | Completed | 10 | Effect of gliclazide on glucagon secretion in HNF1A/HNF4A-MODY (an atypical, non-T2DM diabetes subtype) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18539916](https://pubmed.ncbi.nlm.nih.gov/18539916/) | 2008 | RCT | New England Journal of Medicine | ADVANCE trial: intensive glucose control (gliclazide MR-based) and vascular outcomes in T2DM |
| [39792745](https://pubmed.ncbi.nlm.nih.gov/39792745/) | 2025 | RCT | Medicine | Sitagliptin vs. gliclazide + metformin in treatment-naive T2DM with glucotoxicity |
| [40326063](https://pubmed.ncbi.nlm.nih.gov/40326063/) | 2025 | RCT (crossover) | Diabetes, Obesity & Metabolism | RACELINES: renal haemodynamic effects of empagliflozin/linagliptin vs. gliclazide |
| [36300277](https://pubmed.ncbi.nlm.nih.gov/36300277/) | 2022 | Review | Expert Opinion on Pharmacotherapy | Overview of gliclazide's role in T2DM management vs. newer agents |
| [29802958](https://pubmed.ncbi.nlm.nih.gov/29802958/) | 2018 | Review | Diabetes Research and Clinical Practice | Positioning of gliclazide MR among sulfonylureas and newer antihyperglycemics |
| [24533045](https://pubmed.ncbi.nlm.nih.gov/24533045/) | 2014 | Systematic Review/Meta-analysis | PLoS ONE | Safety and efficacy of gliclazide vs. other glucose-lowering agents |
| [35398820](https://pubmed.ncbi.nlm.nih.gov/35398820/) | 2022 | Observational | Acta Medica Indonesiana | Real-world DIA-RAMADAN study of gliclazide MR safety/efficacy during Ramadan |
| [32516291](https://pubmed.ncbi.nlm.nih.gov/32516291/) | 2020 | RCT/Cohort | Journal of Hypertension | Cardiorenal effects of dapagliflozin vs. gliclazide in T2DM |
| [29558784](https://pubmed.ncbi.nlm.nih.gov/29558784/) | 2019 | RCT | Exp Clin Endocrinol Diabetes | Alogliptin and gliclazide similarly increase circulating endothelial progenitor cells |
| [30119196](https://pubmed.ncbi.nlm.nih.gov/30119196/) | 2018 | PK Study | Biomedicine & Pharmacotherapy | Minimum steady-state gliclazide concentration in T2DM patients on MR tablets |

---

## Malaysia Market Information

NPRA records confirm gliclazide is currently marketed in Malaysia with **36 registered product licenses**. However, this data pull did not retrieve individual license numbers, product names, dosage forms, or indication text (all license-detail fields returned empty), so a per-product table cannot be presented. This gap should be remediated by re-querying the NPRA product register for the full license listing.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(TFDA/NPRA package insert warnings and contraindications were flagged as a Blocking-severity data gap (DG001) in this evidence pack — no key warnings, contraindications, or drug interaction data could be retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All five predicted "new" indications are the drug's own existing indication (T2DM) at different naming granularities, with a TxGNN score of 0.0 — this is a data-pipeline duplication artifact (missing `original_indications` field), not a repurposing hypothesis. There is nothing here to evaluate as "old drug, new use."
- Separately, a Blocking-severity gap (missing package insert warnings/contraindications) means this candidate could not pass even a baseline safety screen (S1) regardless of the indication question.

**To proceed, the following is needed:**
- Fix the upstream data pipeline to populate `drug.original_indications` for gliclazide and re-run deduplication so already-approved indications are excluded from the repurposing candidate list
- Retrieve TFDA/NPRA package insert warnings, contraindications, and DDI data (DG001, Blocking)
- Retrieve structured MOA data from DrugBank (DG002, High)
- Re-query NPRA for complete per-license product details (license number, product name, dosage form, indication text)
- If TxGNN is re-run after the data fix and surfaces a genuinely distinct, non-zero-score indication for gliclazide, re-evaluate as a new candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

