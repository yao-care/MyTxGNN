---
layout: default
title: Alverine Citrate
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 0
---

# Alverine Citrate
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

# ALVERINE CITRATE: Drug Repurposing Evaluation — Insufficient Data for Prediction

## One-Sentence Summary

Alverine Citrate is a smooth muscle relaxant (antispasmodic) registered in Malaysia, commonly indicated for gastrointestinal spasm and irritable bowel syndrome (IBS).
However, the current Evidence Pack contains **no TxGNN-predicted new indications**, and critical data fields — including mechanism of action and approved indication text — are missing.
**This report cannot proceed to a full repurposing evaluation until the blocking data gaps are resolved.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | None — TxGNN prediction not completed |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — not yet run) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, no TxGNN predicted indications are available for Alverine Citrate in this Evidence Pack. The `predicted_indications` array is empty, which means the knowledge graph and deep learning prediction pipeline has not yet produced output for this compound.

Additionally, detailed mechanism of action (MOA) data is absent. Based on general pharmacological knowledge, Alverine Citrate is a smooth muscle relaxant of the antispasmodic class, acting on visceral smooth muscle to relieve cramps. Its established use in gastrointestinal and gynaecological spasm conditions provides a mechanistic basis for potential repurposing into related motility or pain disorders — but this analysis cannot be formally conducted without completing the prediction pipeline.

**No further mechanistic or indication-relatedness analysis can be performed until the Evidence Pack is populated.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

*(Reason: No predicted indication available to anchor trial search.)*

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

*(Reason: No predicted indication available to anchor literature search.)*

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | — |
| — | — | — | — |

> **Note:** 2 registrations are confirmed in the Malaysia regulatory database (market status: Marketed), but the product names, dosage forms, and approved indication texts were not retrieved in this data pull. Re-querying the NPRA database or accessing individual product records is required.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** Both key warnings and contraindications returned `[Data Gap]` in this Evidence Pack (classified as **Blocking** severity). No drug-drug interaction records were found. Safety evaluation cannot proceed until the TFDA/NPRA package insert is retrieved and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Alverine Citrate is critically incomplete — there are no TxGNN-predicted indications, no MOA data, no approved indication text, and no safety information. A repurposing evaluation cannot be meaningfully conducted in this state.

**To proceed, the following is needed:**

- [ ] **[Blocking — DG001]** Download and parse the TFDA/NPRA package insert PDF to extract approved indications, key warnings, and contraindications
- [ ] **[High — DG002]** Query DrugBank API using INN "alverine citrate" to retrieve DrugBank ID, MOA, pharmacodynamics, and drug categories
- [ ] **[Required]** Re-run TxGNN KG and DL prediction pipeline with correct DrugBank ID mapped to populate `predicted_indications`
- [ ] **[Required]** Re-query NPRA product records to fill in license number, product name, dosage form, and approved indication text for the 2 confirmed registrations
- [ ] **[Optional]** Confirm INN spelling and alternate names (e.g., "Alverine", "Alverin citrate") to improve mapping coverage across all collectors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

