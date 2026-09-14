---
layout: default
title: Zinc Acetate
parent: 僅模型預測 (L5)
nav_order: 696
evidence_level: L5
indication_count: 10
---

# Zinc Acetate
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

# Zinc Acetate: From Zinc Deficiency (Hypozincemia) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Zinc acetate is a trace-element replacement therapy, documented in the evidence pack's literature as used for Wilson's disease and hypozincemia (zinc deficiency); Malaysia-specific approved indication text is not available in the current dataset.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, with a **99.97% prediction score**,
> but **0 clinical trials** and **0 publications** currently support this direction — the evidence pack itself flags this as a likely knowledge-graph embedding artifact rather than a genuine biological association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Malaysia license data (structured fields empty); literature in this evidence pack references Wilson's disease / hypozincemia (zinc deficiency) as approved uses in other markets |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the literature captured elsewhere in this evidence pack, zinc acetate belongs to the trace-element replacement class, with established use in Wilson's disease (copper chelation via metallothionein induction) and in hypozincemia/zinc deficiency states. No original-indication data was provided in the Malaysia license records to compare against.

For this specific prediction, the evidence pack's own analysis is explicit and should be taken at face value: there is **no verifiable mechanistic link** between zinc supplementation and progression staging of diabetic retinopathy. No clinical trial or publication in the evidence pack addresses this relationship. The very high TxGNN score (99.97%, global rank 764) is assessed by the pipeline as likely reflecting **knowledge-graph embedding similarity bias** rather than a true biological association — the same pattern recurs across several other top-10 predictions for this drug (e.g., "acrodermatitis chronica atrophicans," ranked 5th, is flagged as a probable name-similarity confusion with the unrelated zinc-deficiency condition "acrodermatitis enteropathica").

Among the 10 predicted indications reviewed, the only entry with a biologically plausible rationale and supporting (if indirect) literature is **dermatitis** (rank 4, L4 evidence, "Research Question" stage) — zinc deficiency is a recognized cause of dermatitis-like skin lesions, and oral zinc repletion is standard treatment for that specific etiology. This is a materially stronger signal than the top-ranked prediction and may warrant separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Malaysia regulatory data confirms 5 active product registrations (market status: 已上市 / Marketed), but the structured license fields (license number, product name, dosage form, manufacturer, approved indication text) are all empty in the current dataset and could not be tabulated. This has been logged as Data Gap DG001 (Blocking severity) — TFDA/NPRA label warnings and indication text need to be sourced directly from the regulator before this section or the safety review below can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings` and `safety.contraindications` contain only unresolved data gaps, and the DDI query returned no results — this is logged as Data Gap DG001, Blocking severity, and must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (severe nonproliferative diabetic retinopathy) has zero supporting clinical trials or literature, and the evidence pack's own rationale explicitly attributes the high TxGNN score to probable embedding-similarity bias rather than a real drug-disease relationship. Additionally, a Blocking-severity data gap (missing TFDA/NPRA label warnings and contraindications) prevents any safety pre-screening (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the actual product label/insert for warnings, contraindications, and DDI data
- Resolve DG002 (High): confirm mechanism of action via DrugBank API query
- Obtain complete Malaysia license records (license number, product name, dosage form, approved indication text) — current dataset has 5 registrations but no populated fields
- If pursuing repurposing research, redirect focus toward **dermatitis** (rank 4, L4, "Research Question"), which has a mechanistically coherent rationale (zinc-deficiency dermatitis) versus the unsupported top-ranked prediction
- No further action recommended on severe/nonproliferative diabetic retinopathy without new primary evidence (trial or mechanistic study) directly linking zinc status to retinopathy progression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

