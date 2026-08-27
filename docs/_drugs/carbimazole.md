---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 3
---

# Carbimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone Beta (RTHβ)

## One-Sentence Summary

Carbimazole is a thionamide antithyroid agent, originally used to treat hyperthyroidism/thyrotoxicosis (e.g. Graves' disease) by inhibiting thyroid peroxidase (TPO).
The TxGNN model predicts it may be effective for **Resistance to Thyroid Hormone due to a Mutation in Thyroid Hormone Receptor Beta (RTHβ)**,
but this direction is currently supported by **0 clinical trials** and only **1 case report**, so it remains an early-stage research signal rather than a validated indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism / thyrotoxicosis (inferred from drug class and mechanism; TFDA/NPRA licence indication text was not returned in this data pull — see Malaysia Market Information) |
| Predicted New Indication | Resistance to Thyroid Hormone due to a Mutation in Thyroid Hormone Receptor Beta (RTHβ) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Carbimazole is not available in this evidence pack (data gap). Based on known pharmacology reflected in the evidence, Carbimazole is a prodrug of methimazole belonging to the thionamide/antithyroid drug class; it inhibits thyroid peroxidase (TPO), blocking synthesis of thyroid hormone. Its efficacy in hyperthyroidism is well established clinically.

In RTHβ, a mutation in the thyroid hormone receptor beta makes the pituitary insensitive to thyroid hormone negative feedback. As a result, TSH is not appropriately suppressed and continues to stimulate the thyroid gland; some patients present with peripheral hyperthyroid symptoms such as palpitations and weight loss despite a structurally normal thyroid axis.

Mechanistically, Carbimazole's TPO inhibition could reduce the amount of thyroid hormone synthesized and thereby relieve these peripheral hyperthyroid symptoms. However, it does not correct the underlying receptor defect — it would function only as symptomatic adjunct therapy, not disease-modifying treatment. This is a plausible but unproven extension of an established mechanism, consistent with the "Research Question" stage this candidate is currently scored at.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case Report | BMJ Case Reports | Young man with persistently elevated free T4 (25–35.7 pmol/L) and non-suppressed TSH (6.78–22.1 mIU/L) over 10 years, treated intermittently with carbimazole; presentation consistent with a thyroid hormone resistance-type picture rather than classic Graves' disease. |

---

## Malaysia Market Information

Malaysia (NPRA) market status confirms Carbimazole is marketed with **4 registered licences**. However, the licence numbers, product names, dosage forms, manufacturers, and approved indication texts were not populated in this data pull — this is a gap in the source query, not an absence of registration. These details should be pulled directly from the NPRA product registry before this evaluation proceeds further.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not returned in this data pull — this is flagged as a **Blocking** data gap, DG001, which prevents a full S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RTHβ indication is supported only by a plausible mechanistic rationale and a single case report (L4, decision stage S1, model-scored "Research Question") — there are no clinical trials and no controlled studies. Combined with a blocking safety data gap (TFDA/NPRA label warnings and contraindications unavailable), this candidate does not yet meet the bar to proceed.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the TFDA/NPRA package insert for warnings, contraindications, and DDI data
- Resolve DG002 (High): obtain formal MOA data from DrugBank to confirm/refine the mechanistic rationale
- Full-text review of the single available RTHβ case report (PMID 24165508) and a broader literature search, since only 1 publication currently supports this specific indication
- Complete the NPRA licence detail fields (licence number, product name, dosage form, approved indication text) for the 4 registered products

---

## Other TxGNN-Predicted Indications for Carbimazole (Not Covered in Detail Above)

This evidence pack contained two additional predicted indications with notably different evidence strength, worth flagging for separate evaluation:

| Rank | Disease | Score | Evidence Level | Recommendation |
|------|---------|-------|-----------------|-----------------|
| 2 | Neonatal thyrotoxicosis | 99.41% | L3 | Proceed with Guardrails |
| 3 | Hyperthyroxinemia | 99.21% | L4 | Hold |

Rank 2 (neonatal thyrotoxicosis) is backed by 20 publications, including cohort studies, and reflects an already-established clinical practice (transplacental maternal Graves' antibodies causing neonatal thyrotoxicosis, treated with antithyroid drugs per ATA/ESPE guidance) — its evidence base is materially stronger than the RTHβ candidate featured above and may warrant prioritization if this evaluation is intended to identify the most actionable repurposing opportunity for Carbimazole.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

