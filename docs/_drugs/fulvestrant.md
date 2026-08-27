---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

> Fulvestrant is a selective estrogen receptor degrader (SERD) used to treat hormone receptor-positive, HER2-negative advanced or metastatic breast cancer.
> The TxGNN model predicts it may be effective for **HIV Infectious Disease**,
> but this direction is currently supported by **0 clinical trials** and only **1 tangentially related publication** (on HTLV-1, a distinct retrovirus), indicating a high-score but essentially unvalidated signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not disclosed in NPRA license text (all 5 sampled license records have empty `approved_indication_text`) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fulvestrant is not available in this evidence pack. Based on known information, fulvestrant is a selective estrogen receptor degrader (SERD) that binds to and accelerates degradation of the estrogen receptor; its efficacy in hormone receptor-positive breast cancer is well established.

There is no known pharmacological pathway connecting estrogen receptor degradation to antiretroviral or anti-HIV activity. The only literature item returned for this prediction is a 2025 cross-omics analysis of HTLV-1-associated myelopathy (HAM) — a neuroinflammatory disease caused by a different retrovirus (HTLV-1, not HIV) — and it does not mention fulvestrant, estrogen signaling, or any anti-HIV mechanism.

Given the absence of a plausible mechanistic bridge and the complete lack of drug-specific clinical or preclinical evidence, this TxGNN prediction should be treated as an unvalidated high-score model artifact rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics Analysis (preprint) | Research Square | Multi-cohort cross-omics study of HTLV-1-associated myelopathy (HAM) mechanisms and therapeutic targets; does not address HIV or fulvestrant. |

## Malaysia Market Information

The evidence pack confirms fulvestrant is marketed in Malaysia (market status: 已上市) with **8** active NPRA registrations. However, the returned license records contain no license numbers, product names, dosage forms, or indication text, so a per-license table cannot be produced from this data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV indication is supported only by TxGNN's model score (L5, decision stage S0) — there are no clinical trials and only one unrelated (HTLV-1) publication, with no mechanistic rationale linking ER degradation to antiretroviral activity.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently Blocking data gap DG001) before any S1 safety screening can begin
- Detailed mechanism of action (MOA) data (currently High-severity data gap DG002)
- Dedicated preclinical or mechanistic studies specifically testing fulvestrant against HIV/retroviral targets, since existing literature does not address this indication
- Confirmed original indication text and full license details from NPRA (current records are blank)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

