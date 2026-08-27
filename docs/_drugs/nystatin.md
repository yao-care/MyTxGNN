---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Fungal Infections to Vulvovaginitis

## One-Sentence Summary

> Nystatin is a polyene antifungal antibiotic, historically used to treat Candida (fungal) infections of the skin, mouth, and mucous membranes.
> The TxGNN model predicts it may be effective for **Vulvovaginitis**,
> with **0 dedicated clinical trials** but **20 supporting publications**, including one comparative cohort study directly evaluating nystatin in this setting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the registration data provided (Nystatin's general pharmacology class targets Candida/fungal infections) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (observational/cohort data + review literature; no completed RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, Nystatin belongs to the polyene macrolide antifungal class — it binds ergosterol in fungal cell membranes, creating pores that cause leakage of cellular contents and fungal cell death. It is poorly absorbed systemically and is primarily used topically or in the gastrointestinal tract for Candida-related infections.

Vulvovaginitis, particularly vulvovaginal candidiasis (VVC), is predominantly caused by *Candida albicans* (85–90% of cases). Since Nystatin's established antifungal activity directly targets the *Candida* species responsible for most vulvovaginitis cases, the TxGNN prediction aligns with well-documented pharmacological rationale rather than an unexpected mechanistic leap.

This is further supported by decades of clinical literature describing nystatin's use in vulvovaginal/mixed vulvovaginitis, including comparative susceptibility studies against fluconazole and combination therapy with other antimicrobials (e.g., nifuratel), suggesting the prediction reflects a plausible, mechanistically grounded repurposing candidate rather than a spurious knowledge-graph association — unlike several lower-ranked predictions in this same evidence pack (e.g., orbital disease, teratoma), which lack any mechanistic or evidentiary connection to Nystatin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | In 287 *Candida* isolates from complicated VVC patients, correlated fluconazole/nystatin in-vitro susceptibility with clinical outcome; supports nystatin's continued efficacy against resistant strains |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclinical (rat model) | BMC Microbiology | Nystatin enhanced mucosal immune response and protected vaginal epithelial ultrastructure in a rat model of VVC |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro | Infection and Drug Resistance | Nystatin (vs. ZnO nanoparticles) downregulated virulence gene (SAP1-3) expression in fluconazole-resistant *C. albicans* isolates from VVC |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Reviews management of fluconazole-resistant VVC; identifies nystatin among viable alternative antifungal therapies |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | Comparative in vitro | J Infect Dev Ctries | Compared tea tree oil vs. nystatin inhibition zones against vaginal *Candida* isolates in pregnancy |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Reviews boric acid for recurrent VVC; discusses nystatin as an existing alternative for azole-resistant non-albicans species |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Clinical | Ceska Gynekologie | Evaluated combined vaginal nystatin + nifuratel therapy for mixed/miscellaneous vulvovaginal infections |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | General review of vulvovaginal candidiasis diagnosis and treatment options |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | Clinical review of vulvovaginal candidiasis |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review (monograph) | Med Clin North Am | Early monograph on nystatin, including its use in candidal infections |

---

## Malaysia Market Information

The evidence pack confirms Nystatin holds **11 active registrations** in Malaysia (market status: ✓ Marketed), but no license number, product name, dosage form, or approved-indication text was returned for any individual registration in this dataset. Registration-level details need to be pulled directly from the NPRA database before this can be used to support formulation/route decisions.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Note: safety warnings, contraindications, and DDI data for Nystatin are currently a blocking data gap in this evidence pack — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic and literature evidence for vulvovaginitis is reasonably supportive (L3 — cohort data plus consistent review literature), but a **Blocking-severity data gap** (missing TFDA/NPRA package-insert warnings and contraindications) means this candidate cannot yet clear the S1 safety initial-assessment gate.

**To proceed, the following is needed:**
- Package insert warnings/contraindications (from NPRA/TFDA product label) to complete S1 safety screening
- Confirmed mechanism of action documentation from DrugBank
- Malaysia license-level detail (product name, dosage form, approved indication text) for all 11 registrations
- DDI data source, since current query returned no results (not confirmed absence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

