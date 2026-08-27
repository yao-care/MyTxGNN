---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 2
---

# Iohexol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Iohexol: From Radiographic Contrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated contrast agent used for radiographic imaging and glomerular filtration rate (GFR) measurement — it has no established therapeutic indication or CNS pharmacological activity. The TxGNN model predicts a possible signal for **Insomnia**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself notes no known mechanistic link between iohexol and sleep disorders.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current Malaysia registration data (no approved indication text available); known clinical use is as a radiographic/CT contrast agent |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for iohexol is not available in this evidence pack ([Data Gap] on original MOA). Based on known pharmacology, iohexol is a non-ionic iodinated contrast medium — its role is purely diagnostic (radiographic imaging, myelography, GFR determination), and it has no recognized central nervous system pharmacological activity.

Given this, the mechanistic link between iohexol and insomnia is not established. The repurposing rationale attached to this prediction explicitly states that iohexol has "no CNS pharmacological activity" and "no known mechanistic association with the treatment of insomnia." The high TxGNN score most likely reflects a knowledge-graph pattern (e.g., shared nodes with diagnostic procedures or comorbid conditions) rather than a genuine pharmacological signal.

For context, a secondary candidate in this evidence pack — anxiety (TxGNN score 99.25%) — did surface six clinical trials and six publications, but on review all of them use iohexol only as an imaging/GFR-measurement tool within studies of unrelated conditions (renal transplant follow-up, weight-loss surgery, cardiac device monitoring, etc.), not as a treatment for anxiety. This reinforces that iohexol's high TxGNN scores in this evidence pack likely reflect co-occurrence in imaging-heavy studies rather than a therapeutic mechanism, and lowers confidence in the insomnia signal as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Iohexol has 6 active registrations in Malaysia (market status: Marketed), but the source data does not include populated license numbers, product names, dosage forms, or approved-indication text for these entries — no registration-level detail table can be produced from the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications are flagged as a Blocking data gap (DG001) in this evidence pack — this is a prerequisite for any safety pre-assessment (S1) before further evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia signal is an L5, model-only prediction with no clinical trials or literature support, and the evidence pack explicitly notes the absence of any plausible mechanistic link given iohexol's role as a diagnostic contrast agent. The secondary anxiety candidate, despite having trial/literature co-occurrence, was assessed as confounded (iohexol used incidentally for imaging within unrelated studies) rather than genuine therapeutic evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action data (DG001/DG002)
- Any preclinical or mechanistic rationale connecting iodinated contrast agents to sleep or anxiety pathways, if one exists
- Re-evaluation if future clinical trials or literature specific to iohexol and insomnia/anxiety emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

