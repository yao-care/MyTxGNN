---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 5
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lamotrigine: From Epilepsy to Cutis Verticis Gyrata

## One-Sentence Summary

> Lamotrigine is an established antiepileptic (voltage-gated sodium-channel blocker) used for epilepsy, including partial seizures and Lennox-Gastaut syndrome. The TxGNN model's top-ranked new-indication prediction is **Cutis Verticis Gyrata**, but this signal carries a **TxGNN score of 0%** and is backed by **0 clinical trials** and **0 publications**, indicating a likely knowledge-graph artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial seizures, Lennox-Gastaut syndrome) — inferred from the evidence pack's own mechanistic rationale; official NPRA label indication text is a data gap (see DG001) |
| Predicted New Indication | Cutis Verticis Gyrata |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity — remediation: query DrugBank API). Based on the information available, Lamotrigine is a broad-spectrum antiepileptic drug that blocks voltage-dependent sodium channels, stabilizing neuronal membranes and inhibiting the release of excitatory neurotransmitters (glutamate, aspartate). This action underlies its established use in epilepsy.

For the top-ranked prediction, **Cutis Verticis Gyrata** (a rare scalp connective-tissue/skin hyperplasia disorder), the evidence pack's own rationale is explicit: there is **no identifiable mechanistic link** between lamotrigine's sodium-channel/glutamate-inhibition pathway and the pathophysiology of this condition. Combined with a TxGNN score of 0.00% and zero clinical trials or literature, this candidate is best interpreted as **knowledge-graph noise** rather than a biologically plausible repurposing hypothesis.

It is worth noting that the remaining candidates in this evidence pack (epilepsy, Lennox-Gastaut syndrome, partial epilepsy) are **not novel predictions** — the model's own rationale for each states these are lamotrigine's existing, label-established indications, which is why they carry rich L1-level evidence (multiple completed Phase 3 RCTs, SANAD/SANAD II, Cochrane reviews). The one candidate with a weaker but genuinely exploratory signal is **visual (photosensitive) epilepsy** (rank 5, L3, "Research Question" recommendation) — broad sodium-channel blockade is theoretically applicable, but no literature specifically addresses this seizure phenotype.

---

## Clinical Trial Evidence

*(for the top-ranked candidate, Cutis Verticis Gyrata)*

Currently no related clinical trials registered.

---

## Literature Evidence

*(for the top-ranked candidate, Cutis Verticis Gyrata)*

Currently no related literature available.

---

## Malaysia Market Information

20 product registrations are on record for Lamotrigine in Malaysia, but the evidence pack does not contain populated license details (authorization numbers, product names, dosage forms, manufacturers, and approved indication text are all unavailable in the source data — see DG001, Blocking severity). Retrieval of the NPRA label PDF is required before this section can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in the evidence pack — DG001, Blocking severity, currently prevents entry into the S1 safety pre-assessment stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Cutis Verticis Gyrata) has a 0% prediction score, no supporting clinical trials or literature, and no plausible mechanistic link per the model's own rationale — it does not meet the threshold to advance. Separately, a Blocking-severity data gap (missing NPRA label warnings/contraindications) prevents any candidate for this drug from entering safety pre-assessment (S1) at present.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the NPRA/Malaysia label PDF for warnings and contraindications
- Resolve DG002 (High): query DrugBank API for confirmed mechanism of action
- If pursuing a genuinely novel signal, prioritize **visual/photosensitive epilepsy** (rank 5) for targeted literature review rather than Cutis Verticis Gyrata
- Populate Malaysia license/registration details (authorization numbers, product names, approved indication text) currently missing from the data source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

