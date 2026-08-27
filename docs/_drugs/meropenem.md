---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
---

# Meropenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Meropenem: From Serious Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic used for serious bacterial infections. The TxGNN model predicts it may be effective for **Bacterial Arthritis**, with **1 clinical trial** and **20 publications** currently identified in the evidence pool — though most of this evidence is indirect (case reports and susceptibility/observational studies rather than trials designed specifically for this indication).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in current dataset — TFDA/NPRA license records were returned with empty indication text (5 licenses on file, all blank). Meropenem is broadly known as a carbapenem antibiotic for serious bacterial infections. |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 25 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured dataset (data gap DG002). Based on known pharmacology, meropenem is a broad-spectrum carbapenem that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs), producing bactericidal activity against a wide range of Gram-positive and Gram-negative organisms, including anaerobes and many multidrug-resistant (MDR) pathogens.

Bacterial (septic) arthritis is typically caused by organisms that fall within meropenem's spectrum — *Staphylococcus aureus*, streptococci, Gram-negative bacilli (including *Pseudomonas aeruginosa*), and in tropical/endemic settings, *Burkholderia pseudomallei* (melioidosis). Several of the retrieved publications specifically describe musculoskeletal and osteoarticular melioidosis where isolates remained susceptible to meropenem, and pharmacokinetic literature supports adequate bone/joint tissue and cement-elution penetration.

Mechanistically, this supports meropenem as a plausible carbapenem option for MDR or polymicrobial septic arthritis when first-line agents (e.g., cefazolin, vancomycin, ceftriaxone) are inadequate — but this is a rescue/salvage-therapy rationale rather than evidence of first-line efficacy, and no trial in the evidence pack directly tests meropenem against bacterial arthritis as a primary endpoint.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Studied levofloxacin (not meropenem) for infection prevention in children with acute leukemia/HSCT. Not a direct efficacy trial of meropenem in bacterial arthritis — included here as the only trial the search surfaced for this indication; relevance is unconfirmed (marked "pending" in the source data). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective cohort | Indian Journal of Medical Microbiology | 22 musculoskeletal melioidosis cases (9 septic arthritis, 12 osteomyelitis); all isolates susceptible to meropenem. |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective cohort | Le Infezioni in Medicina | Characterizes patients with osteoarticular melioidosis, a rare focal presentation treatable with carbapenems. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohort/lab | Clinical Laboratory | Pathogen distribution and antimicrobial resistance in bone and joint infections in children under 4. |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case report | Pharmaceuticals (Basel) | Septic arthritis of the hip from rare *Bacillus*/*Paenibacillus* species, managed with long-term linezolid. |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | In vitro/PK | J Bone Joint Surg Am | Thermal stability and elution kinetics of meropenem (among others) in PMMA bone cement for orthopaedic infection use. |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Cohort/antibiogram | Eur J Orthop Surg Traumatol | Antibiogram development for empiric antibiotic strategy in non-spinal orthopaedic infections including septic arthritis. |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | Animal model | Int J Antimicrob Agents | Colistin-cement spacer combined with systemic antibiotics in a rabbit model of carbapenemase-producing *K. pneumoniae* prosthetic joint infection. |
| [38134096](https://pubmed.ncbi.nlm.nih.gov/38134096/) | 2023 | Case report | Medicine | *Campylobacter fetus*-induced psoas abscess in a patient with gouty arthritis. |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | PK study | Clinical Pharmacokinetics | Population pharmacokinetics of meropenem across the adult lifespan, informing dosing for serious infections. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Review of off-label vs. formal-recommendation antibiotic use (including carbapenems) for MDR/XDR bacterial infections. |

## Malaysia Market Information

NPRA records show **25 registered licenses** for Meropenem with market status "已上市" (Marketed), but the underlying license detail fields (license number, product name, dosage form, manufacturer, approved indication text) were returned empty in the current dataset and cannot be tabulated. This is a data-completeness gap in the source extract, not evidence of a missing market presence.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data were not available in the current dataset — flagged as a **Blocking** data gap, DG001: TFDA label warnings/contraindications, required before a S1 safety review can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for meropenem in bacterial arthritis is L3 (retrospective cohorts and case reports showing in vitro/clinical susceptibility, notably in osteoarticular melioidosis) — supportive but not confirmatory, and no trial directly tests meropenem as a treatment for bacterial/septic arthritis.
- More critically, TFDA/NPRA label safety data (warnings, contraindications) is a **Blocking** gap (DG001), which by itself prevents a S1 safety review regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) via PDF retrieval and parsing (DG001)
- DrugBank-sourced mechanism of action data (DG002)
- Complete NPRA license detail records (product names, dosage forms, approved indication text) for the 25 registered products
- Confirmation of relevance for the single clinical trial (NCT01371656), which studies levofloxacin rather than meropenem
- A dedicated literature/clinical search specific to "septic arthritis" or "meropenem AND joint infection" to reduce noise from the current broader "bacterial arthritis" query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

