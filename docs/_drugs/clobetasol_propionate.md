---
layout: default
title: Clobetasol Propionate
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 5
---

# Clobetasol Propionate
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

# Clobetasol Propionate: From Corticosteroid-Responsive Skin Conditions to Dermatitis

## One-Sentence Summary

Clobetasol Propionate is a super-potent topical corticosteroid already used broadly for steroid-responsive skin conditions. The TxGNN model flags **Dermatitis** as its top-ranked predicted indication, and this direction is currently supported by **19 clinical trials** and **20 publications**. Because clobetasol is already a mainstay therapy for dermatitis-spectrum conditions in most markets, this prediction largely confirms an established use rather than revealing a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (NPRA license indication text and `original_indications` were both empty); generally known as a super-potent topical corticosteroid for corticosteroid-responsive dermatoses |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 0.00% (as returned in the evidence pack — this value warrants a data-quality check before use in scoring) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 28 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, Clobetasol Propionate belongs to the super-potent (Class I) topical corticosteroid class. Its efficacy in corticosteroid-responsive dermatoses — including atopic dermatitis, psoriasis, and vulvar lichen sclerosus — is well established in the dermatology literature, and mechanistically its anti-inflammatory, immunosuppressive, and antimitotic actions on epidermal cells directly apply to inflammatory dermatitis.

The relationship between the original use and the predicted indication is close rather than distant: dermatitis is a corticosteroid-responsive inflammatory skin condition, the same pharmacological category clobetasol already treats. The evidence pack's own rationale for this prediction acknowledges this directly: *"'Dermatitis' is a broad category that aligns closely with clobetasol's core pharmacology — this is essentially within its existing indication scope rather than a genuinely novel repurposing hypothesis, though the evidence quality is sufficient to support it."*

