---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an androgen receptor (AR) antagonist already approved for prostate cancer (mCRPC/nmCRPC); its approved-indication text is not included in this evidence pack, though it is referenced within the pack's own rationale notes.
The TxGNN model's top-ranked prediction for this candidate is **"Prostate Cancer/Brain Cancer Susceptibility"**, but this label represents a knowledge-graph susceptibility-gene node rather than a defined clinical entity, and it is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (mCRPC/nmCRPC) — referenced only within evidence-pack rationale text; formal TFDA/NPRA approved-indication wording is a data gap (DG001) |
| Predicted New Indication | Prostate Cancer/Brain Cancer Susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Enzalutamide is known as a second-generation androgen receptor antagonist that blocks AR nuclear translocation and DNA binding, and on that basis it is already approved for prostate cancer.

However, for this specific top-ranked prediction, the disease label "prostate cancer/brain cancer susceptibility" is not a defined clinical entity — per the evidence pack's own rationale, it is a composite label attached to a susceptibility-gene node within the knowledge graph. There is no mechanistic pathway or clinical rationale that can be articulated beyond the model's statistical association, and no clinical trial or literature evidence exists to support or refute it.

For context, this evidence pack contains six other predicted indications for enzalutamide. Notably, rank 6 ("male reproductive organ cancer") carries much stronger evidence (L1, S3, Proceed with Guardrails), but its own rationale flags that this largely overlaps with enzalutamide's already-approved prostate cancer indication rather than representing a genuinely novel repurposing target — it is noted here for decision context, not as a substitute for the rank-1 candidate this report evaluates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The product is recorded as marketed in Malaysia with 4 total registrations (NPRA), but this evidence pack does not include per-license details (license number, product name, dosage form, or approved indication text) — these fields are all empty in the source data and represent a data gap.

## Cytotoxicity

*Included because the original indication (prostate cancer) is oncologic.*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (androgen receptor signaling inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low (consistent with hormonal/AR-targeted agents as a class) |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 predicted indication has no supporting clinical trial or literature evidence (L5), and the disease label itself represents a knowledge-graph artifact (a susceptibility-gene node) rather than a defined clinical entity, so no meaningful mechanistic or clinical case can currently be built.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank — currently a High-severity data gap (DG002)
- Clarification of what clinical entity "prostate cancer/brain cancer susceptibility" actually refers to before further evaluation
- Per-license registration details (license numbers, product names, approved indication text) for the 4 Malaysia registrations
- If pursuing repurposing further, consider evaluating rank 6 ("male reproductive organ cancer") separately, noting it substantially overlaps with the already-approved prostate cancer indication rather than representing a novel target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

