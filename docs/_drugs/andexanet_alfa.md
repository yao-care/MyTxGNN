---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa is a recombinant modified human Factor Xa decoy protein approved to reverse life-threatening or uncontrolled bleeding caused by Factor Xa inhibitors (apixaban and rivaroxaban).
The TxGNN model predicts it may be effective for **Glanzmann Thrombasthenia**,
with **0 clinical trials** and **0 publications** currently directly supporting this direction — making this a model-only prediction at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Factor Xa inhibitor reversal (anticoagulant antidote) |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Andexanet alfa is a recombinant, catalytically inactive modified human Factor Xa protein. It functions as a decoy receptor in the secondary coagulation cascade, binding to and sequestering Factor Xa inhibitors (apixaban, rivaroxaban) in the plasma, thereby restoring the natural coagulation process in patients experiencing life-threatening bleeding during anticoagulation therapy.

Glanzmann thrombasthenia is a hereditary platelet aggregation disorder caused by deficiency or dysfunction of the platelet surface glycoprotein GPIIb/IIIa (integrin αIIbβ3). This is a **primary hemostasis** defect — the platelet adhesion/aggregation pathway — and is mechanistically entirely separate from the **secondary coagulation cascade** where Andexanet alfa exerts its action (at the Factor Xa level in the prothrombinase complex). The two pathways do not share a direct pharmacological intersection.

The high TxGNN prediction score most likely originates from indirect knowledge graph connections: both conditions share "bleeding phenotype" classification nodes in the graph, creating a graph-proximity artifact rather than a genuine mechanistic or clinical repurposing signal. This prediction should be treated with caution and is not supported by any real-world evidence at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Andexanet alfa holds **1 registered licence** in Malaysia with confirmed marketed status. Detailed product-level registration data (authorization number, product name, dosage form, and approved indication text) was not returned in the current data query and should be retrieved directly from the National Pharmaceutical Regulatory Agency (NPRA) database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| (Not recorded in current data) | Andexanet Alfa | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Data Gap Note**: Key warnings and contraindications data were not retrieved in this evidence cycle. The package insert PDF should be obtained from the NPRA website and parsed prior to any clinical assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Glanzmann thrombasthenia is assessed as a knowledge graph artifact with no supporting clinical or preclinical evidence (L5). Andexanet alfa acts exclusively on Factor Xa inhibitors within the secondary coagulation cascade, while Glanzmann thrombasthenia is a primary platelet aggregation disorder (GPIIb/IIIa dysfunction) — these two biological pathways have no known pharmacological overlap, and there is currently zero trial or literature evidence to suggest a plausible repurposing opportunity.

**To proceed, the following would be needed:**

- Retrieval and parsing of the full package insert (NPRA PDF) to populate key warnings, contraindications, and approved indication text (Data Gap DG001)
- DrugBank API query to confirm full MOA and drug categories (Data Gap DG002)
- Mechanistic studies or expert opinion demonstrating any plausible pharmacological effect on platelet GPIIb/IIIa function — which is currently not theoretically supported
- Preclinical data in Glanzmann thrombasthenia animal models before any further evaluation is warranted

---

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. *(YMYL)*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

