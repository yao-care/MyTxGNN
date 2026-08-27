---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
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

# Megestrol Acetate: From Palliative Hormonal Therapy for Breast/Endometrial Carcinoma to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a synthetic progestin historically used for palliative treatment of breast and endometrial carcinoma and for cancer/AIDS-related anorexia-cachexia. The TxGNN model's top-ranked prediction, **Uterine Corpus Endometrial Carcinoma**, is supported by **3 clinical trials** directly retrieved for this exact ontology term, while the closely related (and evidence-richer) sibling term "endometrial cancer" carries **36 clinical trials and 20 publications**, reflecting that this is largely a refinement of an already-recognized clinical use (fertility-sparing progestin therapy) rather than an entirely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in this data pack (TFDA/NPRA license `approved_indication_text` fields are empty). Per international labeling referenced within the evidence pack itself (e.g., NCT00163072), megestrol acetate is approved for palliative treatment of breast and endometrial carcinoma, and is widely used as an appetite stimulant in cancer-related cachexia. |
| Predicted New Indication | Uterine Corpus Endometrial Carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a Blocking/High data gap in this pack (DG001, DG002). Based on information recoverable from the evidence itself, megestrol acetate is a progestin that acts as a progesterone receptor (PR) agonist, suppressing estrogen-driven proliferation of PR-positive endometrial tissue and inducing glandular differentiation — a mechanism described repeatedly across the retrieved literature (e.g., PMID 34233525, "Megestrol acetate drives endometrial carcinoma cell senescence via interacting with progesterone receptor B/FOXO1 axis").

The predicted new indication is mechanistically almost a restatement of an existing use: megestrol acetate is already an internationally recognized agent for endometrial carcinoma (particularly in fertility-sparing regimens for young women with early-stage, PR-positive disease). The evidence pack's own rationale notes that "uterine corpus endometrial carcinoma" and "endometrial cancer" are different ontology terms for essentially the same clinical entity, which explains why both score almost identically (99.94%) despite very different amounts of retrieved evidence — the rank-1 term simply has thinner direct query coverage (3 trials, 0 literature hits) than its sibling node (36 trials, 20 publications, including a completed Phase III temsirolimus±MA trial and multiple GOG-sponsored studies).

Because the mechanism (PR agonism → suppressed endometrial proliferation) is identical regardless of which ontology label is used, the strength of this prediction should be read together with the "endometrial cancer" evidence cluster rather than in isolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor combined with progesterone vs. progesterone alone for fertility preservation in early-stage endometrial cancer |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Continuous vs. sequential progestin therapy for endometrial intraepithelial neoplasia/atypical hyperplasia in patients desiring uterine preservation; terminated with very small sample |
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Temsirolimus with or without megestrol acetate + tamoxifen in advanced/persistent/recurrent endometrial carcinoma; directly evaluates MA-containing regimen |

*Note: A far larger evidence base (36 trials) exists for the closely related node "endometrial cancer," including completed Phase II/III studies directly testing megestrol acetate (e.g., NCT05538897, NCT04576104, NCT03241914, NCT00016341). See rationale above.*

---

## Literature Evidence

Currently no related literature available for this specific ontology term (0 PubMed hits recorded in the query log for "uterine corpus endometrial carcinoma"). Substantial literature (20 publications, including a Tier-1 GOG randomized trial, PMID 24456823) exists for the related term "endometrial cancer."

---

## Malaysia Market Information

Three NPRA registrations are on record (`total_licenses: 3`, market status: Marketed), but license number, product name, dosage form, and approved-indication fields were not populated in this data pack — product-level detail could not be extracted for this report.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) antineoplastic agent — progestin/PR agonist; **not** conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low — megestrol acetate is not associated with clinically significant bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Adrenal function (secondary adrenal suppression reported, PMID 10491532), coagulation parameters/VTE risk (PMID 11727356), weight/glycemic status, blood pressure |
| Handling Protection | Standard cytotoxic-drug handling precautions are not required (non-cytotoxic hormonal agent) |

---

## Safety Considerations

Please refer to the package insert for formal warnings, contraindications, and drug-interaction data (none were retrievable in this data pack; DDI query returned no results).

Supplementary signals noted in the retrieved literature (not part of the formal safety dataset): secondary adrenal suppression with MA therapy (PMID 10491532) and effects on hemostasis/thromboembolic risk at high doses (PMID 11727356).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and megestrol acetate is already used clinically for endometrial carcinoma, but the specific ontology term ranked first by TxGNN has only thin direct trial evidence (3 trials, no literature) and a critical safety data gap (TFDA/NPRA label warnings and contraindications are missing, flagged Blocking).

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- DrugBank-sourced MOA and drug interaction profile (DG002)
- Product-level Malaysia registration detail (license numbers, dosage forms, approved indication text)
- Formal evidence synthesis across the "uterine corpus endometrial carcinoma" and "endometrial cancer" ontology nodes, since they represent the same clinical entity and should not be evaluated in isolation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

