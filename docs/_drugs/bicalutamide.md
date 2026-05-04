---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal antiandrogen originally approved for the treatment of prostate cancer.
The TxGNN model predicts it may be effective for **Hypertrichosis (disease)**, with **1 publication** currently referencing this direction. Notably, a secondary prediction for **Female Breast Carcinoma** (Rank #9) is supported by **1 Phase 2 clinical trial** and **20 publications**, representing the strongest evidence among all 10 predicted indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (antiandrogen therapy) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bicalutamide is a non-steroidal antiandrogen that competitively blocks the androgen receptor (AR). Originally developed for the treatment of advanced prostate cancer, it works by preventing testosterone and dihydrotestosterone (DHT) from binding to the AR, thereby inhibiting androgen-mediated signaling in target tissues including the prostate, skin, and hair follicles.

Hypertrichosis — excessive hair growth beyond what is expected for a person's age, sex, and ethnicity — can be driven or exacerbated by androgen signaling at the hair follicle level. Drug-induced hypertrichosis (e.g., from minoxidil) and androgen-excess states both involve stimulation of hair follicle growth cycles. Since bicalutamide directly blocks AR signaling in peripheral tissues including hair follicles, it has a direct and plausible mechanism for reducing androgen-driven excessive hair growth.

In clinical dermatology practice, antiandrogens (including bicalutamide) have been used off-label for androgen-related hair conditions such as hirsutism and androgenetic alopecia, providing real-world precedent for this prediction. The existing literature specifically documents bicalutamide improving minoxidil-induced hypertrichosis in female pattern hair loss patients, supporting the mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypertrichosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter/Comment | Journal of the American Academy of Dermatology | Comments on a retrospective review of 35 patients showing bicalutamide improved minoxidil-induced hypertrichosis in female pattern hair loss |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Registration 1) | — | — | License details pending data collection |
| (Registration 2) | — | — | License details pending data collection |
| (Registration 3) | — | — | License details pending data collection |

> Bicalutamide is confirmed as marketed in Malaysia with 3 active registrations. Detailed license information is pending retrieval from the NPRA database.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Non-steroidal antiandrogen) |
| Myelosuppression Risk | Low — bicalutamide is not a conventional cytotoxic agent and does not typically cause significant myelosuppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT, AST, bilirubin) — hepatotoxicity is the primary concern; CBC at baseline; PSA in prostate cancer context |
| Handling Protection | Standard handling; no special cytotoxic drug handling precautions required as this is a hormonal agent |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications data were not available in this evidence pack (Data Gap DG001, severity: Blocking). Obtaining the package insert from NPRA is required before proceeding to safety evaluation.

---

## All Predicted Indications Summary

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------|-------------|----------------|--------|-------------|----------------|
| 1 | Hypertrichosis (disease) | 99.69% | L4 | 0 | 1 | Proceed with Guardrails |
| 2 | Malformation syndrome (odontal/periodontal) | 99.59% | L5 | 0 | 20* | Hold |
| 3 | Ambras type hypertrichosis universalis congenita | 99.57% | L5 | 0 | 0 | Research Question |
| 4 | Dandy-Walker malformation syndrome | 99.57% | L5 | 0 | 0 | Hold |
| 5 | Isolated genetic hair shaft abnormality | 99.53% | L5 | 0 | 0 | Hold |
| 6 | Leprosy | 99.41% | L5 | 0 | 0 | Hold |
| 7 | Multiple endocrine neoplasia | 99.22% | L4 | 2 | 0 | Research Question |
| 8 | Pulmonary hypertension | 99.18% | L5 | 0 | 1 | Hold |
| **9** | **Female breast carcinoma** | **99.11%** | **L2** | **1** | **20** | **Proceed with Guardrails** |
| 10 | Nephrogenic syndrome of inappropriate antidiuresis | 99.03% | L5 | 0 | 0 | Hold |

\* *Rank #2 literature consists entirely of general periodontology papers with no mention of bicalutamide or antiandrogen therapy — mechanistic mismatch.*

---

## Spotlight: Female Breast Carcinoma (Rank #9, Strongest Evidence)

Although ranked 9th by TxGNN prediction score (99.11%), **female breast carcinoma** carries the strongest clinical evidence (Level L2) among all 10 predicted indications and merits special attention.

