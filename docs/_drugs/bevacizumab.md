---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 5
---

# Bevacizumab
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

# Bevacizumab: From Multiple Solid Tumours to Peritoneum Cancer

## One-Sentence Summary

Bevacizumab (Avastin®) is a recombinant humanised monoclonal antibody targeting VEGF-A, approved globally for multiple solid tumours including metastatic colorectal cancer, non-small cell lung cancer, glioblastoma, and ovarian cancer.
The TxGNN model predicts it may be effective for **Peritoneum Cancer**,
with **50 clinical trials** and **20 publications** currently supporting this direction — many of which are completed Phase III landmark trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple solid tumours (colorectal, NSCLC, glioblastoma, ovarian, cervical, renal cell carcinoma) |
| Predicted New Indication | Peritoneum Cancer |
| TxGNN Prediction Score | Not available (score = 0.0, likely data gap) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bevacizumab is a humanised monoclonal antibody that binds and neutralises vascular endothelial growth factor A (VEGF-A), the key mediator of tumour angiogenesis. By blocking VEGF-A from binding to its receptors (VEGFR-1 and VEGFR-2), bevacizumab inhibits new blood vessel formation, normalises existing tumour vasculature to improve chemotherapy delivery, and reduces vascular permeability — the latter being particularly relevant to malignant ascites control in peritoneal cancers.

Peritoneum cancer (both primary peritoneal carcinoma and peritoneal metastases from various origins) is highly dependent on VEGF-driven angiogenesis and ascites formation. The peritoneal microenvironment is rich in VEGF, which promotes tumour dissemination across peritoneal surfaces and the accumulation of malignant ascites. This makes VEGF-targeted therapy a mechanistically sound approach. Indeed, primary peritoneal carcinoma shares near-identical molecular features with high-grade serous ovarian cancer — both arising from Müllerian epithelium — and has been consistently included as an eligible population in the pivotal bevacizumab ovarian cancer trials (GOG-0218, ICON7, AURELIA, OCEANS).

