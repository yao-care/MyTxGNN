---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# GALCANEZUMAB: From Migraine Prevention to Heparin Cofactor II Deficiency

## One-Sentence Summary

Galcanezumab is an anti-CGRP (calcitonin gene-related peptide) monoclonal antibody used clinically for migraine prevention. TxGNN's top prediction for this drug is **Heparin Cofactor II Deficiency**, a rare inherited coagulation disorder, but the prediction is supported by **zero clinical trials and zero publications**, and the underlying mechanism shows no known connection to CGRP signaling.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (based on known pharmacology; Malaysia label text not present in this evidence pack) |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned by DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). Based on the rationale notes accompanying the prediction, galcanezumab works by blocking CGRP from binding its receptor, a pathway relevant to migraine and pain signaling — it has no established role in coagulation or hemostasis.

Heparin Cofactor II Deficiency is caused by mutations in *SERPIND1*, a gene governing a coagulation-inhibitor protein. There is no known mechanistic overlap between CGRP receptor blockade and *SERPIND1*/heparin cofactor II function, and no shared upstream or downstream pathway has been reported in the literature. The evidence pack's own analysis flags the 99.5% TxGNN score as a likely statistical artifact — a false-positive signal arising from sparse graph connectivity around rare-disease nodes, rather than a genuine pharmacological relationship.

Two additional candidates surfaced for this drug — **Antithrombin Deficiency Type 2** (99.41%, rank 8166) and **Factor 5 Excess with Spontaneous Thrombosis** (99.41%, rank 8179) — show the identical pattern: high TxGNN scores, no mechanistic link, and zero clinical or literature evidence. All three appear to stem from the same graph-topology artifact rather than independent biological signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No mechanistic rationale, clinical trial, or published evidence supports this indication. The scoring engine itself flags the TxGNN signal as likely graph noise from a sparsely connected rare-disease node, and this same pattern repeats across all three top-ranked candidates for this drug — none should advance past S0.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (currently blocking — DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Any independent biological rationale connecting CGRP-pathway modulation to coagulation-factor regulation, before this candidate is reconsidered
- Malaysia registration/license detail (product name, dosage form, approved indication text) — not populated in this evidence pack despite 2 active registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

