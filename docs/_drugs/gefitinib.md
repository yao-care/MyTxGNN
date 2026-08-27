---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From EGFR-Mutant Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor whose core approved use is EGFR mutation-positive advanced non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, a benign gum tissue overgrowth condition,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | EGFR mutation-positive advanced NSCLC (established pharmacology; TFDA/NPRA label text not yet extracted — see Data Gap DG001) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, gefitinib is a small-molecule EGFR tyrosine kinase inhibitor, and its efficacy in EGFR-mutant NSCLC has been well established and proven in clinical practice.

Gingival fibromatosis is a benign fibrous overgrowth of gum connective tissue. The evidence pack's own mechanistic assessment notes that EGFR signaling is theoretically involved in fibrotic proliferation pathways, which is the presumed basis for the TxGNN association. However, this link is speculative rather than demonstrated — no clinical trial or published study connecting gefitinib to gingival fibromatosis was found in this data pull.

Because the predicted indication shares no anatomical, oncologic, or established mechanistic overlap with gefitinib's approved oncology use, this candidate should be treated as a pure model signal rather than a clinically grounded hypothesis at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Gefitinib holds 10 active registrations in Malaysia (market status: Marketed), but the detailed license fields (authorization number, product name, dosage form, approved indication text) were not populated in this data extract and require a follow-up NPRA data pull.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.89%), this candidate has zero clinical trial or literature support, and the mechanistic link between EGFR inhibition and gingival fibromatosis is speculative. Evidence level L5 (model prediction only) does not meet the threshold to advance to safety review.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (Data Gap DG001, currently blocking safety pre-screening)
- Detailed mechanism of action data (Data Gap DG002)
- Any preclinical or case-level evidence specifically linking EGFR inhibition to gingival fibromatosis

**Note on other candidates in this evidence pack:** Among gefitinib's 10 TxGNN-predicted indications, two show meaningfully stronger evidence than the top-scored candidate above — **lung hilum carcinoma** (L3, Proceed with Guardrails, supported by a case report and falling within gefitinib's known NSCLC mechanism) and **pulmonary sulcus neoplasm** (L4, Research Question, indirect NSCLC-subtype literature). If the goal is to identify an actionable repurposing candidate rather than review the top model score specifically, these two warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

