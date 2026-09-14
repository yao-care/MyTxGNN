---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Pregnancy-Associated Osteoporosis

## One-Sentence Summary

> Teriparatide (DrugBank DB06285) is a recombinant PTH(1-34) analogue originally used to treat osteoporosis by stimulating bone formation.
> Among the 10 TxGNN-predicted indications in this pack, most of the highest-scoring candidates (e.g. duodenal ulcer, esophageal malformation) have **no supporting evidence** and are explicitly flagged in the pack's own rationale as likely **model noise**.
> The most evidence-backed candidate is **Pregnancy-Associated Osteoporosis**, supported by **2 completed clinical trials** (neither enrolled the target population) and corresponding to **Evidence Level L3**.

*Note on selection: the raw #1 TxGNN score (duodenal ulcer, 99.86%) was not used as the headline indication because it has zero clinical/literature evidence and the pack's own mechanistic-link field describes it as embedding noise. This report instead highlights the highest-scoring candidate that has actual supporting data.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (per FORTEO/teriparatide labeling referenced in trial NCT00277706; not directly available from NPRA license text) |
| Predicted New Indication | Pregnancy-Associated Osteoporosis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Teriparatide is a PTH(1-34) recombinant analogue that activates the PTH1 receptor, stimulating osteoblastic bone formation. It is an approved osteoanabolic agent for osteoporosis. Pregnancy-associated osteoporosis is, at its core, still a low-bone-density/bone-loss disorder, so there is a plausible mechanistic overlap with teriparatide's core indication — activating the same PTH1-mediated bone-formation pathway that underlies its approved osteoporosis use.

However, neither supporting trial was designed for this population: NCT00277706 (Phase 1, completed, N=40) tested PTH(1-34)/FORTEO for periodontal bone regeneration, and NCT02440581 (NA phase, completed, N=141) studied bone loss in dialysis-dependent renal osteodystrophy patients. Both provide only indirect, mechanism-level support rather than direct efficacy evidence in pregnant or postpartum patients. Critically, teriparatide use in pregnancy carries an unresolved reproductive-safety question — animal studies have raised an osteosarcoma signal, and no fetal safety data exists for this population.

By contrast, the majority of the other 9 predicted indications (duodenal ulcer, non-syndromic esophageal malformation, duodenal obstruction, duodenogastric reflux, Worth syndrome, autosomal dominant neovascular inflammatory vitreoretinopathy, succinyl-CoA:3-ketoacid CoA transferase deficiency) have no clinical trials, no literature, and no plausible mechanistic link to PTH1-receptor signaling — several are even mechanistically contradictory (e.g., Worth syndrome is a high-bone-density disorder, the opposite direction of an osteoanabolic drug). One additional candidate, amenorrhea (rank 10, L4), has indirect support via estrogen-deficiency-related bone loss (PMID 36303862), but the only literature is a general review, not a direct intervention study. Esophageal disease (rank 5) literature was also reviewed and excluded — the cited papers describe teriparatide **adverse events** (including calcinosis cutis), not efficacy in esophageal disease, so it is a safety signal in the wrong direction, not repurposing support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | Tested PTH(1-34) (FORTEO) combined with periodontal surgery for oral bone regeneration; confirms osteoanabolic mechanism but not specific to pregnancy-associated osteoporosis |
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Evaluated bone loss/renal osteodystrophy in CKD dialysis patients; population and intervention only tangentially relevant |

---

## Literature Evidence

Currently no literature is registered specifically for the Pregnancy-Associated Osteoporosis indication.

(For context: the secondary candidate, amenorrhea, is supported by one review — [PMID 36303862](https://pubmed.ncbi.nlm.nih.gov/36303862/), 2022, *Frontiers in Endocrinology* — on bone health in functional hypothalamic amenorrhea, but it is not a direct teriparatide intervention study.)

---

## Malaysia Market Information

NPRA status is **Marketed (已上市)** with **5 registered licenses**. However, product name, dosage form, manufacturer, and approved-indication text for these 5 licenses are not populated in the current data extract, so a license-level table cannot be produced. This gap should be remediated (NPRA product search or label PDF) before Malaysia-specific labeling comparisons are made.

---

## Safety Considerations

TFDA/NPRA package insert warnings, contraindications, and drug-interaction data are currently unavailable — this is flagged as a **Blocking** data gap (DG001), which prevents a formal safety (S1) review. Please refer to the official package insert for safety information until this gap is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Safety data required for even an initial risk screen is blocked (DG001, Blocking severity), and the strongest available indication (pregnancy-associated osteoporosis) is only supported by trials in unrelated populations plus an unresolved reproductive-safety concern (potential osteosarcoma signal in animal data, no fetal safety data). Evidence is directional, not confirmatory.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications, DDI) to close DG001
- Confirmed mechanism of action from DrugBank to close DG002
- Dedicated clinical evidence in pregnant/postpartum osteoporosis patients
- Reproductive and fetal safety data before any pregnancy-related indication is considered
- Completion of Malaysia license details (product name, dosage form, indication text) for the 5 existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

