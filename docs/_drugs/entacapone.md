---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 5
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to Juvenile Onset Parkinson Disease 19A

## One-Sentence Summary

Entacapone is a peripheral COMT inhibitor used as an adjunct to levodopa/carbidopa in Parkinson's disease, marketed in Malaysia across 11 registrations. The TxGNN model's top-ranked prediction for this candidate points to **Juvenile Onset Parkinson Disease 19A (PARK19A)**, a rare genetic Parkinsonism subtype, but this direction is currently supported by **0 clinical trials** and **0 publications** — the rationale is a mechanistic extrapolation only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, as adjunct to levodopa/carbidopa (per evidence-pack rationale; NPRA label indication text was not populated in this data pull — see Malaysia Market Information) |
| Predicted New Indication | Juvenile Onset Parkinson Disease 19A (PARK19A) |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug-level MOA field in this evidence pack is marked as a data gap (DG002), so DrugBank-verified mechanism data is not yet available. However, the evidence pack's own repurposing rationale (attached to the "Parkinson disease" candidate in this bundle) describes entacapone as a peripherally-acting, selective COMT (catechol-O-methyltransferase) inhibitor: it blocks the conversion of levodopa to 3-O-methyldopa in the gut/plasma, prolonging levodopa's plasma half-life and central availability when co-administered with levodopa/carbidopa.

PARK19A is a rare, early-onset hereditary parkinsonism caused by *DNAJC6* mutations. The mechanistic link proposed for this candidate is that patients with this genetic subtype who are treated with levodopa and who develop motor fluctuations ("wearing-off") could theoretically benefit from entacapone's levodopa-sparing effect, by the same general pharmacological logic used in idiopathic Parkinson's disease.

This is explicitly flagged in the evidence pack as an extrapolation from general PD pharmacology rather than a finding specific to PARK19A — there is no disease-specific mechanistic or pharmacological study behind it, which is why the evidence level is rated L5 (model prediction only, no actual studies).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Entacapone holds **11 NPRA registrations** and is currently **Marketed** in Malaysia. Detailed license-level records (authorization numbers, product names, dosage forms, approved indication text) were not populated in this data pull, so a per-license table cannot be produced without guessing values.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this data pull — obtaining the NPRA/TFDA package insert is flagged as a Blocking data gap, DG001, required before any safety pre-screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature currently support entacapone use in PARK19A specifically; the only basis is a general mechanistic extrapolation from standard levodopa-adjunct therapy in idiopathic Parkinson's disease, applied to an ultra-rare genetic subtype with a fundamentally different, structurally-driven disease process.

**To proceed, the following is needed:**
- NPRA/TFDA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Verified mechanism-of-action data from DrugBank (DG002)
- Any case reports, registries, or genetic-subtype-specific pharmacological data on levodopa/COMT-inhibitor response in PARK19A patients
- Note for context: within this same candidate bundle, the "Parkinson disease" prediction (rank 3) carries strong L1 evidence (multiple completed Phase 3/4 RCTs), but that reflects entacapone's already-approved indication rather than a novel repurposing opportunity — it should not be conflated with the PARK19A hypothesis addressed in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

