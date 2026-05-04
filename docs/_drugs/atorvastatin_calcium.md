---
layout: default
title: Atorvastatin Calcium
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Atorvastatin Calcium: Drug Repurposing Assessment — TxGNN Prediction Data Pending

## One-Sentence Summary

Atorvastatin Calcium is a widely-used statin originally indicated for hyperlipidaemia and cardiovascular risk reduction via HMG-CoA reductase inhibition.
The current Evidence Pack does **not contain TxGNN prediction output** — the `predicted_indications` array is empty — meaning no new repurposing indication can be evaluated at this time.
With **71 registered products** in Malaysia and key safety and MOA data still outstanding, the repurposing evaluation is **blocked** until upstream data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperlipidaemia / Cardiovascular risk reduction (well-established; TFDA indication text not yet retrieved) |
| Predicted New Indication | — *(No TxGNN output available)* |
| TxGNN Prediction Score | — *(Pending)* |
| Evidence Level | — *(Cannot be determined)* |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 71 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

TxGNN prediction data is not yet available in this Evidence Pack (`predicted_indications: []`), so no mechanism-to-indication bridging analysis can be performed at this stage.

From established pharmaceutical knowledge, atorvastatin is an HMG-CoA reductase inhibitor (statin). Beyond lipid-lowering, statins are widely researched for pleiotropic effects — including anti-inflammatory, anti-proliferative, and neuroprotective properties — which have driven repurposing hypotheses in areas such as neurodegenerative disease, sepsis, and certain cancers. However, these hypotheses **cannot be confirmed or scored** without the TxGNN model output.

Formal mechanism-to-indication analysis will be completed once the TxGNN prediction pipeline is executed and DrugBank MOA data is retrieved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

*Note: This reflects missing `predicted_indications` data — not the absence of real-world trial activity for atorvastatin. Once a target indication is identified by TxGNN, a ClinicalTrials.gov search should be conducted.*

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

*Note: Same reason as above — literature evidence retrieval is tied to a specific predicted indication, which is not yet available.*

---

## Malaysia Market Information

The Evidence Pack confirms **71 registered products** for ATORVASTATIN CALCIUM in Malaysia. However, individual product details (authorization number, product name, dosage form, approved indication) were not returned in the current data pull.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* |

> **Action Required:** Re-run the NPRA/BPFK query with full licence-level detail retrieval. With 71 registrations confirmed, this data should be accessible.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug-drug interactions) returned as data gaps or were not found in the current query. A TFDA/NPRA package insert (PIL/SmPC) retrieval is required before any safety-gated decision can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The core repurposing analysis cannot proceed because the TxGNN prediction pipeline has not returned output for this candidate, and two blocking data gaps (safety/MOA) remain unresolved. The drug is well-established in the market (71 Malaysia registrations), so regulatory feasibility is strong once a prediction target is confirmed.

**To proceed, the following is needed:**

- [ ] **[DG001 — Blocking]** Retrieve TFDA/NPRA package insert: download SmPC/PIL PDF from the NPRA official portal and parse key warnings and contraindications
- [ ] **[DG002 — High]** Retrieve DrugBank MOA: query DrugBank API using the resolved DrugBank ID (TFDA → DrugBank ID mapping was attempted; ensure the mapping result is written to `drug.drugbank_id`)
- [ ] **[Critical]** Execute TxGNN prediction pipeline for ATORVASTATIN CALCIUM to populate `predicted_indications` — this is the prerequisite for the entire repurposing evaluation
- [ ] Retrieve full NPRA licence-level details (product name, dosage form, indication text) for the 71 registered products
- [ ] Re-run DDI query after DrugBank ID is confirmed (current `query_status: not_found` likely due to missing DrugBank ID linkage)

Once the above are resolved, this report should be regenerated with Evidence Pack v5.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

