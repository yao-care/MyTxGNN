---
layout: default
title: Danazol
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Danazol
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

# Danazol: From Endometriosis to Breast Fibrocystic Disease

## One-Sentence Summary

Danazol is a synthetic androgen-derivative steroid historically approved (in other jurisdictions) for endometriosis and hereditary angioedema. The TxGNN model predicts it may also be effective for **Breast Fibrocystic Disease**, with **4 clinical trials** and **19 publications** currently identified, several of them decades-old danazol-specific studies already showing clinical benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Malaysia NPRA license data on file (per literature in this evidence pack — PMID 39051650 — danazol is historically indicated for endometriosis and hereditary angioedema) |
| Predicted New Indication | Breast Fibrocystic Disease |
| TxGNN Prediction Score | 99.9996% (rank 28) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is not available (data gap DG002). Based on the mechanistic evidence collected for this candidate, danazol is a weak androgen ("impeded androgen") that suppresses pituitary LH/FSH secretion and binds directly to steroid receptors in breast tissue, reducing estrogen-driven stimulation of fibroglandular breast tissue.

Notably, this is not a purely novel repurposing hypothesis: literature within this evidence pack (PMID 39051650, PMID 7041729) explicitly states that danazol has, in some jurisdictions, already been approved for "benign fibrocystic breast disease" alongside endometriosis and hereditary angioedema. This means the TxGNN prediction is corroborated by decades of published clinical experience rather than being a purely mechanistic extrapolation — several dose-ranging and comparative studies from the 1979–1989 period (e.g., PMID 3074777, PMID 6594009, PMID 7386553) directly tested danazol in fibrocystic/mammary dysplasia patients with positive results on pain, tenderness, and nodularity.

The main gap is Malaysia-specific: current NPRA licensing data does not confirm whether the locally registered product's approved indication text already includes fibrocystic breast disease, and detailed MOA/safety data has not yet been retrieved.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00744276](https://clinicaltrials.gov/study/NCT00744276) | Phase 2 | Completed | 60 | RCT of topically applied danazol (FP1198) vs. placebo for pain in fibrocystic breast disease; dose-ranging design, same indication as predicted but topical (not oral) route. |
| [NCT04873102](https://clinicaltrials.gov/study/NCT04873102) | Phase 2 | Recruiting | 10 | Oral danazol 600 mg/day for cytopenias in cirrhosis — same drug, different indication; provides oral safety/dosing reference only. |
| [NCT01105793](https://clinicaltrials.gov/study/NCT01105793) | Phase 2 | Completed | 20 | Topical FP1198 for cyclic mastalgia — same disease family, but tested drug is not danazol itself. |
| [NCT02002403](https://clinicaltrials.gov/study/NCT02002403) | Phase 2 | Completed | 34 | Low-dose oral Optina (formerly Danazol/DMI-5207) for diabetic macular edema — same molecule, unrelated indication. |

Note: none of the identified trials are a direct, currently-registered oral-danazol RCT in fibrocystic breast disease; the strongest direct RCT evidence for this indication comes from older published literature (see below) rather than the ClinicalTrials.gov registry.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3074777](https://pubmed.ncbi.nlm.nih.gov/3074777/) | 1988 | RCT | Aust N Z J Obstet Gynaecol | Prospective randomized double-blind trial, danazol 200 mg BID in 80 women with symptomatic benign mammary dysplasia; significant improvement in pain, tenderness, and nodularity. |
| [6594009](https://pubmed.ncbi.nlm.nih.gov/6594009/) | 1984 | Cohort | Acta Obstet Gynecol Scand Suppl | Long-term follow-up (Hjørring project) of danazol treatment in severely symptomatic fibrocystic breast disease with mastodynia. |
| [7386553](https://pubmed.ncbi.nlm.nih.gov/7386553/) | 1980 | Clinical study | Am J Obstet Gynecol | Danazol 100–400 mg/day across 3 dose groups in 130 women with benign breast disease; nodularity eliminated in ~2/3 of patients. |
| [395520](https://pubmed.ncbi.nlm.nih.gov/395520/) | 1979 | Case series | Postgrad Med J | Clinical description and danazol treatment outcomes in fibrocystic breast disease. |
| [2264418](https://pubmed.ncbi.nlm.nih.gov/2264418/) | 1990 | Review | Zentralblatt für Gynäkologie | Diagnosis and therapy of fibrocystic breast disease, including danazol as a treatment option. |
| [7041729](https://pubmed.ncbi.nlm.nih.gov/7041729/) | 1982 | Review | Ann Intern Med | Notes danazol's approval progression from endometriosis to cystic disease of the breast; broad review of mechanisms and indications. |
| [3314435](https://pubmed.ncbi.nlm.nih.gov/3314435/) | 1987 | Review | Am Fam Physician | General management of fibrocystic breast disease, including danazol as a symptom-alleviating option. |
| [3511705](https://pubmed.ncbi.nlm.nih.gov/3511705/) | 1986 | Review | Am J Obstet Gynecol | Pathophysiology, pathomorphology, and clinical management of fibrocystic breast disease. |
| [28649033](https://pubmed.ncbi.nlm.nih.gov/28649033/) | 2017 | Preclinical/in vitro | Breast (Edinburgh) | Mechanistic study showing danazol alters mitochondrial metabolism in fibrocystic breast (MCF10A) cells. |
| [16444894](https://pubmed.ncbi.nlm.nih.gov/16444894/) | 2005 | Review | J Reprod Med | Review of mastalgia management, including danazol among effective pharmacologic options. |

---

## Malaysia Market Information

NPRA registration records confirm **3 active licenses** for Danazol in Malaysia (market status: Marketed), but detailed license numbers, product names, dosage forms, and approved-indication text have not yet been retrieved/parsed (blocking data gap DG001 — TFDA/NPRA package insert needs to be downloaded and parsed).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data have not yet been retrieved for this candidate (DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Danazol's efficacy in fibrocystic breast disease is supported by multiple decades-old dose-ranging and cohort studies (including one prospective double-blind RCT), and the indication is already historically recognized alongside danazol's core approvals for endometriosis and hereditary angioedema. However, no current registered oral-danazol RCT and no Malaysia-specific safety/labeling data are yet available, so this cannot advance without guardrails.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, contraindications, and DDI data (DG001, blocking)
- DrugBank mechanism-of-action confirmation (DG002)
- Confirmation of whether existing Malaysia-registered Danazol products already carry a fibrocystic breast disease indication, and their exact license details
- Assessment of route compatibility (available local formulations are oral; supporting RCT evidence above is largely oral-dose based, while the most recent registered trial, NCT00744276, used a topical formulation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

