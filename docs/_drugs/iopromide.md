---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is an iodinated radiographic contrast agent used for diagnostic imaging rather than a therapeutic drug for a specific disease. The TxGNN model predicts a possible link to **osteoarthritis susceptibility**, but this prediction is currently a pure knowledge-graph output with **no clinical trials and no supporting literature** of any kind.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registration records — evidence pack identifies iopromide as an iodinated contrast medium for diagnostic imaging, not a treatment indication |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, iopromide belongs to the class of low-osmolar iodinated contrast agents used to enhance visualization during CT and other radiographic imaging — it has no established anti-inflammatory, chondroprotective, or disease-modifying pharmacological activity.

The predicted indication, "osteoarthritis susceptibility," reads more like a genetic-susceptibility trait node in the knowledge graph than a conventional clinical indication. The evidence pack itself states plainly that there is no mechanistic link: this is a pure TxGNN graph-embedding prediction (score 0.9957) with zero clinical trials or literature backing it.

Even the closely related candidate "osteoarthritis" (rank 2) only returned two papers, both of which use iopromide purely as an imaging tool for diagnostic technique or cartilage-measurement studies — not as a treatment. There is no pharmacological rationale connecting a contrast agent to osteoarthritis pathophysiology at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Iopromide is marketed in Malaysia under 2 registrations; however, license numbers, product names, dosage forms, manufacturers, and approved indication text are not available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information (TFDA label warnings/contraindications are flagged as a Blocking data gap — package insert has not yet been retrieved/parsed).

**Additional safety signal identified during literature search (not part of formal label data):** A case report (PMID [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/)) describes a cerebral vaso-occlusive event following low-osmolar intravenous contrast (the class iopromide belongs to) in a patient with sickle cell disease, surfaced under the "hemoglobinopathy" candidate. This appears to be an adverse-event/contraindication signal rather than a treatment signal, and should be treated as a caution flag for hemoglobinopathy patients pending confirmation from the official label once retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (osteoarthritis susceptibility) has no clinical trial or literature support whatsoever — it is L5, model-prediction-only evidence. Combined with a Blocking data gap on TFDA safety warnings/contraindications, the candidate cannot proceed to safety screening (S1) or be considered for further development at this time.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA package insert (warnings, contraindications) to clear the Blocking data gap
- Obtain DrugBank mechanism-of-action data to assess biological plausibility
- If pursuing an arthritis-related indication, run targeted searches for actual treatment studies (current hits for "osteoarthritis" and "rheumatoid arthritis" are imaging-technique papers only, not efficacy evidence)
- Clarify and confirm the sickle cell disease / vaso-occlusive event safety signal against the official label before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

