---
layout: default
title: Medroxyprogesterone Acetate
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 5
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From an Unspecified Original Indication to Uterine Corpus Cancer

## One-Sentence Summary

Medroxyprogesterone Acetate (MPA, DrugBank DB00603) is a synthetic progestin marketed in Malaysia under 7 registrations, though the specific original approved indication text is not available in the current NPRA extract.
The TxGNN model's top-ranked prediction is **Uterine Corpus Cancer**, supported by **5 clinical trials** and **20 publications** — but the evidence pack itself flags this label as likely overlapping with the separately ranked **Endometrial Cancer** prediction, which carries materially stronger evidence (43 trials, 20 publications, evidence level L2 vs. L3).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current NPRA license records (data gap) |
| Predicted New Indication | Uterine Corpus Cancer |
| TxGNN Prediction Score | 0.00% (as recorded in source data) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for MPA was not returned by this query (DrugBank MOA field is a data gap). However, the underlying evidence records consistently describe MPA as a **synthetic progestin (progestogen)** acting through the progesterone receptor (PR), producing anti-proliferative and radiosensitizing effects on PR-positive endometrial tissue, and inducing differentiation/apoptosis in PR-positive endometrial cancer cells.

"Uterine corpus cancer" and "endometrial cancer" are, in most clinical usage, the same disease entity (the corpus uteri's malignancy is overwhelmingly endometrial carcinoma), and the evidence pack's own analysis for this rank explicitly notes this overlap: the trials linked to "uterine corpus cancer" are less direct (HRT risk cohorts, fertility-preservation trials where MPA is not the primary arm) than those linked to the separately scored "endometrial cancer" entry, which includes multiple Phase 2/3 trials with MPA as the primary intervention and a guideline-supported role in fertility-sparing and palliative treatment of endometrial cancer.

In short, the mechanistic rationale (PR-mediated antiproliferative action) is sound and well documented, but the specific "uterine corpus cancer" label appears to be a partially redundant/lower-quality subset of a broader, better-supported endometrial cancer signal. This should be clarified before treating the two as independent findings.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00064025](https://clinicaltrials.gov/study/NCT00064025) | Phase 2 | Completed | 75 | Phase II pilot of short-term Depo-Provera (MPA) exposure and its morphologic/biochemical/molecular effects on endometrioid adenocarcinoma of the uterine corpus |
| [NCT03018249](https://clinicaltrials.gov/study/NCT03018249) | Early Phase 1 | Completed | 50 | Randomized surgical-window trial: short-term MPA vs. MPA + entinostat on progesterone receptor-related molecular changes in endometrioid endometrial tumors |
| [NCT03463252](https://clinicaltrials.gov/study/NCT03463252) | Phase 2/3 | Recruiting | 224 | LNG-IUS fertility-sparing trial for atypical endometrial hyperplasia/early endometrial carcinoma; MPA is not the primary arm |
| [NCT04710017](https://clinicaltrials.gov/study/NCT04710017) | N/A | Completed | 110 | Tranexamic acid vs. depot-MPA for perimenopausal irregular uterine bleeding (non-cancer indication) |
| [NCT01698164](https://clinicaltrials.gov/study/NCT01698164) | Phase 4 | Unknown | 1200 | Multi-center HRT trial in early-menopausal Chinese women; not a direct MPA-cancer treatment trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15535270](https://pubmed.ncbi.nlm.nih.gov/15535270/) | 2004 | Review | Nihon Rinsho | Introductory review of hormone therapy for uterine corpus cancer |
| [6842804](https://pubmed.ncbi.nlm.nih.gov/6842804/) | 1983 | Cohort | JAMA | Risk of breast, uterine corpus, and ovarian cancer in women receiving MPA injections (5,000-woman cohort) |
| [2526620](https://pubmed.ncbi.nlm.nih.gov/2526620/) | 1989 | Case series | Gan To Kagaku Ryoho | MPA combined with chemotherapy enabled complete surgical removal of stage III uterine corpus carcinoma |
| [20414038](https://pubmed.ncbi.nlm.nih.gov/20414038/) | 2010 | Case report | Gan To Kagaku Ryoho | Two cases of multidrug-resistant recurrent endometrial cancer successfully treated with MPA |
| [38469132](https://pubmed.ncbi.nlm.nih.gov/38469132/) | 2024 | Case report | Gynecol Oncol Rep | Successful fertility preservation in stage II endometrial carcinoma with long-term progestin therapy |
| [2973195](https://pubmed.ncbi.nlm.nih.gov/2973195/) | 1988 | Cohort | Zentralbl Gynakol | Adjuvant gestagen (MPA) therapy in 221 stage I endometrial cancer patients; 5-year survival reported |
| [6218817](https://pubmed.ncbi.nlm.nih.gov/6218817/) | 1983 | Cohort | Br J Obstet Gynaecol | Progestogens (incl. MPA) as adjuvant to surgery in stage I adenocarcinoma of the uterine corpus |
| [6467144](https://pubmed.ncbi.nlm.nih.gov/6467144/) | 1984 | Preclinical (in vitro) | Cancer | MPA increases radiosensitivity of endometrial adenocarcinoma explants |
| [9605604](https://pubmed.ncbi.nlm.nih.gov/9605604/) | 1997 | Preclinical (animal) | Acta Anat | Effects of conjugated estrogens ± MPA on mammary carcinogenesis and uterine adenomyosis in mice |
| [7559094](https://pubmed.ncbi.nlm.nih.gov/7559094/) | 1995 | Preclinical (animal) | Jpn J Cancer Res | Inhibitory effects of MPA on mouse endometrial carcinogenesis |

---

## Malaysia Market Information

Taiwan/NPRA source data confirms **7 active registrations** and Marketed status, but the individual license fields (license number, product name, dosage form, manufacturer, approved indication text) were returned empty in this extract and cannot be tabulated. Registration-level detail needs to be re-pulled from the NPRA source before it can be reported.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for progestin activity in uterine/endometrial tissue is credible, but this specific "uterine corpus cancer" prediction has lower-quality, largely indirect trial support and is flagged by the evidence pack itself as likely overlapping with the stronger "endometrial cancer" prediction (L2, Proceed with Guardrails). A Blocking-severity gap in TFDA label warnings/contraindications also prevents any S1 safety screen.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap
- DrugBank/authoritative MOA confirmation for MPA
- Clarification of whether "uterine corpus cancer" and "endometrial cancer" should be merged into a single indication before further scoring, to avoid double-counting evidence
- Re-extraction of NPRA license-level fields (product name, dosage form, manufacturer, indication text) for the 7 registrations
- Verification of the TxGNN score field, which currently reads 0.00% across all ranked indications and may reflect an extraction issue rather than the model's actual confidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

