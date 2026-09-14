---
layout: default
title: Selumetinib
parent: 僅模型預測 (L5)
nav_order: 610
evidence_level: L5
indication_count: 10
---

# Selumetinib
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

# Selumetinib: From Neurofibromatosis Type 1 (NF1)-Associated Plexiform Neurofibromas to Familial Generalized Lentiginosis

## One-Sentence Summary

Selumetinib is a selective MEK1/2 inhibitor, internationally known and marketed (as Koselugo) for NF1-associated plexiform neurofibromas.
The TxGNN model predicts it may be effective for **Familial Generalized Lentiginosis**, but this is currently a **model-prediction-only** signal — **no clinical trials and no published literature** support this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neurofibromatosis type 1 (NF1)-associated plexiform neurofibromas *(known drug identity; not confirmed by local registration text — see Data Gap DG002)* |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, Selumetinib is a selective MEK1/2 inhibitor acting on the RAS-MAPK signaling pathway, and its efficacy in NF1-associated plexiform neurofibromas has been clinically established.

Familial generalized lentiginosis belongs to the LEOPARD syndrome / Noonan syndrome spectrum, a group of RASopathies. The evidence pack's rationale notes that the disease's characteristic melanocyte proliferation may involve over-activation of the RAS-MAPK pathway — the same pathway targeted by Selumetinib — which provides a plausible theoretical rationale for the model's prediction.

However, this mechanistic link is inferential and not yet backed by any experimental or clinical data. No clinical trials or publications specific to Selumetinib in this indication currently exist, so the biological plausibility described above should be treated as a hypothesis requiring confirmation, not established fact.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Cytotoxicity

*(Selumetinib is classified as an antineoplastic agent — a MEK1/2 protein kinase inhibitor — under its known international drug classification.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Familial Generalized Lentiginosis) has no clinical trial or literature support — evidence level L5, model prediction only. Combined with two blocking/high-severity data gaps (TFDA/NPRA label warnings, and drug MOA), there is currently no basis for an S1 safety review.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking)
- DrugBank-confirmed mechanism of action data (DG002, High)
- Any preclinical or case-level evidence specific to familial generalized lentiginosis or the LEOPARD/Noonan syndrome spectrum
- Confirmation of the drug's originally approved indication from local registration records (currently blank in both license entries)

**Note:** Within this same evidence pack, *peripheral nerve schwannoma* (rank 9) has substantially stronger evidence — a completed Phase 2 trial and 7 supporting publications (evidence level L2, decision stage S2, "Research Question") — and may warrant separate, prioritized evaluation ahead of the top-ranked candidate above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

