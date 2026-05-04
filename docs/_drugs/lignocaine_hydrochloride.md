---
layout: default
title: Lignocaine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 0
---

# Lignocaine Hydrochloride
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

# Lignocaine Hydrochloride: From Local Anaesthesia — Repurposing Evaluation (Data Supplement Required)

## One-Sentence Summary

Lignocaine Hydrochloride (Lidocaine) is a well-established local anaesthetic and Class Ib antiarrhythmic agent with decades of clinical use across multiple routes of administration.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, and detailed regulatory licence information was not retrieved.
**A complete repurposing evaluation cannot be finalised until data gaps DG001 (safety warnings) and DG002 (MOA) are resolved.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anaesthesia; ventricular arrhythmia *(general pharmacological knowledge; approved indication text not present in current data)* |
| Predicted New Indication | Not available — no TxGNN predictions in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — insufficient data for higher classification |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No new indication has been predicted in this Evidence Pack, so a mechanistic link analysis cannot be performed at this stage.

Currently, detailed mechanism of action data is not available in the Evidence Pack (Data Gap DG002). Based on established pharmacological knowledge, Lignocaine Hydrochloride is a **voltage-gated sodium channel blocker**. It stabilises excitable membranes by inhibiting ionic flux required for impulse initiation and conduction — underpinning both its local anaesthetic effect (peripheral nerve blockade) and its antiarrhythmic activity (Class Ib: shortens action potential duration and effective refractory period).

Emerging preclinical and clinical research has explored lignocaine's potential in perioperative oncology (anti-tumour and anti-metastatic effects), chronic neuropathic pain, and systemic inflammatory states — however, these directions require formal TxGNN scoring and structured evidence review before any repurposing recommendation can be issued.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a repurposing indication in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available for a repurposing indication in this Evidence Pack.

---

## Malaysia Market Information

Lignocaine Hydrochloride is registered in Malaysia (NPRA) with **6 active licences**. Detailed licence-level information (authorisation numbers, product names, dosage forms, and approved indication texts) was not retrieved in this Evidence Pack and must be supplemented directly from the NPRA database.

| Authorisation Number | Product Name | Dosage Form | Approved Indication |
|----------------------|-------------|------------|---------------------|
| — | — | — | Data not available — query NPRA portal for full licence details |

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ Data Gap DG001 (Severity: **Blocking**): NPRA/TFDA package insert warnings and contraindications have not been retrieved. This gap **blocks entry into the S1 safety screening stage**. Remediation: download the package insert PDF from the NPRA/TFDA official website and parse the warnings and contraindications sections.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack lacks the minimum required data for a drug repurposing evaluation — no TxGNN predictions are present, regulatory licence details are absent, and safety data has not been retrieved. Proceeding without these elements would result in an unsupported recommendation.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download and parse the NPRA/TFDA package insert PDF to extract warnings, contraindications, and approved indication texts
- **[High — DG002]** Retrieve DrugBank ID and MOA data — the query log confirms 1 DrugBank result was found; this record should be extracted and linked
- Run the TxGNN prediction pipeline for Lignocaine Hydrochloride to generate repurposing candidate scores and disease rankings
- Populate all 6 NPRA licence records with authorisation numbers, product names, dosage forms, and approved indications
- Re-generate the Evidence Pack once DG001 and DG002 are resolved, then proceed to S1 safety and S2 mechanistic screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

