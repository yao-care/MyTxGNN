---
layout: default
title: Peppermint Oil
parent: 僅模型預測 (L5)
nav_order: 537
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: From Unspecified Indication to Leprosy

## One-Sentence Summary

Peppermint oil is currently marketed in Malaysia under 46 NPRA registrations, but the evidence pack does not contain the approved indication text for any of these products. The TxGNN model's top-ranked prediction is that peppermint oil may be effective for **Leprosy**, with a graph-embedding score of **99.80%** — but this prediction is supported by **zero clinical trials** and **zero publications**, and the model's own rationale states there is no known or plausible antimycobacterial mechanism for this drug. This candidate should be treated as a speculative, model-only signal, not an evidence-based lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified — no approved indication text available in the NPRA records supplied |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 46 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available for peppermint oil in this evidence pack (flagged as a High-severity data gap). Peppermint oil's principal active constituent, menthol, is generally known for smooth-muscle relaxant, local anaesthetic, and topical/in-vitro antimicrobial effects — none of which correspond to an established mechanism against *Mycobacterium leprae*.

The evidence pack's own repurposing rationale for this candidate is explicit on this point: there is "no known or plausible antimycobacterial mechanism," and the association exists purely because of the TxGNN model's graph-embedding score, with no clinical or literature support behind it. In other words, this is a case where a high model score does not correspond to biological plausibility.

For context, among the 10 predicted indications returned for peppermint oil, only one — **cardiovascular disease** (rank 9, evidence level L3) — has any real clinical trial or literature backing, including two completed trials on oral peppermint and cardiometabolic outcomes and a 2025 RCT on hypertension. Leprosy, by contrast, sits at the opposite end of the evidence spectrum despite having the single highest raw prediction score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The evidence pack confirms 46 active NPRA registrations for peppermint oil in Malaysia (market status: Marketed), but the license records supplied contain no product name, dosage form, manufacturer, or approved indication text — these fields were not populated in the source extraction. Authorization-level detail cannot be reported until this data gap is resolved.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: NPRA label warnings/contraindications are flagged as a Blocking data gap — this prevents the candidate from entering initial safety screening (S1) regardless of the strength of the efficacy signal.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no clinical trial or literature support, and the mechanistic rationale is assessed as implausible even by the pipeline's own analysis. Combined with a Blocking gap on label warnings/contraindications, there is no basis to advance this candidate past a model-prediction-only status.

**To proceed, the following is needed:**
- NPRA label warnings and contraindications (Blocking gap — required before any safety screening)
- Mechanism of action (MOA) data for peppermint oil (via DrugBank)
- Completed NPRA license/product details (name, dosage form, manufacturer, approved indication text)
- Independent mechanistic or preclinical evidence linking peppermint oil to *M. leprae* or leprosy pathophysiology before this candidate is reconsidered
- If cardiovascular disease is of interest instead, that candidate (rank 9, L3, "Research Question") already has trial and literature support worth a separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

