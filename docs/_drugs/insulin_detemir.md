---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir (DrugBank DB01307) is a long-acting basal insulin analogue already established in clinical practice for managing diabetes mellitus. The TxGNN model's top-ranked prediction — **Type 1 Diabetes Mellitus** — is supported by extensive evidence (50 clinical trials queried, multiple completed Phase 3 RCTs with up to 2,287 participants, and 19 PubMed publications), but as the evidence pack itself notes, this is **not a genuine new indication**: insulin detemir is already a standard T1DM treatment, so this prediction is best read as a validation of known pharmacology rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1 & Type 2) — established use; formal Malaysia licence indication text was not captured in this evidence pack (see Market Information below) |
| Predicted New Indication | Type 1 Diabetes Mellitus *(already an existing, approved use of this drug — see caveat below)* |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action data from DrugBank is not available (Data Gap DG002). Based on the literature captured in this evidence pack, insulin detemir is a soluble, long-acting human insulin analogue acylated with a 14-carbon fatty acid; this modification allows reversible binding to albumin, producing slow, predictable absorption and a prolonged glucose-lowering effect of up to 24 hours (PMID [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/), PMID [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/)). Like other basal insulins, it acts directly on the insulin receptor to normalize glucose metabolism.

**Important caveat:** Unlike a typical drug-repurposing candidate, insulin detemir's mechanistic link to type 1 diabetes mellitus is not an inferred cross-indication relationship — the drug's `repurposing_rationale` explicitly states it "is already a standard T1DM treatment" and that this is "not true drug repurposing." The TxGNN model has effectively rediscovered an already-approved use, which explains the unusually strong and abundant clinical/literature evidence (L1) compared to the other candidates below.

The remaining nine TxGNN-predicted indications for this drug (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, classic/focal stiff person syndrome, pancreatic agenesis, and three lipodystrophy-related conditions) all score similarly high (99.4–99.7%) but have **zero supporting clinical trials or literature**. Their rationale notes describe them as comorbidity artifacts (shared autoimmune markers with T1DM), molecular pathway coincidences (e.g., INPPL1/SHIP2 signaling), or — in the case of the lipodystrophy conditions — likely **reversed causality**, since insulin injection is a known *cause* of localized lipodystrophy rather than a treatment for it.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Multinational RCT comparing insulin detemir + aspart vs. NPH + human soluble insulin in T1DM basal-bolus regimen |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN Young 1: 26-week efficacy/safety comparison of insulin degludec vs. detemir in children/adolescents with T1DM |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | Six-month comparison of insulin detemir (2400 nmol/mL formulation) vs. NPH insulin in T1DM basal-bolus regimen |
| [NCT00738153](https://clinicaltrials.gov/study/NCT00738153) | N/A (observational) | Completed | 798 | Post-marketing efficacy and serious adverse drug reaction surveillance of Levemir® in T1DM and T2DM (Africa) |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Phase 3 | Completed | 2287 | Large multicentre, non-randomised safety study of insulin detemir in insulin-dependent T1DM and T2DM |
| [NCT01454284](https://clinicaltrials.gov/study/NCT01454284) | Phase 3 | Completed | 1114 | 52-week double-blind RCT comparing LY2605541 vs. insulin glargine in T1DM (detemir-class comparator context) |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | RCT of insulin detemir vs. NPH insulin (with aspart bolus) in pregnant women with T1DM |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | Completed | 447 | RCT comparing insulin detemir + aspart vs. insulin glargine + aspart in T1DM |
| [NCT00487240](https://clinicaltrials.gov/study/NCT00487240) | Phase 3 | Completed | 387 | Comparison of insulin lispro protamine suspension vs. insulin detemir as basal insulin in T1DM basal-bolus therapy |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | Completed | 330 | 12-month double-blind safety comparison of insulin detemir made by two different production processes in T1DM |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT trial: insulin degludec non-inferior to insulin detemir (both + aspart) in pregnant women with T1DM |
| [36896906](https://pubmed.ncbi.nlm.nih.gov/36896906/) | 2024 | Review | Current Diabetes Reviews | Two-decade review of insulin glargine trials in T1DM, with detemir as key comparator |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Review (systematic review + network meta-analysis) | Value in Health | Comparative efficacy/safety of basal insulin regimens (including detemir) in adults with T1DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review / Meta-analysis | Polskie Archiwum Medycyny Wewnetrznej | Detemir vs. NPH insulin in T1DM: mixed evidence on glycemic control improvement |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vascular Health and Risk Management | Overview of insulin detemir as basal analogue in T1DM/T2DM; lower hypoglycemia rate vs. NPH |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Pharmacology review: albumin-binding mechanism gives detemir predictable, prolonged action in T1DM/T2DM |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vascular Health and Risk Management | Detemir's unique albumin-binding mechanism reduces hypoglycemia risk, especially nocturnal, in T1DM |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Spotlight review on detemir's predictable metabolic effect vs. NPH insulin in T1DM/T2DM |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Comprehensive review of detemir's reduced within-patient variability vs. NPH/ultralente |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes & Endocrinology | Management of T1DM in pregnancy: lifestyle, pharmacological treatment (incl. basal insulins), and technology |

---

## Malaysia Market Information

The evidence pack confirms **3 registered licences** with market status "已上市 (Marketed)," but the individual licence numbers, product names, dosage forms, manufacturers, and approved-indication text fields were not populated in this data source. This is a data-completeness gap in the regulatory extraction pipeline (separate from Data Gap DG001, which concerns package-insert warnings), not evidence that the product is unlicensed — insulin detemir is internationally marketed as Levemir®.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: the evidence pack flags TFDA/NPRA label warnings and contraindications as a **Blocking** data gap (DG001) — this specifically prevents a formal S1 safety pre-assessment and should be resolved before final sign-off, even though insulin detemir's real-world safety profile (primarily hypoglycemia risk) is well characterized in long-standing clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence for the T1DM indication itself is very strong (L1, multiple completed Phase 3 RCTs), but this reflects confirmation of an already-approved use rather than novel repurposing value — it should not be marketed or resourced as a "new indication" finding.
- All other TxGNN-predicted indications for this drug (ranks 2–10) lack any clinical trial or literature support (L4–L5) and are flagged in their own rationale as comorbidity artifacts, pathway coincidences, or reversed-causality errors (lipodystrophy candidates) — none warrant advancement.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA package-insert warnings and contraindications (DG001, Blocking) to complete the S1 safety pre-assessment
- Retrieve formal DrugBank MOA text (DG002) to replace the literature-derived mechanism summary above
- Populate the 3 Malaysia licence records (numbers, product names, dosage forms, approved indication text) currently missing from the regulatory data source
- If this candidate is retained in the repurposing pipeline, reclassify it as "known-use validation" rather than a novel repurposing lead, since rank-1 is not a true new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

