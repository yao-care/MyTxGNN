---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Castration-Resistant Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Cabazitaxel is a next-generation taxane chemotherapy agent, originally approved (in combination with prednisone) for docetaxel-refractory metastatic castration-resistant prostate cancer.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, and this direction is already supported by **1 completed randomized Phase II trial, 2 additional early-phase clinical trials, and 20 publications** identified in this evidence pack — though no entries were found in the structured ClinicalTrials.gov/ICTRP registries.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic castration-resistant (hormone-refractory) prostate cancer, in combination with prednisone (per literature evidence, e.g. PMID [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/), [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/); TFDA/NPRA structured indication text not available in this pack) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% (rank 1,590) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`, DG002). Based on the literature evidence collected here, cabazitaxel is a **taxane-class anti-microtubule agent** (PMID [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/), [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/)) developed as a next-generation taxane specifically to overcome P-glycoprotein-mediated resistance seen with docetaxel and paclitaxel (PMID [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/), [21152241](https://pubmed.ncbi.nlm.nih.gov/21152241/)). Its established use is in docetaxel-pretreated metastatic castration-resistant prostate cancer.

Taxanes as a class (paclitaxel, docetaxel) are already standard-of-care cytotoxic chemotherapy in breast cancer, so the mechanistic link between the original indication and the predicted indication is strong: both are solid tumors in which microtubule-stabilizing agents disrupt mitotic spindle function to induce cell death. Cabazitaxel's reduced susceptibility to Pgp-mediated efflux resistance is particularly relevant for breast cancer patients who have progressed on prior taxane therapy.

This mechanistic plausibility is not purely theoretical — it is already being tested clinically. The GENEVIEVE trial (PMID [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/)) directly compared neoadjuvant cabazitaxel against weekly paclitaxel in operable HER2-negative breast cancer, and separate trials have evaluated cabazitaxel in taxane/anthracycline-pretreated metastatic breast cancer (PMID [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/)) and in HER2-positive breast cancer with CNS metastases, leveraging cabazitaxel's blood-brain barrier penetration (PMID [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/)). These findings substantially strengthen the credibility of the TxGNN prediction beyond model-score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP queries for "Cabazitaxel" + "female breast carcinoma" both returned 0 results as of 2026-03-26). Note: several relevant clinical-phase studies were identified via PubMed literature instead — see Literature Evidence below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | European Journal of Cancer | GENEVIEVE trial: randomized, open-label Phase II comparing neoadjuvant cabazitaxel vs. weekly paclitaxel in operable triple-negative or luminal B/HER2-negative breast cancer, evaluating pathological complete response rate. |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II Trial | Clinical Breast Cancer | Dose-finding study of cabazitaxel plus lapatinib (NCT01934894) for HER2+ metastatic breast cancer with intracranial metastases, exploiting cabazitaxel's blood-brain barrier penetration. |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II Trial | European Journal of Cancer | Multicentre dose-escalation study of cabazitaxel + capecitabine in metastatic breast cancer previously treated with anthracyclines and taxanes; established MTD, safety, PK and activity. |
| [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/) | 2016 | Review | Expert Opinion on Therapeutic Patents | Taxane anticancer agent patent review, including cabazitaxel's approval history and use across cancer types. |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | Review of therapeutic drug monitoring-based dose adjustment for taxanes, including cabazitaxel pharmacokinetics. |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs of Today | Overview of cabazitaxel's pharmacokinetic and safety profile; notes neutropenia and neuropathy as principal toxicities from Phase I data. |
| [27215440](https://pubmed.ncbi.nlm.nih.gov/27215440/) | 2016 | Review | Current Pharmaceutical Design | Review of colloidal drug delivery carriers for taxanes (paclitaxel, docetaxel, cabazitaxel) in breast, prostate, lung and ovarian cancer. |
| [36080414](https://pubmed.ncbi.nlm.nih.gov/36080414/) | 2022 | Review | Molecules | Historical/mechanistic review of microtubule-targeting agents, including the taxane class. |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Preclinical | Molecular Cancer Therapeutics | Mechanisms of cabazitaxel resistance studied using cabazitaxel-resistant variants derived from MCF-7 breast cancer cells. |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | Cabazitaxel-loaded nanoparticles showed improved efficacy over free drug in a basal-like patient-derived breast cancer xenograft model. |

---

## Malaysia Market Information

The evidence pack confirms cabazitaxel is **marketed in Malaysia with 4 active registrations** (`market_status: 已上市`), but individual license details (registration number, product name, dosage form, approved indication text) were not populated in this data pull. This should be treated as a data gap requiring a follow-up query to the NPRA QUEST3+ registration system before Malaysia-specific labelling can be confirmed.

---

## Cytotoxicity

Cabazitaxel is a cytotoxic chemotherapy agent (taxane class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — taxane-class microtubule inhibitor |
| Myelosuppression Risk | High — neutropenia is reported as a principal dose-limiting toxicity in Phase I data (PMID [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/)); consistent with known taxane class effects |
| Emetogenicity Classification | Low to Moderate (consistent with taxane class) |
| Monitoring Items | CBC with differential (absolute neutrophil count), peripheral neuropathy assessment, liver and renal function |
| Handling Protection | Requires cytotoxic drug handling precautions (hazardous drug PPE, closed-system transfer where applicable) per standard chemotherapy handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warnings, contraindications, and drug interaction data were not available in this evidence pack (DG001, Blocking severity — TFDA/NPRA package insert not yet parsed; DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence Level L2 is supported by a completed randomized Phase II trial (GENEVIEVE) directly comparing cabazitaxel to a standard taxane in breast cancer, plus two additional early-phase clinical trials showing activity in pretreated and CNS-involved metastatic breast cancer. The mechanistic rationale (taxane-class agent in a cancer type where taxanes are standard of care) is strong, and the drug is already marketed in Malaysia. However, the **Blocking** safety data gap (DG001) prevents this candidate from formally entering the S1 safety pre-screen until resolved.

**To proceed, the following is needed:**
- TFDA/NPRA package insert PDF retrieval and parsing for warnings/contraindications (DG001 — Blocking)
- DrugBank MOA confirmation (DG002)
- Malaysia-specific license record details (registration number, dosage form, approved indication text) — currently blank in this evidence pack
- Formal drug-drug interaction database query (current status: not found)
- Clarify whether the 3 clinical-phase literature findings (GENEVIEVE, dose-finding, dose-escalation) should be manually cross-registered into the structured clinical trial evidence store, since they did not surface via the ClinicalTrials.gov/ICTRP search

*Note: Ranks 2–10 in this evidence pack (a cluster of near-identical scores ~0.9989 for sickle cell disease variants, plus HIV, hyperthyroidism, neuroblastoma, and rheumatoid arthritis) show no supporting clinical trial or literature evidence, and reviewer annotations already flag several of these as likely TxGNN embedding-space noise (L5/S0/Hold). These are not carried forward in this report and are recommended for no further individual investigation unless new evidence emerges.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

