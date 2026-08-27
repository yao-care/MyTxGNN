---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 1
---

# Carbocisteine
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

# Carbocisteine: From Respiratory Mucus Hypersecretion to Gout

## One-Sentence Summary

Carbocisteine is a mucolytic (mucoactive) agent conventionally used to reduce the viscosity of respiratory secretions in productive cough and airway mucus hypersecretion. The TxGNN model predicts a possible effect in **Gout**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on knowledge-graph embedding similarity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Respiratory mucus hypersecretion / productive cough (mucolytic) — not sourced from this data pack; Malaysia licence indication texts were not provided |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, carbocisteine belongs to the mucolytic/mucoactive drug class, and its efficacy in reducing sputum viscosity for respiratory conditions is well established; some literature also attributes mild antioxidant and anti-inflammatory properties to it, but this has not been formally captured in this evidence pack.

Gout is fundamentally a purine-metabolism and urate-handling disorder — driven by urate transporters (e.g., URAT1, ABCG2) and NLRP3 inflammasome activation in response to monosodium urate crystal deposition. There is no known overlap between the mucolytic mechanism of carbocisteine and any of these gout-specific pathways.

No mechanistic link, clinical trial, or publication currently connects carbocisteine to gout. The prediction most likely reflects an indirect topological association in the knowledge graph (e.g., shared co-prescription or comorbidity patterns with other anti-inflammatory agents) rather than a genuine pharmacological relationship. This is consistent with the L5 evidence level and the model's own "Hold" recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Carbocisteine holds 18 active registrations in Malaysia (market status: marketed). Licence-level details (registration numbers, product names, dosage forms, approved indication texts) were not populated in this data pack and cannot be listed here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure TxGNN embedding-similarity prediction (L5) with no clinical trials, no supporting literature, and no identifiable mechanistic overlap between carbocisteine's mucolytic action and gout pathophysiology. Combined with missing MOA and safety data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert — warnings, contraindications (blocking gap, DG001)
- DrugBank mechanism of action data (DG002)
- Preclinical or mechanistic studies establishing any plausible link between mucolytic activity and urate metabolism / NLRP3 inflammasome pathways
- Malaysia licence-level product detail (registration numbers, indication texts) for market verification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

