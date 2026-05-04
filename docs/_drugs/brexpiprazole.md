---
layout: default
title: Brexpiprazole
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 0
---

# Brexpiprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Brexpiprazole: Drug Repurposing Evaluation Report (Pending Prediction)

## One-Sentence Summary

Brexpiprazole is a marketed atypical antipsychotic (DrugBank ID: DB09128) with 6 registered licenses in Malaysia. Currently, the TxGNN model has **no predicted new indications** for this drug, and key data gaps in mechanism of action and safety information need to be addressed before further evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *(Data not available in current license records)* |
| Predicted New Indication | **None** — No TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, **no TxGNN prediction has been generated** for Brexpiprazole, so there is no new indication to evaluate at this time.

Brexpiprazole is known to be a serotonin-dopamine activity modulator (SDAM), acting as a partial agonist at 5-HT₁A and dopamine D₂ receptors and an antagonist at 5-HT₂A receptors. It is approved internationally for the treatment of schizophrenia and as adjunctive therapy for major depressive disorder (MDD). However, the Evidence Pack lists the mechanism of action as a data gap, and no original indications are recorded in the current dataset.

Before a meaningful repurposing evaluation can be conducted, the following foundational data must be populated: (1) the detailed mechanism of action from DrugBank, (2) original approved indications from the Malaysian NPRA registry, and (3) TxGNN model predictions. Without these, it is not possible to assess mechanistic plausibility for any new therapeutic direction.

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication to query against).

## Literature Evidence

Currently no related literature available (no predicted indication to query against).

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(Not recorded)* | *(Not recorded)* | *(Not recorded)* | *(Not recorded)* |

> **Note:** 6 licenses are reported as registered, but detailed license information (authorization numbers, product names, dosage forms, and approved indications) is not available in the current dataset. The NPRA registry should be re-queried to populate these fields.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety data fields (key warnings, contraindications, drug-drug interactions) are currently unavailable. This is classified as a **Blocking** data gap — safety assessment cannot proceed until the package insert (PI) is obtained and parsed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications are available for Brexpiprazole, and critical data gaps exist in mechanism of action, approved indication text, and safety information. The evaluation cannot proceed until foundational data is populated.

**To proceed, the following is needed:**

1. **Populate TxGNN predictions** — Run the TxGNN model for Brexpiprazole (DB09128) to generate candidate repurposing indications
2. **Resolve MOA data gap (DG002)** — Query DrugBank API for detailed mechanism of action (partial agonist at 5-HT₁A/D₂, antagonist at 5-HT₂A)
3. **Resolve safety data gap (DG001, Blocking)** — Download and parse the package insert PDF from the NPRA website to extract warnings, contraindications, and DDI information
4. **Complete license records** — Re-query NPRA for full license details (authorization numbers, product names, dosage forms, approved indications) for all 6 registrations
5. **Populate original indications** — Confirm approved indications in Malaysia (expected: schizophrenia, adjunctive MDD treatment)

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