The extensive overlap between bevacizumab's approved ovarian cancer indication and peritoneum cancer means that much of the clinical evidence base already validates this repurposing prediction. Multiple completed Phase III RCTs with thousands of enrolled patients have demonstrated progression-free survival benefits for bevacizumab-containing regimens in populations that include primary peritoneal cancer, providing an unusually strong evidence foundation for this drug repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00262847](https://clinicaltrials.gov/study/NCT00262847) | Phase 3 | Completed | 1,873 | **GOG-0218**: Carboplatin/Paclitaxel ± Bevacizumab in newly diagnosed Stage III/IV ovarian/peritoneal cancer. Bevacizumab throughout + maintenance significantly improved PFS. Landmark trial leading to regulatory approval. |
| [NCT00483782](https://clinicaltrials.gov/study/NCT00483782) | Phase 3 | Completed | 1,520 | **ICON7**: Adding bevacizumab to standard chemotherapy in epithelial ovarian/peritoneal cancer. Demonstrated PFS improvement, with greatest benefit in high-risk subgroup. |
| [NCT00976911](https://clinicaltrials.gov/study/NCT00976911) | Phase 3 | Completed | 361 | **AURELIA**: Bevacizumab + chemotherapy vs chemotherapy alone in platinum-resistant ovarian/fallopian tube/peritoneal cancer. Significant PFS benefit (6.7 vs 3.4 months). |
| [NCT03038100](https://clinicaltrials.gov/study/NCT03038100) | Phase 3 | Completed | 1,301 | **IMagyn050**: Atezolizumab vs placebo + Paclitaxel/Carboplatin/Bevacizumab in newly diagnosed Stage III/IV ovarian/peritoneal cancer. Bevacizumab used in all arms as backbone therapy. |
| [NCT02659384](https://clinicaltrials.gov/study/NCT02659384) | Phase 2 | Completed | 122 | Atezolizumab + Bevacizumab ± Aspirin in platinum-resistant ovarian/peritoneal cancer. Evaluated PFS at 6 months across 5 treatment arms to select optimal combinations. |
| [NCT04670978](https://clinicaltrials.gov/study/NCT04670978) | Phase 2 | Unknown | 96 | Abraxane + Bevacizumab biosimilar in platinum-resistant recurrent ovarian/peritoneal cancer. Directly evaluates bevacizumab efficacy in refractory setting. |
| [NCT02873962](https://clinicaltrials.gov/study/NCT02873962) | Phase 2 | Active | 73 | Nivolumab + Bevacizumab ± Rucaparib in relapsed ovarian/peritoneal cancer. Explores immuno-oncology + anti-angiogenic combinations. |
| [NCT01097746](https://clinicaltrials.gov/study/NCT01097746) | Phase 2 | Completed | 33 | Bevacizumab + Carboplatin + weekly Paclitaxel as first-line treatment in ovarian/peritoneal/fallopian tube cancer. |
| [NCT05445778](https://clinicaltrials.gov/study/NCT05445778) | Phase 3 | Recruiting | 520 | **GLORIOSA**: Mirvetuximab Soravtansine + Bevacizumab vs Bevacizumab alone as maintenance in platinum-sensitive recurrent ovarian/peritoneal cancer. |
| [NCT06824467](https://clinicaltrials.gov/study/NCT06824467) | Phase 3 | Recruiting | 770 | **TroFuse-022**: Sacituzumab Tirumotecan ± Bevacizumab vs standard of care after second-line platinum-based chemotherapy in platinum-sensitive recurrent ovarian cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30905627](https://pubmed.ncbi.nlm.nih.gov/30905627/) | 2019 | Clinical Guideline | Eur J Obstet Gynecol Reprod Biol | French clinical practice guidelines (FRANCOGYN/CNGOF) for management of epithelial ovarian/peritoneal cancer, including bevacizumab-based regimens. |
| [24476788](https://pubmed.ncbi.nlm.nih.gov/24476788/) | 2014 | Phase II Trial | Gynecol Oncol | Oxaliplatin + Docetaxel + Bevacizumab as first-line therapy for advanced ovarian/peritoneal cancer. Demonstrated safety and efficacy of the novel combination. |
| [40690248](https://pubmed.ncbi.nlm.nih.gov/40690248/) | 2025 | Review | JAMA | Comprehensive review of ovarian cancer including peritoneal involvement. Bevacizumab identified as standard component of first-line and recurrent treatment regimens. |
| [39168966](https://pubmed.ncbi.nlm.nih.gov/39168966/) | 2024 | Translational Research | Nat Commun | Gut microbiota as biomarker for response to Atezolizumab + Bevacizumab in mesothelioma (including peritoneal). Novel predictive approach for anti-VEGF therapy. |
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Retrospective/Cohort | Future Oncol | Bevacizumab efficacy in low-grade serous ovarian cancer: ORR 54.1%, median PFS 15 months. Supports activity across histological subtypes. |
| [38644553](https://pubmed.ncbi.nlm.nih.gov/38644553/) | 2024 | Narrative Review | Ann Palliat Med | Review of malignant ascites management. Bevacizumab discussed as key intervention for VEGF-driven ascites in peritoneal carcinomatosis. |
| [30936025](https://pubmed.ncbi.nlm.nih.gov/30936025/) | 2019 | Clinical Guideline | J Gynecol Obstet Hum Reprod | French guidelines Part 2: systemic/IP treatment for ovarian/peritoneal cancer. Recommends bevacizumab in first-line and recurrent settings. |
| [38238055](https://pubmed.ncbi.nlm.nih.gov/38238055/) | 2024 | Protocol | BMJ Open | INTERACT-II: IP irinotecan + FOLFOX + Bevacizumab for unresectable colorectal peritoneal metastases. Explores bevacizumab in peritoneal-specific setting. |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Review of malignant peritoneal mesothelioma. Discusses anti-angiogenic strategies including bevacizumab in peritoneal malignancies. |
| [28139261](https://pubmed.ncbi.nlm.nih.gov/28139261/) | 2017 | Retrospective | Gynecol Oncol | Bevacizumab-containing regimens in recurrent low-grade serous ovarian/peritoneal cancer. Demonstrated clinical activity in this difficult-to-treat subtype. |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |

> **Note:** 9 product registrations are recorded in the Malaysia market with "Marketed" status, but detailed authorization numbers, product names, dosage forms, and approved indication texts were not available in the data source at the time of this report. Further verification with NPRA records is recommended.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Anti-VEGF humanised monoclonal antibody) |
| Myelosuppression Risk | Low as monotherapy; moderate when combined with myelosuppressive chemotherapy (neutropenia, thrombocytopenia reported in combination regimens) |
| Emetogenicity Classification | Low (minimal emetogenic potential as monotherapy) |
| Monitoring Items | Blood pressure (every 2–3 weeks), urinalysis for proteinuria, CBC with differential, hepatic and renal function, wound healing assessment pre-/post-surgery |
| Handling Protection | Standard biologic handling procedures; does not require conventional cytotoxic drug handling precautions as it is a monoclonal antibody, not a genotoxic agent |

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug–drug interaction data were not available in the current evidence pack.

**Known class-effect concerns for bevacizumab (from published literature) include:**
- **Hypertension** — dose-related, requires active monitoring and antihypertensive management
- **Proteinuria** — monitor urine protein; discontinue for nephrotic syndrome
- **Gastrointestinal perforation** — risk increased in patients with peritoneal carcinomatosis
- **Wound healing complications** — withhold bevacizumab ≥28 days before elective surgery
- **Thromboembolic events** — arterial events (stroke, MI) and venous thromboembolism
- **Haemorrhage** — including CNS and pulmonary haemorrhage in at-risk populations

---

## Additional Predicted Indications Summary

| Rank | Disease | Evidence Level | Recommendation | Key Rationale |
|------|---------|---------------|----------------|---------------|
| 1 | Peritoneum Cancer | L1 | Proceed with Guardrails | Multiple completed Phase 3 RCTs; mechanistically aligned |
| 2 | Hereditary Breast Ovarian Cancer Syndrome | L4 | Hold | No direct clinical trials; bevacizumab does not target BRCA pathway |
| 3 | Malignant Epithelial Tumour of Ovary | L1 | Proceed with Guardrails | GOG-0218, ICON7 landmark trials; already approved indication in many jurisdictions |
| 4 | Primary Peritoneal Carcinoma | L1 | Proceed with Guardrails | Included in pivotal ovarian cancer trials; identical molecular profile |
| 5 | Breast Neoplasm | L1 | Proceed with Guardrails | E2100 showed PFS benefit; however, FDA revoked breast cancer indication due to lack of OS benefit — proceed with caution |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bevacizumab has an exceptionally strong evidence base for peritoneum cancer, with multiple completed Phase III RCTs (GOG-0218, ICON7, AURELIA) enrolling >3,700 patients collectively and demonstrating significant progression-free survival benefits. Primary peritoneal carcinoma is already an accepted eligible population in bevacizumab's ovarian cancer labelling in many jurisdictions. The mechanistic rationale — VEGF-driven angiogenesis and malignant ascites in the peritoneal microenvironment — is well-established and clinically validated.

**To proceed, the following is needed:**
- Obtain detailed Malaysia NPRA registration information (authorization numbers, approved indications) to confirm local regulatory status
- Retrieve complete package insert safety data (warnings, contraindications, drug interactions) to enable formal safety assessment (currently a blocking data gap — DG001)
- Obtain detailed mechanism of action data from DrugBank to strengthen the mechanistic rationale documentation (DG002)
- Confirm whether "peritoneum cancer" as a standalone indication is covered under existing ovarian cancer approval, or whether a separate indication pathway is required
- Develop a safety monitoring plan addressing GI perforation risk (elevated in peritoneal disease), hypertension, and proteinuria
- Establish clear patient selection criteria and clinical governance framework for any off-label use

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All data current as of 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

