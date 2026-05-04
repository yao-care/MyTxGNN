---
layout: default
title: Baloxavir Marboxil
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 0
---

# Baloxavir Marboxil
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

# Baloxavir Marboxil: Drug Repurposing Evaluation Report

## One-Sentence Summary

Baloxavir marboxil (Xofluza) is a cap-dependent endonuclease inhibitor originally developed for the treatment of influenza. The TxGNN model **did not generate any predicted new indications** for this drug, and the Evidence Pack contains significant data gaps in regulatory details, mechanism of action, and safety information.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (licence detail not provided in data source) |
| Predicted New Indication | — (No prediction generated) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction or supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There is **no TxGNN-predicted new indication** for Baloxavir marboxil in this Evidence Pack. The `predicted_indications` array is empty, meaning the model either did not identify a sufficiently confident repurposing candidate or the drug was not successfully mapped to the knowledge graph for prediction.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on publicly known information, Baloxavir marboxil is a selective inhibitor of the cap-dependent endonuclease of the influenza virus polymerase acidic (PA) protein. It blocks viral mRNA synthesis at an early stage of infection, representing a distinct mechanism from neuraminidase inhibitors (e.g., oseltamivir). Its specificity for the influenza polymerase may limit the breadth of repurposing opportunities identifiable by the knowledge graph approach.

Without a predicted indication, no mechanism-based plausibility assessment can be performed at this time.

---

## Clinical Trial Evidence

Currently no predicted indication has been generated; therefore, no targeted clinical trial search was conducted.

---

## Literature Evidence

Currently no predicted indication has been generated; therefore, no targeted literature search was conducted.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Not provided) | (Not provided) | (Not provided) | (Not provided) |

> **Note:** The NPRA query confirmed 1 registration for Baloxavir marboxil in Malaysia, but the licence details (authorization number, product name, dosage form, and approved indication text) were not populated in the Evidence Pack. This data gap should be remediated by querying the [NPRA Quest3+ database](https://quest3plus.bpfk.gov.my/).

---

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, and drug interactions) are currently unavailable in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No new indication was predicted by TxGNN for Baloxavir marboxil. Additionally, critical data gaps exist across regulatory details, mechanism of action, and safety information, making any repurposing assessment premature.

**To proceed, the following is needed:**

1. **Resolve Data Gaps (Blocking):**
   - Obtain NPRA licence details (authorization number, product name, dosage form, approved indication) from the NPRA Quest3+ database
   - Retrieve package insert warnings and contraindications from the Malaysian product label or NPRA records

2. **Resolve Data Gaps (High Priority):**
   - Query DrugBank API for mechanism of action (MOA) data for DB13997
   - Populate `original_indications` field from regulatory or DrugBank sources

3. **Re-run Prediction Pipeline:**
   - Verify that DB13997 (Baloxavir marboxil) is correctly mapped in the TxGNN knowledge graph (`node.csv` / `kg.csv`)
   - If the drug node exists but no edges connect it to disease nodes, investigate whether DrugBank mapping or ingredient normalization failed
   - Re-execute `run_kg_prediction.py` after resolving mapping issues

4. **If Predictions Emerge After Re-run:**
   - Collect clinical trial evidence from ClinicalTrials.gov and ICTRP
   - Collect literature evidence from PubMed
   - Update the Evidence Pack and regenerate this report

---

*This report is for research reference only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

