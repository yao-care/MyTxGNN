---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral multi-target kinase inhibitor (BCR-ABL, SRC family, KIT, PDGFR) established for chronic myeloid leukemia and Ph+ ALL. The TxGNN model's top-ranked prediction is that it may be effective for **Ewing Sarcoma**, supported by **3 clinical trials** and **9 publications**, though direct human efficacy data specific to this indication remain limited.

> Note: The evidence pack's official Taiwan/TFDA license fields (approved indication text, brand names, license numbers) are empty, and the formal DrugBank MOA record is a flagged data gap (DG002). Where noted below, background on dasatinib's established mechanism/indication draws on well-established public knowledge rather than this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Myeloid Leukemia (CML) / Ph+ ALL — TFDA-specific approved indication text not provided in this dataset (see DG001) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank mechanism-of-action record is not available for this drug (data gap DG002). Based on known information, dasatinib is a second-generation multi-kinase inhibitor targeting BCR-ABL and SRC-family kinases (as well as KIT and PDGFR), and its efficacy in CML/Ph+ ALL is well established.

Ewing sarcoma cells are highly dependent on SRC-family kinase (SRC/FAK) signaling to drive invadopodia formation, migration, and invasion. Multiple in vitro studies in this evidence pack show that dasatinib, as a potent SRC inhibitor, suppresses proliferation and migratory/invasive capacity in Ewing sarcoma cell lines (PMID 17363602, 18202781, 27566104, 31521948). This gives the prediction a coherent mechanistic basis.

However, the clinical evidence remains preliminary: the only completed trial directly relevant to this population (NCT00464620) was a broad "advanced sarcomas" Phase 2 study without an Ewing-sarcoma-specific efficacy readout in this dataset, and a targeted pediatric combination trial (dasatinib + ifosfamide/carboplatin/etoposide, NCT00788125) was terminated with only 7 patients enrolled — a signal that warrants caution rather than confidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib in advanced sarcomas (response rate, 6-month PFS); most direct efficacy evidence to date, includes an Ewing sarcoma cohort, but no indication-specific results summary is included in this dataset. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib + ifosfamide/carboplatin/etoposide in pediatric solid tumors; terminated with very small enrollment (N=7), possibly reflecting accrual difficulty or an early negative signal. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy trial in relapsed/refractory pediatric solid tumors (including Ewing sarcoma); dasatinib, if used, likely serves only as a kinase-based CAR-T safety switch, not as an anti-Ewing-sarcoma therapy itself — low direct relevance. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Reviews SRC signaling's role in sarcoma biology and its feasibility as a drug target. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review/Mechanistic | Sarcoma | Discusses FAK-SRC complex targeting in DSRCT, Ewing sarcoma and rhabdomyosarcoma; notes dasatinib failed as a single agent in a prior Phase 2 study for these subtypes, motivating combination approaches. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review (chondrosarcoma-focused; low direct relevance) | Curr Treat Options Oncol | Systemic therapy review for chondrosarcoma, not Ewing-sarcoma-specific. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical (in vitro) | Cancer Research | Dasatinib inhibits migration/invasion across sarcoma cell lines and induces apoptosis in SRC-dependent bone sarcoma cells. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical (in vitro) | Oncology Reports | Dasatinib shows antiproliferative and antimigratory activity in neuroblastoma and Ewing sarcoma cell lines via c-KIT/PDGFR inhibition. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical (in vitro) | Neoplasia | Microenvironmental stress activates SRC-dependent invadopodia and cell migration in Ewing sarcoma. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical (in vitro) | Neoplasia | Tenascin C and SRC cooperate to promote invadopodia formation and metastatic potential in Ewing sarcoma. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical (in vitro; not dasatinib-focused) | Cell Commun Signal | CXCR4 antagonist plerixafor activates receptor tyrosine kinase signaling in Ewing sarcoma — supportive context, not direct dasatinib evidence. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Case report (CML blast crisis — appears unrelated to Ewing sarcoma) | Case Rep Oncol | Chromosomal abnormality in CML blast crisis; likely a classification mismatch in this evidence pack, not relevant to the Ewing sarcoma indication. |

---

## Malaysia Market Information

Market status indicates the drug is marketed with **2 registered licenses**, but license-level detail (authorization number, product name, dosage form, approved indication text) is not populated in this dataset — this is the blocking data gap DG001 (TFDA label/warning data), which needs to be resolved via the TFDA product label before regulatory or safety review can proceed.

---

## Cytotoxicity

Dasatinib is an antineoplastic agent (originally indicated for CML/Ph+ ALL; a multi-kinase inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: BCR-ABL, SRC family, KIT, PDGFR) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (formal toxicity data is a blocking gap, DG001); class-level TKI experience and the literature in this pack (e.g., pleural effusion/chylothorax, interstitial pneumonitis reports) indicate hematologic and fluid-retention adverse effects are clinically significant and should be monitored |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function; given literature signals in this pack, also monitor for pleural/pericardial effusion and pulmonary symptoms |
| Handling Protection | Please refer to the package insert warnings and precautions; follow standard cytotoxic/targeted oncology drug handling protocols pending confirmation |

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are available in this evidence pack — DG001 is a blocking gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Mechanistic and in vitro evidence plausibly links dasatinib's SRC-pathway inhibition to Ewing sarcoma biology, but indication-specific clinical evidence is weak — the relevant completed trial pooled multiple sarcoma types without an Ewing-specific result, and the one targeted pediatric combination trial was terminated at N=7. Combined with the blocking safety/label data gap (DG001), this candidate is not yet ready to advance past the research-question stage.

**To proceed, the following is needed:**
- TFDA product label — key warnings and contraindications (DG001, blocking)
- DrugBank mechanism-of-action record (DG002)
- Ewing-sarcoma-specific subgroup results from NCT00464620
- Complete TFDA license details (authorization numbers, dosage forms, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

