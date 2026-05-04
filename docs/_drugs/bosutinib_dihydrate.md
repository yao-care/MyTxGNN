---
layout: default
title: Bosutinib Dihydrate
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 0
---

# Bosutinib Dihydrate
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

# Bosutinib Dihydrate: Drug Repurposing Preliminary Assessment

## One-Sentence Summary

Bosutinib dihydrate is a tyrosine kinase inhibitor (TKI) currently marketed in Malaysia with 2 registered products, primarily indicated for the treatment of chronic myeloid leukaemia (CML). The TxGNN model has **not yet generated predicted new indications** for this compound, and significant data gaps remain in the evidence pack — including mechanism of action details, DrugBank ID mapping, and approved indication text — that must be resolved before a repurposing assessment can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia (CML) — *indication text not captured in current evidence pack* |
| Predicted New Indication | None — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Insufficient — no predictions generated) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, bosutinib is a dual Src/ABL tyrosine kinase inhibitor that blocks the activity of the BCR-ABL fusion oncoprotein, which drives the proliferation of leukaemic cells in chronic myeloid leukaemia (CML). It also inhibits several members of the Src family of kinases and has demonstrated activity against other kinase targets relevant to oncology.

Because the TxGNN model has not yet generated any predicted new indications for bosutinib dihydrate, it is not possible to evaluate mechanistic plausibility for a repurposing hypothesis at this time. The absence of predictions may result from an unsuccessful DrugBank ID mapping (the `drugbank_id` field is null), which would prevent the compound from being matched to nodes in the TxGNN knowledge graph. Resolving this mapping is a prerequisite for generating meaningful predictions.

Given bosutinib's multi-kinase inhibitory profile — targeting not only BCR-ABL but also Src, HER, PDGFR, and other kinases — the drug could theoretically have repurposing potential across several oncology indications and possibly kinase-driven non-oncology conditions. However, any such hypothesis requires validated TxGNN output and supporting clinical evidence.

## Clinical Trial Evidence

Currently no predicted indications have been generated; therefore, no targeted clinical trial search was conducted.

## Literature Evidence

Currently no predicted indications have been generated; therefore, no targeted literature search was conducted.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *(not captured)* | *(not captured)* | *(not captured)* | *(not captured)* |
| *(not captured)* | *(not captured)* | *(not captured)* | *(not captured)* |

> **Note:** Two product registrations are recorded in the NPRA database, but the licence details (authorization number, product name, dosage form, and approved indication text) were not successfully captured during data collection. A re-query of the NPRA database is required to populate these fields.

## Cytotoxicity

Bosutinib is an antineoplastic agent (tyrosine kinase inhibitor class). The following safety profile is based on generally known pharmacological properties:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Tyrosine kinase inhibitor — dual Src/ABL TKI) |
| Myelosuppression Risk | Moderate (thrombocytopenia, neutropenia, and anaemia are commonly reported) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST — hepatotoxicity is a known risk), renal function, electrolytes, lipase |
| Handling Protection | Standard precautions for oral antineoplastic agents; follow institutional cytotoxic drug handling regulations |

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug–drug interaction data were not available in the current evidence pack and represent a **blocking data gap** (DG001) that must be resolved before safety evaluation can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for bosutinib dihydrate is substantially incomplete. No TxGNN predictions have been generated (likely due to a missing DrugBank ID mapping), and critical data fields — including approved indication text, mechanism of action, safety warnings, and contraindications — remain unfilled. A repurposing evaluation cannot proceed until these foundational gaps are resolved.

**To proceed, the following is needed:**
- **DrugBank ID mapping** — Query DrugBank for "bosutinib" (likely DB06616) and update the `drugbank_id` field to enable TxGNN knowledge graph matching
- **Re-run TxGNN prediction** — Once the DrugBank ID is mapped, re-execute the KG and DL prediction pipelines to generate repurposing candidates
- **NPRA licence details** — Re-query the NPRA database to capture authorization numbers, product names, dosage forms, and approved indication text for the 2 registered products
- **Package insert parsing** — Obtain and parse the bosutinib package insert (仿單) to extract key warnings, contraindications, and drug interaction data (resolving DG001)
- **MOA data** — Retrieve detailed mechanism of action from DrugBank API (resolving DG002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

