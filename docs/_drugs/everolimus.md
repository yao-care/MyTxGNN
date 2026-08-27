---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 5
---

# Everolimus
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

# Everolimus: From Prior Approved Indications to Breast Neoplasm

## One-Sentence Summary

Everolimus is an oral mTOR-pathway inhibitor already registered and marketed in Malaysia under 8 licenses, though this evidence pack does not include the specific approved-indication text for those registrations. The TxGNN model flags **Breast Neoplasm** as the top-ranked candidate indication, and the evidence pack already contains substantial supporting data — **50 clinical trials** and **20 publications**, including the pivotal BOLERO-2 Phase 3 RCT that underpins everolimus's established use in hormone-receptor-positive advanced breast cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified — NPRA license records show 8 registrations but the approved-indication text field is empty for all of them |
| Predicted New Indication | Breast Neoplasm |
| TxGNN Prediction Score | 0.00% (as recorded in this evidence pack — see note below) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

*Note: the TxGNN score is recorded as 0.0 for all five predicted indications in this evidence pack, which looks like an upstream data-population issue rather than a genuine tied score — flagged here rather than silently corrected.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap in this evidence pack). Based on known information, everolimus is an oral inhibitor of the mTOR (mammalian target of rapamycin) signaling pathway, a class already approved worldwide across multiple oncology indications (renal cell carcinoma, subependymal giant cell astrocytoma, pancreatic neuroendocrine tumors) as well as breast cancer.

