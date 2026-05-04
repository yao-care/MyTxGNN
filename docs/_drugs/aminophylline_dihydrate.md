---
layout: default
title: Aminophylline Dihydrate
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Aminophylline Dihydrate
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

# AMINOPHYLLINE DIHYDRATE: Drug Repurposing Evaluation — Evidence Pack Incomplete

## One-Sentence Summary

Aminophylline Dihydrate is a methylxanthine bronchodilator widely used for respiratory conditions including asthma and COPD.
This Evidence Pack contains **no TxGNN-predicted new indications**, and two critical data gaps — mechanism of action and official safety warnings — remain unresolved.
A full repurposing evaluation **cannot be completed** until these gaps are remediated; the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in this Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction absent; no supporting studies assessable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indication was returned in this Evidence Pack, so no formal mechanistic rationale for a new indication can be constructed.

Detailed mechanism of action data is not available in the current Evidence Pack (Data Gap DG002). From established pharmacological knowledge, Aminophylline is a salt of theophylline and ethylenediamine belonging to the methylxanthine class. It is understood to act primarily as a non-selective phosphodiesterase inhibitor and adenosine receptor antagonist, producing smooth muscle relaxation, bronchodilation, and mild positive chronotropic and inotropic cardiac effects. Its established clinical role is in the management of bronchospasm associated with asthma and COPD.

Without a predicted new indication from the TxGNN model, the mechanistic bridge analysis — the central pillar of a repurposing evaluation — cannot proceed. This section will be populated once TxGNN predictions are available and the MOA data gap is resolved.

---

## Malaysia Market Information

One registration record exists in the Malaysia NPRA database for Aminophylline Dihydrate; however, all associated license fields (authorization number, product name, dosage form, and approved indication text) were not captured during data retrieval and are absent from this Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| Not retrieved | Not retrieved | Not retrieved | Not retrieved |

To complete this table, the NPRA license record must be re-queried and the approved indication text extracted.

---

## Safety Considerations

Please refer to the official package insert for safety information.

Both the key warnings and contraindications for Aminophylline Dihydrate are flagged as blocking data gaps (DG001) in this Evidence Pack. No drug–drug interaction data was returned from the DrugBank query. Until the package insert is retrieved and parsed, no safety profile can be presented, and the drug **cannot advance to clinical feasibility screening**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — the TxGNN prediction pipeline returned no candidate indications, and the two highest-priority data gaps (safety warnings and MOA) remain unresolved, blocking both safety screening and mechanistic analysis.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Download the Malaysia-registered package insert PDF from NPRA and extract key warnings, contraindications, and dosage information
- **Resolve DG002 (High):** Query DrugBank API using the INN "aminophylline" or "theophylline" to obtain DrugBank ID, full MOA, and drug categories
- **Obtain TxGNN predictions:** Confirm that Aminophylline Dihydrate (or its active moiety theophylline) is present in the TxGNN knowledge graph; re-run the KG + DL prediction pipeline and populate `predicted_indications`
- **Complete the NPRA license record:** Re-query NPRA to retrieve authorization number, product name, dosage form, and approved indication text for the 1 registered product
- **Re-generate the Evidence Pack** once all four items above are resolved, then proceed to full S1 safety screening and mechanistic evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

