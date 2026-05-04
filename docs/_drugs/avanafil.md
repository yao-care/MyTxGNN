---
layout: default
title: Avanafil
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 0
---

# Avanafil
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

# Avanafil: From Erectile Dysfunction — Repurposing Evaluation (Prediction Data Unavailable)

## One-Sentence Summary

Avanafil (DrugBank: DB06237) is a selective phosphodiesterase type 5 (PDE5) inhibitor primarily used to treat erectile dysfunction, confirmed as marketed in Malaysia with 3 registered products.
However, **no TxGNN repurposing predictions are present** in this Evidence Pack, and both mechanism of action data and package insert safety information are flagged as unresolved data gaps.
This report documents the current data status and defines the remediation steps required before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile dysfunction (based on pharmacological background; not retrieved from NPRA records in this Evidence Pack) |
| Predicted New Indication | Not available — TxGNN prediction data absent |
| TxGNN Prediction Score | N/A |
| Evidence Level | Insufficient Data |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

Three data gaps — two of which are blocking — prevent a complete repurposing analysis from being generated at this time.

**1. No TxGNN Predicted Indications**
The `predicted_indications` array in the Evidence Pack is empty. Without a target indication from the TxGNN model, there is no repurposing candidate to evaluate. This is the fundamental input required for all downstream sections of this report.

**2. Mechanism of Action Unavailable**
Based on established pharmacology, Avanafil belongs to the same drug class as sildenafil (Viagra) and tadalafil (Cialis) — selective PDE5 inhibitors that increase cyclic GMP in vascular smooth muscle, producing vasodilation. This class has already yielded approved repurposing successes: sildenafil and tadalafil are both approved for pulmonary arterial hypertension (PAH), and tadalafil is approved for benign prostatic hyperplasia (BPH). However, formal MOA documentation from DrugBank (DB06237) must be retrieved before mechanistic reasoning can be included in a validated evidence report.

**3. Package Insert Data Unavailable (Blocking for Safety Screening)**
Key warnings and contraindications were not retrieved. For a PDE5 inhibitor, this is particularly critical: the class carries an absolute contraindication against concurrent nitrate use (risk of severe hypotension), and clinically significant interactions with strong CYP3A4 inhibitors (e.g., ketoconazole, ritonavir, clarithromycin). This data gap prevents the mandatory S1 safety screening step from being completed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

> **Note:** Clinical trial evidence cannot be collected until a specific repurposing indication is identified by the TxGNN model. Once a predicted indication is available, searches of ClinicalTrials.gov and ICTRP should be conducted for that indication paired with Avanafil.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

> **Note:** Literature collection requires a target indication. Upon re-running the TxGNN prediction pipeline and obtaining a candidate indication, PubMed searches should be performed accordingly.

---

## Malaysia Market Information

Three product registrations are confirmed as currently marketed in Malaysia; however, detailed registration data (MAL numbers, product names, dosage forms, approved indication text) was not populated in the Evidence Pack returned by the NPRA query.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| (Not retrieved) | (Not retrieved) | (Not retrieved) | (Not retrieved) |
| (Not retrieved) | (Not retrieved) | (Not retrieved) | (Not retrieved) |
| (Not retrieved) | (Not retrieved) | (Not retrieved) | (Not retrieved) |

To retrieve complete registration details, query the **NPRA e-Pharmacy database** directly using the INN "AVANAFIL". The 3 registered products are expected to carry the approved indication of erectile dysfunction.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Priority action required:** Retrieve the Summary of Product Characteristics (SPC) or package leaflet from the NPRA portal for all 3 registered Avanafil products. Key safety items to extract for a PDE5 inhibitor include:
> - Contraindication with organic nitrates and nitric oxide donors (absolute)
> - Hypotensive effects, especially in combination with antihypertensives or alpha-blockers
> - Drug interactions with CYP3A4 inhibitors (dose adjustment required)
> - Cardiovascular precautions in patients with recent MI, stroke, or unstable angina

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Avanafil is critically incomplete — no TxGNN repurposing predictions have been generated, and both MOA and safety data remain unresolved. A meaningful repurposing evaluation cannot be written in this state; all core analytical sections are blocked.

**To proceed, the following is needed:**

1. **Re-run the TxGNN prediction pipeline** for DB06237 (Avanafil) to generate predicted indication candidates with confidence scores
2. **Retrieve MOA from DrugBank API** (entry DB06237) — expected to document selective PDE5 inhibition and cyclic GMP pathway
3. **Download NPRA product package inserts** for all 3 registered products to extract:
   - Full approved indication text (to populate the Malaysia Market table)
   - Key warnings and contraindications
   - Drug-drug interaction profile
4. **Retrieve full license details** from the NPRA e-Pharmacy system (MAL numbers, product names, dosage forms, manufacturer information)
5. **Re-generate the Evidence Pack** once data gaps DG001 and DG002 are resolved, then re-submit for a complete evaluation report

---

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

