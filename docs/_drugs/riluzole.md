---
layout: default
title: Riluzole
parent: Low Evidence (L4-L5)
nav_order: 593
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole is a glutamatergic neurotransmission inhibitor originally approved for **Amyotrophic Lateral Sclerosis (ALS)**.
The TxGNN model's top-ranked prediction for this drug is **Bilateral Parasagittal Parieto-Occipital Polymicrogyria**, a congenital brain malformation,
but this prediction is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags it as likely knowledge-graph noise rather than a genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic Lateral Sclerosis (ALS) *(per evidence-pack rationale; TFDA license record itself is blank — see Market Information)* |
| Predicted New Indication | Bilateral Parasagittal Parieto-Occipital Polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured drug record. Based on known pharmacology cited elsewhere in this evidence pack, Riluzole acts by inhibiting presynaptic glutamate release and blocking voltage-dependent sodium channels, reducing motor neuron excitotoxicity — the basis for its efficacy in ALS.

Bilateral parasagittal parieto-occipital polymicrogyria is a structural cortical malformation caused by abnormal neuronal migration during fetal brain development. This is a fundamentally different disease category from ALS: it is a developmental disorder, not a neurodegenerative/excitotoxic one, and it manifests before or at birth rather than in adulthood.

The evidence pack's own repurposing rationale is explicit on this point: there is **no known pathophysiological link** between Riluzole's glutamate/sodium-channel modulation and cortical migration disorders. The very high TxGNN score (99.99%, model rank 232) is assessed as likely reflecting embedding-space proximity or knowledge-graph noise rather than a real mechanistic signal. No mechanistic hypothesis supports this pairing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The evidence pack records 1 total registration for Riluzole with market status "Marketed" (Marketed), but the underlying license record (authorization number, product name, dosage form, approved indication text) is empty in the source data — no populated fields are available to construct a market information table.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate has no clinical or literature support (L5, S0), and the mechanistic review within this same evidence pack concludes there is no plausible biological link between Riluzole's mode of action and this congenital cortical malformation — the high model score is most likely an artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- DrugBank-sourced mechanism of action (MOA) data for Riluzole
- TFDA label data: warnings, contraindications, and complete license/product details (currently blank)
- Any preclinical or case-level evidence specifically linking Riluzole to cortical migration disorders, before this candidate can move past S0

**Note on other candidates in this pack:** rank 2 (ALS) is Riluzole's original approved indication, not a repurposing candidate, despite strong evidence (L1). Ranks 4, 7, and 8 (lower motor neuron syndrome, monomelic amyotrophy, Mills syndrome) carry plausible mechanistic overlap with ALS pathology but currently have zero trial/literature support (L5) — these are flagged "Research Question" in the source data and may be more productive candidates for future evidence-gathering than the top-ranked prediction reviewed above.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

