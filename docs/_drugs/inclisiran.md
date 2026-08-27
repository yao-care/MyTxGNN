---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: Original Indication Not Available — Predicted Association with Potassium Deficiency Disease (Low Confidence)

## One-Sentence Summary

Inclisiran (DrugBank DB14901) is a PCSK9-targeting siRNA therapeutic; its original approved indication is not recorded in this evidence pack (data gap). The TxGNN model's top-ranked candidate is **Potassium Deficiency Disease** (score 99.93%), but the evidence pack's own review flags this link as a likely **false positive** of the TxGNN embedding space, with **no clinical trials and no literature** identified to support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (data gap — `drug.original_indications` empty, license text empty) |
| Predicted New Indication | Potassium Deficiency Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Inclisiran is marked as a data gap (DG002) in this pack. The only mechanistic information available comes from the model's own rationale text, which identifies Inclisiran as acting through the **PCSK9 pathway** (consistent with its known role as an LDL-cholesterol–lowering siRNA).

For the top-ranked candidate, however, the evidence pack's rationale is explicit that **no plausible mechanistic connection exists**: *"PCSK9 通路與鉀離子代謝無已知關聯，判斷為 TxGNN 嵌入空間之偽陽性關聯"* (no known relationship between the PCSK9 pathway and potassium metabolism; assessed as a false-positive artifact of the TxGNN embedding space). No clinical trials, ICTRP records, or PubMed literature were found linking Inclisiran to potassium deficiency disease.

It is also worth noting this is not an isolated case within this candidate set — ranks 2–10 in the same pack (esophageal disease, aortic malformation, migraine variants, esophageal ulcer, Raynaud disease, etc.) were each independently assessed as lacking a credible mechanistic basis, and where evidence was returned (migraine-susceptibility literature, aortic-malformation trials), it was found on review to be either off-topic (epilepsy/migraine genetics unrelated to PCSK9) or mismatched (the "aortic malformation" trials were verified to actually be pediatric familial hypercholesterolemia studies — a disease-label mapping error, not real supporting evidence).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

One registration record exists (`total_licenses = 1`), but the license number, product name, dosage form, and approved indication text are all empty in this evidence pack — no usable licensing detail is currently available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack; DG001 — TFDA label warnings/contraindications — is flagged as a **Blocking** gap that prevents safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Potassium Deficiency Disease) has no clinical trial or literature support, and the evidence pack's own mechanistic review labels it a likely false positive from the TxGNN embedding space. No candidate among the top 10 predictions in this batch has both a plausible mechanistic link and corroborating real-world evidence. Combined with a **blocking** safety data gap (DG001), this candidate is not ready to advance beyond model prediction.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (warnings, contraindications) — resolves DG001 (blocking)
- Confirmed original approved indication(s) and detailed MOA — resolves DG002 and the missing title/overview fields
- Complete drug license details (product name, dosage form, indication text) for the existing registration
- If pursuing repurposing further, re-run KG/literature search against alternative candidate diseases with clearer PCSK9-pathway biological plausibility, since ranks 1–10 in this batch do not meet that bar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

