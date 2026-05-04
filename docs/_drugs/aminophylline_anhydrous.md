---
layout: default
title: Aminophylline Anhydrous
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Aminophylline Anhydrous
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

# Aminophylline Anhydrous: Bronchodilator with Insufficient Repurposing Data

## One-Sentence Summary

Aminophylline Anhydrous is a methylxanthine bronchodilator classically used for bronchial asthma and chronic obstructive pulmonary disease (COPD).
No TxGNN repurposing predictions are currently available for this drug — the `predicted_indications` field is empty — meaning **no new indication target** and **no supporting evidence** can be reported at this time.
This report documents the current data status and outlines remediation steps before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchial asthma / COPD / Acute bronchospasm (based on known pharmacology; package insert text not retrieved) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (Model prediction not yet generated) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction is available for this candidate at the time of report generation (`predicted_indications: []`). Therefore, a mechanistic link to any new indication cannot be evaluated.

From established pharmacology, Aminophylline is a 2:1 complex of theophylline and ethylenediamine. Theophylline acts primarily as a **non-selective phosphodiesterase (PDE) inhibitor**, raising intracellular cAMP and cGMP levels, leading to bronchial smooth muscle relaxation. It also acts as an **adenosine receptor antagonist** (A1, A2A), which accounts for secondary effects including positive chronotropy, mild diuresis, and central respiratory stimulation.

These pleiotropic mechanisms — particularly adenosine antagonism and anti-inflammatory effects via PDE4 inhibition — have historically generated interest in repositioning xanthines toward neurological, cardiological, and inflammatory conditions. However, without TxGNN scores or supporting evidence, no specific repurposing candidate can be recommended at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a predicted new indication (prediction data unavailable).

---

## Literature Evidence

Currently no related literature available for a predicted new indication (prediction data unavailable).

---

## Malaysia Market Information

The Evidence Pack reports **1 active registration** in Malaysia, but all license detail fields (authorization number, product name, dosage form, manufacturer, approved indication text) were returned as empty strings. The following is a placeholder pending data retrieval:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|-------------|-------------|---------------------|
| *(Pending retrieval)* | Aminophylline Anhydrous | *(Pending)* | *(Pending — download package insert from NPRA portal)* |

> **Action required**: Query the NPRA product database directly for the single registered product to populate these fields.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug interactions) were returned as `[Data Gap]` or empty. The following known safety concerns are documented in international references and should be verified against the Malaysian-approved package insert before clinical use:
>
> - **Narrow therapeutic index**: Theophylline serum levels must be monitored (target 10–20 µg/mL; toxicity above 20 µg/mL).
> - **Cardiovascular**: Tachycardia, arrhythmia, and hypotension risk — use with caution in cardiac disease.
> - **CNS**: Seizures reported at toxic concentrations.
> - **Drug interactions**: Multiple significant interactions (e.g., with ciprofloxacin, cimetidine, rifampicin, phenytoin) that alter theophylline clearance; DDI module returned 0 results and requires re-query.
>
> These are reference observations only and do not substitute for the approved local label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline has not returned any repurposing candidates for Aminophylline Anhydrous, making it impossible to identify a new indication, assess mechanistic plausibility, or evaluate supporting evidence. The safety profile cannot be formally reviewed until the package insert is retrieved.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN prediction** — Confirm that `AMINOPHYLLINE ANHYDROUS` is correctly mapped to its DrugBank entry (theophylline: DB00277; aminophylline: DB01223) and re-execute the KG and DL prediction pipelines to populate `predicted_indications`.
- [ ] **Resolve DrugBank ID** — `drugbank_id` is `null`; link to DrugBank DB01223 (aminophylline) or DB00277 (theophylline) to unlock MOA, toxicity, and DDI data.
- [ ] **Retrieve NPRA package insert** — Download and parse the PDF from the NPRA portal to populate `approved_indication_text`, warnings, and contraindications (Data Gaps DG001, DG002).
- [ ] **Populate license details** — The single registration record has all fields empty; retrieve product name, dosage form, and manufacturer from the NPRA database.
- [ ] **Re-query DDI module** — Once DrugBank ID is resolved, re-run the drug–drug interaction query to replace the empty `interactions` array.
- [ ] **Re-issue this report** after the above data gaps are resolved to enable a full L1–L5 evidence grading and a substantive Go / Proceed with Guardrails decision.

---

> ⚠️ *This report is for research reference only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

