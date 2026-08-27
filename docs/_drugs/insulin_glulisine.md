---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus (Label Indication) to Type 1 Diabetes Mellitus (Confirmatory Signal, Not True Repurposing)

## One-Sentence Summary

Insulin glulisine is a rapid-acting insulin analogue already used for glycemic control in diabetes mellitus. The TxGNN model's top-ranked prediction is **Type 1 Diabetes Mellitus** — but this is the drug's **existing, on-label indication**, not a novel repurposing candidate, supported by **50 clinical trials** and **19 publications**. The model's high score here reflects correct recall of a known drug–disease relationship rather than a new hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus, glycemic control (formal NPRA label indication text not yet retrieved — data gap) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa`: Data Gap). Based on the evidence pack's own model rationale, insulin glulisine is a **rapid-acting insulin analogue** that is already approved for glycemic control in type 1 diabetes. This means the top-ranked "predicted" indication is in fact the drug's established, on-label use — not a genuine repurposing candidate. The very high TxGNN score (99.55%) is consistent with this: it reflects the model correctly recovering a known, well-documented drug–disease association from the knowledge graph, rather than surfacing a novel signal.

This is corroborated by the depth of supporting evidence: 50 registered clinical trials and 19 publications directly involving insulin glulisine in type 1 diabetes populations, including multiple completed Phase 3 non-inferiority trials against insulin lispro and insulin aspart across adult, pediatric, and CSII (pump) settings. This volume of evidence is what would be expected for a mature, approved indication — not an exploratory hypothesis.

It is worth noting that ranks 2–10 in this evidence pack (e.g., thiamine-responsive dysfunction syndrome, stiff person syndrome, autoimmune oophoritis, and several lipodystrophy entries) carry no clinical trial or literature support (Evidence Level L5, decision stage S0/Hold). Several of these — particularly the lipodystrophy-related entries — are flagged in the model rationale as potentially **causality-reversed**: localized lipoatrophy/lipodystrophy is a known adverse effect of insulin injection, so the graph may be linking "insulin" and "lipodystrophy" via an adverse-event edge rather than a treatment edge. These should not be advanced without independent mechanistic review. The only mid-tier candidate is rank 7 (pancreatic agenesis, L4, "Research Question") — insulin replacement is standard care for the permanent neonatal diabetes caused by pancreatic agenesis, but no dedicated trials or literature were found in this data pull.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | Completed | 100 | Apidra (glulisine) + Lantus basal-bolus regimen in children/adolescents with T1DM in Russia; evaluated HbA1c targets and hypoglycemia rates |
| [NCT02688933](https://clinicaltrials.gov/study/NCT02688933) | Phase 4 | Completed | 638 | Large RCT comparing morning Toujeo (glargine U300) vs Lantus in T1DM using CGM-measured glycemic control |
| [NCT02685449](https://clinicaltrials.gov/study/NCT02685449) | Phase 4 | Unknown | 70 | Cross-over study of insulin requirement for pure-protein meals in children with T1DM on CSII |
| [NCT01792830](https://clinicaltrials.gov/study/NCT01792830) | Phase 3 | Completed | 175 | Glargine-based hospital discharge insulin algorithm efficacy/safety in cardiac surgery patients with perioperative hyperglycemia |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | 26-week efficacy/safety study of insulin glulisine (HMR1964) with insulin glargine in T1DM |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Insulin glulisine vs insulin lispro (both with Lantus) in T1DM/T2DM — efficacy, hypoglycemia frequency |
| [NCT01768559](https://clinicaltrials.gov/study/NCT01768559) | Phase 3 | Completed | 894 | 26-week RCT: lixisenatide vs once-daily/thrice-daily insulin glulisine added to insulin glargine ± metformin in T2DM |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | INHALE-1: inhaled Afrezza vs rapid-acting analogs (incl. glulisine) + basal insulin in pediatric T1DM/T2DM |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | 28-week non-inferiority study: insulin glulisine (HMR1964) vs insulin lispro in T1DM |
| [NCT00135083](https://clinicaltrials.gov/study/NCT00135083) | Phase 3 | Completed | 347 | Once vs twice vs thrice-daily insulin glulisine as add-on to glargine + oral sensitizer in T2DM |

40 additional trials were identified in the evidence pack but are not listed here for brevity.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | 683-patient RCT comparing insulin glulisine vs insulin lispro in adults with T1DM |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | 26-week trial: comparable efficacy/safety of glulisine vs lispro in basal-bolus regimen, pediatric T1DM |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Randomized crossover: glulisine vs aspart vs lispro via CSII in T1DM |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | RCT | Diabetes Obes Metab | Glulisine vs lispro (with glargine) in Japanese patients with T1DM |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of insulin glulisine use in diabetes mellitus management |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Review | Drugs of Today | Review of insulin analogues, including glulisine, in children/adolescents with T1DM |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Review (PK/PD) | Clin Pharmacokinet | Clinical pharmacokinetics and pharmacodynamics of insulin glulisine |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | Study | Diabetes Care | PK, postprandial glucose control, and safety of glulisine in pediatric T1DM |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Study | Pediatr Int | Efficacy/safety of glulisine for CSII in pediatric T1DM (Japan) |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Review | Drugs | Review of insulin glulisine pharmacology and clinical trial data in T1DM/T2DM |

9 additional publications were identified in the evidence pack but are not listed here for brevity.

---

## Malaysia Market Information

Malaysia (NPRA) market status is **✓ Marketed**, with 1 registration on record. However, the registration detail fields (authorization number, product name, dosage form, approved indication text) were **not populated in this data pull** — this is tracked as Data Gap DG001 (Blocking) in the evidence pack and must be resolved before a full label table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this data pull — DG001, Blocking.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base (L1, 50 trials, 19 publications) is strong, but it supports the drug's **existing** indication rather than a new one — this candidate should be treated as a label/data-completeness item, not a repurposing opportunity. The "Proceed with Guardrails" status is driven by the blocking data gap on TFDA/NPRA label safety information (DG001), not by uncertainty about efficacy.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (warnings, contraindications) — blocking for safety review (DG001)
- DrugBank mechanism-of-action data to complete the mechanistic record (DG002)
- Confirmation that this candidate is not a duplicate of an already-approved indication in the pipeline database
- If pursuing genuinely novel signals from this drug, rank 7 (pancreatic agenesis, L4) is the only candidate with a plausible mechanistic rationale and would need dedicated evidence collection; ranks 2–6 and 8–10 (L5, Hold) are not actionable without independent mechanistic verification, and the lipodystrophy-related ranks (8–10) should first be checked for causality-reversed graph edges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

