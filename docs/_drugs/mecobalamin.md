---
layout: default
title: Mecobalamin
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 3
---

# Mecobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Mecobalamin: From Unspecified Original Indication to Sclerosing Cholangitis

## One-Sentence Summary

Mecobalamin (DrugBank DB03614) is a vitamin B12 coenzyme analogue marketed in Malaysia under 16 registrations, but its approved indication text was not captured in the current data extraction.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no known biological link to the proposed mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (no non-empty approved indication text on record) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for mecobalamin (Data Gap). Based on general pharmacology, mecobalamin is the active coenzyme form of vitamin B12, primarily involved in the methionine synthase reaction, homocysteine metabolism, and myelin/nerve repair.

There is no established mechanistic link between vitamin B12 metabolism and sclerosing cholangitis, which is pathologically driven by immune-mediated bile duct fibrosis (IgG4-related disease, autoimmune, or cholestatic processes). The model's own rationale for this candidate explicitly states that the association is a data-driven statistical signal from the knowledge graph rather than one supported by a biological hypothesis, and that the missing original MOA data further limits confidence in this link.

The two lower-ranked candidates (multiple endocrine neoplasia and bone Paget disease) show a similar pattern: no established pathway overlap with B12/homocysteine metabolism, and the model rationale for each states the connection is inferred rather than mechanistically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Detailed authorization records (license numbers, product names, dosage forms, approved indication text) for the 16 registered mecobalamin products are not available in the current dataset — all license fields returned empty on extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications are flagged as a Blocking data gap (DG001) — this prevents a full S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (sclerosing cholangitis) is evidence level L5 — a model-only prediction with zero supporting clinical trials or literature, and the model's own rationale notes no known biological plausibility. Combined with a Blocking safety data gap (missing TFDA label/warnings) and missing MOA data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF with warnings and contraindications (DG001, Blocking)
- DrugBank-sourced mechanism of action data (DG002, High)
- Confirmed original approved indication text (current license records are empty)
- Literature or trial evidence specifically linking B12/homocysteine metabolism to bile duct fibrosis, if this candidate is to be re-evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

