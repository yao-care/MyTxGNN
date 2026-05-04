---
layout: default
title: Diltiazem Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 0
---

# Diltiazem Hydrochloride
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

# Diltiazem Hydrochloride: Drug Repurposing Evaluation — Pending Prediction Data

## One-Sentence Summary

Diltiazem Hydrochloride is a benzothiazepine-class calcium channel blocker widely used for hypertension, angina pectoris, and certain cardiac arrhythmias. Currently, the TxGNN model has **no predicted new indications** on file for this compound, and the evidence pack contains significant data gaps in regulatory details, safety information, and mechanism of action, preventing a meaningful repurposing evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris, arrhythmias (per established pharmacology; licence-level detail not available in this pack) |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN-predicted indication exists for Diltiazem Hydrochloride in this evidence pack, so a mechanistic plausibility analysis cannot be performed.

For reference, Diltiazem Hydrochloride is a well-characterised non-dihydropyridine calcium channel blocker. It inhibits the influx of extracellular calcium ions through L-type calcium channels in vascular smooth muscle and cardiac myocytes. This results in vasodilation (reducing blood pressure and coronary vasospasm) and slowing of atrioventricular conduction (useful in rate control of supraventricular tachyarrhythmias). The evidence pack lists the mechanism of action as a data gap; however, the pharmacology is extensively documented in the literature and in DrugBank (DB00343).

Once TxGNN predictions are generated and populated into this evidence pack, the mechanistic plausibility of any candidate indication should be evaluated against Diltiazem's calcium-channel-blocking, vasodilatory, and negative chronotropic properties.

---

## Malaysia Market Information

The evidence pack records **6 product registrations** with market status "Marketed." However, all licence-level details (authorisation numbers, product names, dosage forms, and approved indication text) are currently missing from the data.

| Item | Status |
|------|--------|
| Total Registrations | 6 |
| Market Status | Marketed |
| Licence Details | Not available — data fields are empty |

> **Action required:** Retrieve complete NPRA registration records for Diltiazem Hydrochloride to populate authorisation numbers, product names, dosage forms, and approved indication text.

---

## Safety Considerations

> Please refer to the package insert for safety information.

All safety fields (key warnings, contraindications, drug–drug interactions) are marked as data gaps in this evidence pack. The DrugBank query log shows a successful query (result_count = 1), suggesting that safety data may be retrievable but was not integrated into this pack.

**Known safety profile (general pharmacological knowledge):**
- Diltiazem is contraindicated in severe hypotension, sick sinus syndrome (without pacemaker), second- or third-degree AV block, and acute myocardial infarction with pulmonary congestion.
- Significant drug interactions exist with beta-blockers (additive cardiac depression), CYP3A4 substrates (Diltiazem is a moderate CYP3A4 inhibitor), cyclosporine, simvastatin, and other agents.
- Common adverse effects include bradycardia, oedema, dizziness, and headache.

> **Action required:** Download and parse the package insert (仿單) from the regulatory authority and populate the safety fields.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack lacks critical data needed for a drug repurposing evaluation. There are **no TxGNN-predicted indications**, the DrugBank ID is not linked (despite a successful query), licence-level regulatory details are missing, and all safety fields are empty. Without a candidate indication to evaluate, no repurposing assessment can proceed.

**To proceed, the following is needed:**

1. **Run TxGNN prediction pipeline** for Diltiazem Hydrochloride and populate `predicted_indications` with candidate diseases, scores, clinical trials, and literature evidence
2. **Link DrugBank ID** — the query log confirms DB lookup succeeded (result_count = 1); map to **DB00343** and retrieve MOA, pharmacodynamics, and toxicity data
3. **Populate NPRA licence details** — retrieve authorisation numbers, product names, dosage forms, and approved indication text for all 6 registered products
4. **Retrieve safety data** — download package insert and parse key warnings, contraindications, and drug interaction information (addresses Blocking data gap DG001)
5. **Populate MOA field** — retrieve mechanism of action from DrugBank to enable mechanistic plausibility analysis (addresses High-severity data gap DG002)

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

