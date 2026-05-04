---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lithium Carbonate: From Mood Stabilization to Pseudoachondroplasia

## One-Sentence Summary

Lithium Carbonate is a well-established psychiatric agent widely used as a mood stabilizer for bipolar disorder and related conditions.
The TxGNN model predicts it may have potential utility in **Pseudoachondroplasia**, a rare skeletal dysplasia caused by COMP gene mutations.
However, with **no clinical trials** and **no publications** directly supporting this indication, current evidence is limited to model prediction only (Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Malaysia registration data |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack (DrugBank MOA data gap). Based on known pharmacology, Lithium Carbonate is a monovalent cation that exerts its primary effects through inhibition of **GSK-3β (Glycogen Synthase Kinase-3 beta)**, thereby activating the **Wnt/β-catenin signalling pathway**. It also modulates inositol phosphate metabolism and influences multiple neurotrophic pathways including BDNF.

Pseudoachondroplasia is caused by gain-of-function mutations in the **COMP (cartilage oligomeric matrix protein)** gene, leading to misfolding of the COMP protein, its pathological accumulation within the endoplasmic reticulum (ER) of chondrocytes, and resulting ER stress and cell death. Theoretically, GSK-3β inhibition by Lithium could reduce ER stress and promote osteoblast survival via Wnt/β-catenin pathway activation, which plays a known role in skeletal development and bone homeostasis.

However, the mechanistic link between Lithium's Wnt/β-catenin activation and the correction of COMP protein aggregation remains **highly speculative and unestablished**. There is currently no published preclinical model (cell line or animal) demonstrating that Lithium treatment mitigates COMP-related ER stress or improves the skeletal phenotype of pseudoachondroplasia. This prediction should be interpreted as a hypothesis-generating signal from the knowledge graph model rather than a clinically actionable finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The Evidence Pack records 1 active registration for Lithium Carbonate in Malaysia; however, detailed registration particulars (authorization number, product name, dosage form, and approved indication text) were not populated in the current data extraction. Please refer directly to the National Pharmaceutical Regulatory Agency (NPRA) Drug Register for full product details.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert warnings, contraindications, and drug interaction data were identified as data gaps in this Evidence Pack (DG001). Lithium Carbonate is a drug with a **narrow therapeutic index** and requires therapeutic drug monitoring. Before any repurposing exploration, a complete safety review from the official NPRA-approved prescribing information must be conducted.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.98%) to Lithium Carbonate for pseudoachondroplasia, but this is currently supported by **no clinical trials, no published literature, and no preclinical experimental data** — making this a pure computational hypothesis (Evidence Level L5). The proposed mechanistic link (GSK-3β inhibition → reduced ER stress → COMP aggregation correction) is biologically indirect and unvalidated, and the overall evidence base is insufficient to justify clinical or translational investment at this stage.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001**: Download and parse the NPRA-approved package insert PDF to extract official warnings, contraindications, and dosing guidance before any safety assessment can proceed
- **Resolve Data Gap DG002**: Query the DrugBank API to confirm the complete mechanism of action profile for Lithium Carbonate
- **Preclinical validation**: Conduct in vitro studies in COMP-mutant chondrocyte models (e.g., COMP-p.T585M iPSC-derived chondrocytes) to determine whether Lithium or GSK-3β inhibitors reduce ER stress markers
- **Literature scoping review**: Perform a broader search combining "lithium" with "ER stress," "chondrocyte," "COMP," and "skeletal dysplasia" to capture any mechanistic studies not captured by the current drug–disease pair query
- **Review WHIM syndrome separately**: Among the top-10 predicted indications, WHIM syndrome (Rank 9) presents a more mechanistically coherent hypothesis — Lithium's known neutrophil-mobilising effect aligns directionally with the WHIM pathophysiology of neutrophil bone marrow retention. This candidate may warrant a dedicated evidence review prior to pseudoachondroplasia

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

