---
layout: default
title: Aripiprazole Monohydrate
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 0
---

# Aripiprazole Monohydrate
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

# Aripiprazole Monohydrate: Drug Repurposing Evaluation — Pending TxGNN Prediction Data

---

## One-Sentence Summary

Aripiprazole monohydrate is an atypical antipsychotic (second-generation), widely established for the treatment of schizophrenia, bipolar I disorder, and adjunctive major depressive disorder treatment.
This Evidence Pack confirms **1 active Malaysian market registration**, but **TxGNN repurposing predictions are not yet available** — the `predicted_indications` array is empty, which means a full indication-to-indication evaluation cannot be completed at this stage.
The report is therefore classified as **incomplete** and a **Hold** decision is recommended until prediction data, mechanism of action, and full regulatory licence details are retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar I disorder; Adjunctive major depressive disorder *(from established pharmacological knowledge — not present in current Evidence Pack)* |
| Predicted New Indication | **Pending** — TxGNN prediction data not yet available |
| TxGNN Prediction Score | Pending |
| Evidence Level | **Undetermined** (no predictions to evaluate) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, aripiprazole monohydrate is an atypical antipsychotic belonging to the quinolinone class. It acts as a **partial agonist at dopamine D2 and D3 receptors** and **serotonin 5-HT1A receptors**, and as an **antagonist at 5-HT2A receptors**. This unique "dopamine system stabiliser" profile distinguishes it from earlier antipsychotics that act as full D2 antagonists.

Because aripiprazole modulates both dopaminergic and serotonergic pathways simultaneously, it has generated research interest in conditions beyond classical psychosis — including impulse-control disorders, autism spectrum disorder–related irritability, Tourette syndrome, and treatment-resistant depression. These cross-indication mechanistic bridges make aripiprazole a plausible candidate for drug repurposing studies.

However, **no TxGNN model prediction scores or candidate diseases are present in this Evidence Pack**. Until the prediction pipeline is re-run and results are populated, no specific new indication can be formally evaluated, and the above mechanistic narrative cannot be linked to a quantitative evidence assessment.

---

## Clinical Trial Evidence

TxGNN prediction data is not yet available in this Evidence Pack. Once a target indication is identified, clinical trial evidence will be retrieved from ClinicalTrials.gov and ICTRP.

Currently no related clinical trials are linked to this evaluation.

---

## Literature Evidence

TxGNN prediction data is not yet available in this Evidence Pack. Once a target indication is identified, PubMed literature evidence will be retrieved and assessed.

Currently no related literature is linked to this evaluation.

---

## Malaysia Market Information

The Evidence Pack confirms **1 active registration** with Malaysia NPRA and a market status of **已上市 (Marketed)**. However, the licence detail fields (registration number, product name, dosage form, manufacturer, approved indication text) were returned as empty strings in the current data extract.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| *(not retrieved)* | *(not retrieved)* | *(not retrieved)* | *(not retrieved)* |

> **Action Required:** Re-query the NPRA database to retrieve full licence record details for ARIPIPRAZOLE MONOHYDRATE.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Both key warnings and contraindications are flagged as data gaps in this Evidence Pack (severity: Blocking and High respectively). No drug–drug interaction records were returned. Safety assessment cannot proceed until the full prescribing information is obtained from the NPRA product monograph or the official package insert PDF.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is structurally incomplete — TxGNN predictions, mechanism of action data, licence details, and safety information are all absent or empty, making it impossible to perform a meaningful repurposing evaluation at this time.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download and parse the NPRA/TFDA package insert PDF to extract approved indications, key warnings, and contraindications; this is required before any safety pre-screening (S1) can begin
- **[High — DG002]** Query the DrugBank API using the drug name `ARIPIPRAZOLE MONOHYDRATE` to retrieve the DrugBank ID, full mechanism of action, pharmacological categories, and toxicity profile
- **[Critical]** Re-run the TxGNN prediction pipeline — the `predicted_indications` array is empty; without at least one candidate disease, the report cannot be completed
- **[Required]** Re-query NPRA to retrieve complete licence record fields (registration number, product name, dosage form, approved indication text)
- **[Optional]** Confirm whether the monohydrate salt form shares DrugBank entries with the free base form of aripiprazole (DrugBank ID: DB01238) to avoid mapping failures
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

