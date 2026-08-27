---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From NSAID Pain/Inflammation Management to Osteoarthritis Susceptibility

## One-Sentence Summary

Ketoprofen is a well-established nonsteroidal anti-inflammatory drug (NSAID) already marketed in Malaysia for pain and inflammatory conditions, including osteoarthritis. TxGNN's top-ranked prediction for this drug, **osteoarthritis susceptibility**, is a genetic-susceptibility trait rather than a treatable clinical disease, and it is supported by **0 clinical trials** and **0 publications** — the evidence base does not currently justify pursuing this specific target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain/inflammatory conditions (NSAID class) — osteoarthritis and related rheumatic/musculoskeletal pain (per this drug's own evidence-pack rationale; TFDA/NPRA license-level indication text not populated in this dataset) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned no MOA record). Based on the mechanistic rationale attached to this candidate in the evidence pack, ketoprofen is a non-selective COX-1/COX-2 inhibitor of the propionic acid NSAID class, acting by suppressing prostaglandin synthesis to relieve pain and inflammation.

However, "osteoarthritis susceptibility" is explicitly flagged in the evidence pack as a **GWAS/genetic-susceptibility node**, not a diagnosable or treatable clinical disease entity. An NSAID cannot intervene on genetic susceptibility itself — it acts downstream, on inflammation and pain once osteoarthritis is clinically manifest. The model's very high confidence score most plausibly reflects that this node sits close to the "osteoarthritis" disease node in the knowledge-graph embedding space, rather than a genuine, actionable new therapeutic signal.

Notably, this same evidence pack shows that ketoprofen already has strong, real-world evidence for osteoarthritis itself (a separate, lower-ranked entry: L1 evidence level, 20 clinical trials, 20 publications) — but that represents its **existing, long-standing indication**, not a novel repurposing opportunity. The top-ranked "susceptibility" prediction should be treated as a distinct, non-actionable model artifact rather than an extension of that established use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA records confirm the drug is marketed with **15 total registrations**, but this dataset did not capture individual authorization numbers, product names, dosage forms, or indication text for the top 5 licenses (all fields returned empty). Registration-level detail needs to be pulled directly from the NPRA product database before this section can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction, osteoarthritis susceptibility, is not a treatable clinical entity and has zero supporting clinical trials or literature — there is no evidentiary or mechanistic basis to advance it.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- DrugBank mechanism-of-action data (currently a High-severity data gap)
- Complete NPRA license-level detail (product name, dosage form, approved indication text) for the 15 existing registrations
- If repurposing interest continues for this drug, redirect evaluation toward this drug's mechanistically coherent, better-evidenced signals in the same evidence pack — osteoarthritis (L1) and arthropathy (L2) — noting these represent existing/overlapping uses rather than novel indications, so any "repurposing" framing there would need separate justification (e.g., new formulation, route, or patient population)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

