---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 514
evidence_level: L5
indication_count: 2
---

# Octreotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Octreotide: From Neuroendocrine Disorders to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a somatostatin analog originally used to treat acromegaly, carcinoid syndrome, VIPoma, and esophageal variceal bleeding via somatostatin receptor (SSTR2/SSTR5) pathways. TxGNN predicts it may be effective for **vulvar inverted follicular keratosis**, but this direction is currently supported by **zero clinical trials** and **zero publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Malaysia registration data; based on the evidence pack's mechanistic description, known clinical uses include acromegaly, carcinoid syndrome, VIPoma, and esophageal variceal bleeding |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.58% (rank 6464) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on the repurposing rationale provided, octreotide is a somatostatin analog that acts mainly through SSTR2/SSTR5 receptors to suppress the growth hormone/IGF-1 axis, producing anti-proliferative and anti-angiogenic effects. Clinically it is used for acromegaly, carcinoid syndrome, VIPoma, and esophageal variceal bleeding.

Vulvar inverted follicular keratosis is a benign keratinocyte proliferative lesion, generally associated with HPV infection or local irritation. There is no established literature linking somatostatin receptor signaling to this type of keratinocyte proliferation.

The evidence pack itself flags this prediction as likely spurious: the high TxGNN score (0.996) probably reflects structural similarity between "keratosis"-related nodes in the knowledge graph rather than a genuine biological mechanism. A second, similarly unsupported prediction for the same drug — seborrheic keratosis (score 0.995) — reinforces this pattern, as that condition is driven by FGFR3/PIK3CA somatic mutations with no known connection to somatostatin signaling either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

License-level details (product names, dosage forms, manufacturers, approved indication text) are not available in the evidence pack. Only aggregate registration data is known: **6 registrations**, market status **Marketed** in Malaysia.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Warning/contraindication data (DG001) is flagged as a Blocking data gap and has not yet been retrieved from the TFDA label, so a full safety assessment cannot be completed at this stage.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies entirely on a TxGNN score (L5, model prediction only) with no clinical trials or literature support. The evidence pack's own mechanistic analysis suggests the high score likely reflects knowledge-graph structural similarity rather than a real biological link between somatostatin signaling and keratinocyte proliferation. Combined with a Blocking safety data gap (DG001), this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action (MOA) data from DrugBank (DG002)
- TFDA label warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Targeted literature/preclinical search for somatostatin receptor expression in keratinocyte or HPV-related proliferative lesions, to test biological plausibility before further investment
- Malaysia license-level details (product names, dosage forms, approved indication text) to confirm current marketed formulations and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

