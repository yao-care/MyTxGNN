---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: From Gastric Cancer to Gastric Carcinoma

## One-Sentence Summary

> Gimeracil is a DPD-inhibitor component of the S-1 combination (tegafur + gimeracil + oteracil potassium), whose established use is in gastric cancer chemotherapy. The TxGNN model's top-ranked prediction, **Gastric Carcinoma**, essentially reconfirms this known indication rather than identifying a novel one — it is supported by **50 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs. A more genuinely novel signal appears at rank 2, **Colonic Neoplasm** (8 trials, 15 publications), reflecting S-1's established off-label/regional use in colorectal cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the current registry extract; gimeracil is a known component of the S-1 combination used for gastric cancer (see Clinical Trial Evidence) |
| Predicted New Indication | Gastric Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gimeracil is part of the S-1 combination (tegafur + gimeracil + oteracil potassium), a well-established oral fluoropyrimidine antineoplastic regimen. Gimeracil functions as a dihydropyrimidine dehydrogenase (DPD) inhibitor: it blocks the enzyme that degrades 5-fluorouracil (5-FU), the active metabolite of tegafur, thereby prolonging and enhancing 5-FU's antitumor activity while reducing gastrointestinal toxicity relative to continuous-infusion 5-FU.

Because gimeracil is not administered alone but only as part of the S-1 combination, its clinical evidence base is inseparable from S-1's own indication profile — which is predominantly gastric cancer, with substantial secondary use in colorectal cancer. The top-ranked TxGNN prediction, "Gastric Carcinoma," therefore largely reconfirms the drug's already-established therapeutic role rather than surfacing a new hypothesis. This is a common and expected outcome for knowledge-graph models applied to drugs whose components are tightly bound to a single approved combination product.

