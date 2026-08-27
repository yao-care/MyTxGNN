---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

# Cyproterone Acetate: From Androgen-Dependent Conditions to Migraine Disorder

## One-Sentence Summary

Cyproterone acetate is an antiandrogen with progestogenic activity, marketed in Malaysia for androgen-dependent conditions (specific approved indication text is not available in the current dataset). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on a theoretical mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (NPRA license indication text is blank); generally known use is androgen-dependent conditions (e.g. hirsutism, severe acne, hormone-responsive conditions) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset (DG002, DrugBank query pending). Based on the mechanistic rationale attached to this candidate, cyproterone acetate suppresses ovarian function and blunts LH surges, which is the pharmacological basis proposed for this prediction: menstrual migraine is triggered by cyclical estrogen withdrawal, so stabilizing hormonal fluctuation could theoretically reduce migraine frequency.

This is explicitly flagged in the source data as an inferential, unverified mechanism — no clinical trial, case report, or preclinical study confirms this link for cyproterone acetate specifically. The connection to the drug's known hormonal activity (antiandrogen + progestogenic) is biologically plausible but has not been tested in the migraine population.

It is also worth noting that of the 10 TxGNN-predicted indications for this drug, several lower-ranked candidates (thrombophilia, antithrombin deficiency, heparin cofactor 2 deficiency, factor 5 excess with spontaneous thrombosis) are flagged in the source rationale as probable **false positives from inverted risk direction** — i.e., conditions where cyproterone acetate (particularly in combined estrogen-containing formulations) is a known risk factor, not a treatment. This raises a general caution about relying on TxGNN scores alone for this drug without mechanistic screening.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA records confirm cyproterone acetate holds **4 marketed authorizations** in Malaysia (status: 已上市/Marketed). Detailed authorization numbers, product names, dosage forms, and approved indication text are not available in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has evidence level L5 — a TxGNN score alone, with zero supporting clinical trials or literature (confirmed by 3 separate source queries returning 0 results). Combined with a Blocking data gap on TFDA/NPRA warnings and contraindications, the candidate cannot yet enter safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review)
- Verified mechanism of action data from DrugBank (DG002)
- At minimum, preclinical or observational evidence linking hormonal modulation to migraine frequency before considering further clinical evaluation
- Caution: re-screen the full 10-candidate prediction set for this drug — several entries appear to reflect risk-factor associations rather than therapeutic ones, and should not be advanced without independent mechanistic review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

