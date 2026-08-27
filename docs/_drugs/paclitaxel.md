---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 526
evidence_level: L5
indication_count: 5
---

# Paclitaxel
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

# Paclitaxel: From Ovarian Cancer to Ovarian Clear Cell Adenocarcinoma

## One-Sentence Summary

> Paclitaxel is a taxane-class chemotherapy agent widely used as part of platinum/taxane regimens for epithelial ovarian cancer.
> The TxGNN model ranks **Ovarian Clear Cell Adenocarcinoma** — a distinct, chemoresistant histological subtype of epithelial ovarian cancer — as its top predicted indication for this drug,
> with **50 clinical trials queried** (several graded directly relevant) and **20 publications** currently supporting this direction, though the subtype's known relative resistance to platinum/taxane therapy warrants caution.

*Note: Structured "original indication" text was not captured from the Malaysia NPRA license records in this evidence pack (all `approved_indication_text` fields returned empty). The title above reflects Paclitaxel's well-established general oncology use; formal indication wording should be confirmed against the package insert.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack — NPRA license records did not include indication text |
| Predicted New Indication | Ovarian Clear Cell Adenocarcinoma |
| TxGNN Prediction Score | 0.00%* (score field appears unpopulated in this evidence pack; ranking order was used instead — this is rank 1 of 5 candidates evaluated) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Paclitaxel in this evidence pack. Based on known information, Paclitaxel is a taxane-class, microtubule-stabilizing cytotoxic agent whose efficacy in epithelial ovarian cancer (typically combined with carboplatin) is well established as a global standard of care.

Ovarian clear cell adenocarcinoma (OCCC) is a distinct histological subtype of epithelial ovarian cancer. Because Paclitaxel + Carboplatin is already the backbone regimen used across epithelial ovarian cancer histologies, extending its use to the clear cell subtype is mechanistically plausible and, in fact, reflects existing real-world practice in gynecologic oncology.

