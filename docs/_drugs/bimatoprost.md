---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma / Eyelash Hypotrichosis to Alopecia

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analogue, originally approved for the treatment of glaucoma (Lumigan®) and eyelash hypotrichosis (Latisse®). The TxGNN model predicts it may be effective for **Alopecia** (including androgenetic alopecia and alopecia areata), with **11 clinical trials** and **20 publications** currently supporting this direction. Among 10 predicted indications, alopecia demonstrates the strongest evidence base (Level L2), while several other hair-related predictions are flagged as directional contradictions or false positives.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular hypertension; Eyelash hypotrichosis |
| Predicted New Indication | Alopecia (Rank 9 of 10 predictions; highest evidence) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (1 completed Phase 2 RCT with n=307) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bimatoprost is a synthetic prostamide F2α analogue that acts as an agonist at the FP prostanoid receptor. Its primary pharmacological action involves promoting the transition of hair follicles from the resting phase (telogen) to the active growth phase (anagen), while simultaneously extending the duration of the growth phase. This mechanism was first discovered as a side effect in glaucoma patients using bimatoprost eye drops (Lumigan®), who developed longer, thicker, and darker eyelashes — leading to its FDA approval as Latisse® for eyelash hypotrichosis in 2008.

The link between the original ophthalmic indication and the predicted alopecia indication is rooted in shared receptor biology. Scalp hair follicles express the same FP receptors as eyelash follicles. If bimatoprost can stimulate eyelash growth through prostamide signalling, the same pharmacological pathway should, in principle, be applicable to scalp hair follicles. This biological rationale is strongly supported by multiple completed Phase 2 clinical trials specifically designed to test bimatoprost for androgenetic alopecia (AGA) in both men (n=307) and women (n=306), as well as investigational studies in alopecia areata.

