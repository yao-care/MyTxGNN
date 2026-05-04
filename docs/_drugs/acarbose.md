---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acarbose: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Acarbose is an intestinal alpha-glucosidase inhibitor originally approved for managing postprandial hyperglycemia in type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**,
with **no clinical trials** and **no publications** currently supporting this direction.
The high prediction score is assessed as a likely false positive arising from the knowledge graph proximity between Stiff Person Syndrome and diabetes (both conditions involve GAD65 autoantibodies), rather than a genuine pharmacological connection.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (postprandial hyperglycemia management) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, Acarbose is an intestinal alpha-glucosidase inhibitor that competitively blocks the enzymes responsible for breaking down complex carbohydrates into absorbable glucose in the small intestine. This delays carbohydrate digestion and blunts postprandial blood glucose peaks, making it effective as an adjunct oral therapy for type 2 diabetes. Its action is entirely confined to the gastrointestinal lumen; it is minimally absorbed systemically.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder driven primarily by autoantibodies against GAD65 (Glutamic Acid Decarboxylase 65), an enzyme that catalyses the synthesis of the inhibitory neurotransmitter GABA. SPS and Type 1 Diabetes are known to share GAD65 autoantibodies — both conditions can co-exist in the same patient — which creates a strong edge in the TxGNN knowledge graph linking Acarbose (a diabetes drug) to SPS through their shared antigen.

However, this connection is assessed as a **false positive signal**. Acarbose acts exclusively at the intestinal brush border and has no known mechanism to modulate GAD65-directed autoimmunity, suppress central nervous system inhibitory tone, or provide any neuroprotection. The elevated TxGNN score reflects the graph topology of diabetes–SPS comorbidity rather than any pharmacologically actionable pathway. No preclinical or clinical evidence supports the use of Acarbose in SPS.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Five Acarbose product registrations are confirmed in the NPRA (National Pharmaceutical Regulatory Agency) database (Malaysia market status: Marketed). However, detailed product information — including product names, dosage forms, and approved indication text — was not captured in the current evidence pack. Please refer directly to the [NPRA Product Search](https://www.npra.gov.my/) for complete authorisation details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Classic Stiff Person Syndrome is assessed as a knowledge graph artefact — the model correctly identifies a disease that co-occurs with diabetes (via shared GAD65 autoantibodies) but Acarbose has no pharmacological mechanism relevant to autoimmune neurological disease. There is zero supporting clinical or preclinical evidence.

**To proceed, the following is needed:**
- **MOA data** from DrugBank (DB00284) to formally confirm the absence of any neuroimmunological or systemic immunomodulatory activity
- **Full package insert** (warnings, contraindications) from NPRA to complete the S1 safety screening — currently a blocking data gap
- **Complete Malaysia licence details** (product names, dosage forms, approved indications) from the NPRA database to populate the regulatory table
- If any further investigation of SPS is considered, a mechanistic hypothesis explaining how intestinal alpha-glucosidase inhibition could suppress GAD65 autoimmunity in the CNS would be required as a minimum prerequisite before any preclinical work is justified

> **Research Note:** Among all 9 predicted indications in this pack, **Pancreatic Agenesis** (rank 9, L4) presents the most biologically coherent — though still indirect — rationale for Acarbose use, as an adjunct to insulin therapy to smooth postprandial glycaemic variability in a condition of complete pancreatic insulin deficiency. This direction has 11 associated publications and may warrant a separate focused assessment.

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

