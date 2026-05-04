---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 1
---

# Aflibercept
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

# AFLIBERCEPT: From Retinal Vascular Disease to Esotropia

## One-Sentence Summary

Aflibercept is a recombinant fusion protein (VEGF trap) that blocks VEGF-A, VEGF-B, and placental growth factor (PlGF) to inhibit pathological angiogenesis, and is primarily indicated for retinal vascular conditions such as wet age-related macular degeneration and diabetic macular edema.
The TxGNN model predicts it may be effective for **Esotropia** (inward deviation of the eye), yet there are **zero supporting clinical trials** and **zero published literature** backing this direction.
Critically, the available mechanistic signal runs *counter* to a therapeutic role — existing evidence associates intravitreal anti-VEGF treatment with *causing* esotropia rather than resolving it.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Retinal vascular disease (wet AMD, diabetic macular edema) — detailed regulatory text not available in current dataset |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 — model prediction only; no clinical trials or literature identified |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Aflibercept acts as a decoy receptor, binding VEGF-A, VEGF-B, and PlGF with high affinity and preventing them from activating their native receptors on vascular endothelial cells. This arrests the growth of leaky, aberrant blood vessels in the retina. The drug is administered by intravitreal injection and has a well-established role in conditions driven by retinal neovascularisation.

Esotropia, however, is a form of strabismus characterised by inward turning of one or both eyes. Its aetiology involves neuromuscular imbalance of the extraocular muscles, refractive accommodation errors, or deficits in ocular motor innervation — mechanisms that have no established direct link to the VEGF signalling pathway. The two disease categories occupy fundamentally different pathophysiological territory.

The high TxGNN score (99.38%) most likely reflects a **confounding co-occurrence pattern** in the knowledge graph rather than a true therapeutic relationship. Aflibercept is frequently used to treat retinopathy of prematurity (ROP), and esotropia is a known *complication* of ROP and its treatments. The graph therefore encodes a shared disease context ("anti-VEGF drug ↔ retinal disease ↔ strabismus") rather than a pharmacological mechanism of benefit. Reinforcing this concern, published literature on intravitreal anti-VEGF therapy (bevacizumab, ranibizumab) for ROP shows a **significantly elevated incidence of subsequent esotropia** compared to laser photocoagulation, with the proposed mechanism being that VEGF participates in the development of retinal ganglion cells and lateral rectus muscle innervation. Blocking VEGF during a sensitive developmental period may disrupt rather than restore normal ocular alignment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Six product registrations are recorded for AFLIBERCEPT in Malaysia. Detailed registration information — including authorization numbers, product names, dosage forms, and approved indication texts — was not available in the current data extract. Please refer to the Malaysian National Pharmaceutical Regulatory Agency (NPRA) database directly for full registration records.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Two data gaps with direct safety relevance have been flagged: (DG001) TFDA package insert warnings and contraindications have not yet been retrieved, which blocks a formal safety pre-screen; (DG002) detailed mechanism of action data from DrugBank is pending, which limits the mechanistic risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical or published evidence supports aflibercept as a treatment for esotropia, and the biological signal points in the *opposite* direction — anti-VEGF agents appear to be a risk factor for strabismus, not a remedy for it. The TxGNN score, while numerically high, is assessed as a confounding artefact of shared disease context rather than genuine therapeutic relevance.

**To proceed, the following would be needed:**

- A credible mechanistic hypothesis explaining how VEGF inhibition could *correct* esotropia (not currently supported in the literature)
- Preclinical data (animal models or in vitro) demonstrating therapeutic benefit in strabismus or extraocular muscle dysfunction
- Retrieval and review of the full approved indication texts from the Malaysian NPRA database (6 registrations on file)
- TFDA package insert warnings and contraindications to complete the safety pre-screen (DG001 — Blocking severity)
- DrugBank MOA and category data to enable mechanistic link and cytotoxicity classification (DG002 — High severity)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

