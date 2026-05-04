---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Albutrepenonacog Alfa: From Haemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa (Idelvion®) is a recombinant Factor IX–albumin fusion protein (rIX-FP) with extended half-life, originally approved for prophylaxis and treatment of bleeding episodes in Haemophilia B (congenital Factor IX deficiency).
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease** as its top-ranked new indication,
however **no supporting clinical trials or publications** were identified, leaving this prediction at evidence level **L5** — model inference only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia B (congenital Factor IX deficiency) — prophylaxis and on-demand bleeding control |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, albutrepenonacog alfa is a recombinant coagulation Factor IX fused to human albumin. The albumin fusion extends the circulating half-life of FIX approximately five-fold compared to standard FIX products, allowing less frequent intravenous dosing. Its efficacy in Haemophilia B is well-proven through multiple Phase 3 programmes — it restores the intrinsic coagulation cascade (secondary haemostasis) by replacing deficient FIX.

Pseudo-von Willebrand Disease (pseudo-vWD), by contrast, is a primary haemostasis disorder caused by a **gain-of-function mutation in platelet GPIbα**, which causes GPIbα to bind vWF excessively, leading to spontaneous consumption of high-molecular-weight vWF multimers and consequent thrombocytopenia and mucocutaneous bleeding. The core defect resides entirely in the platelet–vWF interaction, upstream of the coagulation cascade where FIX operates. Supplementing FIX does not correct the aberrant GPIbα–vWF interaction, nor does it restore vWF multimer levels or platelet count.

The TxGNN high score for this pairing most likely reflects **graph proximity** within the knowledge graph — both Haemophilia B and pseudo-vWD are nodes in the "haemorrhagic/bleeding disorder" neighbourhood — rather than a genuine mechanistic pathway. The biological rationale for this specific repurposing is extremely weak, and no corroborating evidence was identified.

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Plausibility |
|------|---------|------------|----------------|----------------|--------------------------|
| 1 | Pseudo-von Willebrand Disease | 99.94% | L5 | Hold | Very weak — FIX (2° haemostasis) cannot correct GPIbα gain-of-function (1° haemostasis) |
| 2 | Primary Release Disorder of Platelets | 99.94% | L5 | Hold | Indirect — thrombin-amplified platelet activation is a theoretical bypass; unvalidated clinically |
| 3 | Glanzmann Thrombasthenia | 99.92% | L5 | Research Question | Moderate analogy — FEIBA (containing FIX) is an established bypass therapy; rIX-FP alone unproven |
| 4 | Scott Syndrome | 99.63% | L5 | Hold | Mechanistic contradiction — FIXa requires PS-exposed membrane surfaces that are absent in Scott syndrome |
| 5 | Bleeding Diathesis due to Collagen Receptor Defect | 99.28% | L5 | Hold | Weak — FIX cannot repair platelet–collagen adhesion; mild phenotype does not justify IV biologics |
| 6 | Haemorrhagic Disorder due to Constitutional Thrombocytopenia | 99.26% | L5 | Hold | Partial — thrombin generation may partially compensate, insufficient in severe thrombocytopenia |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the six predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the six predicted indications.

---

## Malaysia Market Information

Four registrations are confirmed in Malaysia (NPRA data as of 2026-04-04); however, individual licence details (authorisation numbers, product names, dosage forms, and approved indication text) were not returned in the current data query. A supplementary NPRA lookup is recommended to populate this table.

| Registration | Detail |
|-------------|--------|
| Total active licences | 4 |
| Market status | Marketed |
| Licence details | Pending NPRA supplementary lookup |

---

## Safety Considerations

Please refer to the package insert for safety information.
All safety fields (warnings, contraindications, and drug–drug interactions) were identified as data gaps in this Evidence Pack. Albutrepenonacog alfa is an injectable biological — refer to the Idelvion® Summary of Product Characteristics for thromboembolic risk, inhibitor development monitoring, and hypersensitivity precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications are at Evidence Level L5 (model prediction only, no supporting clinical trials or publications). The top-ranked prediction — pseudo-von Willebrand Disease — has a mechanistically implausible link given the fundamental separation between FIX's role in secondary haemostasis and pseudo-vWD's primary haemostasis defect. Advancing any of these indications at this stage is not supported by current evidence.

**Exception — Research Question (Glanzmann Thrombasthenia):**
This indication warrants monitoring: bypass therapy with FEIBA (which contains activated FIX) is an established salvage strategy, providing indirect mechanistic precedent. This does not yet justify a repurposing study, but should be tracked for emerging investigator-initiated research.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full DrugBank pharmacology entry (DB13884) to formally confirm the mechanism of action and target interactions
- **NPRA licence details**: Re-query NPRA for the 4 registered products to confirm approved indications, dosage forms, and current marketing authorisation holders
- **Package insert safety data**: Download and parse the Malaysian-registered product insert (PDF) to populate warnings, contraindications, and special population data
- **Glanzmann thrombasthenia literature sweep**: Conduct a targeted PubMed search combining "Factor IX" or "FIX" with "Glanzmann thrombasthenia" and "bypass therapy" to determine whether any case reports or small series exist before classifying this as a formal research question
- **Re-evaluation trigger**: If any Phase 2 or Phase 3 trials investigating FIX-based bypass strategies in non-Haemophilia platelet disorders are registered in future, re-initiate evidence scoring for ranks 2–3

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

