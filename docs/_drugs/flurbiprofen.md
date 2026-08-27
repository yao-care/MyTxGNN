---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From NSAID Therapy to Osteoarthritis Susceptibility

## One-Sentence Summary

Flurbiprofen is a well-established non-steroidal anti-inflammatory drug (NSAID) already marketed in Malaysia, though its specific approved indication text is not available in the current regulatory dataset. The TxGNN model's top-ranked prediction is **Osteoarthritis Susceptibility**, a genetic predisposition phenotype rather than a treatable clinical disease, and it is currently supported by **zero clinical trials** and **zero publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current regulatory extract (NPRA license records contain no indication text) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flurbiprofen is a phenylalkanoic acid–derivative NSAID; class-wide, this group works by non-selective inhibition of cyclooxygenase (COX-1/COX-2), reducing prostaglandin synthesis to relieve inflammation and pain.

However, "osteoarthritis susceptibility" is not a treatable clinical entity — it is a genetic/GWAS susceptibility phenotype describing predisposition risk, not disease activity. The evidence pack's own rationale for this candidate states that the high TxGNN score most likely arises from the knowledge graph's structural proximity to the "osteoarthritis" disease node itself, rather than from any drug mechanism acting on genetic susceptibility. No clinical or literature evidence supports this specific pairing.

By contrast, the same evidence pack shows much stronger, better-supported directions further down the ranked list: **rheumatoid arthritis** (rank 2) and **osteoarthritis** (rank 7) both reach evidence level L1 with numerous completed RCTs spanning decades, consistent with flurbiprofen's known, classic use as an anti-inflammatory analgesic in joint disease. These are not novel repurposing hypotheses but confirmations of an already-established use pattern.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

The evidence pack confirms flurbiprofen is marketed in Malaysia with **4 active NPRA registrations**, but the license-level details (authorization number, product name, dosage form, approved indication text) were not populated in this data extract — all fields returned empty.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/NPRA label warnings and contraindications are flagged as a Blocking data gap (DG001) — the drug's package insert has not yet been retrieved and parsed, so no safety pre-screening (S1) can be completed at this time.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, osteoarthritis susceptibility, has no clinical trial or literature support (L5/S0) and targets a genetic risk phenotype rather than an actionable disease — the evidence pack's own analysis attributes the high score to knowledge-graph proximity rather than a genuine drug-disease signal. A Blocking data gap on label warnings/contraindications also prevents any safety evaluation.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — Blocking gap, required before any S1 safety review
- DrugBank-sourced mechanism of action data
- Clarification on whether this candidate should instead be re-scoped to the better-evidenced rheumatoid arthritis (L1) or osteoarthritis proper (L1) predictions from the same evidence pack, since those already carry Proceed with Guardrails recommendations
- Malaysia license detail records (product names, dosage forms, approved indication text) to complete the market table
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

