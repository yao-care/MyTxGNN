---
layout: default
title: Linezolid
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 0
---

# Linezolid
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

# Linezolid: Drug Repurposing Evaluation Report (TxGNN Predictions Pending)

## One-Sentence Summary

Linezolid is a synthetic oxazolidinone-class antibiotic approved for treating serious Gram-positive bacterial infections, including those caused by methicillin-resistant *Staphylococcus aureus* (MRSA) and vancomycin-resistant *Enterococcus* (VRE).
At this time, **no TxGNN repurposing predictions are available** for this drug, as the `predicted_indications` list in the current Evidence Pack is empty.
Without a prediction target, a full mechanistic and clinical evidence evaluation cannot be completed; this report documents the current data status and outlines the steps needed before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrievable from current data (all license detail fields are empty) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no prediction target to assess |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

This section cannot be completed in its standard form because no repurposing target has been predicted. The following contextual information is provided based on publicly known pharmacology to support future evaluation once predictions are generated.

Linezolid inhibits bacterial protein synthesis by binding to the 23S ribosomal RNA component of the 50S ribosomal subunit, thereby preventing formation of the 70S initiation complex. This mechanism is distinct from all other antibiotic classes, which explains its activity against multidrug-resistant Gram-positive organisms. Within the drug repurposing literature, oxazolidinone scaffolds have attracted interest beyond infectious disease — notably in oncology (ribosomal biology overlap) and some inflammatory conditions — though no such prediction is available in this pack.

The MOA field is currently flagged as a data gap (DG002). Retrieving the full DrugBank MOA entry should be the first remediation step, as it is foundational to any mechanistic plausibility argument for a predicted new indication.

---

## Clinical Trial Evidence

No predicted indication is available in this Evidence Pack; therefore, no disease-specific clinical trial evidence can be presented.

Once a prediction target is confirmed, the ClinicalTrials.gov and ICTRP collectors should be queried for that specific drug–disease pair.

---

## Literature Evidence

No predicted indication is available in this Evidence Pack; therefore, no disease-specific literature evidence can be presented.

---

## Malaysia Market Information

Nine active registrations are recorded with the National Pharmaceutical Regulatory Agency (NPRA) of Malaysia. However, all license detail fields (authorization number, product name, dosage form, approved indication) were returned as empty strings in the current Evidence Pack. The table below reflects this data gap.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Detailed fields not populated in current data pull |

> **Action required:** Re-query the NPRA database with explicit field extraction for all 9 registrations, or download the corresponding product information leaflets, to populate this table.

---

## Safety Considerations

All safety fields in the current Evidence Pack are flagged as data gaps:

- **Key Warnings**: Not available (DG001 — Blocking severity)
- **Contraindications**: Not available (DG001 — Blocking severity)
- **Drug Interactions**: Query returned no results (DDI status: `not_found`)

> Please refer to the package insert (SmPC / PIL) available on the NPRA or originator (Pfizer) product pages for complete safety information. Linezolid is known to carry important warnings regarding myelosuppression, serotonin syndrome (in combination with serotonergic agents), peripheral and optic neuropathy, and lactic acidosis — these must be formally extracted before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Linezolid currently contains no TxGNN repurposing predictions and is missing all safety, MOA, and regulatory detail data. There is no actionable prediction to evaluate, and three of the four data domains required for a standard assessment are incomplete.

**To proceed, the following is needed:**

- **[Critical — DG001]** Download and parse NPRA / originator product insert PDFs to extract approved indications, warnings, and contraindications for all 9 registered products.
- **[Critical — DG002]** Query the DrugBank API for Linezolid (DB00601) to retrieve the full mechanism of action, pharmacodynamics, and toxicity profile.
- **[Critical]** Re-run the TxGNN prediction pipeline to generate `predicted_indications` for Linezolid; confirm whether the empty list reflects a true model output (no candidates above threshold) or a pipeline failure.
- **[High]** Re-query NPRA with structured field extraction to populate all 9 license records (authorization number, product name, dosage form, indication text).
- **[Medium]** Rerun the DDI query against DrugBank interaction data (the `not_found` status may reflect a query issue rather than a genuine absence of interactions, given linezolid's well-known serotonergic interaction profile).
- **[Medium]** Once a prediction target is confirmed, run ClinicalTrials.gov and PubMed collectors for that specific drug–disease pair to establish an evidence level (L1–L5).

---

*This report is for research reference only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

