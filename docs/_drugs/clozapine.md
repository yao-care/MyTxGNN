---
layout: default
title: Clozapine
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Clozapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Clozapine: From Treatment-Resistant Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Clozapine is a tricyclic dibenzodiazepine antipsychotic, globally recognized for treatment-resistant schizophrenia (the TFDA license-level indication text was not retrievable in this data pull). The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, but this evidence pack contains **0 clinical trials** and **0 publications** directly supporting the link — the case rests on mechanistic reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment-resistant schizophrenia *(known drug profile; TFDA/NPRA license text not retrieved — see Data Gap DG001)* |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 9 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, clozapine is an atypical antipsychotic that acts as a multi-receptor antagonist — most notably at dopamine D2/D4 and serotonin 5-HT2A receptors — and its efficacy in treatment-resistant schizophrenia is well established.

Mania with psychotic features and treatment-resistant schizophrenia sit close together on the psychosis spectrum, sharing overlapping dopaminergic/serotonergic dysregulation. The dossier's own rationale for this candidate notes that clozapine's dopamine/serotonin antagonism has mood-stabilizing potential, and that it is already used off-label in clinical practice for treatment-resistant mania and bipolar disorder with psychotic features.

Mechanistically this makes the prediction plausible, but it is important to note the rationale is explicitly labeled as **indirect evidence** in the source data — no trial or literature record in this pack corroborates it directly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*(Query log confirms explicit zero-result searches across ClinicalTrials.gov, ICTRP, and PubMed for "CLOZAPINE" + "manic bipolar affective disorder" on 2026-03-27.)*

---

## Malaysia Market Information

NPRA records show clozapine is marketed with **9 active registrations**, but this data extraction did not capture license-level detail (authorization numbers, product names, dosage forms, or approved indication text — all fields returned blank). This is a data gap, not an absence of registrations. Full license detail should be pulled directly from the NPRA product registry before use in any regulatory-facing document.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications are flagged as a **Blocking** data gap — DG001 — meaning this candidate cannot yet complete an S1 safety pre-screen. Clozapine carries well-known class-level monitoring requirements (e.g., absolute neutrophil count monitoring for agranulocytosis risk) under its existing label; these must be confirmed against the actual Malaysia package insert, not assumed from general knowledge, before any clinical use decision.)*

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link between clozapine's receptor-antagonist profile and mood stabilization in psychotic mania is biologically plausible and consistent with known off-label practice, but this evidence pack has zero clinical trials and zero literature records directly supporting the indication (Evidence Level L4) — the score reflects a knowledge-graph association, not corroborated clinical evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert — warnings, contraindications (DG001, **Blocking**)
- DrugBank mechanism-of-action detail (DG002)
- Broader literature/trial search using alternate terminology (current searches for "manic bipolar affective disorder" returned zero across all three sources; try "bipolar mania," "psychotic mania," "treatment-resistant bipolar disorder")
- Complete NPRA license-level detail (authorization numbers, product names, approved indication text)
- A formal hematological safety monitoring plan given clozapine's known agranulocytosis risk profile, before any indication-expansion discussion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

