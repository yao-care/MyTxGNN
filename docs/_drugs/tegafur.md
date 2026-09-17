---
layout: default
title: Tegafur
parent: High Evidence (L1-L2)
nav_order: 637
evidence_level: L1
indication_count: 10
---

# Tegafur
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Tegafur: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

> Tegafur is an oral fluoropyrimidine (prodrug of 5-fluorouracil) marketed in Malaysia as part of fluoropyrimidine combinations (e.g., UFT, S-1) used for gastrointestinal malignancies. The TxGNN model predicts it may be effective for **Colonic Neoplasm**, with **30 clinical trials** and **20 publications** currently supporting this direction — including six completed Phase 3 randomized trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (fluoropyrimidine class; specific NPRA-approved label text was not captured in this evidence pack — see Malaysia Market Information) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this Tegafur record is not yet available in the evidence pack (flagged as data gap DG002). Based on general pharmacology, Tegafur is a prodrug of 5-fluorouracil (5-FU) and is the active component of widely used oral combinations such as UFT (tegafur + uracil, where uracil blocks 5-FU degradation) and S-1 (tegafur + gimeracil + oteracil). Once converted to 5-FU, it inhibits thymidylate synthase, blocking DNA synthesis in rapidly dividing cells.

Gastric cancer and colonic neoplasm are both gastrointestinal adenocarcinomas that share chemosensitivity to fluoropyrimidines. This is directly reflected in the evidence pack itself: the second-ranked predicted indication, gastric carcinoma, is explicitly assessed as an "existing approved indication extension" (L1 evidence, Proceed with Guardrails), meaning tegafur-based regimens are already standard-of-care across multiple GI cancer types in East Asia.

The colonic neoplasm signal is therefore mechanistically consistent: tegafur/UFT and S-1-based regimens (SOX, UFT+LV, S-1+oxaliplatin) are established adjuvant and metastatic treatments for colon and colorectal cancer in international and Asian guidelines, further supporting the plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2025 | Adjuvant tegafur-uracil (UFT) vs. observation in curatively resected Stage II colon cancer |
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1608 | Oral UFT+leucovorin vs. IV 5-FU+leucovorin in Stage II/III colon carcinoma |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+leucovorin vs. S-1 (TS-1) as adjuvant therapy for Stage III colon cancer |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1+oxaliplatin) vs. XELOX as adjuvant chemotherapy, Stage III colorectal cancer |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | Postoperative adjuvant UFT vs. surgery alone in Dukes C colorectal cancer (NSAS-CC) |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | S-1 vs. capecitabine, first-line metastatic colorectal cancer (SALTO trial) |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | Completed | 89 | Crossover comparison of capecitabine vs. UFT+folinic acid in advanced/metastatic colorectal cancer |
| [NCT02836977](https://clinicaltrials.gov/study/NCT02836977) | N/A | Unknown | 400 | Maintenance tegafur-uracil vs. observation after adjuvant oxaliplatin-based regimen, Stage III colon cancer |
| [NCT02887365](https://clinicaltrials.gov/study/NCT02887365) | Phase 4 | Unknown | 300 | Tegafur-uracil as maintenance chemotherapy, Stage II MSI-L/MSS colon cancer |
| [NCT05266300](https://clinicaltrials.gov/study/NCT05266300) | N/A | Completed | 722 | DPYD-genotyping implementation and QA in patients treated with fluoropyrimidines (relevant to toxicity risk stratification) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT (Phase 3) | Clinical Colorectal Cancer | ACTS-CC 02 trial: S-1+oxaliplatin (SOX) vs. UFT/LV as adjuvant chemotherapy, high-risk Stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT (Phase 3 update) | ESMO Open | ACTS-CC 02 updated 5-year overall survival and subgroup analysis |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT (Phase 3) | Journal of Clinical Oncology | NSABP C-06: oral UFT+leucovorin vs. IV 5-FU+leucovorin, Stage II/III colon carcinoma |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT (Phase 3) | Annals of Oncology | JFMC33-0502: optimal treatment duration for UFT/LV adjuvant chemotherapy, Stage IIB/III colon cancer |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Prospective observational | BMC Cancer | JFMC46-1201: UFT/LV efficacy in high-risk Stage II colon cancer using propensity score matching |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective controlled study (final analysis) | International Journal of Clinical Oncology | JFMC46-1201 final results, updated 5-year survival and risk factor analysis |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Nationwide cohort + meta-analysis | Medicine | UFT vs. 5-FU as postoperative adjuvant chemotherapy, Stage II/III colon cancer (Taiwan NHIRD) |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT as postoperative adjuvant chemotherapy for solid tumors: clinical evidence, mechanism, future direction |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review / Consensus guideline | Clinical Colorectal Cancer | Asian consensus on adaptation of international guidelines for metastatic colorectal cancer |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | International Journal of Clinical Oncology | Adjuvant immunochemotherapy (OK-432) with UFT/HCFU for colorectal cancer |

---

## Malaysia Market Information

The evidence pack confirms Tegafur is currently marketed in Malaysia with **3 active registrations**, but the underlying license record (registration number, product name, dosage form, and approved indication text) was not populated in this data pull. This is a data-collection gap on the NPRA source side, not an indication that the product is unregistered — it should be resolved by re-querying the NPRA product register before finalizing any regulatory submission.

---

## Cytotoxicity

Tegafur is an antineoplastic drug (conventional cytotoxic, fluoropyrimidine class; prodrug of 5-fluorouracil), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — fluoropyrimidine class (5-FU prodrug) |
| Myelosuppression Risk | Moderate — leukopenia and thrombocytopenia are recognized class effects of fluoropyrimidines; the evidence pack also includes a case report of UFT-induced haemolytic anaemia (PMID 11320674) |
| Emetogenicity Classification | Low to moderate (typical for oral fluoropyrimidines) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; DPD/DPYD genotyping or phenotyping is directly supported by evidence in this pack (NCT05266300, DPYD-genotyping implementation in fluoropyrimidine-treated patients) to reduce risk of severe fluoropyrimidine toxicity |
| Handling Protection | Standard cytotoxic drug handling and disposal precautions required per institutional/regulatory hazardous drug protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clinical and literature evidence for tegafur-based regimens in colonic neoplasm is strong (L1: six completed Phase 3 RCTs, including the ACTS-CC 02 and NSABP C-06 trials), and mechanistically consistent with the drug's already-supported role in gastric cancer. However, TFDA/NPRA label safety data (warnings, contraindications) is a **Blocking** data gap (DG001) that must be resolved before this candidate can pass the S1 safety pre-assessment.

**To proceed, the following is needed:**
- Retrieve and parse the NPRA package insert to close the Blocking safety data gap (DG001) — warnings, contraindications, and dosing precautions
- Obtain DrugBank/mechanism-of-action data to strengthen the mechanistic rationale (DG002)
- Re-query NPRA license records to populate registration number, product name, dosage form, and approved indication text for the 3 existing Malaysia registrations
- Confirm DPD/DPYD deficiency screening protocol as part of the safety monitoring plan, given known severe-toxicity risk in DPD-deficient patients
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

