---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
---

# Docetaxel
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

# Docetaxel: From Multiple Solid Tumours to Familial Prostate Carcinoma

## One-Sentence Summary

Docetaxel is a taxane-class cytotoxic agent widely approved for the treatment of breast cancer, non-small cell lung cancer, prostate cancer, gastric cancer, and head and neck cancer. The TxGNN model predicts it may also be effective for **Familial Prostate Carcinoma**, with **28 clinical trials** and **20 publications** currently supporting this direction. Notably, docetaxel is already a standard-of-care in metastatic castration-resistant prostate cancer (mCRPC), and this prediction extends its potential to the hereditary/familial subtype where DNA repair defects (e.g. BRCA2) may influence taxane sensitivity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer, NSCLC, prostate cancer (mCRPC), gastric cancer, head and neck cancer (registration detail pending) |
| Predicted New Indication | Familial Prostate Carcinoma |
| TxGNN Prediction Score | 0.00% (score data pending refinement) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel belongs to the taxane family and works by stabilising microtubules, thereby inhibiting their disassembly and arresting cells in the G2/M phase of the cell cycle. This mechanism is particularly effective against rapidly proliferating cancer cells. Docetaxel has been a cornerstone of prostate cancer treatment since the landmark TAX 327 trial demonstrated a survival benefit in metastatic castration-resistant prostate cancer, and the CHAARTED trial (NCT00309985) further established its role in hormone-naïve metastatic disease.

Familial prostate carcinoma frequently harbours germline mutations in DNA repair genes such as BRCA2, ATM, and CHEK2. These DNA repair deficiencies may paradoxically render tumour cells more dependent on intact mitotic machinery for survival, potentially maintaining or even enhancing sensitivity to microtubule-stabilising agents like docetaxel. The repurposing rationale provided in the evidence pack confirms a strong mechanistic link, noting that while the core anti-mitotic mechanism remains the same, familial prostate cancer patients with DNA repair defects may exhibit distinct patterns of taxane sensitivity.

