---
layout: default
title: Bismuth Subgallate
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 0
---

# Bismuth Subgallate
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

# Bismuth Subgallate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bismuth Subgallate (DrugBank: DB13909) is a bismuth compound currently marketed in Malaysia with 1 registered product. No new indications have been predicted by the TxGNN model at this time, and critical data gaps — including mechanism of action, approved indication text, and safety information — prevent meaningful repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (licence indication text is empty) |
| Predicted New Indication | None (no TxGNN predictions generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No prediction to evaluate |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There is currently **no TxGNN prediction** available for Bismuth Subgallate. The `predicted_indications` array is empty, meaning the model either did not generate a repurposing candidate for this drug or the prediction pipeline has not yet been run for it.

Additionally, detailed mechanism of action (MOA) data is not available. Bismuth subgallate is a bismuth salt known in general pharmacology for astringent and haemostatic properties, but without a confirmed MOA entry in the evidence pack, mechanistic reasoning for any potential new indication cannot be established.

Before any repurposing evaluation can proceed, the drug must first pass through the TxGNN prediction pipeline with successful DrugBank-to-KG node mapping, and the foundational data gaps (MOA, approved indications, safety profile) must be resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication available to search against.

---

## Literature Evidence

Currently no related literature available — no predicted indication available to search against.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Not provided) | (Not provided) | (Not provided) | (Not provided) |

> **Note:** One licence is recorded in the NPRA database, but all detail fields (licence number, product name, dosage form, approved indication) are empty in the current evidence pack. These need to be retrieved from the NPRA portal.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, drug-drug interactions) are currently unavailable. The DrugBank DDI query returned no results. A full safety profile must be obtained from the product package insert or NPRA database before any repurposing assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions have been generated for Bismuth Subgallate, and multiple blocking data gaps exist. Without a predicted indication, there is nothing to evaluate for clinical plausibility or evidence support.

**To proceed, the following is needed:**

1. **Run TxGNN prediction pipeline** — Verify that DB13909 maps to a valid node in the knowledge graph; if mapping fails, investigate alternative DrugBank IDs or salt forms
2. **Retrieve MOA data** (Data Gap DG002, severity: High) — Query DrugBank API for pharmacodynamics and mechanism of action
3. **Retrieve NPRA licence details** — Obtain complete registration information (licence number, product name, dosage form, approved indication text) from the NPRA portal
4. **Retrieve safety information** (Data Gap DG001, severity: Blocking) — Download and parse the package insert PDF from the regulatory authority website for warnings, contraindications, and precautions
5. **Re-evaluate** once prediction results and foundational data are available

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

