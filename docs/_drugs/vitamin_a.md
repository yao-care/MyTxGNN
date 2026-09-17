---
layout: default
title: Vitamin A
parent: Low Evidence (L4-L5)
nav_order: 690
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

Using no additional skill — this is a direct, fully-specified content-generation task; I'll follow the report prompt exactly.

# Vitamin A: From Vitamin A Deficiency to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Vitamin A (retinol) is a fat-soluble vitamin whose established indication is prevention and treatment of vitamin A deficiency; specific approved-indication text from the registration database was not provided in this evidence pack.
> The TxGNN model's top-ranked prediction suggests possible use in **Congenital Prothrombin Deficiency**, but this candidate is supported by **0 directly relevant clinical trials** and **0 literature citations**, and is very likely a knowledge-graph artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (license/indication text fields were empty; drug is generically known for vitamin A deficiency) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 166 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Vitamin A is not available in this evidence pack (DrugBank MOA field flagged as a data gap). Based on established pharmacology, Vitamin A (retinol) and its active metabolite retinoic acid act through nuclear retinoid receptors (RAR/RXR) to regulate epithelial differentiation, vision, immune function, and cell proliferation.

Congenital prothrombin deficiency, by contrast, is a coagulation disorder in which Factor II (prothrombin) activity is impaired. The γ-carboxylation step required to activate prothrombin is **Vitamin K–dependent**, not Vitamin A–dependent. There is no known overlap between retinoid signaling and the vitamin K–dependent coagulation cascade.

Given this lack of mechanistic overlap, and the fact that none of the associated clinical trials in this evidence pack actually tested Vitamin A in this population, this prediction most likely reflects a **false-positive artifact** — probably arising from the proximity of generic "vitamin" nodes within the knowledge graph embedding space, rather than a genuine biological signal. This should be treated as a hypothesis-generating anomaly, not a repurposing lead.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Descriptive retrospective study of adult inborn-errors-of-metabolism patients in Switzerland; not an interventional trial |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Dietary supplement (L-arginine, Pycnogenol, vitamin K2, lipoic acid, B-vitamins) in hypertensive patients; unrelated to this disease |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | Haemophilia and bone loss study; unrelated to Vitamin A or prothrombin deficiency |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | Tests BERIPLEX (a prothrombin complex concentrate), not Vitamin A, for reversal of oral-anticoagulant-induced coagulation factor deficiency |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | "Vitalliver" product in decompensated cirrhosis; drug identity and relevance to Vitamin A unconfirmed |

**None of the above trials directly evaluate Vitamin A in patients with congenital prothrombin deficiency.**

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The evidence pack confirms Vitamin A is marketed with **166 total registrations**, but individual license records (license number, product name, dosage form, manufacturer, approved indication text) were returned empty and are not available for citation in this pack. This should be treated as a data gap requiring direct lookup against the source registry rather than an absence of market presence.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.97%), but there is no mechanistic plausibility (Vitamin A acts via retinoid signaling; prothrombin activation is Vitamin K–dependent) and zero directly relevant clinical or literature evidence. This pattern is consistent with a model artifact rather than a true repurposing signal, matching the automated evidence-level rating of L5.

**To proceed, the following is needed:**
- Confirmation of whether this association is a genuine embedding artifact (e.g., via ablation or nearest-neighbor analysis of the "vitamin" node cluster in the knowledge graph)
- DrugBank-sourced mechanism of action data for Vitamin A
- TFDA/NPRA label data (key warnings, contraindications, approved indication text) currently missing from this pack
- If pursued further, a search specifically for Vitamin A + coagulation factor synthesis literature to rule out an indirect mechanism

---

### Note: Other Predicted Indications in This Evidence Pack

This evidence pack (`TW-UNKNOWN-multi`) contains 10 ranked TxGNN predictions for Vitamin A. For completeness, two are worth flagging separately from the headline candidate above:

- **Rank 3 – "Vitamin Deficiency Disorder" (L1, Proceed with Guardrails):** This is Vitamin A's **existing, already-approved indication**, not a novel repurposing candidate. It appears in the prediction list due to how the knowledge graph encodes the drug–disease relationship, and should be excluded from repurposing consideration.
- **Rank 7 – "Perinatal Disease" (L2, Proceed with Guardrails):** This is the most scientifically credible candidate in the set. Vitamin A supplementation in very-low-birth-weight (VLBW) preterm infants to reduce bronchopulmonary dysplasia (BPD) risk is supported by **multiple Cochrane systematic reviews** (PMID 27552058, 21975731, 17943744, 12519545, 10796372). If a repurposing candidate from this pack merits a full evaluation report, this is the one recommended for follow-up — noting that "perinatal disease" as a category is broader than the specific VLBW/BPD population where evidence actually concentrates.

All remaining candidates (ranks 2, 4, 5, 6, 8, 9, 10) carry Evidence Level L3–L5 with weak-to-no direct supporting evidence and are recommended for **Hold** or **Research Question** status only.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

