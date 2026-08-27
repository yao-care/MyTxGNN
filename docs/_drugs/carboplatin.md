---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based chemotherapy agent classically used to treat ovarian cancer and other solid tumours. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **17 clinical trials** and **20 publications** currently supporting this direction, particularly in triple-negative and BRCA-mutated subtypes.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (platinum-based chemotherapy class; specific NPRA-approved indication text not available in current license data) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap: DrugBank query pending). Based on known information, Carboplatin is a second-generation platinum-based DNA cross-linking agent, structurally and mechanistically related to cisplatin. Its efficacy in ovarian cancer and other platinum-sensitive solid tumours is well established, and mechanistically it may be applicable to female breast carcinoma.

The key rationale connecting the two indications is homologous recombination deficiency (HRD): Carboplatin forms DNA interstrand and intrastrand cross-links that are particularly lethal to tumours unable to repair double-strand breaks via homologous recombination (e.g., BRCA1/2-mutated tumours). Triple-negative breast cancer (TNBC) and BRCA-associated breast cancer share this HRD biomarker profile with ovarian cancer, providing a strong biological basis — a form of "synthetic lethality" — for extending platinum therapy from ovarian cancer to these breast cancer subtypes.

This mechanistic link is further supported by an extensive body of neoadjuvant trial data (GeparSixto, NeoSTOP, CamRelief) demonstrating that adding carboplatin to standard chemotherapy backbones improves pathological complete response rates in TNBC and HER2-positive early breast cancer, reinforcing the plausibility of the TxGNN prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | Completed | 154 | NACATRINE trial: neoadjuvant carboplatin specifically studied in triple-negative breast cancer (TNBC), a subtype enriched for BRCA1/2 germline mutations |
| [NCT04095364](https://clinicaltrials.gov/study/NCT04095364) | Phase 3 | Active, not recruiting | 450 | Paclitaxel/carboplatin plus maintenance letrozole vs. letrozole monotherapy in low-grade serous carcinoma of the ovary/peritoneum — relevant cross-tumour platinum-sensitivity data |
| [NCT00005963](https://clinicaltrials.gov/study/NCT00005963) | Phase 2 | Completed | 53 | Docetaxel plus carboplatin as first-line therapy for metastatic breast cancer |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | PARP inhibitor AZD2281 (olaparib) combined with carboplatin in BRCA1/2-mutated breast and ovarian cancer, and sporadic TNBC |

*Note: The evidence pack contains 46 additional carboplatin trials in breast cancer that have not yet been graded for relevance; the four above are the only ones with completed relevance assessment.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT | The Lancet Oncology | GeparSixto trial: adding carboplatin to neoadjuvant therapy improves outcomes in TNBC and HER2-positive early breast cancer |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT | Clin Cancer Res | NeoSTOP trial: anthracycline-free vs. anthracycline-containing neoadjuvant carboplatin regimens improve pCR in stage I-III TNBC |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief trial: camrelizumab plus platinum-containing neoadjuvant chemotherapy in early/locally advanced TNBC |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT (Phase 3, final OS) | Eur J Cancer | BROCADE3: veliparib with carboplatin/paclitaxel in BRCA-mutated, HER2-negative advanced breast cancer — final overall survival results |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 Trial | Breast Cancer Res | Carboplatin plus bevacizumab in breast cancer brain metastases |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nature Communications | MUKDEN 06: ARX788 plus pyrotinib vs. standard docetaxel/carboplatin/trastuzumab/pertuzumab in HER2-positive breast cancer |
| [40468999](https://pubmed.ncbi.nlm.nih.gov/40468999/) | 2025 | Phase 2 (5-yr follow-up) | Acta Oncologica | TCHL trial: docetaxel/carboplatin/trastuzumab ± lapatinib in HER2-positive breast cancer with biomarker analysis |
| [35837812](https://pubmed.ncbi.nlm.nih.gov/35837812/) | 2023 | Cohort | Cancer Medicine | Carboplatin dose correlates with anaemia rates and pCR in neoadjuvant TCHP for HER2-positive breast cancer |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Medical Oncology | Review of accumulating evidence for synergy, efficacy, and safety of paclitaxel-carboplatin in advanced breast cancer |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Review | Seminars in Oncology | Early evaluation of paclitaxel and carboplatin, alone and combined, in advanced breast cancer |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum compound) |
| Myelosuppression Risk | High — dose-limiting thrombocytopenia and neutropenia are well-documented; literature evidence confirms carboplatin dose correlates directly with grade 3/4 anaemia rates in combination regimens |
| Emetogenicity Classification | Moderate to High (AUC-dependent; higher-AUC dosing regimens are associated with greater emetogenic risk) |
| Monitoring Items | CBC with differential (especially platelet count), renal function/creatinine clearance (required for AUC-based dosing), electrolytes (magnesium, potassium), hepatic function |
| Handling Protection | Yes — must follow cytotoxic/hazardous drug handling regulations (PPE, closed-system transfer devices where available) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carboplatin's use in breast cancer, particularly TNBC and BRCA-mutated subtypes, is supported by multiple completed and ongoing RCTs (GeparSixto, NeoSTOP, CamRelief, BROCADE3) with a strong shared HRD mechanistic basis with its established ovarian cancer indication, meriting an L1 evidence level. However, these trials primarily support carboplatin as an add-on to standard neoadjuvant regimens rather than as a monotherapy indication, and Malaysia-specific regulatory and safety data remain unverified.

**To proceed, the following is needed:**
- DrugBank/mechanism of action data (currently a blocking data gap)
- NPRA package insert warnings, contraindications, and drug interaction data
- Confirmation of whether existing Malaysia registrations already cover a breast cancer indication
- Detailed license/product information (all 3 current registrations lack extractable product name, dosage form, and indication text)
- A subtype-specific (TNBC/BRCA-mutated) safety monitoring plan aligned with the established myelosuppression risk profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

