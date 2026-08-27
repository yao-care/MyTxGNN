---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 4
---

# Palbociclib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Palbociclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

> Palbociclib is a CDK4/6 inhibitor already marketed in Malaysia (NPRA, 12 registrations) for HR+/HER2- metastatic breast cancer.
> Among four TxGNN-predicted indications in this screening batch, **rheumatoid arthritis** has the most substantive supporting evidence —
> a mechanistic link to synovial fibroblast proliferation, two preclinical/animal studies, one pharmacovigilance cohort, and a human case report —
> though still short of a dedicated clinical trial. Two other candidates (hyperthyroidism, thyroid hormone resistance) have TxGNN scores but zero supporting evidence, and a third (thrombotic disease) appears in the data as a **safety risk signal, not a treatment opportunity**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (publicly known indication for palbociclib; NPRA license indication text and structured MOA were not returned by this data pull — see Data Gaps) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.36% (rank 8774) |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Research Question (not yet Go / Hold / Guardrails — see Conclusion) |

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the literature evidence collected for this candidate, palbociclib is a CDK4/6 kinase inhibitor that blocks the Rb-E2F cell-cycle pathway — its efficacy in breast cancer relies on halting proliferation of hormone-receptor-driven tumor cells.

The mechanistic bridge to rheumatoid arthritis (RA) is fibroblast-like synoviocyte (FLS) proliferation, which drives pannus formation in the inflamed joint. A 2025 study (PMID 39940918) demonstrated CDK6-dependent, CDK4-independent synovial hyperplasia in an arthritic mouse model, directly implicating the same CDK4/6 axis palbociclib targets. An earlier animal study (PMID 25165034) showed that cell-cycle inhibition of synovial fibroblasts, combined with cytokine blockade, ameliorated arthritis without increasing immunosuppression — a mechanistically distinct approach from current biologic DMARDs.

Human-level plausibility comes from a case report (PMID 33587021) describing RA improvement in a breast cancer patient incidentally treated with palbociclib, and a cohort/pharmacovigilance study (PMID 40504547) examining immune-mediated disease patterns in breast cancer patients on CDK4/6 inhibitors. This is still preclinical-plus-anecdotal evidence rather than a purpose-designed RA trial, which is why the evidence level is capped at L4.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort/Pharmacovigilance | The Oncologist | Investigated prevalence of autoimmune disease in HR+/HER2- breast cancer patients on CDK4/6 inhibitors + endocrine therapy, to identify predictive biomarkers |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical/Mechanistic | International Journal of Molecular Sciences | CDK6-dependent (CDK4-independent) synovial hyperplasia demonstrated in arthritic mice; palbociclib explored for RA but preclinical myelosuppression noted |
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case Report | Modern Rheumatology Case Reports | RA improvement observed in a breast cancer patient treated with palbociclib, following prior mouse collagen-induced arthritis findings |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical (animal model) | Annals of the Rheumatic Diseases | CDK inhibition of synovial fibroblasts + cytokine blockade ameliorated arthritis in animal models without increasing immune suppression |

## Malaysia Market Information

NPRA records confirm 12 active registrations and "Marketed" status, but this data pull did not return per-license detail (product name, dosage form, or approved-indication text — all fields returned empty). Registration-level detail should be re-pulled from NPRA before this is used in a formal submission.

## Cytotoxicity

Palbociclib is a targeted antineoplastic (CDK4/6 inhibitor class), based on breast-cancer usage referenced throughout the collected literature.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | High — preclinical evidence (PMID 39940918) and drug-safety review (PMID 37994878) both document palbociclib-induced myelosuppression as a class effect |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (neutropenia surveillance); consider hepatic/renal function per standard CDK4/6 inhibitor monitoring |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

NPRA label warnings, contraindications, and drug-interaction data were not retrieved in this pull (flagged as a **Blocking** data gap — required before this candidate can enter Stage 1 safety review). Please refer to the package insert for safety information in the interim.

**Related safety signal:** literature collected under a separate candidate indication (thrombotic disease, see below) shows multiple FAERS disproportionality studies and a breast-cancer cohort reporting **increased venous thromboembolism risk** with CDK4/6 inhibitors as a class. This should be treated as a safety consideration for any expanded use of palbociclib, not filed as a treatment opportunity.

## Other TxGNN-Ranked Candidates (Same Screening Batch)

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Note |
|------|---------|-------------|-----------------|----------|------|
| 1 | Hyperthyroidism | 99.44% | L5 | Hold | No clinical trials or literature; no known mechanistic link to CDK4/6; may be a spurious knowledge-graph association |
| 3 | Thrombotic disease | 99.32% | L4 | Hold | Evidence points the *opposite* direction — FAERS/cohort studies show CDK4/6 inhibitors **increase** VTE risk; this is a safety signal, not a repurposing opportunity |
| 4 | Thyroid hormone resistance (THRB mutation) | 99.30% | L5 | Hold | Rare monogenic receptor disorder; no mechanistic overlap with cell-cycle inhibition; no trials or literature |

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The rheumatoid arthritis signal has a coherent mechanism (CDK6-driven synoviocyte proliferation) and converging preclinical/animal/case-report evidence, but no purpose-designed human trial exists yet — it merits a formal research question rather than a Go or Hold at this stage.

**To proceed, the following is needed:**
- NPRA label warnings/contraindications (Blocking gap — required before Stage 1 safety review)
- Structured mechanism-of-action data from DrugBank (High-severity gap)
- A dedicated early-phase RA trial (or at minimum a case series) rather than reliance on a single incidental case report
- Explicit thromboembolism risk assessment before any RA-directed protocol, given the class-wide VTE signal identified under the thrombotic disease candidate
- Re-pull of NPRA per-license detail (product name, dosage form, indication text) for the Malaysia Market Information table
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

