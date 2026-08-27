---
layout: default
title: Omidenepag Isopropyl
parent: 僅模型預測 (L5)
nav_order: 521
evidence_level: L5
indication_count: 7
---

# Omidenepag Isopropyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Omidenepag Isopropyl: From Ocular Hypertension/Glaucoma to Pancreatitis

## One-Sentence Summary

Omidenepag isopropyl is a selective EP2 (prostaglandin E2 receptor subtype 2) agonist used as a topical ophthalmic agent for glaucoma and ocular hypertension. The TxGNN model predicts it may be effective for **pancreatitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on knowledge-graph similarity with no mechanistic or clinical evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension (per embedded rationale notes; not confirmed in NPRA license text — license indication fields are blank) |
| Predicted New Indication | Pancreatitis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omidenepag isopropyl acts as a selective EP2 receptor agonist: activation raises intracellular cAMP, relaxing the ciliary muscle and trabecular meshwork to increase aqueous humor outflow. This is the accepted mechanism behind its approved use in glaucoma and ocular hypertension.

The link to pancreatitis is speculative. EP2 signaling via the PGE2-EP2-cAMP axis has been reported to modulate inflammatory responses in some tissues, but the direction of that effect (pro- vs anti-inflammatory) varies by tissue and context, and there is no pancreas-specific data supporting a role here. In addition, omidenepag isopropyl is administered as a topical eye drop with very low systemic exposure, which further weakens any plausible extrapolation to a systemic/visceral organ effect.

In short: this is a case where the TxGNN embedding similarity picked up a distant, unproven signal rather than a mechanistically grounded relationship. The evidence pack itself flags this prediction as "purely a knowledge-graph similarity inference, without mechanistic evidence."

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

NPRA records confirm the drug is marketed in Malaysia with **2 active registrations**, but the evidence pack does not include populated product-level fields (registration number, product name, dosage form, or approved indication text) for these licenses — this data will need to be pulled directly from the NPRA registry before it can be reported.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: safety label data — key warnings and contraindications — is flagged as a **Blocking** data gap in this evidence pack (DG001), meaning it is not yet available and prevents this candidate from proceeding to the S1 safety review stage.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pancreatitis prediction is L5 evidence — a TxGNN model score with zero clinical trials, zero literature, and no plausible direct mechanistic pathway. Independently, a blocking data gap on TFDA/NPRA label warnings and contraindications means the candidate cannot yet even enter formal safety screening.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — resolves blocking gap DG001
- Confirmed original indication and DrugBank-sourced MOA documentation (currently reconstructed only from embedded rationale text, not a primary source)
- Preclinical or mechanistic studies establishing an EP2–pancreatic inflammation pathway before any clinical evidence-gathering is warranted
- Malaysia registration details (product name, dosage form, approved indication text) for the 2 existing NPRA licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

