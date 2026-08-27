---
layout: default
title: Ethinylestradiol
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 5
---

# Ethinylestradiol
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

# Ethinylestradiol: From Hormonal Contraception to Acne

## One-Sentence Summary

Ethinylestradiol is a synthetic estrogen used as the estrogenic component of combined hormonal contraceptive products marketed in Malaysia. The TxGNN model predicts it may also be effective for **Acne**, with **20 clinical trials** and **20 publications** currently supporting this direction — the strongest evidence tier (L1) among the five predicted indications in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Combined hormonal contraception (component of combined oral contraceptives); NPRA-specific label indication text not retrieved in this extract |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 27 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ethinylestradiol itself is not available (data gap). Based on known information, ethinylestradiol is the synthetic estrogen component of many combined oral contraceptives (e.g., with norgestimate, drospirenone, or cyproterone acetate), and its role in contraception is well established.

Mechanistically, combined ethinylestradiol/progestin formulations raise sex hormone-binding globulin (SHBG), lower free testosterone, and suppress ovarian and adrenal androgen secretion — reducing sebaceous gland activity and sebum production. This antiandrogenic pathway is the same one exploited for acne treatment, and it explains why several ethinylestradiol combinations (EE/norgestimate, EE/drospirenone, EE/cyproterone acetate) are already approved by FDA/EMA specifically for acne vulgaris.