However, an important caveat from the evidence: histologically, the clear cell subtype shows a markedly lower response rate to platinum/taxane chemotherapy compared with serous ovarian cancer, reflecting an inherent relative chemoresistance in this subtype. Several of the supporting publications specifically investigate mechanisms of paclitaxel resistance in OCCC (e.g., glycolytic metabolism shifts, NNMT overexpression, HIN-1 methylation), reinforcing that while the mechanistic rationale for use is sound, the subtype's biology limits expected efficacy relative to other ovarian cancer histologies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02129036](https://clinicaltrials.gov/study/NCT02129036) | N/A | Completed | 5 | Retrospective multi-institutional survey of clinical characteristics and response to paclitaxel-platinum vs. conventional platinum chemotherapy specifically in OCCC patients |
| [NCT01196429](https://clinicaltrials.gov/study/NCT01196429) | Phase 2 | Completed | 90 | Temsirolimus + Carboplatin/Paclitaxel as first-line therapy, then Temsirolimus consolidation, specifically in newly diagnosed clear cell ovarian cancer |
| [NCT01824615](https://clinicaltrials.gov/study/NCT01824615) | Phase 2 | Completed | 30 | Evaluated Sunitinib efficacy in recurrent ovarian clear cell carcinoma after standard paclitaxel/platinum-based regimens |
| [NCT02866370](https://clinicaltrials.gov/study/NCT02866370) | Phase 2 | Unknown | 120 | Randomized Nintedanib vs. chemotherapy (incl. paclitaxel-based) in recurrent clear cell carcinoma of ovary or endometrium |
| [NCT06023862](https://clinicaltrials.gov/study/NCT06023862) | Phase 2 | Recruiting | 198 | DOVE trial: Dostarlimab ± Bevacizumab vs. non-platinum chemotherapy in recurrent gynecological clear cell carcinoma |
| [NCT06237946](https://clinicaltrials.gov/study/NCT06237946) | N/A | Unknown | 272 | Retrospective biomarker study of recurrence risk in early-stage OCCC patients after platinum/taxane-based adjuvant therapy |
| [NCT03648489](https://clinicaltrials.gov/study/NCT03648489) | Phase 2 | Completed | 134 | DICE trial: TAK228 + weekly Paclitaxel vs. Paclitaxel alone in advanced/recurrent ovarian cancer including clear cell, endometrioid and high-grade serous types |
| [NCT01097746](https://clinicaltrials.gov/study/NCT01097746) | Phase 2 | Completed | 33 | Bevacizumab + Carboplatin + weekly Paclitaxel as first-line treatment in epithelial ovarian, primary peritoneal and fallopian tube carcinoma |
| [NCT05281471](https://clinicaltrials.gov/study/NCT05281471) | Phase 3 | Recruiting | 186 | OnPrime/GOG-3076: Olvi-Vec followed by platinum-doublet chemotherapy and Bevacizumab vs. physician's choice in platinum-resistant/refractory ovarian cancer |
| [NCT00483782](https://clinicaltrials.gov/study/NCT00483782) | Phase 3 | Completed | 1520 | ICON7: Adding Bevacizumab to standard Carboplatin + Paclitaxel chemotherapy in epithelial ovarian cancer (large RCT, broad histology population) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16445610](https://pubmed.ncbi.nlm.nih.gov/16445610/) | 2006 | Cohort | Int J Gynecol Cancer | Multicenter trial of Paclitaxel-platinum combination chemotherapy specifically in advanced/recurrent ovarian clear cell adenocarcinoma |
| [20192580](https://pubmed.ncbi.nlm.nih.gov/20192580/) | 2009 | Cohort | Asian Pac J Cancer Prev | Compared progression-free survival of OCCC vs. other epithelial ovarian cancer histologies treated with Paclitaxel + Carboplatin |
| [25275661](https://pubmed.ncbi.nlm.nih.gov/25275661/) | 2014 | Cohort | Int J Gynecol Cancer | Analyzed recurrence patterns and role of pelvic radiotherapy in OCCC treated with standard chemotherapy |
| [22041903](https://pubmed.ncbi.nlm.nih.gov/22041903/) | 2011 | Cohort | Gynecol Obstet Invest | Survival impact of adjuvant Paclitaxel + Carboplatin vs. cisplatin-based regimens in early-stage OCCC with complete surgical staging |
| [23714502](https://pubmed.ncbi.nlm.nih.gov/23714502/) | 2013 | Review | ASCO Educational Book | Reviews risk factors, presentation, and treatment direction for ovarian clear cell and mucinous carcinoma |
| [32787339](https://pubmed.ncbi.nlm.nih.gov/32787339/) | 2020 | Review | Chin Clin Oncol | Systemic therapy review for non-serous ovarian carcinoma, including clear cell carcinoma |
| [26497956](https://pubmed.ncbi.nlm.nih.gov/26497956/) | 2015 | Preclinical/Mechanistic | BMC Cancer | Demethylation of HIN-1 reverses paclitaxel resistance in OCCC via the AKT-mTOR signaling pathway |
| [39341074](https://pubmed.ncbi.nlm.nih.gov/39341074/) | 2024 | Preclinical/Mechanistic | Biomed Pharmacother | Paclitaxel resistance facilitates glycolytic metabolism via Hexokinase-2-regulated transporter genes in OCCC |
| [40853419](https://pubmed.ncbi.nlm.nih.gov/40853419/) | 2025 | Preclinical/Mechanistic | Human Cell | Nicotinamide N-methyltransferase (NNMT) enhances paclitaxel resistance in ovarian clear cell carcinoma |
| [39178526](https://pubmed.ncbi.nlm.nih.gov/39178526/) | 2024 | Cohort | Gynecol Oncol | JGOG 3017-A3 analysis of recurrence timing/site in OCCC comparing irinotecan+cisplatin vs. paclitaxel+carboplatin regimens |

---

## Malaysia Market Information

License-level details (authorization number, product name, dosage form, approved indication text) were not available for any of the 14 registered Paclitaxel products in this evidence pack — all NPRA license records returned empty fields. Market status confirms Paclitaxel is currently **Marketed** in Malaysia with **14 total registrations**, but individual product metadata requires re-collection from the NPRA registry.

---

## Cytotoxicity

Paclitaxel is a conventional cytotoxic chemotherapy agent (taxane class), meeting the antineoplastic classification criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | Moderate–High (neutropenia is the principal dose-limiting toxicity of paclitaxel class-wide); official TFDA/NPRA package insert warning text was not available in this evidence pack |
| Emetogenicity Classification | Low–Moderate |
| Monitoring Items | CBC with differential, peripheral neuropathy assessment, liver function |
| Handling Protection | Standard cytotoxic drug handling precautions required |

Please refer to the official package insert warnings and precautions for institution-specific and formulation-specific toxicity data.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a blocking data gap — DG001: TFDA/NPRA package insert warnings/contraindications not yet collected).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by OCCC-specific Phase 2 trials and multiple cohort studies showing Paclitaxel + Carboplatin is already used as a real-world regimen for this subtype, but the well-documented relative chemoresistance of OCCC to platinum/taxane therapy means efficacy expectations should be tempered and monitored closely.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, blocking — required before safety assessment can proceed)
- Detailed mechanism of action data (DG002)
- Malaysia license-level product metadata (authorization numbers, product names, approved indication text)
- Confirmation of formal original indication wording from an authoritative source

**Other predicted indications evaluated in this evidence pack (not detailed above):**

| Rank | Disease | Evidence Level | Decision |
|------|---------|----------------|----------|
| 2 | Peritoneum cancer | L1 | Proceed with Guardrails |
| 3 | Hereditary breast ovarian cancer syndrome | L3 | Research Question |
| 4 | Primary non-gestational choriocarcinoma of ovary | L4 | Hold |
| 5 | Ovarian carcinosarcoma | L1 | Proceed with Guardrails |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

