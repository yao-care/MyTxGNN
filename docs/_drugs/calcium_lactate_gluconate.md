---
layout: default
title: Calcium Lactate Gluconate
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 2
---

# Calcium Lactate Gluconate
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

# Calcium Lactate Gluconate: From Calcium Supplementation to Calcium-Alkali Syndrome

## One-Sentence Summary

> Calcium Lactate Gluconate (DrugBank DB13365) is a calcium salt combination generally used for calcium supplementation, though detailed original indication and mechanism-of-action data are not currently available in the registration record.
> The TxGNN model's top-ranked signal points to **Calcium-Alkali Syndrome**, but this is very likely a **reverse/adverse-event association** — the drug is a known causal risk factor for this syndrome, not a candidate treatment for it.
> There are currently **0 clinical trials** and **0 publications** supporting a therapeutic relationship, so this candidate does not meet the evidentiary bar for repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available registration records (calcium lactate gluconate is broadly known as an oral calcium supplement) |
| Predicted New Indication | Calcium-Alkali Syndrome *(likely an adverse-event association, not a treatment indication — see below)* |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for this product. Based on known pharmacology, calcium lactate gluconate is an oral calcium salt combination used to correct calcium deficiency states; its role as a systemic source of ionic calcium is well established. Mechanistically, however, this is precisely why the top TxGNN signal should be treated with caution rather than enthusiasm.

Calcium-alkali syndrome (historically "milk-alkali syndrome") is a clinical syndrome of hypercalcemia, metabolic alkalosis, and renal impairment caused by **excess intake of calcium together with absorbable alkali**. Calcium lactate gluconate supplementation is a recognized *causal/risk factor* for this syndrome — the pharmacological relationship runs in the opposite direction from a therapeutic one. The high TxGNN score most plausibly reflects a drug–disease co-occurrence learned from adverse-event or toxicity contexts within the knowledge graph, rather than a genuine treatment signal. This candidate should **not** be interpreted as a repurposing opportunity; the model's own rationale notes explicitly that this is a reversed (drug-causes-disease) relationship.

A second, lower-priority candidate identified by the model — *primary bone dysplasia with defective bone mineralization* — has a more plausible, though still purely mechanistic, rationale: calcium is a required substrate for hydroxyapatite formation, and supplementation could theoretically support mineralization in some bone disorders. However, this disease group is heterogeneous and often driven by underlying genetic/enzymatic defects (e.g., ALPL, PHEX, FGF23-related pathways) rather than simple calcium insufficiency; in some subtypes (e.g., hypophosphatasia) additional calcium may even increase risk of hypercalcemia or ectopic calcification. No clinical or literature evidence currently exists for this indication either, so it remains a research question rather than an actionable candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA registration records confirm the product is currently marketed in Malaysia with **6 active authorizations**, but license-level details (authorization numbers, product names, dosage forms, and approved indication text) are not populated in the current evidence pack and require direct extraction from NPRA product registration data before they can be reported individually.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: the current evidence pack has a **blocking data gap (DG001)** — TFDA/NPRA label warnings and contraindications have not yet been retrieved — so no drug-specific safety statements can be made at this time; a DDI database query also returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (calcium-alkali syndrome) is best understood as a known adverse effect/risk association of calcium lactate gluconate rather than a treatable indication, and is unsupported by any clinical trials or literature (Evidence Level L5, model prediction only). The secondary candidate (bone mineralization disorders) has a plausible mechanistic rationale but likewise has zero supporting trials or publications and involves a heterogeneous disease group where calcium supplementation may not address the underlying pathology. Neither candidate currently justifies moving beyond hypothesis stage.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA product label warnings and contraindications (blocking gap, DG001)
- Retrieve confirmed mechanism-of-action data from DrugBank (DG002)
- Clarify whether the calcium-alkali syndrome signal in the knowledge graph reflects an adverse-event co-occurrence rather than a treatment relationship, to confirm it should be excluded from further repurposing evaluation
- If pursuing the bone dysplasia candidate, identify the specific disease subtype/genetic etiology to determine whether calcium supplementation is mechanistically appropriate, and seek preclinical or case-level evidence before any further investment
- Complete license-level extraction of Malaysia NPRA registration data (product names, dosage forms, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

