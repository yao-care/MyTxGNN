---
layout: default
title: Bilastine
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 0
---

# Bilastine
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

# Bilastine: Drug Repurposing Evaluation — Awaiting Predictions

## One-Sentence Summary

Bilastine is a second-generation H1-antihistamine registered in Malaysia with 5 active authorizations, primarily used for symptomatic treatment of allergic rhinitis and urticaria. The TxGNN model has **not yet generated any predicted new indications** for this drug. **No clinical trial or literature evidence** has been collected for repurposing candidates, and critical data gaps remain.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data |
| Predicted New Indication | None (no TxGNN predictions generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction not yet available |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack. Based on known pharmacological information, Bilastine is a second-generation, non-sedating H1-antihistamine that selectively blocks peripheral histamine H1 receptors. It is clinically used for the symptomatic relief of allergic rhinoconjunctivitis and urticaria (hives).

No TxGNN predictions have been generated for Bilastine at this time. This may be due to incomplete mapping between the drug's DrugBank ID (DB11591) and nodes in the TxGNN knowledge graph, or the drug may not have met the scoring thresholds for any candidate disease indications. Without predictions, no mechanistic plausibility assessment can be performed.

Before a repurposing evaluation can proceed, the TxGNN prediction pipeline must be re-run or debugged to determine why no candidate indications were produced for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for repurposing candidates, as no new indications have been predicted.

---

## Literature Evidence

Currently no related literature available for repurposing candidates, as no new indications have been predicted.

---

## Malaysia Market Information

5 authorizations are recorded in the NPRA database, but detailed product information has not yet been populated in the evidence pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(Data pending)* | *(Data pending)* | *(Data pending)* | *(Data pending)* |

> **Note:** License detail fields are currently empty. Please retrieve full product information from the [NPRA Quest3+ database](https://quest3plus.bpfk.gov.my/) to complete this section.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gaps Identified:**
> - TFDA/NPRA package insert warnings and contraindications have not been parsed (Severity: **Blocking** — cannot proceed to Stage 1 safety assessment)
> - Drug–drug interaction data not found in current query

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications exist for Bilastine at this time, and multiple blocking data gaps prevent evaluation from proceeding. The evidence pack lacks MOA data, approved indication text, package insert safety information, and — most critically — any repurposing predictions to evaluate.

**To proceed, the following is needed:**

1. **Re-run TxGNN prediction pipeline** — Verify that Bilastine (DB11591) is correctly mapped in the knowledge graph (`node.csv` / `kg.csv`) and re-execute `run_kg_prediction.py` to generate candidate indications
2. **Populate NPRA license details** — Retrieve product names, dosage forms, and approved indication text from the NPRA Quest3+ database for all 5 registrations
3. **Obtain MOA data** — Query DrugBank API for Bilastine's mechanism of action, targets, and pharmacodynamics
4. **Parse package insert** — Download and extract warnings, contraindications, and adverse reactions from the official package insert (Blocking severity — required for Stage 1 safety assessment)
5. **Query DDI databases** — Re-attempt drug–drug interaction search once DrugBank data is fully integrated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

