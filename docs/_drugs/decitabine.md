---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 5
---

# Decitabine
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

# Decitabine: From Myelodysplastic Syndrome to Therapy-Related Acute Myeloid Leukemia and Myelodysplastic Syndrome

## One-Sentence Summary

Decitabine (DrugBank DB01262) is a DNA hypomethylating agent long used for myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML). The TxGNN model's top-ranked candidate points to **Therapy-Related Acute Myeloid Leukemia and Myelodysplastic Syndrome (t-AML/MDS)** — a secondary disease subtype arising after prior cytotoxic treatment — supported by roughly **50 clinical trials** and **20 publications** in the evidence pack, though most of these studied decitabine in MDS/AML broadly rather than the therapy-related subtype specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Malaysia registry data provided (all license fields are blank); decitabine is generally known as a hypomethylating agent indicated for myelodysplastic syndrome (MDS) / acute myeloid leukemia (AML) |
| Predicted New Indication | Therapy-Related Acute Myeloid Leukemia and Myelodysplastic Syndrome |
| TxGNN Prediction Score | 0.00% (score field returned 0.0 for all 5 ranked candidates — likely a data population issue in this evidence pack rather than a genuine near-zero prediction) |
| Evidence Level | L1 (with caveat — see below) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, decitabine is a nucleoside analogue that inhibits DNA methyltransferase 1 (DNMT1), reversing aberrant hypermethylation and reactivating silenced tumor-suppressor genes in myeloid blasts. Its efficacy in MDS and AML is well established, and this mechanism is not disease-etiology specific — it targets the epigenetic dysregulation common to myeloid neoplasms regardless of whether they arose de novo or secondary to prior chemotherapy/radiation exposure.

Therapy-related AML/MDS (t-AML/MDS) is a recognized secondary malignancy that develops after prior cytotoxic therapy (e.g., alkylating agents, topoisomerase II inhibitors) for an earlier cancer. Pathologically and molecularly it overlaps heavily with de novo MDS/AML, often sharing high-risk cytogenetic features. Because decitabine's hypomethylating activity is not restricted by disease origin, it is mechanistically plausible that its established benefit in MDS/AML extends to the therapy-related subtype — several items in the evidence pack (e.g., PMID 19090005, PMID 35172484) describe decitabine already being used clinically in exactly this secondary-disease setting.

