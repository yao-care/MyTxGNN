---
layout: default
title: Aprotinin
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 0
---

# Aprotinin
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

# Aprotinin: Drug Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Aprotinin (DrugBank: DB06692) is a serine protease inhibitor classically used as an antifibrinolytic agent to reduce perioperative blood loss in cardiac surgery.
However, **the current Evidence Pack contains no TxGNN-predicted new indications**, and critical data fields including mechanism of action, package insert warnings, and approved indication text are all missing.
This report serves as a **data gap assessment** rather than a full repurposing evaluation; no recommendation can be made until the identified gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | None — TxGNN prediction not yet completed |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Model prediction only — but no prediction exists) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

The `predicted_indications` array in this Evidence Pack is **empty**, meaning TxGNN has either not yet processed this candidate, or Aprotinin's DrugBank entry (DB06692) could not be successfully linked to the knowledge graph for scoring.

Two critical upstream data gaps are blocking the full repurposing workflow:

1. **Mechanism of Action (MOA)** — classified as severity **High**. Without MOA data, the knowledge graph cannot correctly anchor Aprotinin's pharmacological profile to disease nodes, which directly impairs the quality of any TxGNN scoring.

2. **TFDA Package Insert Warnings and Contraindications** — classified as severity **Blocking**. This prevents even basic safety screening (S1 triage), meaning the candidate cannot proceed to clinical feasibility review.

Until these two gaps are resolved, no mechanistic rationale, clinical trial evidence table, or literature evidence table can be meaningfully generated for a repurposing target.

---

## Malaysia Market Information

Registration details in the Evidence Pack are incomplete — all fields (license number, product name, dosage form, manufacturer, approved indication text) are empty despite 2 registered licenses being recorded.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| (Not available) | (Not available) | (Not available) | (Not available) |
| (Not available) | (Not available) | (Not available) | (Not available) |

> **Action Required:** Retrieve full license details from the Malaysia NPRA product registry to populate this table.

---

## Safety Considerations

All safety fields in the current Evidence Pack contain no usable data:

- Key warnings: not retrieved
- Contraindications: not retrieved
- Drug-drug interactions: query returned 0 results (`not_found`)

> Please refer to the approved package insert for safety information. Note that Aprotinin has a notable post-market safety history in other jurisdictions (including market withdrawal in several countries due to cardiovascular and renal adverse events) — this regulatory history must be reviewed before any repurposing evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — there are no TxGNN predictions, no MOA, no safety data, and no approved indication text — making it impossible to evaluate Aprotinin's repurposing potential at this time.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download and parse the TFDA package insert PDF to extract warnings, contraindications, and approved indication text; re-run the S1 safety triage gate
- **[High — DG002]** Query the DrugBank API for DB06692 to retrieve mechanism of action, drug categories, and toxicity profile; use this to re-run TxGNN KG mapping
- **[Required]** Confirm whether Aprotinin's DrugBank node is correctly present in `data/node.csv` and `data/kg.csv`; if missing or misidentified, the KG prediction step will produce no output
- **[Required]** Retrieve full NPRA license details (license number, product name, dosage form, indication text) for both registered products
- **[Required]** Investigate Aprotinin's international regulatory status (suspended/withdrawn in EU and Canada since 2007–2008 due to BART trial findings) and assess whether Malaysia's 2 registrations remain active and clinically appropriate
- **[Optional]** Once MOA is confirmed, manually verify whether Aprotinin appears in any repurposing literature (e.g., anti-inflammatory, hereditary angioedema, pancreatitis) to supplement the TxGNN pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

