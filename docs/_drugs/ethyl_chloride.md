---
layout: default
title: Ethyl Chloride
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Ethyl Chloride
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

# Ethyl Chloride: From Topical Anesthesia to Craniostenosis Cataract

## One-Sentence Summary

Ethyl chloride is a volatile halogenated hydrocarbon traditionally used as a topical vapocoolant/local anesthetic (and historically as an inhalation general anesthetic); no structured original-indication text is available in the current Malaysia NPRA registration record. The TxGNN model's top-ranked prediction is **Craniostenosis Cataract**, with a score of **99.77%**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale explicitly flags the signal as likely reflecting graph co-occurrence with cataract-surgery anesthesia rather than a genuine treatment relationship.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data extract (topical/local anesthesia is the drug's general known use) |
| Predicted New Indication | Craniostenosis Cataract |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only; no clinical trials or literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known general pharmacology, ethyl chloride is a short-acting volatile agent applied topically as a vapocoolant/local anesthetic and used historically by inhalation as a general anesthetic. Its efficacy in producing rapid, transient local or general anesthesia is well established, but there is no known mechanism by which it would act on lens protein aggregation, oxidative stress, osmotic/sorbitol pathways, or other processes implicated in cataract formation.

The evidence pack's own repurposing rationale for this and the surrounding candidates (9 of the top 10 predictions are cataract subtypes) is explicit that the high TxGNN score most likely arises from ethyl chloride's co-occurrence with cataract *surgery* nodes in the knowledge graph — i.e., it is commonly used as a topical anesthetic during minor ophthalmic/surgical procedures — rather than any disease-modifying effect on the cataract itself. This is a drug–procedure confusion pattern rather than a drug–disease treatment signal, and the same caveat is repeated independently across the craniostenosis, tetanic, diabetic, mature, immature, cortical, nuclear senile, and senile cataract entries.

The 10th candidate, acne, is rationalized only through the drug's local cooling/analgesic effect during comedone extraction — again a procedural-adjunct use, not a disease-modifying mechanism, with no antimicrobial or anti-inflammatory activity cited.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The NPRA record indicates 1 registered license for ethyl chloride with market status "Marketed," but the authorization number, product name, dosage form, and approved indication text are not populated in the current data extract, so no license-level table can be produced.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a high TxGNN score with zero clinical trial or literature support (L5), and the evidence pack's own mechanistic analysis attributes the score to a co-occurrence artifact (ethyl chloride as a peri-procedural anesthetic for cataract surgery) rather than a real disease-modifying pathway. Combined with a Blocking data gap on TFDA/NPRA label warnings, this candidate does not meet the minimum bar to advance.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- DrugBank-confirmed mechanism of action (DG002)
- An independent mechanistic hypothesis that distinguishes a genuine drug–disease signal from the suspected anesthesia-procedure co-occurrence artifact
- Any preclinical/in vitro data linking ethyl chloride to lens or cataract-relevant pathways before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

