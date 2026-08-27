---
layout: default
title: Clobetasone
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Clobetasone
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

# Clobetasone: From Topical Corticosteroid Use to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Clobetasone is a topical corticosteroid (glucocorticoid receptor agonist) used for inflammatory skin conditions.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma**,
but this direction is currently supported only by mechanistic reasoning — **no clinical trials and no literature** specific to Clobetasone in this indication have been found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current Malaysia registration data; drug class is topical corticosteroid (glucocorticoid receptor agonist) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Clobetasone is not available. Based on known information, Clobetasone is a topical glucocorticoid receptor agonist — a class whose efficacy in inflammatory skin conditions is well established.

Mechanistically, topical corticosteroids suppress local inflammation and can induce T-cell apoptosis. This is directly relevant to primary cutaneous T-cell lymphoma (CTCL): a chemically related topical steroid, clobetasol propionate, is an established standard treatment for early-stage CTCL/mycosis fungoides. Since both the original use (inflammatory dermatoses) and the predicted new indication (a cutaneous lymphoma) are treated at the skin surface, the route of administration is plausibly compatible — unlike several of TxGNN's other top-ranked predictions for this drug (e.g. Crohn's colitis, nephrotic syndrome, adrenocortical insufficiency), which would require systemic/oral corticosteroid activity that a topical formulation cannot provide.

However, this mechanistic plausibility has not yet been tested for Clobetasone specifically — no drug-disease-specific trials or publications currently exist to confirm it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Clobetasone has 3 active registrations in Malaysia (market status: ✓ Marketed). Detailed license-level information (registration numbers, product names, dosage forms, approved indication text) was not returned in the current NPRA data pull, so individual license entries cannot be listed here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is evidence level L5 (model prediction only) — searches of ClinicalTrials.gov, ICTRP, and PubMed returned zero results for Clobetasone in primary cutaneous T-cell lymphoma. In addition, a Blocking data gap exists: NPRA package insert warnings and contraindications are unavailable, which prevents even an initial (S1) safety assessment.

**To proceed, the following is needed:**
- NPRA package insert — warnings/precautions and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Complete license-level registration details (product names, dosage forms, approved indication text) for the 3 Malaysia registrations
- Preclinical or case-report-level evidence specifically for Clobetasone in CTCL/mycosis fungoides, given the absence of registered trials or publications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

