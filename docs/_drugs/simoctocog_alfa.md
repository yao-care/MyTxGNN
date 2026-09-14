---
layout: default
title: Simoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Simoctocog alfa (Nuwiq®) is a fourth-generation recombinant human factor VIII (rFVIII) whose established use is replacement therapy in **Hemophilia A**. The TxGNN model's top-ranked new-indication prediction is **Pseudo-von Willebrand Disease**, but this candidate currently has **zero supporting clinical trials and zero publications**, and the drug's own repurposing rationale argues the underlying mechanism does not match this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (not populated in the NPRA license records pulled for this pack; inferred from drug identity as rFVIII replacement therapy and corroborated by the hemophilia evidence below) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is unresolved). Based on known drug identity, simoctocog alfa is a human-cell-line-derived rFVIII that directly replaces the factor VIII deficient in Hemophilia A patients — its efficacy in that setting is well established (see the Hemophilia evidence below, which was captured for this same drug under a different ranked candidate).

For the top-ranked prediction, **Pseudo-von Willebrand Disease**, the mechanistic case is weak. Per the repurposing rationale supplied with this candidate: pseudo-von Willebrand disease is caused by a platelet GP1BA mutation that abnormally increases platelet affinity for von Willebrand factor (VWF), leading to depletion of high-molecular-weight VWF multimers and consumptive thrombocytopenia — it is **not** a FVIII-deficiency disorder. Supplementing rFVIII does not correct this underlying defect. The high TxGNN score most likely reflects semantic proximity within a "bleeding disorder" embedding cluster rather than a genuine pharmacological mechanism, and no clinical trial or literature evidence currently exists to support the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate (Pseudo-von Willebrand Disease) has no clinical or literature evidence (L5) and a mechanistic rationale that argues against efficacy, not for it.
- For context, this evidence pack also screened 9 other TxGNN candidates for simoctocog alfa: the only one with strong evidence is "hemophilia" itself (L1, 3 clinical trials incl. the pivotal NuProtect study, 19 publications) — which is the drug's existing approved indication, not a new repurposing opportunity. The one genuinely novel candidate that reached even a preliminary evidence tier is "symptomatic form of hemophilia in female carriers" (L4, Research Question); all remaining candidates (pseudo-von Willebrand disease, primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome, acquired coagulation factor deficiency, collagen-receptor bleeding diathesis, constitutional thrombocytopenia, and fetal/neonatal alloimmune thrombocytopenia) are Hold, all L5, and several rationales explicitly note the disease mechanism does not involve FVIII deficiency.

**To proceed, the following is needed:**
- Resolve the blocking data gap: TFDA/NPRA package insert warnings and contraindications (currently unavailable), required before any S1 safety screening.
- Obtain confirmed mechanism-of-action data via DrugBank to formally document the drug's original-indication linkage.
- If pursuing repurposing further, prioritize "symptomatic form of hemophilia in female carriers" over pseudo-von Willebrand disease given its more coherent mechanistic link to FVIII replacement, and commission targeted trial/literature searches for that candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

