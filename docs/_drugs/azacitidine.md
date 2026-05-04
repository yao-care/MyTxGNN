---
layout: default
title: Azacitidine
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 5
---

# Azacitidine
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

# Azacitidine: From Myelodysplastic Syndrome to Therapy-Related AML/MDS

## One-Sentence Summary

Azacitidine is a DNA methyltransferase (DNMT) inhibitor originally approved for the treatment of myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML).
The TxGNN model predicts it may be effective for **Therapy-Related Acute Myeloid Leukemia and Myelodysplastic Syndrome (t-AML/t-MDS)**,
with **50 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelodysplastic syndrome (MDS), Acute myeloid leukemia (AML) |
| Predicted New Indication | Therapy-related acute myeloid leukemia and myelodysplastic syndrome |
| TxGNN Prediction Score | 0.00% (Rank 1) |
| Evidence Level | L1 (≥2 completed Phase 2/3 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Therapy-related AML/MDS (t-AML/t-MDS) arises as a complication of prior cytotoxic therapy, with core pathogenic mechanisms including aberrant DNA methylation and clonal selection. The affected bone marrow cells exhibit widespread epigenetic dysregulation—particularly hypermethylation of tumour suppressor gene promoters such as *CDKN2B* and genes in the *TP53* pathway—which silences their normal growth-restraining functions. These patients frequently harbour genomic instability from prior chemotherapy exposure, making them poor candidates for intensive reinduction.

Azacitidine, as a DNMT inhibitor, directly reverses these aberrant methylation patterns by incorporating into DNA during replication and forming covalent bonds with DNA methyltransferases, leading to their degradation. This restores expression of silenced tumour suppressor genes, promotes leukemic cell differentiation, and induces apoptosis. The drug's relatively low-intensity profile makes it particularly suitable for t-AML/t-MDS patients, who are often older and carry comorbidities from prior cancer treatments.

The mechanistic rationale is further strengthened by the emergence of **venetoclax + azacitidine** as a standard-of-care combination for this patient population. Multiple completed Phase 3 trials (e.g., NCT03416179, n=730; NCT03268954, n=454) directly evaluated azacitidine-based regimens in AML/MDS populations that include therapy-related subtypes. A dedicated Phase 2 trial (NCT05379166) is specifically evaluating venetoclax + azacitidine in therapy-related MDS, providing highly targeted evidence for this prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03416179](https://clinicaltrials.gov/study/NCT03416179) | Phase 3 | Completed | 730 | Randomized, double-blind, placebo-controlled trial of glasdegib ± azacitidine in previously untreated AML. Largest registration-level trial directly evaluating azacitidine-based therapy in t-AML/MDS population. |
| [NCT03268954](https://clinicaltrials.gov/study/NCT03268954) | Phase 3 | Completed | 454 | Pevonedistat + azacitidine vs azacitidine alone as first-line treatment for higher-risk MDS, CMML, or low-blast AML. Azacitidine served as control arm standard, providing efficacy baseline. |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | Completed | 68 | Evaluated azacitidine added to reduced-intensity conditioning allogeneic transplantation for MDS and older AML patients. Provides direct evidence for azacitidine in the transplant setting. |
| [NCT05379166](https://clinicaltrials.gov/study/NCT05379166) | Phase 2 | Active, not recruiting | 33 | Directly evaluates venetoclax + azacitidine in therapy-related MDS (t-MDS). The most disease-specific trial for this prediction. |
| [NCT02719574](https://clinicaltrials.gov/study/NCT02719574) | Phase 1/2 | Completed | 336 | Olutasidenib ± azacitidine in IDH1-mutated AML/MDS. Large-scale trial with azacitidine combination arm; demonstrates azacitidine's role in targeted therapy combinations. |
| [NCT02921061](https://clinicaltrials.gov/study/NCT02921061) | Phase 1/2 | Completed | 28 | Decitabine + G-CLAM in newly diagnosed AML/high-risk MDS. Validated hypomethylating agent-based combination feasibility and safety in this population. |
| [NCT01928537](https://clinicaltrials.gov/study/NCT01928537) | Phase 3B | Completed | 67 | Rigosertib in MDS patients progressing on/after azacitidine or decitabine. Azacitidine established as prior standard treatment baseline. |
| [NCT02750254](https://clinicaltrials.gov/study/NCT02750254) | Phase 1 | Terminated | 5 | Directly tested azacitidine in haploidentical donor transplantation. Terminated early but provides initial safety data for this approach. |
| [NCT06129734](https://clinicaltrials.gov/study/NCT06129734) | Phase 1B/2A | Recruiting | 20 | Weekly decitabine + venetoclax maintenance in high-risk myeloid malignancy post-transplant. Represents next-generation HMA combination strategies. |
| [NCT03146871](https://clinicaltrials.gov/study/NCT03146871) | Phase 2 | Terminated | 7 | sEphB4-HSA + HMA (including azacitidine) in relapsed/refractory MDS/AML. Directly tested azacitidine in combination therapy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40155601](https://pubmed.ncbi.nlm.nih.gov/40155601/) | 2025 | Prospective Cohort | Blood Cancer J | Venetoclax + azacitidine in untreated t-AML patients with antecedent MDS or CMML. Most directly relevant evidence for the predicted indication. |
| [38135371](https://pubmed.ncbi.nlm.nih.gov/38135371/) | 2024 | RCT (Phase 3) | Lancet Haematol | ASCERTAIN trial: oral decitabine-cedazuridine vs IV decitabine for MDS/CMML. Demonstrates equivalent PK exposure for oral HMA formulations. |
| [36370742](https://pubmed.ncbi.nlm.nih.gov/36370742/) | 2023 | Phase 1/2 Trial | Lancet Haematol | Olutasidenib ± azacitidine in IDH1-mutated AML/MDS. Demonstrated safety and clinical activity of azacitidine combinations. |
| [38452788](https://pubmed.ncbi.nlm.nih.gov/38452788/) | 2024 | Phase 2 Trial | Lancet Haematol | Oral decitabine-cedazuridine + venetoclax for older/unfit AML patients. Effective HMA-based regimen supporting the class mechanism. |
| [31990086](https://pubmed.ncbi.nlm.nih.gov/31990086/) | 2020 | Translational Research | Eur J Haematol | Clonal selection in t-MDS/AML under azacitidine treatment. Directly examines azacitidine's biological effects in therapy-related disease. |
| [40737597](https://pubmed.ncbi.nlm.nih.gov/40737597/) | 2025 | Translational | Blood | XPO1 drives resistance to eprenetapopt + azacitidine in TP53-mutated MDS/AML. Identifies resistance mechanism relevant to t-AML treatment. |
| [40259101](https://pubmed.ncbi.nlm.nih.gov/40259101/) | 2025 | Retrospective | Leukemia | Impact of MDS-related gene mutations on venetoclax/azacitidine outcomes in AML. Identifies molecular predictors of response. |
| [38052038](https://pubmed.ncbi.nlm.nih.gov/38052038/) | 2024 | Phase 1b Trial | Blood Adv | Tagraxofusp + azacitidine ± venetoclax in AML. Demonstrated azacitidine re-sensitization of resistant cells. |
| [37470508](https://pubmed.ncbi.nlm.nih.gov/37470508/) | 2023 | Review | Expert Rev Anticancer Ther | Comprehensive review of oral therapies for MDS/AML. Positions azacitidine + venetoclax as backbone therapy with evolving oral formulations. |
| [36964818](https://pubmed.ncbi.nlm.nih.gov/36964818/) | 2023 | Systematic Review / Meta-analysis | Clin Exp Med | Efficacy of epigenetic agents for older AML/MDS patients in RCTs. Network meta-analysis supporting azacitidine-based regimens. |

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details pending) | — | — | — |

> **Note:** Azacitidine is confirmed as marketed in Malaysia with **12 registered products**. Detailed registration information (authorization numbers, product names, dosage forms, approved indications) was not available in the current data extraction. Please refer to the NPRA database for complete license details.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Nucleoside analog / Hypomethylating agent) |
| Myelosuppression Risk | **High** — Neutropenia, thrombocytopenia, and anemia are among the most common dose-limiting toxicities. Grade 3/4 cytopenias occur frequently. |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle and as needed), liver function tests (LFTs), renal function (serum creatinine, BUN), electrolytes, serum bicarbonate |
| Handling Protection | Must follow cytotoxic drug handling regulations; azacitidine is classified as a hazardous drug requiring appropriate protective equipment during preparation and administration |

## Safety Considerations

> Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not available in the current evidence pack (data gap identified as blocking severity — DG001). Package insert PDF review is recommended before proceeding to safety evaluation.

## Additional Predicted Indications

The TxGNN model identified **4 additional indications** beyond the primary prediction. A summary is provided below:

| Rank | Predicted Indication | Evidence Level | Clinical Trials | Publications | Recommendation |
|------|---------------------|---------------|----------------|-------------|---------------|
| 2 | Acute myeloblastic leukemia with maturation (FAB M2) | L1 | 42 | 20 | Proceed with Guardrails |
| 3 | AML/MDS related to topoisomerase type 2 inhibitor | L5 | 0 | 0 | Research Question |
| 4 | Myelomonocytic leukemia (CMML/JMML) | L1 | 50 | 20 | Proceed with Guardrails |
| 5 | AML with minimal differentiation (FAB M0) | L1 | 8 | 5 | Proceed with Guardrails |

**Key observations:**
- **Rank 2 (AML with maturation)** and **Rank 4 (Myelomonocytic leukemia)** are strongly supported, with azacitidine already included in treatment guidelines (ELN/NCCN) for CMML, and FDA approval of ivosidenib + azacitidine for IDH1-mutated newly diagnosed AML.
- **Rank 3 (Topoisomerase II inhibitor-related AML/MDS)** has zero clinical trial or literature evidence, representing a pure model prediction. The mechanistic rationale is plausible but requires dedicated investigation.
- **Rank 5 (AML with minimal differentiation)** is a poor-prognosis subtype where the undifferentiated phenotype may limit azacitidine's differentiation-inducing effects; caution is warranted.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azacitidine is already a well-established treatment for AML and MDS, and the TxGNN prediction for therapy-related AML/MDS aligns closely with existing clinical evidence. Multiple completed Phase 2/3 clinical trials (NCT03416179, n=730; NCT03268954, n=454) and a dedicated t-MDS trial (NCT05379166) directly support azacitidine-based regimens in this population. The venetoclax + azacitidine combination has emerged as a standard-of-care approach for patients ineligible for intensive chemotherapy, including those with therapy-related disease.

**To proceed, the following is needed:**
- **Detailed mechanism of action (MOA) data** — current evidence pack has a data gap; retrieve from DrugBank API
- **NPRA package insert review** — obtain warnings, contraindications, and drug interaction data (blocking severity data gap DG001)
- **Malaysia-specific registration details** — populate license numbers, product names, and approved indication text from the NPRA database
- **Safety monitoring plan** — develop specific monitoring protocols for myelosuppression (the primary dose-limiting toxicity), particularly in the t-AML/t-MDS population who may have compromised bone marrow reserve from prior cytotoxic therapy
- **Subtype-specific analysis for Rank 3 indication** — topoisomerase II inhibitor-related AML/MDS has zero evidence and requires dedicated preclinical or translational study before further evaluation

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions generated by the TxGNN model should be interpreted in conjunction with clinical judgement and regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

