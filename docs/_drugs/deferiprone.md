---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 9
---

# Deferiprone
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

# Deferiprone: From Iron Overload (Thalassemia) to Hepatic Porphyria

## One-Sentence Summary

> Deferiprone is an oral iron chelator; based on general drug knowledge (Ferriprox) it is used for transfusional iron overload in thalassemia, though this evidence pack's own `original_indications` field is currently a data gap. The TxGNN model's top-ranked prediction is **Hepatic Porphyria**, but this is supported by **0 clinical trials** and **0 publications** — the model's own rationale flags it as a possible false-positive driven by graph-embedding clustering rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron overload in thalassemia (background knowledge, referenced in this pack's rank-8 rationale as the Ferriprox-approved use; **not sourced from TFDA/NPRA data** — `original_indications` is a data gap) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` = Data Gap). Based on the TxGNN rationale provided in this pack, deferiprone is a selective ferric-iron chelator, and hepatic porphyria involves disruption of the heme biosynthesis pathway, for which iron is a required cofactor. This gives a theoretical, indirect pathway link between the drug's known pharmacology and the predicted disease.

However, the directionality of this link is explicitly unclear in the underlying rationale: excessive iron chelation could just as plausibly worsen certain porphyria subtypes by inducing iron deficiency, rather than helping. There is no clinical, preclinical, or case-report evidence in this evidence pack to resolve that ambiguity.

It is also worth noting that ranks 2–6 in the predicted-indications list (idiopathic copper-associated cirrhosis, portal hypertension, hepatoportal sclerosis, portal vein thrombosis, hepatopulmonary syndrome) all carry an almost identical score (~0.99196) to each other and lack any drug-specific mechanistic rationale. The evidence pack's own annotations attribute this to TxGNN knowledge-graph clustering of "liver disease" nodes rather than a real, drug-specific pharmacological signal — a pattern that also raises caution about the top-ranked hepatic porphyria prediction, since it sits in the same score band.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The evidence pack records 6 total registrations with market status "已上市" (Marketed), but the 5 license entries returned contain no populated fields (license number, product name, dosage form, manufacturer, and indication text are all blank) — this is a data gap in the source query, not an absence of registrations. License-level detail needs to be re-collected from NPRA before it can be reported here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hepatic porphyria) is supported only by an L5, model-only score with zero clinical trials or literature, and the mechanistic rationale itself flags directional uncertainty — iron chelation could plausibly worsen some porphyria subtypes rather than treat them. Several neighboring predictions in the same score band show signs of being graph-clustering artifacts rather than genuine signals, which further undermines confidence in this specific rank-1 result.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, blocking — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank (DG002)
- Preclinical or mechanistic studies clarifying the *direction* of iron-chelation effects across porphyria subtypes before considering hepatic porphyria as a repurposing candidate
- Confirmation of `original_indications` (currently empty) — note that **beta-thalassemia with other manifestations (rank 8)** appears to be deferiprone's already-approved use (Ferriprox), not a genuinely new indication; this should be verified so it is not miscounted as a repurposing candidate
- Populated Malaysia license/indication data to replace the current blank entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