### Mechanistic Rationale

The androgen receptor (AR) is expressed in approximately 70–90% of all breast cancers. Within triple-negative breast cancer (TNBC), the **luminal androgen receptor (LAR) subtype** (~30% of TNBC) is driven by AR signaling. Bicalutamide blocks AR, thereby inhibiting AR-positive breast cancer cell proliferation. Preclinical studies further demonstrate that bicalutamide may suppress β-catenin transcriptional activity and, in combination with ERK inhibitors, induce ferroptosis in TNBC cells. The mechanistic link is strong and well-supported by multiple lines of pharmacological evidence.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, not recruiting | 30 | Evaluates bicalutamide combined with nivolumab and ipilimumab in metastatic HER2-negative breast cancer. Combines AR blockade with immune checkpoint therapy to improve efficacy while omitting/delaying chemotherapy. |

### Literature Evidence (Top 10)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | Comprehensive review of anti-androgen therapy for TNBC; highlights bicalutamide, enzalutamide, and enobosarm as key AR antagonists with combination strategies |
| [21633166](https://pubmed.ncbi.nlm.nih.gov/21633166/) | 2011 | Translational | J Clin Invest | Landmark study identifying 6 TNBC subtypes including LAR subtype; established the molecular basis for AR-targeted therapy in TNBC |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Mechanistic | Sci China Life Sci | AR/ERK co-targeting with bicalutamide + GDC-0994 triggers ferroptosis via FOXC2 in TNBC; demonstrates synergistic antitumour effect |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | Reviews AR role in breast cancer; discusses AR–ERα crosstalk and rationale for AR-targeted therapy |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treat Rev | Reviews AR as therapeutic target in TNBC LAR subtype; discusses clinical trial landscape |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | In vitro | Medicine | Bicalutamide inhibits proliferation and invasion of MDA-MB-231 TNBC cells via AR pathway blockade |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | Preclinical | Anti-cancer Drugs | Bicalutamide + curcumin combination shows strong therapeutic effect on AR-positive TNBC |
| [29069648](https://pubmed.ncbi.nlm.nih.gov/29069648/) | 2017 | Mechanistic | Cell Physiol Biochem | Bicalutamide antagonizes AR and inhibits β-catenin transcription complex in ER-negative breast cancer |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clin Breast Cancer | Reviews apocrine carcinoma (ER−/AR+) molecular characteristics; supports AR-targeted therapy approach |
| [24888812](https://pubmed.ncbi.nlm.nih.gov/24888812/) | 2016 | Case Report | J Clin Oncol | Complete response of metastatic AR-positive breast cancer to bicalutamide monotherapy |

---

## Conclusion and Next Steps

### Primary Prediction: Hypertrichosis

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between bicalutamide's AR antagonism and hypertrichosis management is direct and pharmacologically sound. Off-label use in dermatology has been documented, and a retrospective review of 35 patients supports efficacy in minoxidil-induced hypertrichosis. However, clinical trial evidence is absent.

**To proceed, the following is needed:**
- Retrieve package insert safety data from NPRA (Blocking data gap DG001)
- Obtain detailed mechanism of action data from DrugBank (Data gap DG002)
- Conduct systematic literature search specifically for bicalutamide in hirsutism/hypertrichosis
- Evaluate dose–response data for dermatological (non-oncological) use
- Design a prospective observational study or pilot trial

### High-Priority Secondary Prediction: Female Breast Carcinoma

**Decision: Proceed with Guardrails**

**Rationale:**
This is the most evidence-rich prediction with Level L2 evidence: an active Phase 2 clinical trial (NCT03650894) directly evaluating bicalutamide in HER2-negative metastatic breast cancer, 20 publications spanning reviews, mechanistic studies, preclinical data, and a published case report of complete response. The LAR subtype of TNBC provides a well-characterized molecular target for bicalutamide.

**To proceed, the following is needed:**
- Monitor NCT03650894 results (expected completion December 2026)
- Retrieve package insert safety data from NPRA (Blocking data gap DG001)
- Evaluate AR expression testing availability in Malaysia
- Assess feasibility of AR-based patient selection for breast cancer treatment
- Review regulatory pathway for indication expansion in Malaysia

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

