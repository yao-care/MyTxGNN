---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone-class antibacterial agent marketed in Malaysia (21 registrations); specific approved indication wording was not included in this evidence pack.
The TxGNN model's top-ranked prediction is **Hyperamylasemia**, with a raw score of 99.98%, but this candidate is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory data provided (moxifloxacin is a fluoroquinolone antibacterial; general indications for this class include respiratory, skin/soft-tissue and intra-abdominal bacterial infections, not confirmed from this pack) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 21 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known information, moxifloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV; its established efficacy is in bacterial infections, not in pancreatic or metabolic disease.

The evidence pack's own mechanistic assessment for this candidate states there is **no known biological pathway** linking moxifloxacin's antibacterial mechanism to hyperamylasemia (pancreatic amylase elevation). The high TxGNN score most likely reflects proximity between nodes in the knowledge graph rather than a plausible pharmacological relationship. No clinical trials, no ICTRP-registered trials, and no PubMed literature were found linking these two entities.

Because the score is high but entirely unsupported by mechanism or empirical evidence, this candidate should be treated as a pure model output requiring independent biological validation before any further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

NPRA records confirm 21 active registrations and "Marketed" status for moxifloxacin, but license number, product name, dosage form and approved-indication text were not populated in this evidence pack, so a per-product table cannot be produced. This is tracked as a Blocking data gap (DG001) affecting downstream safety review.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction reaches Evidence Level L5 (model prediction only) — no clinical trials, no literature, and no identifiable mechanistic link between moxifloxacin's antibacterial activity and hyperamylasemia. A high TxGNN score alone is not sufficient grounds to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently blocking safety screening, DG001)
- Confirmed mechanism of action data for moxifloxacin (DG002)
- Preclinical or mechanistic evidence connecting fluoroquinolone antibacterials to pancreatic amylase regulation
- Original approved indication text from the regulatory license record, to properly assess indication-to-indication plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

