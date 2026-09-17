---
layout: default
title: Filgrastim
parent: Low Evidence (L4-L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Unspecified Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

> The evidence pack does not include Filgrastim's original approved indication (data field empty), though it is a marketed product in Malaysia with 10 registrations on file.
> The TxGNN model predicts potential effectiveness for **Primary Release Disorder of Platelets**, but the evidence pack's own mechanistic review flags this as likely a **graph-topology artifact rather than true pharmacology** — none of the 14 retrieved clinical trials, and no literature, directly support the indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (license and indication fields empty) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Filgrastim is a recombinant granulocyte colony-stimulating factor (G-CSF) that binds the CSF3R receptor on bone marrow myeloid precursor cells, driving neutrophil proliferation/differentiation and hematopoietic stem cell mobilization. This is the only mechanistic information available for this drug in the evidence pack (`original_moa` itself is marked as a data gap; the mechanism above is drawn from the repurposing-rationale evidence).

Primary release disorder of platelets, by contrast, is a platelet function disorder involving defective dense-granule/α-granule secretion during platelet activation — a pathway unrelated to CSF3R-mediated myeloid signaling. The evidence pack's own mechanistic assessment states this explicitly: no known direct mechanistic link exists between the two, and the high TxGNN score most likely reflects the topological proximity of "bone marrow / hematopoiesis" nodes in the knowledge graph rather than a genuine pharmacological relationship.

Supporting this caution, all 14 clinical trials retrieved for this pairing were graded "C" (low relevance) by the evidence pack's own relevance scoring — they are stem cell transplantation, GVHD prophylaxis, or CMV-prevention studies where Filgrastim is used only as a stem cell mobilization/supportive-care agent, not as a treatment for platelet release disorders. No literature was found at all.

---

## Clinical Trial Evidence

**Caution: the trials below were retrieved via drug/disease co-occurrence but were assessed as low relevance (Grade C) by the evidence pack's own review — Filgrastim appears only as a supportive/mobilization agent in transplant or oncology settings, not as a treatment for the predicted indication.**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous stem cell transplant in MCL/DLBCL; G-CSF used only for stem cell mobilization, not a platelet-disorder treatment trial. |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved unrelated-donor bone marrow transplant study; withdrawn with zero enrollment. |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSCT vs. best available therapy in treatment-resistant MS; unrelated to platelet disorders. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding for post-transplant cyclophosphamide GVHD prophylaxis; not a platelet-disorder study. |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral prophylaxis for CMV reactivation in critical care; unrelated indication. |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile for moderate COVID-19; terminated, unrelated to Filgrastim or platelet disorders. |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation in respiratory failure; unrelated indication. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic stem cell transplant pilot in pediatric sarcomas; unrelated indication. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for hematologic malignancies; unrelated indication. |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT pilot for GATA2 mutation patients; unrelated indication. |

4 additional trials were retrieved but not yet graded for relevance (not shown; none target the predicted indication directly based on their titles).

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications are flagged as a **Blocking** data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature directly support Filgrastim for primary release disorder of platelets, and the proposed mechanism (CSF3R-driven myelopoiesis) has no established link to platelet granule secretion pathways — the evidence pack's own review attributes the high TxGNN score to knowledge-graph topology rather than pharmacology. Combined with a **Blocking** data gap on product label warnings/contraindications, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record — currently a High-severity data gap (DG002)
- Preclinical or mechanistic studies directly linking G-CSF/CSF3R signaling to platelet dense-granule/α-granule release
- A dedicated clinical trial or case series testing Filgrastim in patients with platelet release disorders (none currently exist)
- Confirmed original approved indication(s) for Filgrastim, which were not present in this evidence pack
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

