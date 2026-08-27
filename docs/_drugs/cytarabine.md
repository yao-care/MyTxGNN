---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Original Indication Not on File to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a cytotoxic antimetabolite chemotherapy agent registered in Malaysia (3 active licenses), but the specific original approved indication text is not present in the current dataset. The TxGNN model's top-ranked prediction is **Small Cell Lung Carcinoma** (score **99.78%**), but this specific rank-1 candidate currently has **zero clinical trials and zero publications** supporting it — the evidence pack itself flags it as a pure score-driven speculation with no known mechanistic basis. Two other candidates further down the ranked list (primary pulmonary lymphoma, neuroblastoma) carry stronger mechanistic rationale and are worth separate attention (see Appendix below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current Malaysia registration data (see Data Gap DG001/DG002) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cytarabine is not available in this evidence pack (flagged as Data Gap DG002, severity High). Based on the mechanistic notes embedded elsewhere in this evidence pack, cytarabine (Ara-C) is a pyrimidine nucleoside analogue that, after intracellular phosphorylation to Ara-CTP, competitively inhibits DNA polymerase and causes chain termination — a classic S-phase-specific cytotoxic mechanism. This mechanism underlies its established role in haematologic malignancies (e.g., high-dose cytarabine regimens in leukaemia and non-Hodgkin lymphoma).

For the top-ranked candidate specifically — **Small Cell Lung Carcinoma** — the evidence pack's own rationale is explicit that this link is *not* mechanistically well-supported: SCLC standard-of-care is platinum/etoposide, cytarabine is not a known active agent in this setting, and no trial or literature evidence exists to corroborate the prediction. This candidate should be read as a TxGNN score-driven hypothesis only, not a mechanism-anchored one.

Because the original indication text itself is missing from the Malaysia registration data, the usual comparison between "original indication" and "predicted new indication" cannot be made directly here — this gap should be closed before any further scoring is finalized.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Appendix: Other Predicted Indications (Full Ranked List)

This evidence pack contains 9 TxGNN-predicted indications for cytarabine, not all with the same strength of rationale as the top-ranked candidate. None have direct trial or literature support in this dataset, but two stand out for stronger mechanistic/clinical-practice plausibility and may warrant prioritization over the rank-1 candidate:

| Rank | Predicted Indication | Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------|-----------------|-----------------|-----------------|
| 1 | Small cell lung carcinoma | 99.78% | L5 | S0 | Hold |
| 2 | **Primary pulmonary lymphoma** | 99.78% | **L4** | **S1** | **Research Question** |
| 3 | Well-differentiated fetal adenocarcinoma of the lung | 99.76% | L5 | S0 | Hold |
| 4 | Pulmonary blastoma | 99.76% | L5 | S0 | Hold |
| 5 | Upper aerodigestive tract neoplasm | 99.49% | L5 | S0 | Hold |
| 6 | **Ganglioneuroblastoma (disease)** | 99.36% | **L4** | **S1** | **Research Question** |
| 7 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 99.32% | L5 | S0 | Hold — likely knowledge-graph noise, needs manual node review |
| 8 | Retroperitoneal neoplasm | 99.23% | L5 | S0 | Hold |
| 9 | **Neuroblastoma** | 99.19% | **L4** | **S1** | **Research Question** |

Notable: rank 2 (primary pulmonary lymphoma) is grounded in cytarabine's established role in non-Hodgkin lymphoma regimens; rank 9 (neuroblastoma) is grounded in real-world use of high-dose cytarabine + topotecan as salvage therapy for relapsed/refractory neuroblastoma. Both lack direct trial/literature hits in this pack but are mechanistically stronger than the top-scored SCLC candidate and may be better starting points for further evidence-gathering.

---

## Malaysia Market Information

Malaysia regulatory status shows cytarabine as **marketed (已上市)** with **3 active licenses**. However, license number, product name, dosage form, manufacturer, and approved indication text are not populated in the current dataset for any of the 3 entries — this data will need to be pulled directly from NPRA records before it can be cited in a formal report.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Pyrimidine antimetabolite / nucleoside analogue) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic drug handling regulations apply (class-level requirement); confirm specifics in package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (small cell lung carcinoma) has no clinical trial or literature support and the evidence pack itself identifies it as a pure model-score artifact without mechanistic grounding. Blocking-severity data gaps in TFDA warnings/contraindications (DG001) prevent even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — DG001, Blocking
- DrugBank mechanism-of-action query — DG002, High
- Original approved indication text from NPRA license records (all 3 licenses currently blank)
- If pursuing repurposing further, prioritize evidence-gathering on primary pulmonary lymphoma or neuroblastoma (L4/Research Question) over the rank-1 SCLC candidate, given their stronger mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