The predicted breast-neoplasm indication is not a novel hypothesis so much as a well-established use already reflected in the evidence: the BOLERO-2 trial (NEJM 2012, PMID 22149876) demonstrated that adding everolimus to exemestane significantly prolonged progression-free survival in postmenopausal women with hormone-receptor-positive, HER2-negative advanced breast cancer that progressed on a nonsteroidal aromatase inhibitor — a result later confirmed for overall survival (PMID 25231953) and PFS durability (PMID 24158787). Mechanistically, aberrant PI3K/AKT/mTOR signaling is a recognized driver of endocrine-therapy resistance in HR+ breast cancer, which is why blocking mTOR downstream of the estrogen receptor pathway restores sensitivity to aromatase inhibition. The subsequent trial landscape (TRINITI-1, PrE0102, LEO, and numerous CDK4/6-inhibitor-resistance combination studies) further extends this rationale into post-CDK4/6i settings.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01805271](https://clinicaltrials.gov/study/NCT01805271) | Phase 3 | Active, not recruiting | 1278 | Adjuvant everolimus added to hormone therapy in high-relapse-risk, ER+/HER2− primary breast cancer |
| [NCT01773444](https://clinicaltrials.gov/study/NCT01773444) | Phase 2 | Completed | 309 | Three-arm trial: everolimus+exemestane vs. everolimus alone vs. capecitabine after AI failure in ER+ advanced breast cancer |
| [NCT06382948](https://clinicaltrials.gov/study/NCT06382948) | Phase 3 | Active, not recruiting | 240 | Elacestrant + everolimus vs. elacestrant alone in ER+/HER2−, ESR1-mutated advanced breast cancer post-CDK4/6i |
| [NCT00107016](https://clinicaltrials.gov/study/NCT00107016) | Phase 2 | Completed | 267 | Everolimus + letrozole vs. placebo + letrozole as preoperative therapy in newly diagnosed ER+ primary breast cancer |
| [NCT02871791](https://clinicaltrials.gov/study/NCT02871791) | Phase 1/2 | Completed | 41 | Palbociclib + everolimus + exemestane in ER+/HER2− metastatic breast cancer resistant to CDK4/6 inhibitors |
| [NCT02258451](https://clinicaltrials.gov/study/NCT02258451) | Phase 2 | Completed | 283 | Radium-223 + exemestane/everolimus vs. placebo + exemestane/everolimus in HER2− HR+ breast cancer with bone metastases |
| [NCT02344550](https://clinicaltrials.gov/study/NCT02344550) | Phase 2 | Completed | 137 | Ovarian suppression + letrozole + everolimus in premenopausal, tamoxifen-pretreated HR+ recurrent/metastatic breast cancer (LEO trial) |
| [NCT00674414](https://clinicaltrials.gov/study/NCT00674414) | Phase 2 | Terminated | 82 | Everolimus added to trastuzumab as preoperative therapy in HER2+ primary breast cancer |
| [NCT02069093](https://clinicaltrials.gov/study/NCT02069093) | Phase 2 | Completed | 92 | Steroid-based mouthwash to prevent everolimus-related stomatitis in HR+/HER2− metastatic breast cancer |
| [NCT00426556](https://clinicaltrials.gov/study/NCT00426556) | Phase 1 | Completed | 88 | Everolimus + trastuzumab + paclitaxel in HER2-overexpressing metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22149876](https://pubmed.ncbi.nlm.nih.gov/22149876/) | 2012 | RCT | N Engl J Med | BOLERO-2: everolimus + exemestane significantly improved outcomes vs. exemestane alone in HR+ advanced breast cancer |
| [25231953](https://pubmed.ncbi.nlm.nih.gov/25231953/) | 2014 | RCT | Ann Oncol | BOLERO-2 final overall survival analysis |
| [24158787](https://pubmed.ncbi.nlm.nih.gov/24158787/) | 2013 | RCT | Adv Ther | BOLERO-2 final progression-free survival analysis |
| [29664714](https://pubmed.ncbi.nlm.nih.gov/29664714/) | 2018 | RCT | J Clin Oncol | PrE0102: randomized fulvestrant + everolimus vs. placebo in AI-resistant HR+/HER2− metastatic breast cancer |
| [40897974](https://pubmed.ncbi.nlm.nih.gov/40897974/) | 2025 | RCT | Nat Med | Randomized Phase 2 targeting dormant disseminated tumor cells to prevent breast cancer recurrence |
| [33722897](https://pubmed.ncbi.nlm.nih.gov/33722897/) | 2021 | Trial (Phase I/II) | Clin Cancer Res | TRINITI-1: exemestane + ribociclib + everolimus after CDK4/6-inhibitor progression |
| [33151471](https://pubmed.ncbi.nlm.nih.gov/33151471/) | 2020 | Systematic Review / Meta-analysis | Target Oncol | Review of everolimus efficacy across breast cancer phenotypes and combinations |
| [25659402](https://pubmed.ncbi.nlm.nih.gov/25659402/) | 2015 | Review | Expert Opin Drug Metab Toxicol | PK/PD evaluation of everolimus in breast cancer treatment |
| [23907751](https://pubmed.ncbi.nlm.nih.gov/23907751/) | 2013 | Review | Breast Cancer Res Treat | Everolimus side-effect profile and toxicity management in breast cancer |
| [36453053](https://pubmed.ncbi.nlm.nih.gov/36453053/) | 2022 | Review | Cancer Prev Res | Perspective on everolimus for ER-negative breast cancer prevention |

---

## Malaysia Market Information

The NPRA registry shows **8 licenses** for Everolimus with market status "已上市" (Marketed), but this evidence pack does not include the per-license details (license number, product name, dosage form, or approved-indication text) — all corresponding fields were returned empty. These details need to be pulled from the NPRA source directly before a license-level table can be produced.

---

## Cytotoxicity

Everolimus is an antineoplastic agent (used across renal cell carcinoma, breast cancer, and other oncology indications), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor), based on the drug's known pharmacologic class — detailed institutional MOA documentation is a flagged data gap in this evidence pack |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack flags the absence of TFDA/NPRA label warnings and contraindications as a **Blocking** data gap (DG001) — meaning safety data currently cannot support the mandatory S1 safety review — and the drug-drug interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for everolimus in HR+/HER2− breast cancer is solid (L2 — one completed, well-replicated pivotal Phase 3 RCT, BOLERO-2, plus a substantial supporting trial and literature base), but a Blocking gap in TFDA/NPRA label warnings and contraindications means the mandatory S1 safety review cannot proceed yet, and Malaysia license-level indication text is also unavailable to confirm current local labeling.

**To proceed, the following is needed:**
- Retrieve and parse the NPRA package insert (仿單) PDF for warnings/contraindications (closes DG001, Blocking)
- Retrieve DrugBank MOA detail (closes DG002)
- Populate per-license details (license number, product name, dosage form, approved-indication text) for the 8 registered products
- Complete the drug-drug interaction query (currently `not_found`)
- Once S1 safety review is unblocked, re-evaluate — given the existing efficacy evidence, this candidate is a strong fit for "Proceed with Guardrails"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

