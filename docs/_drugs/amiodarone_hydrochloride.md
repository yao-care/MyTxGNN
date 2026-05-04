---
layout: default
title: Amiodarone Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 0
---

# Amiodarone Hydrochloride
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

# Amiodarone Hydrochloride: Drug Repurposing Evaluation — Awaiting TxGNN Predictions

## One-Sentence Summary

Amiodarone Hydrochloride is a well-established Class III antiarrhythmic agent used for the management of ventricular and supraventricular arrhythmias.
**No TxGNN repurposing predictions have been generated yet** for this compound — the prediction pipeline has not been completed for this candidate.
This report documents the current data status and outlines the steps required before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiarrhythmic agent (formal approved indication text pending retrieval) |
| Predicted New Indication | Not yet generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — prediction pipeline not yet completed |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 7 |
| Recommended Decision | **Hold** — critical data gaps must be resolved first |

---

## Why Is This Prediction Reasonable?

No TxGNN repurposing predictions have been returned for Amiodarone Hydrochloride at this time, so a mechanistic rationale for a specific new indication cannot be provided in this report.

From established pharmacological knowledge, Amiodarone is a structurally unique Class III antiarrhythmic that exerts effects across multiple ion channels — blocking potassium, sodium, and calcium channels — while also exhibiting alpha- and beta-adrenergic blocking activity. This unusually broad electrophysiological profile has historically prompted researchers to explore its potential beyond arrhythmia, including in inflammatory conditions, certain infections, and even oncological contexts, though none of these directions have been formally evaluated through the TxGNN pipeline for this candidate.

Once the prediction pipeline is completed and a top-ranked disease target is identified, this section will be updated with a full mechanistic bridging analysis linking Amiodarone's known MOA to the predicted new indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — TxGNN repurposing prediction is pending. Once a target indication is identified, clinical trial evidence will be populated here.

---

## Literature Evidence

Currently no related literature available — TxGNN repurposing prediction is pending. Once a target indication is identified, supporting publications will be summarised here.

---

## Malaysia Market Information

Amiodarone Hydrochloride holds **7 product registrations** in Malaysia. However, the detailed licence records (product names, dosage forms, manufacturers, and approved indication text) were not returned in this Evidence Pack. The table below reflects the current data state; full details should be retrieved directly from the NPRA product registration database.

| Authorisation Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| (Pending retrieval) | — | — | — |

> **Note:** 7 registrations are confirmed as active. Full licence details require supplementation from the NPRA database query.

---

## Safety Considerations

Full safety data (warnings, contraindications, and key precautions) could not be assessed from this Evidence Pack. Retrieval of the official package insert is a **blocking requirement** before this candidate can advance to safety pre-screening (see Data Gaps below).

Based on widely published clinical literature, Amiodarone is broadly recognised as a drug with a significant interaction profile — it is a potent inhibitor of CYP2C9, CYP3A4, and P-glycoprotein, and carries well-documented risks including pulmonary toxicity, hepatotoxicity, thyroid dysfunction (both hypo- and hyperthyroidism), and corneal microdeposits. These known risks must be formally verified against the NPRA-approved package insert before any repurposing safety assessment proceeds.

No drug–drug interaction data was returned by the DDI query in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions are currently available, and two critical data gaps — safety warnings/contraindications (blocking severity) and mechanism of action (high severity) — must be resolved before this candidate can enter the standard evaluation workflow.

**To proceed, the following is needed:**

1. **[Blocking — DG001]** Retrieve the official package insert (warnings and contraindications) from the TFDA/NPRA website to enable Safety Pre-screening Step S1
2. **[High — DG002]** Query the DrugBank API to obtain the full MOA, drug categories, and cytotoxicity data; confirm the DrugBank ID (currently unresolved) to unlock DDI analysis
3. **[Pipeline]** Complete the TxGNN prediction run for Amiodarone Hydrochloride to generate ranked repurposing candidates — without this, no mechanistic or evidence analysis can be performed
4. **[Data Completeness]** Populate all 7 Malaysia NPRA licence records (product names, dosage forms, manufacturers, approved indication texts) from the NPRA product registration database
5. **[Re-evaluation]** Once the above are completed, re-generate the Evidence Pack and proceed to full L1–L5 evidence grading against the top-ranked predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

