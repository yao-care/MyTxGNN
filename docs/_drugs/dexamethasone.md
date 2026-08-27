---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 5
---

# Dexamethasone
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

# Dexamethasone: From Corticosteroid Anti-Inflammatory Therapy to Diffuse Large B-Cell Lymphoma

## One-Sentence Summary

Dexamethasone is a synthetic glucocorticoid corticosteroid used broadly for anti-inflammatory and immunosuppressive therapy across many conditions. The TxGNN model's top-ranked prediction identifies **Diffuse Large B-Cell Lymphoma (DLBCL)** as a candidate new indication, supported by **50 clinical trials** and **20 publications** retrieved for this drug–disease pair — though most evidence reflects dexamethasone's role as a component of combination chemotherapy regimens (e.g., DHAP, GDP) rather than as a standalone agent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no approved indication text available from Malaysia NPRA license records) |
| Predicted New Indication | Diffuse Large B-Cell Lymphoma |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 38 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for dexamethasone in this evidence pack. Based on known pharmacology, dexamethasone is a potent synthetic glucocorticoid that binds the glucocorticoid receptor to suppress inflammatory and immune signaling pathways.

In the context of DLBCL, dexamethasone is a standard component of several well-established salvage and induction chemotherapy backbones — including DHAP (dexamethasone, cytarabine, cisplatin) and GDP (gemcitabine, dexamethasone, cisplatin) — and is also widely used for prophylaxis and management of cytokine release syndrome (CRS) around CAR-T cell therapy (e.g., axicabtagene ciloleucel). Mechanistically, glucocorticoids induce apoptosis in lymphoid malignant cells and suppress B-cell receptor (BCR) oncogenic signaling, a recurrent feature of aggressive B-cell lymphomas including DLBCL.

