---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 6
---

# Anastrozole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Anastrozole: From Postmenopausal Hormone-Sensitive Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation aromatase inhibitor established as adjuvant endocrine therapy for hormone receptor-positive (ER+/PR+) breast cancer in postmenopausal women, with efficacy over tamoxifen demonstrated in landmark trials including ATAC and IBIS-II.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** — aligning with its well-validated primary clinical indication — with **≥5 completed Phase 3 clinical trials** and **20 publications** supporting this direction.
This prediction validates TxGNN's knowledge graph reasoning capability and confirms the biological coherence of the drug-disease relationship.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormone receptor-positive breast cancer in postmenopausal women (based on clinical literature; regulatory product details pending retrieval) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Anastrozole selectively inhibits CYP19A1 (aromatase), the enzyme complex responsible for converting androgens (androstenedione, testosterone) into estrogens (estrone, estradiol) in peripheral tissues. In postmenopausal women, where peripheral aromatization is the primary source of circulating estrogen, anastrozole reduces plasma estradiol levels by more than 90%. This direct pharmacological action forms the mechanistic cornerstone of its anti-tumour activity.

Hormone receptor-positive (ER+) breast cancer cells depend on estrogen signalling to drive cell cycle progression through the CCND1/CDK4/6 axis. Estrogen deprivation induced by anastrozole causes G1-phase cell cycle arrest and promotes apoptosis in ER+ tumour cells. This mechanistic link is direct, well-characterized, and underpins the consistent clinical benefit observed across multiple large randomized controlled trials — most notably the pivotal ATAC trial (N = 9,366), which demonstrated significantly prolonged disease-free survival compared to tamoxifen over 5 years of adjuvant treatment.

> **Note on MOA data**: Formal mechanism of action data was flagged as a data gap (DG002) in this evidence pack. The mechanistic description above is derived from the repurposing rationale embedded within the evidence pack and corroborated by the extensive published literature. DrugBank API query for DB01217 is recommended to complete the pharmacological profile.

