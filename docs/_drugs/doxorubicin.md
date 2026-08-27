---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Broad-Spectrum Anthracycline Chemotherapy to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is a classic anthracycline antineoplastic agent used across a wide range of hematologic and solid tumors. The TxGNN model predicts it may be effective for **Ewing Sarcoma**, and this is already strongly reflected in real-world practice — with **48 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications** supporting doxorubicin-containing regimens as part of the standard of care for this tumor.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the NPRA license records on file; doxorubicin is a well-established anthracycline antineoplastic used across breast cancer, lymphomas, leukemias, and soft tissue/bone sarcomas |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% (rank 2126) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not returned for this candidate (data gap DG002). Based on well-established pharmacology, doxorubicin is an anthracycline that intercalates into DNA and inhibits topoisomerase II, blocking DNA replication and transcription in rapidly dividing cells — a broad-spectrum cytotoxic mechanism applicable across many tumor histologies.

This mechanism is directly relevant to Ewing sarcoma, an aggressive, rapidly proliferating small round-cell tumor of bone and soft tissue. Doxorubicin is not a novel candidate for this disease in the research sense — it is already a **core component of the standard VDC/IE regimen** (vincristine, doxorubicin, cyclophosphamide, alternating with ifosfamide/etoposide) used worldwide in both localized and metastatic Ewing sarcoma.

The TxGNN prediction therefore reflects an already-validated clinical reality rather than a speculative repurposing hypothesis: decades of Phase 2/3 trial data (COG, EURO-E.W.I.N.G., EICESS) consistently use doxorubicin-based backbones as either the experimental or control arm, confirming both mechanistic plausibility and clinical utility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | RCT testing addition of vincristine-topotecan-cyclophosphamide to standard 5-drug regimen (incl. doxorubicin) for non-metastatic Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | RCT adding IGF-1R antibody ganitumab to standard doxorubicin-containing chemotherapy backbone for metastatic Ewing sarcoma |
| [NCT01696669](https://clinicaltrials.gov/study/NCT01696669) | Phase 2 | Completed | 43 | Prospective study of intensive chemotherapy (doxorubicin-based), surgery and radiotherapy in children/young adults with Ewing sarcoma |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Doxorubicin-containing combination chemotherapy for newly diagnosed metastatic Ewing sarcoma/PNET |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | RCT of chemotherapy intensification via interval compression combined with radiotherapy/surgery |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | RCT of standard vs. dose-intensified treatment in non-metastatic Ewing sarcoma |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, not recruiting | 437 | Compares vincristine-irinotecan-regorafenib add-on to standard VDC/IE (doxorubicin-based) in newly diagnosed metastatic Ewing sarcoma |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Completed | N/A | Randomized study of vincristine, doxorubicin, cyclophosphamide, dexrazoxane ± ImmTher in high-risk Ewing sarcoma |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy, radiotherapy and cyclophosphamide/anti-COX2 consolidation for metastatic Ewing sarcoma |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99 — large international trial of combination chemotherapy ± radiotherapy/surgery ± stem cell transplant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | NEJM | Landmark trial showing addition of ifosfamide/etoposide to standard (doxorubicin-based) chemotherapy improves survival in newly diagnosed Ewing sarcoma |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012 trial comparing two international standard chemotherapy regimens for newly diagnosed Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT (protocol) | Trials | EURO EWING 2012 protocol comparing induction/consolidation regimens for Ewing sarcoma family of tumours |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | COG AEWS1221 — addition of ganitumab to interval-compressed chemotherapy in newly diagnosed metastatic Ewing sarcoma |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT | J Clin Oncol | High-dose treosulfan/melphalan consolidation vs. standard therapy in high-risk metastatic Ewing sarcoma |
| [31553693](https://pubmed.ncbi.nlm.nih.gov/31553693/) | 2019 | RCT | J Clin Oncol | High-dose chemotherapy vs. standard chemotherapy + lung irradiation in Ewing sarcoma with pulmonary metastases |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncology | Overview of Ewing sarcoma treatment progress, noting multiagent chemotherapy has raised survival from ~10% to ~75% in localized disease |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review/Guideline | Cancer | National Ewing Sarcoma Tumor Board consensus recommendations on standard-of-care management |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management and future directions in Ewing sarcoma multidisciplinary therapy |
| [25993235](https://pubmed.ncbi.nlm.nih.gov/25993235/) | 2015 | Review | ASCO Educational Book | Systemic therapy overview for osteosarcoma and Ewing sarcoma, including anthracycline-based regimens |

---

## Malaysia Market Information

NPRA records confirm doxorubicin is marketed in Malaysia with **8 active registrations**, but license-level details (registration numbers, product names, dosage forms, manufacturers, approved indication text) were not returned in this data pull and require a direct NPRA lookup to complete.

---

## Cytotoxicity

Doxorubicin is a conventional cytotoxic chemotherapy agent (anthracycline class), meeting the antineoplastic classification criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Anthracycline class; DNA intercalator / topoisomerase II inhibitor) |
| Myelosuppression Risk | High — anthracyclines are well known to cause dose-limiting neutropenia and thrombocytopenia |
| Emetogenicity Classification | High (standard IV doxorubicin doses used in sarcoma/leukemia regimens are classified as highly emetogenic) |
| Monitoring Items | CBC with differential, LVEF/echocardiogram or MUGA (cumulative-dose cardiotoxicity), liver and renal function |
| Handling Protection | Yes — requires handling under cytotoxic/hazardous drug precautions (closed-system transfer devices, PPE, spill protocols) |

Supporting evidence: cumulative-dose cardiotoxicity (congestive heart failure) is documented in a large retrospective analysis ([PMID 12767102](https://pubmed.ncbi.nlm.nih.gov/12767102/)), reinforcing the need for cardiac monitoring alongside hematologic monitoring.

---

## Safety Considerations

TFDA/NPRA-sourced key warnings, contraindications, and drug–drug interaction data were not available in this evidence pull (data gap DG001, flagged **Blocking** — this must be resolved before a formal S1 safety assessment can be completed). Please refer to the package insert for official safety information in the interim.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxorubicin-containing regimens are already extensively validated as standard-of-care backbone therapy for Ewing sarcoma across multiple completed and ongoing Phase 3 RCTs (L1 evidence), making this less a novel repurposing hypothesis than a confirmation of established clinical practice. However, the missing TFDA/NPRA label safety data (warnings, contraindications, DDI) is a **blocking** gap that must be closed before this can move past a preliminary safety screen.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking)
- DrugBank-confirmed mechanism of action data (DG002)
- Malaysia-specific license details (registration numbers, dosage forms, approved indication text per product)
- Confirmation of local reimbursement/formulary status for Ewing sarcoma use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

