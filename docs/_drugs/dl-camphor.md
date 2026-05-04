---
layout: default
title: Dl-Camphor
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 0
---

# Dl-Camphor
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

# DL-Camphor: Drug Repurposing Evaluation Report

## One-Sentence Summary

DL-Camphor is a topical agent marketed in Malaysia with 9 registered products, commonly used as a counterirritant and mild analgesic. The TxGNN model has **no predicted new indications** for this compound, and critical data gaps exist in mechanism of action, approved indication text, and safety information.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (license indication text missing) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No prediction to evaluate |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There is **no TxGNN prediction to evaluate** for DL-Camphor. The model returned an empty predicted indications list, which may be attributable to one or more of the following factors:

1. **Missing DrugBank ID**: DL-Camphor could not be mapped to a DrugBank identifier (`drugbank_id: null`). The TxGNN knowledge graph relies on DrugBank nodes to anchor drug entities; without a valid mapping, the model cannot generate predictions. This is the most likely root cause.

2. **Limited knowledge graph coverage**: DL-Camphor is a racemic mixture of d-camphor and l-camphor. It is primarily used as an excipient or in over-the-counter topical preparations. Such compounds may have limited representation in the TxGNN knowledge graph, which is weighted toward prescription therapeutics with well-characterized molecular targets.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, DL-Camphor is a cyclic monoterpene ketone that acts on TRPV1 and TRPV3 receptors, producing a sensation of coolness and mild local analgesia. Its therapeutic profile is predominantly topical, which further limits systemic repurposing opportunities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no TxGNN prediction was generated to search against.

---

## Literature Evidence

Currently no related literature available — no TxGNN prediction was generated to search against.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (not provided) | (not provided) | (not provided) | (not provided) |
| (not provided) | (not provided) | (not provided) | (not provided) |
| (not provided) | (not provided) | (not provided) | (not provided) |
| (not provided) | (not provided) | (not provided) | (not provided) |
| (not provided) | (not provided) | (not provided) | (not provided) |

> **Note:** 9 registrations were identified by the NPRA query, but license details (authorization numbers, product names, dosage forms, and indication text) were not populated in the evidence pack. This data gap must be resolved before any further evaluation.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, drug interactions) are currently missing. No drug–drug interactions were found in the DrugBank query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing prediction was generated for DL-Camphor, most likely because the compound lacks a DrugBank ID mapping. Without a prediction, there is no candidate indication to evaluate. Additionally, multiple critical data gaps (MOA, indication text, safety profile) prevent meaningful assessment.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping** — Investigate whether DL-Camphor (or its individual enantiomers d-camphor / l-camphor) has a DrugBank entry (e.g., DB01744 for Camphor) and re-run the mapping pipeline
- **Populate NPRA license details** — Retrieve authorization numbers, product names, dosage forms, and approved indication text for all 9 registered products
- **Obtain safety data** — Download and parse package inserts from the NPRA database to populate warnings, contraindications, and interaction profiles
- **Obtain MOA data** — Query DrugBank or PubChem for pharmacological mechanism details
- **Re-run TxGNN prediction** — Once DrugBank ID is resolved, re-execute the knowledge graph and deep learning prediction pipeline

---

### Data Gap Summary

| Gap ID | Item | Severity | Recommended Source |
|--------|------|----------|--------------------|
| DG001 | NPRA package insert warnings/contraindications | **Blocking** | NPRA website — download and parse PDF |
| DG002 | Mechanism of Action (MOA) | High | DrugBank API query |
| — | License detail fields (all empty) | High | NPRA database re-query |
| — | DrugBank ID mapping | **Blocking** | DrugBank search for "Camphor" (DB01744) |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

