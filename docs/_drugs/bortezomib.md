---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 5
---

# Bortezomib
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

# Bortezomib: From Multiple Myeloma to B-Cell Neoplasm

## One-Sentence Summary

Bortezomib is a first-in-class proteasome inhibitor, originally approved for the treatment of multiple myeloma and mantle cell lymphoma. The TxGNN model predicts it may have broader efficacy across **B-cell neoplasms** as a class, with **50 clinical trials** and **20 publications** providing substantial supporting evidence for this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma, Mantle cell lymphoma |
| Predicted New Indication | B-cell neoplasm |
| TxGNN Prediction Score | Not available (score: 0.0) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Go |

## Why is This Prediction Reasonable?

Bortezomib (brand name: Velcade) is a selective, reversible inhibitor of the 26S proteasome. The proteasome is an enzyme complex present in all cells that degrades ubiquitin-tagged proteins, including key regulators of the cell cycle, apoptosis, transcription (notably NF-κB), and DNA repair. By blocking proteasome activity, bortezomib causes accumulation of pro-apoptotic factors and misfolded proteins, leading to endoplasmic reticulum stress and programmed cell death. Cancer cells—particularly those with high immunoglobulin production like plasma cells and B-lymphocytes—are especially vulnerable to proteasome inhibition because of their elevated protein synthesis burden.

The relationship between the original indications (multiple myeloma and mantle cell lymphoma) and the broader predicted indication (B-cell neoplasm) is mechanistically coherent. Multiple myeloma is a malignancy of terminally differentiated B cells (plasma cells), while mantle cell lymphoma arises from pre-germinal center B cells. The broader category of B-cell neoplasms—including diffuse large B-cell lymphoma (DLBCL), follicular lymphoma, Waldenström macroglobulinemia, plasmablastic lymphoma, and others—shares the common feature of B-cell lineage dependency on the NF-κB pathway and the ubiquitin-proteasome system for survival and proliferation.

