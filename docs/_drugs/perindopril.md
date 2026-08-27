---
layout: default
title: Perindopril
parent: 僅模型預測 (L5)
nav_order: 539
evidence_level: L5
indication_count: 5
---

# Perindopril
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

# Perindopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Perindopril (DrugBank DB00790) is an ACE inhibitor established for the treatment of hypertension (the current evidence pack does not include the exact NPRA-approved indication text). The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but currently only **0 clinical trials** and **1 tangentially related publication** support this direction, and a blocking safety data gap (missing package-insert warnings/contraindications) prevents a full safety assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (based on known ACE-inhibitor class use; NPRA license indication text not available in this evidence pack) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 39 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on known pharmacology, perindopril is an angiotensin-converting enzyme (ACE) inhibitor that blocks the renin-angiotensin-aldosterone system (RAAS) and dilates the glomerular efferent arteriole, thereby lowering intraglomerular pressure. This is the established pharmacological rationale for ACE inhibitor use across hypertensive kidney disease more broadly.

Malignant hypertensive renal disease is a severe manifestation of uncontrolled hypertension causing acute renal damage, and RAAS blockade is a standard-of-care mechanism for hypertension-related nephropathy. This gives the TxGNN prediction plausible mechanistic grounding.

However, this same mechanism is a double-edged sword: in malignant hypertension with acute kidney involvement, ACE inhibitor initiation carries a real risk of further worsening renal function (efferent arteriolar dilation can drop GFR further in a compromised kidney), so serum creatinine/GFR monitoring is essential at treatment initiation — this is flagged directly in the evidence pack's own repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Cohort/Case series | Urologiia (Moscow) | Discusses residual kidney function after nephrectomy for renal cancer; does not directly evaluate perindopril or ACE inhibitors in malignant hypertensive renal disease — relevance to this specific indication is unconfirmed ("pending" in source data) |

---

## Malaysia Market Information

Perindopril holds 39 active registrations in Malaysia under "已上市" (Marketed) status, but this evidence pack does not contain license-level detail (authorization numbers, product names, dosage forms, or approved indication text) — all license fields were returned empty by the NPRA query, so no table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (DG001) means TFDA/NPRA package-insert warnings and contraindications are unavailable, so this candidate cannot pass initial safety screening (S1). Combined with zero clinical trials and only one publication that is not directly on-topic, the evidence base is currently model-prediction-plus-mechanism only, and the same ACE-inhibitor mechanism carries a known acute renal risk in this exact patient population that must be resolved before proceeding.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — resolve DG001 before any S1 safety evaluation
- DrugBank MOA detail to confirm the mechanistic linkage — resolve DG002
- Literature or case reports specifically evaluating ACE inhibitors (ideally perindopril) in malignant hypertensive renal disease
- A defined renal-function monitoring plan (serum creatinine, eGFR) given the known risk of ACE-inhibitor-induced GFR decline in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

