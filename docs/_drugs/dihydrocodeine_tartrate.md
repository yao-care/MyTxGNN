---
layout: default
title: Dihydrocodeine Tartrate
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 0
---

# Dihydrocodeine Tartrate
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

# Dihydrocodeine Tartrate: Drug Repurposing Evaluation

## One-Sentence Summary

Dihydrocodeine Tartrate is a semi-synthetic opioid derivative, currently marketed in Malaysia with 3 registered products. The TxGNN model **has not generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps in regulatory details, mechanism of action, and safety information, precluding a meaningful repurposing assessment at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | (Registration details unavailable — see Data Gaps below) |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There is **no TxGNN prediction to evaluate** for Dihydrocodeine Tartrate at this time. The predicted indications list is empty, meaning the model either did not identify a viable repurposing candidate or the drug could not be mapped to the knowledge graph (no DrugBank ID was resolved in the evidence pack).

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, Dihydrocodeine is a semi-synthetic opioid analgesic structurally related to codeine. It acts primarily as a μ-opioid receptor agonist and is typically used for moderate pain relief and as an antitussive (cough suppressant). Without a confirmed DrugBank mapping and TxGNN knowledge graph linkage, the model cannot generate repurposing predictions.

Before any repurposing analysis can proceed, the foundational data gaps — particularly the DrugBank ID mapping and mechanism of action — must be resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication to query against).

---

## Literature Evidence

Currently no related literature available (no predicted indication to query against).

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (unavailable) | (unavailable) | (unavailable) | (unavailable) |
| (unavailable) | (unavailable) | (unavailable) | (unavailable) |
| (unavailable) | (unavailable) | (unavailable) | (unavailable) |

> **Note:** 3 registrations were confirmed via NPRA query (2026-03-27), but detailed licence information (product names, dosage forms, approved indications) was not populated in the evidence pack. This data needs to be re-collected from the NPRA database.

---

## Safety Considerations

> Please refer to the package insert for safety information. The current evidence pack does not contain resolved warnings, contraindications, or drug interaction data for Dihydrocodeine Tartrate. As an opioid analgesic, standard opioid precautions (respiratory depression, dependence potential, CNS depression with concurrent sedatives) should be assumed pending formal data collection.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions exist for Dihydrocodeine Tartrate, and multiple critical data gaps (DrugBank ID, MOA, regulatory details, safety profile) prevent any meaningful evaluation. The candidate cannot advance without foundational data.

**To proceed, the following is needed:**

1. **Resolve DrugBank ID mapping** — Query DrugBank for "Dihydrocodeine" (DB01955 is the expected ID) and confirm the knowledge graph linkage
2. **Retrieve mechanism of action (MOA)** from DrugBank or primary pharmacology references
3. **Re-collect NPRA registration details** — Licence numbers, product names, dosage forms, and approved indication text for all 3 registrations
4. **Collect safety data** — Package insert warnings, contraindications, and drug-drug interactions (particularly CNS depressants, MAOIs, and CYP2D6 inhibitors)
5. **Re-run TxGNN prediction pipeline** once DrugBank mapping is established, to determine if viable repurposing candidates emerge

---

*This report is for research reference only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

