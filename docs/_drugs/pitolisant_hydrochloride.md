---
layout: default
title: Pitolisant Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 0
---

# Pitolisant Hydrochloride
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

# Pitolisant Hydrochloride: Narcolepsy Treatment — Repurposing Analysis Pending

## One-Sentence Summary

Pitolisant Hydrochloride is a histamine H3 receptor antagonist/inverse agonist approved for narcolepsy (with or without cataplexy), promoting wakefulness by enhancing endogenous histamine neurotransmission. This Evidence Pack contains **no TxGNN-predicted new indications**, as the prediction pipeline did not return candidates for this drug. With critical data gaps in MOA documentation, safety warnings, and licence details, **a full repurposing evaluation cannot be completed at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Narcolepsy (excessive daytime sleepiness / cataplexy) |
| Predicted New Indication | — (No predictions returned) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — Model prediction only (no output generated) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction is available in this Evidence Pack; therefore, a mechanism-based bridge to a new indication cannot be formally constructed at this stage.

From published pharmacological knowledge, pitolisant acts as an inverse agonist at presynaptic histamine H3 auto-receptors, relieving tonic inhibition and increasing cortical histamine release. This wake-promoting mechanism is mechanistically distinct from amphetamine-class stimulants, making it a candidate of interest for other CNS disorders characterised by hypersomnia, cognitive impairment, or attentional deficits (e.g., idiopathic hypersomnia, ADHD, Parkinson's disease fatigue).

Currently, detailed MOA documentation and DrugBank linkage are absent from this Evidence Pack (DG002). Retrieval of the DrugBank record (expected ID: DB11909) and the full NPRA/TFDA package insert is required before mechanism-based applicability to any new indication can be formally assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in this Evidence Pack.

> **Note**: ClinicalTrials.gov and ICTRP queries were not executed as part of this pipeline run (no predicted indication to query against). Manual searches for pitolisant in indications such as idiopathic hypersomnia, obstructive sleep apnea, and ADHD are recommended as a next step.

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

> **Note**: PubMed evidence collection requires a predicted indication target. Once a repurposing candidate is identified, the evidence collector should be re-run.

---

## Malaysia Market Information

Two registrations are recorded in the Malaysia NPRA database; however, **all licence detail fields are empty in the current Evidence Pack**. The table below reflects the available (null) data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|-------------|-------------|---------------------|
| — | — | — | — |
| — | — | — | — |

> **Action Required**: Download the NPRA licence records directly from the NPRA ePortal to obtain the MAL numbers, product names (expected: Wakix®), dosage forms (film-coated tablet, 4.5 mg / 18 mg), and approved indication texts.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields in this Evidence Pack are flagged as data gaps (DG001 — Severity: **Blocking**). Key warnings and contraindications could not be assessed. Known safety signals from the international label (QTc prolongation, foetal risk in pregnancy, CYP2D6-dependent exposure variability, interactions with MAOIs and CNS depressants) should be reviewed manually from the NPRA-approved SmPC or TFDA package insert before any repurposing evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is incomplete — no TxGNN repurposing predictions were generated, and two blocking or high-severity data gaps (DG001, DG002) prevent both safety pre-screening and mechanism-of-action analysis. A repurposing evaluation cannot be responsibly issued without this foundational data.

**To proceed, the following is needed:**

- [ ] **DG001 (Blocking)** — Download and parse the NPRA/TFDA package insert PDF to extract key warnings and contraindications; this must be resolved before any Safety Stage S1 assessment
- [ ] **DG002 (High)** — Query DrugBank API for pitolisant (expected: DB11909) to retrieve MOA, drug categories, and toxicity data
- [ ] **Re-run TxGNN prediction pipeline** — With a valid DrugBank ID and mapped indications, generate repurposing candidates so that clinical trial and literature evidence collection can proceed
- [ ] **Populate NPRA licence details** — Retrieve MAL registration numbers, product names, dosage forms, and approved indication texts from the NPRA ePortal
- [ ] **Confirm INN alignment** — The Evidence Pack uses "PITOLISANT HYDROCHLORIDE" (salt form); ensure the prediction pipeline correctly maps this to the free-base INN "pitolisant" in the TxGNN knowledge graph

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

