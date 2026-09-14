---
layout: default
title: Urofollitropin
parent: 僅模型預測 (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
---

# Urofollitropin
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

# Urofollitropin: From Fertility Treatment to Migraine Disorder

## One-Sentence Summary

Urofollitropin (DrugBank DB00094) is a purified urine-derived FSH preparation; this evidence pack does not contain its formally registered indication text or mechanism-of-action data, though FSH preparations of this class are generally used for ovulation induction in fertility treatment. The TxGNN model predicts potential efficacy for **Migraine Disorder** (score **99.85%**), but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug-level mechanistic rationale supplied alongside the prediction is weak to contradictory rather than supportive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extracted from Malaysia licenses in this evidence pack (data gap); FSH preparations of this class are generally used for ovulation induction / female infertility |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for urofollitropin in this evidence pack. Based on known information, urofollitropin is a purified urinary-derived follicle-stimulating hormone (FSH) preparation that acts on FSH receptors on ovarian granulosa cells to promote follicular development — a reproductive endocrine mechanism.

Migraine disorder involves an entirely different physiological system, centered on trigeminovascular activation and CGRP-mediated neurovascular signaling. Per the drug-level rationale accompanying this prediction, there is no known direct physiological link between exogenous FSH administration and migraine pathophysiology. The TxGNN score may instead reflect an indirect graph-embedding association — for example, known links between estrogen fluctuation and migraine susceptibility — rather than a genuine treatment mechanism for FSH itself.

Notably, the supplied rationale flags a potential **directional concern**: exogenous FSH commonly amplifies estrogen fluctuation, which could theoretically provoke or worsen migraine rather than treat it. The same directional mismatch appears across the other top-ranked predictions in this evidence pack (e.g., restless legs syndrome, POTS), where hormonal fluctuation is associated with symptom *worsening* in the literature, not therapeutic benefit. Combined with the complete absence of clinical trials or literature specifically linking urofollitropin to migraine, the mechanistic case for this prediction is not currently persuasive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Malaysia regulatory records show **5 registered licenses** for urofollitropin (market status: 已上市 / Marketed), but this evidence pack does not include the detailed authorization number, product name, dosage form, or approved-indication text for any of these licenses (data gap).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and drug-interaction data were all flagged as data gaps in this evidence pack — including a **Blocking**-severity gap on TFDA/NPRA label warnings and contraindications, which prevents a full S1 safety screen.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction sits at the lowest evidence tier (L5) with zero supporting clinical trials or literature, and the supplied mechanistic rationale is weak-to-contradictory (exogenous FSH may plausibly worsen rather than treat migraine via estrogen fluctuation). Combined with a **Blocking** data gap on TFDA/NPRA safety labeling, this candidate cannot proceed past initial screening (S0/S1) at this time.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data from DrugBank or equivalent source (High-priority gap, DG002)
- Complete license/authorization details (product name, dosage form, approved indication text) for the 5 Malaysia registrations
- At minimum, preclinical or mechanistic evidence directly connecting FSH signaling to migraine pathophysiology before this candidate can be re-scored above L5
- Re-evaluation should also consider the directional risk (potential migraine aggravation) rather than treating the TxGNN score alone as evidence of therapeutic benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

