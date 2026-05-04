---
layout: default
title: Artesunate
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Artesunate
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

# Artesunate: Antimalarial Drug — Repurposing Evaluation (Preliminary)

## One-Sentence Summary

Artesunate (DrugBank: DB09274) is a well-established artemisinin-derived antimalarial agent, currently holding one active market authorisation in Malaysia.
However, this Evidence Pack contains critical data gaps — **no TxGNN predictions were returned**, and mechanism of action, regulatory indication text, and safety data are all absent — meaning a complete drug repurposing evaluation **cannot be finalised at this stage**.
Immediate data remediation is required before proceeding to evidence synthesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (inferred from drug class; approved indication text not available in current pack) |
| Predicted New Indication | No predictions available in current data |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — insufficient data to assign level |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack, and the TxGNN model returned no repurposing candidates for this compound.

Artesunate belongs to the artemisinin class of antimalarials. Its primary clinical role is in treating severe and uncomplicated *Plasmodium* infections. Prior research has suggested that artemisinins may exert cytotoxic activity through iron-dependent free radical generation, which has prompted exploratory investigation into oncology applications — however, this evidence base is **not reflected in the current Evidence Pack** and cannot be formally evaluated here.

Without a confirmed predicted indication, a mechanism-to-indication bridging analysis is not applicable at this time. Once TxGNN predictions are successfully generated, this section should be revisited to assess whether the known antimalarial mechanism is mechanistically plausible for the predicted new indication.

---

## Clinical Trial Evidence

No predicted indication is available in the current Evidence Pack. Clinical trial evidence cannot be extracted or summarised.

Once a target indication is identified from TxGNN output, relevant trials should be retrieved from `predicted_indications[0].evidence.clinical_trials`.

---

## Literature Evidence

No predicted indication is available in the current Evidence Pack. Literature evidence cannot be extracted or summarised.

Once a target indication is identified, relevant publications should be retrieved from `predicted_indications[0].evidence.literature`.

---

## Malaysia Market Information

The Evidence Pack confirms **1 active market authorisation** in Malaysia; however, all registration detail fields are currently empty.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| *(Not available)* | *(Not available)* | *(Not available)* | *(Not available — requires NPRA record retrieval)* |

To populate this table, the full NPRA registration record for Artesunate must be retrieved and parsed.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All safety fields in this Evidence Pack — including key warnings, contraindications, and drug-drug interactions — are either marked as data gaps or returned no results. This is classified as a **Blocking** data gap (DG001) that prevents any safety-dependent evaluation steps.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is incomplete in two blocking dimensions: (1) the TxGNN prediction pipeline returned no repurposing candidates for Artesunate, and (2) critical safety and regulatory data are absent. No evidence-based repurposing recommendation can be made in the current state.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve and parse the NPRA/TFDA package insert PDF to extract approved indication, key warnings, and contraindications
- **[High — DG002]** Query the DrugBank API for Artesunate (DB09274) to retrieve the mechanism of action, pharmacodynamics, and drug categories
- **[Blocking — Predictions]** Diagnose why `predicted_indications` is empty — verify that Artesunate's DrugBank ID is present in the TxGNN knowledge graph node list (`data/node.csv`) and re-run the prediction pipeline (`scripts/run_kg_prediction.py`)
- **[Medium]** Populate NPRA licence details (product name, dosage form, authorisation number) from the regulatory record confirmed as present (1 registration found)
- **[Post-remediation]** Once predictions and MOA are available, re-run the full Evidence Pack generation to enable a complete L1–L5 evidence-level assessment and a Go / Proceed with Guardrails decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

