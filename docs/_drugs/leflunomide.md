---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

> Leflunomide is a DHODH inhibitor / immunomodulator clinically established for rheumatoid arthritis (this original-indication detail is general pharmacological knowledge, not present in the source evidence pack — TFDA license text was returned blank).
> The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital skeletal developmental disorder,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review found no known biological link between the drug's mechanism and this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from TFDA license records in this evidence pack (all 5 registrations returned blank indication text); clinically known for rheumatoid arthritis (general knowledge, unverified against local label) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.93% (rank 1531 of full candidate list) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, leflunomide is a dihydroorotate dehydrogenase (DHODH) inhibitor that blocks pyrimidine synthesis, producing an immunomodulatory effect used clinically in autoimmune conditions such as rheumatoid arthritis.

Brachydactyly-syndactyly syndrome is a congenital skeletal malformation syndrome, driven by developmental/structural gene defects rather than autoimmune or inflammatory processes. The evidence pack's own repurposing rationale is explicit that there is **no known mechanistic overlap** between leflunomide's DHODH-inhibition/immunomodulatory action and the developmental pathology underlying this syndrome — the score reflects a graph-topology association from the TxGNN model, not a pharmacologically grounded hypothesis. The same caveat applies to the second-ranked candidate (colobomatous microphthalmia-rhizomelic dysplasia syndrome, score 99.93%, rank 1568), which is likewise a congenital structural syndrome with no identified mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

5 registrations exist for leflunomide in the source registry, but license-level detail (authorization number, product name, dosage form, approved indication text) was not returned in this evidence pack — all fields came back blank. This must be re-queried before it can be reported.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA warning/contraindication data is flagged as a **Blocking** data gap (DG001) — it must be resolved before this candidate can proceed to safety screening (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN model output (L5) with zero supporting clinical trials or literature, and the evidence pack's own mechanistic assessment finds no known biological plausibility linking leflunomide's mechanism to this developmental/skeletal syndrome. A blocking safety data gap also prevents any initial safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — resolve DG001 before any S1 safety screening
- Confirmed mechanism of action from DrugBank — resolve DG002
- Complete TFDA license records (authorization numbers, approved indication text) for the 5 existing registrations
- Preclinical or mechanistic evidence establishing a plausible biological rationale for this indication, given the current rationale finds none
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

