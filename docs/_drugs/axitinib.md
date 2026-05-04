---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Advanced Renal Cell Carcinoma to Renal Cell Carcinoma Associated with Neuroblastoma

## One-Sentence Summary

Axitinib (Inlyta®) is a selective VEGFR-1/2/3 tyrosine kinase inhibitor approved for the second-line treatment of advanced renal cell carcinoma (RCC), currently marketed in Malaysia with 2 registered products. The TxGNN model's highest-ranked prediction is **renal cell carcinoma associated with neuroblastoma** (score 99.90%), an extremely rare RCC variant with currently **no supporting clinical trials or published literature**. This is a multi-indication evaluation covering 10 TxGNN predictions; the most evidence-supported candidate is **renal carcinoma** (Rank 6, L1 level, 20 publications including multiple Phase 3 RCTs), while **Xp11.2/TFE3-translocation RCC**, **childhood RCC**, and **collecting duct carcinoma** carry active Phase 2 trial support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced Renal Cell Carcinoma (second-line; derived from known approved use) |
| Predicted New Indication | Renal Cell Carcinoma Associated with Neuroblastoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no clinical studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (Rank 1) — see multi-indication summary for full picture |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on clinical literature referenced within this report, Axitinib is a selective second-generation VEGFR-1/2/3 tyrosine kinase inhibitor (TKI). It works by blocking VEGFR signaling to suppress tumor angiogenesis — the key growth mechanism in most renal cell carcinoma subtypes. This activity has been confirmed in multiple Phase 3 randomized controlled trials (KEYNOTE-426, JAVELIN Renal 101, RENOTORCH), leading to FDA approval as a second-line RCC agent and current Malaysia market approval.

The TxGNN model assigns high scores across multiple RCC subtypes because renal cell carcinoma broadly depends on VEGF/VEGFR-driven angiogenesis. The top prediction — RCC associated with neuroblastoma — is an extremely rare entity (only a handful of reported cases worldwide) that shares the broader RCC disease node in the knowledge graph. The high TxGNN score is most plausibly explained by graph-proximity to better-studied RCC subtypes rather than direct mechanistic or clinical evidence for this specific variant.

For RCC subtypes with demonstrated molecular evidence of VEGFR pathway activation — notably Xp11.2/TFE3-translocation RCC (mTOR-VEGF axis upregulation) and collecting duct carcinoma (partial VEGFR overexpression reported) — the mechanistic rationale is substantially stronger and is being actively tested in clinical trials.

---

## Clinical Trial Evidence

*Primary prediction (Rank 1): renal cell carcinoma associated with neuroblastoma*

Currently no related clinical trials registered.

> For clinical trial evidence across all 10 predicted indications, see the **All Predicted Indications Summary** section below.

---

## Literature Evidence

*Primary prediction (Rank 1): renal cell carcinoma associated with neuroblastoma*

Currently no related literature available.

> For literature evidence across all 10 predicted indications, see the **All Predicted Indications Summary** section below.

---

## All Predicted Indications Summary

This evidence pack is a **multi-indication evaluation** (ID: TW-DB06626-multi) covering 10 TxGNN predictions. Below is a consolidated overview followed by the clinical evidence for each actionable prediction.

### Prediction Overview

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|-------------|----------------|----------|
| 1 | Renal cell carcinoma associated with neuroblastoma | 99.90% | L5 | Hold |
| 2 | RCC with Xp11.2 translocations/TFE3 gene fusions | 99.90% | L2 | Research Question |
| 3 | Unclassified renal cell carcinoma | 99.90% | L3 | Research Question |
| 4 | Childhood kidney cell carcinoma | 99.87% | L2 | Research Question |
| 5 | Liposarcoma | 99.87% | L5 | Hold |
| **6** | **Renal carcinoma** | **99.85%** | **L1** | **Proceed with Guardrails** |
| 7 | Ovarian myxoid liposarcoma | 99.84% | L5 | Hold |
| 8 | Angiolipoma | 99.83% | L5 | Hold |
| 9 | Collecting duct carcinoma | 99.81% | L3 | Research Question |
| 10 | Familial spontaneous pneumothorax | 99.78% | L5 | Hold |

---

