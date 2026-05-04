---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 1
---

# Adapalene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Adapalene: From Acne Vulgaris to Zinc, Elevated Plasma

## One-Sentence Summary

Adapalene is a third-generation synthetic retinoid, originally approved for the topical treatment of acne vulgaris.
The TxGNN model predicts it may have potential relevance to **Zinc, Elevated Plasma (hyperзincaemia)**,
with a high model prediction score of **99.51%**; however, **no clinical trials and no published literature** currently support this direction — making this a purely computational signal requiring substantial further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (topical retinoid) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Adapalene is a third-generation naphthoic acid-derived retinoid that selectively binds to retinoic acid receptors RAR-β and RAR-γ. In acne treatment, it exerts its effects by normalising keratinocyte differentiation, reducing follicular hyperkeratinisation, and suppressing inflammatory mediators. Importantly, retinoids and zinc metabolism are known to interact at a biological level: zinc is an essential cofactor for the synthesis of retinol-binding protein (RBP), which is responsible for transporting vitamin A in the blood; conversely, retinoic acid receptors (RARs) may regulate the expression of zinc transporter family genes (ZnT/ZIP family), theoretically influencing systemic zinc homeostasis.

The TxGNN prediction score of 0.995 is remarkably high. However, this most likely reflects the topological proximity of "retinoids" and "zinc metabolism" nodes within the knowledge graph, rather than a true therapeutic signal. The knowledge graph encodes known biological associations — in this case, the well-documented retinol–zinc axis — which the model interprets as a potential therapeutic link. This is a known limitation of graph-based prediction: mechanistic adjacency does not equate to therapeutic efficacy.

Currently, detailed mechanism of action data for Adapalene is not available in this Evidence Pack. Based on known pharmacology, Adapalene is a selective RAR-β/γ agonist. While a theoretical mechanistic link to zinc homeostasis can be constructed via the retinoid–RBP–zinc axis, this connection is highly speculative and has not been tested clinically. No evidence currently supports Adapalene as a treatment for elevated plasma zinc.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

5 product registrations are confirmed via NPRA (Malaysia National Pharmaceutical Regulatory Agency) as of 2026-03-27. However, detailed product-level information (authorization numbers, product names, dosage forms, and approved indication text) was not retrievable in the current dataset pull.

> **Note:** Adapalene is globally well-established as a topical gel/cream (0.1% and 0.3%) for acne vulgaris. Malaysia-registered products are expected to follow this profile. Please consult the NPRA Product Registration database directly for full authorisation details.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug interactions) were not available in this Evidence Pack. Given that Adapalene is a topical retinoid, prescribers should be aware of the general retinoid class precautions, including avoidance in pregnancy (teratogenicity risk class), sensitivity to sunlight, and potential for local skin irritation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns Adapalene an unusually high prediction score (99.51%) for elevated plasma zinc; however, this is an **L5 evidence finding** — supported solely by a computational model with zero corroborating clinical trials or published literature. The predicted indication ("zinc, elevated plasma") is a laboratory finding rather than a primary disease entity, and no plausible clinical development pathway currently exists for this application.

**To proceed, the following would be needed:**

- **Mechanistic validation**: Preclinical (in vitro / in vivo) studies directly assessing Adapalene's effect on plasma zinc levels or zinc transporter expression
- **Safety data retrieval**: Download and parse the TFDA/NPRA package insert PDFs to populate key warnings and contraindications (currently a Blocking data gap)
- **MOA data**: Query DrugBank API for full pharmacodynamic and pharmacokinetic profile (currently a High-severity data gap)
- **Disease re-assessment**: Evaluate whether "zinc, elevated plasma" represents a clinically actionable condition amenable to pharmacological intervention with a retinoid
- **Expert review**: Consult a pharmacologist or endocrinologist to assess biological plausibility before any resource investment in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

