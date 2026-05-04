---
layout: default
title: Atazanavir Sulfate
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 0
---

# Atazanavir Sulfate
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

# Atazanavir Sulfate: HIV Protease Inhibitor — Repurposing Analysis Pending

## One-Sentence Summary

Atazanavir Sulfate is an antiretroviral protease inhibitor used in combination therapy for HIV-1 infection.
This evidence pack contains **no TxGNN repurposing predictions**, and critical drug-level data — including mechanism of action, licence details, and safety warnings — are absent.
A full repurposing evaluation cannot be completed until the identified data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

> **Note:** The Clinical Trial Evidence, Literature Evidence, and "Why is This Prediction Reasonable?" sections are omitted because `predicted_indications` is empty in this evidence pack. Once TxGNN predictions are generated, those sections will be populated automatically.

---

## Malaysia Market Information

The NPRA query confirmed 1 registered product with a market status of **Marketed**. However, all product-level fields (licence number, product name, dosage form, manufacturer, approved indication) were returned as empty strings in this evidence pack and cannot be displayed.

| Authorisation Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | — |

*Detailed registration data should be retrieved directly from the [NPRA Product Registration Search](https://www.npra.gov.my/index.php/en/registration/product-registration.html).*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions are present in this evidence pack, and key drug-level and regulatory data are missing — making any meaningful repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Run TxGNN prediction pipeline** for Atazanavir Sulfate to generate candidate repurposing indications
- **Populate DrugBank data** (MOA, drug categories, known interactions) — the DrugBank query returned 1 result but no fields were captured; the DrugBank entry for atazanavir is `DB01072`
- **Download and parse the NPRA / TFDA package insert PDF** to extract warnings, contraindications, and the officially approved indication text (Data Gap DG001 — classified as *Blocking*)
- **Re-query the NPRA product register** to retrieve licence number, product name, dosage form, and manufacturer details for the 1 confirmed registration
- **Resolve MOA data gap (DG002)** via DrugBank API to enable mechanistic plausibility analysis for any predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

