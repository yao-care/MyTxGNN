---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is an oral ALK/ROS1 tyrosine kinase inhibitor; based on literature contained in this evidence pack (structured original-indication data was not returned), it was originally developed and approved for **ALK-positive non-small cell lung cancer (NSCLC)**. TxGNN predicts a possible new application in **Gingival Fibromatosis** with a very high model score, but currently **0 clinical trials** and **0 publications** support this specific pairing — the prediction rests entirely on the model's graph-based scoring, with no mechanistic or clinical corroboration found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive Non-Small Cell Lung Cancer (NSCLC)* |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

\* No approved-indication text was returned in the structured regulatory data (`taiwan_regulatory.licenses` fields are blank, and `drug.original_indications` is empty). The NSCLC indication above is inferred from literature retrieved elsewhere in this evidence pack (e.g., PMID 24980964 "Ceritinib: first global approval"; PMID 28126333, the ASCEND-4 Phase 3 trial), not from a confirmed regulatory source.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is flagged as a data gap in the structured drug record. Based on information available elsewhere in this evidence pack, Ceritinib is a small-molecule inhibitor of the ALK (anaplastic lymphoma kinase) and ROS1 receptor tyrosine kinases, developed to treat ALK-rearranged NSCLC — a malignancy driven by oncogenic ALK fusion signaling.

Gingival fibromatosis, in contrast, is a benign, non-neoplastic overgrowth of gingival connective tissue, typically hereditary or drug-induced (e.g., by phenytoin, cyclosporine, calcium channel blockers), and is not associated with ALK gene rearrangement or ALK-driven signaling in the literature reviewed. No clinical trial or publication in this evidence pack links Ceritinib, ALK inhibition, or ALK biology to gingival fibromatosis pathophysiology.

Given the complete absence of supporting evidence and the lack of an established mechanistic pathway, this prediction should be treated as a graph-proximity artifact of the TxGNN model rather than a pharmacologically grounded hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia regulatory records show **1 registered license** under market status "已上市" (Marketed). License number, product name, dosage form, and approved-indication text were not returned in the current data extract, so no license-level table can be produced.

---

## Cytotoxicity

Ceritinib is an antineoplastic agent (targeted kinase inhibitor used in oncology), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Not established in the retrieved data. As a class, ALK inhibitors are generally associated with lower myelosuppression risk than conventional cytotoxic chemotherapy; please refer to the package insert for confirmed hematologic toxicity data |
| Emetogenicity Classification | Not established in the retrieved data; please refer to the package insert |
| Monitoring Items | Class-related safety signals identified in retrieved literature (not specific to this new indication) include QT prolongation, hepatotoxicity, and pneumonitis/hypersensitivity reactions — suggesting ECG/QTc monitoring, liver function tests (ALT/AST/bilirubin), and respiratory symptom monitoring as reasonable considerations |
| Handling Protection | Not established in the retrieved data; please refer to institutional hazardous-drug handling protocols and the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score, there are zero clinical trials and zero publications supporting Ceritinib for gingival fibromatosis, and no plausible mechanistic link was found — this is model-only evidence (L5) and does not meet the bar to proceed.

**To proceed, the following is needed:**
- Confirmed original-indication and MOA data (both currently data gaps)
- Any preclinical or mechanistic rationale connecting ALK inhibition to gingival fibromatosis
- Full Malaysia license details (license number, product name, dosage form, approved indication text)
- TFDA/NPRA package-insert warnings, contraindications, and DDI data (all currently unavailable)
- Note: this evidence pack contains other predicted indications for Ceritinib with materially stronger evidence (e.g., rank 6, "lung germ cell tumor," L3/S1) that may warrant separate evaluation before further work on this specific candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

