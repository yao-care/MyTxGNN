---
layout: default
title: Doxofylline
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Doxofylline
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

# Doxofylline: From Asthma/COPD to Pierre Robin Syndrome (Chromosomal Anomaly)

## One-Sentence Summary

Doxofylline is a methylxanthine-class bronchodilator used clinically for asthma and chronic obstructive pulmonary disease (COPD). The TxGNN model's top prediction is **Pierre Robin syndrome associated with a chromosomal anomaly**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as a likely score artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in the Malaysia regulatory record (license fields empty); per literature in this evidence pack, doxofylline is used as a bronchodilator for asthma and COPD |
| Predicted New Indication | Pierre Robin syndrome associated with a chromosomal anomaly |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, high severity). Based on the literature entries present elsewhere in this evidence pack, doxofylline is a methylxanthine derivative — mechanistically related to theophylline — with bronchodilator and anti-inflammatory activity via phosphodiesterase (PDE) inhibition and (unlike theophylline) minimal adenosine-receptor blockade, which gives it a more favorable cardiovascular safety profile. Its established use is in asthma and COPD.

Pierre Robin syndrome associated with a chromosomal anomaly is a craniofacial developmental disorder, not a smooth-muscle-tone or airway-inflammation condition. The evidence pack's own rationale for this candidate is explicit: **"無機轉關聯"** — no known mechanistic link between the PDE4/cAMP pathway and this chromosomal/developmental disorder, with the entry supported by zero trials and zero literature. This pattern (high TxGNN score, no supporting evidence, no biological plausibility) is consistent with a model score artifact rather than a real repurposing signal.

It is worth noting that none of the top 10 TxGNN candidates in this evidence pack have genuine therapeutic support: most are structural/genetic disorders with no mechanistic rationale, and the one candidate with meaningful literature ("heart disease," rank 9, L4) is supported only by cardiovascular *safety/tolerability* studies (doxofylline vs. theophylline not inducing cardiostimulant effects) — not by any trial or publication evaluating efficacy against heart disease itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

The evidence pack records the drug as marketed in Malaysia with 1 registration on file, but structured license details (registration number, product name, dosage form, approved indication text) are not populated in this evidence pack and could not be extracted.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Pierre Robin syndrome associated with a chromosomal anomaly) has no clinical trials, no literature, and no plausible mechanistic link per the evidence pack's own analysis — it does not meet even a minimal bar for further evaluation. No other candidate in the top 10 shows genuine therapeutic evidence either.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF with warnings and contraindications (blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank (high-severity data gap — needed to assess mechanistic plausibility of any candidate)
- Complete Malaysia license/product details (registration number, dosage form, approved indication text)
- If further TxGNN-based repurposing candidates are needed for doxofylline, re-run prediction with tighter mechanistic filtering, since the current top-10 output is dominated by structural/genetic disorders with no biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

