---
layout: default
title: Dextrose Anhydrous
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 0
---

# Dextrose Anhydrous
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

# Dextrose Anhydrous: Drug Repurposing Evaluation — No Predicted Indications Available

## One-Sentence Summary

Dextrose Anhydrous (anhydrous glucose) is a fundamental nutritional and metabolic agent widely used for caloric supplementation, fluid replacement, and the treatment of hypoglycaemia. The TxGNN model has **not generated any repurposing predictions** for this compound, and critical data gaps (DrugBank ID, mechanism of action, approved indication text) remain unresolved.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (licence indication text not provided) |
| Predicted New Indication | **None** — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions, no studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | **Hold** |

---

## Why Is There No Prediction?

Dextrose Anhydrous is the anhydrous form of D-glucose, the body's primary energy substrate. It is classified as a nutritional agent rather than a pharmacologically active therapeutic drug. Its principal clinical roles — intravenous fluid therapy, caloric supplementation, hypoglycaemia correction, and use as an excipient or vehicle — do not involve a disease-specific pharmacological mechanism that the TxGNN knowledge graph can leverage for repurposing predictions.

Furthermore, the DrugBank ID for this compound was not resolved in the current pipeline (`drugbank_id: null`). Without a valid DrugBank node, the compound cannot be mapped into the TxGNN knowledge graph (which relies on DrugBank–disease edges from `kg.csv`), and therefore no drug–disease prediction scores can be computed.

Additionally, the mechanism of action (MOA) data is unavailable. Dextrose acts as a caloric source metabolised via glycolysis and the citric acid cycle; it does not possess a targeted pharmacological MOA in the conventional sense (e.g., receptor binding, enzyme inhibition), which further limits its candidacy for indication-based repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials to display, as no new indication was predicted by TxGNN.

---

## Literature Evidence

Currently no related literature to display, as no new indication was predicted by TxGNN.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|-------------|-------------|---------------------|
| (Not provided) | (Not provided) | (Not provided) | (Not provided) |

> **Note:** 15 registrations were identified in the NPRA database for Dextrose Anhydrous, but the detailed licence records (authorization number, product name, dosage form, and approved indication text) were not populated in the evidence pack. This data gap should be remediated by re-querying the NPRA database.

---

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, and drug interactions) returned as data gaps in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dextrose Anhydrous is a basic nutritional/metabolic compound with no targeted pharmacological mechanism. The TxGNN model produced zero repurposing predictions, and multiple critical data gaps (DrugBank ID, MOA, licence indication text, safety data) remain unresolved. This compound is not a viable candidate for drug repurposing evaluation at this time.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping**: Verify whether Dextrose Anhydrous maps to DrugBank ID [DB09341](https://go.drugbank.com/drugs/DB09341) (Glucose) or a related entry, and re-run the KG prediction pipeline with the correct node
- **Populate NPRA licence details**: Re-query the NPRA database to retrieve full registration records (authorization numbers, product names, dosage forms, approved indications)
- **Retrieve safety data**: Download and parse the relevant package inserts for warnings, contraindications, and drug interaction information
- **Re-evaluate candidacy**: If the DrugBank mapping is successfully resolved and the compound is re-integrated into the knowledge graph, re-run TxGNN predictions to determine whether any indication scores emerge

> ⚠️ *This report is for research reference only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

