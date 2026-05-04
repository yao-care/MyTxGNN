---
layout: default
title: Piracetam
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 0
---

# Piracetam
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

# Piracetam: Drug Repurposing Evaluation — TxGNN Prediction Pending

## One-Sentence Summary

Piracetam (DrugBank: DB09210) is a nootropic agent currently holding **9 marketing authorisations** in Malaysia.
The Evidence Pack contains **no TxGNN repurposing predictions**, and critical drug-level data — including mechanism of action, approved indication text, and safety warnings — remain outstanding data gaps.
A complete repurposing evaluation **cannot be performed** until these gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | None (TxGNN prediction not yet generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no prediction data available |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Currently Available

The `predicted_indications` field in this Evidence Pack is empty, meaning the TxGNN knowledge-graph and deep-learning pipeline has not yet produced a candidate new indication for Piracetam. Without a target indication, the core mechanistic reasoning, clinical trial review, and literature analysis that form the backbone of a repurposing report cannot be conducted.

Additionally, detailed mechanism of action (MOA) data is flagged as a high-severity data gap (DG002). Without understanding how Piracetam acts at the molecular level, it would not be possible to evaluate whether any predicted indication is pharmacologically plausible.

Once TxGNN predictions are generated and MOA data is retrieved from DrugBank, this section will be replaced with a full mechanistic rationale linking the original and new indications.

---

## Malaysia Market Information

Nine marketing authorisations were confirmed via NPRA query on 2026-03-27. However, the individual licence records — including product name, dosage form, and approved indication text — are not populated in this version of the Evidence Pack.

| Status | Detail |
|--------|--------|
| Confirmed licences | 9 (source: NPRA, queried 2026-03-27) |
| Product names | Not retrieved |
| Dosage forms | Not retrieved |
| Approved indication text | Not retrieved |

> **Action required:** Retrieve full licence records from the NPRA portal to populate product-level details before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings and contraindications have not yet been retrieved from the package insert PDF (data gap DG001, severity: Blocking). No drug–drug interactions were found in the current query (DDI count: 0), but this result should be interpreted cautiously until the full package insert is reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The two prerequisites for a repurposing evaluation — a TxGNN-predicted target indication and basic drug-level safety/MOA data — are both absent. Proceeding without them would produce an analysis with no evidential or mechanistic foundation.

**To proceed, the following is needed:**

1. **Run TxGNN prediction pipeline** for Piracetam (KG + DL methods) to generate repurposing candidates with confidence scores
2. **Retrieve MOA from DrugBank API** (DG002 — High severity): query DrugBank for mechanism of action, pharmacodynamics, and drug targets
3. **Download and parse the TFDA/NPRA package insert PDF** (DG001 — Blocking severity): extract key warnings, contraindications, and special population guidance
4. **Retrieve full NPRA licence records**: product names, dosage forms, manufacturers, and approved indication text for all 9 authorisations
5. **Re-run Evidence Pack generation** (v5 or later) with the above data, then regenerate this report

> ⚠️ *This report is for research reference only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