An important caveat: the clinical trials and literature retrieved for this candidate are overwhelmingly trials of decitabine in **MDS/AML in general**, not trials restricted specifically to the therapy-related subtype. This prediction should therefore be read as reinforcing decitabine's role across the broader MDS/AML spectrum (which includes t-AML/MDS as a recognized subset) rather than as evidence for a wholly novel disease area.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03306264](https://clinicaltrials.gov/study/NCT03306264) | Phase 3 | Completed | 227 | Crossover PK/efficacy study of oral decitabine+cedazuridine (ASTX727) vs IV decitabine in MDS, CMML and AML |
| [NCT02907359](https://clinicaltrials.gov/study/NCT02907359) | Phase 3 | Completed | 417 | Guadecitabine vs treatment choice in MDS/CMML after prior azacitidine or decitabine failure |
| [NCT01928537](https://clinicaltrials.gov/study/NCT01928537) | Phase 3 | Completed | 67 | IV rigosertib vs standard care in MDS with excess blasts progressing after azacitidine/decitabine |
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Phase 3 | Completed | 727 | Decitabine maintenance vs observation following induction in AML patients aged ≥60 |
| [NCT00416598](https://clinicaltrials.gov/study/NCT00416598) | Phase 2 | Completed | 546 | Decitabine as maintenance therapy after standard induction in previously untreated AML (<60y) |
| [NCT04655755](https://clinicaltrials.gov/study/NCT04655755) | Phase 1/2 | Active, not recruiting | 52 | Venetoclax + oral decitabine/cedazuridine (ASTX727) in treatment-naïve high-risk MDS/CMML |
| [NCT03404193](https://clinicaltrials.gov/study/NCT03404193) | Phase 2 | Active, not recruiting | 235 | Venetoclax + 10-day decitabine in newly diagnosed elderly/relapsed AML and high-risk MDS |
| [NCT06129734](https://clinicaltrials.gov/study/NCT06129734) | Phase 1/2 | Recruiting | 20 | Weekly low-dose decitabine + venetoclax as post-allogeneic-transplant maintenance in high-risk myeloid malignancy |
| [NCT00903422](https://clinicaltrials.gov/study/NCT00903422) | Phase 1 | Completed | 98 | Eltrombopag for thrombocytopenia in advanced MDS/secondary AML after MDS, relapsed/refractory to decitabine and others |
| [NCT01130506](https://clinicaltrials.gov/study/NCT01130506) | Phase 1 | Completed | 17 | Decitabine + vorinostat + cytarabine in relapsed/refractory AML or MDS |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38135371](https://pubmed.ncbi.nlm.nih.gov/38135371/) | 2024 | Phase 3 RCT | Lancet Haematol | ASCERTAIN trial: oral decitabine-cedazuridine shows PK/safety equivalence to IV decitabine in MDS/CMML |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | Lancet Haematol | G-CSF + decitabine + Bu/Cy conditioning reduced relapse vs Bu/Cy alone in MDS/secondary AML pre-transplant |
| [38452788](https://pubmed.ncbi.nlm.nih.gov/38452788/) | 2024 | Phase 2 | Lancet Haematol | Oral decitabine-cedazuridine + venetoclax effective and safe in older/unfit AML |
| [40784355](https://pubmed.ncbi.nlm.nih.gov/40784355/) | 2025 | Phase 2 | Lancet Haematol | Oral decitabine-cedazuridine as post-HSCT maintenance reduced relapse in very high-risk AML/MDS |
| [38316133](https://pubmed.ncbi.nlm.nih.gov/38316133/) | 2024 | Phase 1/2 | Lancet Haematol | Oral decitabine-cedazuridine + venetoclax active and safe in higher-risk MDS/CMML |
| [26365212](https://pubmed.ncbi.nlm.nih.gov/26365212/) | 2016 | Phase 2 | Leukemia | Decitabine + gemtuzumab ozogamicin in newly diagnosed and relapsed AML/high-risk MDS |
| [36964818](https://pubmed.ncbi.nlm.nih.gov/36964818/) | 2023 | Systematic review / meta-analysis | Clin Exp Med | Network meta-analysis of epigenetic agents (including decitabine) for older AML/MDS patients |
| [37470508](https://pubmed.ncbi.nlm.nih.gov/37470508/) | 2023 | Review | Expert Rev Anticancer Ther | Review of the shift toward oral hypomethylating agent therapy in MDS/AML |
| [19090005](https://pubmed.ncbi.nlm.nih.gov/19090005/) | 2009 | Case series | Cancer | Therapy-related AML/MDS occurring in ALL patients previously treated with hyper-CVAD regimens |
| [35172484](https://pubmed.ncbi.nlm.nih.gov/35172484/) | 2017 | Case report | JCO Precis Oncol | BRAF-mutant, treatment-related AML managed with decitabine before targeted therapy |

## Cytotoxicity

Decitabine is a nucleoside-analogue DNA methyltransferase inhibitor and is classified as an antineoplastic agent used for hematologic malignancies (MDS/AML). Formal DrugBank/NPRA toxicity data were not available in this evidence pack (see Safety Considerations), so the table below is based on general pharmacology and the literature captured above.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — hypomethylating agent / DNA methyltransferase inhibitor (nucleoside analogue class) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia and anemia are well-documented class effects; the evidence pack includes studies specifically on infectious complications during decitabine cycles (e.g., PMID 29058375) and on reduced-toxicity dosing schedules (e.g., PMID 39316768) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, platelet count, renal and hepatic function, infection surveillance |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack flags the absence of NPRA package-insert warnings, contraindications, and drug interaction data as a **Blocking** data gap (DG001), which prevents an initial safety (S1) assessment for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Decitabine has strong mechanistic and clinical-trial support across the broader MDS/AML disease spectrum, of which therapy-related AML/MDS is a recognized subtype — but a **Blocking** data gap (missing NPRA warnings/contraindications, DG001) prevents completion of even an initial safety review, so no advancement decision can be made yet.

**To proceed, the following is needed:**
- NPRA package insert (warnings, contraindications) — download and parse per DG001 remediation
- DrugBank mechanism-of-action data to formally support the mechanistic rationale (DG002)
- Malaysia-specific approved indication text and license details (currently blank across all 6 registrations)
- Confirmation of whether existing trial/literature evidence specifically addresses the therapy-related AML/MDS subtype, versus general MDS/AML populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

