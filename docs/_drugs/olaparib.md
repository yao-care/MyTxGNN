---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 518
evidence_level: L5
indication_count: 1
---

# Olaparib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Olaparib (Lynparza) is a PARP1/2 inhibitor originally developed and approved for BRCA-mutated ovarian cancer, exploiting a synthetic lethality mechanism in DNA repair-deficient tumors.
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **10 highly relevant clinical trials** and **20 publications** currently supporting this direction — including multiple completed Phase 3 RCTs (OlympiAD, OlympiA).
> **Important caveat**: breast cancer is already an internationally approved Olaparib indication in many markets, so this evidence base largely represents label-consolidation/confirmation rather than a novel repurposing signal; local (Malaysia/Taiwan) registry data does not confirm whether the local label already covers this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in local registry data (globally, Olaparib's first approved indication was BRCA-mutated ovarian cancer maintenance therapy) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Olaparib is a PARP1/2 (poly ADP-ribose polymerase) inhibitor. Its mechanism relies on **synthetic lethality**: in tumors with BRCA1/2 mutations (germline or somatic), homologous recombination DNA repair is already deficient. PARP inhibition blocks single-strand break repair, causing unrepaired breaks to collapse into lethal double-strand breaks selectively in these repair-deficient cancer cells, while sparing normal cells with intact repair machinery.

This mechanism is not tumor-type specific — it depends on the BRCA1/2 or homologous-recombination-deficiency (HRD) status of the tumor, not on the organ of origin. Since both ovarian and breast cancers frequently harbor BRCA1/2 mutations, the mechanistic rationale for extending Olaparib from ovarian to breast cancer is strong and has already been directly validated in randomized controlled trials (OlympiAD, OlympiA), rather than being purely a computational prediction.

**Caveat on novelty**: the evidence pack notes that female breast carcinoma is very likely already an approved global indication for Olaparib (Lynparza), given the maturity of the OlympiAD/OlympiA RCT program. This candidate should therefore be treated primarily as a **local label-verification/evidence-consolidation case** — confirming whether the Malaysia/Taiwan-registered product already carries this indication — rather than a genuinely novel repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06580314](https://clinicaltrials.gov/study/NCT06580314) | Phase 3 | Recruiting | 880 | Compares 1 vs. 2 years of maintenance olaparib (± bevacizumab) in BRCA1/2-mutated or HRD+ ovarian cancer after first-line platinum chemotherapy |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Randomized olaparib monotherapy vs. physician's choice chemotherapy in platinum-sensitive relapsed germline BRCA1/2-mutated ovarian cancer |
| [NCT04553926](https://clinicaltrials.gov/study/NCT04553926) | N/A (post-marketing) | Completed | 661 | Real-world post-marketing surveillance of Lynparza (olaparib) safety/effectiveness in South Korea per approved indications |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Olaparib (AZD2281) + carboplatin in BRCA1/2 mutation carriers with breast/ovarian cancer and sporadic triple-negative breast/ovarian cancer |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | Completed | 77 | PK/PD study of olaparib + carboplatin for refractory/recurrent women's cancers (breast, ovarian, uterine, cervical) |
| [NCT02264678](https://clinicaltrials.gov/study/NCT02264678) | Phase 1/2 | Active, not recruiting | 357 | Ceralasertib + cytotoxic chemotherapy and/or DNA damage repair agents (including olaparib combinations) in advanced solid malignancies |
| [NCT05932862](https://clinicaltrials.gov/study/NCT05932862) | Phase 1 | Recruiting | 429 | First-in-human study of XL309 (ISM3091) alone or combined with olaparib in advanced solid tumors |
| [NCT02684318](https://clinicaltrials.gov/study/NCT02684318) | Phase 1/2 | Unknown | 100 | PM01183 + olaparib combination in advanced solid tumors |
| [NCT06065059](https://clinicaltrials.gov/study/NCT06065059) | Phase 1/2 | Terminated | 7 | TNG348 (USP1 inhibitor) alone and combined with olaparib in BRCA1/2-mutant or HRD+ solid tumors |
| [NCT03162627](https://clinicaltrials.gov/study/NCT03162627) | Phase 1 | Active, not recruiting | 90 | Selumetinib + olaparib in endometrial, ovarian and other solid tumors with Ras pathway alterations or PARP resistance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | The New England Journal of Medicine | OlympiA trial: adjuvant olaparib reduces recurrence in BRCA1/2 germline-mutated, HER2-negative early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | The New England Journal of Medicine | OlympiAD trial: olaparib shows antitumor activity in germline BRCA-mutated metastatic breast cancer |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Annals of Oncology | OlympiAD final OS/tolerability: olaparib vs. chemotherapy of physician's choice in gBRCA-mutated HER2-negative metastatic breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | European Journal of Cancer | OlympiAD extended follow-up confirming OS and safety profile |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Annals of Oncology | OlympiA overall survival analysis of adjuvant olaparib in high-risk early breast cancer with germline BRCA1/2 variants |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT | Nature | PARTNER trial: neoadjuvant olaparib + chemotherapy in germline BRCA wild-type triple-negative breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT (Phase 2) | Journal of Clinical Oncology | TBCRC 048: olaparib activity in metastatic breast cancer with non-BRCA1/2 homologous recombination gene mutations |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT (Phase 2) | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel increases pathologic complete response in HER2-negative breast cancer |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Annals of Laboratory Medicine | Review of BRCA1/BRCA2 pathogenic variant breast cancer treatment and prevention strategies |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved for BRCA-mutated HER2-negative breast cancer |

---

## Malaysia Market Information

The local registry (2 records, market status: 已上市/Marketed) does not include license numbers, product names, dosage forms, or approved-indication text in this evidence pack — these fields were returned empty by the source query and cannot be populated without re-querying the source registry.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is met — multiple completed Phase 3 RCTs (OlympiAD, OlympiA) plus a large post-marketing surveillance study directly support olaparib's efficacy and safety in BRCA-mutated breast cancer. However, local drug-level safety data (warnings, contraindications, DDI) and the exact local approved-indication text are unavailable, and the possibility that breast cancer is already within the current local label has not been confirmed.

**To proceed, the following is needed:**
- Local package insert (warnings, contraindications, drug interactions) — currently a Blocking data gap
- Confirmation of the exact currently approved indication text on the 2 local licenses, to determine whether breast cancer is already covered or requires label expansion
- Formal DrugBank/label-sourced mechanism of action record (currently a High-severity data gap; the mechanistic rationale above is derived from trial/literature evidence, not a structured MOA source)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

