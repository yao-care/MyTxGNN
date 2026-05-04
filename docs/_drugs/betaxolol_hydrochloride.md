---
layout: default
title: Betaxolol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 0
---

# Betaxolol Hydrochloride
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

# Betaxolol Hydrochloride: Drug Repurposing Evaluation Report

## One-Sentence Summary

Betaxolol hydrochloride is a selective beta-1 adrenergic receptor antagonist (beta-blocker), commonly used for hypertension and glaucoma (ocular hypertension). The TxGNN model **did not generate any predicted new indications** for this drug, and critical data gaps (DrugBank ID, MOA, safety profile) remain unresolved, preventing further evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *(Data unavailable — license indication text is empty)* |
| Predicted New Indication | **None** (no TxGNN predictions generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions, no supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for Betaxolol Hydrochloride, so there is no mechanistic rationale to evaluate at this time.

Based on general pharmacological knowledge, Betaxolol is a cardioselective (beta-1 selective) adrenergic receptor blocker. In its oral form it is used to manage hypertension, and in its ophthalmic form it is used to reduce intraocular pressure in open-angle glaucoma and ocular hypertension. Its selectivity for beta-1 receptors means it has relatively less effect on beta-2 receptors in bronchial and vascular smooth muscle compared to non-selective beta-blockers.

Currently, detailed mechanism of action data was not retrieved from DrugBank (DrugBank ID is missing from this evidence pack). Without a confirmed DrugBank mapping and without any TxGNN prediction output, it is not possible to assess cross-indication mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no predicted indication exists, therefore no clinical trial search was performed.

---

## Literature Evidence

Currently no predicted indication exists, therefore no literature search was performed.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |

> **Note:** One registration record exists in the NPRA database, but all detail fields (authorization number, product name, dosage form, approved indication) are missing from the evidence pack. This data gap should be remediated by re-querying the NPRA database.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, drug interactions) are currently unavailable. This is classified as a **Blocking** data gap (DG001) that must be resolved before any safety assessment can proceed.

---

## Data Gaps Summary

The following critical data gaps were identified and must be addressed:

| Gap ID | Item | Severity | Impact | Remediation |
|------|------|------|------|------|
| DG001 | TFDA Label Warnings / Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse the label PDF from the regulatory authority website |
| DG002 | Mechanism of Action (MOA) | **High** | Affects mechanistic relevance analysis | Query DrugBank API (Betaxolol is likely DB00195) |
| — | DrugBank ID | High | Cannot retrieve MOA, DDI, or toxicity data | Confirm mapping: Betaxolol → DrugBank DB00195 |
| — | License detail fields | Medium | Market information table is empty | Re-query NPRA with corrected parameters |
| — | TxGNN Predictions | High | No repurposing candidates to evaluate | Verify that Betaxolol was included in the KG input and re-run prediction pipeline |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for Betaxolol Hydrochloride, and multiple blocking data gaps (safety profile, DrugBank ID, MOA) remain unresolved. There is insufficient information to evaluate any repurposing opportunity.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping**: Betaxolol Hydrochloride is very likely DrugBank [DB00195](https://go.drugbank.com/drugs/DB00195) — confirm and populate the evidence pack
- **Retrieve MOA data** from DrugBank to enable mechanistic analysis
- **Obtain safety information** (warnings, contraindications, DDI) from the package insert or regulatory database
- **Re-populate NPRA license details** (authorization number, product name, dosage form, approved indication)
- **Verify TxGNN pipeline input**: Confirm that Betaxolol was correctly mapped in the knowledge graph and re-run the prediction if necessary
- **Re-generate the evidence pack** once the above gaps are filled, then re-evaluate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

