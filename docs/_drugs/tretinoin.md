---
layout: default
title: Tretinoin
parent: Low Evidence (L4-L5)
nav_order: 666
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Acute Promyelocytic Leukemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (all-trans retinoic acid) is internationally known for treating acute promyelocytic leukemia (oral) and acne/photoaging (topical). The TxGNN model predicts a possible link to **Rheumatoid Nodulosis**, but this is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph prediction with no corroborating evidence found in ClinicalTrials.gov, ICTRP, or PubMed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in NPRA license extract (fields blank in this evidence pack); tretinoin is internationally indicated for acute promyelocytic leukemia (oral) and acne vulgaris/photoaging (topical) |
| Predicted New Indication | Rheumatoid Nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (Marketed) |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tretinoin was not retrieved in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, tretinoin is a retinoid that acts through retinoic acid receptors (RAR), and it is established that retinoic acid signaling participates in immune cell differentiation, including regulatory T-cell (Treg) and Th17 balance.

The repurposing rationale generated for this candidate states the association explicitly: TxGNN's high score (0.998) likely reflects this theoretical immune-modulation role rather than any direct clinical observation — "推測與視黃酸之免疫調節角色(Treg/Th17分化)相關，但無任何臨床試驗或文獻佐證，純為圖譜連結預測" (the link is inferred from graph connectivity, not evidence).

Rheumatoid nodulosis is a rare nodular manifestation associated with rheumatoid arthritis and is mechanistically distant from tretinoin's established indications (leukemia differentiation therapy, dermatologic keratinization). Targeted searches against ClinicalTrials.gov, ICTRP, and PubMed for this specific drug–disease pair returned zero results, so the mechanistic plausibility described above remains unverified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Tretinoin (systemic ATRA) is used as an antineoplastic differentiation-inducing agent in acute promyelocytic leukemia, distinct from conventional DNA-damaging cytotoxic chemotherapy. DrugBank toxicity/category data was not retrieved in this evidence pack, so the table below relies on established pharmacology rather than pack-sourced data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Non-cytotoxic differentiation therapy (retinoid receptor agonist); classified as antineoplastic when used systemically, not a classic DNA-damaging cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data retrieved in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (no toxicity data retrieved in this evidence pack) |
| Monitoring Items | CBC with differential and coagulation profile; monitoring for differentiation syndrome is a well-known ATRA-specific risk in oncologic use |
| Handling Protection | Retinoids are teratogenic — pregnancy prevention measures and standard handling precautions per package insert are expected, pending confirmation |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were all flagged as data gaps in this evidence pack — TFDA/NPRA labeling retrieval is a Blocking-severity gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, Rheumatoid Nodulosis, has zero supporting clinical trials or literature despite active searches, placing it at the lowest evidence tier (L5, model prediction only). Critical safety data (warnings, contraindications) also remain unretrieved, which blocks even a preliminary safety assessment.

**To proceed, the following is needed:**
- Retrieve NPRA/package insert warnings and contraindications (Blocking gap, DG001)
- Retrieve confirmed mechanism of action and DrugBank drug categories (High-severity gap, DG002)
- Populate complete NPRA license/product details (all 12 registrations currently have blank fields in this pack)
- Consider re-evaluating other candidates from the same TxGNN run with stronger evidence bases — e.g., osteoarthritis (rank 7, L4, 20 literature hits, though with conflicting pro-/anti-inflammatory signals) or Quinquaud's folliculitis decalvans (rank 10, L4, flagged "Research Question") — as these have at least some literature signal, unlike Rheumatoid Nodulosis.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

