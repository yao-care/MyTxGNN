---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
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

# Thyrotropin Alfa: From Thyroid Cancer Follow-up to Migraine Disorder

## One-Sentence Summary

Thyrotropin alfa (recombinant human TSH) is internationally used as a diagnostic and adjunctive agent in the follow-up of well-differentiated thyroid cancer after thyroidectomy. The TxGNN model's top prediction for this drug is **Migraine Disorder**, but this direction currently has **zero clinical trials** and **zero publications** supporting it — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid cancer follow-up (adjunctive to thyroidectomy) — based on general pharmacological reference; Malaysia NPRA-specific approved indication text is not available in the current dataset (Blocking Data Gap, see DG001) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Thyrotropin alfa is flagged as a Data Gap (DG002) in this evidence pack. Based on established pharmacological knowledge — and corroborated by this same evidence pack's own analysis of the rank-10 candidate (hyperthyroidism) — Thyrotropin alfa is a recombinant human TSH that acts as a **TSH-receptor agonist**, stimulating thyroid follicular cell proliferation and thyroid hormone secretion. Internationally, it is used to aid detection of thyroid remnant/recurrent disease and to support radioiodine ablation in patients with well-differentiated thyroid cancer.

For the top-ranked prediction, **migraine disorder**, there is no known mechanistic pathway linking TSH-receptor signaling to migraine pathophysiology. The evidence pack's own rationale states this plainly: "無任何臨床試驗或文獻支持；TSH 受體訊號與偏頭痛病理生理無已知直接連結，純為模型預測分數" — i.e., no clinical trial or literature support exists, and the connection is purely a model score artifact. This pattern repeats across ranks 2–9 (Raynaud disease, atrophoderma vermiculata, pulmonary hypertension, POTS, etc.), which the evidence pack itself characterizes as likely knowledge-graph embedding proximity errors rather than genuine biological relationships.

Notably, the one candidate in this set with real supporting clinical trials — **hyperthyroidism** (rank 10, L2/S1) — carries a documented mechanistic contradiction: Thyrotropin alfa is a thyroid-*stimulating* agent, so it would be expected to induce or worsen hyperthyroidism rather than treat it. The two supporting trials actually studied rhTSH as pretreatment for radioiodine therapy in benign goiter, not as a treatment for primary hyperthyroidism. This underscores that the overall repurposing signal set for this drug should be treated with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

NPRA records confirm 1 active registration for Thyrotropin alfa, with market status "已上市" (Marketed). However, the licence number, product name, dosage form, and approved indication text are not populated in the current dataset — retrieval/parsing of the NPRA product label is required (see DG001, Blocking severity) before this information can be reported.

## Safety Considerations

Please refer to the package insert for safety information. Note: label-level warnings, contraindications, and drug interaction data could not be retrieved for this drug (DG001, Blocking) — this gap by itself is sufficient to prevent progression past the initial safety screening stage (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (migraine disorder) has no clinical trial or literature evidence and no plausible mechanistic basis — it is a pure model-score signal (L5, decision stage S0). Compounding this, a Blocking data gap in TFDA/NPRA label safety information (DG001) prevents even a preliminary safety review for this drug.

**To proceed, the following is needed:**
- Retrieve and parse the NPRA product label/insert to fill DG001 (warnings, contraindications, DDI) and confirm the actual approved indication text
- Obtain DrugBank mechanism-of-action and categorization data to close DG002
- If pursuing further evaluation of this drug's repurposing potential, prioritize the hyperthyroidism/goiter signal (rank 10) instead of migraine — but first resolve the mechanistic contradiction (TSH agonism vs. treating hyperthyroidism) with an endocrinology-literate review before any S2+ progression
- Given the near-total absence of supporting evidence across 9 of 10 predicted indications, consider deprioritizing this candidate in favor of TxGNN outputs with stronger underlying evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

