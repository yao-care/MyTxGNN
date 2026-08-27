---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally used for type 2 diabetes management (with established extensions to heart failure and chronic kidney disease). The TxGNN model predicts potential efficacy for **Focal Stiff Limb Syndrome**, but this candidate — along with two other top-ranked candidates (Classic Stiff Person Syndrome, Opsismodysplasia) — currently has **0 clinical trials** and **0 publications** supporting it, a pattern consistent with a knowledge-graph artifact rather than a genuine pharmacological hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Malaysia (NPRA) registry data; empagliflozin is globally established for Type 2 Diabetes Mellitus (also heart failure, chronic kidney disease) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned by the DrugBank query for this pack (flagged as a High-severity data gap, DG002). Based on what is embedded in the evidence pack's own rationale text, empagliflozin acts as an SGLT2 inhibitor, blocking the sodium-glucose cotransporter-2 in the renal proximal tubule to reduce glucose reabsorption — the pharmacological basis of its established use in type 2 diabetes, and more recently in heart failure and chronic kidney disease.

None of the three top-ranked TxGNN candidates share an evident mechanistic link with this pathway. Focal stiff limb syndrome and classic stiff person syndrome are autoimmune/neurological conditions driven by GABAergic transmission deficits (often anti-GAD65 antibody-mediated) — unrelated to renal glucose handling. Opsismodysplasia is a rare congenital skeletal dysplasia linked to INPPL1/PI3K signaling — a structural developmental disorder that a metabolic drug would not be expected to address.

The evidence pack's own rationale text for all three candidates independently raises this same concern, and 11 separate queries across ClinicalTrials.gov, ICTRP, and PubMed for these three drug–disease pairs all returned zero results. Together with the near-identical, unusually high TxGNN scores (0.990–0.991) across three mechanistically unrelated diseases, this pattern is more consistent with a knowledge-graph embedding artifact — possibly driven by superficial phenotype-node proximity (e.g., "stiff"-related terms) — than a real repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Empagliflozin is confirmed marketed in Malaysia with 15 total product registrations; however, this evidence pack did not return license-level details (authorization numbers, product names, dosage forms, or approved indication text) from the NPRA query — these fields require a follow-up query.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three top-ranked candidates are L5 (model prediction only) with zero supporting trials or literature, and the pack's own mechanistic analysis finds no plausible biological link between SGLT2 inhibition and any of the three predicted diseases. Combined with the blocking data gap on TFDA/NPRA label warnings (DG001), there is no basis to advance this candidate past S0.

**To proceed, the following is needed:**
- TFDA/NPRA label (warnings, contraindications) — currently blocking, required before any S1 safety screening
- Confirmed original indication text from Malaysia license records
- Verified MOA from DrugBank API (current MOA field is a data gap)
- Independent mechanistic or preclinical rationale for any of the three candidates before committing further evaluation resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

