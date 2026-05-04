---
layout: default
title: Dextromethorphan Hbr
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 0
---

# Dextromethorphan Hbr
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

# Dextromethorphan HBr: Drug Repurposing Evaluation Report

## One-Sentence Summary

Dextromethorphan hydrobromide (DXM) is a widely used over-the-counter antitussive (cough suppressant) that acts on sigma-1 and NMDA receptors. The TxGNN model has **not yet generated predicted new indications** for this drug. The evidence pack is currently incomplete, with critical data gaps in mechanism of action, regulatory label details, and safety information that must be resolved before repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antitussive (cough suppressant) — *license details pending* |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Insufficient data for evaluation) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 24 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN prediction has been generated for Dextromethorphan HBr, so a mechanistic plausibility assessment cannot be performed at this time.

> Detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, Dextromethorphan is a synthetic morphinan derivative that acts as a non-opioid antitussive. It exerts its cough-suppressing effect primarily through sigma-1 receptor agonism and NMDA receptor antagonism in the central nervous system. These receptor targets have attracted research interest in areas beyond cough suppression — including neuropsychiatric disorders, neuropathic pain, and pseudobulbar affect — which may represent potential repurposing directions once TxGNN predictions become available.

Until a formal TxGNN prediction is generated and linked to this drug, no mechanistic bridge to a new indication can be evaluated.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted clinical trial search has been performed.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature search has been performed.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *(details pending)* | *(details pending)* | *(details pending)* | *(details pending)* |

> **Note:** 24 registrations were identified in the NPRA database for Dextromethorphan HBr, but detailed license information (authorization numbers, product names, dosage forms, and approved indication text) has not yet been populated in this evidence pack. This data should be retrieved from the NPRA database to complete the assessment.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (identified as **Blocking** data gap DG001). These must be obtained from the NPRA website or product insert PDFs before any repurposing evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is incomplete — no TxGNN-predicted new indication exists, and critical data fields (MOA, license details, safety information) remain unfilled. A repurposing evaluation cannot be meaningfully initiated without a predicted indication and baseline safety profile.

**To proceed, the following is needed:**

1. **Run TxGNN prediction** — Execute the KG and/or DL prediction pipeline for Dextromethorphan to generate candidate new indications
2. **Resolve DrugBank ID** — Map "DEXTROMETHORPHAN HBR" to its DrugBank entry (likely [DB00514](https://go.drugbank.com/drugs/DB00514)) to retrieve MOA, pharmacology, and toxicity data
3. **Populate NPRA license details** — Retrieve full registration records (authorization numbers, product names, dosage forms, approved indications) from the NPRA database
4. **Obtain safety data (DG001 — Blocking)** — Download and parse product insert PDFs to extract key warnings, contraindications, and drug interactions
5. **Obtain mechanism of action (DG002 — High)** — Query DrugBank API to fill in MOA details for mechanistic plausibility analysis

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

