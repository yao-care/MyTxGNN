---
layout: default
title: Activated Charcoal
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 0
---

# Activated Charcoal
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

# Activated Charcoal: Emergency Toxin Adsorption Agent — No TxGNN Predictions Available

## One-Sentence Summary

Activated charcoal is a broad-spectrum gastrointestinal adsorbent primarily used in emergency medicine for acute poisoning and drug overdose management.
The current TxGNN analysis returned **no predicted new indications** for this drug.
As a result, a formal drug repurposing evaluation cannot be completed without re-running the prediction pipeline with complete input data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute poisoning / Toxin adsorption (emergency use) |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no predictions or supporting studies retrieved) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why No Predictions Are Available

The `predicted_indications` array in this Evidence Pack is empty. This typically occurs for one or more of the following reasons:

1. **Mapping failure**: Activated charcoal may not have been matched to a node in the TxGNN knowledge graph. Because it is a non-specific physical adsorbent rather than a targeted small molecule, it may lack the pharmacological fingerprint (receptor binding, enzymatic targets) required for graph-based similarity scoring.

2. **Score threshold filtering**: Any candidate predictions may have been removed by the post-processing score cutoff before reaching this report.

3. **Pipeline incompleteness**: The Evidence Pack was flagged with two blocking/high-severity data gaps (DG001: TFDA warnings, DG002: MOA), which may have halted downstream prediction steps.

Until the prediction pipeline is re-run with resolved data gaps, there is no repurposing hypothesis to evaluate.

---

## Malaysia Market Information

Three product registrations are confirmed in the NPRA database, but the detailed licence records (product names, dosage forms, approved indications) were not retrieved in this data pull.

| Item | Status |
|------|--------|
| Number of Registered Products | 3 |
| Market Status | ✓ Marketed |
| Detailed Licence Records | Not retrieved — requires a targeted NPRA record lookup |

To populate the full licence table, re-query the NPRA portal with the individual product registration numbers associated with DB09278.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Both the TFDA package insert warnings/contraindications (DG001, severity: Blocking) and drug interaction data were absent from this Evidence Pack. These must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no TxGNN-predicted indications to evaluate, and two critical data gaps (MOA and regulatory safety text) remain unresolved, making it impossible to assess either mechanistic plausibility or safety at this stage.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking)**: Download and parse the TFDA package insert PDF to extract approved indications, warnings, and contraindications.
- **Resolve DG002 (High)**: Query the DrugBank API for DB09278 to retrieve mechanism of action, drug categories, and toxicity data.
- **Re-run TxGNN prediction pipeline**: After confirming that activated charcoal maps correctly to a knowledge graph node, re-execute `run_kg_prediction.py` to generate scored repurposing candidates.
- **Verify NPRA licence details**: Retrieve the three product registration records in full (product name, dosage form, approved indication text) from the NPRA database.
- **Confirm KG node eligibility**: Determine whether activated charcoal is represented as a tractable node in the TxGNN knowledge graph (`data/node.csv`); if absent, assess whether a surrogate compound or a mechanism-level placeholder can be used.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

