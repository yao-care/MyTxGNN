---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (Adcetris) is an anti-CD30 antibody-drug conjugate (ADC) originally approved for the treatment of relapsed/refractory Hodgkin lymphoma and systemic anaplastic large cell lymphoma (sALCL). The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **6 clinical trials** and **20 publications** currently supporting this direction. However, the key prerequisite is CD30 expression screening, as CD30 is expressed in only approximately 15–40% of follicular lymphoma cases.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, systemic anaplastic large cell lymphoma (sALCL) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Brentuximab vedotin is an antibody-drug conjugate consisting of the anti-CD30 monoclonal antibody brentuximab linked to the microtubule-disrupting agent monomethyl auristatin E (MMAE). Upon binding to CD30 on the cell surface, the ADC is internalized and MMAE is released intracellularly, leading to cell cycle arrest and apoptosis. This mechanism has proven highly effective in CD30-expressing malignancies such as classical Hodgkin lymphoma and systemic ALCL.

Follicular lymphoma (FL) is an indolent B-cell non-Hodgkin lymphoma that exhibits heterogeneous CD30 expression—approximately 15–40% of cases show CD30 positivity, with expression levels that can increase upon histological transformation (e.g., to diffuse large B-cell lymphoma or ALCL). Both the original indications and follicular lymphoma share the common feature of being lymphoid neoplasms where CD30 can serve as a therapeutic target, providing a mechanistic rationale for brentuximab vedotin's potential activity in a biomarker-selected FL subpopulation.

Critically, this is not a pan-FL strategy. The prediction's validity is contingent on CD30 expression screening, and the evidence to date supports exploration specifically in CD30-positive FL subsets. One active Phase 2 trial (NCT04587687) is directly investigating BV plus bendamustine in relapsed/refractory FL, though results are pending.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + bendamustine in R/R follicular lymphoma; the only currently active FL-specific trial. Results pending. |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized study of rituximab + bendamustine ± BV in R/R CD30+ DLBCL. Terminated (n=25); termination reason may relate to efficacy or safety concerns. |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline therapy for CD30+/EBV+ lymphomas (including FL). Terminated (n=20); not FL-specific. |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Rituximab + BV + bendamustine (RBvB) risk-stratified study in newly diagnosed PTLD. Withdrawn before enrollment. |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | BV + bendamustine + rituximab in CD30+ R/R B-cell NHL. Withdrawn before enrollment. |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | BV + pembrolizumab in recurrent PTCL. Not FL-specific; withdrawn. |

