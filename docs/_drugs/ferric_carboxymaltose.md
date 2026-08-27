---
layout: default
title: Ferric Carboxymaltose
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 1
---

# Ferric Carboxymaltose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ferric Carboxymaltose: From Unspecified Original Indication to Bronchitis

## One-Sentence Summary

> Ferric carboxymaltose's original approved indication is not available in the current dataset, though it is registered and marketed in Malaysia under 1 license.
> The TxGNN model predicts it may be effective for **Bronchitis**, but this prediction is currently supported by **no clinical trials** and **no published literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ferric carboxymaltose is not available in this dataset (marked as a High-severity data gap). Based on the evidence review associated with this prediction, ferric carboxymaltose is known to be an intravenous iron preparation used for iron deficiency anemia, working by replenishing ferritin iron stores and transferrin iron saturation.

This mechanism has no established direct link to bronchitis, which is a respiratory tract disease driven by viral or bacterial infection and airway inflammation. The high TxGNN score (0.99) most likely reflects an indirect knowledge-graph association — for example, the common comorbidity between chronic respiratory disease (such as COPD) and anemia of chronic disease, which often requires iron therapy — rather than a genuine pharmacological effect of iron repletion on bronchitis itself.

Because original indication data is unavailable for this drug in the current dataset, no direct cross-comparison between the original and predicted indications can be made at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

License details (license number, product name, dosage form, approved indication text) are not populated in the current dataset. The drug is confirmed as marketed in Malaysia with 1 registered license, but detailed registration data requires further collection.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only), with zero clinical trials and zero literature supporting a bronchitis indication, and the proposed mechanistic link is indirect at best. A Blocking-severity data gap (TFDA label warnings/contraindications) also prevents safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — currently blocking safety evaluation
- Mechanism of action data from DrugBank
- Confirmed original indication and approved indication text for the Malaysia license
- Targeted literature/clinical trial search for ferric carboxymaltose in respiratory/bronchitis-related contexts to establish or rule out a plausible biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

