---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Imipenem
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

# Imipenem: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

> Imipenem (with cilastatin) is a broad-spectrum carbapenem antibiotic used for severe and multidrug-resistant bacterial infections; the specific TFDA-approved indication text is not available in the source data.
> The TxGNN model's top-ranked prediction is **Diffuse Scleroderma**, with a very high prediction score but **0 clinical trials** and **0 publications** currently supporting this direction.
> This candidate should be treated as a low-confidence model output requiring further scrutiny before any action is taken.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in source data (Imipenem is generally known as a broad-spectrum antibacterial for severe/multidrug-resistant infections) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, Imipenem is a carbapenem-class beta-lactam antibiotic that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs), giving it broad-spectrum bactericidal activity against Gram-positive, Gram-negative, and anaerobic organisms.

Diffuse scleroderma, however, is an autoimmune and fibrotic connective tissue disease with no known bacterial etiology. There is no antimicrobial target in its pathophysiology that would explain a therapeutic effect from a cell-wall-synthesis inhibitor. Consistent with this, the evidence pack's own mechanistic assessment states there is **no mechanistic link** between the drug and this disease, and that the high TxGNN score most likely reflects a spurious association from the knowledge-graph embedding rather than a real biological signal — supported by the complete absence of clinical trials or literature (0/0).

By contrast, several lower-ranked predictions in this same evidence pack (e.g., typhoid fever, salmonellosis, staphylococcus aureus infection) fall squarely within Imipenem's known antibacterial spectrum and are backed by clinical and literature evidence. This reinforces that the top-ranked diffuse scleroderma prediction is an outlier rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Malaysia (NPRA) records indicate the product is marketed with **5 registered licenses**, but detailed license information (authorization numbers, product names, dosage forms, approved indication text) is not available in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications (DG001) are flagged as a Blocking data gap — this information must be obtained before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (diffuse scleroderma) has no plausible mechanistic rationale, no clinical trials, and no supporting literature — it does not meet even the minimum bar for further evaluation (L5/S0).

**To proceed, the following is needed:**
- Package insert warnings/contraindications (DG001, Blocking) to complete basic safety screening
- Mechanism of action data (DG002) to properly assess biological plausibility for any predicted indication
- If pursuing repurposing analysis further, prioritize better-supported candidates from the same prediction set (e.g., typhoid fever, staphylococcus aureus infection) rather than diffuse scleroderma
- Complete Malaysia license detail (product names, dosage forms, approved indication text) currently missing from registry records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

