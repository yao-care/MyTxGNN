---
layout: default
title: Loperamide Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 0
---

# Loperamide Hydrochloride
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

# Loperamide Hydrochloride: Antidiarrheal Agent — Drug Repurposing Evaluation Pending

## One-Sentence Summary

Loperamide Hydrochloride is a peripherally-acting opioid receptor agonist widely used as an antidiarrheal agent for acute and chronic diarrhea.
The current Evidence Pack contains **no TxGNN predicted indications**, which means a formal repurposing analysis cannot be completed at this time.
Before proceeding, critical data gaps — including package insert safety information and DrugBank MOA — must be resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antidiarrheal (acute diarrhea, chronic diarrhea, traveler's diarrhea) |
| Predicted New Indication | Not available — no TxGNN output in this Evidence Pack |
| TxGNN Prediction Score | Not available |
| Evidence Level | N/A (prediction data absent) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Why Can This Evaluation Not Proceed?

The Evidence Pack for Loperamide Hydrochloride is missing two categories of data that are prerequisites for a complete repurposing report:

**1. No TxGNN Predicted Indications**
The `predicted_indications` array is empty. Without a TxGNN model output, there is no candidate repurposing target to evaluate, no evidence trail to assess, and no clinical trial or literature linkage to review. This is the most fundamental gap — the engine of the entire report.

**2. Mechanism of Action (MOA) Data Gap**
Loperamide acts as a **μ-opioid receptor agonist** in the myenteric plexus of the intestinal wall, reducing peristalsis and intestinal secretion without significant central nervous system effects at therapeutic doses. However, this information has not been formally confirmed via DrugBank or the package insert in this Evidence Pack (marked as DG002, severity: High). Until MOA is confirmed from a structured data source, mechanistic plausibility analysis for any new indication cannot be formally documented.

**3. Package Insert Safety Data Gap**
Warnings and contraindications are marked as DG001 (severity: Blocking). Without these, the safety section of this report cannot be completed, and any repurposing candidate cannot pass the standard S1 safety pre-screening step.

---

## Malaysia Market Information

License detail fields are not populated in the current Evidence Pack (all entries are blank). Based on regulatory query results, **9 product registrations** are confirmed as marketed in Malaysia. The table below reflects the available structured data:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | *(License details not populated in Evidence Pack)* |

> **Action Required**: Retrieve full license records from the NPRA database to populate product names, dosage forms, and approved indications for all 9 registrations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack lacks TxGNN predicted indications entirely, making it impossible to identify, assess, or report on any repurposing candidate. Additionally, two blocking or high-severity data gaps prevent safety and mechanistic analysis from proceeding.

**To proceed, the following is needed:**

- [ ] **[Critical]** Re-run TxGNN model for Loperamide Hydrochloride and populate `predicted_indications` with at least one candidate indication, including associated clinical trials and literature
- [ ] **[Blocking — DG001]** Download and parse the TFDA/NPRA package insert PDF to extract key warnings and contraindications, enabling S1 safety pre-screening
- [ ] **[High — DG002]** Query the DrugBank API using INN "loperamide" to retrieve structured MOA, drug categories, and toxicity data; confirm DrugBank ID
- [ ] **[Standard]** Populate all 9 license records in `taiwan_regulatory.licenses` with authorization numbers, product names, dosage forms, and approved indication text from NPRA
- [ ] **[Standard]** Re-submit the complete Evidence Pack for a full repurposing report once all critical gaps are resolved

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

