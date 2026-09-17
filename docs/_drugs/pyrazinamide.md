---
layout: default
title: Pyrazinamide
parent: Low Evidence (L4-L5)
nav_order: 581
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Pulmonary Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line anti-tuberculosis agent, used as part of standard combination therapy (with isoniazid, rifampicin, ± ethambutol) for pulmonary tuberculosis. The TxGNN model predicts it may be effective for **Infectious Otitis Media**, but this specific candidate currently has **0 clinical trials** and **0 publications** supporting it directly — the model's high score appears to reflect embedding proximity to a related, better-documented entity (tuberculous otitis media) rather than direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis (component of first-line anti-TB combination regimen; NPRA license-level indication text not available in source data) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap in the source pack). Based on known pharmacology, pyrazinamide is a prodrug converted by mycobacterial pyrazinamidase to pyrazinoic acid, which disrupts membrane potential and energy metabolism of *Mycobacterium tuberculosis* in the acidic, necrotic environment of TB lesions. It is a core component of the standard first-line four-drug regimen for pulmonary tuberculosis, and its efficacy in that indication is well established.

For the top-ranked candidate itself — infectious otitis media — no clinical trial or literature evidence was returned in this evidence pack. Per the model's own rationale, the high TxGNN score (rank 1030 internally) most likely reflects knowledge-graph embedding similarity to a neighboring, more specific disease node — "tuberculous otitis media" — rather than a genuinely novel, evidence-backed signal.

Notably, several closely related candidates in the same prediction set (middle ear disease, chronic otitis media, suppurative otitis media — ranks 2, 4, 5) **are** each backed by 5–8 case reports/reviews. All of that literature describes **tuberculous otitis media** — a rare extrapulmonary manifestation of TB affecting the middle ear — successfully treated with standard anti-TB regimens that include pyrazinamide. This suggests the pharmacologically justifiable indication is narrower than "infectious otitis media" in general: it is otitis media **secondary to confirmed tuberculosis infection**, not otitis media of other (e.g., typical bacterial) etiology, since pyrazinamide's antimicrobial spectrum is essentially limited to mycobacteria.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

5 product authorizations are registered with NPRA (market status: Marketed), but license-level details (license number, product name, dosage form, approved indication text) were not returned in the source data pack and could not be populated here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN confidence score, "infectious otitis media" has zero direct clinical trial or literature support, meeting only the model-prediction-only evidence tier (L5). The actual supporting evidence in this dataset concentrates on tuberculous otitis media specifically, which is arguably an extension of pyrazinamide's existing TB indication rather than a genuinely new one.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a blocking data gap preventing safety pre-screening
- DrugBank mechanism-of-action data via API — needed to formally assess mechanistic plausibility
- Consider re-scoping the candidate from "infectious otitis media" to "tuberculous otitis media" and gather diagnosis-linked clinical evidence for that narrower indication
- Malaysia license-level product data (license numbers, product names, dosage forms, approved indication text) to complete the market information section
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

