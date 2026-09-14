---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 614
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Silodosin is a highly selective alpha-1A adrenergic receptor antagonist used to treat benign prostatic hyperplasia (BPH) and lower urinary tract symptoms (LUTS).
> The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth syndrome,
> but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the prediction as likely a knowledge-graph embedding artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) / Lower Urinary Tract Symptoms (LUTS) — based on known drug class; structured NPRA indication text not available in this evidence pack |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap). Based on known information, silodosin is a highly selective alpha-1A adrenergic receptor antagonist that relaxes smooth muscle in the prostate and bladder neck, and is approved for BPH and associated lower urinary tract symptoms.

There is no known or plausible mechanistic link between alpha-1A receptor antagonism and Ambras type hypertrichosis, a rare congenital disorder of follicular development. The evidence pack's own rationale is explicit on this point: it describes the prediction as most likely arising from proximity in the TxGNN knowledge-graph embedding space rather than any genuine biological relationship, and notes it has no supporting biological plausibility.

This assessment is reinforced by the pattern across silodosin's top 6 predicted indications: nearly all are rare congenital or dysmorphic syndromes (hypertrichosis, odonto-periodontal malformation syndrome, Dandy-Walker malformation, hair shaft abnormality, familial trichomegaly) that cluster together in a way suggestive of a systematic embedding artifact rather than five independent, biologically grounded repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Silodosin is registered and marketed in Malaysia (1 NPRA license on file), but the evidence pack does not contain the underlying license number, product name, dosage form, or approved indication text — this needs to be pulled directly from the NPRA registry to complete a product-level record.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/NPRA label warnings and contraindications are a Blocking data gap in this evidence pack (DG001) — this must be resolved before any S1 safety review can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction sits at evidence level L5 (model score only, zero trials, zero literature), and the evidence pack's own mechanistic review judges it biologically implausible and likely an embedding artifact — this holds for all 6 of silodosin's top predicted indications, none of which have supporting clinical or literature evidence. A Blocking data gap in TFDA/NPRA safety labeling also prevents this candidate from entering initial safety screening (S1) regardless of the indication question.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) to close the Blocking safety data gap (DG001)
- Structured mechanism-of-action data from DrugBank (DG002)
- Complete NPRA license record (product name, dosage form, approved indication text) for the Malaysia market entry
- If this candidate is pursued further, an independent review of whether the TxGNN embedding cluster around rare congenital/dysmorphic syndromes reflects a systematic model artifact, before allocating further evidence-collection resources to it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

