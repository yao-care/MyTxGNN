---
layout: default
title: Acitretin
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 4
---

# Acitretin
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

# Acitretin: From Psoriasis to Acne (Disease)

## One-Sentence Summary

Acitretin is a second-generation aromatic retinoid, primarily used for severe psoriasis and other keratinization disorders.
The TxGNN model predicts it may be effective for **acne (disease)**,
with **1 clinical trial** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriasis and keratinization disorders (per literature context; NPRA approved indication text not available in current dataset) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acitretin is a second-generation aromatic retinoid that acts as a full agonist of retinoic acid receptors (RAR-α, RAR-β, and RAR-γ). Through nuclear receptor signalling, it regulates keratinocyte differentiation, inhibits sebaceous gland activity (sebosuppression), and modulates inflammatory pathways including leukotriene production and NF-κB activity. Detailed MOA data from DrugBank was not available in this dataset, but the mechanistic framework is well-characterised in the dermatological literature.

Acne pathogenesis is driven by three overlapping mechanisms that retinoids directly target: follicular hyperkeratinisation, excessive sebaceous gland secretion, and local inflammation. A closely related molecule, isotretinoin (13-cis retinoic acid), is already the established first-line treatment for severe nodulocystic acne. Acitretin belongs to the same pharmacological class and shares sebosuppressive and anti-inflammatory mechanisms, though it differs in pharmacokinetic profile and teratogenic risk classification.

Case reports have documented acitretin's use in nodulocystic acne and hidradenitis suppurativa (acne inversa), a chronic inflammatory disorder mechanistically and anatomically related to acne. Long-term follow-up data from a 25-year case series (PMID 20874789) further supports the biological plausibility of the TxGNN prediction, positioning acitretin as a mechanistically coherent, if pharmacologically second-choice, retinoid candidate for acne management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study examining whether oral retinoid-induced nasal mucosal dryness increases COVID-19 infection risk. Study subject is isotretinoin (not acitretin); indirectly indicates systemic retinoid use in the acne population is under active safety scrutiny. No efficacy data for acitretin. |

> **Note:** No clinical trials directly evaluating acitretin for acne were identified. The sole trial retrieved concerns a related retinoid (isotretinoin) and addresses a safety question, not treatment efficacy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Case Series / Retrospective | Br J Dermatol | 25-year experience with acitretin for hidradenitis suppurativa (acne inversa); demonstrates clinically meaningful long-term responses and questions whether HS is truly a misnomer for acne inversa |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case Report | Cutis | Patient with severe nodulocystic facial acne and HS treated with acitretin after two isotretinoin courses; partial clinical improvement noted in persistent facial cysts |
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Clinical Guideline | J Eur Acad Dermatol Venereol | European S1 guideline for HS/acne inversa; includes retinoids (including acitretin) within recommended treatment options |
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of drug treatments for discoid lupus erythematosus; evaluates retinoids as a treatment class, providing high-level evidence context for acitretin's immunomodulatory and skin-normalising effects |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Narrative Review | Clin Dermatol | Comprehensive update on vitamin A and retinoids in dermatology; explicitly covers acitretin alongside isotretinoin for acne-related and keratinisation disorders |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Review / Mechanistic | Dermatology (Basel) | Examines retinoid-mediated inhibition of sebaceous gland activity; establishes the mechanistic basis for predicting anti-acne effects across the retinoid class, including acitretin |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Der Hautarzt | Review of pharmacological treatments for acne inversa; positions retinoids including acitretin within the treatment landscape alongside antibiotics and TNF-α inhibitors |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Narrative Review | Drugs | Broad review of retinoid indications in dermatology; describes acitretin's established role in psoriasis and discusses applicability to acne-related dermatoses |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | Mechanistic (In Vitro) | Prostaglandins | Demonstrates that acitretin inhibits eosinophil leukotriene C4 (LTC4) production; supports anti-inflammatory mechanism relevant to acne-associated tissue inflammation |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | PK / Efficacy Review | Clin Pharmacokinet | Pharmacokinetic comparison of retinoids; confirms acitretin's established efficacy for psoriasis and hyperkeratosis, and discusses PK differences versus isotretinoin that are relevant to acne use |

---

## Malaysia Market Information

Four product registrations for acitretin are recorded with the NPRA (market status: **Marketed**). However, detailed licence information — including authorisation numbers, product names, dosage forms, and approved indication text — was not available in the current dataset. Please verify directly via the NPRA online portal (https://www.npra.gov.my) for complete registration details.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| (Not available in dataset) | — | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note**: Safety data including key warnings, contraindications, and drug interaction information were not retrievable in this dataset (Data Gap DG001). Given that acitretin carries **FDA Pregnancy Category X** status and is associated with teratogenicity, hepatotoxicity, and hypertriglyceridaemia, reviewing the official NPRA-approved package insert before any clinical or regulatory decision is **essential**.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acitretin shares the core retinoid mechanism of action with isotretinoin — an established first-line treatment for severe acne — and case series and observational data support its use in acne-related disorders such as hidradenitis suppurativa. The L3 evidence base (no RCTs; supported by case reports, guidelines, and mechanistic reviews) justifies cautious advancement rather than outright rejection, but direct efficacy data for acitretin specifically in acne vulgaris is currently absent.

**To proceed, the following is needed:**

- **Safety data retrieval** (Priority: Blocking): Download and parse the NPRA-approved package insert to extract key warnings, contraindications, and pregnancy risk information before any clinical assessment
- **MOA confirmation**: Query DrugBank API (DB00459) to retrieve structured mechanism of action data for regulatory dossier use
- **Differentiation analysis**: Clarify the clinical niche for acitretin vs. isotretinoin in acne — particularly for patients where isotretinoin is contraindicated or has failed
- **Comparative PK/safety review**: Document the teratogenicity and hepatotoxicity profile differences between acitretin and isotretinoin to assess feasibility in target populations
- **Prospective study design**: Consider a pilot observational study or structured case series for acitretin in acne inversa/nodulocystic acne where isotretinoin has been inadequate, to generate Tier 2 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

