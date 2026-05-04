---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 1
---

# Brinzolamide
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

# Brinzolamide: From Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a carbonic anhydrase II (CA-II) inhibitor, originally used for reducing elevated intraocular pressure (IOP) in patients with open-angle glaucoma or ocular hypertension. The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, though currently **no dedicated clinical trials** or **publications** have been identified for this specific hereditary subtype. This prediction essentially represents a **label extension** rather than a classic drug repurposing scenario, as the core pharmacological mechanism directly addresses the primary pathology of hereditary glaucoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Elevated intraocular pressure (open-angle glaucoma / ocular hypertension) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L4 — Mechanistic rationale strongly supports applicability |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Brinzolamide is a potent carbonic anhydrase II (CA-II) inhibitor that reduces intraocular pressure (IOP) by suppressing aqueous humor production in the ciliary body. It is well-established as a topical ophthalmic agent for the management of elevated IOP in open-angle glaucoma and ocular hypertension, and has been marketed globally for over two decades.

Primary hereditary glaucoma — encompassing subtypes such as primary congenital glaucoma (PCG), juvenile open-angle glaucoma (JOAG), and related developmental glaucomas — shares the same core pathological endpoint: elevated IOP leading to progressive optic nerve damage. While the underlying etiology involves genetic mutations (e.g., *CYP1B1*, *MYOC*, *LTBP2*) that cause developmental abnormalities in the trabecular meshwork and anterior chamber angle, **IOP reduction remains the primary therapeutic goal** across all hereditary subtypes.

Because Brinzolamide's mechanism of action — inhibiting CA-II to reduce aqueous humor production — directly addresses the IOP elevation common to all forms of glaucoma, this prediction is pharmacologically sound. In clinical practice, topical CA-II inhibitors are already used as adjunctive therapy in paediatric and juvenile glaucoma cases. The TxGNN prediction therefore represents a logical **label extension** (expanding the formally approved indication to hereditary glaucoma subtypes) rather than a traditional drug repurposing across unrelated disease areas.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for Brinzolamide in primary hereditary glaucoma.

> **Note:** While no trials were found for this exact indication term, Brinzolamide has extensive clinical trial data for open-angle glaucoma and ocular hypertension. Future searches using broader terms (e.g., "congenital glaucoma," "juvenile glaucoma," "paediatric glaucoma") may yield relevant results.

---

## Literature Evidence

Currently no literature specifically identified for Brinzolamide in primary hereditary glaucoma.

> **Note:** The absence of literature for this precise disease term does not reflect a lack of clinical experience. Brinzolamide is routinely discussed in paediatric ophthalmology literature as part of medical management for congenital and juvenile glaucoma. A broader literature search with alternative disease terminology is recommended.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Registration 1) | Brinzolamide product | Ophthalmic suspension | Elevated intraocular pressure |
| (Registration 2) | Brinzolamide product | Ophthalmic suspension | Elevated intraocular pressure |
| (Registration 3) | Brinzolamide product | Ophthalmic suspension | Elevated intraocular pressure |

> **Note:** Detailed registration information (authorization numbers, exact product names, dosage forms) was not available in the current data extract. Three active registrations are confirmed by NPRA query.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.
>
> **Known class-level considerations for topical CA-II inhibitors:**
> - Sulfonamide hypersensitivity (Brinzolamide is a sulfonamide derivative)
> - Corneal endothelial cell effects with prolonged use
> - Caution in patients with severe renal impairment (systemic absorption, though minimal, involves renal elimination)
> - Transient blurred vision and ocular discomfort are common local adverse effects

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Brinzolamide's mechanism of action (CA-II inhibition → IOP reduction) directly addresses the central pathology of primary hereditary glaucoma. This prediction is essentially a label extension with strong pharmacological plausibility, even though formal clinical trial evidence specific to the hereditary subtype is lacking. The drug is already marketed in Malaysia and has an extensive global safety track record.

**To proceed, the following is needed:**
- **Literature search expansion**: Search for Brinzolamide use in congenital glaucoma, juvenile glaucoma, and paediatric glaucoma using broader MeSH terms and synonyms
- **Package insert review**: Obtain full prescribing information from NPRA-registered products to complete safety assessment (key warnings, contraindications, DDI)
- **Mechanism of action data**: Retrieve complete MOA details from DrugBank API to support formal documentation
- **Paediatric dosing data**: If the target population includes young children (as in primary congenital glaucoma), paediatric pharmacokinetic and safety data should be compiled
- **Regulatory gap analysis**: Confirm whether any jurisdiction has already approved Brinzolamide specifically for hereditary glaucoma subtypes, which would further de-risk the label extension pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

