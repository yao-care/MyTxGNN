---
layout: default
title: Bezafibrate
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 0
---

# Bezafibrate
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

# Bezafibrate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bezafibrate is a fibrate-class lipid-lowering agent, widely used for the treatment of hyperlipidaemia and hypertriglyceridaemia. The current evidence pack contains **no TxGNN-predicted new indications**, and critical data gaps (mechanism of action, safety profile) remain unresolved, preventing a meaningful repurposing assessment at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *(Not specified in evidence pack — see note below)* |
| Predicted New Indication | **None** (no TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — Model prediction not yet generated |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

> **Note on Original Indication:** The single registered licence in the evidence pack has an empty `approved_indication_text` field. Based on established pharmacological knowledge, Bezafibrate is a fibrate indicated for hyperlipidaemia and mixed dyslipidaemia.

---

## Why is This Prediction Reasonable?

Currently, **no new indication has been predicted by TxGNN** for Bezafibrate in this evidence pack. The `predicted_indications` array is empty, so a mechanistic plausibility assessment cannot be performed.

> Detailed mechanism of action data is not available in this evidence pack (flagged as Data Gap DG002). Based on established pharmacological knowledge, Bezafibrate is a pan-PPAR (peroxisome proliferator-activated receptor) agonist — primarily PPARα, with additional activity on PPARγ and PPARδ. It reduces triglycerides, raises HDL cholesterol, and has anti-inflammatory and insulin-sensitising properties. These pleiotropic effects make Bezafibrate a potentially interesting candidate for repurposing once TxGNN predictions become available.

Once TxGNN predictions are generated, the fibrate mechanism — particularly its broad PPAR modulation — should be evaluated for relevance to metabolic, inflammatory, and hepatobiliary diseases (e.g., primary biliary cholangitis, where Bezafibrate has emerging clinical evidence internationally).

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication exists for this drug. Clinical trial evidence cannot be mapped without a target indication.

---

## Literature Evidence

Currently no TxGNN-predicted indication exists for this drug. Literature evidence cannot be mapped without a target indication.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *(Not provided)* | *(Not provided)* | *(Not provided)* | *(Not provided)* |

> **Note:** The evidence pack confirms 1 registered licence with market status "Marketed" (已上市), but the licence detail fields (authorization number, product name, dosage form, and approved indication) are all empty. This data gap should be remediated by querying the NPRA database directly.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields in this evidence pack are marked as data gaps:
> - **Key Warnings**: Not available (Data Gap DG001 — Blocking severity)
> - **Contraindications**: Not available (Data Gap DG001)
> - **Drug Interactions**: No interactions found in current query
>
> **DG001 is classified as "Blocking"** — safety data must be obtained before any repurposing assessment can proceed to Stage 1 safety screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is incomplete. No TxGNN-predicted indications have been generated, and critical data gaps (MOA, safety profile, licence details) prevent any meaningful repurposing evaluation. The drug cannot proceed until these foundational data elements are in place.

**To proceed, the following is needed:**

1. **Run TxGNN prediction** — Execute the KG and/or DL prediction pipeline for Bezafibrate (DB01393) to generate candidate indications
2. **Resolve DG001 (Blocking)** — Obtain package insert warnings and contraindications from the NPRA website or product insert PDF
3. **Resolve DG002 (High)** — Query DrugBank API for full mechanism of action data
4. **Complete licence information** — Re-query NPRA for authorisation number, product name, dosage form, and approved indication text
5. **Re-generate evidence pack** — Once predictions and safety data are available, rebuild the evidence pack and re-evaluate

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

