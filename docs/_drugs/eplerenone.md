---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 5
---

# Eplerenone
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

# Eplerenone: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Eplerenone (DrugBank DB00700) is a selective mineralocorticoid (aldosterone) receptor antagonist marketed in Malaysia, with hypertension as its known original indication (though the registry's approved-indication text has not yet been extracted from the product insert). The TxGNN model predicts potential efficacy for **Pulmonary Hypertension with Unclear Multifactorial Mechanism**, but currently **zero clinical trials and zero drug-specific literature** support this direction — this is a model-score-only prediction (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (per known pharmacological classification as an MRA; official approved-indication text not yet extracted from the license record — see Data Gap DG001) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not yet available in this evidence pack (Data Gap DG002). Based on known pharmacological classification, eplerenone is a selective aldosterone (mineralocorticoid) receptor antagonist (MRA); its efficacy in hypertension is well established, and mechanistically MRA-class drugs are theorized to counteract aldosterone-driven pulmonary vascular remodeling and fibrosis, which is the basis of the TxGNN mechanistic hypothesis for pulmonary hypertension.

However, this specific predicted indication — "pulmonary hypertension with unclear multifactorial mechanism" — is itself a category whose underlying mechanism is undefined, and the evidence pack returns **no clinical trials and no literature** for eplerenone against this indication. A closely adjacent, similarly-scored prediction (rank 2, "pulmonary hypertension owing to lung disease and/or hypoxia," score 99.50%) did return 20 PubMed hits, but per the evidence pack's own classification these are generic hypoxia-biology papers (brain aging, tumor metabolism, cognitive impairment) with no drug-specific relevance to eplerenone or MRAs — they represent literature-search noise rather than supporting evidence.

At present, this prediction rests entirely on the TxGNN model score and a plausible but unverified mechanistic hypothesis, with no drug-specific or disease-specific data confirming applicability.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Two registrations exist under the current market status (✓ Marketed), but the license detail fields (authorization number, product name, dosage form, approved indication text) have not yet been populated in this evidence pack. This gap also underlies the missing "Original Indication" text above and should be resolved before further evaluation.

## Safety Considerations

Please refer to the package insert for safety information. Note: retrieval of the TFDA/NPRA product insert (warnings and contraindications) is flagged as a **Blocking** data gap (DG001) — until resolved, this candidate cannot proceed to the S1 safety pre-assessment stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pulmonary hypertension with unclear multifactorial mechanism) has no supporting clinical trials or literature — it is a pure model-score prediction (L5). In addition, the blocking safety data gap (missing product insert warnings/contraindications) prevents this candidate from even entering the S1 safety pre-assessment.

**To proceed, the following is needed:**
- Retrieve the TFDA/NPRA product insert for warnings and contraindications (DG001, blocking)
- Obtain confirmed mechanism-of-action data from DrugBank (DG002)
- Populate the Malaysia license records (product name, dosage form, approved indication text) for both registrations
- If pursuing rank-2 "pulmonary hypertension owing to lung disease and/or hypoxia" as an alternative, run a targeted literature search for eplerenone/MRA-specific studies, since the current 20 hits are generic hypoxia biology, not drug- or disease-specific evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

