---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From Diffuse Large B-Cell Lymphoma to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) approved for diffuse large B-cell lymphoma (DLBCL).
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's target (CD79b, a B-cell receptor component) has no known mechanistic overlap with HER2-driven epithelial tumor biology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diffuse Large B-Cell Lymphoma (DLBCL) *(sourced from mechanistic rationale text; formal TFDA/NPRA license indication text not yet retrieved — see Malaysia Market Information)* |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for polatuzumab vedotin is not fully available in this evidence pack, but the underlying rationale record indicates it is an antibody-drug conjugate targeting CD79b, a component of the B-cell receptor complex, and it is approved for diffuse large B-cell lymphoma — a hematologic malignancy of B-cell origin.

HER2 positive breast carcinoma, by contrast, is driven by amplification and overexpression of HER2/ERBB2, a receptor tyrosine kinase expressed on epithelial tumor cells. There is no established biological overlap between CD79b/B-cell antigen biology and HER2-driven epithelial signaling, and breast cancer cells are not known to express CD79b.

Given this absence of any plausible mechanistic bridge, the high TxGNN score (99.34%) is not corroborated by biology, clinical trials, or literature. The evidence pack itself flags this as a likely **false-positive model prediction** rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

NPRA records confirm 2 active registrations for polatuzumab vedotin ("已上市" market status), but license number, product name, dosage form, and approved indication text were not returned in this data pull — retrieval of the full license record is required (see Data Gap DG001) before this table can be completed.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC) carrying a cytotoxic microtubule-inhibitor payload |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations (ADC with cytotoxic payload) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for this indication, and the proposed mechanistic link between CD79b-targeted ADC activity and HER2-driven breast carcinoma is biologically implausible — the evidence pack itself identifies this as a likely false-positive TxGNN prediction. The candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) to close Data Gap DG001
- Confirmed full mechanism-of-action data via DrugBank to close Data Gap DG002
- Any preclinical evidence of CD79b expression in HER2-positive breast tumors, absent which this candidate should likely be deprioritized rather than advanced
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

