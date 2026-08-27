---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
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

# Ergocalciferol: From Unrecorded Original Indication to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Ergocalciferol (vitamin D2) is a long-marketed product in Malaysia (10 active NPRA registrations), but this evidence pack contains no usable record of its formally approved indication text. The TxGNN model's top-ranked prediction — **obsolete vitamin D deficiency** — is supported by **zero clinical trials and zero literature citations**, and its own rationale text flags it as very likely a re-identification of the drug's own established, already-approved use rather than a genuine new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — all NPRA license indication-text fields and the drug-level `original_indications` field were empty in this evidence pack |
| Predicted New Indication | Obsolete Vitamin D Deficiency* |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (zero clinical trials, zero literature — see note below) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

*"Obsolete" here is the disease-ontology term itself (MONDO/OMIM marks it a deprecated concept), and the model's own `repurposing_rationale` states this is likely a re-detection of ergocalciferol's known indication rather than a real repurposing candidate.

**Note on Evidence Level:** the evidence pack's internal scoring field labels this candidate "L1," but per the determination rules (L1 requires ≥2 completed Phase 3 RCTs) and the fact that both `clinical_trials` and `literature` arrays are empty for this candidate, the correct level by the stated criteria is **L5**. This discrepancy should be corrected upstream in the scoring pipeline.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, ergocalciferol (vitamin D2) is a fat-soluble vitamin D precursor that undergoes hepatic 25-hydroxylation and renal 1α-hydroxylation to its active metabolite, calcitriol, which regulates intestinal calcium/phosphate absorption and bone mineralization. This pathway is well established and is the pharmacological basis for essentially all of the candidates surfaced in this pack.

The top-ranked candidate, however, is not a useful repurposing signal: the disease term "obsolete vitamin D deficiency" is itself vitamin D2's original, textbook indication, and the model's own rationale explicitly states that the high score likely reflects "already-known pharmacological fact, not a new discovery" — an artifact plausibly caused by the missing `original_indications` data, which left TxGNN unable to distinguish this candidate from ergocalciferol's known use.

Looking past rank 1, several lower-ranked candidates show a more genuine, evidence-backed repurposing pattern — ergocalciferol used as an adjunct in calcium/phosphate-metabolism bone disorders adjacent to its core indication: **renal osteodystrophy** (rank 9, L2, a Phase 4 trial plus a 1985 head-to-head clinical study of ergocalciferol vs. calcitriol), **hereditary hypophosphatemic rickets** (rank 7, L3, including a 1980 NEJM clinical study using ergocalciferol directly), and **hypophosphatemia** (rank 8, L3, including an actively planned ergocalciferol dosing trial, NCT07366450). These are mechanistically coherent and worth separate evaluation, even though modern practice has largely shifted to active vitamin D analogues (calcitriol/doxercalciferol) for these conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

(TFDA/NPRA warnings and contraindications were not available in this evidence pack — this is flagged as a **Blocking**-severity data gap, DG001, and prevents this candidate from entering the S1 safety review stage regardless of efficacy evidence.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate carries no clinical trial or literature support, and the evidence pack's own rationale indicates it likely duplicates ergocalciferol's existing, already-approved use rather than representing a novel indication. Separately, a Blocking safety-data gap (no TFDA/NPRA label warnings or contraindications on file) prevents any candidate for this drug from clearing the initial safety screen.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the NPRA package insert for warnings/contraindications
- Resolve DG002 (High): query DrugBank for confirmed mechanism of action
- Obtain the drug's actual approved indication text — all 10 current NPRA license records in this pack have empty product name, dosage form, and indication fields
- If a genuine repurposing opportunity is still wanted, redirect review effort to ranks 7–9 (hereditary hypophosphatemic rickets, hypophosphatemia, renal osteodystrophy), which carry real — if dated — clinical evidence, rather than rank 1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

