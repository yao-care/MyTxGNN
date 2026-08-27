---
layout: default
title: Ferrous Gluconate
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 5
---

# Ferrous Gluconate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ferrous Gluconate: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferrous gluconate is a standard oral iron salt used to treat and prevent iron-deficiency anemia. The TxGNN model predicts it may also be effective for **Plummer-Vinson syndrome**, a condition whose underlying cause is chronic iron deficiency, but this specific application is currently supported only by mechanistic reasoning — **no dedicated clinical trials or published literature** were found for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available registry text (data gap); ferrous gluconate is a well-established iron salt used for treatment/prevention of iron-deficiency anemia |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ferrous gluconate is not currently available in this dataset. Based on known pharmacology, ferrous gluconate is an oral iron salt that replenishes iron stores and supports hemoglobin synthesis — its efficacy in correcting iron-deficiency anemia is well established and mechanistically may be applicable to any condition rooted in chronic iron deficiency.

Plummer-Vinson syndrome (also known as Paterson-Brown-Kelly syndrome) is a classic example: its core etiology is long-standing iron-deficiency anemia, and oral or injectable iron supplementation is the current textbook standard of care, used to correct the deficiency and relieve associated esophageal web formation and dysphagia. The mechanistic link between ferrous gluconate and this indication is therefore very strong.

However, this represents an established standard of care rather than a novel repurposing hypothesis. This dataset does not include any clinical trials or literature specifically indexed for Plummer-Vinson syndrome, which more likely reflects a database coverage gap than a true absence of clinical evidence — the underlying rationale (treating iron deficiency) is not in dispute. Other TxGNN candidates for this drug (e.g., vitamin B12/folate-independent megaloblastic anemia, non-syndromic esophageal malformation, biotin metabolic disease) were assessed as mechanistically implausible or contradictory and are recommended for **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Ferrous gluconate currently holds **7 active marketing authorizations** in Malaysia (market status: Marketed). Detailed license-level information (authorization numbers, product names, dosage forms, and approved-indication text) is not available in the current dataset and will need to be pulled directly from NPRA records to complete this section.

---

## Safety Considerations

Please refer to the package insert for safety information.

No key warnings, contraindications, or drug-drug interaction data are currently available for this drug (DDI search status: not found). Notably, TFDA/NPRA package-insert warnings and contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before a formal safety review (S1) can be considered complete.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale linking iron supplementation to Plummer-Vinson syndrome is strong and consistent with established clinical practice, but it is unsupported by any indication-specific trials or literature in this dataset (Evidence Level L4), and a blocking safety data gap remains open.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently blocking safety review (DG001)
- DrugBank mechanism-of-action data (DG002)
- Malaysia license-level detail (product names, dosage forms, approved indication text)
- Targeted literature/clinical evidence search specific to Plummer-Vinson syndrome to confirm whether the current absence of hits reflects a true evidence gap or a search/coverage limitation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

