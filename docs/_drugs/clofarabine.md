---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a purine nucleoside analog originally approved for relapsed/refractory pediatric acute lymphoblastic leukemia (ALL). The TxGNN model predicts it may also be effective for **Myeloid Leukemia**, with a prediction score of **99.88%**, but **0 clinical trials** and **0 publications** are currently captured in this evidence pack, so the mechanistic rationale is not yet backed by retrievable primary evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory pediatric acute lymphoblastic leukemia (ALL) — known global indication; TFDA-specific approved indication text is unavailable in this pack (data gap) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is flagged as a data gap in this pack (DG002). Based on information available within the evidence pack itself, clofarabine is a second-generation purine nucleoside analog in the same pharmacological class as fludarabine and cladribine — it inhibits DNA polymerase and ribonucleotide reductase, driving apoptosis in leukemic blasts. Its efficacy in relapsed/refractory pediatric ALL has been established (FDA accelerated approval, 2004, based on a Phase 2 pivotal trial, as referenced in the rank-8 rationale of this pack).

Myeloid Leukemia is mechanistically adjacent to ALL: both are hematologic malignancies of blast-cell origin, and the same class of purine analogs already has an established role in myeloid disease — the evidence pack's own rationale references combination regimens with low-dose cytarabine in elderly AML/MDS as an active area of Phase 2/3 investigation. This supports biological plausibility for extending clofarabine's cytotoxic activity from lymphoid to myeloid blasts.

That said, this specific evidence pack did not retrieve any clinical trial or literature records for "myeloid leukemia" (ClinicalTrials.gov, ICTRP, and PubMed all returned 0 results per the query log). The mechanistic rationale therefore currently rests on class-effect reasoning rather than indication-specific primary evidence, which is why the evidence level is capped at L2 despite the high model confidence score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia (NPRA) regulatory data confirms **1 active registration** with market status "Marketed." However, the specific license number, product name, dosage form, and approved indication text are not populated in this evidence pack (extraction gap) — please consult the NPRA product registration database directly for the full label.

---

## Cytotoxicity

Clofarabine is a conventional cytotoxic antineoplastic agent (purine nucleoside analog / antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog, same class as fludarabine and cladribine) |
| Myelosuppression Risk | High (class-associated with severe myelosuppression); drug-specific toxicity detail not available — please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert (no data available) |
| Monitoring Items | CBC with differential, liver and renal function, neurological status (class-associated monitoring for purine analogs) |
| Handling Protection | Must follow cytotoxic drug handling regulations as an antineoplastic agent |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- DG001 (TFDA/NPRA label warnings and contraindications) is a **Blocking** gap that prevents even an initial (S1) safety review, and no clinical trial or literature evidence for myeloid leukemia was retrievable in this pack despite a high TxGNN score. The prediction is mechanistically plausible (class effect with fludarabine/cladribine in myeloid disease) but not yet independently verifiable.

**To proceed, the following is needed:**
- Local (Malaysia/TFDA-equivalent) product label with warnings, contraindications, and DDI data (resolves DG001)
- Confirmed mechanism-of-action reference from DrugBank or primary literature (resolves DG002)
- Manual/expanded literature and trial search specifically for clofarabine in AML/MDS (the rationale references elderly AML/MDS + low-dose cytarabine studies not captured by the current automated query set)
- Complete Malaysia license record (product name, dosage form, full approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

