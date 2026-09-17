---
layout: default
title: Amoxycillin Trihydrate
parent: Low Evidence (L4-L5)
nav_order: 68
evidence_level: L5
indication_count: 0
---

# Amoxycillin Trihydrate
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **0** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Amoxycillin Trihydrate: Preliminary Assessment — No TxGNN Predictions Available

## One-Sentence Summary

Amoxycillin trihydrate is a broad-spectrum antibiotic with 49 product registrations in the Malaysia NPRA database, confirming active market presence.
However, this Evidence Pack contains **no TxGNN-predicted new indications**, and critical data fields including mechanism of action, license details, and safety warnings remain unfilled.
A full repurposing evaluation **cannot proceed** until these gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved in current data pull |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Insufficient data; no model output available |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 49 |
| Recommended Decision | **Hold** |

---

## Malaysia Market Information

49 product authorizations for amoxycillin trihydrate are recorded in the NPRA database. Individual record details (authorization numbers, product names, dosage forms, and approved indication text) were not retrieved during this data pull and must be re-queried.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | 49 registrations confirmed; detail records pending retrieval |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions were generated for this drug, and all foundational data fields — mechanism of action, individual license records, safety warnings, and contraindications — are absent. There is no repurposing candidate to evaluate at this stage.

**To proceed, the following is needed:**

- **Map to DrugBank ID**: Resolve the DrugBank identifier for amoxycillin trihydrate so the TxGNN pipeline can locate the drug node in the knowledge graph and generate disease predictions.
- **Re-run TxGNN prediction pipeline**: Execute both the KG and DL prediction modules once the DrugBank ID is confirmed to populate `predicted_indications`.
- **Retrieve NPRA license details**: Re-query the NPRA database to populate authorization numbers, product names, dosage forms, and approved indication text for the 49 registered products.
- **Extract package insert data**: Download and parse the NPRA-registered product insert (PIL) to obtain mechanism of action, approved indications, key warnings, and contraindications.
- **Run evidence collection**: Once a target repurposing indication is identified from TxGNN output, execute ClinicalTrials.gov and PubMed collectors to populate clinical trial and literature evidence.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

