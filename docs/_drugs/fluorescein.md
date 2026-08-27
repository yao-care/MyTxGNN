---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein: From Diagnostic Ophthalmic Use to Prinzmetal Angina

## One-Sentence Summary

Fluorescein is a diagnostic fluorescent dye traditionally used for ophthalmic angiography and ocular surface staining, not a therapeutic agent with an established treatment indication.
The TxGNN model predicts it may be effective for **Prinzmetal Angina**, but this prediction is supported by **0 clinical trials** and **0 publications** — no evidence of any kind exists to substantiate it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic dye for ophthalmic angiography / ocular surface staining (specific licensed indication text not available in this data pack) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity data gap). Based on known information, Fluorescein is a fluorescent dye used to visualize retinal/iris vasculature and ocular surface defects diagnostically — it has no established pharmacological activity on coronary vascular smooth muscle or the vasospastic mechanisms underlying Prinzmetal angina.

The evidence pack's own repurposing rationale is explicit on this point: there is **no mechanistic link**, and the prediction has zero corroborating clinical trials or literature across all three evidence sources queried (ClinicalTrials.gov, ICTRP, PubMed). This pattern — a high TxGNN score with a complete absence of supporting real-world evidence — is most consistent with **knowledge-graph noise** rather than a genuine biological signal, and should not be interpreted as a credible repurposing hypothesis.

It is also worth noting that across the other 9 ranked candidates for this drug, the pattern repeats: most have zero evidence, and the few with retrieved literature (e.g., hemoglobinopathy, thrombophilia, hyperthyroidism) are confounded — the studies use fluorescein *angiography* as a diagnostic imaging tool to detect vascular complications of those diseases, not as a treatment for them. None of the 10 predictions currently has genuine therapeutic-use evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

License-level details (registration number, product name, dosage form, approved indication text) were not returned in this data pack — all fields were blank. What is confirmed: the product is marketed in Malaysia (✓ Marketed) with 1 total registration on file.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications are flagged as a Blocking data gap — DG001 — meaning this candidate cannot yet enter a formal S1 safety review.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prinzmetal angina) has zero supporting clinical trials or literature and no plausible mechanism of action — it is best explained as model noise rather than a real signal. No candidate in this evidence pack currently has genuine therapeutic-use evidence for repurposing.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- DrugBank mechanism of action data for Fluorescein — currently a High-severity data gap (DG002)
- A disease-specific literature/trial search that excludes diagnostic-imaging uses of fluorescein, to determine whether any of the 10 predicted indications has genuine therapeutic support
- If no mechanistic or evidentiary support emerges, this candidate should be deprioritized in favor of higher-scoring repurposing opportunities elsewhere in the pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