Because the original indication (hormonal contraception) and the predicted indication (acne) share the identical hormonal mechanism, this is not a novel biological hypothesis but rather an extension of an already-established drug class effect — supporting the plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00818519](https://clinicaltrials.gov/study/NCT00818519) | Phase 3 | Completed | 179 | Multicenter, double-blind, placebo-controlled RCT of YAZ (drospirenone 3mg/EE 20µg) over 6 cycles in women with moderate acne; highest-quality trial in this dataset. |
| [NCT00752635](https://clinicaltrials.gov/study/NCT00752635) | Phase 4 | Completed | 48 | Compared Tricilest (norgestimate-EE) vs Diane-35 (cyproterone acetate-EE) for moderate acne vulgaris. |
| [NCT01466673](https://clinicaltrials.gov/study/NCT01466673) | Phase 4 | Completed | 201 | Head-to-head comparison of EE/norgestimate (triphasic) vs EE/desogestrel (biphasic) for mild-to-moderate acne vulgaris. |
| [NCT00651469](https://clinicaltrials.gov/study/NCT00651469) | Phase 3 | Completed | 534 | Multicenter, double-blind, placebo-controlled RCT of drospirenone 3mg/EE 20µg over 6 cycles in moderate acne vulgaris. |
| [NCT00656981](https://clinicaltrials.gov/study/NCT00656981) | Phase 3 | Completed | 541 | Companion multicenter, double-blind, placebo-controlled RCT of the same drospirenone/EE regimen for moderate acne vulgaris. |
| [NCT00280657](https://clinicaltrials.gov/study/NCT00280657) | Phase 3 | Completed | 1326 | Double-blind, double-dummy RCT over 6 cycles for acne papulopustulosa; largest enrollment in the dataset. |
| [NCT02710708](https://clinicaltrials.gov/study/NCT02710708) | Phase 4 | Completed | 1921 | Post-authorization safety and efficacy study of YAZ (24/4 regimen) in Chinese women, with moderate acne efficacy as a secondary endpoint. |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Evaluated doxycycline added to continuous combined OC (EE + progestin); acne referenced as a related condition, not a clean EE-only comparison. |
| [NCT01850095](https://clinicaltrials.gov/study/NCT01850095) | N/A | Unknown | 60 | Mechanistic study of peripheral androgen conversion and TLR-2/CD1d expression in keratinocytes after 6 months of OC treatment; supports mechanism, not clinical efficacy. |
| [NCT00722761](https://clinicaltrials.gov/study/NCT00722761) | Phase 3 | Completed | 30 | Randomized, double-blind, placebo-controlled study of YAZ for moderate truncal acne vulgaris. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21212911](https://pubmed.ncbi.nlm.nih.gov/21212911/) | 2011 | RCT | Saudi Medical Journal | Compared desogestrel+EE vs levonorgestrel+EE (2nd vs 3rd generation OCs) on acne, hirsutism, and weight change. |
| [40949888](https://pubmed.ncbi.nlm.nih.gov/40949888/) | 2025 | RCT/Cohort | Int J Women's Dermatology | Evaluated EE 20µg/dienogest 2mg for mild-to-moderate acne vulgaris and its psychological effects in young university women. |
| [140576](https://pubmed.ncbi.nlm.nih.gov/140576/) | 1976 | Clinical study | Acta Europaea Fertilitatis | Treated 175 women with hirsutism/acne using two cyproterone acetate + EE combinations across 1,534 treatment cycles. |
| [34919250](https://pubmed.ncbi.nlm.nih.gov/34919250/) | 2021 | RCT | Eur Rev Med Pharmacol Sci | Follow-up comparison of Myo-Inositol vs oral contraceptives in lean PCOS teenagers with acne, hirsutism, and menstrual irregularity. |
| [17683173](https://pubmed.ncbi.nlm.nih.gov/17683173/) | 2007 | Review | Drugs | Reviewed drospirenone 3mg/EE 20µg (24/4 regimen) use in contraception, PMDD, and moderate acne vulgaris. |
| [18389090](https://pubmed.ncbi.nlm.nih.gov/18389090/) | 2008 | Review | Drugs of Today | Reviewed drospirenone/EE dosing regimen combining low EE dose with antiandrogenic drospirenone. |
| [21175386](https://pubmed.ncbi.nlm.nih.gov/21175386/) | 2011 | Review | Women's Health (London) | Reviewed efficacy and noncontraceptive benefits of drospirenone/EE, including antiandrogenic effects relevant to acne. |
| [32404240](https://pubmed.ncbi.nlm.nih.gov/32404240/) | 2020 | Review | Actas Dermo-Sifiliográficas | Reviewed oral contraceptive use in dermatology for acne and hyperandrogenism-related skin conditions. |
| [36986218](https://pubmed.ncbi.nlm.nih.gov/36986218/) | 2023 | Cohort | Nutrients | Evaluated metabolic/dietary factors in acne vulgaris and OC-based therapy outcomes in young adult women. |
| [18840013](https://pubmed.ncbi.nlm.nih.gov/18840013/) | 2008 | Phase IV study | Clinical Drug Investigation | Investigated chlormadinone 2mg/EE 0.03mg (Belara) effects on acne-prone facial skin physiology across age groups. |

---

## Malaysia Market Information

NPRA records confirm the drug is marketed with **27 active registrations**, but the registry extract for this evidence pack did not return usable license-level detail — license number, product name, dosage form, manufacturer, and approved indication text are all blank for the retrieved entries. This should be re-queried before relying on it for regulatory decisions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3, placebo-controlled RCTs (including two large N=500+ trials and one N=1,326 trial) directly support the efficacy of ethinylestradiol-containing combined oral contraceptives for moderate acne vulgaris, and several EE combinations already carry FDA/EMA-approved acne indications — giving this candidate the highest evidence level (L1) among the five predicted indications. However, a **Blocking** data gap on NPRA label warnings/contraindications (DG001) means safety review (S1) cannot yet be completed.

**To proceed, the following is needed:**
- NPRA package insert data — warnings and contraindications (DG001, Blocking)
- Detailed mechanism of action documentation for ethinylestradiol (DG002)
- Malaysia-specific product license details (license number, product name, indication text — currently blank in registry extract)
- Drug-drug interaction data (current DDI query returned no results)
- VTE/cardiovascular risk assessment specific to acne-indication dosing in the Malaysian population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

