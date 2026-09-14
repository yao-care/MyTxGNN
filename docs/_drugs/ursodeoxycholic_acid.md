---
layout: default
title: Ursodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 679
evidence_level: L5
indication_count: 1
---

# Ursodeoxycholic Acid
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

# Ursodeoxycholic Acid: From Gallstone Dissolution/PBC to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a hydrophilic bile acid used to dissolve gallstones and treat primary biliary cholangitis (PBC) through cytoprotective and choleretic effects. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph association with no direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gallstone dissolution; Primary Biliary Cholangitis (PBC) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.86% (rank 2731) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

UDCA's known pharmacology involves three mechanisms: (1) reducing bile cholesterol saturation to promote gallstone dissolution, (2) cytoprotective/anti-apoptotic effects on hepatocytes (the basis for its PBC use), and (3) partial modulation of bile acid receptor signaling (FXR/TGR5). HoFH, by contrast, results from loss-of-function defects in the LDL receptor pathway (LDLR, APOB, PCSK9, or LDLRAP1), and effective therapies must work through LDLR-independent routes — PCSK9 inhibition, ANGPTL3 inhibition, MTP inhibition, or LDL apheresis.

While bile acid synthesis (via CYP7A1) intersects biochemically with cholesterol metabolism, UDCA is not a potent FXR agonist (unlike obeticholic acid), and there is currently no biochemical evidence that it can bypass or compensate for LDL receptor deficiency. The TxGNN score of 99.86% is very high, but it reflects a graph-topology association rather than a validated pharmacological pathway — the mechanistic link to HoFH should be considered speculative at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Ursodeoxycholic acid holds 3 active NPRA registrations in Malaysia (market status: marketed). However, the current data pull did not return license numbers, product names, dosage forms, or approved indication text for these registrations (see Data Gap DG001 — blocking). These details need to be retrieved from the NPRA product registry or package insert before a full market summary can be produced.

## Safety Considerations

Please refer to the package insert for safety information. A dedicated data pull for key warnings, contraindications, and drug interactions returned no results (DDI query status: not found), and this gap is flagged as **blocking** for safety evaluation (DG001) — it must be resolved before this candidate can proceed to any clinical assessment stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the proposed mechanism does not plausibly address the LDL-receptor defect underlying HoFH. Combined with a blocking safety data gap (DG001), this candidate is not ready to advance.

**To proceed, the following is needed:**
- TFDA/NPRA package insert with warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Targeted literature/trial search for UDCA in familial hypercholesterolemia or related lipid disorders, since the current pull returned zero hits
- Complete Malaysia license details (license numbers, product names, dosage forms, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

