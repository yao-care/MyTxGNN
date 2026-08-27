---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 3
---

# Colchicine
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

# Colchicine: From Unspecified Original Indication to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine (DrugBank DB01394) is a marketed drug in Malaysia with 7 active product registrations, though the specific original approved indication text is not available in the current data extract. The TxGNN model predicts a possible new application for **Plasmodium falciparum malaria**, but this prediction is currently supported by **no clinical trials and no published literature**, placing it at the lowest evidence tier.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current registry data extract |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for colchicine is not available in the source dataset (flagged as a High-severity data gap). Based on the mechanistic rationale associated with this prediction, colchicine is a **tubulin polymerization inhibitor**. *Plasmodium falciparum*'s schizogony (asexual replication) and mitotic division also depend on microtubule/cytoskeletal machinery, which provides a theoretical, indirect link between colchicine's known pharmacology and the predicted indication.

However, this link is weak in practice: colchicine does not selectively distinguish between mammalian and parasite tubulin, and it has a narrow therapeutic window (toxic doses are close to effective doses). There is no clinical or preclinical evidence of antimalarial activity for colchicine. The high TxGNN score most likely reflects structural connectivity between tubulin/cytoskeleton-related nodes in the knowledge graph rather than confirmed pharmacological selectivity for the malaria parasite — this is a model-prediction-only signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Colchicine holds **7 active product registrations** with NPRA (market status: Marketed), but license-level details (registration numbers, product names, dosage forms, manufacturers, and approved indication text) are not populated in the current data extract and cannot be reported here.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying warnings/contraindications data point is flagged as a Blocking-severity data gap — TFDA/NPRA label text has not yet been retrieved, which prevents a full safety pre-assessment for this candidate.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction sits at Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the proposed mechanistic link is non-specific and lacks any clinical or preclinical antimalarial data. A Blocking-severity data gap on the drug's own safety labeling further prevents a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap
- The drug's original approved indication(s), currently missing from the registry extract
- Preclinical or in vitro antiparasitic activity data for colchicine before any further evaluation is warranted

---
**Note:** This evidence pack contains two additional predicted indications for colchicine not covered in this report. Notably, **familial Mediterranean fever** (rank 2, score 99.38%) carries **Evidence Level L1** with a "Proceed with Guardrails" recommendation — substantially stronger evidence than the malaria prediction summarized above. If the goal is to identify colchicine's most promising repurposing candidate, a separate report on that indication is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

