---
layout: default
title: Glutamic Acid
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 4
---

# Glutamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Glutamic Acid: From Unspecified Marketed Use to Postmenopausal Osteoporosis

## One-Sentence Summary

Glutamic acid (DrugBank DB00142) is marketed in Malaysia under 29 registrations, though the original approved indication text was not captured in current regulatory data. The TxGNN model predicts potential efficacy for **postmenopausal osteoporosis**, but this is currently supported by only **1 clinical trial** (low relevance — the trial tests ibandronate, not glutamic acid) and **11 publications**, of which only one directly studies glutamic acid itself (an animal study).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available regulatory records (indication text not captured for any of the 29 Malaysia licenses) |
| Predicted New Indication | Postmenopausal Osteoporosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 29 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a data gap). Based on the evidence collected, glutamic acid is a component of the glutamate receptor signaling pathway. An animal study (ovariectomized mice) found that glutamic acid ameliorated estrogen-deficiency-induced menopausal-like symptoms, including some bone-metabolism-related indicators — this is the only evidence directly testing glutamic acid itself.

Beyond that direct animal signal, the supporting literature largely involves related-but-distinct compounds: poly-γ-glutamic acid (a structurally different polymer) improved calcium absorption in a small human study of postmenopausal women, and several RCTs on vitamin K2/D3 reference "bone glutamic acid residues" only insofar as vitamin K enables their γ-carboxylation — these trials do not test glutamic acid as an intervention.

Given the absence of any human RCT or observational study using glutamic acid itself as the intervention for bone density or fracture outcomes, the mechanistic link to postmenopausal osteoporosis is biologically plausible but indirect, and the current evidence base does not yet support advancement past preclinical/mechanistic status.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048061](https://clinicaltrials.gov/study/NCT00048061) | Phase 3 | Completed | 1,609 | Compared monthly oral ibandronate (100mg/150mg) vs. daily 2.5mg ibandronate, with vitamin D and calcium supplementation, in postmenopausal osteoporosis. **Note:** this trial tests ibandronate, not glutamic acid — flagged as low relevance (Grade C), included only because TxGNN co-occurrence linked it to this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26144993](https://pubmed.ncbi.nlm.nih.gov/26144993/) | 2015 | Animal study | Nutrition Research | Glutamic acid ameliorated estrogen-deficiency-induced menopausal-like symptoms in ovariectomized mice — the only study directly testing glutamic acid for this indication |
| [18187428](https://pubmed.ncbi.nlm.nih.gov/18187428/) | 2007 | Small human intervention | J Am Coll Nutr | Poly-γ-glutamic acid (a related polymer, not glutamic acid itself) acutely increased calcium absorption in postmenopausal women |
| [14529146](https://pubmed.ncbi.nlm.nih.gov/14529146/) | 2003 | RCT (vitamin D3/K2) | Keio Journal of Medicine | Vitamin D3/K2 sustains lumbar BMD and prevents fractures; vitamin K2 enhances γ-carboxylation of bone glutamic acid residues — mechanistic mention only, not a glutamic acid intervention |
| [14584089](https://pubmed.ncbi.nlm.nih.gov/14584089/) | 2003 | RCT (vitamin K2 + bisphosphonate) | Yonsei Medical Journal | Vitamin K2 enhances γ-carboxylation of bone glutamic acid residues; combined with bisphosphonates for BMD/fracture prevention — indirect mechanistic reference |
| [19172219](https://pubmed.ncbi.nlm.nih.gov/19172219/) | 2009 | RCT (menatetrenone) | J Bone Miner Metab | Menatetrenone (vitamin K2) increased γ-carboxylation of osteocalcin vs. calcium aspartate control — not a glutamic acid intervention |
| [29437025](https://pubmed.ncbi.nlm.nih.gov/29437025/) | 2018 | Cohort (genetic) | Endocrine, Metabolic & Immune Disorders Drug Targets | VKORC1 polymorphism associated with osteoporosis risk via vitamin K-dependent γ-carboxylation pathway |
| [18414001](https://pubmed.ncbi.nlm.nih.gov/18414001/) | 2008 | Genetic/genomic | Molecules and Cells | SLC22A11 (hOAT4) SNP characterization in Korean postmenopausal osteoporosis patients — not a glutamic acid study |
| [39698319](https://pubmed.ncbi.nlm.nih.gov/39698319/) | 2024 | Preclinical | Frontiers in Cellular and Infection Microbiology | Traditional Chinese medicine ointment (not glutamic acid) modulated gut microbiota-bone metabolism axis in postmenopausal osteoporosis model |
| [34529430](https://pubmed.ncbi.nlm.nih.gov/34529430/) | 2021 | Preclinical | Nano Letters | Bone-targeted polymer vesicle (using a glutamic acid-containing polymer backbone) for estradiol delivery in osteoporosis therapy |
| [11668761](https://pubmed.ncbi.nlm.nih.gov/11668761/) | 2001 | Review | Tidsskrift for den Norske Legeforening | General review of vitamin K in Norwegian diet and osteoporosis — not related to glutamic acid |

---

## Malaysia Market Information

Detailed license-level data (license number, product name, dosage form, approved indication text) was not captured for this drug — all 5 sampled license records returned empty fields. The regulatory database records **29 total registrations** with market status "已上市" (Marketed), but no structured product-level detail is currently available.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Warning/contraindication data (TFDA/NPRA package insert) is flagged as a **Blocking** data gap (DG001) — this prevents completion of the S1 safety pre-screen for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence Level L4 reflects predominantly preclinical/mechanistic support — only one animal study directly tests glutamic acid for this indication, and the single associated clinical trial actually evaluates a different drug (ibandronate). Combined with a Blocking data gap on TFDA/NPRA safety warnings and contraindications, the candidate cannot yet advance past initial screening.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, contraindications, and DDI data (currently blocking S1 safety pre-screen)
- Confirmed mechanism of action from DrugBank
- Original approved indication text for the 29 Malaysia licenses (currently blank)
- Direct human interventional evidence (RCT or controlled study) testing glutamic acid itself — not vitamin K/D analogs or structurally distinct polymers — for bone density or fracture outcomes in postmenopausal osteoporosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

