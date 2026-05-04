---
layout: default
title: Benzydamine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 0
---

# Benzydamine Hydrochloride
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

# Benzydamine Hydrochloride: Drug Repurposing Evaluation

## One-Sentence Summary

Benzydamine hydrochloride is a locally-acting non-steroidal anti-inflammatory drug (NSAID) with analgesic and local anaesthetic properties, commonly used for inflammatory conditions of the mouth and throat.
Currently, the TxGNN model has **not generated any predicted new indications** for this drug, and critical data gaps remain in mechanism of action, safety profile, and regulatory details.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (registration data incomplete) |
| Predicted New Indication | None (no TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No predictions or supporting studies |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on publicly known information, benzydamine hydrochloride is a locally-acting NSAID belonging to the indazole class. It exhibits anti-inflammatory, analgesic, and local anaesthetic activity, and is primarily used topically for conditions such as pharyngitis, stomatitis, and other inflammatory conditions of the oropharyngeal cavity.

Because the TxGNN model has not produced any predicted new indications for benzydamine hydrochloride, a mechanistic plausibility assessment cannot be performed at this time. The absence of predictions may be due to the drug's predominantly local (non-systemic) mechanism of action, limited representation in the knowledge graph, or insufficient mapping data (the DrugBank ID was not resolved in the evidence pack).

Before any repurposing evaluation can proceed, the DrugBank mapping must be completed, the mechanism of action confirmed, and the TxGNN prediction pipeline re-run with corrected inputs.

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication to evaluate).

## Literature Evidence

Currently no related literature available (no predicted indication to evaluate).

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(Data pending)* | *(Data pending)* | *(Data pending)* | *(Data pending)* |

> **Note:** 20 registrations were identified via NPRA query, but detailed licence information (authorization numbers, product names, dosage forms, and approved indications) was not populated in the evidence pack. This data needs to be retrieved from the NPRA database.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack and must be retrieved from the NPRA database or package insert PDFs.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack contains critical data gaps — no DrugBank ID mapping, no mechanism of action data, no predicted indications from TxGNN, and no populated regulatory details. Without a predicted new indication, a repurposing evaluation cannot proceed.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping**: Query DrugBank for "Benzydamine" (DB09084) and confirm the drug–ID linkage
- **Retrieve mechanism of action (MOA)**: Obtain pharmacological data from DrugBank or package insert
- **Populate NPRA registration details**: Extract authorization numbers, product names, dosage forms, and approved indications for the 20 identified licences
- **Retrieve safety data**: Download and parse package insert PDFs for key warnings, contraindications, and drug interactions
- **Re-run TxGNN prediction pipeline**: With the corrected DrugBank ID and complete input data, re-execute the knowledge graph and deep learning prediction models
- **Re-generate evidence pack**: Once predictions are available, collect supporting clinical trial and literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