The more interpretively interesting signal is rank 2, "Colonic Neoplasm," where S-1-based regimens (SOX: S-1 + oxaliplatin) have substantial Phase 3 evidence in adjuvant and metastatic colorectal cancer settings (e.g., NCT03448549, NCT00660894), mechanistically consistent with gastric cancer given the shared fluoropyrimidine sensitivity of GI adenocarcinomas.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01516944](https://clinicaltrials.gov/study/NCT01516944) | Phase 2/3 | Completed | 749 | Perioperative Tegafur-Gimeracil-Oteracil + oxaliplatin superior to surgery alone; non-inferior to capecitabine + oxaliplatin in localized advanced gastric cancer |
| [NCT00216034](https://clinicaltrials.gov/study/NCT00216034) | Phase 3 | Completed | 255 | Postoperative adjuvant TS-1 alone vs. TS-1+PSK for Stage II/IIIA gastric cancer |
| [NCT00182611](https://clinicaltrials.gov/study/NCT00182611) | Phase 3 | Completed | 100 | Preoperative S-1/cisplatin combination chemotherapy in resectable Stage III gastric cancer |
| [NCT03013010](https://clinicaltrials.gov/study/NCT03013010) | Phase 3 | Completed | 204 | PREACT study: preoperative radiochemotherapy vs. chemotherapy alone in locally advanced gastric/EGJ adenocarcinoma |
| [NCT03941561](https://clinicaltrials.gov/study/NCT03941561) | Phase 3 | Recruiting | 1006 | S-1 for 9 months vs. 1 year as adjuvant chemotherapy after D2 resection in Stage II gastric cancer |
| [NCT04997837](https://clinicaltrials.gov/study/NCT04997837) | Phase 3 | Recruiting | 433 | Adjuvant chemotherapy ± PD-1 inhibitors and chemoradiotherapy for D2/R0-resected pN3 gastric/GEJ adenocarcinoma |
| [NCT07023315](https://clinicaltrials.gov/study/NCT07023315) | Phase 3 | Recruiting | 760 | Cadonilimab + SOX vs. placebo + SOX as perioperative treatment for resectable gastric/GEJ adenocarcinoma |
| [NCT02527785](https://clinicaltrials.gov/study/NCT02527785) | Phase 2 | Completed | 44 | Triple combination of S-1 + oxaliplatin + irinotecan as first-line therapy for advanced gastric cancer |
| [NCT01845337](https://clinicaltrials.gov/study/NCT01845337) | Phase 2 | Completed | 59 | Comparative cardiotoxicity study of capecitabine vs. Teysuno (S-1) |
| [NCT02564367](https://clinicaltrials.gov/study/NCT02564367) | Phase 1/2 | Completed | 30 | Feasibility and tolerability of adjuvant S-1 in Caucasian patients after R0 resection of gastric/EGJ adenocarcinoma |

*(50 trials matched in total; the above 10 are the most directly relevant completed/large-scale studies.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38906161](https://pubmed.ncbi.nlm.nih.gov/38906161/) | 2024 | RCT (Phase 3) | Lancet Gastroenterol Hepatol | ATTRACTION-5: adjuvant nivolumab + chemotherapy vs. placebo + chemotherapy for Stage III gastric/GEJ cancer post-D2 gastrectomy |
| [36160880](https://pubmed.ncbi.nlm.nih.gov/36160880/) | 2022 | Comparative study | Exp Ther Med | Neoadjuvant apatinib + SOX (S-1+oxaliplatin) vs. SOX alone in locally advanced gastric carcinoma |
| [38719675](https://pubmed.ncbi.nlm.nih.gov/38719675/) | 2025 | Retrospective analysis | J Formos Med Assoc | Long-term follow-up of adjuvant chemotherapy outcomes in Stage II/III gastric adenocarcinoma |
| [15224197](https://pubmed.ncbi.nlm.nih.gov/15224197/) | 2004 | Feasibility study | Gastric Cancer | Feasibility of S-1 (TS-1) as postoperative adjuvant chemotherapy after curative gastric cancer resection |
| [27966431](https://pubmed.ncbi.nlm.nih.gov/27966431/) | 2017 | Retrospective (toxicity) | Hong Kong Med J | Tolerability and risk factors for adjuvant S-1 toxicity in Chinese gastric cancer patients |
| [39004983](https://pubmed.ncbi.nlm.nih.gov/39004983/) | 2024 | Retrospective case series | Zhonghua Wei Chang Wai Ke Za Zhi | Efficacy/safety of preoperative PD-1 inhibitor + CapeOx or SOX in immunotherapy-sensitive locally advanced gastric/EGJ cancer |
| [31061042](https://pubmed.ncbi.nlm.nih.gov/31061042/) | 2019 | Phase 1 protocol | BMJ Open | Intraperitoneal paclitaxel + IV cisplatin + oral S-1 (tegafur/gimeracil/oteracil) for gastric cancer with peritoneal metastases |
| [19621385](https://pubmed.ncbi.nlm.nih.gov/19621385/) | 2010 | Preclinical | Int J Cancer | S-1 (5-FU analog) combined with FGFR2 inhibitor shows synergistic antitumor effect in scirrhous gastric carcinoma models |
| [11525030](https://pubmed.ncbi.nlm.nih.gov/11525030/) | 2001 | Case report | Gan To Kagaku Ryoho | Postoperative chemotherapy with tegafur/gimeracil/oteracil in curability-C scirrhous gastric cancer |
| [24918280](https://pubmed.ncbi.nlm.nih.gov/24918280/) | 2014 | Case report | Klin Onkol | Advanced disseminated gastric carcinoma treated with S-1 |

*(20 publications matched in total; the above 10 prioritize RCT/comparative/retrospective evidence over isolated case reports.)*

---

## Malaysia Market Information

The evidence pack confirms **2 active NPRA registrations** and a **"Marketed" status** for Gimeracil-containing products, but the underlying extract does not include the individual authorization numbers, product names, dosage forms, or approved-indication text for these registrations. This detail should be pulled directly from NPRA's product registry as a follow-up step before any regulatory-facing use of this report.

---

## Cytotoxicity

Gimeracil is not administered as a standalone agent; it is a biomodulator component of the S-1 combination (tegafur + gimeracil + oteracil potassium), a conventional cytotoxic fluoropyrimidine chemotherapy regimen.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class, via DPD-inhibition potentiation of 5-FU) |
| Myelosuppression Risk | Moderate — literature reports Grade 3–4 hematological toxicity in ~16% of patients on S-1 + irinotecan regimens for colonic cancer (PMID 21084813); neutropenia and thrombocytopenia are the principal concerns |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; triglycerides have also been reported to rise with S-1 (PMID 32936722) |
| Handling Protection | Must follow standard cytotoxic drug handling regulations for antineoplastic combination products |

---

## Safety Considerations

Please refer to the package insert for safety information. The current evidence pack has no usable data for key warnings, contraindications, or drug–drug interactions (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for the gastric carcinoma indication is strong (L1: ≥2 completed Phase 3 RCTs plus a 2024 Phase 3 RCT in the adjuvant setting), but this indication substantially overlaps with gimeracil's already-established role within S-1, so it is not a genuinely novel repurposing signal.
- A **Blocking** data gap (TFDA/NPRA label warnings and contraindications, DG001) prevents this candidate from entering the S1 safety review stage at all, regardless of efficacy strength.

**To proceed, the following is needed:**
- Official product label (warnings, contraindications) from the Malaysia NPRA registry for the 2 registered Gimeracil products (DG001, Blocking)
- DrugBank-sourced mechanism of action detail for gimeracil specifically, distinct from the S-1 combination (DG002, High)
- Complete license metadata (authorization numbers, product names, dosage forms, indication text) for the 2 NPRA registrations
- If pursuing the colonic neoplasm signal (rank 2) as the more genuinely novel candidate, a dedicated evaluation of S-1/SOX regimens in colorectal cancer is recommended as a separate candidate assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

