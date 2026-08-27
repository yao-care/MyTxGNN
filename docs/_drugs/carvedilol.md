---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: From Hypertension/Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a non-selective β1/β2- and α1-adrenergic antagonist widely used to treat hypertension and chronic heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this data pack (NPRA license text and `original_indications` are empty); generally known clinical use is hypertension / chronic heart failure |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this data pack (`original_moa`: Data Gap). Based on general pharmacological knowledge, carvedilol is a combined α1/β-adrenergic antagonist that lowers systemic blood pressure and cardiac afterload, and this class-level property has proven efficacy in hypertension.

Malignant hypertensive renal disease involves severely elevated blood pressure causing acute renal microvascular injury. Since carvedilol lowers systemic blood pressure, it could theoretically contribute as part of a multi-drug antihypertensive regimen. However, this is a **pharmacological class-level inference, not indication-specific evidence** — the acute management of malignant hypertension with renal involvement typically requires intravenous antihypertensives and treatment of the underlying cause, which oral carvedilol alone would not address.

No clinical trials, ICTRP registrations, or PubMed literature were found linking carvedilol to this specific indication, so the mechanistic plausibility above remains a theoretical hypothesis rather than a validated treatment pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Carvedilol holds **14 registered licenses** in Malaysia with market status **Marketed**, but the individual license records (authorization numbers, product names, dosage forms, approved indication text) are not populated in this data pack and cannot be displayed.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings` and `contraindications` are flagged as Data Gap in this pack; `DDI` query returned no results. This is recorded as a Blocking data gap — DG001 — since it prevents initial safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (malignant hypertensive renal disease) has zero supporting clinical trials or literature — evidence level L5, model prediction only. In addition, TFDA/NPRA warning and contraindication data (DG001, Blocking severity) is missing, which by itself blocks entry into the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA/NPRA product label with warnings and contraindications (DG001)
- DrugBank mechanism-of-action data to support mechanistic-link analysis (DG002)
- Actual NPRA license records (product names, approved indication text) for the Malaysia market table
- Targeted literature/clinical search specifically on carvedilol in malignant hypertension with renal involvement

**Additional note on other candidates in this evidence pack:** Ranks 2, 3, and 5 (malignant renovascular hypertension, unclear-mechanism pulmonary hypertension, Braddock syndrome) are similarly L5/Hold with no supporting evidence — Braddock syndrome in particular appears to be a spurious knowledge-graph link with no plausible mechanistic connection. Rank 4 (pulmonary hypertension owing to lung disease/hypoxia) is the only candidate with literature (20 PubMed hits, mostly general hypoxia biology, tier 3), but the rationale for that candidate leans toward a **safety caution signal** rather than a therapeutic opportunity — non-selective β-blockers are traditionally used with caution in hypoxic pulmonary hypertension due to blunting of compensatory right-ventricular response.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

