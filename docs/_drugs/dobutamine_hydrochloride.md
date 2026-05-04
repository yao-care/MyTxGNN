---
layout: default
title: Dobutamine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 0
---

# Dobutamine Hydrochloride
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

# Dobutamine Hydrochloride: Drug Repurposing Evaluation Report

## One-Sentence Summary

Dobutamine hydrochloride is a synthetic catecholamine and beta-1 adrenergic agonist, widely used as a short-term inotropic agent for cardiac decompensation. The TxGNN model **did not generate any predicted new indications** for this drug, and the evidence pack contains significant data gaps across regulatory, safety, and mechanistic domains. This report serves as a **data gap assessment** to guide subsequent data collection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (known use: short-term inotropic support in cardiac decompensation) |
| Predicted New Indication | **None** — No TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions or supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not generated any repurposing candidates for dobutamine hydrochloride. This may be due to one or more of the following reasons:

1. **Missing DrugBank ID mapping**: The evidence pack shows `drugbank_id: null`. Without a valid DrugBank identifier, the drug cannot be properly anchored in the TxGNN knowledge graph, preventing the model from generating disease-association predictions. The query log indicates a DrugBank search was performed and returned 1 result, but the ID was not successfully linked to this record.

2. **Narrow therapeutic profile**: Dobutamine is a beta-1 selective adrenergic agonist primarily used as an intravenous inotrope for acute cardiac support. Its mechanism — stimulating cardiac contractility via beta-1 receptors — is highly specific and may have limited cross-disease applicability in the knowledge graph's relational structure.

3. **Data gaps in the evidence pack**: The original MOA, approved indication text, and safety data are all missing, which limits the system's ability to perform mechanistic reasoning and cross-indication inference.

Before drawing conclusions about dobutamine's repurposing potential, the data gaps identified below must be resolved.

---

## Malaysia Market Information

The evidence pack records **4 registrations** for dobutamine hydrochloride with a market status of "Marketed." However, detailed registration information (authorization numbers, product names, dosage forms, and approved indications) was not available in the current dataset.

> **Action needed**: Retrieve full registration details from the NPRA database to populate this section.

---

## Safety Considerations

> Please refer to the package insert for safety information.

**Note**: The following critical data gaps were identified:
- **Key Warnings**: Not available — TFDA/NPRA package insert data not yet parsed
- **Contraindications**: Not available — package insert PDF download and parsing required
- **Drug Interactions**: DrugBank DDI query returned no results (query status: `not_found`)

---

## Data Gap Summary

The following blocking and high-severity data gaps must be addressed before this candidate can proceed through the evaluation pipeline:

| Gap ID | Category | Item | Severity | Remediation |
|--------|----------|------|----------|-------------|
| DG001 | Drug Level | Package insert warnings/contraindications | **Blocking** | Download and parse package insert PDF from regulatory authority website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Query DrugBank API using INN "dobutamine" |
| — | Drug Level | DrugBank ID | **High** | Link the DrugBank search result (1 hit found) to this record |
| — | Prediction Level | TxGNN prediction | **High** | Re-run prediction pipeline after DrugBank ID is resolved |
| — | Regulatory Level | License details (authorization numbers, product names, indications) | **Medium** | Re-query NPRA with expanded fields |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for dobutamine hydrochloride, primarily due to a missing DrugBank ID linkage that prevents knowledge graph integration. Additionally, multiple blocking data gaps in safety and regulatory information preclude any meaningful evaluation at this stage.

**To proceed, the following is needed:**
- Resolve **DrugBank ID mapping** (the query log shows 1 result was found — confirm and link `DB00841` for dobutamine)
- Re-run the **TxGNN prediction pipeline** once the DrugBank ID is properly linked
- Download and parse the **package insert PDF** to populate safety warnings and contraindications
- Re-query **NPRA** to retrieve full license details (authorization numbers, product names, dosage forms, approved indications)
- Once predictions are available, collect **clinical trial** and **literature evidence** for the top-ranked candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

