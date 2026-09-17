---
layout: default
title: Tyrosine
parent: Low Evidence (L4-L5)
nav_order: 676
evidence_level: L5
indication_count: 10
---

# Tyrosine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Tyrosine: From Unspecified Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid marketed in Malaysia under 20 registered licenses, but no original approved indication or mechanism-of-action data is currently available in the evidence pack. The TxGNN model's top prediction links it to **Cauda Equina Syndrome**, but this pairing is supported by **0 clinical trials** and only **1 unrelated case report**, and is flagged in the underlying rationale as a likely database indexing mismatch rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available regulatory records (all license indication fields are blank) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Malaysia Market Status | Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for tyrosine is not available. Tyrosine is a standard amino acid and a known biochemical precursor to catecholamines and thyroid hormones, but no established pharmacological rationale connects it to cauda equina syndrome (a compressive neurological condition of the lumbosacral nerve roots).

The repurposing rationale for this candidate explicitly states that no identifiable mechanism links tyrosine to cauda equina syndrome. The single supporting literature record (PMID 17341045) describes a case of clear cell sarcoma / melanotic schwannoma originating in the spinal nerve root — a histopathology case report with no mention of tyrosine as a therapeutic intervention. This suggests the TxGNN association is most likely a database indexing artifact rather than a substantiated biological hypothesis, and it should not be treated as mechanistically supported at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case Report | Neurosurgical focus | Case report of clear cell sarcoma originating from the S1 nerve root, previously misdiagnosed as psammomatous melanotic schwannoma; discusses tumor histogenesis and potential immunotherapy directions. Does not evaluate tyrosine or any drug intervention for cauda equina syndrome. |

---

## Malaysia Market Information

The evidence pack confirms tyrosine holds 20 active registrations in Malaysia ("Marketed" status), but no license-level details (registration number, product name, dosage form, or approved indication text) were returned by the source query — all fields are blank in the underlying records. Product-level registration data could not be reported here and would need to be re-queried from the NPRA source.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only), with zero clinical trials and a single literature record that is unrelated to tyrosine or cauda equina syndrome — the rationale itself flags this as a likely false-positive database mismatch. In addition, a Blocking data gap (TFDA/NPRA label warnings and contraindications, DG001) prevents even an initial safety screen (S1) from being conducted.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve the official Malaysia product label warnings/contraindications before any safety-stage evaluation
- Resolve DG002 (High): obtain tyrosine's mechanism-of-action data from DrugBank to support or refute mechanistic plausibility
- Confirm the original approved indication(s) from NPRA license-level records (currently blank)
- Independently verify whether the cauda equina syndrome association is a genuine TxGNN signal or a knowledge-graph indexing error before allocating further review resources
- If pursued, generate a dedicated literature/preclinical search specifically on tyrosine and lumbosacral nerve root pathology, since the current single reference is not relevant
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

