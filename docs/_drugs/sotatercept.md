---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Pulmonary Arterial Hypertension to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept is an ActRIIA-Fc fusion protein ("ligand trap") whose established pharmacology centers on pulmonary vascular remodeling in pulmonary arterial hypertension (PAH) and on bone metabolism. The TxGNN model predicts a possible link to **acute lymphoblastic leukemia (ALL)**, but this is a **model-only signal (L5)** — no clinical trials or publications currently support it, and the underlying mechanistic note itself flags the connection as weak and possibly a prediction artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — inferred from mechanistic notes in this evidence pack; formal NPRA label indication text was not available (blocking data gap) |
| Predicted New Indication | Acute Lymphoblastic Leukemia (disease) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data was not returned for this drug (data gap). Based on the mechanistic notes attached to this evidence pack, Sotatercept is an ActRIIA-Fc fusion protein that traps Activin A/B and GDF8/11 (TGF-β superfamily ligands), inhibiting SMAD2/3 signaling. This pathway underlies its established use in pulmonary vascular remodeling (PAH) and its effects on hematopoiesis/bone metabolism — the same superfamily targeted by the related ligand-trap luspatercept, which is approved for anemia in myelodysplastic syndrome.

For the top-ranked prediction, ALL, the evidence pack's own rationale is explicitly skeptical: Activin/GDF signaling relates to red-cell production and the bone-marrow microenvironment, but this is a hematopoietic *regulatory* mechanism, not a pathway with a direct link to the malignant lymphoblast proliferation that drives ALL. No clinical or literature evidence corroborates the connection, and the source note itself assesses this as a mechanistically weak link with a high likelihood of being TxGNN prediction noise rather than a genuine pharmacological signal.

In short, the biological rationale for Sotatercept's known indications is coherent, but its extension to ALL specifically is not well supported and should be treated as a low-confidence, exploratory signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Sotatercept is recorded as marketed in Malaysia with **2 active registrations** (NPRA, market status: 已上市). Per-license details (authorization number, product name, dosage form, approved indication text) were not returned in this data extract, so no license-level table can be presented at this time.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ALL prediction rests solely on a TxGNN topological score (L5) with zero supporting clinical trials or publications, and the mechanistic rationale supplied with the evidence pack itself rates the drug–disease link as weak and possibly noise. Separately, TFDA/NPRA label data (warnings/contraindications) is a **blocking** gap that prevents even an initial (S1) safety assessment, regardless of the strength of the efficacy signal.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — required before any S1 safety review
- Confirmed DrugBank mechanism-of-action record
- Preclinical or mechanistic studies specifically linking Activin/GDF signaling to ALL pathophysiology
- Complete license-level detail (product names, dosage forms, approved indication text) for the 2 Malaysia registrations

Note: all 10 TxGNN-predicted indications for this drug (including ALL) are currently rated L5/Hold — none has clinical or literature support in this evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

