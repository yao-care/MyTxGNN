---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

Oteracil is a component of the S-1 combination (tegafur/gimeracil/oteracil), internationally established for gastric cancer and other GI cancers. The TxGNN model predicts it may also be effective for **Colonic Neoplasm**, and this is backed by **8 clinical trials** (including 2 completed Phase 3 RCTs) and **20 publications**. Notably, the evidence pack's own mechanistic review flags that this may not be a *novel* signal — S-1-based regimens already carry established colorectal cancer indications internationally, so TxGNN may be confirming existing practice rather than discovering a new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric Cancer (S-1 fixed-dose combination; NPRA license text for this specific field is currently blank in the dataset) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for oteracil is currently a data gap. However, the evidence pack's mechanistic review clarifies oteracil's role: it has no independent pharmacological activity of its own. It is the OPRT-inhibitor component of the S-1 fixed-dose combination (tegafur + gimeracil + oteracil), acting locally in the GI mucosa to reduce intestinal phosphorylation of 5-FU, thereby lowering GI toxicity from the 5-FU released by tegafur. This allows the cytotoxic antitumor effect of 5-FU (inhibition of DNA/RNA synthesis) to be delivered more safely.

Gastric cancer and colonic neoplasm are both gastrointestinal malignancies with a shared chemotherapeutic rationale, and S-1-based regimens are already widely used and studied in colorectal cancer across Japan and other markets (e.g., the ACTS-CC and ACTS-RC Phase 3 trials below).

**Important caveat**: the evidence pack explicitly notes that colorectal cancer use is likely an *existing* core indication of the S-1 combination rather than a genuinely novel repurposing hypothesis — TxGNN's high score here may reflect an already-marketed use rather than a new discovery. This should be verified against the actual NPRA label text (currently blank in this dataset) before treating this as a novel finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs. capecitabine (± bevacizumab) as first-line therapy for metastatic colorectal cancer, with a focus on oral fluoropyrimidine safety |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | ACTS-CC trial: UFT+leucovorin vs. S-1 as adjuvant therapy for Stage III colon cancer, with gene-expression predictive biomarker analysis |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown (results not updated) | 1191 | SOX (oxaliplatin+S-1) vs. XELOX (oxaliplatin+capecitabine) as adjuvant therapy for Stage III colorectal cancer |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after standard chemotherapy failure; primary endpoint is progression-free survival |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after prior irinotecan/oxaliplatin failure |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL regimen) in untreated metastatic colorectal cancer |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | Cardiac safety comparison of S-1 vs. capecitabine/oxaliplatin in metastatic GI adenocarcinoma (cardiotoxicity study, not an efficacy trial) |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib + S-1 (tegafur/gimeracil/oteracil) in third-line treatment of advanced metastatic colorectal cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02: S-1+oxaliplatin (SOX) vs. UFT/LV as adjuvant therapy in high-risk Stage III colon cancer |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Ann Oncol | ACTS-RC (JFMC35-C1): S-1 vs. UFT as adjuvant chemotherapy for Stage II/III rectal cancer |
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT | Ann Oncol | ACTS-CC trial: S-1 as adjuvant chemotherapy for Stage III colon cancer, noninferiority vs. UFT/LV |
| [26976971](https://pubmed.ncbi.nlm.nih.gov/26976971/) | 2016 | RCT (biomarker substudy) | Anticancer Research | Genome-wide DNA copy-number analysis within the ACTS-CC adjuvant trial |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | RCT (safety analysis) | Br J Cancer | Planned safety analysis of the ACTS-CC Phase 3 trial (UFT/LV vs. S-1) |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | Phase 2 trial | Int J Clin Oncol | KSCC1303: efficacy and feasibility of S-1+oxaliplatin (C-SOX) as adjuvant therapy for Stage III colon cancer, 3-year DFS analysis |
| [23320901](https://pubmed.ncbi.nlm.nih.gov/23320901/) | 2013 | RCT protocol | Trials | Study protocol for optimal scheduling of S-1 adjuvant chemotherapy in Stage III colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review/Guideline | Clin Colorectal Cancer | Asian consensus adaptation of international guidelines for metastatic colorectal cancer |
| [10897209](https://pubmed.ncbi.nlm.nih.gov/10897209/) | 2000 | Review | Gan To Kagaku Ryoho | Conceptual basis of S-1's biochemical modulation of 5-FU (mechanism review) |
| [17496461](https://pubmed.ncbi.nlm.nih.gov/17496461/) | 2007 | Review | Gan To Kagaku Ryoho | Status and issues of adjuvant chemotherapy for colorectal cancer in Japan |

---

## Malaysia Market Information

NPRA records 2 active registrations for this product, but the license number, product name, dosage form, and approved indication text fields are currently blank in this dataset — the underlying label/registration detail has not yet been retrieved (see Data Gap DG001, blocking severity). This needs to be sourced directly from NPRA before market-status claims can be finalized.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — fluoropyrimidine class (oteracil is the OPRT-inhibitor component of the S-1 combination) |
| Myelosuppression Risk | Not directly quantified in this evidence pack; please refer to the package insert. Literature case reports document hand-foot syndrome with erythroderma (PMID 28414195) and hypertriglyceridemia (PMID 32936722) as reported adverse events with S-1-based regimens |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (no data in evidence pack) |
| Monitoring Items | CBC with differential, liver and renal function, triglycerides |
| Handling Protection | Standard cytotoxic drug handling precautions apply for fluoropyrimidine chemotherapy; confirm specific requirements via the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — DG001, blocking severity.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1: 2 completed Phase 3 RCTs plus multiple additional Phase 3 RCTs in the literature, e.g. ACTS-CC/ACTS-RC), but a blocking data gap on the official label/warnings (DG001) and MOA (DG002) prevents a full safety sign-off. There is also an important open question: the evidence pack itself suggests colorectal cancer may already be an established indication for S-1 internationally, meaning this "predicted" indication could be confirming existing practice rather than a genuinely novel repurposing candidate — this needs to be resolved before further action.

**To proceed, the following is needed:**
- NPRA package insert/label download and parsing (resolves DG001, blocking)
- DrugBank MOA confirmation (resolves DG002)
- Actual NPRA-registered indication text for the 2 Malaysia licenses (currently blank), to confirm whether colorectal cancer is already on-label locally
- DDI data source, since the current query returned no results (not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