In practical terms, this candidate should be read less as "new therapeutic hypothesis" and more as "confirmation of established use, worth validating against the actual NPRA-approved label" — which is precisely why the missing label data (DG001) is the critical open item below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01323673](https://clinicaltrials.gov/study/NCT01323673) | Phase 4 | Completed | 125 | Ethanol-free clobetasol propionate foam 0.05% vs. vehicle foam for chronic hand dermatitis |
| [NCT00862654](https://clinicaltrials.gov/study/NCT00862654) | Phase 3 | Completed | 326 | Clobetasol propionate shampoo 0.05% combined with antifungal shampoo for moderate-to-severe scalp seborrheic dermatitis |
| [NCT01591785](https://clinicaltrials.gov/study/NCT01591785) | N/A | Completed | 60 | Treating S. aureus colonization in hand eczema to reduce disease severity |
| [NCT02376049](https://clinicaltrials.gov/study/NCT02376049) | Phase 1 | Completed | 30 | Intra-patient comparison of topical agents in mild-to-moderate atopic dermatitis |
| [NCT00828464](https://clinicaltrials.gov/study/NCT00828464) | Phase 4 | Completed | 30 | Open-label safety, efficacy, and tolerability of clobetasol propionate foam in chronic hand dermatitis |
| [NCT01870050](https://clinicaltrials.gov/study/NCT01870050) | N/A | Unknown | 20 | Topical steroid/vehicle vs. steroid/dapsone combination in lichen simplex chronicus and prurigo nodularis |
| [NCT01987076](https://clinicaltrials.gov/study/NCT01987076) | N/A | Unknown | 112 | Corticosteroid treatment strategy in DRESS syndrome |
| [NCT02573883](https://clinicaltrials.gov/study/NCT02573883) | Phase 3 | Completed | 52 | Clobetasol propionate 0.05% ointment vs. fractionated CO2 laser for vulvar lichen sclerosus |
| [NCT03847389](https://clinicaltrials.gov/study/NCT03847389) | Phase 1/2 | Terminated | 8 | Pharmacokinetics and HPA-axis suppression safety of clobetasol topical oil in pediatric moderate-to-severe atopic dermatitis |
| [NCT06120140](https://clinicaltrials.gov/study/NCT06120140) | Phase 2 | Recruiting | 300 | Enhanced vs. standard dermatologic management of EGFR-inhibitor-related skin adverse events (indirect relevance) |

*9 additional registered trials exist in the source data but are lower relevance/status (withdrawn, unknown, or only tangentially related) and were omitted per the top-10 rule.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24672120](https://pubmed.ncbi.nlm.nih.gov/24672120/) | 2005 | RCT | Curr Ther Res Clin Exp | Relative efficacy and interchangeability of different clobetasol propionate vehicles in steroid-responsive dermatoses |
| [18806904](https://pubmed.ncbi.nlm.nih.gov/18806904/) | 2008 | Review | Drugs of Today | Overview of clobetasol propionate use across atopic dermatitis, psoriasis, and lichen sclerosus |
| [3528243](https://pubmed.ncbi.nlm.nih.gov/3528243/) | 1986 | Review | J Am Acad Dermatol | Clinical efficacy and safety review of topical clobetasol-17-propionate |
| [20672788](https://pubmed.ncbi.nlm.nih.gov/20672788/) | 2010 | Review | Am Fam Physician | Diagnosis and management of contact dermatitis |
| [30145645](https://pubmed.ncbi.nlm.nih.gov/30145645/) | 2019 | Review | Clin Rev Allergy Immunol | Contact dermatitis to medications and skin products, including corticosteroid contact allergy |
| [30222987](https://pubmed.ncbi.nlm.nih.gov/30222987/) | 2019 | Cohort | J Am Acad Dermatol | Clobetasol pretreatment to reduce/prevent injection-site dermatitis from biologic agents |
| [19454093](https://pubmed.ncbi.nlm.nih.gov/19454093/) | 2007 | Unclassified | BMJ Clin Evid | Seborrhoeic dermatitis overview — Malassezia-driven inflammatory mechanism |
| [32462741](https://pubmed.ncbi.nlm.nih.gov/32462741/) | 2020 | Case Report | Contact Dermatitis | Allergic contact dermatitis caused by clobetasol propionate and lanoconazole |
| [35214115](https://pubmed.ncbi.nlm.nih.gov/35214115/) | 2022 | Unclassified | Pharmaceutics | Update on novel dermal delivery systems for clobetasol propionate |
| [9542676](https://pubmed.ncbi.nlm.nih.gov/9542676/) | 1998 | Unclassified (double-blind RCT design) | Int J Dermatol | 4-week double-blind trial of clobetasol propionate emollient cream 0.05% vs. vehicle in atopic dermatitis |

*10 additional publications exist in the source data with abstracts pending classification/relevance grading and were omitted per the top-10 rule.*

---

## Malaysia Market Information

License-level detail (authorization numbers, product names, dosage forms, indication text) was **not returned** in this data pull — all 5 sample license records in the evidence pack have empty fields. What is confirmed: NPRA records show **28 active registrations** under market status **已上市 (Marketed)**. License-level detail should be re-queried from NPRA before this report is used for regulatory purposes.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data were all returned as Data Gaps in this pull — DG001 is flagged as **Blocking** for safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for dermatitis is strong (L1: multiple completed Phase 3/4 trials directly evaluating clobetasol propionate in dermatitis-spectrum conditions), but this is best understood as validation of an already-established use rather than a novel repurposing opportunity. The recommendation is capped at "Guardrails" rather than "Go" because the safety label data needed for an S1 safety pre-assessment is missing (DG001, Blocking).

**To proceed, the following is needed:**
- NPRA product insert (warnings, contraindications) — retrieve and parse the PDF label (DG001, Blocking)
- DrugBank mechanism-of-action confirmation (DG002, High)
- License-level indication text from NPRA to confirm whether "dermatitis" is already within the approved label (would reclassify this from repurposing candidate to label-consistency check)
- Data-quality check on the TxGNN score field, which returned 0.0 across all five ranked indications in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

