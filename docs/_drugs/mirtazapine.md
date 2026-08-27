---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 487
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Mirtazapine: From Major Depressive Disorder to Ohdo Syndrome and Variants

## One-Sentence Summary

> Mirtazapine is a NaSSA-class antidepressant established for major depressive disorder.
> The TxGNN model predicts it may be effective for **Ohdo Syndrome and Variants**,
> but currently **no clinical trials** and **no publications** support this direction — the prediction is model-output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (based on established drug class; TFDA-specific indication text not captured in evidence pack) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mirtazapine is a noradrenergic and specific serotonergic antidepressant (NaSSA) — it antagonizes central presynaptic α2-adrenergic auto-/heteroreceptors and blocks postsynaptic 5-HT2, 5-HT3, and H1 receptors, and its efficacy in major depressive disorder is well established.

Ohdo syndrome and its variants, however, are congenital disorders caused by pathogenic variants in chromatin-regulator genes (e.g. *KAT6A*, *KAT6B*, *MED12*), presenting with intellectual disability and blepharophimosis. There is no known pathophysiological overlap between this genetic developmental disorder and mirtazapine's monoaminergic mechanism.

The TxGNN score most likely reflects an indirect knowledge-graph connection — such as a shared "intellectual disability / behavioral symptom" node, possibly linked through symptomatic use of antidepressants for comorbid sleep or mood disturbances in affected patients — rather than a mechanistically grounded therapeutic hypothesis. This assessment is consistent with the model's own rationale field, which explicitly flags the link as lacking direct relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Mirtazapine holds 8 active registrations in Malaysia (market status: 已上市 / Marketed). Detailed licence-level data (registration numbers, product names, dosage forms, approved indication text) was not returned in this evidence pack and requires a separate NPRA lookup.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and DDI data were not available for this evaluation — this is flagged as a Blocking data gap (DG001) and must be resolved before any safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three top predictions (Ohdo syndrome and variants, blepharophimosis-intellectual disability syndrome Ohdo type, benign paroxysmal torticollis of infancy) are rare congenital/pediatric conditions with L5 evidence — model prediction only, zero clinical trials, zero literature, and no plausible mechanistic link to mirtazapine's known pharmacology. Two of the three candidate diseases predominantly affect infants, a population where mirtazapine has no established safety profile.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed drugbank MOA data (DG002)
- A genuine mechanistic hypothesis linking mirtazapine to chromatin-regulation or channelopathy pathways, if pursued further
- Given the current evidence profile, recommend deprioritizing this candidate in favor of higher-scoring, evidence-backed predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

