---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Oncology Indications to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil is a long-established antineoplastic agent; the specific original indication text is not present in the available NPRA records for this evidence pack. The TxGNN model predicts a possible new application in **botryoid-type embryonal rhabdomyosarcoma of the vagina**, but this top-ranked prediction currently has **0 clinical trials** and **0 publications** supporting it — it is a model-score-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available NPRA license records |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature identified) |
| Malaysia Market Status | ✓ Marketed (NPRA) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack. Based on general pharmacological knowledge, fluorouracil belongs to the fluoropyrimidine antimetabolite class, with proven efficacy across multiple oncology indications; mechanistically, cytotoxic antimetabolites are broadly applied across solid and soft-tissue malignancies, which is the likely basis for the model associating it with a rhabdomyosarcoma subtype.

However, this specific predicted indication (botryoid-type embryonal rhabdomyosarcoma of the vagina) returned **zero** clinical trial and **zero** literature hits in targeted searches (query_log IDs 3–5). The score is derived purely from the TxGNN knowledge-graph/deep-learning model, with no corroborating external evidence yet identified. By contrast, other lower-ranked predictions for this drug (e.g., rhabdomyosarcoma generally, rank 2; liver sarcoma, rank 7) do have some literature or trial support, but per the reporting rules this report focuses on the rank-1 prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

NPRA records confirm the drug is marketed in Malaysia with **3 active license registrations**; however, the evidence pack does not include the detailed license number, product name, dosage form, or approved-indication text for these registrations.

## Cytotoxicity

*(Fluorouracil is a classic cytotoxic chemotherapy agent — fluoropyrimidine antimetabolite class — so this section applies.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine/antimetabolite class) |
| Myelosuppression Risk | Medium–High — fluoropyrimidines are commonly associated with neutropenia; no drug-specific toxicity data available in this pack, please refer to the package insert |
| Emetogenicity Classification | Low–Moderate (typical for fluoropyrimidines) |
| Monitoring Items | CBC with differential, renal and hepatic function, DPD-deficiency screening where applicable |
| Handling Protection | Cytotoxic drug handling precautions required per standard chemotherapy protocols |

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/NPRA label warnings and contraindications (DG001) are currently a **Blocking** data gap and must be resolved before any safety assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the top-ranked predicted indication has no clinical trial or literature support (L5), and a Blocking safety data gap (missing label warnings/contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (DG001, Blocking)
- Mechanism of action data via DrugBank (DG002)
- Any preclinical or case-level evidence specific to rhabdomyosarcoma subtypes
- Complete license/indication text for the 3 Malaysia registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

