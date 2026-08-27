---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: From Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a third-generation aromatase inhibitor originally used to treat hormone receptor-positive (HR+) breast cancer in postmenopausal women. The TxGNN model's top prediction points back to **Female Breast Carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction — however, this largely reconfirms letrozole's existing, well-established indication rather than identifying a genuinely novel repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormone receptor-positive (HR+) breast cancer in postmenopausal women *(NPRA license indication text was not captured in this data pull — see Data Gap DG001)* |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action (MOA) data was not returned by the DrugBank query for this candidate (Data Gap DG002). However, across the clinical trial and literature evidence collected in this pack, letrozole is consistently and repeatedly described as a third-generation, non-steroidal aromatase inhibitor. It blocks the peripheral conversion of androgens to estrogens, depriving estrogen-dependent breast tumor cells of the hormonal signal that drives their proliferation.

"Female breast carcinoma" is a broad KG disease node that overlaps almost entirely with letrozole's core, already-approved indication (HR+ postmenopausal breast cancer). The large volume and quality of supporting evidence — including landmark Phase 3 trials such as the head-to-head letrozole-vs-tamoxifen adjuvant trial (NCT00004205, n=8,028) and multiple CDK4/6-inhibitor-combination trials — reflects the fact that this is a well-validated, on-label use rather than a new therapeutic hypothesis.

