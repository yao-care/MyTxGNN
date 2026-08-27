---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

Using the general drug-repurposing evidence pack you provided (no specialized skill applies to this pure report-authoring task — it's a direct template-fill job), here is the evaluation report generated strictly from the fields present in the Evidence Pack, with clearly labeled data gaps where the pack is empty (per the "no [Data Gap] literal, no fabrication" rules).

---

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor generally known to be used for benign prostatic hyperplasia (BPH); the Malaysia-specific approved indication text was not available in this evidence pack. The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the pack's own mechanistic analysis flags the biological direction as inconsistent with the drug's known pharmacology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) — based on general pharmacological knowledge; not sourced from this pack (Malaysia license indication text was empty for all entries) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on general pharmacological knowledge, dutasteride is a dual inhibitor of both Type 1 and Type 2 5α-reductase, the enzyme that converts testosterone to dihydrotestosterone (DHT). By lowering DHT, it shrinks androgen-driven prostate tissue — the basis of its established use in BPH — and, through the same mechanism, reduces hair growth in androgen-sensitive follicles (the rationale behind its known off-label/regional use for androgenetic alopecia).

Ambras type hypertrichosis universalis congenita is a rare, congenital, autosomal-dominant condition (associated with rearrangements at chromosome 8q) characterized by excessive generalized hair growth. Critically, its pathophysiology is **not androgen-dependent** — it is a structural/developmental disorder of hair follicle patterning, not a hormone-driven process.

This means the mechanistic direction is inconsistent on two levels: (1) dutasteride *reduces* hair growth in androgen-sensitive follicles, whereas hypertrichosis would require *increasing or correcting* hair distribution, and (2) the target condition is congenital/structural rather than DHT-mediated, so lowering DHT would not be expected to have any effect on it. The evidence pack's own rationale for this candidate explicitly notes there is no clinical trial or literature support, and characterizes the prediction as arising from knowledge-graph embedding similarity rather than a substantiated biological link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Malaysia's NPRA records show dutasteride as **✓ Marketed** with **14 active registrations**. However, individual license-level details (registration number, product name, dosage form, and approved indication text) were not returned in the current evidence pack for any of the sampled entries — this is a data gap requiring direct NPRA lookup before licensing/labeling claims can be made.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack — DG001, Blocking severity: this gap prevents the candidate from entering the S1 safety pre-screen stage.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction has no clinical trial or literature support (L5, model-prediction-only) and its own mechanistic rationale describes a directional mismatch between dutasteride's known pharmacology and the biology of the target condition — consistent with a knowledge-graph artifact rather than a plausible repurposing lead. In addition, TFDA/NPRA-equivalent safety labeling data is entirely missing (DG001, Blocking), which by itself prevents any candidate for this drug from proceeding to safety evaluation regardless of indication.

**To proceed, the following is needed:**
- Retrieve Malaysia package insert warnings and contraindications (DG001, Blocking — required before any S1 safety screen)
- Retrieve DrugBank/authoritative MOA detail (DG002)
- Populate license-level Malaysia market data (registration numbers, product names, dosage forms, approved indication text) for the 14 existing registrations
- If repurposing evaluation continues for this drug, consider redirecting attention to a mechanistically coherent candidate rather than the top-ranked one — e.g., "diffuse alopecia areata" (rank 8, L3/S1, 1 supporting review) — though note the pack itself flags this as likely conflating androgenetic alopecia (mechanistically well-supported for dutasteride) with alopecia areata (autoimmune, mechanistically unrelated); this disease-ontology ambiguity should be resolved before further evidence collection is invested there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

