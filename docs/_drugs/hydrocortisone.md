---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 5
---

# Hydrocortisone
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

# Hydrocortisone: From Corticosteroid Replacement & Anti-Inflammatory Therapy to Erythema Multiforme

## One-Sentence Summary

Hydrocortisone is the physiological glucocorticoid used broadly for adrenocortical insufficiency and inflammatory/allergic conditions (topical, systemic, ophthalmic, and rectal formulations); specific TFDA label indication text was not available in this evidence pack. The TxGNN model's top-ranked prediction points to **Erythema Multiforme**, but the supporting evidence is weak — **6 clinical trials** (none directly testing hydrocortisone in EM) and **20 publications**, most of which are case reports on tangential topics or even report hydrocortisone-induced EM rather than treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from TFDA license data in this evidence pack (all `approved_indication_text` fields blank); as a corticosteroid, hydrocortisone is generally indicated for adrenocortical insufficiency and inflammatory/allergic conditions |
| Predicted New Indication | Erythema Multiforme |
| TxGNN Prediction Score | 0.00% *(as recorded in this evidence pack — likely an unpopulated/placeholder value rather than a true near-zero score; should be re-verified before use)* |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 58 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydrocortisone is a glucocorticoid receptor agonist with anti-inflammatory and immunosuppressive effects; its efficacy across a wide range of inflammatory and immune-mediated dermatologic conditions has been established, and mechanistically it could plausibly modulate the immune/inflammatory reaction underlying erythema multiforme (EM).

However, the rationale here is theoretical rather than evidence-backed. The oldest and most relevant literature (Patterson et al., 1990) frames corticosteroid use in EM/Stevens-Johnson syndrome as an explicit **"therapeutic controversy"** — corticosteroids are not established first-line therapy for EM, and their role remains debated. None of the six retrieved clinical trials directly test hydrocortisone as an intervention for EM; they were captured by keyword overlap (atopic dermatitis, unrelated oncology/cardiology trials) rather than genuine relevance.

Notably, one case report in the literature set (PMID 10696380) describes a patient who **developed EM after topical application of a hydrocortisone-containing product** (Gentisone HC ear drops) — an adverse reaction, not a therapeutic use. This further weakens, rather than supports, the repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02153762](https://clinicaltrials.gov/study/NCT02153762) | N/A | Completed | 41 | Locoid Lipocream (hydrocortisone butyrate) application-order study in atopic dermatitis — **not EM-related** (Grade C) |
| [NCT05199376](https://clinicaltrials.gov/study/NCT05199376) | N/A | Recruiting | 30 | Percutaneous cryotherapy for neurofibromas in NF1 — keyword mismatch, **not relevant** (Grade C) |
| [NCT00332163](https://clinicaltrials.gov/study/NCT00332163) | Phase 2 | Completed | 95 | Skin toxicity management for panitumumab/FOLFIRI in mCRC — not specific to EM (Grade C) |
| [NCT05468372](https://clinicaltrials.gov/study/NCT05468372) | Phase 2 | Recruiting | 50 | Amphotericin B vs posaconazole for pulmonary mucormycosis — **unrelated** (Grade C) |
| [NCT06878729](https://clinicaltrials.gov/study/NCT06878729) | N/A | Recruiting | 74 | Coronary CTO-PCI procedural comparison — **unrelated** (Grade C) |
| [NCT01650194](https://clinicaltrials.gov/study/NCT01650194) | Phase 2 | Completed | 60 | Enzalutamide + abiraterone in prostate cancer — **unrelated** (Grade C) |

**None of the retrieved trials directly evaluate hydrocortisone for the treatment of erythema multiforme.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2198136](https://pubmed.ncbi.nlm.nih.gov/2198136/) | 1990 | Review | Chest | Reviews EM/SJS management; explicitly frames corticosteroid therapeutic role as controversial |
| [3869906](https://pubmed.ncbi.nlm.nih.gov/3869906/) | 1985 | Case series (pending classification) | Czasopismo stomatologiczne | Hydrocortisone iontophoresis used in treatment of erythema exudativum multiforme — most directly relevant record |
| [26627523](https://pubmed.ncbi.nlm.nih.gov/26627523/) | 2015 | Case report | JPMA | Corticosteroids used in management of Herpes-associated EM in a pediatric case |
| [10696380](https://pubmed.ncbi.nlm.nih.gov/10696380/) | 1999 | Case report | J Laryngol Otol | EM **caused by** topical hydrocortisone acetate/gentamicin ear drops — adverse reaction, not treatment |
| [1068978](https://pubmed.ncbi.nlm.nih.gov/1068978/) | 1976 | Review | Int Dent J | Corticosteroids (incl. hydrocortisone hemisuccinate) in oral mucosal disease management |
| [37854261](https://pubmed.ncbi.nlm.nih.gov/37854261/) | 2023 | Case report | Clin Case Rep | EM-like lesions provoked by radiotherapy |
| [15243755](https://pubmed.ncbi.nlm.nih.gov/15243755/) | 2005 | Case report | Arch Gynecol Obstet | EM major following docetaxel administration |
| [18370879](https://pubmed.ncbi.nlm.nih.gov/18370879/) | 2008 | Case report | J Ocul Pharmacol Ther | EM following topical dorzolamide use |
| [20407030](https://pubmed.ncbi.nlm.nih.gov/20407030/) | 2010 | Case report | Ann Pharmacother | Caspofungin-induced toxic epidermal necrolysis (TEN) |
| [13994257](https://pubmed.ncbi.nlm.nih.gov/13994257/) | 1963 | Comparative topical therapy | Arch Dermatol | Triamcinolone vs hydrocortisone comparison in topical therapy |

*10 of 20 retrieved publications are shown, prioritized for direct relevance to hydrocortisone and EM. No RCTs were identified; evidence is dominated by case reports, several of which describe hydrocortisone as a **cause** rather than a treatment of EM.*

---

## Malaysia Market Information

License-level details (authorization number, product name, dosage form, manufacturer) are not available in the current evidence pack — all five sampled license records have blank fields. The regulatory data confirms 58 total registered licenses and "已上市" (marketed) status (see Quick Overview), but product-level specifics require direct TFDA lookup.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found (`query_status: not_found`).

Note: the evidence pack flags TFDA package insert warnings/contraindications as a **Blocking** data gap (DG001) — this must be resolved before any Stage 1 safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 (mechanism/preclinical-adjacent only) with no clinical trials directly testing hydrocortisone in EM, and the literature itself characterizes corticosteroid use in EM as a longstanding therapeutic controversy. One case report even documents hydrocortisone-induced EM, which cuts against the repurposing hypothesis rather than supporting it.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking) — required before any safety evaluation
- Mechanism of action data (DG002, High) — needed to assess mechanistic plausibility beyond general corticosteroid class effects
- A clinical trial or case series specifically testing hydrocortisone (not other corticosteroids) as an EM treatment, to move beyond preclinical/anecdotal evidence
- **Note:** this evidence pack also scored "hemorrhoid" as this drug's rank-2 predicted indication, with substantially stronger evidence (L2, multiple completed Phase 2 RCTs, "Proceed with Guardrails" recommendation) reflecting hydrocortisone's already-established label use (e.g., Anusol-HC, Proctofoam-HC). That candidate may warrant separate evaluation as a more actionable repurposing/label-extension case than erythema multiforme.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

