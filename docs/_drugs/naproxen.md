---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 496
evidence_level: L5
indication_count: 5
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Naproxen: From Pain and Inflammation (NSAID) to Spondyloarthropathy, Susceptibility To

## One-Sentence Summary

Naproxen is a nonsteroidal anti-inflammatory drug (NSAID), originally used to relieve pain, inflammation and fever in conditions such as arthritis and musculoskeletal injury. The TxGNN model's top-ranked prediction for this drug is **Spondyloarthropathy, susceptibility to**, but this specific prediction carries a **0.00% model score** and is currently supported by **0 clinical trials** and **0 publications** — it should be treated as an unvalidated screening-level signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain, inflammation and fever (NSAID class); exact NPRA-approved indication wording is a data gap in this pack |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for naproxen is not available in this evidence pack (data gap). Based on known pharmacology, naproxen is a propionic-acid-derivative NSAID that non-selectively inhibits COX-1/COX-2, reducing prostaglandin-mediated inflammation and pain — this is a well-established, approved mechanism for musculoskeletal and inflammatory pain.

NSAIDs as a class do have a recognized role in managing spondyloarthropathies (e.g., ankylosing spondylitis), where they are used as first-line symptomatic therapy. This provides a plausible theoretical rationale for the TxGNN association between naproxen and spondyloarthropathy susceptibility.

However, this particular candidate is a **pure knowledge-graph prediction with a score of 0.0** and no supporting clinical trial or literature evidence was retrieved for it. It should be regarded as an initial screening hit only, not a substantiated repurposing signal — notably weaker than several other candidates surfaced for naproxen in the same evidence pack (see note at the end of this report).

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
The TxGNN prediction score for this indication is 0.00%, and no clinical trials or peer-reviewed literature currently link naproxen to spondyloarthropathy susceptibility specifically. There is insufficient evidence to advance this candidate beyond initial screening (S0).

**To proceed, the following is needed:**
- Clinical trial or literature evidence directly linking naproxen to spondyloarthropathy/spondyloarthritis
- Confirmed NPRA-approved indication wording (license-level data currently blank in this pack)
- Mechanism of action data from DrugBank (DG002, High severity)
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking severity — required before any S1 safety assessment)

---

**Note on other candidates in this evidence pack:** This pack contains four additional naproxen repurposing predictions with materially stronger evidence than the one above, and may warrant separate evaluation:
- **Migraine disorder** (L1, S3, *Proceed with Guardrails*) — 50 clinical trials and 20 publications, including multiple completed Phase 3 RCTs supporting the FDA-approved sumatriptan/naproxen combination (Treximet).
- **Osteoarthritis** (L1, S3, *Proceed with Guardrails*) — 50 clinical trials and 20 publications; naproxen is already an established NSAID therapy for OA.
- **Migraine with or without aura, susceptibility to** (L2, S3, *Proceed with Guardrails*) — 20 supporting publications, mechanistically overlapping with the migraine disorder finding above.
- **Myositis** (L4, S1, *Hold*) — 8 publications, mostly case reports of limited relevance to autoimmune myositis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

