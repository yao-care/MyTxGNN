---
layout: default
title: Asenapine Maleate
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 0
---

# Asenapine Maleate
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

# Asenapine Maleate: From Schizophrenia/Bipolar Disorder — Awaiting TxGNN Repurposing Prediction

## One-Sentence Summary

Asenapine maleate is an atypical antipsychotic approved for schizophrenia and acute manic/mixed episodes of bipolar I disorder, acting through multi-receptor antagonism across dopaminergic and serotonergic pathways.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, and critical data fields — including the approved indication text for both Malaysian registrations and mechanism of action details — are missing.
Before a repurposing direction can be evaluated, the identified data gaps must be resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Acute manic or mixed episodes of Bipolar I Disorder *(from pharmacological knowledge; approved indication text in Malaysia registry not retrieved)* |
| Predicted New Indication | — (No TxGNN prediction available in this Evidence Pack) |
| TxGNN Prediction Score | — |
| Evidence Level | N/A — No predictions available |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction is present in this Evidence Pack, so a mechanistic bridge to a new indication cannot be constructed at this stage.

From established pharmacology, asenapine maleate is a second-generation (atypical) antipsychotic with high-affinity antagonism at dopamine D₂, D₃, and D₄ receptors, serotonin 5-HT₂A, 5-HT₂B, 5-HT₂C, 5-HT₆, and 5-HT₇ receptors, as well as α₁- and α₂-adrenergic and histamine H₁ receptors. This broad receptor profile is the pharmacological basis for its efficacy in both positive and negative symptoms of schizophrenia and for mood stabilisation in bipolar mania. Research interest in this receptor fingerprint has historically pointed toward exploratory indications such as treatment-resistant depression, agitation in dementia, and pain modulation — but none of these can be confirmed or scored without a valid TxGNN prediction run.

The MOA data gap (DG002, rated **High** severity) and the absence of retrieved approved indication text from the Malaysian NPRA registry mean that both the mechanistic rationale and the regulatory baseline are currently unavailable within this data package. Remediation of these gaps is prerequisite to any meaningful repurposing analysis.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no disease-targeted clinical trial evidence can be presented. Once a repurposing candidate is identified, a targeted ClinicalTrials.gov and ICTRP query should be executed.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature can be presented. A PubMed systematic query should follow once the repurposing direction is established.

---

## Malaysia Market Information

Two product registrations are recorded in the Malaysian NPRA database, but the detailed fields (authorization number, product name, dosage form, approved indication text) were not populated in the Evidence Pack returned by the registry query.

| Item | Status |
|------|--------|
| Total Registrations | 2 |
| Authorization Numbers | Not retrieved |
| Product Names | Not retrieved |
| Dosage Forms | Not retrieved |
| Approved Indications | Not retrieved |

> **Action required**: Re-query NPRA with the full product name (e.g., *Saphris*) or MAL number to retrieve complete registration records.

---

## Safety Considerations

All safety fields in this Evidence Pack are flagged as data gaps. No drug–drug interaction records were found (DDI query status: `not_found`).

> Please refer to the Malaysian NPRA-approved package insert for safety information, including QT-interval prolongation risk, neuroleptic malignant syndrome, tardive dyskinesia, metabolic changes (weight gain, dyslipidaemia, hyperglycaemia), and orthostatic hypotension — all of which are class-level concerns for atypical antipsychotics.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack lacks the two elements required to initiate a repurposing evaluation: a TxGNN prediction score pointing to a candidate indication, and the approved indication text from the Malaysian NPRA registry. Without these, neither a mechanistic case nor a regulatory gap analysis can be performed.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Download and parse the TFDA/NPRA package insert PDF to extract approved indications, key warnings, and contraindications
- **[DG002 — High]** Query DrugBank API using the DrugBank ID for asenapine (DB06216) to retrieve verified MOA, pharmacodynamics, and toxicity data
- **Re-run TxGNN prediction pipeline** with asenapine maleate mapped to its correct DrugBank node to generate repurposing candidate scores
- **Retrieve full NPRA registration records** (authorization numbers, product names, dosage forms, indication texts) for the 2 existing Malaysian licenses
- Once predictions are available, execute a targeted **ClinicalTrials.gov**, **ICTRP**, and **PubMed** search for the top-ranked indication to establish an evidence level (L1–L5)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

