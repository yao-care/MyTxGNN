---
layout: default
title: Norelgestromin
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 1
---

# Norelgestromin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin, the active metabolite of norgestimate, is a third-generation progestin currently marketed in Malaysia as the active component of a combined transdermal contraceptive patch. The TxGNN model predicts a possible link to **Amenorrhea**, with a prediction score of **99.51%**, but this is based **purely on graph-embedding similarity** — there are currently **no clinical trials and no published literature** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (progestin component of a transdermal contraceptive patch) — not separately confirmed in the Malaysia license text, which was not populated in this data pull |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% (rank 7212) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for norelgestromin is not currently available in this evidence pack. Based on known pharmacology, norelgestromin is a third-generation progestin and the active metabolite of norgestimate; progestins as a class act on the endometrium and hypothalamic-pituitary-ovarian axis, and are used clinically to induce withdrawal bleeding or manage cycle regulation — a mechanistic basis that could plausibly extend to amenorrhea.

However, the directionality of this link is ambiguous. Norelgestromin's established clinical role is as the progestin in a combined transdermal contraceptive patch, and chronic progestin exposure from that same class of product is itself a well-recognized *cause* of amenorrhea rather than a treatment for it. TxGNN's graph-embedding similarity does not distinguish between "treats" and "is associated with/causes" relationships, so this prediction should be read as a hypothesis worth investigating, not a therapeutic signal.

No original indication data, no MOA record, and no clinical or literature evidence exist in this pack to resolve that ambiguity — the entire prediction currently rests on model output alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

One NPRA registration is on record (market status: Marketed), but the license number, product name, dosage form, manufacturer, and approved indication text were not populated in this data pull — no usable registration details can be reported without guessing.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — DG001 is flagged as a **Blocking** gap for safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or literature, and the proposed mechanism has an unresolved directionality problem (progestins can plausibly both treat and cause amenorrhea). Combined with a Blocking safety data gap (DG001), the candidate cannot proceed to safety screening (S1) as-is.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — resolves DG001, currently blocking
- Confirmed mechanism of action from DrugBank — resolves DG002
- Confirmed original approved indication text from the Malaysia license record
- Preclinical or mechanistic literature clarifying whether progestin exposure treats or induces amenorrhea in this context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

