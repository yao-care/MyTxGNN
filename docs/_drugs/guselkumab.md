---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Psoriasis to Drug-induced Osteoporosis

## One-Sentence Summary

Guselkumab (an anti-IL-23p19 monoclonal antibody, marketed as Tremfya) was originally approved for moderate-to-severe plaque psoriasis. The TxGNN model's top-ranked prediction in this evidence pack is **drug-induced osteoporosis**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the model's own rationale flags the score as likely embedding noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe plaque psoriasis (identified from evidence-pack annotations; not confirmed by NPRA label text — see Malaysia Market Information) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for guselkumab is not available in this evidence pack (flagged internally as a High-severity data gap requiring DrugBank verification). Based on information embedded elsewhere in this pack, guselkumab is a human IgG1 monoclonal antibody that selectively binds the p19 subunit of interleukin-23 (IL-23), blocking the IL-23/Th17 inflammatory axis — the mechanism underlying its original approval for plaque psoriasis.

For the top-ranked candidate, **drug-induced osteoporosis**, there is no established biological link between IL-23p19 blockade and bone metabolism or steroid-induced osteoporosis pathology. The evidence pack's own rationale states this score likely arises from graph-embedding proximity to "inflammatory disease" nodes rather than genuine pharmacological evidence, and no clinical trials or publications were found to support it.

Worth noting: two other candidates in this same evidence pack carry far stronger support — **psoriasis** (rank 3), which the pack itself identifies as guselkumab's original approved indication rather than a novel prediction, and **ulcerative colitis** (rank 6, L1/S3, 18 trials, 20 publications, including the completed QUASAR Phase 3 program), which the pack notes was already approved in the US in 2024–2025. Neither is a true novel repurposing signal for this evaluation, but they illustrate that the model's raw top score does not correspond to the most clinically actionable finding in this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Guselkumab has 2 registered licenses in Malaysia (market status: Marketed). Detailed registration information — license numbers, product names, dosage forms, and approved indication text — was not captured in this evidence pack and requires direct NPRA lookup.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (drug-induced osteoporosis) has no supporting clinical trials, no literature, and no plausible mechanistic link — the TxGNN score is most likely a graph-embedding artifact rather than a real signal.

**To proceed, the following is needed:**
- NPRA product label / package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action data from DrugBank
- Preclinical or mechanistic rationale connecting IL-23 blockade to bone metabolism, if this indication is to be pursued further
- If a genuinely evidence-backed repurposing opportunity is desired, evaluate **ulcerative colitis** instead (L1 evidence level, Phase 3 RCT support, already approved in other markets) as a separate candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

