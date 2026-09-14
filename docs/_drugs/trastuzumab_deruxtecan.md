---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trastuzumab Deruxtecan: From HER2-Positive Breast/Gastric Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Trastuzumab deruxtecan is a HER2-targeted antibody-drug conjugate (ADC) whose cytotoxic payload is used to treat HER2-positive breast and gastric cancer. The TxGNN model predicts a possible link to **drug-induced osteoporosis**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the drug's own evidence pack flags the mechanistic direction as likely reversed (i.e., the model may be detecting a known adverse-effect association rather than a therapeutic one).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer / gastric cancer (per known drug profile — TFDA approved-indication text is not available in this dataset) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (data gap DG002). Based on the known drug profile, trastuzumab deruxtecan is an ADC combining a HER2-targeting antibody with a topoisomerase I inhibitor payload (DXd), and its clinical use is as cytotoxic chemotherapy for HER2-positive solid tumours.

This mechanism does not point toward a bone-protective effect. On the contrary, cytotoxic chemotherapy, chemotherapy-induced menopause/hypogonadism, and related supportive therapies are well-established **causes** of drug-induced osteoporosis in clinical practice — not treatments for it. The TxGNN score of 99.31% is very high, but the evidence pack's own rationale assesses this as a likely case of the knowledge graph confusing a "drug → adverse effect → disease" proximity with a genuine "drug → treats → disease" relationship. In other words, the predicted direction of causality may be inverted.

Given this, the prediction should be treated as mechanistically implausible until independently corroborated, rather than as a promising repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

The product is marketed in Malaysia with 1 registered license, but the license number, product name, dosage form, and approved-indication text are not populated in the current dataset. This detail needs to be pulled directly from the NPRA registry before further evaluation.

---

## Cytotoxicity

This drug qualifies as antineoplastic (HER2-targeted ADC with a cytotoxic topoisomerase I inhibitor payload, used for breast/gastric cancer).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate) with a conventional cytotoxic payload (topoisomerase I inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (L5, model-only), and the drug's own repurposing rationale indicates the mechanistic direction is likely inverted — trastuzumab deruxtecan's cytotoxic mechanism is a plausible cause of drug-induced osteoporosis, not a treatment for it.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF with full warnings and contraindications (blocking data gap DG001; required before any S1 safety review)
- Confirmed mechanism of action via DrugBank API (DG002)
- Complete Malaysia license details (license number, product name, dosage form, approved indication text)
- Independent mechanistic review to confirm/rule out reversed causality before any further evidence collection is commissioned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

