---
layout: default
title: Hydroquinone
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 4
---

# Hydroquinone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# HYDROQUINONE: From [Indication Not Specified] to Seborrheic Keratosis

## One-Sentence Summary

> Hydroquinone (DrugBank DB09526) is a marketed topical agent whose formal original-indication text is not captured in the current evidence pack, though annotated evidence describes it as a tyrosinase inhibitor used in pigmentary skin conditions.
> The TxGNN model predicts it may be effective for **Seborrheic Keratosis**, but this is currently supported by **0 clinical trials** and only **2 publications**, both of which relate to a pigmented subtype (dermatosis papulosa nigra) rather than seborrheic keratosis itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA/NPRA license `approved_indication_text` is empty in this evidence pack |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is not available in this evidence pack (Data Gap DG002, High severity). Based on annotations embedded in the evidence, hydroquinone acts as a **tyrosinase inhibitor**, reducing melanin synthesis — a mechanism consistent with its well-known role in topical pigmentary/depigmenting therapy (this is also reflected indirectly in the clinical-trial evidence collected for another candidate in this pack, which is dominated by melasma trials).

The relevance to seborrheic keratosis is narrow and indirect. Seborrheic keratosis is fundamentally a benign keratinocyte-proliferative lesion, a process hydroquinone's tyrosinase-inhibition mechanism does not act on. The one plausible link is to **dermatosis papulosa nigra (DPN)** — a pigmented, facially-distributed variant of seborrheic keratosis common in darker-skinned populations — where excess pigmentation (not keratinocyte proliferation) is the treatable feature.

Because of this, the mechanistic rationale supports at most a subset of seborrheic keratosis presentations (pigmented facial lesions in patients with skin of color), not the disease category as a whole. The TxGNN score (99.73%) reflects strong graph-level association but is not yet corroborated by disease-specific clinical or mechanistic studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Cohort | J Plast Reconstr Aesthet Surg | Prospective observational study in Asian patients proposing a combination treatment algorithm for facial pigmentary disorders; not specific to seborrheic keratosis. |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | J Drugs Dermatol | Reviews treatment options for dermatosis papulosa nigra (DPN), a pigmented seborrheic-keratosis variant common in African-American/Afro-Caribbean patients; notes DPN histology closely resembles seborrheic keratosis. |

---

## Malaysia Market Information

NPRA records show **3 active registrations** for hydroquinone, but license number, product name, dosage form, manufacturer, and approved-indication text were not populated in this evidence pack extraction.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (3 licenses on file) | Not available | Not available | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: retrieval of TFDA/NPRA label warnings and contraindications is a Blocking data gap — DG001 — and is required before any safety evaluation can proceed; see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Seborrheic keratosis has no direct clinical trial support, and the only two supporting publications relate to a pigmented subtype (DPN), not the disease's core keratinocyte-proliferative pathology.
- Package-insert warnings/contraindications are missing (DG001, Blocking severity) — per evidence-pack policy this alone blocks entry into the S1 safety review stage.

**To proceed, the following is needed:**
- Retrieve NPRA package insert warnings and contraindications (DG001)
- Obtain a formal DrugBank mechanism-of-action record (DG002)
- Fill in complete Malaysia license details (product names, dosage forms, indication text) for the 3 existing registrations
- Clarify whether the predicted indication should be narrowed specifically to DPN/pigmented seborrheic keratosis rather than the broader disease category
- Note: other ranked candidates in this pack (e.g., "exanthem," rank 3) show apparent disease-label mismatches in their clinical trial evidence (melasma trials mapped to an unrelated disease node) — worth a knowledge-graph mapping review before further use of this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

