---
layout: default
title: Benzyl Benzoate
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 0
---

# Benzyl Benzoate
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

# Benzyl Benzoate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Benzyl Benzoate (DrugBank: DB00676) is a marketed drug in Malaysia with 6 registered licenses. However, the TxGNN model has **not generated any predicted new indications** for this compound, and critical data gaps remain in mechanism of action and safety information, preventing further repurposing evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Benzyl Benzoate |
| DrugBank ID | DB00676 |
| Original Indication | Not available in current dataset |
| Predicted New Indication | **None** — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no prediction to evaluate |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

---

## Why Are There No Predictions?

Benzyl Benzoate is a well-established topical antiparasitic and scabicidal agent. The TxGNN model did not generate any repurposing candidates for this drug. Several factors may contribute to this outcome:

1. **Incomplete drug characterisation**: The mechanism of action (MOA) data is currently unavailable in the evidence pack. Without MOA information, the model's ability to identify mechanistically plausible new indications may be limited.

2. **Nature of the drug**: Benzyl Benzoate is primarily used as a topical agent (for scabies and pediculosis). Drugs with predominantly local/topical mechanisms may have fewer systemic target interactions in the knowledge graph, resulting in fewer or no repurposing candidates being identified.

3. **Sparse knowledge graph connectivity**: If the drug node in the TxGNN knowledge graph has limited edges (few known drug–target, drug–disease, or drug–pathway connections), the prediction algorithm may not have sufficient signal to generate confident repurposing hypotheses.

---

## Clinical Trial Evidence

Currently no predicted indications to evaluate — no clinical trial search was performed.

---

## Literature Evidence

Currently no predicted indications to evaluate — no literature search was performed.

---

## Malaysia Market Information

6 licenses are registered in Malaysia. However, detailed license information (authorization numbers, product names, dosage forms, and approved indications) was not available in the current dataset.

> **Note**: License details should be retrieved from the NPRA database to complete this section.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

---

## Data Gaps Summary

The following critical data gaps were identified and must be resolved before any repurposing evaluation can proceed:

| ID | Item | Severity | Impact | Remediation |
|----|------|----------|--------|-------------|
| DG001 | Package insert warnings / contraindications | **Blocking** | Cannot enter Stage 1 safety screening | Download and parse package insert PDF from regulatory authority website |
| DG002 | Mechanism of Action (MOA) | **High** | Affects mechanistic relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not generate any repurposing predictions for Benzyl Benzoate. Combined with the absence of MOA data and safety information, there is insufficient basis to advance this candidate into further evaluation.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): Obtain package insert warnings and contraindications from the regulatory authority
- Resolve **DG002** (High): Retrieve mechanism of action data from DrugBank
- Populate Malaysia license details (authorization numbers, product names, dosage forms, approved indications) from the NPRA database
- Re-run TxGNN prediction pipeline after enriching the drug's knowledge graph node with MOA and indication data
- If predictions remain absent after data enrichment, consider whether the drug's topical/local action profile inherently limits systemic repurposing potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

