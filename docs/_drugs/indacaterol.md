---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From COPD to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is a long-acting β2-adrenergic receptor agonist (LABA) originally used for chronic obstructive pulmonary disease. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this direction currently has **0 clinical trials** and **0 publications** supporting it, and no plausible receptor-level mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD) — inferred from known drug class (LABA); formal TFDA/NPRA approved-indication text is a data gap |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, indacaterol is a long-acting β2-adrenergic receptor agonist (LABA); its efficacy in COPD (and, in combination products, asthma) is well established, acting by stimulating β2-receptors on bronchial smooth muscle to produce bronchodilation.

Nephrogenic Syndrome of Inappropriate Antidiuresis is caused by a gain-of-function mutation in the vasopressin V2 receptor, a pathway with no known crosstalk to β2-adrenergic signaling. The evidence pack's own mechanistic review states there is "no known interaction pathway" and "no mechanistic plausibility" between indacaterol's target and this disease.

In other words, this candidate is driven purely by the TxGNN model's score (99.54%, network rank 6872) without any supporting biological rationale, clinical trial, or literature. Within the same evidence pack, a lower-ranked candidate for this drug — bronchial disease — actually has strong clinical support (L1, 37 trials, 20 publications), but that mainly re-discovers indacaterol's already-known indication rather than representing new repurposing value; it is not part of this report's designated candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Malaysia has 6 active drug registrations for indacaterol (market status: Marketed). Per-registration details (authorization number, product name, dosage form, approved indication text) are not available in the current data extract.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence for indacaterol in NSIAD, and no plausible mechanistic link exists between β2-adrenergic receptor agonism and the V2-receptor-driven pathology of this syndrome. The prediction rests solely on the TxGNN model score (L5).

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for indacaterol
- TFDA/NPRA approved-indication text and full license detail for the 6 Malaysia registrations
- Preclinical/in vitro pharmacology evidence exploring any indirect link between β2-adrenergic signaling and AVP/V2 receptor regulation
- Package insert safety data (key warnings, contraindications, DDI), currently unavailable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