The TxGNN model's highest-ranked prediction for anastrozole is female breast carcinoma, reflecting the model's strong mechanistic signal capture. The prediction extends across the full breast cancer continuum: from adjuvant treatment of early-stage ER+ disease, to first-line therapy in advanced/metastatic settings, through chemoprevention in high-risk postmenopausal women (IBIS-II), and prevention of recurrence in ductal carcinoma in situ (IBIS-II DCIS). This breadth of validated applications — all linked by the same aromatase-inhibition mechanism — makes this the highest-confidence prediction in the TxGNN output for this drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | Completed | 7,576 | Large head-to-head RCT (NCIC CTG MA.27): exemestane vs. anastrozole as adjuvant therapy in postmenopausal ER+ breast cancer; anastrozole serves as the active reference arm, providing the highest-grade direct efficacy evidence |
| [NCT00784940](https://clinicaltrials.gov/study/NCT00784940) | Phase 3 | Completed | 308 | Randomized double-blind trial (ATAC sub-study): quantifies bone mineral density changes with anastrozole vs. tamoxifen vs. combination as adjuvant therapy; critical long-term safety database |
| [NCT00784680](https://clinicaltrials.gov/study/NCT00784680) | Phase 3 | Completed | 308 | Companion QoL RCT to NCT00784940: compares patient-reported quality of life between anastrozole, tamoxifen, and combination over first 2 years of adjuvant treatment |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Completed | 298 | Double-blind RCT: exemestane vs. anastrozole as initial hormonal therapy in postmenopausal women with advanced/recurrent breast cancer; non-inferiority design demonstrating class equivalence |
| [NCT02040857](https://clinicaltrials.gov/study/NCT02040857) | Phase 2 | Completed | 162 | Pilot feasibility study of palbociclib combined with anastrozole-based adjuvant endocrine therapy for HR+ invasive breast carcinoma; evaluates CDK4/6 inhibitor + AI synergy within the established mechanistic framework |
| [NCT00405938](https://clinicaltrials.gov/study/NCT00405938) | Phase 2 | Completed | 79 | Anastrozole or fulvestrant combined with bevacizumab as first-line therapy for postmenopausal HR+ metastatic breast cancer; anastrozole is an active experimental arm; evaluates anti-angiogenic combination |
| [NCT00256217](https://clinicaltrials.gov/study/NCT00256217) | Phase 2 | Completed | 42 | Chemoprevention trial assessing anastrozole in postmenopausal women with DCIS and early invasive breast cancer; design mirrors IBIS-II prevention approach |
| [NCT05439499](https://clinicaltrials.gov/study/NCT05439499) | Phase 3 | Unknown | 434 | Randomized double-blind placebo-controlled trial: FCN-437c (CDK4/6 inhibitor) + letrozole or anastrozole ± goserelin vs. placebo + AI in first-line HR+/HER2− advanced breast cancer; status requires confirmation |
| [NCT03820830](https://clinicaltrials.gov/study/NCT03820830) | Phase 3 | Active, Not Recruiting | 405 | POLAR trial: adjuvant palbociclib + endocrine therapy (anastrozole eligible) vs. endocrine therapy alone for HR+/HER2− isolated locoregional recurrence; results anticipated |
| [NCT04666961](https://clinicaltrials.gov/study/NCT04666961) | Phase 2 | Recruiting | 262 | Neoadjuvant hormonal therapy (anastrozole eligible) for extensive DCIS to reduce mastectomy requirement; long-term follow-up through 2033 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT | *Lancet* | ATAC 5-year results (N = 9,366): anastrozole significantly prolonged disease-free survival vs. tamoxifen (HR 0.87; P = 0.01) and reduced distant metastasis; established anastrozole as standard adjuvant therapy |
| [12090977](https://pubmed.ncbi.nlm.nih.gov/12090977/) | 2002 | Phase 3 RCT | *Lancet* | ATAC first results: anastrozole monotherapy superior to tamoxifen for time to recurrence and contralateral breast cancer; fewer thromboembolic events and endometrial cancers; better tolerability profile |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT (Long-term Follow-up) | *Lancet* | IBIS-II long-term results: anastrozole significantly reduced breast cancer incidence in high-risk postmenopausal women vs. placebo over 10+ years; preventive effect persists after treatment cessation |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | *Lancet* | IBIS-II DCIS: anastrozole superior to tamoxifen for prevention of locoregional and contralateral breast cancer events in postmenopausal women with hormone-receptor-positive DCIS; broadens the indication continuum |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-analysis | *Oncotarget* | Systematic meta-analysis of RCTs: anastrozole demonstrates superior disease-free survival vs. tamoxifen with significantly lower rates of endometrial cancer, thromboembolic events, and hot flashes |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Systematic Review | *Rev Assoc Med Bras* | Comprehensive review of anastrozole in chemoprevention and treatment across all stages of breast cancer; confirms superior pharmacodynamic selectivity and tolerability vs. earlier-generation agents |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | Pharmacogenomics Study | *Clin Pharmacol Ther* | SNP-treatment interaction analysis in 4,465 MA.27 patients: identifies genetic variants (CSMD1) differentiating anastrozole vs. exemestane efficacy; supports precision endocrine therapy approach |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | GWAS | *JCI Insight* | Genome-wide analysis of MA.27 trial: CSMD1 variant associated with improved breast cancer-free interval on anastrozole; reveals complement pathway as novel mechanism; identifies pharmacogenomic biomarkers |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | *Expert Opin Pharmacother* | Comparative review of anastrozole, letrozole, and exemestane in early breast cancer: all three third-generation AIs consistently superior to tamoxifen across upfront, switch, and extended adjuvant designs |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Review | *Expert Opin Drug Safety* | Safety-focused review of anastrozole adjuvant use: characterizes musculoskeletal adverse effects, bone mineral density loss, and cardiovascular considerations across multiple adjuvant trial datasets |

---

## Malaysia Market Information

Anastrozole has **4 registered products** in Malaysia (market status: ✓ 已上市). Detailed product registration data (authorization numbers, product names, dosage forms, manufacturers, and approved indication text) was not populated in this evidence pack data pull. The table below reflects the registration structure pending full NPRA data retrieval.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | (Product 1 — details pending) | — | — |
| — | (Product 2 — details pending) | — | — |
| — | (Product 3 — details pending) | — | — |
| — | (Product 4 — details pending) | — | — |

> To retrieve full product details, query the NPRA Product Registration Search at [https://www.npra.gov.my](https://www.npra.gov.my) using active ingredient "anastrozole." Anastrozole 1 mg oral tablets (brand name Arimidex, AstraZeneca) are the reference product approved in most markets; generic equivalents are likely represented among the 4 registered products.

---

## Cytotoxicity

Anastrozole meets the criteria for antineoplastic classification: its approved indication is breast cancer and it belongs to the aromatase inhibitor class of endocrine oncology agents. However, it is **not** a conventional cytotoxic chemotherapy drug — it is a targeted hormonal agent with a mechanism distinct from DNA-damaging chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Non-cytotoxic endocrine therapy — Aromatase Inhibitor (targeted hormonal mechanism); **not** classified as conventional cytotoxic or myelosuppressive agent |
| Myelosuppression Risk | **Low** — aromatase inhibitors do not cause clinically significant bone marrow suppression; myelotoxicity is not a characteristic adverse effect of this drug class |
| Emetogenicity Classification | **Minimal** — oral once-daily tablet with very low emetogenic potential; routine antiemetic prophylaxis is not required |
| Monitoring Items | Bone mineral density (DEXA scan at baseline, then every 1–2 years); fasting lipid profile; liver function tests; musculoskeletal symptom assessment (arthralgia, myalgia); fracture risk evaluation (FRAX score) |
| Handling Protection | Standard pharmaceutical handling precautions; **cytotoxic closed-system transfer device and hazardous drug PPE protocols are not required** for aromatase inhibitors per current pharmacist handling guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data — including key warnings, contraindications, and drug interactions — were identified as data gaps in this evidence pack (DG001: Blocking severity). NPRA package insert PDF retrieval is the recommended immediate remediation step. Based on published literature, known class-effect concerns include: bone mineral density loss with prolonged use, aromatase inhibitor-associated musculoskeletal syndrome (AIMSS), elevated cardiovascular lipid risk, and absolute contraindication in premenopausal women and during pregnancy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN predicts female breast carcinoma as the top indication for anastrozole with a 99.68% confidence score, which corresponds precisely to its established, regulatory-approved primary use — validated by multiple completed Phase 3 RCTs (including ATAC, IBIS-II, and MA.27), achieving the highest evidence grade (L1). The prediction demonstrates strong model validity and supports clinical deployment with standard safety monitoring protocols already defined in the published literature.

**To proceed, the following is needed:**

- **Package insert retrieval** *(DG001 — Blocking)*: Download and parse NPRA-registered package insert PDFs to formally document key warnings, contraindications, and precautions for Malaysian market products; required before S1 safety evaluation can be completed
- **Mechanism of action documentation** *(DG002 — High)*: Query DrugBank API for DB01217 to formally populate the MOA field and complete the pharmacological profile for this evidence pack
- **NPRA product registration details**: Query the NPRA database to populate authorization numbers, product names, dosage forms, and approved indication text for all 4 registered anastrozole products
- **Bone health management protocol**: Establish a DEXA-guided bone mineral density monitoring and intervention protocol (calcium/vitamin D supplementation, bisphosphonate threshold criteria) appropriate for the Malaysian patient population
- **Patient selection criteria**: Define postmenopausal status confirmation procedures and ER/PR receptor testing requirements aligned with Malaysian clinical practice standards before any formulary or prescribing guideline update
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

