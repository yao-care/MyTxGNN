---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 482
evidence_level: L5
indication_count: 5
---

# Metronidazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metronidazole: From Anaerobic/Protozoal Infections to Rosacea

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial originally used for anaerobic bacterial and protozoal infections (e.g., trichomoniasis, amoebiasis, giardiasis, bacterial vaginosis). The TxGNN model's top-ranked prediction is **Rosacea**, supported by **20 clinical trials** and **20 publications** — though the underlying mechanism (topical anti-inflammatory/anti-*Demodex* activity) is already a globally approved use rather than a truly novel signal. Note: the TxGNN raw score for this pairing is reported as **0.0** in the evidence pack, which appears to be a data artifact and should be verified before use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial and protozoal infections (trichomoniasis, amoebiasis, giardiasis, bacterial vaginosis) — established pharmacology; Malaysia license text was not extracted in this dataset (all 5 sampled license records are blank) |
| Predicted New Indication | Rosacea |
| TxGNN Prediction Score | 0.00% (raw score = 0.0 — likely a data extraction artifact; recommend re-verifying against the model output) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 28 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap in the evidence pack). Based on known pharmacology, metronidazole is a nitroimidazole-class antimicrobial whose efficacy against anaerobic bacteria and protozoa (via DNA strand breakage from toxic nitro-radical metabolites) is well established; it also has topical anti-inflammatory activity and suppresses *Demodex folliculorum*, a mite implicated in rosacea pathophysiology.

Topical metronidazole (e.g., MetroGel®) is in fact already an FDA-approved and internationally recognized standard therapy for rosacea. The evidence pack's own rationale for this candidate states explicitly that this represents "confirmation of an existing indication rather than a novel repurposing signal" — the TxGNN prediction is directionally correct but is reproducing established clinical knowledge rather than surfacing a new use. This should be factored into decision-making: the value here is regulatory/market confirmation for Malaysia, not discovery of a new therapeutic avenue.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02393937](https://clinicaltrials.gov/study/NCT02393937) | Phase 3 | Completed | 963 | Multicenter, double-blind, vehicle-controlled RCT comparing two Metronidazole Gel 1% formulations for rosacea — head-to-head efficacy data |
| [NCT01493947](https://clinicaltrials.gov/study/NCT01493947) | Phase 3 | Completed | 962 | Ivermectin 1% cream vs. Metronidazole 0.75% cream in papulopustular rosacea over 16 weeks + 36-week extension; metronidazole as active comparator |
| [NCT01016782](https://clinicaltrials.gov/study/NCT01016782) | Phase 3 | Completed | 867 | Double-blind, vehicle-controlled trial assessing efficacy of Metronidazole Topical Gel 1% for inflammatory lesions of rosacea |
| [NCT01513863](https://clinicaltrials.gov/study/NCT01513863) | Phase 1 | Completed | 602 | Bioequivalence study of two metronidazole 1% topical gel formulations in moderate-to-severe rosacea |
| [NCT00855595](https://clinicaltrials.gov/study/NCT00855595) | Phase 4 | Completed | 207 | Azelaic acid 15% gel vs. metronidazole 1% gel, both plus low-dose doxycycline, in moderate papulopustular rosacea |
| [NCT01426269](https://clinicaltrials.gov/study/NCT01426269) | Phase 4 | Completed | 235 | Long-term relapse/efficacy/safety of Oracea® vs. placebo after initial 12-week Oracea®+MetroGel® 1% regimen |
| [NCT00495313](https://clinicaltrials.gov/study/NCT00495313) | Phase 4 | Completed | 91 | COL-101+metronidazole gel vs. doxycycline+metronidazole gel in moderate-to-severe rosacea |
| [NCT00436527](https://clinicaltrials.gov/study/NCT00436527) | Phase 4 | Completed | 26 | Kinetic regression study of MetroGel® 1% skin hydration delivery |
| [NCT05861310](https://clinicaltrials.gov/study/NCT05861310) | Phase 1 | Unknown | 48 | Effectiveness/safety of metronidazole 1% cream as main rosacea therapy |
| [NCT00668655](https://clinicaltrials.gov/study/NCT00668655) | N/A | Completed | 30 | Cosmetic appearance of MetroGel® 1% combined with facial foundations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35929658](https://pubmed.ncbi.nlm.nih.gov/35929658/) | 2022 | Guideline (Tier 1) | J Dtsch Dermatol Ges | S2k guideline on rosacea diagnosis and treatment |
| [26280139](https://pubmed.ncbi.nlm.nih.gov/26280139/) | 2015 | Review (Tier 2) | American Family Physician | Rosacea diagnosis and treatment overview |
| [30657582](https://pubmed.ncbi.nlm.nih.gov/30657582/) | 2019 | Review (Tier 2) | Eur Rev Med Pharmacol Sci | Therapeutic uses and side effects of metronidazole across indications |
| [34347259](https://pubmed.ncbi.nlm.nih.gov/34347259/) | 2021 | Review (Tier 2) | Skin Therapy Letter | Updated rosacea diagnosis, classification and management |
| [35104917](https://pubmed.ncbi.nlm.nih.gov/35104917/) | 2022 | Review (Tier 2) | J Cosmet Dermatol | Comprehensive review of rosacea management |
| [33646026](https://pubmed.ncbi.nlm.nih.gov/33646026/) | 2021 | Review (Tier 2) | Br J Hosp Med | Rosacea pathophysiology, features and treatment options |
| [17679183](https://pubmed.ncbi.nlm.nih.gov/17679183/) | 2007 | Review | J Drugs Dermatol | Metronidazole alone and combined with oral antibiotics for rosacea |
| [16673797](https://pubmed.ncbi.nlm.nih.gov/16673797/) | 2006 | Review | J Drugs Dermatol | Effect of formulation, dosing, and concentration on metronidazole efficacy in rosacea |
| [30585305](https://pubmed.ncbi.nlm.nih.gov/30585305/) | 2019 | Systematic Review | Br J Dermatol | Phenotype-based interventions for rosacea with GRADE assessment |
| [40213532](https://pubmed.ncbi.nlm.nih.gov/40213532/) | 2025 | Network Meta-analysis | JAAD International | Efficacy/safety of minocycline, metronidazole, ivermectin, azelaic acid in moderate-to-severe papulopustular rosacea |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack — flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Rosacea has L1-level evidence (multiple completed Phase 3 RCTs) and metronidazole is already a globally recognized standard topical therapy for this condition, giving high biological plausibility. However, the TxGNN score itself is anomalous (0.0), Malaysia-specific safety labeling (warnings/contraindications) is entirely missing (Blocking gap), and the original approved indication text could not be extracted from the license dataset.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action detail from DrugBank (DG002, High)
- Verification/re-query of the TxGNN score for this drug–disease pair (currently reported as 0.0)
- Malaysia license-level detail (product name, dosage form, approved indication text) — all 5 sampled records were blank
- Confirmation of whether rosacea is already a labeled indication for any Malaysia-marketed metronidazole product, to distinguish "regulatory gap-filling" from genuine off-label repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

