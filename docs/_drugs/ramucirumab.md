---
layout: default
title: Ramucirumab
parent: Low Evidence (L4-L5)
nav_order: 583
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: From Advanced Gastric Cancer to Uterine Ligament Adenocarcinoma

> **Note on data provenance**: The evidence pack's `original_indications` field and NPRA license `approved_indication_text` are both empty. The original indication cited below reflects Ramucirumab's (Cyramza®) established public drug label (gastric/GE-junction adenocarcinoma, NSCLC, colorectal cancer, hepatocellular carcinoma) rather than a value extracted from this evidence pack — flagged explicitly rather than presented as sourced data.

## One-Sentence Summary

Ramucirumab is a VEGFR-2-targeting monoclonal antibody approved for several solid tumours (gastric/GE-junction adenocarcinoma, NSCLC, colorectal cancer, hepatocellular carcinoma). The TxGNN model's top-ranked prediction is **Uterine Ligament Adenocarcinoma**, but this is a **pure computational prediction (L5)** — **0 clinical trials** and **0 publications** currently support it, and the model's own rationale states no anti-angiogenic agent has been studied in this rare pathology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced Gastric Cancer *(public label information — not present in evidence pack)* |
| Predicted New Indication | Uterine Ligament Adenocarcinoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (Marketed) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, Ramucirumab is a fully human IgG1 monoclonal antibody that binds VEGFR-2 and blocks VEGF-A/-C/-D signalling, thereby inhibiting tumour angiogenesis. It is approved as monotherapy or in combination regimens across several solid tumours where angiogenesis drives progression.

For the top-ranked candidate, **Uterine Ligament Adenocarcinoma**, the model's own rationale is explicitly cautionary: this is described as an extremely rare, pathologically distinct entity that does **not** belong to the cervical cancer lineage, and no anti-angiogenic agent — including bevacizumab or ramucirumab — has any recorded trial or literature evidence in this tissue. The prediction is driven by the TxGNN score alone, with no mechanistic or clinical corroboration.

By contrast, several lower-ranked candidates in this pack (e.g., rank 2 **endocervical carcinoma**, rank 3 **adenoid cystic carcinoma of the cervix uteri**, rank 5, 6, and 10) carry a materially stronger rationale: they belong to the cervical cancer spectrum, where the VEGF/VEGFR-2 pathway is well characterised, and where bevacizumab — a drug in the same anti-VEGF class — demonstrated an OS benefit in the Phase 3 GOG-240 trial. These candidates are scored L4/S1 ("Research Question") rather than L5/S0 ("Hold"), and may warrant prioritisation over the top-ranked hit if this pipeline is advanced further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia (NPRA) shows **2 active registrations** for Ramucirumab (market status: Marketed / Marketed). However, license number, product name, dosage form, manufacturer, and approved indication text were not populated for either entry in this evidence pack, so a per-license table cannot be presented without fabricating values.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGFR-2 monoclonal antibody / anti-angiogenic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Uterine Ligament Adenocarcinoma) is supported only by a TxGNN score, with no clinical trials, no literature, and an explicit statement in the model rationale that no anti-angiogenic drug has ever been studied in this rare pathology. A Blocking data gap on TFDA/NPRA package insert warnings and contraindications (DG001) also prevents S1 safety screening.

**To proceed, the following is needed:**
- NPRA/TFDA package insert (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism of action via DrugBank API — High-priority gap (DG002)
- License-level detail (product name, dosage form, approved indication text) for the 2 Malaysia registrations
- Consider re-scoping toward higher-evidence candidates (e.g., endocervical carcinoma, rank 2) which carry class-level support from bevacizumab's GOG-240 trial, before committing resources to the top-ranked but evidence-free hit
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

