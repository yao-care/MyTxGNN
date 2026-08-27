---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a classic osmotic diuretic long used to reduce intracranial/intraocular pressure and promote diuresis in acute oliguric states. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, a rare hereditary hyponatremia disorder, but this direction is currently supported by **0 clinical trials** and only **1 general review publication** that does not specifically address mannitol or NSIAD.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osmotic diuretic (reduction of intracranial/intraocular pressure, promotion of diuresis) — specific NPRA license indication text was not captured in this data pull |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known pharmacology, mannitol is a classic osmotic diuretic; its efficacy in reducing intracranial pressure, treating cerebral edema, lowering intraocular pressure, and promoting forced diuresis has been well established for decades, and mechanistically it may theoretically extend to conditions involving abnormal free-water handling.

NSIAD is a rare inherited disorder caused by constitutive (gain-of-function) activation of the vasopressin V2 receptor, leading to inappropriate water retention and hyponatremia independent of vasopressin levels. In theory, an osmotic diuretic could promote free-water excretion and help correct the resulting hyponatremia, which is the conceptual basis for TxGNN's prediction.

However, the only literature returned for this candidate is a general review on pitfalls in evaluating hyponatremia — it does not discuss mannitol specifically, nor does it address NSIAD as a distinct treatment target. This is a purely inferential mechanistic link rather than an evidence-based one, and no clinical trials exist to test it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European journal of internal medicine | General review of common pitfalls in evaluating hyponatremic patients; addresses diagnostic/management errors in hyponatremia broadly but does not discuss mannitol or NSIAD specifically |

---

## Malaysia Market Information

The evidence pack confirms Mannitol is marketed in Malaysia with **7 total registered licenses**, but license-level details (authorization numbers, product names, dosage forms, approved indication text) were not populated in this data pull and cannot be tabulated here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for mannitol in NSIAD is plausible in theory but rests on a single general review that does not mention mannitol or NSIAD directly, with zero supporting clinical trials — evidence level L5 (model prediction only). This is insufficient to justify further investment at this stage.

**To proceed, the following is needed:**
- TFDA/NPRA-equivalent package insert data (warnings, contraindications) to complete the S1 safety screen (currently blocking per DG001)
- Confirmed mechanism of action (DrugBank) data (DG002)
- Targeted literature/case search specifically on osmotic diuretics or mannitol in NSIAD or V2-receptor-mediated hyponatremia
- Complete Malaysia license-level detail (product names, dosage forms, approved indication text) for the 7 existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

