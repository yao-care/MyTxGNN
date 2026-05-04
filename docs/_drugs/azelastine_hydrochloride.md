---
layout: default
title: Azelastine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 0
---

# Azelastine Hydrochloride
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

# Azelastine Hydrochloride: Drug Repurposing Evaluation — No Predicted Indication Available

## One-Sentence Summary

Azelastine hydrochloride is a second-generation antihistamine currently marketed in Malaysia with 2 registered products. The TxGNN model has **not generated any predicted new indications** for this drug, and significant data gaps remain in drug-level information including mechanism of action, safety warnings, and approved indication text.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *(Data unavailable — license indication text not retrieved)* |
| Predicted New Indication | None (no TxGNN prediction available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

No TxGNN prediction has been generated for Azelastine Hydrochloride. This section cannot be evaluated at this time.

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, azelastine is a second-generation phthalazinone-derivative antihistamine with mast cell stabilising properties. It is commonly used for the symptomatic relief of allergic rhinitis (nasal spray) and allergic conjunctivitis (eye drops). It acts primarily as a selective H1-receptor antagonist and also inhibits the release of histamine and other inflammatory mediators from mast cells.

Without a predicted indication from TxGNN, no mechanistic plausibility analysis can be conducted. The absence of a prediction may be due to the drug lacking a mapped DrugBank ID (`drugbank_id: null`) in the evidence pack, which would prevent the knowledge graph from establishing the necessary linkages for repurposing candidate generation.

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication to query against.

## Literature Evidence

Currently no related literature available — no predicted indication to query against.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* |
| *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* |

> **Note:** Two registrations were identified by the NPRA query (query date: 2026-03-27), but the detailed license fields (authorization number, product name, dosage form, approved indication) were not populated in the evidence pack. A follow-up NPRA data retrieval is required.

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, drug interactions) are currently unavailable in the evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No repurposing candidate has been predicted by TxGNN for Azelastine Hydrochloride. Additionally, critical data gaps — including the DrugBank ID mapping, approved indication text, mechanism of action, and safety profile — prevent any meaningful evaluation. The drug cannot proceed through the repurposing pipeline until these foundational data elements are resolved.

**To proceed, the following is needed:**

1. **DrugBank ID Resolution** — Map Azelastine Hydrochloride to its DrugBank ID (expected: DB00972) to enable knowledge graph linkage and TxGNN prediction
2. **NPRA License Detail Retrieval** — Re-query NPRA to populate authorization numbers, product names, dosage forms, and approved indication text for the 2 registered products
3. **Mechanism of Action (MOA)** — Retrieve MOA data from DrugBank API (Severity: High, per DG002)
4. **Safety Profile (Package Insert)** — Download and parse the package insert to extract warnings and contraindications (Severity: Blocking, per DG001)
5. **Re-run TxGNN Prediction** — After DrugBank ID is mapped, re-execute the KG and DL prediction pipeline to generate repurposing candidates

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