It is worth noting that this evidence pack contains several closely related disease nodes for the same underlying tumor type at different granularities (e.g., "estrogen-receptor positive breast cancer," "hormone-resistant breast carcinoma," "bilateral breast carcinoma"). Some of these are mechanistically sound extensions (e.g., ER+ subtype, L1 evidence), while others — notably "estrogen-receptor negative breast cancer" and "Ehrlich tumor carcinoma" — were flagged internally as likely knowledge-graph node-confusion artifacts (ER-negative tumors do not depend on the aromatase pathway letrozole inhibits, and Ehrlich tumor is a murine model, not a human disease entity). This heterogeneity underscores that the "multi-indication" candidate should be interpreted as a confirmation-and-refinement exercise around letrozole's known pharmacology rather than a single clean repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00073528](https://clinicaltrials.gov/study/NCT00073528) | Phase 3 | Completed | 1,286 | RCT comparing lapatinib + letrozole vs. letrozole alone in HR+ advanced/metastatic breast cancer; direct approved-indication evidence |
| [NCT00330317](https://clinicaltrials.gov/study/NCT00330317) | Phase 3 | Completed | 300 | Neoadjuvant letrozole in postmenopausal ER/PR+ primary breast cancer to permit breast-conserving surgery |
| [NCT02040857](https://clinicaltrials.gov/study/NCT02040857) | Phase 2 | Completed | 162 | Palbociclib + adjuvant endocrine therapy (letrozole-based) in HR+ invasive breast carcinoma |
| [NCT00004205](https://clinicaltrials.gov/study/NCT00004205) | Phase 3 | Completed | 8,028 | Landmark RCT: letrozole vs. tamoxifen as adjuvant endocrine therapy for ER/PR+ postmenopausal breast cancer |
| [NCT04571437](https://clinicaltrials.gov/study/NCT04571437) | Phase 2 | Unknown | 204 | Letrozole ± metronomic capecitabine as first-line therapy in ER+/HER2- advanced breast cancer |
| [NCT05439499](https://clinicaltrials.gov/study/NCT05439499) | Phase 3 | Unknown | 434 | FCN-437c vs. placebo combined with letrozole/anastrozole ± goserelin in HR+/HER2- advanced breast cancer |
| [NCT03820830](https://clinicaltrials.gov/study/NCT03820830) | Phase 3 | Active, not recruiting | 405 | Adjuvant palbociclib + endocrine therapy vs. endocrine therapy alone for resected locoregional recurrence, HR+/HER2- |
| [NCT04095364](https://clinicaltrials.gov/study/NCT04095364) | Phase 3 | Active, not recruiting | 450 | Paclitaxel/carboplatin/maintenance letrozole vs. letrozole monotherapy in low-grade serous ovarian/peritoneal carcinoma |
| [NCT03969121](https://clinicaltrials.gov/study/NCT03969121) | Phase 3 | Completed | 141 | Neoadjuvant hormonal therapy (letrozole) + palbociclib vs. placebo in operable HR+/HER2- primary breast cancer |
| [NCT00062751](https://clinicaltrials.gov/study/NCT00062751) | Phase 2 | Completed | 108 | Letrozole + temsirolimus vs. letrozole alone in locally advanced/metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT (Phase 2) | The Lancet Oncology | CORALLEEN: neoadjuvant ribociclib + letrozole vs. chemotherapy in luminal B HR+/HER2- breast cancer |
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT (Phase 2) | Breast Cancer Res Treat | PALOMA-1 overall survival: palbociclib + letrozole vs. letrozole alone, first-line ER+/HER2- advanced breast cancer |
| [34645649](https://pubmed.ncbi.nlm.nih.gov/34645649/) | 2022 | Biomarker sub-analysis | Clin Cancer Res | Ki67 response biomarkers for palbociclib + letrozole in ER+/HER2- breast cancer |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review (pharmacology) | Life Sciences | Comprehensive review of letrozole pharmacology, toxicity, and therapeutic effects |
| [35378469](https://pubmed.ncbi.nlm.nih.gov/35378469/) | 2022 | Review/biomarker | Current Problems in Cancer | Predictive and prognostic factors for palbociclib + letrozole response in HR+ advanced breast cancer |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamic/pharmacokinetic review of letrozole and its clinical efficacy/safety |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh) | Review of letrozole development and use in advanced and neoadjuvant breast cancer |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | Translational study | Medical Oncology | Letrozole-induced changes in carcinoma-associated fibroblasts and effect on breast cancer cell biology |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | Comparative study | Comput Math Methods Med | Efficacy/safety/prognosis of sequential tamoxifen + letrozole vs. letrozole monotherapy |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | Commentary | Women's Health Issues | Clinical implications and remaining questions from the Letrozole Breast Cancer Trial |

---

## Malaysia Market Information

NPRA records confirm letrozole is marketed in Malaysia with **7 registered licenses** (`market_status: 已上市 / Marketed`). However, individual license numbers, product names, dosage forms, manufacturers, and approved-indication texts were not returned in this data pull — this is a flagged Blocking-severity data gap (DG001) that also prevents a full safety pre-assessment. These details should be sourced directly from NPRA registration records before proceeding further.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted endocrine therapy — non-steroidal aromatase inhibitor (non-cytotoxic hormonal agent), mechanistically distinct from conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low — aromatase inhibitors as a class are not associated with significant myelosuppression; no hematologic toxicity signal appears in the collected evidence. Please refer to the package insert for confirmed hematologic monitoring requirements |
| Emetogenicity Classification | Low — oral hormonal/endocrine agents typically carry minimal emetogenic potential; not independently confirmed in this data pull |
| Monitoring Items | Bone mineral density, lipid profile, and liver function are typically monitored for this drug class; specific TFDA/NPRA-labeled monitoring requirements were not available in this evidence pack (Data Gap DG001) |
| Handling Protection | Oral solid-dosage hormonal agent; not typically classified as requiring special cytotoxic-drug handling precautions. Please refer to the package insert for confirmation |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for letrozole in breast cancer is very strong (L1, multiple completed Phase 3 RCTs including a landmark 8,028-patient adjuvant trial), but this largely confirms an already-approved indication rather than a novel repurposing opportunity. Critically, TFDA/NPRA label warnings and contraindications (DG001, Blocking severity) are missing, which currently blocks a complete safety pre-assessment (S1) — this must be resolved before any "Go" decision.

**To proceed, the following is needed:**
- Retrieve the TFDA/NPRA package insert (warnings, contraindications, DDI) to resolve the Blocking data gap (DG001)
- Obtain structured DrugBank MOA data to complete the mechanistic-relevance analysis (DG002)
- Confirm the specific approved-indication text for each of the 7 Malaysia licenses to determine whether "female breast carcinoma" is already covered under the existing label, versus representing a genuinely incremental indication
- Clarify whether the other KG-predicted nodes in this multi-indication candidate (e.g., ER-negative breast cancer, Ehrlich tumor) should be excluded as likely graph-node noise before any downstream regulatory use of this prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