> **Note:** Of 6 identified trials, only 1 (NCT04587687) is actively recruiting and directly targets follicular lymphoma. Three trials were withdrawn before enrollment, and two were terminated with small sample sizes. This trial landscape suggests early-stage exploration with no completed FL-specific efficacy data yet available.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf J Oncol | Grade I FL transformation to ALCL CD30+ ALK1−, with complete response to BV and high-dose methotrexate. Demonstrates BV efficacy in a FL-derived CD30+ transformed lymphoma. |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leuk Res Rep | Review of immunotherapy in indolent NHL including FL. Discusses monoclonal antibody therapies and emerging immunotherapeutic approaches. |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | ASH Educ Program | "BV and beyond": discusses incorporation of novel agents including BV into PTCL management; contextualizes CD30-targeting strategies across lymphoma subtypes. |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Current and upcoming treatment approaches for common PTCL subtypes; discusses BV-CHP (A+CHP) regimen as a new standard in CD30+ PTCL. |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Phase 2 Report | Blood Adv | LYSA Phase 2 study of BV + gemcitabine in R/R PTCL with CD30+ cells ≥5%. ORR data provides cross-indication CD30 targeting evidence. |
| [22045523](https://pubmed.ncbi.nlm.nih.gov/22045523/) | 2011 | Review | Ther Umsch | Overview of monoclonal antibodies in haematologic neoplasms; discusses rituximab maintenance in FL and the emerging role of CD30-targeted agents. |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplant | Post-ASCT maintenance therapies in lymphoma; discusses BV maintenance after transplant in HL and notes consideration for other lymphoma subtypes including FL. |
| [38028985](https://pubmed.ncbi.nlm.nih.gov/38028985/) | 2023 | Case Report | Case Rep Hematol | Composite lymphoma with FL transformation to EBV+ DLBCL and EBV+ cHL, highlighting the potential for CD30 expression in FL-transformed disease. |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Retrospective | Adv Ther | Real-world study of BV + CHP in untreated CD30+ NHL including TFH-PTCL and ALCL; provides safety and efficacy data relevant to CD30-targeting ADCs. |
| [41409526](https://pubmed.ncbi.nlm.nih.gov/41409526/) | 2025 | Case Report | Skin Appendage Disord | Extensive alopecia mucinosa (folliculotropic MF variant) responding to BV; demonstrates BV activity in CD30+ follicular-pattern lymphoproliferative disorders. |

> **Note:** Direct FL-specific literature is limited. Most publications address BV in PTCL or HL contexts. The most directly relevant evidence is a case report (PMID 32476657) demonstrating BV efficacy in FL-transformed ALCL, rather than in primary FL.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *(Registration number not available in data)* | Brentuximab Vedotin | *(Not specified)* | *(Approved indication text not available; drug is registered and marketed)* |

> Brentuximab vedotin holds 1 registration in Malaysia with market status confirmed as marketed. Detailed registration information (product name, dosage form, approved indication text) was not available in the data source at the time of query.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate (ADC) with conventional cytotoxic payload (MMAE, an auristatin-class microtubule inhibitor) |
| Myelosuppression Risk | **High** — Neutropenia is among the most common grade 3/4 adverse events; thrombocytopenia and anaemia also reported. Febrile neutropenia may occur. |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each dose), liver function tests (hepatotoxicity including fatal cases reported), renal function, peripheral neuropathy assessment, tumour lysis syndrome screening in high tumour burden patients |
| Handling Protection | Must follow cytotoxic drug handling regulations; appropriate personal protective equipment required during preparation and administration |

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Important note:** Key warnings, contraindications, and drug interaction data were not available in the current evidence pack (data gap identified as blocking severity). Known class-level safety signals for brentuximab vedotin from published literature include:
> - **Peripheral neuropathy** (cumulative, dose-limiting; sensory > motor)
> - **Progressive multifocal leukoencephalopathy (PML)** — rare but fatal; boxed warning
> - **Infusion-related reactions**
> - **Severe hepatotoxicity** including fatal hepatic failure
> - **Stevens-Johnson syndrome / Toxic epidermal necrolysis**
> - **Pulmonary toxicity**
>
> Formal safety assessment requires package insert review and local regulatory data.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score is very high (99.89%), and the mechanistic rationale is sound for the CD30-positive subpopulation of follicular lymphoma. One active Phase 2 trial (NCT04587687) is directly investigating BV in R/R FL, supporting active clinical interest. However, CD30 expression in FL is heterogeneous (15–40%), and no completed FL-specific efficacy data is yet available. The majority of literature evidence is cross-indication rather than FL-specific, and several related trials were terminated or withdrawn, warranting caution.

**To proceed, the following is needed:**
- **CD30 expression profiling data** in the target FL population to define the eligible patient subgroup
- **Results from NCT04587687** (BV + bendamustine in R/R FL) — expected completion December 2026
- **Detailed mechanism of action (MOA) data** from DrugBank (currently a data gap)
- **Package insert safety data** — key warnings and contraindications (currently a blocking data gap preventing formal S1 safety assessment)
- **Biomarker selection strategy** — define CD30 positivity threshold (e.g., ≥1% vs ≥10% by IHC) for patient selection
- **Comparison with standard of care** — assess incremental benefit vs. existing FL therapies (e.g., rituximab-bendamustine, lenalidomide-rituximab, PI3K inhibitors)

---

## Appendix: Additional Predicted Indications Summary

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Consideration |
|------|---------------------|-------------|---------------|----------------|-------------------|
| 1 | Follicular Lymphoma | 99.89% | L2 | Proceed with Guardrails | CD30 expression in 15–40% of FL; 1 active Phase 2 trial |
| 2 | Myeloid Leukemia | 99.76% | L2 | Proceed with Guardrails | CD30 expressed in ~10–20% AML; completed Phase 1 (PMID 31860140) and Phase 2 (NCT01461538) |
| 3 | Acute Lymphoblastic Leukemia | 99.65% | L4 | Hold | CD30 expression <5% in ALL; no BV-specific trials; weak mechanistic basis |
| 4 | B-cell Neoplasm | 99.60% | L2 | Proceed with Guardrails | Broad category; strong evidence in DLBCL and PMBL subtypes with CD30 expression |
| 5 | Pre-GC CLL/SLL | 99.46% | L5 | Hold | CD30 expression <5% in CLL; no clinical or literature evidence |
| 6 | CLL/SLL with IGHV Mutation | 99.46% | L5 | Hold | Same as above; IGHV status unrelated to CD30 |
| 7 | Richter Syndrome | 99.38% | L4 | Research Question | HL-type Richter (~15–20%) expresses CD30; 3 case reports support exploration |
| 8 | Mantle Cell Lymphoma | 99.32% | L3 | Research Question | CD30 expression ~10–30% (weak); 1 terminated trial; limited evidence |
| 9 | Ganglioneuroblastoma | 99.23% | L5 | Hold | Neural crest tumour; CD30 not expressed; likely false positive |
| 10 | Vertebral Anomalies / T-cell Dysfunction | 99.16% | L5 | Hold | Congenital/genetic syndrome; not a neoplasm; BV completely inapplicable |

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

