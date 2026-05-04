---
layout: default
title: Diphenoxylate Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 0
---

# Diphenoxylate Hydrochloride
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

# Diphenoxylate Hydrochloride: Drug Repurposing Evaluation — Insufficient Prediction Data

## One-Sentence Summary

Diphenoxylate hydrochloride is an opioid-type antidiarrheal agent, typically used in combination with atropine to manage acute and chronic diarrhoea. The TxGNN model has **not generated any predicted new indications** for this drug. The evidence pack contains significant data gaps across regulatory details, mechanism of action, and safety information, precluding a meaningful repurposing assessment at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antidiarrheal (license details not available in current data) |
| Predicted New Indication | — None predicted |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 4 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

**No TxGNN prediction was generated for this drug**, so there is no repurposing hypothesis to evaluate at this time.

From general pharmacological knowledge, diphenoxylate is a synthetic phenylpiperidine opioid that acts primarily on mu-opioid receptors in the gastrointestinal tract. It slows intestinal motility and reduces fluid secretion, which is the basis of its antidiarrheal effect. It is almost always formulated in combination with a sub-therapeutic dose of atropine sulphate (marketed as Lomotil® and generics) to discourage deliberate misuse.

Detailed mechanism of action data was not available in this evidence pack (flagged as Data Gap DG002). Without a TxGNN prediction score or candidate disease, no mechanistic bridge to a new indication can be assessed.

---

## Clinical Trial Evidence

Currently no predicted indication exists, therefore no related clinical trials can be evaluated.

---

## Literature Evidence

Currently no predicted indication exists, therefore no targeted literature search was performed.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(not available)* | *(not available)* | *(not available)* | *(not available)* |

> **Note:** 4 registrations are recorded in the regulatory database, but the detailed licence information (authorization number, product name, dosage form, and approved indication text) was not populated in the current evidence pack. This data should be retrieved from the NPRA database to complete the assessment.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, drug–drug interactions) are currently flagged as data gaps. Before any repurposing evaluation can proceed, the following must be obtained:
> - Package insert warnings and precautions (Data Gap DG001 — severity: **Blocking**)
> - Drug–drug interaction profile (query returned 0 results)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not produce any predicted new indications for diphenoxylate hydrochloride. In addition, the evidence pack has multiple blocking-level data gaps (safety information, regulatory detail, mechanism of action), making it impossible to conduct a meaningful repurposing evaluation.

**To proceed, the following is needed:**
- **TxGNN prediction re-run**: Confirm that diphenoxylate hydrochloride (or its DrugBank ID) is correctly mapped in the knowledge graph; if the DrugBank mapping failed, resolve the identifier first (Data Gap DG002)
- **DrugBank ID resolution**: The `drugbank_id` is currently null — query DrugBank for "Diphenoxylate" (expected: DB01081) and re-run the prediction pipeline
- **NPRA licence detail retrieval**: Populate the 4 licence records with authorization numbers, product names, dosage forms, and approved indication text
- **Safety data extraction**: Download and parse the package insert PDF from NPRA to obtain warnings, contraindications, and interaction data (Data Gap DG001 — **Blocking**)
- **Mechanism of action documentation**: Retrieve MOA details from DrugBank to enable future mechanistic plausibility analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

