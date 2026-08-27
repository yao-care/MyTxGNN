---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: From Chronic Myeloid Leukemia/GIST to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Imatinib is a BCR-ABL/KIT/PDGFR tyrosine kinase inhibitor originally developed for chronic myeloid leukemia and gastrointestinal stromal tumors (GIST), as referenced in the evidence pack's trial records. The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, with **9 clinical trials** and **20 publications** currently supporting this direction — notably, this is already an FDA/EMA-approved use of imatinib in other jurisdictions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in TFDA license data (Data Gap DG001); imatinib's globally-approved indications include CML and GIST, per trial documentation in this evidence pack |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Market Status (Taiwan, TFDA) | ✓ Marketed |
| Number of Registrations | 22 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug record is not available (Data Gap DG002). However, the evidence pack's own repurposing rationale documents that imatinib is a small-molecule tyrosine kinase inhibitor targeting BCR-ABL, KIT, and PDGFR (α/β).

DFSP is driven by the t(17;22)(q22;q13) translocation, producing a COL1A1-PDGFB fusion gene that causes constitutive activation of PDGFRB signaling. Because imatinib directly inhibits PDGFRB, it blocks the core oncogenic driver of this tumor — a mechanistic fit that is unusually direct for a repurposing candidate.

This is not a purely theoretical extrapolation: imatinib already holds regulatory approval in the US and EU for unresectable, metastatic, or recurrent DFSP, based on multiple single-arm Phase 1/2 trials rather than a large Phase 3 RCT. That is why the evidence is scored L2 (strong clinical support, but not the L1 bar of ≥2 completed Phase 3 RCTs) — in clinical practice, the strength of this evidence is generally regarded as close to definitive for this rare tumor type.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00084630](https://clinicaltrials.gov/study/NCT00084630) | Phase 2 | Completed | 40 | Imatinib in locally advanced/metastatic DFSP, including transformed fibrosarcomatous DFSP; DFSP-specific pivotal trial (Grade A) |
| [NCT00122473](https://clinicaltrials.gov/study/NCT00122473) | Phase 1/2 | Completed | 30 | Open-label Glivec® in primary or recurrent DFSP; directly relevant (Grade A) |
| [NCT00555581](https://clinicaltrials.gov/study/NCT00555581) | Phase 2A | Completed | 30 | Safety/tolerability study; notes imatinib is FDA-approved for CML, GIST, DFSP, Ph+ ALL, hypereosinophilic syndrome, and systemic mastocytosis (Grade A) |
| [NCT00243191](https://clinicaltrials.gov/study/NCT00243191) | Phase 2 | Completed | 18 | Short-course neoadjuvant Gleevec in DFSP (Grade A) |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Broad rare-tumor basket trial including DFSP; not DFSP-specific but large cohort (Grade B) |
| [NCT01046487](https://clinicaltrials.gov/study/NCT01046487) | Phase 1 | Completed | 26 | Imatinib + metronomic cyclophosphamide dose-escalation in rare tumors incl. soft tissue sarcoma/DFSP (Grade B) |
| [NCT00171912](https://clinicaltrials.gov/study/NCT00171912) | Phase 2 | Completed | 38 | Imatinib across malignancies with activated tyrosine kinases; DFSP as subgroup (Grade B) |
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | Completed | 17 | Glivec in soft tissue sarcomas expressing COL1A1/PDGF-β fusion (DFSP and giant cell fibroblastoma) (Grade B) |
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | Phase 2a | Terminated | 23 | Pazopanib (not imatinib) in unresectable DFSP; mechanistic analogy only (Grade C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30601909](https://pubmed.ncbi.nlm.nih.gov/30601909/) | 2019 | Systematic Review | JAMA Dermatology | Systematic review of imatinib treatment for locally advanced/metastatic DFSP |
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | European Journal of Cancer | European multidisciplinary (EADO/EDF/UEMS/EADV) interdisciplinary guideline update on DFSP diagnosis and treatment |
| [41042442](https://pubmed.ncbi.nlm.nih.gov/41042442/) | 2025 | Review | Current Treatment Options in Oncology | Current treatments and clinical trials for DFSP, including imatinib's role |
| [27608549](https://pubmed.ncbi.nlm.nih.gov/27608549/) | 2017 | Translational Study | Journal of Investigative Dermatology | Gene expression/immunohistochemistry study of imatinib-induced senescence in fibrosarcomatous DFSP |
| [33449152](https://pubmed.ncbi.nlm.nih.gov/33449152/) | 2021 | Review | Cellular and Molecular Life Sciences | PDGFRB mutations as oncogenic drivers relevant to DFSP and related disorders |
| [28988501](https://pubmed.ncbi.nlm.nih.gov/28988501/) | 2017 | Expert Review | Expert Review of Anticancer Therapy | DFSP and GIST as models for targeted therapy in soft tissue sarcomas |
| [31466588](https://pubmed.ncbi.nlm.nih.gov/31466588/) | 2019 | Review | Dermatologic Clinics | Overview of DFSP clinical features, histology, and systemic therapy options |
| [28795284](https://pubmed.ncbi.nlm.nih.gov/28795284/) | 2017 | Review | Current Treatment Options in Oncology | Multidisciplinary approach to DFSP management |
| [22285046](https://pubmed.ncbi.nlm.nih.gov/22285046/) | 2012 | Review | Actas Dermo-Sifiliográficas | COL1A1-PDGFB translocation and its diagnostic/therapeutic implications |
| [41032154](https://pubmed.ncbi.nlm.nih.gov/41032154/) | 2025 | Review | Current Treatment Options in Oncology | Diagnostics and molecular pathology of DFSP |

## Market Information

TFDA/NPRA regulatory data confirms **22 registered licenses** with market status "已上市" (Marketed), but individual license fields (license number, product name, manufacturer, approved indication text) are blank in this data pack — this is tracked as Blocking Data Gap **DG001** (TFDA label/warnings not yet retrieved). A full license-level breakdown cannot be presented until this gap is remediated.

## Cytotoxicity

Imatinib is an antineoplastic agent (targeted small-molecule kinase inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor targeting BCR-ABL/KIT/PDGFR) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four Grade-A, DFSP-specific completed trials (NCT00084630, NCT00122473, NCT00555581, NCT00243191) plus a dedicated systematic review and a 2025 international guideline directly support imatinib's activity in DFSP, and this indication is already regulatory-approved elsewhere. Evidence level is L2 rather than L1 only because approval rested on single-arm Phase 1/2 trials, not head-to-head Phase 3 RCTs — the guardrail reflects that gap, not doubt about the mechanism.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap DG001
- DrugBank-sourced MOA and full safety/DDI profile — High-priority gap DG002
- Taiwan-specific license and approved-indication text (currently blank in this pack)
- Confirmation of whether DFSP is within imatinib's currently approved Taiwan label, or would require off-label/expanded-access pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

