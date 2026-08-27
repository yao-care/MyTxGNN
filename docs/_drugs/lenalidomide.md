---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 5
---

# Lenalidomide
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

# Lenalidomide: From Multiple Myeloma to Mantle Cell Lymphoma

## One-Sentence Summary

Lenalidomide is an oral immunomodulatory drug (IMiD) originally developed for multiple myeloma and myelodysplastic syndrome with deletion 5q (del5q). The TxGNN model's top-ranked prediction identifies **Mantle Cell Lymphoma** as a candidate new indication, backed by **50 clinical trials** and **20 publications** in this evidence pack — though this is already a globally approved indication for lenalidomide in several markets, which is important context for the Malaysia-specific evaluation below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Myeloma / Myelodysplastic Syndrome with del(5q) (per literature evidence in this pack; NPRA license indication text was not resolved — see Malaysia Market Information) |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 0.00% (score field returned 0.0 in the evidence pack — likely a data/pipeline gap, not a true near-zero prediction; flagged for verification) |
| Evidence Level | L2 (1 completed Phase 3 RCT — NCT01865110 — plus multiple completed Phase 2 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 26 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action text was not available in this evidence pack (drug-level data gap, DG002). Based on the literature evidence collected here, Lenalidomide acts by binding cereblon (CRBN), a substrate receptor of the CRL4 E3 ubiquitin ligase complex, redirecting it to ubiquitinate and degrade the transcription factors IKZF1 and IKZF3 in multiple myeloma cells (PMID 24292625, 24292623), and CK1α in del(5q) MDS cells (PMID 26131937). This cereblon-mediated protein degradation underlies both its direct anti-tumour and immunomodulatory (T-cell costimulatory, NK-cell activating, anti-angiogenic) effects.

Mantle cell lymphoma, like multiple myeloma and MDS, is a clonal haematologic/lymphoid malignancy, and lenalidomide's immunomodulatory and cereblon-dependent mechanisms are not tumour-type restricted — they have shown activity across a broad range of B-cell neoplasms. Consistent with this, several trial summaries in this pack (e.g. NCT00609869, NCT02341781) explicitly state that Revlimid® is "approved by the Food and Drug Administration (FDA) for the treatment" of relapsed/refractory MCL after bortezomib failure, and lenalidomide plus rituximab (R2) is a recognised chemotherapy-free regimen for both untreated and relapsed MCL.

This is an important nuance for interpretation: MCL (along with MM and MDS del5q) already appears to be an internationally approved indication for lenalidomide, not a mechanistically novel repurposing candidate. The TxGNN "prediction" here most plausibly reflects a **Malaysia label/registration gap** rather than a new biological hypothesis — which should shape the regulatory next steps below.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01865110](https://clinicaltrials.gov/study/NCT01865110) | Phase 3 | Completed | 623 | R-CHOP+R-HAD vs R-CHOP induction, followed by lenalidomide+rituximab vs rituximab-alone maintenance in older MCL patients |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Phase 3 | Recruiting | 182 | Glofitamab monotherapy vs investigator's choice (incl. lenalidomide+rituximab) in R/R MCL |
| [NCT01021423](https://clinicaltrials.gov/study/NCT01021423) | Phase 3 | Terminated | 9 | Lenalidomide maintenance after first-line chemotherapy in MCL (stopped early, design no longer relevant) |
| [NCT00737529](https://clinicaltrials.gov/study/NCT00737529) | Phase 2 | Completed | 134 | Single-agent lenalidomide in MCL relapsed/refractory to bortezomib — basis for FDA approval in this setting |
| [NCT01472562](https://clinicaltrials.gov/study/NCT01472562) | Phase 2 | Completed | 38 | First-line lenalidomide + rituximab in previously untreated MCL |
| [NCT02460276](https://clinicaltrials.gov/study/NCT02460276) | Phase 2 | Completed | 50 | Ibrutinib + lenalidomide + rituximab in R/R MCL |
| [NCT03863184](https://clinicaltrials.gov/study/NCT03863184) | Phase 2 | Active, not recruiting | 37 | Acalabrutinib + lenalidomide + rituximab/obinutuzumab in previously untreated MCL |
| [NCT01737177](https://clinicaltrials.gov/study/NCT01737177) | Phase 2 | Completed | 42 | Bendamustine + lenalidomide + rituximab (R2-B) as second-line therapy for first relapsed/refractory MCL |
| [NCT02633137](https://clinicaltrials.gov/study/NCT02633137) | Phase 2 | Completed | 49 | Sequential chemotherapy + lenalidomide-RCHOP, followed by lenalidomide-rituximab maintenance in untreated MCL |
| [NCT03647124](https://clinicaltrials.gov/study/NCT03647124) | N/A | Completed | 105 | Post-authorization safety study characterizing lenalidomide-associated tumor flare reaction and high tumor burden in R/R MCL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40104044](https://pubmed.ncbi.nlm.nih.gov/40104044/) | 2025 | Trial follow-up | HemaSphere | Long-term outcomes of ibrutinib+lenalidomide+rituximab (Nordic MCL6 Philemon phase 2 trial) in relapsed MCL |
| [36257914](https://pubmed.ncbi.nlm.nih.gov/36257914/) | 2023 | Retrospective/observational | British Journal of Haematology | SCHOLAR-2 real-world chart review of R/R MCL after BTK-inhibitor failure across Europe (n=240) |
| [30608891](https://pubmed.ncbi.nlm.nih.gov/30608891/) | 2019 | Review | Expert Opinion on Pharmacotherapy | Overview of lenalidomide efficacy in MCL, monotherapy and chemo-free combinations |
| [24883181](https://pubmed.ncbi.nlm.nih.gov/24883181/) | 2014 | Review | Therapeutic Advances in Hematology | Overview of lenalidomide in relapsed/refractory MCL; notes FDA approval for MDS and relapsed MM |
| [25952533](https://pubmed.ncbi.nlm.nih.gov/25952533/) | 2015 | Review | Expert Review of Hematology | Lenalidomide mechanisms and approval status in relapsed MCL after ≥2 prior lines including bortezomib |
| [26755518](https://pubmed.ncbi.nlm.nih.gov/26755518/) | 2016 | Review | Journal of Clinical Oncology | Comprehensive review of MCL biology and treatment landscape |
| [38906740](https://pubmed.ncbi.nlm.nih.gov/38906740/) | 2024 | Review | Blood Reviews | Current management of relapsed/refractory MCL in the BTK-inhibitor era |
| [32552760](https://pubmed.ncbi.nlm.nih.gov/32552760/) | 2020 | Review | Journal of Hematology & Oncology | Emerging therapies in MCL, including IMiD-based combinations |
| [35639332](https://pubmed.ncbi.nlm.nih.gov/35639332/) | 2022 | Review | Current Oncology Reports | Risk-adapted therapy and management of relapsed MCL |
| [26297281](https://pubmed.ncbi.nlm.nih.gov/26297281/) | 2015 | Safety review | Clinical Lymphoma, Myeloma & Leukemia | Practical management of lenalidomide-related rash; notes hematologic toxicity as most common cause of dose interruption/discontinuation across MDS/MM/MCL |

## Malaysia Market Information

NPRA registration data confirms Lenalidomide is **marketed in Malaysia with 26 active registrations**, but the individual license records provided in this evidence pack (license numbers, product names, dosage forms, approved indication text) were all returned empty and could not be resolved. A separate data pull from the NPRA product register is needed to confirm the exact approved indication wording and dosage forms currently on the Malaysia label before this can be compared against the predicted MCL indication.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/immunomodulatory therapy (IMiD class — cereblon E3 ubiquitin ligase modulator), not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are consistently reported as the most common Grade ≥3 toxicities and the leading cause of dose interruption/discontinuation across MM, MDS, and MCL trials in this evidence pack (PMID 26297281) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (frequent, especially early cycles), renal function (dose adjustment by CrCl), thyroid function, VTE risk assessment |
| Handling Protection | Special handling required due to teratogenicity (thalidomide analogue) — dispensing must follow a pregnancy prevention/REMS-equivalent program; many institutions also apply hazardous-drug handling precautions given its cereblon-mediated cytotoxic activity |

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack's key warnings, contraindications, and drug interaction data are all marked as unresolved (query DG001 — TFDA/NPRA label warnings and contraindications — is flagged Blocking severity, meaning safety screening could not be completed from available data).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Global clinical evidence for lenalidomide in MCL is strong (L2, including a completed Phase 3 RCT and multiple completed Phase 2 RCTs, plus an FDA-approved indication abroad), but the Blocking-severity data gap (DG001 — no NPRA label warnings/contraindications available) means safety screening (S1) cannot be completed, and the current scope of the Malaysia label for lenalidomide has not been confirmed.

**To proceed, the following is needed:**
- NPRA package insert (warnings, contraindications, REMS/pregnancy-prevention program details) — resolves DG001
- Confirmed mechanism-of-action documentation from DrugBank — resolves DG002
- Confirmation of whether MCL (and MM/MDS del5q) are already within the current Malaysia-approved label, since this candidate may represent a label-alignment gap rather than a genuinely novel repurposing
- Drug-drug interaction data (current query returned no results)
- Resolved NPRA license records (product names, dosage forms, indication text) to complete the market information table
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

