---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest is a fourth-generation progestin primarily used for the treatment of endometriosis and endometriosis-related pelvic pain. The TxGNN model predicts it may be effective for **Amenorrhea**, with **0 clinical trials** and **6 publications** indirectly related to this direction. However, expert review flags this prediction as a **likely false positive** — amenorrhea is a well-known pharmacological side effect of dienogest (incidence ~20–30%), not a therapeutic target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (derived from literature; license-level indication text unavailable) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (mechanism/pharmacological studies only) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, dienogest is a selective progestin with high affinity for the progesterone receptor and minimal androgenic activity. It suppresses the hypothalamic-pituitary-ovarian (HPO) axis, inhibits ovulation, and creates a hypoestrogenic environment that causes endometrial atrophy — the basis for its efficacy in endometriosis.

**This prediction is flagged as a likely false positive.** Amenorrhea (absence of menstruation) is a direct and expected pharmacological consequence of dienogest's HPO axis suppression. In the clinical management of endometriosis, the induction of amenorrhea is actually considered a marker of therapeutic efficacy, not a disease to be treated. The TxGNN knowledge graph has detected a strong "drug–amenorrhea" association, but this reflects a **drug–side effect relationship**, not a **drug–therapeutic indication relationship**.

Among the remaining 9 predicted indications, several share a similar pattern of false association: primary ovarian failure (rank 2) and hypogonadotropic hypogonadism (rank 7) are pharmacologically contraindicated, while chromosomal anomalies (ranks 8–10) and genetic syndromes (ranks 5–6) have no mechanistic basis. Only **breast fibrocystic disease** (rank 3) has limited theoretical plausibility based on progesterone's anti-estrogenic effects on breast tissue, though evidence is minimal (1 pilot study).

## Clinical Trial Evidence

Currently no related clinical trials registered for dienogest in amenorrhea.

> Note: One clinical trial ([NCT04306276](https://clinicaltrials.gov/study/NCT04306276)) was retrieved under the related prediction for primary ovarian failure (rank 2), but its actual focus is dienogest pretreatment before IVF in endometriosis patients — not relevant to amenorrhea as a therapeutic target.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review | BMC Pharmacol Toxicol | Systematic review of adverse effects of dienogest; amenorrhea identified as a common side effect during endometriosis treatment |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Pharmacological Study | Eur J Contracept Reprod Health Care | High inhibition ratio of dienogest 2 mg supports its use in endometriosis by inducing amenorrhea and a hypoestrogenic environment |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Hormonal treatments for endometriosis; dienogest reduces ectopic endometrial implants via estrogen suppression |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Cohort | Reprod Sci | Long-term dienogest use (>12 months) in ovarian endometrioma; efficacy and safety assessed in 514 women across 7 centres |
| [19499407](https://pubmed.ncbi.nlm.nih.gov/19499407/) | 2009 | Pilot Study | Gynecol Endocrinol | High-dose dienogest (2×10 mg) for 24 weeks caused mammary gland size reduction and regression of mastopathic changes in 21 endometriosis patients |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Case/Imaging | J Pediatr Adolesc Gynecol | Advanced visualization for Müllerian anomalies; dienogest mentioned as medical management — tangentially related |

> **Note:** These publications discuss amenorrhea as a **side effect or efficacy marker** of dienogest in endometriosis treatment, not as a disease target. No publication directly investigates dienogest as a treatment for pathological amenorrhea.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Not available) | (Not available) | (Not available) | (Not available) |

> 6 product registrations are recorded with marketed status in Malaysia. Detailed license-level information (authorization numbers, product names, dosage forms, and approved indication text) was not available in this evidence pack.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack.

**Known data gaps (severity noted):**
- NPRA package insert warnings/contraindications — **Blocking** (required for Stage 1 safety review)
- Mechanism of action (MOA) detail — **High** (impacts mechanistic relevance analysis)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (amenorrhea) is assessed as a **false positive** — amenorrhea is a known and common pharmacological side effect of dienogest, not a therapeutic target. The remaining 9 predictions are similarly problematic: most involve contraindicated logic (primary ovarian failure, hypogonadotropic hypogonadism), irrelevant genetic/chromosomal conditions, or have only marginal mechanistic plausibility (breast fibrocystic disease). Additionally, critical safety data (package insert warnings, contraindications) and MOA detail are missing, blocking formal safety evaluation.

**To proceed, the following is needed:**
- **Re-evaluate model output**: Flag amenorrhea, primary ovarian failure, and hypogonadotropic hypogonadism as known side effects / contraindicated associations and exclude from future candidate lists
- **Investigate breast fibrocystic disease (rank 3)**: The only prediction with limited mechanistic plausibility — requires additional literature search and expert consultation before advancing
- **Obtain package insert data**: Download and parse NPRA-approved product inserts to complete safety profile
- **Query DrugBank for MOA**: Retrieve detailed mechanism of action (DrugBank ID lookup needed) to enable proper mechanistic analysis
- **Model improvement recommendation**: Consider incorporating a side-effect exclusion filter in TxGNN post-processing to reduce false-positive predictions where known adverse effects are misclassified as therapeutic indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