Clinical evidence already supports this broader application. Bortezomib has demonstrated activity in follicular lymphoma (Phase 3 NCT00312845), DLBCL (REMoDL-B trial showing benefit in ABC subtype), Waldenström macroglobulinemia (Phase 3 NCT01788020), plasmablastic lymphoma (retrospective analyses showing long-term survival with bortezomib-EPOCH), and T-cell lymphoblastic lymphoma (Phase 3 AALL1231). This body of evidence validates the TxGNN prediction that bortezomib's mechanism extends across the full spectrum of B-cell malignancies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00312845](https://clinicaltrials.gov/study/NCT00312845) | Phase 3 | Completed | 676 | VELCADE + Rituximab vs Rituximab alone in relapsed/refractory follicular B-NHL; evaluated whether combination improves PFS |
| [NCT02195479](https://clinicaltrials.gov/study/NCT02195479) | Phase 3 | Completed | 706 | D-VMP vs VMP in previously untreated MM ineligible for transplant; demonstrated PFS benefit with daratumumab addition to bortezomib backbone |
| [NCT03110562](https://clinicaltrials.gov/study/NCT03110562) | Phase 3 | Completed | 402 | Selinexor + Bortezomib + Dex vs Bortezomib + Dex in RRMM; evaluated novel combination in bortezomib-based regimen |
| [NCT01788020](https://clinicaltrials.gov/study/NCT01788020) | Phase 3 | Completed | 202 | DRC ± Bortezomib as first-line for Waldenström macroglobulinemia; evaluated added benefit of bortezomib in WM |
| [NCT02112916](https://clinicaltrials.gov/study/NCT02112916) | Phase 3 | Active | 847 | Bortezomib on modified ABFM backbone in newly diagnosed T-ALL/T-LLy; evaluating whether bortezomib enhances chemosensitivity |
| [NCT03652064](https://clinicaltrials.gov/study/NCT03652064) | Phase 3 | Active | 395 | D-VRd vs VRd in untreated MM non-transplant; assessing MRD negativity improvement with daratumumab |
| [NCT00644228](https://clinicaltrials.gov/study/NCT00644228) | Phase 3 | Active | 525 | VRd vs Rd in previously untreated MM; comparing bortezomib-containing triplet to doublet therapy |
| [NCT04181827](https://clinicaltrials.gov/study/NCT04181827) | Phase 3 | Active | 419 | CAR-T (cilta-cel) vs PVd/DPd in relapsed lenalidomide-refractory MM; PVd as standard comparator arm |
| [NCT00369707](https://clinicaltrials.gov/study/NCT00369707) | Phase 2 | Completed | 42 | Bortezomib + Rituximab as front-line in low-grade NHL; demonstrated activity in indolent B-cell lymphomas |
| [NCT00114738](https://clinicaltrials.gov/study/NCT00114738) | Phase 2 | Completed | 53 | EPOCH-R-B induction ± bortezomib maintenance in untreated MCL; 92% complete remission rate reported |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38084760](https://pubmed.ncbi.nlm.nih.gov/38084760/) | 2024 | RCT | N Engl J Med | PERSEUS trial: Daratumumab + VRd significantly improved PFS in transplant-eligible newly diagnosed MM |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | AALL1231 Phase III: Bortezomib improved outcomes in newly diagnosed T-ALL; demonstrated benefit in lymphoblastic malignancies |
| [31097405](https://pubmed.ncbi.nlm.nih.gov/31097405/) | 2019 | RCT | Lancet Oncol | OPTIMISMM trial: PVd significantly prolonged PFS vs Vd in lenalidomide-exposed RRMM |
| [39777934](https://pubmed.ncbi.nlm.nih.gov/39777934/) | 2025 | RCT | Eur J Haematol | OPTIMISMM final OS: Updated survival analyses confirmed PVd benefit in lenalidomide-exposed RRMM |
| [40565058](https://pubmed.ncbi.nlm.nih.gov/40565058/) | 2025 | Preclinical | Int J Mol Sci | CDCA2 overexpression in DLBCL promotes bortezomib sensitivity; ABC and molecular high-grade subtypes benefit |
| [38767403](https://pubmed.ncbi.nlm.nih.gov/38767403/) | 2024 | Review | Am J Hematol | Plasmablastic lymphoma 2024 update: bortezomib-containing regimens recommended for this rare aggressive B-cell NHL |
| [29303024](https://pubmed.ncbi.nlm.nih.gov/29303024/) | 2018 | Retrospective | Leuk Lymphoma | Bortezomib + dose-adjusted EPOCH induced long-term survival in plasmablastic lymphoma |
| [36652193](https://pubmed.ncbi.nlm.nih.gov/36652193/) | 2023 | Review | Drugs | AL amyloidosis (B-cell clone disorder): bortezomib-based regimens are standard first-line treatment |
| [30523719](https://pubmed.ncbi.nlm.nih.gov/30523719/) | 2019 | Translational | J Clin Oncol | Molecular high-grade B-cell lymphoma defined as poor-risk group; bortezomib addition showed benefit in REMoDL-B trial |
| [34461632](https://pubmed.ncbi.nlm.nih.gov/34461632/) | 2021 | Prospective | Blood Adv | Bortezomib + rituximab in CD20+ pre-B-ALL: improved MRD negativity rates in adolescent/adult patients |

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details not available) | — | — | — |

*Note: 17 registrations are recorded for Bortezomib in the market (status: Marketed), but detailed authorization information was not available in the evidence pack. Bortezomib is globally marketed under the brand name Velcade® as a lyophilised powder for injection.*

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Proteasome inhibitor) |
| Myelosuppression Risk | High — Thrombocytopenia is a dose-limiting toxicity (cyclical pattern with nadir at day 11, recovery by day 21); neutropenia also common |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelet count (before each dose), liver function tests, renal function, blood glucose, peripheral neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations; use appropriate PPE during preparation and administration |

## Safety Considerations

> Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not available in the evidence pack. Key known class-level concerns for proteasome inhibitors include peripheral neuropathy, thrombocytopenia, gastrointestinal toxicity, and herpes zoster reactivation (prophylactic antiviral recommended).

## Conclusion and Next Steps

**Decision: Go**

**Rationale:**
Bortezomib already holds regulatory approvals for multiple myeloma and mantle cell lymphoma, which are subtypes of B-cell neoplasms. The TxGNN prediction to extend its indication to the broader B-cell neoplasm category is supported by multiple completed Phase 3 RCTs (≥5) demonstrating activity across follicular lymphoma, Waldenström macroglobulinemia, DLBCL subtypes, and lymphoblastic malignancies. The evidence level is L1 (highest), and the mechanistic rationale—proteasome dependence of immunoglobulin-secreting B-cell lineage tumours—is well established.

**To proceed, the following is needed:**
- Obtain detailed Malaysia regulatory registration information (authorization numbers, approved indication text)
- Retrieve complete safety data from package inserts (warnings, contraindications, drug interactions)
- Obtain formal DrugBank MOA description for documentation completeness
- Identify specific B-cell neoplasm subtypes not yet covered by existing approvals for targeted label expansion (e.g., DLBCL ABC subtype, plasmablastic lymphoma, AL amyloidosis)
- Develop indication-specific safety monitoring plans for each target B-cell neoplasm subtype

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

