---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 7
---

# Cyclosporine
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

# Cyclosporine: From Organ Transplant Rejection to Chronic Granulomatous Disease (Autosomal Recessive)

## One-Sentence Summary

Cyclosporine is a calcineurin-inhibitor immunosuppressant, established globally for prevention of organ transplant rejection and treatment of select autoimmune conditions (the specific NPRA-approved indication text for this product is not available in the current dataset). The TxGNN model predicts it may be effective for **Chronic Granulomatous Disease, Autosomal Recessive**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and a mechanistic rationale for this specific candidate has not yet been generated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Organ transplant rejection prophylaxis / immunosuppressant (general pharmacology; specific NPRA-approved indication text not available in current registration record) |
| Predicted New Indication | Chronic Granulomatous Disease, Autosomal Recessive |
| TxGNN Prediction Score | 99.68% (rank 5221) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a High-severity data gap). Based on known pharmacology, cyclosporine is a calcineurin inhibitor that blocks T-cell activation and IL-2 transcription, and its established efficacy is in suppressing adaptive (T-cell-mediated) immune responses — used clinically for transplant rejection prophylaxis and T-cell-driven autoimmune/inflammatory diseases such as psoriasis and rheumatoid arthritis.

Chronic Granulomatous Disease (autosomal recessive form) is a primary immunodeficiency caused by defective NADPH oxidase in phagocytes, which impairs the innate immune system's ability to kill catalase-positive organisms. This is mechanistically distinct from — and largely unrelated to — the T-cell suppressive pathway that cyclosporine acts on. No mechanistic linkage for this specific candidate has been generated in the evidence pack, and on general pharmacological grounds, further suppressing immune function with a T-cell inhibitor in a patient who already has an underlying phagocyte immunodeficiency raises a plausibility concern rather than a therapeutic rationale (cyclosporine is occasionally used off-label to manage CGD-associated inflammatory/autoimmune complications such as colitis, but this is a distinct clinical context from treating the underlying immunodeficiency itself).

Given the absence of supporting trials, literature, or a documented mechanistic link for this top-ranked candidate, the prediction should currently be treated as a model-generated hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The dataset confirms the product is **Marketed** in Malaysia with **1 active NPRA registration**, but the specific authorization number, product name, dosage form, and approved indication text fields were not populated in the current record and cannot be reported here without risking inaccuracy.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: package-insert-level warnings and contraindications for this product are marked as a Blocking data gap in the underlying evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has only model-prediction-level evidence (L5) — no clinical trials, no literature, and no documented mechanistic link — and a Blocking data gap on TFDA/NPRA label warnings and contraindications means the candidate cannot yet enter initial safety screening (S1). The six other TxGNN-ranked candidates for this drug were also all scored Hold with weak or no plausible mechanistic support, reinforcing that this evidence pack does not currently justify advancing any candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (blocking gap — required before any safety screening)
- Detailed mechanism of action data from DrugBank or equivalent source
- Complete NPRA registration record (license number, product name, dosage form, approved indication text)
- A generated mechanistic rationale and clinical trial/literature search specific to the top-ranked indication before any Go/Guardrails consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

