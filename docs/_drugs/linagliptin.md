---
layout: default
title: Linagliptin
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 0
---

# Linagliptin
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

# Linagliptin: From Type 2 Diabetes Mellitus — No Repurposing Prediction Available

## One-Sentence Summary

Linagliptin is a DPP-4 (dipeptidyl peptidase-4) inhibitor approved for the management of Type 2 Diabetes Mellitus.
This Evidence Pack contains **no TxGNN repurposing predictions** — the `predicted_indications` field is empty, indicating the prediction pipeline has not yet run or returned results.
Two blocking data gaps (MOA and package insert) must be resolved before a repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Not available — `predicted_indications` is empty |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions to evaluate |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Malaysia Market Information

The 9 NPRA registrations are confirmed, but all individual licence records in this Evidence Pack are unpopulated (empty strings). Detailed product-level information is unavailable until licence data is retrieved from the NPRA database.

| Item | Status |
|------|--------|
| Total registrations (NPRA) | 9 |
| Licence details | Not available in this Evidence Pack |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings and contraindications are flagged as data gaps (DG001, severity: Blocking). No drug–drug interaction records were returned by the DDI query. Safety evaluation cannot proceed until the package insert is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The `predicted_indications` array is empty, meaning no repurposing candidate has been identified by TxGNN for this drug. Combined with two unresolved data gaps covering MOA and package insert safety information, there is currently no basis on which to conduct a repurposing evaluation.

**To proceed, the following is needed:**

1. **Resolve DG001 (Blocking)** — Download and parse the TFDA/NPRA package insert PDF to extract approved indications, warnings, and contraindications; this is prerequisite for the safety screening step.
2. **Resolve DG002 (High)** — Query the DrugBank API for Linagliptin's mechanism of action (DB08882); MOA data is required by the TxGNN pipeline for mechanistic similarity scoring.
3. **Re-run the TxGNN prediction pipeline** with complete inputs to populate `predicted_indications`; only then can a disease target and evidence level be assigned.
4. **Retrieve NPRA licence details** for the 9 registered products (product names, dosage forms, approved indication text) to complete the Malaysia Market Information section.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

