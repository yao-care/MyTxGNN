---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Lactulose: From Constipation / Hepatic Encephalopathy to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose is a non-absorbable synthetic disaccharide long established for treating constipation and hepatic (portosystemic) encephalopathy. The TxGNN model's top-ranked prediction proposes potential effectiveness for **Acute Urate Nephropathy**, but currently **0 clinical trials** and **0 publications** support this specific pairing — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the current NPRA license extract (this data pull returned no `approved_indication_text`); lactulose's globally established indications are constipation and hepatic/portosystemic encephalopathy |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a data gap). Based on known pharmacology, lactulose acts locally in the colon — its osmotic effect and bacterial fermentation to short-chain organic acids lower luminal pH, which underlies its efficacy in constipation and in reducing ammonia absorption in hepatic encephalopathy.

For this specific prediction, there is no known mechanistic link between lactulose and acute urate nephropathy: lactulose does not affect uric acid metabolism or renal tubular urate deposition/excretion. No clinical trial or literature evidence was found for this pairing. This appears to be a pure model-score prediction without pharmacological or empirical support, and should be treated as a low-confidence signal rather than a research lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Detailed license records (product names, dosage forms, manufacturers) were not returned in this data extract — all license fields came back empty. NPRA data confirms lactulose has **12 active registrations** and a market status of **Marketed (已上市)** in Malaysia; individual authorization details would need to be re-pulled from the NPRA source.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, there is no known mechanistic link between lactulose and acute urate nephropathy, and zero clinical trials or literature exist for this pairing — this is an L5, model-only prediction with insufficient basis to advance.

**To proceed, the following is needed:**
- Preclinical/mechanistic studies on lactulose's effect on uric acid metabolism or renal urate handling, to establish any plausible biological rationale
- TFDA/NPRA package insert data (warnings, contraindications) — currently a blocking data gap for even a baseline safety screen
- DrugBank MOA data to properly assess mechanistic plausibility across all candidate indications

**Note:** Among the other indications in this evidence pack, **obstructive jaundice** (rank 3, evidence level L3, 1 completed Phase 4 trial plus 20 publications including a multicentre RCT on postoperative renal protection) shows substantially stronger mechanistic and evidentiary support and may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

