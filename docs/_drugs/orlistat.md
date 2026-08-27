---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 522
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is a pancreatic lipase inhibitor originally used for weight management in obesity. The TxGNN model predicts a possible link to **Hypervitaminosis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanism argues more naturally against this indication than for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity / weight management (based on known drug information — TFDA license indication text not available in current data) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Taiwan Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack (data gap). Based on known information, orlistat is a pancreatic lipase inhibitor: it blocks intestinal hydrolysis of triglycerides and reduces dietary fat absorption by approximately 30%, which is the basis of its use in obesity/weight management.

This mechanism is mechanistically closer to **hypovitaminosis** than to hypervitaminosis: reduced fat absorption also reduces absorption of fat-soluble vitamins (A, D, E, K), which is a well-documented adverse effect of orlistat, not a treatment effect. The only theoretically defensible link to hypervitaminosis is indirect — in a patient with fat-soluble vitamin toxicity (e.g., vitamin A or D overdose), orlistat's blockade of fat absorption could in principle blunt further intestinal uptake of the offending vitamin. This is a speculative, off-label mechanism with no direct literature support for treating hypervitaminosis as an indication.

The high TxGNN score (99.42%) most likely reflects the knowledge graph's proximity between orlistat and fat-soluble-vitamin-metabolism nodes, rather than a validated therapeutic relationship. This prediction should be treated as a graph-topology artifact requiring independent confirmation, not a mechanistically well-supported repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Orlistat is marketed in Taiwan (TFDA) with 2 registered licenses. Detailed license information (product names, dosage forms, manufacturers, approved indication text) is not available in the current data pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only candidate with zero clinical trials or literature support. The repurposing rationale itself is mechanistically weak — orlistat's known pharmacology (reduced fat-soluble vitamin absorption) points toward causing hypovitaminosis, not treating hypervitaminosis, so the high TxGNN score is more likely a graph-proximity artifact than a real signal.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001); required before any S1 safety screening
- Confirmed mechanism of action (MOA) data from DrugBank (High-severity data gap, DG002)
- Independent literature/pharmacology review specifically addressing whether orlistat can reduce absorption of an already-ingested/circulating fat-soluble vitamin, since no clinical trials or publications currently exist for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

