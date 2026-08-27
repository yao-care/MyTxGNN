---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Pancreatic Cancer to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine (DrugBank DB00441) is a deoxycytidine-analog chemotherapy agent long established in solid-tumor treatment (pancreatic, NSCLC, bladder, ovarian cancer). The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, a use already partially supported outside this evidence pack (e.g., approved gemcitabine + paclitaxel regimens), with **50 clinical trials** and **20 publications** currently retrieved. However, a **Blocking** data gap in safety labeling (NPRA warnings/contraindications) means this candidate cannot yet clear the S1 safety screen.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this NPRA data pull (all license `approved_indication_text` fields are blank). Gemcitabine's internationally approved indications include pancreatic cancer, non-small cell lung cancer, bladder cancer, and ovarian cancer. |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is a data gap). Based on well-established pharmacology, gemcitabine is a pyrimidine (deoxycytidine) nucleoside analog antimetabolite: it is phosphorylated intracellularly to its active triphosphate form, which is incorporated into DNA to cause chain termination, and its diphosphate form inhibits ribonucleotide reductase, depleting deoxynucleotide pools needed for DNA replication and repair.

This mechanism is not tumor-type specific — it targets rapidly dividing cells broadly, which is why gemcitabine already has approved or guideline-supported use across multiple solid tumors (pancreatic, NSCLC, bladder, ovarian) and is combined with taxanes, platinum agents, and HER2-targeted therapy. Breast cancer shares the same fundamental dependence on rapid cell proliferation, and gemcitabine + paclitaxel is in fact an established regimen for metastatic breast cancer in many jurisdictions, which aligns mechanistically and clinically with the TxGNN prediction.

The very large volume of retrieved trials (50) spanning HER2-positive, triple-negative, and metastatic breast cancer settings — often in combination with trastuzumab, taxanes, platinum agents, or bevacizumab — further supports that this is not a novel, untested mechanistic hypothesis but an extension of an already active clinical development line.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Gemcitabine+Herceptin vs. Capecitabine+Herceptin in pretreated HER2-positive metastatic breast cancer |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | Completed | 326 | Maintenance vs. observation after 6 cycles of gemcitabine+paclitaxel as 1st-line chemotherapy for metastatic/recurrent breast cancer |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant trial adding capecitabine or gemcitabine to docetaxel (±bevacizumab) before AC, evaluating pathologic complete response |
| [NCT01050322](https://clinicaltrials.gov/study/NCT01050322) | Phase 2 | Completed | 142 | Lapatinib-capecitabine vs. lapatinib-vinorelbine vs. lapatinib-gemcitabine in HER2/neu-amplified metastatic breast cancer after taxane progression |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Completed | 50 | Weekly nab-paclitaxel plus gemcitabine in metastatic breast cancer |
| [NCT00193063](https://clinicaltrials.gov/study/NCT00193063) | Phase 2 | Completed | 41 | Weekly gemcitabine plus trastuzumab in HER2-overexpressing metastatic breast cancer |
| [NCT00005991](https://clinicaltrials.gov/study/NCT00005991) | Phase 1/2 | Completed | 76 | Gemcitabine plus liposomal doxorubicin (Doxil) in metastatic breast cancer |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Phase 2 | Completed | 59 | Gemcitabine plus pemetrexed (MTA/LY231514) in metastatic breast cancer |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | Completed | 30 | Gemcitabine monotherapy in metastatic breast cancer previously treated with doxorubicin and paclitaxel |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Phase 2 | Completed | 19 | Gemcitabine plus genistein in metastatic breast cancer, with biomarker assays |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase 1 trial | Gynecologic Oncology | Mirvetuximab soravtansine + gemcitabine in FRα-positive recurrent ovarian/endometrial cancer and triple-negative breast cancer; MTD/RP2D determination |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1 trial | Breast Cancer Research and Treatment | Carboplatin + gemcitabine + mifepristone (GR antagonist) in GR-positive advanced breast and ovarian cancer to enhance chemosensitivity |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Phase 2 trial | Cancer Chemotherapy and Pharmacology | Docetaxel, gemcitabine, and bevacizumab as salvage chemotherapy for HER2-negative metastatic breast cancer |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 trial | Oncology | Weekly docetaxel plus gemcitabine as first-line treatment for metastatic breast cancer |
| [12722022](https://pubmed.ncbi.nlm.nih.gov/12722022/) | 2003 | Phase 2 trial | Seminars in Oncology | Gemcitabine plus trastuzumab in heavily pretreated HER2-overexpressing metastatic breast cancer |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Review of gemcitabine + paclitaxel combination regimens/schedules in metastatic breast cancer |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | Review of gemcitabine + docetaxel combination rationale and dosing in metastatic breast cancer |
| [14754467](https://pubmed.ncbi.nlm.nih.gov/14754467/) | 2004 | Review | Clinical Breast Cancer | Gemcitabine and taxanes positioned as a new standard-of-care combination in breast cancer |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Seminars in Oncology | Review of gemcitabine single-agent and combination (targeted therapy) activity in metastatic breast cancer |
| [21980041](https://pubmed.ncbi.nlm.nih.gov/21980041/) | 2011 | Pharmacogenetic study | Cancer Genomics & Proteomics | Gemcitabine/platinum pathway pharmacogenetics predicting hematologic toxicity in Asian breast cancer patients |

---

## Malaysia Market Information

Gemcitabine is confirmed marketed in Malaysia with **16 active NPRA registrations**. However, the individual license-level fields (authorization number, product name, dosage form, approved indication text) were not populated in this data pull — all `licenses[]` entries came back blank. Product-level detail needs to be re-fetched from the NPRA product registry before this can be tabulated.

---

## Cytotoxicity

Gemcitabine is a conventional cytotoxic chemotherapy agent (pyrimidine/deoxycytidine analog antimetabolite), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (pyrimidine antimetabolite / nucleoside analog) |
| Myelosuppression Risk | High — antimetabolites of this class commonly cause dose-limiting neutropenia, thrombocytopenia, and anemia; drug-specific incidence data is not present in this evidence pack |
| Emetogenicity Classification | Low to moderate (typical for single-agent gemcitabine per standard antiemetic risk classification; combination regimens may be higher) |
| Monitoring Items | CBC with differential before each cycle, liver function tests, renal function |
| Handling Protection | Yes — standard cytotoxic/hazardous drug handling precautions required during preparation and administration |

Please refer to the package insert warnings and precautions for drug-specific detail, as none was captured in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack has no populated key warnings, contraindications, or drug-interaction data — all fields returned as data gaps, and the NPRA drug interaction (DDI) query returned no results (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy-side evidence is substantial (50 trials including a completed Phase 3 RCT and multiple completed Phase 2 studies, plus 20 supporting publications), but data gap DG001 — missing NPRA warnings/contraindications — is flagged **Blocking** and explicitly prevents entry into the S1 safety initial assessment. Efficacy strength alone cannot substitute for a safety review that has not yet occurred.

**To proceed, the following is needed:**
- Retrieve and parse the NPRA package insert (warnings, contraindications) — DG001, Blocking
- Retrieve gemcitabine mechanism of action from DrugBank API — DG002, High
- Re-pull NPRA license-level product data (product name, dosage form, approved indication text) for the 16 registrations
- Drug-drug interaction data from a source other than the current NPRA DDI query (returned zero results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

