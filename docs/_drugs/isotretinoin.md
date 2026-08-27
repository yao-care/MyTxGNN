---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

# Isotretinoin: From Severe Nodular Acne to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Isotretinoin is an oral retinoid conventionally used for severe, treatment-resistant nodular acne (the NPRA-registered indication text for this drug was not captured in the current evidence pack). The TxGNN model predicts possible efficacy in **Malignant Hypertensive Renal Disease**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal with no mechanistic or empirical corroboration.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe nodular acne (based on established pharmacology; NPRA license indication text not captured in this evidence pack) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap). Based on established pharmacological knowledge, isotretinoin (13-cis-retinoic acid) acts primarily on sebaceous gland regulation and epithelial cell differentiation; its known safety signals — hepatotoxicity, hypertriglyceridemia/dyslipidemia, pseudotumor cerebri (benign intracranial hypertension, not malignant hypertension), and teratogenicity — do not point to any established pathway relevant to malignant hypertensive renal disease, a condition driven by renal arteriolar fibrinoid necrosis and acute RAAS activation.

No mechanistic, preclinical, or clinical link between the drug and this indication is identified. The evidence pack's own rationale flags the high TxGNN score as likely reflecting an indirect graph association between retinoid-related and vascular/renal nodes rather than genuine pharmacological plausibility. Notably, the second-ranked prediction, "malignant renovascular hypertension," carries an identical score (99.01%) and describes essentially the same disease concept — this near-duplicate pairing is more consistent with redundant or noisy knowledge-graph structure than with two independent lines of model support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Isotretinoin holds 8 registered licenses in Malaysia and is currently marketed, but per-license details (license number, product name, dosage form, approved indication text) were not captured in this evidence pack — only the aggregate registration count and market status are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-generated only (L5), with no supporting clinical trials or literature and no identifiable mechanistic pathway between isotretinoin's known pharmacology and malignant hypertensive renal disease. The near-identical, redundant score for a second near-duplicate predicted indication further suggests knowledge-graph noise rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank or primary literature (currently a High-severity data gap)
- Independent preclinical or mechanistic evidence linking retinoid activity to renal vascular pathology, or at minimum an initial case report/observational signal, before allocating further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

