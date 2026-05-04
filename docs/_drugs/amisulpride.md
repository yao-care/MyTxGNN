---
layout: default
title: Amisulpride
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 0
---

# Amisulpride
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

# Amisulpride: Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Amisulpride (DB06288) is an atypical antipsychotic with 4 registered products in the Malaysian market.
The current Evidence Pack contains **no TxGNN repurposing predictions**, and critical data fields — including mechanism of action, approved indications, and safety warnings — are absent.
This evaluation cannot proceed beyond a preliminary status assessment until data collection is completed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved from current data |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | — (No predictions generated) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | **Hold** |

---

## Why Are No Predictions Available?

Amisulpride could not generate TxGNN predictions in this cycle due to two unresolved data gaps that block the pipeline:

**1. Missing mechanism of action (MOA):** The DrugBank API query returned a result (query log ID 2, 2026-03-27), but MOA fields were not populated in the Evidence Pack. Without confirmed mechanistic data, the knowledge graph cannot establish disease-link pathways to candidate repurposing targets.

**2. Empty approved indication fields:** All 4 NPRA-registered licenses returned blank indication text. Without a baseline disease anchor, the system cannot perform disease-similarity scoring or filter candidate predictions.

From published medical literature, amisulpride is known as a **selective dopamine D2/D3 receptor antagonist**. At standard antipsychotic doses (400–800 mg/day), it reduces positive and negative symptoms of schizophrenia by blocking postsynaptic dopamine receptors. At ultra-low doses (5–25 mg), it preferentially acts on presynaptic autoreceptors, which underpins its well-documented antiemetic properties — a mechanism that resulted in U.S. FDA approval for postoperative nausea and vomiting (PONV) in 2020 (brand name: Barhemsys®). Once MOA and indication data are formally captured, a meaningful TxGNN prediction run is expected to be feasible.

---

## Malaysia Market Information

The NPRA query (2026-03-27) confirmed 4 registered products, but product-level details were not returned in this data cycle. The table below cannot be populated until a secondary NPRA data pull is completed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| (data not retrieved) | (data not retrieved) | (data not retrieved) | (data not retrieved) |

> **Note:** NPRA returned a successful query with 4 results, but all license record fields (product name, dosage form, manufacturer, approved indication) are empty strings. A re-query targeting individual product monographs or package insert PDFs is required.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. NPRA package inserts should be downloaded and parsed as the primary remediation step.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions were generated, and all three core evaluation inputs — approved indication, mechanism of action, and safety profile — are missing. There is insufficient evidence to assess repurposing potential or safety feasibility at this stage.

**To proceed, the following is needed:**

- **NPRA package insert retrieval**: Download PDF monographs for all 4 registered products to extract approved indications, key warnings, and contraindications (Data Gap DG001 — Blocking severity)
- **DrugBank API re-query**: Retrieve mechanism of action, pharmacodynamics, and drug interaction data for DB06288 (Data Gap DG002 — High severity)
- **TxGNN pipeline re-run**: After resolving DG001 and DG002, re-execute the KG prediction and DL prediction pipelines to generate candidate repurposing indications
- **NPRA product detail verification**: Confirm whether all 4 registrations share the same indication (e.g., schizophrenia only) or whether a low-dose antiemetic indication (PONV) is separately registered in Malaysia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