### Clinical Trial Evidence — Rank 2: Xp11.2/TFE3 RCC & Rank 4: Childhood RCC

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|-----------|--------------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, Not Recruiting | 15 | Randomized trial of axitinib + nivolumab vs. nivolumab monotherapy for TFE/translocation RCC across all age groups; directly addresses both Xp11.2 RCC and pediatric RCC (Xp11.2 subtype accounts for ~60–70% of childhood RCC) |
| [NCT04510597](https://clinicaltrials.gov/study/NCT04510597) | Phase 3 | Recruiting | 364 | PROBE Trial: immunotherapy ± cytoreductive nephrectomy for metastatic RCC; primarily adult population but validates ICI + VEGFR TKI framework applicable to pediatric RCC subgroups |

---

### Clinical Trial Evidence — Rank 3: Unclassified RCC

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|-----------|--------------|
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | Real-World Study | Completed | 684 | UK retrospective study of sunitinib (1L) → axitinib (2L) sequencing across metastatic/advanced RCC histologies; subgroup analysis could yield data on unclassified RCC |
| [NCT02156895](https://clinicaltrials.gov/study/NCT02156895) | Post-Marketing Surveillance | Completed | 111 | Safety and efficacy monitoring for axitinib in routine clinical practice across all RCC subtypes |

---

### Clinical Trial Evidence — Rank 9: Collecting Duct Carcinoma

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|-----------|--------------|
| [NCT06211114](https://clinicaltrials.gov/study/NCT06211114) | Phase 2 | Recruiting | 30 | Directly designed for previously treated advanced collecting duct carcinoma using immune checkpoint inhibitor + axitinib combination; trial initiation itself demonstrates mechanistic rationale is recognized by the research community |

---

### Literature Evidence — Rank 6: Renal Carcinoma (L1 — Strongest Evidence)

> **Note:** This prediction reflects Axitinib's known approved indication. The L1 evidence below validates the TxGNN model's accuracy.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | Phase 3 RCT (KEYNOTE-426) | N Engl J Med | Pembrolizumab + axitinib showed superior OS, PFS, and ORR versus sunitinib as first-line treatment for advanced RCC |
| [37500340](https://pubmed.ncbi.nlm.nih.gov/37500340/) | 2023 | Phase 3 RCT 43-month follow-up | European Urology | Long-term KEYNOTE-426 results confirm durable OS and PFS benefit for pembrolizumab + axitinib |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | Phase 3 RCT 5-year analysis | Nature Medicine | 5-year KEYNOTE-426 analysis with prespecified biomarker data confirms durable clinical benefit |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | Phase 3 RCT (JAVELIN Renal 101) | N Engl J Med | Avelumab + axitinib significantly prolonged PFS versus sunitinib in previously untreated advanced RCC |
| [39706335](https://pubmed.ncbi.nlm.nih.gov/39706335/) | 2025 | Phase 3 RCT final analysis (JAVELIN Renal 101) | Ann Oncol | Final OS analysis of JAVELIN Renal 101; overall survival primary endpoint results reported |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | Phase 3 RCT (RENOTORCH) | Ann Oncol | Toripalimab + axitinib vs. sunitinib for intermediate/poor-risk advanced RCC; supports ICI + axitinib as a platform |
| [33284113](https://pubmed.ncbi.nlm.nih.gov/33284113/) | 2020 | Phase 3 RCT extended follow-up | Lancet Oncol | KEYNOTE-426 extended follow-up: sustained efficacy and safety of pembrolizumab + axitinib over sunitinib |
| [32895571](https://pubmed.ncbi.nlm.nih.gov/32895571/) | 2020 | Phase 3 RCT biomarker analysis | Nature Medicine | Molecular analyses of JAVELIN Renal 101 (n=886); PD-L1 and tumor mutational burden were not predictive of PFS |
| [29033542](https://pubmed.ncbi.nlm.nih.gov/29033542/) | 2017 | Drug Review | Drug Des Devel Ther | Axitinib pharmacology, development, and clinical positioning as second-generation VEGFR TKI in RCC |
| [28276433](https://pubmed.ncbi.nlm.nih.gov/28276433/) | 2017 | Disease Review | Nat Rev Dis Primers | Comprehensive overview of RCC biology, molecular subtypes, and treatment landscape |

---

### Literature Evidence — Rank 4: Childhood RCC

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatr Blood Cancer | Review of treatment options for advanced pediatric RCC; highlights lack of standardized therapy and context for VEGFR TKI use |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case Report | Can Urol Assoc J | First reported axitinib use in a child (12-year-old) with malignant epithelioid angiomyolipoma; authors conclude adult protocols can be safely applied in this rare pediatric case |

---

## Malaysia Market Information

Axitinib has **2 registered products** in the Malaysian market. Detailed registration records (product name, dosage form, manufacturer, and approved indication text) are not currently available in the evidence database and require direct verification with NPRA.

| Item | Status |
|------|--------|
| Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Product Details | Not available — please verify via NPRA official database |

---

## Cytotoxicity

Axitinib is an anticancer agent indicated for renal cell carcinoma.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective VEGFR-1/2/3 tyrosine kinase inhibitor (TKI); not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard precautions for oral targeted therapy; consult institutional cytotoxic drug handling guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Full safety data (warnings, contraindications, and drug interactions) are not available in the current evidence pack. Retrieval of the product package insert (SOP remediation item DG001) is required before clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold (Rank 1: RCC Associated with Neuroblastoma) / Proceed with Guardrails (Rank 6: Renal Carcinoma)**

**Rationale:**
- The top TxGNN prediction (RCC associated with neuroblastoma, L5) has no clinical or published evidence and represents an ultra-rare entity; a "Hold" decision is appropriate until any case-level data emerges.
- The strongest evidence sits at Rank 6 (renal carcinoma, L1), supported by multiple completed Phase 3 RCTs — this represents Axitinib's approved indication and confirms the model's face validity.
- RCC subtypes at Ranks 2, 4, and 9 (Xp11.2/TFE3 RCC, childhood RCC, collecting duct carcinoma) have active Phase 2 trials and carry mechanistic rationale; these are appropriate "Research Question" candidates to monitor.
- Predictions with L5 evidence and no mechanistic link to VEGFR (liposarcoma, ovarian myxoid liposarcoma, angiolipoma, familial spontaneous pneumothorax) should remain on "Hold."

**To proceed, the following is needed:**
- Retrieve NPRA full registration records for both Axitinib products (product names, dosage forms, approved indications)
- Obtain detailed MOA data from DrugBank API (data gap DG002) to strengthen mechanistic analysis
- Download and parse the product package insert PDF to extract warnings and contraindications (data gap DG001 — currently blocks safety pre-screening)
- Monitor **NCT03595124** results (Xp11.2/TFE3 RCC, expected completion November 2026) as this will provide pivotal evidence for Ranks 2 and 4
- Monitor **NCT06211114** results (collecting duct carcinoma, expected completion February 2027)
- Before any off-label use in pediatric patients (Rank 4), obtain pediatric pharmacokinetic data and confirm dosing guidance

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

