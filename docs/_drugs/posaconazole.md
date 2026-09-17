---
layout: default
title: Posaconazole
parent: Low Evidence (L4-L5)
nav_order: 562
evidence_level: L4
indication_count: 1
---

# Posaconazole
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **1** 
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

# Posaconazole: From Invasive Fungal Infection to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal; the specific TFDA/NPRA-approved indication text was not retrievable from the registry data in this evidence pack, but posaconazole is broadly known for prophylaxis/treatment of invasive fungal infections. The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis pneumonia)**, but this is currently supported only by **2 tangentially relevant clinical trials** and **5 review/case-level publications**, none of which directly test posaconazole against Pneumocystis jirovecii.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in registry data (known drug class: triazole antifungal) |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Malaysia Market Status | Marketed (Marketed) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for posaconazole is not available in this evidence pack. Based on known pharmacology, posaconazole is a triazole antifungal that inhibits fungal lanosterol 14α-demethylase (CYP51), blocking ergosterol synthesis in the fungal cell membrane — the mechanism underlying its efficacy against filamentous and yeast-like fungi in invasive fungal infections.

However, the repurposing rationale in this evidence pack flags an important mechanistic caveat: *Pneumocystis jirovecii* is an atypical fungus whose trophic form relies primarily on host-derived cholesterol rather than its own ergosterol synthesis, making its sensitivity to triazoles fundamentally different from typical fungal pathogens. This is consistent with clinical practice, where posaconazole is not a first-line agent for Pneumocystis pneumonia (first-line agents are TMP-SMX, atovaquone, or dapsone).

Because both the original indication text and the formal MOA record are data gaps, this prediction should currently be treated as a class-level pharmacological analogy rather than a mechanistically validated hypothesis. The TxGNN score is high, but it is not yet corroborated by direct pharmacodynamic or clinical evidence specific to Pneumocystis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Evaluates rezafungin (an echinocandin, not posaconazole) vs. standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic transplant recipients — same disease-prevention setting but a different drug; graded low relevance (Grade C) to posaconazole specifically. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform study on GVHD prophylaxis after mismatched unrelated donor transplant; posaconazole, if used, would appear only as a co-administered antifungal prophylaxis, not as the primary study intervention for Pneumocystis (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet. Infectious Diseases | UK best-practice update on diagnostic methods for serious fungal diseases (non-culture-based tests); not specific to posaconazole treatment efficacy. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and Pneumocystis pneumonia; notes mould-active posaconazole's role in antifungal prophylaxis in high-risk haemato-oncology patients, reducing invasive candidiasis rates. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | Chinese clinical practice guideline for diagnosis/management of invasive pulmonary fungal disease; general guidance, not posaconazole/Pneumocystis-specific. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective review of infectious complications in acute GVHD after liver transplant; describes antimicrobial management patterns broadly, not a posaconazole efficacy study. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK) | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal/antitubercular agents; pharmacokinetic context only, no efficacy data for Pneumocystis. |

---

## Malaysia Market Information

The evidence pack confirms posaconazole has **3 active registrations** in Malaysia (NPRA, market status: Marketed/Marketed), but the license number, product name, dosage form, and approved indication text fields were not populated in this dataset, so a detailed registration table cannot be produced. This should be sourced directly from NPRA records before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA/NPRA label warnings, contraindications, and drug-drug interaction data were not retrievable in this evidence pack (see Data Gap DG001, marked Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is weak and self-flagged as speculative — Pneumocystis jirovecii's biology differs from typical ergosterol-dependent fungi, and posaconazole is not a first-line agent for this indication. Neither identified clinical trial directly evaluates posaconazole for Pneumocystis (both graded low relevance), and a Blocking data gap on label warnings/contraindications means safety cannot yet be assessed (DG001 explicitly blocks S1 safety review).

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (warnings, contraindications) to resolve DG001
- Confirmed DrugBank MOA record to resolve DG002
- Direct pharmacological or clinical evidence evaluating posaconazole activity against Pneumocystis jirovecii specifically
- Complete NPRA registration details (license numbers, product names, approved indication text) for the 3 existing Malaysia registrations
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

