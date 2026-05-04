---
layout: default
title: Amlodipine Besylate
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 0
---

# Amlodipine Besylate
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

# Amlodipine Besylate: From Hypertension/Angina — Repurposing Predictions Not Yet Available

## One-Sentence Summary

Amlodipine Besylate is a well-established dihydropyridine calcium channel blocker widely prescribed for hypertension and angina pectoris, with 50 registered product licences in Malaysia. The current Evidence Pack contains **no TxGNN-generated repurposing predictions** for this compound, as the DrugBank ID linkage and mechanism of action data are both unresolved data gaps. This report summarises available information and recommends a **Hold** decision until the pipeline is completed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in this Evidence Pack |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 50 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction was generated for Amlodipine Besylate in this Evidence Pack. The `predicted_indications` array is empty, which typically indicates that the compound could not be successfully linked to a node in the TxGNN knowledge graph — most likely because the DrugBank ID was not resolved (recorded as `null` despite a successful DrugBank API query on 2026-03-27).

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on general pharmacological knowledge, Amlodipine Besylate is a long-acting dihydropyridine-class calcium channel blocker. It selectively inhibits the voltage-gated L-type calcium channel in vascular smooth muscle and cardiac myocytes, reducing peripheral vascular resistance and myocardial oxygen demand. This mechanism underpins its established use in hypertension and chronic stable or vasospastic angina. Calcium channel blockade has also been explored in adjacent therapeutic areas — including Raynaud's phenomenon, pulmonary arterial hypertension, and subarachnoid haemorrhage-associated vasospasm — though none of these appear as predictions in the present pack.

To generate valid repurposing candidates, the data pipeline must first confirm the DrugBank ID (expected: **DB00381**), link the compound to the TxGNN knowledge graph node, and re-execute the prediction run.

---

## Clinical Trial Evidence

No TxGNN-predicted indication is available for this compound. Disease-specific clinical trial evidence cannot be presented until a target indication is identified by the prediction model.

Currently no related clinical trials registered under a repurposing context.

---

## Literature Evidence

No TxGNN-predicted indication is available for this compound. Disease-specific literature evidence cannot be presented until a target indication is identified by the prediction model.

Currently no related literature available under a repurposing context.

---

## Malaysia Market Information

Amlodipine Besylate holds **50 registered product licences** with the Malaysian National Pharmaceutical Regulatory Agency (NPRA), confirmed by query on 2026-03-27. However, individual product-level details (licence numbers, product names, dosage forms, approved indication text) were not returned in this Evidence Pack.

| Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | Details not populated in this Evidence Pack | — | — |

> **Note**: 50 active licences confirmed via NPRA. Full product-level records should be retrieved directly from the NPRA portal to populate the table above before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug interactions) are flagged as data gaps in this Evidence Pack. No interactions were returned by the DDI query. This is likely due to the unresolved DrugBank ID rather than a true absence of interactions — Amlodipine is known to have clinically relevant interactions with CYP3A4 inhibitors/inducers.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is structurally incomplete — the TxGNN prediction pipeline was not able to generate any repurposing candidates because the DrugBank ID linkage failed, and all safety and indication fields are unresolved data gaps. A meaningful repurposing evaluation cannot proceed in this state.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve approved indication text and full safety warnings (contraindications, black-box warnings) from the Malaysia NPRA-registered product inserts; these are required before any safety screening can occur.
- **[High — DG002]** Confirm and record the DrugBank ID for Amlodipine Besylate (expected: **DB00381**) via the DrugBank API, and extract the full mechanism of action entry to support mechanistic plausibility analysis.
- **Re-run TxGNN prediction pipeline** with the confirmed DrugBank ID to generate repurposing candidates; this will unlock all downstream sections (predicted indications, clinical trial evidence, literature evidence).
- **Populate all 50 NPRA licence records** with complete product details (product name, dosage form, approved indication text) to enable a proper Malaysia market summary.
- Once all gaps are resolved, **re-generate this report** using the completed Evidence Pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