The evidence is substantial in volume but largely indirect: dexamethasone typically appears as one ingredient within multi-drug regimens rather than as a single-agent intervention, making it difficult to isolate its independent contribution to efficacy. This is reflected in the L2 evidence level and the "Proceed with Guardrails" recommendation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03391466](https://clinicaltrials.gov/study/NCT03391466) | Phase 3 | Completed | 359 | ZUMA-7: axicabtagene ciloleucel vs. standard-of-care second-line therapy in r/r DLBCL; dexamethasone used mainly for CRS prophylaxis rather than as primary anti-lymphoma therapy |
| [NCT00137995](https://clinicaltrials.gov/study/NCT00137995) | Phase 3 | Completed | 481 | R-ICE vs. R-DHAP (DHAP contains dexamethasone) as induction therapy in previously treated DLBCL, followed by rituximab maintenance |
| [NCT00078949](https://clinicaltrials.gov/study/NCT00078949) | Phase 3 | Completed | 849 | (R)-GDP vs. (R)-DHAP as salvage chemotherapy prior to autologous stem cell transplant in relapsed/refractory aggressive NHL — both regimens dexamethasone-containing |
| [NCT05498259](https://clinicaltrials.gov/study/NCT05498259) | Phase 2 | Unknown | 46 | Orelabrutinib + rituximab, followed by orelabrutinib + R-CHOP-like regimen, in newly diagnosed untreated non-GCB DLBCL |
| [NCT02532192](https://clinicaltrials.gov/study/NCT02532192) | Phase 1 | Withdrawn | 0 | Belinostat combined with RDHAP (rituximab, dexamethasone, cytarabine, cisplatin) in relapsed/refractory DLBCL prior to ASCT; trial withdrawn before enrollment |
| [NCT01805557](https://clinicaltrials.gov/study/NCT01805557) | Phase 2/3 | Completed | 108 | R-DHAP ± bortezomib as induction therapy in transplant-eligible relapsed/refractory DLBCL |
| [NCT05966233](https://clinicaltrials.gov/study/NCT05966233) | Phase 2 | Withdrawn | 0 | Addition of polatuzumab vedotin to standard R-DHAP as pre-transplant induction in relapsed/refractory DLBCL |
| [NCT06835530](https://clinicaltrials.gov/study/NCT06835530) | Phase 2 | Recruiting | 47 | Rituximab + golcadomide as chemo-free front-line therapy for frail older patients with DLBCL |
| [NCT03954106](https://clinicaltrials.gov/study/NCT03954106) | Phase 2 | Terminated | 25 | Defibrotide for prevention of CAR-T-associated neurotoxicity in DLBCL patients receiving axicabtagene ciloleucel |
| [NCT04663347](https://clinicaltrials.gov/study/NCT04663347) | Phase 1/2 | Active, not recruiting | 543 | Epcoritamab alone or combined with other agents in B-cell non-Hodgkin lymphoma (B-NHL), including DLBCL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35717989](https://pubmed.ncbi.nlm.nih.gov/35717989/) | 2022 | RCT | Lancet | TRANSFORM trial interim analysis: lisocabtagene maraleucel vs. standard-of-care salvage chemotherapy + ASCT as second-line therapy in relapsed/refractory large B-cell lymphoma |
| [16702182](https://pubmed.ncbi.nlm.nih.gov/16702182/) | 2006 | RCT | Annals of Oncology | CORAL study: randomized Phase 3 comparison of R-ICE vs. R-DHAP (dexamethasone, cytarabine, cisplatin) in relapsed CD20+ DLBCL prior to ASCT |
| [38802107](https://pubmed.ncbi.nlm.nih.gov/38802107/) | 2024 | RCT | British Journal of Haematology | CCTG LY.17: randomized Phase 2 trial of R-DICEP vs. R-GDP (dexamethasone-containing) as pre-ASCT salvage in relapsed/refractory DLBCL |
| [34296427](https://pubmed.ncbi.nlm.nih.gov/34296427/) | 2021 | Cohort | British Journal of Haematology | ZUMA-1 cohort 6: prophylactic corticosteroids for management of CRS and neurologic events with axicabtagene ciloleucel in refractory large B-cell lymphoma |
| [38701792](https://pubmed.ncbi.nlm.nih.gov/38701792/) | 2024 | Review | Cancer Cell | Molecular targets of glucocorticoids elucidating mechanism of efficacy in aggressive lymphomas via inhibition of B-cell receptor (BCR) oncogenic signaling |
| [38191715](https://pubmed.ncbi.nlm.nih.gov/38191715/) | 2024 | Meta-analysis | Annals of Hematology | Systematic review and meta-analysis of 21 RCTs evaluating experimental regimens vs. R-CHOP as frontline DLBCL therapy |
| [37548344](https://pubmed.ncbi.nlm.nih.gov/37548344/) | 2023 | Network meta-analysis | Leukemia & Lymphoma | Comparative effectiveness of salvage chemotherapy regimens vs. CAR-T therapies in relapsed/refractory DLBCL |
| [35727601](https://pubmed.ncbi.nlm.nih.gov/35727601/) | 2022 | Phase 2 trial | Clinical Cancer Research | R2-GDP-GOTEL trial final results: lenalidomide plus R-GDP (dexamethasone-containing) in relapsed/refractory DLBCL with immune biomarker subanalysis |
| [40079097](https://pubmed.ncbi.nlm.nih.gov/40079097/) | 2025 | Retrospective cohort | Haematologica | Real-world comparison of lisocabtagene maraleucel and axicabtagene ciloleucel in large B-cell lymphoma with 3-year follow-up |
| [20660832](https://pubmed.ncbi.nlm.nih.gov/20660832/) | 2010 | Review | Journal of Clinical Oncology | Review of salvage regimens with autologous transplantation for relapsed large B-cell lymphoma in the rituximab era |

## Malaysia Market Information

Malaysia NPRA records show **38 total registrations** for dexamethasone with market status "已上市" (Marketed). However, product-level details (authorization numbers, product names, dosage forms, approved indication text) were not populated in this evidence pack and cannot be reported here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexamethasone has a large body of clinical trial and literature support in the DLBCL context (L2 evidence level), but nearly all of this evidence derives from multi-drug regimens (DHAP, GDP, R-CHOP variants) or CRS-management use around CAR-T therapy, rather than dedicated trials of dexamethasone as a discrete repurposing candidate. This supports guarded, protocol-embedded use rather than a standalone new-indication claim.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, precautions, and contraindications (currently a Blocking data gap — DG001)
- Detailed mechanism of action data from DrugBank (currently a High-severity data gap — DG002)
- Confirmed original approved indication(s) from complete Malaysia license records
- Drug-drug interaction (DDI) profile, currently unqueried/not found
- A trial-design-level analysis isolating dexamethasone's independent contribution within combination regimens, to distinguish "adjunct/supportive" use from "primary anti-lymphoma" repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