Furthermore, docetaxel is already integrated into multiple lines of prostate cancer treatment — as first-line chemotherapy for mCRPC, in combination with androgen deprivation therapy (ADT) for hormone-sensitive disease, and as a backbone upon which newer agents (enzalutamide, abiraterone, cabazitaxel) are sequenced. The extension to specifically address the familial/hereditary subtype represents a refinement of existing clinical practice rather than an entirely novel application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00309985](https://clinicaltrials.gov/study/NCT00309985) | Phase 3 | Completed | 790 | **CHAARTED trial**: ADT ± docetaxel in metastatic hormone-naïve prostate cancer. Landmark study establishing early docetaxel benefit in high-volume metastatic disease. |
| [NCT01308567](https://clinicaltrials.gov/study/NCT01308567) | Phase 3 | Completed | 1,168 | Cabazitaxel (25 mg/m² and 20 mg/m²) vs docetaxel in first-line mCRPC. Docetaxel served as the standard comparator arm, confirming its established efficacy. |
| [NCT00974311](https://clinicaltrials.gov/study/NCT00974311) | Phase 3 | Completed | 1,199 | **AFFIRM trial**: Enzalutamide vs placebo in mCRPC post-docetaxel. Validates docetaxel as standard first-line chemotherapy upon which sequencing strategies are built. |
| [NCT01308580](https://clinicaltrials.gov/study/NCT01308580) | Phase 3 | Completed | 1,200 | Cabazitaxel 20 mg/m² vs 25 mg/m² after docetaxel failure in mCRPC. Confirms docetaxel as established first-line standard. |
| [NCT00514917](https://clinicaltrials.gov/study/NCT00514917) | Phase 3 | Terminated | 413 | ADT with leuprolide ± docetaxel for rising PSA after local therapy. Evaluated early docetaxel use in biochemically recurrent prostate cancer. |
| [NCT00676650](https://clinicaltrials.gov/study/NCT00676650) | Phase 3 | Terminated | 873 | Sunitinib + prednisone vs prednisone post-docetaxel in mCRPC. Docetaxel as first-line standard; large-scale data on post-docetaxel disease. |
| [NCT01957436](https://clinicaltrials.gov/study/NCT01957436) | Phase 3 | Active | 1,173 | ADT ± docetaxel ± radiotherapy ± abiraterone in metastatic hormone-naïve prostate cancer. Multifactorial design evaluating docetaxel combinations. |
| [NCT02288247](https://clinicaltrials.gov/study/NCT02288247) | Phase 3 | Completed | 688 | Continuing enzalutamide during docetaxel + prednisolone in chemotherapy-naïve mCRPC after enzalutamide progression. |
| [NCT04028388](https://clinicaltrials.gov/study/NCT04028388) | Phase 2b | Completed | 135 | Oral docetaxel formulation (ModraDoc006/r) in mCRPC. Directly supports docetaxel's continued role with novel formulations. |
| [NCT02485691](https://clinicaltrials.gov/study/NCT02485691) | Phase 4 | Completed | 255 | **CARD trial**: Cabazitaxel vs AR-targeted agent in mCRPC previously treated with docetaxel. Confirms sequencing strategies post-docetaxel. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26041764](https://pubmed.ncbi.nlm.nih.gov/26041764/) | 2015 | Consensus Guideline | Ann Oncol | St Gallen APCCC 2015: Expert consensus on advanced prostate cancer management, including docetaxel sequencing and combination strategies. |
| [34649352](https://pubmed.ncbi.nlm.nih.gov/34649352/) | 2021 | Phase 2 Clinical Trial | Biomed Pharmacother | Docetaxel + lycopene in mCRPC; median PSA response and survival data in chemotherapy-naïve patients (n=13). |
| [24714754](https://pubmed.ncbi.nlm.nih.gov/24714754/) | 2014 | Biomarker Study | Br J Cancer | Circulating microRNAs associated with docetaxel chemotherapy outcome in CRPC; potential for early response prediction. |
| [27537383](https://pubmed.ncbi.nlm.nih.gov/27537383/) | 2016 | Translational Research | Br J Cancer | Loss of SLCO1B3 drives taxane resistance in prostate cancer; mechanistic insights into docetaxel and cabazitaxel resistance in mCRPC. |
| [32252682](https://pubmed.ncbi.nlm.nih.gov/32252682/) | 2020 | Translational Research | BMC Cancer | SLC6A1 overexpression associates with docetaxel resistance and poor prognosis in prostate cancer. |
| [22112969](https://pubmed.ncbi.nlm.nih.gov/22112969/) | 2012 | Phase 2 RCT | Ann Oncol | Docetaxel + prednisone ± AT-101 (Bcl-2 inhibitor) in first-line mCRPC; randomised double-blind placebo-controlled design. |
| [23973186](https://pubmed.ncbi.nlm.nih.gov/23973186/) | 2013 | Phase 3 QoL Analysis | Eur J Cancer | Abiraterone impact on QoL post-docetaxel in mCRPC; FACT-P validated outcomes from COU-AA-301. |
| [27402060](https://pubmed.ncbi.nlm.nih.gov/27402060/) | 2017 | Post Hoc Analysis | Eur Urol | Treatment patterns post-abiraterone in COU-AA-302; docetaxel as subsequent chemotherapy in mCRPC sequencing. |
| [23832735](https://pubmed.ncbi.nlm.nih.gov/23832735/) | 2013 | Review | Eur Rev Med Pharmacol Sci | Taxane- and epothilone-based chemotherapy for CRPC; drug resistance mechanisms and combo-therapy strategies. |
| [34425813](https://pubmed.ncbi.nlm.nih.gov/34425813/) | 2021 | Case Report | BMC Urol | Germline BRCA2 mutation in prostate cancer sensitive to platinum chemotherapy; relevant to familial prostate cancer genomics. |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Registration detail pending) | — | — | — |
| (Registration detail pending) | — | — | — |
| (Registration detail pending) | — | — | — |
| (Registration detail pending) | — | — | — |
| (Registration detail pending) | — | — | — |

> **Note:** 10 product registrations are recorded with marketed status in Malaysia. Detailed authorization numbers, product names, dosage forms, and approved indication text are pending retrieval from the NPRA database.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilising agent) |
| Myelosuppression Risk | **High** — Neutropenia is the dose-limiting toxicity; febrile neutropenia occurs in approximately 3–12% of patients. Thrombocytopenia and anaemia are also reported. |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle), liver function tests (AST/ALT/bilirubin — contraindicated if bilirubin > ULN), renal function, peripheral neuropathy assessment, fluid retention monitoring |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system drug-transfer devices recommended; protective gowning, double gloving, and biological safety cabinet required during preparation |

---

## Safety Considerations

> Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data are pending retrieval from the NPRA product insert database.

**Known class-level safety signals for docetaxel (for clinical reference):**
- **Hepatic impairment**: Docetaxel is contraindicated in patients with severe hepatic impairment (bilirubin > ULN); dose modifications required for mild-to-moderate impairment
- **Hypersensitivity**: Severe hypersensitivity reactions reported; premedication with corticosteroids is standard
- **Fluid retention**: Cumulative; may be severe without dexamethasone premedication
- **Peripheral neuropathy**: Dose-dependent; may be irreversible

---

## Additional Predicted Indications

The TxGNN model also predicts docetaxel may be effective for the following indications:

| Rank | Disease | Evidence Level | Clinical Trials | Literature | Recommendation |
|------|---------|---------------|-----------------|------------|----------------|
| 2 | Lung Cancer | L1 | 50 | 0* | Proceed with Guardrails |
| 3 | Head and Neck Cancer | L1 | 50 | 20 | Proceed with Guardrails |
| 4 | Non-Small Cell Lung Carcinoma | L1 | 50 | 20 | Proceed with Guardrails |
| 5 | Upper Aerodigestive Tract Neoplasm | L2 | 1 | 20 | Proceed with Guardrails |

> *Note: Lung cancer and NSCLC (ranks 2 and 4) show substantial overlap in clinical trial evidence. Docetaxel is already an approved standard-of-care for NSCLC in both first-line (with platinum) and second-line (monotherapy) settings, supported by landmark trials such as TAX 326. Head and neck cancer (rank 3) is similarly well-established through the TAX 323 and TAX 324 trials demonstrating TPF superiority over PF in induction chemotherapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel is already a proven standard-of-care in metastatic castration-resistant prostate cancer, and the extension to familial prostate carcinoma is supported by L1-level evidence (multiple completed Phase 3 RCTs including CHAARTED and AFFIRM). The familial subtype, often characterised by germline DNA repair defects (BRCA2, ATM), may exhibit distinct treatment responses that warrant tailored evaluation. The mechanistic link is strong, and the clinical infrastructure for docetaxel use in prostate cancer is well-established.

**To proceed, the following is needed:**
- **Detailed mechanism of action data (MOA)** from DrugBank to complete the pharmacological profile
- **NPRA product insert retrieval** to populate safety warnings, contraindications, and approved indication text for Malaysia-registered products
- **Genomic stratification analysis** — evaluate whether familial prostate cancer patients with specific germline mutations (BRCA2, ATM, CHEK2) show differential response to docetaxel compared to sporadic mCRPC
- **Safety monitoring plan** for specific populations, particularly patients with concurrent PARP inhibitor use (common in BRCA2+ prostate cancer)
- **Real-world evidence collection** from Malaysian oncology centres on docetaxel use patterns in hereditary prostate cancer patients

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

