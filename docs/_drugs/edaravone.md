---
layout: default
title: Edaravone
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 2
---

# Edaravone
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

Using the evidence pack provided, here is the evaluation report.

---

# Edaravone: From Unrecorded Original Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Edaravone is currently marketed in Malaysia (1 active registration), but its originally approved indication text has not yet been retrieved from source data. The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, with **no clinical trials** and **no published literature** currently supporting this direction — the signal rests entirely on knowledge-graph model similarity.

> *Note: A second candidate, **Factor V Excess with Spontaneous Thrombosis** (TxGNN score 99.06%), was also flagged by the model with the same evidence gaps and the same Hold recommendation.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA/NPRA license text has not yet been retrieved (see DG001) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for edaravone is currently a documented data gap (DG002). Based on general pharmacological knowledge, edaravone is known as a free-radical scavenger / antioxidant agent used for neuroprotection; no verified mechanistic pathway currently links this action to heparin cofactor 2 (a thrombin-inhibiting coagulation factor) deficiency.

Heparin cofactor 2 deficiency is a rare disorder of anticoagulant regulation. Oxidative stress can, in theory, affect endothelial function and the broader coagulation/anticoagulation balance, so an indirect biological connection cannot be entirely excluded — but this link is speculative and is not supported by any independent experimental or clinical data in the current evidence pack.

As a result, this prediction should be treated as a **model-generated hypothesis only**. The TxGNN similarity score (0.9947, rank 7,593) is the sole basis for the candidate; there is no clinical trial, registry trial, or published literature confirming, refuting, or even exploring this relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Regulatory records confirm edaravone has **1 active registration** in Malaysia (market status: ✓ Marketed). However, the license number, product name, dosage form, manufacturer, and approved indication text have not yet been retrieved from source data — this is tracked as a blocking data gap (DG001) that also prevents a full safety review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are not yet available in the current dataset — this is tracked as a blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN embedding-similarity score (Evidence Level L5) with zero clinical trials, zero published literature, and no established mechanistic pathway connecting edaravone's known antioxidant/neuroprotective action to a rare coagulation-factor disorder. In addition, the blocking data gap on TFDA/NPRA label warnings and contraindications (DG001) means this candidate cannot yet even enter a preliminary safety review (S1).

**To proceed, the following is needed:**
- Retrieve the TFDA/NPRA package insert (warnings, contraindications) — DG001
- Retrieve detailed DrugBank mechanism-of-action data — DG002
- Confirm the original approved indication text and full license details (currently blank in the registry record)
- Conduct a targeted literature/mechanistic review on any link between oxidative-stress pathways and heparin cofactor II or Factor V regulation before advancing past S0
- Given the complete absence of clinical or trial evidence (L5), any further pursuit should start with preclinical/mechanistic studies rather than clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

