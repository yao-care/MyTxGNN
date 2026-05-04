---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# Acalabrutinib
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

# Acalabrutinib: Evidence Pack Incomplete – Prediction Data Pending

---

## One-Sentence Summary

Acalabrutinib (Calquence) is a second-generation Bruton's Tyrosine Kinase (BTK) inhibitor used for B-cell malignancies including chronic lymphocytic leukaemia (CLL) and mantle cell lymphoma (MCL).
The current Evidence Pack (v4) contains **no TxGNN-predicted new indications** — the `predicted_indications` field is empty — meaning a formal repurposing evaluation cannot yet proceed.
Two unresolved data gaps (missing package insert warnings and MOA data) must be addressed before this candidate can advance to screening.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | B-cell malignancies (CLL, SLL, MCL) — from public knowledge; approved indication text not populated in Evidence Pack |
| Predicted New Indication | Not available (prediction pipeline output is empty) |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indications are present in the current Evidence Pack. The `predicted_indications` array is empty, which prevents any formal repurposing hypothesis from being assessed at this time.

From publicly available information, Acalabrutinib is a highly selective, irreversible BTK inhibitor that covalently binds to Cys481 within the BTK active site. This blocks B-cell receptor (BCR) downstream signalling — including PI3K/AKT and NF-κB pathways — which are essential for survival, proliferation, and homing of malignant B cells. Compared to first-generation BTK inhibitors such as ibrutinib, Acalabrutinib exhibits improved kinase selectivity, which reduces off-target effects and may widen its eventual repurposing profile.

Once TxGNN prediction outputs become available, mechanistic plausibility can be formally evaluated. Domains where BTK inhibition has attracted early scientific interest beyond established haematological indications include autoimmune conditions (systemic lupus erythematosus, rheumatoid arthritis, multiple sclerosis) and selected solid tumours — but no recommendation can be made until prediction data is populated.

---

## Clinical Trial Evidence

Currently no related clinical trial evidence can be presented for a repurposing indication — a target disease must first be identified from TxGNN prediction output before evidence can be retrieved and evaluated.

---

## Literature Evidence

Currently no related literature can be presented for a repurposing indication — a target disease must first be identified from TxGNN prediction output before a PubMed search can be directed.

---

## Malaysia Market Information

The NPRA query log (2026-03-27) confirms **2 active registrations** with a successful result status. However, the license detail fields were not populated in the current data extract. The table below reflects the raw state of the Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| (Not retrieved) | (Not retrieved) | (Not retrieved) | (Not retrieved) |
| (Not retrieved) | (Not retrieved) | (Not retrieved) | (Not retrieved) |

> **Action required:** Re-run the NPRA data extraction pipeline with license detail retrieval enabled to populate authorization numbers, product names, dosage forms, and approved indication text.

---

## Cytotoxicity

Acalabrutinib is an antineoplastic agent (BTK inhibitor; kinase inhibitor class targeting B-cell malignancies).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — BTK inhibitor (kinase inhibitor class; not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — neutropenia, anaemia, and thrombocytopenia are commonly reported adverse events in CLL/MCL trials |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (baseline and periodic), liver function tests (ALT/AST), signs of bleeding/bruising, atrial fibrillation risk |
| Handling Protection | Follow institutional cytotoxic/targeted oral therapy handling protocols; standard precautions apply |

---

## Safety Considerations

Package insert warnings and contraindications were not retrieved in this Evidence Pack version (data gap DG001, severity: Blocking). No drug–drug interaction records were returned by the DDI query.

Please refer to the approved NPRA/TFDA package insert for complete safety information, including warnings for haemorrhage, infections, atrial fibrillation, and second primary malignancies — risks known from the Acalabrutinib clinical programme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Acalabrutinib (DB11703 / v4) is critically incomplete: the TxGNN prediction pipeline has not produced any candidate indications, and two unresolved data gaps — missing package insert safety data (Blocking) and missing MOA (High) — prevent the candidate from entering even the preliminary screening stage.

**To proceed, the following is needed:**

- **[Blocking – DG001]** Download and parse the NPRA/TFDA package insert PDF to extract key warnings and contraindications; this must be resolved before any safety pre-screen can run
- **[High – DG002]** Query DrugBank API for DB11703 to retrieve the full Mechanism of Action description
- **[Critical]** Diagnose and re-run the TxGNN prediction pipeline for Acalabrutinib to populate `predicted_indications`; without prediction output, no repurposing target exists
- **[Recommended]** Re-run NPRA data extraction with full license detail retrieval to populate authorization numbers, dosage forms, and approved indication text
- Once all gaps are resolved, regenerate this report as Evidence Pack v5 and proceed to standard S1–S4 evaluation workflow
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

