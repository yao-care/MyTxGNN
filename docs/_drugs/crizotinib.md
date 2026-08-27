---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK/ROS1-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is a tyrosine kinase inhibitor targeting ALK/ROS1/MET, referenced in this evidence pack as approved for ALK/ROS1-positive non-small cell lung cancer (NSCLC). The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags the mechanistic link as absent and suspects this is model noise rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK/ROS1-positive NSCLC *(sourced from rationale notes; the structured license/indication fields in the source data are blank)* |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap in this pack. Based on what the evidence pack's rationale notes do state, crizotinib is a small-molecule inhibitor of ALK, ROS1, and MET tyrosine kinases, used clinically for ALK/ROS1-driven NSCLC — a cancer with a specific oncogenic driver mutation.

Gingival fibromatosis, by contrast, is a benign connective-tissue proliferative condition, not a malignancy, and has no established link to ALK/ROS1/MET signaling. The evidence pack's own rationale for this candidate states there is "no known connection to crizotinib's known ALK/ROS1/MET kinase-inhibition mechanism, nor is it a neoplastic disease," and explicitly flags the score as a likely artifact of knowledge-graph embedding proximity rather than a real pharmacological signal.

This pattern is consistent across the full top-10 list in this evidence pack: every predicted indication carries evidence level L5 (model prediction only), zero clinical trials, and zero literature hits, with several rationale notes independently describing the scores as probable KG noise. This suggests the prediction score alone is not a reliable signal for this drug in this score band, and mechanistic plausibility should be weighted heavily before any further action.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Crizotinib holds **2 registered licenses** in Malaysia with market status "Marketed." Detailed per-license information (authorization number, product name, dosage form, approved indication text) is not available in the source data — all corresponding fields were returned blank.

## Cytotoxicity

Crizotinib is an oncology drug (ALK/ROS1/MET-targeted therapy for NSCLC), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) — not a conventional cytotoxic chemotherapy agent, per rationale notes |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (gingival fibromatosis) has no clinical trial, literature, or mechanistic support, and the evidence pack itself identifies the prediction as likely knowledge-graph noise rather than a genuine repurposing signal. Additionally, a Blocking data gap (missing TFDA/NPRA package insert warnings and contraindications) prevents this candidate from entering the S1 safety review stage regardless of indication-level evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism-of-action data via DrugBank API
- Complete Malaysia license details (product names, dosage forms, full approved indication text)
- If this indication is pursued further, a preclinical or mechanistic rationale connecting ALK/ROS1/MET pathway biology to gingival fibromatosis pathogenesis, which is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

