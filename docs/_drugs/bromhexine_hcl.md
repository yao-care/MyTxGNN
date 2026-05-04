---
layout: default
title: Bromhexine Hcl
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 0
---

# Bromhexine Hcl
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

# Bromhexine HCL: Mucolytic Agent — No New Indication Predicted

## One-Sentence Summary

Bromhexine HCL is a well-established mucolytic agent widely used for the relief of productive cough associated with respiratory conditions. The TxGNN model has **not generated any repurposing predictions** for this drug. With **37 registrations** in Malaysia confirming broad market availability, further data enrichment (DrugBank mapping, MOA, safety profile) is needed before repurposing analysis can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucolytic — relief of productive cough in respiratory disorders |
| Predicted New Indication | None (no TxGNN prediction available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No prediction generated |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 37 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Absent?

Bromhexine HCL is a mucolytic agent that works by depolymerising mucopolysaccharides and stimulating secretion of serous mucus in the respiratory tract, thereby reducing sputum viscosity and facilitating expectoration. It has been in clinical use globally for decades for bronchitis, asthma with mucus plugging, and other respiratory conditions with excessive mucus production.

The TxGNN model did not return any repurposing candidates for Bromhexine HCL. This may be attributable to one or more of the following factors: (1) the drug's DrugBank ID was not successfully mapped (`drugbank_id: null`), which would prevent the model from locating the drug within the knowledge graph; (2) Bromhexine's mechanism of action data was not available for the model to leverage; or (3) the drug's pharmacological profile did not yield high-confidence novel disease associations above the model's threshold.

To enable a meaningful repurposing analysis, the DrugBank mapping must first be resolved. Bromhexine HCL is listed in DrugBank (DB09015), and correcting this linkage would allow the knowledge graph and deep learning pipelines to generate scored predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials are available for evaluation, as no new indication has been predicted.

---

## Literature Evidence

Currently no related literature is available for evaluation, as no new indication has been predicted.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(Details not available)* | — | — | — |

> **Note:** While 37 NPRA registrations were retrieved for Bromhexine HCL, the individual license details (authorization number, product name, dosage form, and approved indication text) were not populated in the evidence pack. A follow-up query to the NPRA database is required to complete this section.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing prediction was generated for Bromhexine HCL, most likely due to a missing DrugBank ID mapping that prevents the drug from being located in the knowledge graph. Without a predicted indication, there is no candidate to evaluate.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping**: Map Bromhexine HCL to its DrugBank ID (DB09015) and re-run the TxGNN prediction pipeline (both KG and DL methods)
- **Obtain mechanism of action data**: Query DrugBank API to populate the MOA field for mechanistic reasoning
- **Populate NPRA license details**: Re-query the NPRA database to retrieve authorization numbers, product names, dosage forms, and approved indication text for the 37 registered products
- **Obtain safety profile**: Download and parse the package insert (PIL) for key warnings, contraindications, and drug interactions
- **Re-generate evidence pack**: Once the above data gaps are filled, re-run the full pipeline to produce an actionable repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

