---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 5
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Neoplasm

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug originally established for metastatic colorectal cancer and metastatic breast cancer. The TxGNN model's top-ranked prediction points to **Gastric Neoplasm**, an indication already substantiated by **50+ clinical trials** and **20 publications** in the evidence pack — including several completed Phase 3 RCTs that already use capecitabine as a chemotherapy backbone in gastric cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Malaysia regulatory extract (all `approved_indication_text` fields are empty). Per capecitabine's global label, established indications are metastatic colorectal cancer, adjuvant colon cancer, and metastatic breast cancer. |
| Predicted New Indication | Gastric Neoplasm |
| TxGNN Prediction Score | 0.00% (as recorded in source data; flagged for verification given it is ranked #1) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on known pharmacology, capecitabine is an orally administered prodrug of 5-fluorouracil (5-FU). It is sequentially converted by carboxylesterase (liver), cytidine deaminase (liver/tumor), and thymidine phosphorylase — an enzyme frequently overexpressed in tumor tissue — into active 5-FU, which inhibits thymidylate synthase and disrupts DNA/RNA synthesis in rapidly dividing cells.

Colorectal cancer and gastric cancer are both gastrointestinal adenocarcinomas with overlapping sensitivity to fluoropyrimidine-based chemotherapy. Capecitabine, in combination with platinum agents (notably oxaliplatin), is already used as a standard chemotherapy backbone for gastric cancer in multiple jurisdictions — a pattern reflected directly in this evidence pack through completed Phase 3 trials such as CLASSIC (adjuvant capecitabine + oxaliplatin after D2 gastrectomy) and ARTIST (capecitabine + cisplatin ± radiotherapy).

Because thymidine phosphorylase upregulation and rapid cell turnover are shared features of gastric and colorectal tumor tissue, the mechanistic rationale for capecitabine's activity in gastric cancer is strong. In effect, this TxGNN prediction largely reconfirms an already well-established off-label/regional use rather than surfacing a novel hypothesis — which also explains why ranks 1, 3, and 4 in this evidence pack (gastric neoplasm, gastric carcinoma, gastric cancer) are essentially synonymous disease terms.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01774786](https://clinicaltrials.gov/study/NCT01774786) | Phase 3 | Completed | 780 | Pertuzumab + trastuzumab + fluoropyrimidine/cisplatin chemotherapy in HER2+ metastatic gastric/GEJ cancer |
| [NCT03615326](https://clinicaltrials.gov/study/NCT03615326) | Phase 3 | Completed | 738 | KEYNOTE-811: pembrolizumab + trastuzumab + chemotherapy vs placebo in HER2+ advanced gastric/GEJ adenocarcinoma |
| [NCT03817268](https://clinicaltrials.gov/study/NCT03817268) | Phase 3 | Unknown | 768 | CAPOGA: adjuvant capecitabine vs observation after R0 resection of early-stage gastric adenocarcinoma |
| [NCT02076594](https://clinicaltrials.gov/study/NCT02076594) | Phase 3 | Terminated | 171 | Low-dose docetaxel/oxaliplatin/capecitabine vs epirubicin/oxaliplatin/capecitabine (EOX) in advanced gastric cancer |
| [NCT06177041](https://clinicaltrials.gov/study/NCT06177041) | Phase 3 | Recruiting | 486 | M108 monoclonal antibody + CAPOX vs placebo + CAPOX in CLDN18.2-positive gastric/GEJ adenocarcinoma |
| [NCT07118527](https://clinicaltrials.gov/study/NCT07118527) | Phase 3 | Recruiting | 600 | SHR-A1811 + chemotherapy + adebrelimab vs trastuzumab + chemotherapy + pembrolizumab, first-line gastric/GEJ adenocarcinoma |
| [NCT03627728](https://clinicaltrials.gov/study/NCT03627728) | Phase 2 | Completed | 67 | a-MANTRA: maintenance regorafenib vs placebo after first-line platinum + fluoropyrimidine (incl. capecitabine) in HER2-negative gastric/GEJ cancer |
| [NCT02335411](https://clinicaltrials.gov/study/NCT02335411) | Phase 2 | Completed | 318 | KEYNOTE-059: pembrolizumab monotherapy and combined with cisplatin + 5-FU/capecitabine in recurrent/metastatic gastric/GEJ adenocarcinoma |
| [NCT05266300](https://clinicaltrials.gov/study/NCT05266300) | N/A | Completed | 722 | Clinical implementation of DPYD-genotyping for patients starting fluoropyrimidines (5-FU, capecitabine, tegafur) — safety-relevant |
| [NCT00130936](https://clinicaltrials.gov/study/NCT00130936) | Phase 1/2 | Terminated | 50 | Epirubicin + carboplatin + capecitabine (ECC) in unresectable/metastatic gastric/GEJ cancer with pharmacogenetic correlates |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT (Phase 2/3) | Lancet | FLOT4: docetaxel triplet vs fluorouracil/capecitabine + cisplatin + epirubicin as perioperative therapy for resectable gastric/GEJ adenocarcinoma |
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT (Phase 3) | Lancet | CLASSIC: adjuvant capecitabine + oxaliplatin vs observation after D2 gastrectomy improves disease-free survival |
| [25439693](https://pubmed.ncbi.nlm.nih.gov/25439693/) | 2014 | RCT (Phase 3, follow-up) | Lancet Oncology | CLASSIC 5-year follow-up confirms sustained benefit of adjuvant capecitabine + oxaliplatin |
| [33278599](https://pubmed.ncbi.nlm.nih.gov/33278599/) | 2021 | RCT (Phase 3) | Annals of Oncology | ARTIST 2: adjuvant S-1 vs S-1+oxaliplatin vs chemoradiation in node-positive gastric cancer after D2 resection |
| [22184384](https://pubmed.ncbi.nlm.nih.gov/22184384/) | 2012 | RCT (Phase 3) | J Clin Oncol | ARTIST: capecitabine + cisplatin vs capecitabine + cisplatin + concurrent capecitabine radiotherapy after D2 resection |
| [34275019](https://pubmed.ncbi.nlm.nih.gov/34275019/) | 2021 | Systematic review / meta-analysis | Eur J Clin Pharmacol | Comparison of S-1-based vs capecitabine-based adjuvant chemotherapy for gastric cancer |
| [32389017](https://pubmed.ncbi.nlm.nih.gov/32389017/) | 2020 | Systematic review / meta-analysis | Annals of Palliative Medicine | Efficacy and safety of capecitabine-based vs S-1-based chemotherapy for metastatic/recurrent gastric cancer |
| [21415237](https://pubmed.ncbi.nlm.nih.gov/21415237/) | 2011 | Meta-analysis (individual patient data) | Annals of Oncology | Capecitabine vs 5-FU efficacy in colorectal and gastric cancers — pooled analysis of 6,171 patients |
| [26470733](https://pubmed.ncbi.nlm.nih.gov/26470733/) | 2015 | Review | Expert Rev Gastroenterol Hepatol | Capecitabine has replaced infusional 5-FU as the preferred fluoropyrimidine backbone for gastric cancer |
| [24090307](https://pubmed.ncbi.nlm.nih.gov/24090307/) | 2013 | Review | Expert Opin Investig Drugs | Capecitabine in the treatment of esophageal and gastric cancers |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Not available | Not available | Not available |

The source dataset records **12 total registrations** with market status "已上市" (Marketed), but all individual license fields (authorization number, product name, dosage form, approved indication text) are empty in this extract. License-level detail needs to be re-pulled from NPRA before this section can be completed.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class — oral 5-FU prodrug) |
| Myelosuppression Risk | Low–Moderate — generally less myelosuppressive than IV 5-FU; hand-foot syndrome and diarrhea are typically the dose-limiting toxicities rather than cytopenia |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, renal function (dose adjustment required in renal impairment), liver function, hand-foot syndrome grading; DPD/DPYD genotype status is a recognized pre-treatment safety consideration (per NCT05266300) |
| Handling Protection | Must follow standard cytotoxic drug handling and dispensing protocols; patient counseling required for an oral cytotoxic agent |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA/NPRA-specific key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (Data Gap DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for capecitabine in gastric cancer is strong (Evidence Level L1 — multiple completed Phase 3 RCTs, including CLASSIC, ARTIST, and FLOT4, directly or indirectly support this use). However, Data Gap DG001 (missing TFDA/NPRA warnings and contraindications) is explicitly Blocking and prevents completion of the S1 safety screening stage, so the candidate cannot advance until safety labeling data is obtained.

**To proceed, the following is needed:**
- Malaysia (NPRA) package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Actual NPRA-approved indication text and product details for the 12 registered licenses (current records are empty)
- Formal DDI query results (current query status: not found)
- Clarification of the TxGNN score of 0.00% for the rank-1 prediction, given it appears inconsistent with the rank position
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

