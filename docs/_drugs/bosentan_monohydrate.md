---
layout: default
title: Bosentan Monohydrate
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 0
---

# Bosentan Monohydrate
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

# Bosentan Monohydrate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bosentan is an endothelin receptor antagonist (ERA) primarily indicated for pulmonary arterial hypertension (PAH). The current Evidence Pack contains **no predicted new indications** from the TxGNN model, and critical data gaps (DrugBank ID, MOA, approved indication text, safety data) must be resolved before any repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Bosentan Monohydrate |
| Original Indication | *(Not provided in evidence pack — see Data Gaps below)* |
| Predicted New Indication | **None** (no TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | **N/A** — No prediction to evaluate |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 5 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There is **no TxGNN-predicted indication** in this Evidence Pack, so a mechanism-based plausibility assessment cannot be performed at this time.

Based on general pharmaceutical knowledge, Bosentan Monohydrate is a dual endothelin receptor antagonist (ET~A~ and ET~B~) that blocks the vasoconstrictive and proliferative effects of endothelin-1. It is well established in the treatment of pulmonary arterial hypertension (PAH) and has also been approved in some jurisdictions for reducing the number of new digital ulcers in systemic sclerosis patients. However, this mechanistic context is not sourced from the Evidence Pack itself, and the `original_moa` field remains unresolved.

Before any repurposing candidates can be evaluated, the TxGNN prediction pipeline must be run with a valid DrugBank ID mapping for Bosentan, and the resulting predicted indications must be populated into the evidence pack.

---

## Clinical Trial Evidence

Currently no predicted indication is available; therefore, no targeted clinical trial search was conducted.

---

## Literature Evidence

Currently no predicted indication is available; therefore, no targeted literature search was conducted.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |

> **Note:** 5 registrations were found via NPRA query (2026-03-27), but the license detail fields (authorization number, product name, dosage form, approved indication) were not populated. This data needs to be re-fetched from the NPRA database.

---

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, drug interactions) are currently unresolved in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is incomplete — there are no TxGNN-predicted indications, no DrugBank ID mapping, no mechanism of action data, and no populated license or safety details. A repurposing evaluation cannot proceed until these foundational data gaps are resolved.

**To proceed, the following is needed:**

1. **DrugBank ID Resolution** — Map "BOSENTAN MONOHYDRATE" to its DrugBank ID (expected: **DB00559**) so the TxGNN knowledge graph can link it to disease nodes
2. **TxGNN Prediction Execution** — Re-run the KG and/or DL prediction pipeline with the corrected DrugBank mapping to generate `predicted_indications`
3. **NPRA License Detail Population** — Re-query the NPRA database to populate authorization numbers, product names, dosage forms, and approved indication text for all 5 registrations
4. **MOA Data Retrieval** — Query DrugBank API for the mechanism of action (endothelin receptor antagonism)
5. **Safety Data Collection** — Extract key warnings, contraindications, and drug–drug interactions from the package insert or DrugBank
6. **Evidence Collection** — Once a predicted indication is available, run ClinicalTrials.gov, PubMed, and ICTRP collectors for supporting evidence

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

