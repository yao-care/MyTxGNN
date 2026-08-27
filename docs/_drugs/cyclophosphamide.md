---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
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

# Cyclophosphamide: From Alkylating Chemotherapy to Myeloid Leukemia

## One-Sentence Summary

> Cyclophosphamide is a classic nitrogen mustard alkylating agent long used as a core component of combination chemotherapy and as an immunosuppressant.
> The TxGNN model predicts it may be effective for **Myeloid Leukemia**,
> but currently **no clinical trials** and **no publications** in this dataset support this specific direction — the prediction rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (label text and indication list are data gaps). Cyclophosphamide is generally known as a broad-spectrum antineoplastic/immunosuppressant used in lymphoma, leukemia and other combination chemotherapy regimens. |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, cyclophosphamide is a nitrogen mustard alkylating agent that is metabolically activated to form DNA-crosslinking metabolites, producing cytotoxic effects preferentially in rapidly dividing cell populations — the same principle underlying its established role in lymphoma, leukemia and other combination chemotherapy regimens.

Myeloid leukemia is characterized by highly proliferative myeloid blast populations, which are theoretically susceptible to alkylating-agent cytotoxicity in the same way other nitrogen mustards are used in leukemia treatment protocols. This gives the TxGNN prediction reasonable mechanistic plausibility.

However, this connection should be interpreted with caution: because cyclophosphamide is already a well-established component of many leukemia and lymphoma chemotherapy regimens (e.g., conditioning regimens, CHOP-type protocols), it is unclear whether "myeloid leukemia" here represents a genuinely novel repurposing signal or simply reflects an existing, real-world indication that was not captured in this dataset's `original_indications` field. This ambiguity should be resolved before further action is taken.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia (NPRA) records show the product is marketed with **1 registration**, but detailed license fields (license number, product name, dosage form, manufacturer, approved indication text) are not populated in this dataset and could not be extracted.

---

## Cytotoxicity

Cyclophosphamide is a well-established cytotoxic antineoplastic agent (predicted/associated indications in this pack are all oncologic), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High — leukopenia and thrombocytopenia are well-documented, dose-limiting toxicities of this drug class |
| Emetogenicity Classification | Moderate to High (dose-dependent; higher with IV administration) |
| Monitoring Items | CBC with differential, platelet count, renal and hepatic function, urinalysis (hemorrhagic cystitis risk) |
| Handling Protection | Yes — requires cytotoxic/hazardous drug handling precautions |

Specific toxicity thresholds and monitoring schedules should be confirmed against the official package insert once available, as no product-specific toxicity data was present in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by mechanistic plausibility (Evidence Level L5) with zero clinical trials or literature identified, and a Blocking-severity data gap (missing NPRA label warnings/contraindications) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- NPRA label PDF (warnings, contraindications) to resolve the Blocking data gap
- DrugBank-confirmed mechanism of action to validate the mechanistic rationale
- Clarification of whether "myeloid leukemia" is a pre-existing indication not captured in `original_indications`, or a genuine new prediction
- Targeted literature/trial search specifically for cyclophosphamide in myeloid leukemia to establish a higher evidence level before any Go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

