---
layout: default
title: Aspirin
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 0
---

# Aspirin
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

# ASPIRIN: Drug Repurposing Evaluation (No Predictions Available)

## One-Sentence Summary

Aspirin (acetylsalicylic acid) is a widely used analgesic, antipyretic, and anti-inflammatory agent with well-established cardiovascular applications, confirmed as marketed in Malaysia with 22 registered products.
However, **no TxGNN predicted indications** are present in this evidence pack, and critical data including mechanism of action, individual license details, and safety profile are absent.
**This report reflects an incomplete evaluation; supplementary data retrieval is required before any repurposing decision can be made.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in registration data |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions to evaluate |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 22 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The TxGNN prediction pipeline did not return any candidate indications for Aspirin in this evidence pack. This is most likely due to one or more of the following upstream failures:

1. **DrugBank ID is absent** — Without a confirmed DrugBank ID, the drug cannot be mapped to a node in the TxGNN knowledge graph, blocking all downstream KG-based and DL-based scoring.
2. **Disease mapping may be incomplete** — If the approved indication text fields are empty (as they are here), the disease normalisation step cannot produce seed nodes for the repurposing graph traversal.
3. **Data retrieval is partial** — The query log confirms that NPRA returned 22 records and DrugBank returned 1 result, but the structured fields were not populated into the evidence pack, suggesting a parsing or integration gap.

Currently, detailed mechanism of action data is not available. Based on widely published pharmacology, Aspirin irreversibly inhibits COX-1 and COX-2 enzymes, reducing prostaglandin synthesis. This makes it mechanistically plausible for repurposing into inflammatory, thrombotic, and potentially oncological contexts. However, this information has not been formally captured in the current evidence pack and cannot be used for a structured evaluation until the DrugBank record is integrated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(No predicted indications are available in this evidence pack, so no indication-specific trial evidence can be displayed.)*

---

## Literature Evidence

Currently no related literature available.

*(No predicted indications are available in this evidence pack, so no indication-specific literature can be displayed.)*

---

## Malaysia Market Information

22 product authorisations are confirmed for Aspirin in Malaysia via NPRA query. However, individual license details (authorization numbers, product names, dosage forms, approved indications) were not retrieved in this evidence pack and are therefore unavailable for tabulation.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | Not retrieved | Not retrieved | Not retrieved |

> **Note:** The NPRA query returned 22 records (query ID 1, status: success), but the structured fields in all 22 license entries are empty. A supplementary data pull is required to populate this table.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack contains no TxGNN predicted indications and is missing all critical data fields — mechanism of action, individual license details, safety warnings, and contraindications — making it impossible to conduct a meaningful drug repurposing evaluation at this stage.

**To proceed, the following is needed:**

- **Re-run TxGNN pipeline** after resolving the DrugBank ID mapping issue, so that candidate indications can be generated
- **Retrieve DrugBank record** (query log confirms 1 result was found) to populate DrugBank ID, MOA, pharmacological categories, and safety data
- **Parse NPRA/package insert PDFs** to populate the 22 license entries with product name, dosage form, and approved indication text (addresses data gap DG001)
- **Resolve MOA data gap** (DG002) via DrugBank API to enable mechanistic plausibility analysis
- **Conduct DDI screening** once the DrugBank ID is confirmed and safety fields are populated
- **Re-evaluate evidence level** once predicted indications and supporting evidence are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