Notably, the TxGNN model also predicted several other hair-related conditions (hypertrichosis, hair shaft abnormalities, Ambras syndrome). However, two of these — hypertrichosis (Rank 1) and Ambras type hypertrichosis (Rank 5) — represent **directional contradictions**: these are conditions of excessive hair growth that bimatoprost would *worsen*, not treat. This highlights a known limitation of the TxGNN knowledge graph in distinguishing between "treats" and "causes/exacerbates" associations. The alopecia prediction (Rank 9), by contrast, is directionally correct and clinically validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Phase 2 RCT comparing 3 doses of bimatoprost vs vehicle and minoxidil 5% in men with androgenetic alopecia — key efficacy trial |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Phase 2 RCT comparing 3 doses of bimatoprost vs vehicle and minoxidil 2% in women with female pattern hair loss |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy study of bimatoprost in men with AGA — dose-response validation |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability, and pharmacokinetics of new scalp-specific bimatoprost formulations |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Effect of topical bimatoprost on androgen-dependent hair follicles — mechanistic validation |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | CO2 fractional laser combined with bimatoprost 0.03% for alopecia areata — combination therapy approach |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Latanoprost vs bimatoprost in promoting eyelash growth in alopecia areata patients |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Scalp pharmacokinetics and tolerability of two bimatoprost formulations after 14-day topical application in AGA |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Bimatoprost 0.03% for eyelash hypotrichosis in children — safety profile extension |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose escalation study in men with AGA — terminated (reason to be clarified; may be safety or commercial) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Systematic Review & Network Meta-analysis | J Dermatol Treat | Determined relative efficacies of non-surgical AGA monotherapies in men and women; bimatoprost included in network comparison |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | Clinical Study | Arch Dermatol Res | CO2 fractional laser + bimatoprost demonstrated enhanced hair regrowth in alopecia areata |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Narrative Review | Expert Opin Investig Drugs | Comprehensive review of bimatoprost for eyelash, eyebrow, and scalp alopecia treatment |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective Open-label | Dermatol Ther | Topical bimatoprost for eyelash loss in alopecia totalis/universalis; 16/19 patients showed response |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Prospective Comparative | Indian Dermatol Online J | Bimatoprost vs clobetasol propionate in scalp alopecia areata — direct head-to-head comparison |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Preclinical + Formulation | Drug Deliv | Novel topical bimatoprost formulation with 4.6× higher skin flux and 529% increased dermal deposition; in vivo hair regrowth in AGA model |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Clinical Practice Guideline | J Dermatol | Japanese guidelines for male/female pattern hair loss (2017 version); bimatoprost referenced as emerging therapy |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatol Online J | Overview of bimatoprost in dermatology — prostamide analogue repurposed from glaucoma to alopecia and vitiligo |
| [22735503](https://pubmed.ncbi.nlm.nih.gov/22735503/) | 2012 | Review | Skin Therapy Lett | Promising therapies for AGA including bimatoprost as a novel prostaglandin-based approach |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | Review | Curr Oncol | Prevention and treatment of chemotherapy-induced alopecia; bimatoprost discussed as interventional option |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Data pending) | — | — | — |
| (Data pending) | — | — | — |
| (Data pending) | — | — | — |

> **Note:** Bimatoprost is confirmed as marketed in Malaysia with 3 active registrations; however, detailed license information (authorization numbers, product names, dosage forms, and approved indication text) was not available in the current data extract. Please refer to the NPRA database for complete registration details.

---

## Other Predicted Indications Summary

The TxGNN model generated 10 predicted indications for bimatoprost. Beyond the primary alopecia recommendation, the following is a summary of all predictions for transparency:

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Assessment |
|------|------------------|-------------|---------------|------------|
| 1 | Hypertrichosis | 99.998% | L5 | ⚠️ **Directional contradiction** — bimatoprost *causes* hypertrichosis; would worsen condition |
| 2 | Malformation syndrome (periodontal) | 99.997% | L5 | ❌ Keyword matching false positive; no bimatoprost literature found |
| 3 | Dandy-Walker malformation syndrome | 99.997% | L5 | ❌ No mechanistic link; KG noise |
| 4 | Isolated genetic hair shaft abnormality | 99.997% | L5 | Weak link — structural protein defect, not follicle cycle issue |
| 5 | Ambras type hypertrichosis | 99.997% | L5 | ⚠️ **Directional contradiction** — same issue as Rank 1 |
| 6 | Hypotrichosis simplex of the scalp | 99.996% | L5 | ✅ Strong rationale (same FP receptor mechanism as Latisse®); no direct trials yet |
| 7 | Congenital hypotrichosis milia | 99.995% | L5 | Weak link — congenital follicle developmental defect |
| 8 | Diffuse alopecia areata | 99.993% | L4 | ✅ Promising; NCT05600673 supports combination approach |
| **9** | **Alopecia** | **99.993%** | **L2** | **✅ Best candidate — 11 trials, 20 publications** |
| 10 | Genetic alopecia | 99.966% | L4 | ✅ Moderate rationale; limited direct evidence |

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** Key warnings, contraindications, and drug interaction data were not available in the current evidence pack. To complete the safety assessment, the following actions are recommended:
> - Download and parse the product insert (仿單) from the NPRA website
> - Query DrugBank for comprehensive safety and DDI data
>
> **Known class-level considerations for prostaglandin analogues (general reference):**
> - Iris pigmentation changes (irreversible in ophthalmic use)
> - Periorbital skin darkening
> - Eyelid erythema and pruritus
> - When applied topically to scalp, systemic absorption and ocular effects should be monitored

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bimatoprost has strong mechanistic plausibility for treating alopecia, supported by its FDA-approved hair growth promotion mechanism (FP receptor agonism). Multiple completed Phase 2 RCTs in both male AGA (n=307) and female pattern hair loss (n=306) provide Level 2 evidence. The drug is already marketed in Malaysia, which reduces regulatory barriers. However, it has not yet received regulatory approval for an alopecia indication in any jurisdiction, and Phase 3 pivotal trials have not been conducted.

**To proceed, the following is needed:**
- **Safety data completion**: Obtain full package insert warnings and contraindications from NPRA; query DrugBank for DDI profile
- **MOA formal documentation**: Retrieve detailed mechanism of action data from DrugBank (DrugBank ID lookup required)
- **Phase 3 trial status**: Investigate why Phase 1 dose-escalation trial (NCT02676310) was terminated — determine if safety signal or commercial decision
- **Formulation development**: Assess availability of scalp-specific bimatoprost formulations (current marketed forms are ophthalmic solutions)
- **Regulatory pathway**: Evaluate Section 505(b)(2) or equivalent pathway for new indication filing in Malaysia
- **Subtype-specific analysis**: Consider separate evaluation tracks for androgenetic alopecia (strongest evidence) vs alopecia areata (emerging evidence with combination therapy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

