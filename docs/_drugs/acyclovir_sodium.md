---
layout: default
title: Acyclovir Sodium
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 0
---

# Acyclovir Sodium
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

# Acyclovir Sodium: Antiviral Agent — Repurposing Evaluation Pending

## One-Sentence Summary

Acyclovir Sodium is a nucleoside analogue antiviral agent with well-established use against herpesvirus infections, including herpes simplex virus (HSV) and varicella-zoster virus (VZV).
The current Evidence Pack does not contain any TxGNN repurposing predictions for this drug — the prediction pipeline has not yet been executed or returned results for this candidate.
Malaysia's NPRA database confirms 1 active registration, but product-level details were not retrievable from the current data extract.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Herpesvirus infections (herpes simplex, varicella-zoster) |
| Predicted New Indication | Not available — no TxGNN predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not applicable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Malaysia Market Information

The NPRA query confirmed 1 active registration for Acyclovir Sodium as of the data cut-off (2026-04-04). However, product-level fields — including license number, brand name, dosage form, and approved indication text — were not populated in the current data extract.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | Details require direct NPRA lookup |

> **Note:** To complete this section, retrieve the full product monograph from the [NPRA Product Search portal](https://www.npra.gov.my/) using the search term "ACYCLOVIR SODIUM".

---

## Safety Considerations

Please refer to the package insert for safety information. No warning or contraindication data was available in the current Evidence Pack, and no drug–drug interaction records were found in the DDI database query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Acyclovir Sodium is structurally incomplete — no TxGNN repurposing predictions have been generated, and critical data fields (MOA, approved indication text, safety warnings, license details) are missing. A meaningful repurposing evaluation cannot be conducted until these gaps are resolved.

**To proceed, the following is needed:**

- **Run TxGNN prediction pipeline** for ACYCLOVIR SODIUM to generate ranked repurposing candidates with supporting evidence
- **Retrieve DrugBank ID and MOA** — query DrugBank by INN ("acyclovir") to obtain DB ID, pharmacological class, and mechanism of action
- **Parse NPRA product monograph** — download the registered product's package insert PDF to extract approved indication text, key warnings, and contraindications (Data Gap DG001 — Blocking)
- **Complete NPRA license record** — populate license number, brand name, dosage form, manufacturer, and full indication text from the NPRA portal (1 registration confirmed but details empty)
- **Re-run Evidence Pack generation** (v5) once the above inputs are available to produce a full L1–L5 evidence evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

