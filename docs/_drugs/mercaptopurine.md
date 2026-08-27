---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Chemotherapy Backbone Agent to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Mercaptopurine is a thiopurine antimetabolite long used as a chemotherapy backbone agent, though the specific original indication text is not available in the current NPRA registry extract. The TxGNN model's top prediction — **Acute Lymphoblastic Leukemia (ALL)** — is notable because mercaptopurine is already a well-established maintenance-therapy component for ALL, so this result is best read as a **confirmation of known clinical use** rather than a novel repurposing signal, supported by **50 clinical trials** and **20 publications** in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current NPRA license extract (registration text field is blank) |
| Predicted New Indication | Acute Lymphoblastic Leukemia (ALL) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known pharmacology, mercaptopurine is a thiopurine antimetabolite: after intracellular activation to thioguanine nucleotides, it is incorporated into DNA/RNA and inhibits de novo purine synthesis, producing cytotoxic and antiproliferative effects in rapidly dividing cells — the classic basis for its use in hematologic malignancies.

Importantly, the "predicted" indication here — acute lymphoblastic leukemia — overlaps substantially with mercaptopurine's already-established clinical role. The clinical trial and literature evidence retrieved for this candidate consists largely of ALL maintenance-therapy protocols (e.g., BFM, AIEOP, COG regimens) in which 6-mercaptopurine is a standard combination-chemotherapy component, alongside a large body of pharmacogenomic literature (TPMT/NUDT15) on dosing and toxicity in ALL patients. This pattern indicates the model is reinforcing a well-documented existing indication rather than identifying a genuinely new therapeutic use.

Because the local (NPRA) registered indication text is not populated in this evidence pack, it cannot be confirmed whether the Malaysia label already covers ALL. This should be resolved before treating the prediction as "new."

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6136 | International collaborative combination-chemotherapy protocol for children/adolescents with ALL |
| [NCT02883049](https://clinicaltrials.gov/study/NCT02883049) | Phase 3 | Active, not recruiting | 5949 | Newly diagnosed high-risk B-ALL, dasatinib added for Ph-like TKI-sensitive mutations |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9350 | Risk-adapted chemotherapy regimens in newly diagnosed standard-risk B-ALL/B-LLy |
| [NCT00816049](https://clinicaltrials.gov/study/NCT00816049) | Phase 3 | Completed | 775 | Nordic (NOPHO) protocol evaluating individualized 6-MP dosing during consolidation |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | Completed | 600 | Total Therapy XVI: PEG-asparaginase dosing in newly diagnosed ALL |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Calaspargase pegol vs pegaspargase combination chemotherapy in high-risk ALL |
| [NCT02042690](https://clinicaltrials.gov/study/NCT02042690) | Phase 3 | Completed | 131 | Haplo-identical HSCT vs chemotherapy in first remission, standard-risk adult ALL |
| [NCT02143414](https://clinicaltrials.gov/study/NCT02143414) | Phase 2 | Active, not recruiting | 53 | Blinatumomab + POMP (incl. 6-MP) in older Ph- ALL patients |
| [NCT03022747](https://clinicaltrials.gov/study/NCT03022747) | Phase 2 | Unknown | 60 | Allopurinol added to 6-MP/methotrexate maintenance to optimize thiopurine metabolites |
| [NCT01906671](https://clinicaltrials.gov/study/NCT01906671) | Phase 4 | Unknown | 16 | Plasma kinetics of tablet vs. liquid 6-mercaptopurine formulations in childhood ALL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38230823](https://pubmed.ncbi.nlm.nih.gov/38230823/) | 2024 | Pharmacogenomic study | J Natl Cancer Inst | Additive effects of TPMT and NUDT15 variants on thiopurine-induced myelosuppression in ALL across multiethnic populations |
| [37550838](https://pubmed.ncbi.nlm.nih.gov/37550838/) | 2023 | Clinical pharmacology study | Clin Pharmacol Ther | Mercaptopurine metabolite levels linked to outcome in AIEOP-BFM ALL 2009 protocol |
| [35157496](https://pubmed.ncbi.nlm.nih.gov/35157496/) | 2022 | Phase 2 trial | J Clin Oncol | SWOG 1318: blinatumomab followed by POMP (incl. 6-MP) maintenance in older Ph- B-ALL |
| [29352703](https://pubmed.ncbi.nlm.nih.gov/29352703/) | 2018 | Phase 2, single-arm | Lancet Oncol | Inotuzumab ozogamicin + low-intensity chemotherapy in older Ph- ALL patients |
| [36279879](https://pubmed.ncbi.nlm.nih.gov/36279879/) | 2022 | Phase 2, single-arm | Lancet Haematol | Hyper-CVAD + sequential blinatumomab in newly diagnosed Ph- B-ALL |
| [35501736](https://pubmed.ncbi.nlm.nih.gov/35501736/) | 2022 | RCT protocol | BMC Cancer | TEAM trial: adding low-dose 6-thioguanine to 6-MP/methotrexate maintenance in ALL |
| [25624441](https://pubmed.ncbi.nlm.nih.gov/25624441/) | 2015 | GWAS | J Clin Oncol | Inherited NUDT15 variant identified as genetic determinant of mercaptopurine intolerance in ALL |
| [33750748](https://pubmed.ncbi.nlm.nih.gov/33750748/) | 2021 | Review | J Pediatr Hematol Oncol | Allopurinol used to prevent mercaptopurine adverse effects in ALL patients |
| [10653870](https://pubmed.ncbi.nlm.nih.gov/10653870/) | 2000 | Cohort study | J Clin Oncol | Hyper-CVAD dose-intensive regimen results in adult ALL |
| [29364809](https://pubmed.ncbi.nlm.nih.gov/29364809/) | 2017 | Review | Bol Med Hosp Infant Mex | Genomic perspective on ALL, including pharmacogenomic treatment considerations |

---

## Malaysia Market Information

One NPRA registration is on record (market status: Marketed), but the license detail fields (registration number, product name, dosage form, and approved indication text) are not populated in the current data extract. These details need to be retrieved directly from the NPRA registry before market-status claims can be finalized.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine antimetabolite / thiopurine class) |
| Myelosuppression Risk | High — extensive literature (TPMT/NUDT15 studies) documents dose-dependent hematotoxicity as the dominant adverse effect |
| Emetogenicity Classification | Low (oral thiopurine, minimal emetogenic potential) |
| Monitoring Items | CBC with differential, liver function tests, renal function; TPMT/NUDT15 genotyping or phenotyping recommended before/during therapy given documented toxicity risk |
| Handling Protection | Yes — standard cytotoxic drug handling precautions required |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack (DG001, Blocking severity) — this must be resolved from the TFDA/NPRA label before any safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Trial and literature evidence for the ALL indication is strong (L1), but a Blocking data gap (DG001: missing package-insert warnings/contraindications) prevents even an initial safety assessment. In addition, since mercaptopurine is already established for leukemia treatment, this candidate should first be confirmed as genuinely novel versus already-labeled use before further action.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — resolve DG001 before any safety review
- DrugBank mechanism-of-action data — resolve DG002
- Confirmation of the actual NPRA-approved indication text for the registered Malaysia product, to determine whether ALL is already a labeled use
- Drug interaction (DDI) data, currently returning no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

