---
layout: default
title: Nonivamide
parent: 僅模型預測 (L5)
nav_order: 507
evidence_level: L5
indication_count: 10
---

# Nonivamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nonivamide: From Topical Analgesic Use to Pulmonary Hypertension

## One-Sentence Summary

Nonivamide (DrugBank DB11324) is a synthetic capsaicin analog currently marketed in Malaysia, known primarily as a topical analgesic/rubefacient. The TxGNN model's top prediction is **Pulmonary Hypertension**, but this candidate — along with 9 similarly-scored alternatives — currently has **zero supporting clinical trials and zero literature**, placing it at the earliest possible evidence stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA/NPRA license text not populated in this data pull; known use is as a topical analgesic/rubefacient (capsaicin-class agent) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned a gap). Based on known information, Nonivamide is a synthetic capsaicin analog and TRPV1 receptor agonist, marketed as a topical analgesic/rubefacient. Its efficacy in local pain relief is established, but this is exclusively a **topical, non-systemic** use.

TRPV1 receptors are expressed in pulmonary vascular smooth muscle and sensory nerve endings, and animal studies suggest TRPV1 activation can influence pulmonary vascular tone — the theoretical basis for this prediction. However, this is a highly indirect mechanistic inference: Nonivamide has no approved systemic formulation, no systemic-exposure pharmacology or safety data, and no evidence base supporting extrapolation from topical use to treatment of a systemic vascular disease like pulmonary hypertension.

It is also worth noting that TxGNN generated 10 candidates for this drug within a narrow score band (99.65%–99.81%), most clustered around vascular/cardiac themes (pulmonary hypertension, peripheral arterial disease, peripheral vascular disease, intermittent claudication) plus several cardiac arrhythmia and hypersensitivity-related diseases. Some of these (ventricular tachycardia, anaphylaxis, catecholaminergic polymorphic ventricular tachycardia) plausibly represent **safety signals rather than repurposing opportunities** — the pack's own rationale notes capsaicinoid systemic exposure has been associated with sympathetic activation and arrhythmia risk, and topical Nonivamide can itself provoke local hypersensitivity/allergic reactions. The relatively more plausible candidate mechanistically is migraine (TRPV1-mediated sensory desensitization, as explored with intranasal civamide), though no Nonivamide-specific evidence exists for that either.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA records confirm the product is Marketed with **5 active registrations**, but individual license numbers, product names, dosage forms, manufacturers, and approved-indication text were not returned in this data pull (all fields blank in the source record).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this is a Blocking data gap — TFDA/NPRA label warnings and contraindications have not yet been retrieved, and safety review cannot proceed to stage S1 without them.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (L5) with no clinical trials, no literature, and no drug-specific mechanistic data — the lowest evidence tier. Several sibling candidates in the same prediction set point toward safety concerns (arrhythmia, hypersensitivity) rather than therapeutic opportunity, which argues for caution rather than acceleration on this drug generally.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (DG001, Blocking) — required before any S1 safety screening
- DrugBank mechanism of action data (DG002, High) — required to assess mechanistic plausibility of the vascular/pulmonary hypothesis
- Confirmation of Nonivamide's approved route(s)/formulation(s) in Malaysia, since the pulmonary hypertension hypothesis presumes systemic exposure not currently supported by any approved formulation
- Any preclinical or case-level evidence specific to Nonivamide (not just the TRPV1 drug class) before moving beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

