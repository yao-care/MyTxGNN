---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cladribine: From Lymphoid Malignancies to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog with established clinical use in hairy cell leukemia, chronic lymphocytic leukemia, and multiple sclerosis. The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on the model's statistical association score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA license data; known clinical use (per evidence pack rationale) includes hairy cell leukemia, CLL, and multiple sclerosis |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (marked as a data gap). Based on information embedded in the evidence pack's own rationale, cladribine is a deoxyadenosine analog that, after phosphorylation by deoxycytidine kinase, accumulates preferentially in cells with high DCK/low 5'-nucleotidase activity — primarily lymphocytes and monocytes. This underlies its established clinical use in lymphoid malignancies (hairy cell leukemia, CLL) and multiple sclerosis.

Rhabdomyosarcoma, by contrast, is a tumor of skeletal-muscle lineage typically driven by PAX3/7-FOXO1 fusion genes or RAS-pathway alterations. There is no known biological overlap between cladribine's lymphocyte-selective nucleoside-analog mechanism and rhabdomyosarcoma's driver pathways.

The evidence pack itself is explicit that this prediction is a knowledge-graph statistical association rather than a mechanistically derived hypothesis: all seven predicted indications are rhabdomyosarcoma subtypes (plus one liver sarcoma) clustered at nearly identical TxGNN scores (0.9975–0.9977), with zero clinical trials, zero literature, and zero ICTRP records across every query performed. This pattern is more consistent with the model's disease-embedding neighborhood than with a targeted mechanistic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA records confirm cladribine has **3 marketed registrations** in Malaysia (market status: 已上市 / Marketed). However, the evidence pack does not include the specific license numbers, product names, dosage forms, or approved-indication text for these registrations — these fields were returned empty from the source query and require follow-up retrieval from NPRA.

---

## Cytotoxicity

Cladribine's known clinical use (hairy cell leukemia, CLL) places it in the antineoplastic/cytotoxic category.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: NPRA label warnings/contraindications for this drug are marked as a **Blocking** data gap (DG001) in the source evidence pack — this data must be obtained before any safety assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical or literature evidence across any of the 7 candidate indications), and a blocking data gap in NPRA label safety information prevents even an initial safety screen. There is no mechanistic, clinical, or preclinical basis currently on file linking cladribine to rhabdomyosarcoma.

**To proceed, the following is needed:**
- NPRA label warnings/contraindications (DG001, Blocking) — required before any S1 safety review
- Confirmed mechanism of action from DrugBank (DG002, High) — required to assess mechanistic plausibility
- Preclinical or case-level evidence specifically linking cladribine to rhabdomyosarcoma or related sarcoma pathways
- Complete NPRA license details (product names, dosage forms, approved indication text) for the 3 existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

