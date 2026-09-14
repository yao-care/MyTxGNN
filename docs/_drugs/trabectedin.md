---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 659
evidence_level: L5
indication_count: 1
---

# Trabectedin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trabectedin: From Soft Tissue Sarcoma/Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Trabectedin is a marine-derived antitumor agent originally used for soft tissue sarcoma and, in combination with pegylated liposomal doxorubicin (PLD), for platinum-sensitive relapsed ovarian cancer. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **2 clinical trials** and **20 publications** — including a randomized Phase 2 trial — currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma; platinum-sensitive relapsed ovarian cancer (in combination with PLD) — per published literature; Malaysia label indication text not currently available in source data |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on information extracted from the supporting literature, trabectedin is a tetrahydroisoquinoline alkaloid derived from the marine tunicate *Ecteinascidia turbinata*. It binds the DNA minor groove, interferes with DNA-repair and transcription-regulating proteins, and also acts as a modulator of the tumor microenvironment by depleting tumor-associated macrophages (TAMs).

Its established efficacy in soft tissue sarcoma and ovarian cancer stems largely from tumors with defects in homologous recombination repair (e.g., BRCA1/2 mutations) and transcriptionally active tumor biology. Breast cancer — particularly BRCA1/2-mutated and triple-negative subtypes — shares these same DNA-repair-deficiency and transcriptional-dependency features, which is the mechanistic basis for the TxGNN prediction. Multiple Phase 1/2 trials and mechanistic studies in the evidence pack directly test trabectedin in breast cancer, including BRCA1/2-mutated metastatic disease, reinforcing that this is not a purely computational extrapolation but one with existing clinical precedent.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance after response to trabectedin-PLD in recurrent ovarian carcinoma (BRCA-mutation relevant biology, adjacent to breast cancer indication) |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-dose trabectedin QT/QTc interval safety study in advanced solid tumor malignancies |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | RCT | Clinical Breast Cancer | Multicenter randomized Phase 2 study comparing two trabectedin administration regimens in advanced breast cancer after anthracycline/taxane treatment |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 trial | Clinical Breast Cancer | Trabectedin efficacy in HR-positive, HER2-negative advanced breast carcinoma stratified by XPG gene expression |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 trial | Annals of Oncology | International first-in-class Phase 2 study of trabectedin in germline BRCA1/2-mutated metastatic breast cancer |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 trial | European Journal of Cancer | Phase 1 clinical/PK study of trabectedin plus doxorubicin in advanced soft tissue sarcoma and breast cancer |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opinion on Investigational Drugs | Overview of trabectedin's mechanism (transcription inhibition, TAM reduction) and potential in breast cancer |
| [18410797](https://pubmed.ncbi.nlm.nih.gov/18410797/) | 2008 | Review | Seminars in Oncology | Emerging agents, including trabectedin, for anthracycline/taxane-refractory metastatic breast cancer |
| [38366738](https://pubmed.ncbi.nlm.nih.gov/38366738/) | 2024 | Case report | The Journal of Dermatology | Trabectedin effective in radiation-induced angiosarcoma of the breast refractory to prior anticancer drugs |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunology Research | Trabectedin depletes MDSCs and enhances IL-12-induced NK-cell cytotoxicity in triple-negative breast cancer |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicology Letters | Trabectedin induces apoptosis via distinct pathways in MCF-7 (HER2-/ER+) and MDA-MB-453 (HER2+/ER-) breast cancer cells |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | European Cytokine Network | Anti-angiogenic effects of trabectedin on human breast cancer cell lines and endothelial cells |

## Malaysia Market Information

NPRA records show the product as **Marketed** with 1 registered license. However, the authorization number, product name, dosage form, and approved indication text fields are not currently populated in the source data — this should be verified directly against the NPRA registry before use in decision-making.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA minor-groove-binding tetrahydroisoquinoline alkylating agent; interferes with transcription-coupled DNA repair) |
| Myelosuppression Risk | High — literature reports Grade 3-4 neutropenia in ~50% and thrombocytopenia in ~20% of patients |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential, liver function tests (transaminase elevation is common), renal function, creatine kinase (rhabdomyolysis reported), cardiac monitoring (QT interval) |
| Handling Protection | Yes — requires cytotoxic/hazardous drug handling precautions per standard chemotherapy handling protocols |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The efficacy evidence (L2 — a completed randomized Phase 2 trial plus supporting Phase 1/2 studies and mechanistic literature) reasonably supports the breast cancer hypothesis, but the Blocking-severity gap in TFDA/NPRA label warnings and contraindications means this candidate cannot yet pass safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/NPRA label PDF with warnings, precautions, and contraindications (DG001, Blocking)
- Confirmed mechanism of action from DrugBank API (DG002, High)
- Complete NPRA license registry details (authorization number, product name, dosage form, approved indication text)
- Formal DDI query results (currently "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

