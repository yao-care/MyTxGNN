---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 500
evidence_level: L5
indication_count: 3
---

# Nevirapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Nevirapine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for human HIV-1 infection. The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a cat disease, not a human indication — supported by only **1 in vitro/structural comparison publication** and **no clinical trials**. The evidence pack itself flags this and the other two ranked candidates as low-value, non-actionable signals.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Official TFDA/NPRA indication text is missing from the four registered licenses; Nevirapine is a known NNRTI used to treat HIV-1 infection in humans |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (preclinical/mechanistic study only) |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug entry is not available (data gap). Based on the supporting evidence in this pack, Nevirapine belongs to the NNRTI class and works by directly inhibiting HIV-1 reverse transcriptase (RT); this mechanism has proven efficacy in human HIV-1 infection.

The predicted indication, however, is a feline disease (FIV), not a human condition. The one supporting publication (PMID 38031646) is a structural/biochemical comparison of NNRTIs (including nevirapine, efavirenz, and rilpivirine) against feline vs. human RT — it investigates cross-species enzyme differences, and does not demonstrate treatment efficacy. Structurally, FIV reverse transcriptase differs substantially from HIV-1 RT, and NNRTIs are traditionally considered poorly active against FIV RT.

Because FIV is a veterinary disease, this prediction does not constitute a viable human drug-repurposing hypothesis even if the mechanistic link were stronger — it has research value only for comparative virology, not clinical application. The other two ranked candidates in this pack (Simian Immunodeficiency Virus infection, and a rare human neurodevelopmental disorder) are similarly non-actionable: the SIV literature largely reflects existing antiretroviral pharmacology re-surfaced by the graph rather than a novel indication, and the neurodevelopmental disorder has no literature, no trials, and no known mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In Vitro (structural comparison) | Journal of Veterinary Science | Compared nevirapine, efavirenz, and rilpivirine against feline vs. human immunodeficiency virus reverse transcriptase; no effective FIV treatment currently exists, and this study investigates NNRTI structural applicability to FIV RT rather than demonstrating clinical efficacy |

## Malaysia Market Information

TFDA/NPRA records show 4 active registrations for this drug (market status: marketed), but the license number, product name, dosage form, and approved indication text fields are all empty in the source data, so a detailed registration table cannot be produced from this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. Note: key warnings and contraindications data are marked as a **Blocking** data gap (DG001) — TFDA label warnings/contraindications must be retrieved and reviewed before any S1 safety assessment can proceed. No drug-drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Feline AIDS) is a veterinary, not human, condition, backed only by a single in vitro structural comparison paper (L4, no clinical trials) — it does not represent an actionable human repurposing opportunity as-is. This is compounded by a Blocking data gap on TFDA safety labeling (DG001), which alone prevents progression to S1 safety review regardless of indication strength.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) retrieval and parsing (DG001, Blocking)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Re-evaluation of whether any ranked candidate has a genuine human-relevant indication, since ranks 1–3 in this pack are veterinary, non-human-primate, or evidence-free
- If pursuing cross-species research value only, reframe as a research/translational note rather than a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

