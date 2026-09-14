---
layout: default
title: Resorcinol
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 6
---

# Resorcinol
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

# Resorcinol: From Topical Dermatological Use to Acne Keloid

## One-Sentence Summary

Resorcinol is a long-established topical keratolytic and mild antiseptic agent, already used in topical acne-related preparations. The TxGNN model predicts it may be relevant for **Acne Keloid** (acne keloidalis nuchae), but this prediction currently has **no supporting clinical trials or published literature** — it rests on model-graph inference alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA license records (registry entries contain no indication text); pharmacologically classified as a topical keratolytic/antiseptic used in acne-related products |
| Predicted New Indication | Acne Keloid |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for resorcinol is not available (DrugBank query returned no MOA entry). Based on known pharmacological classification, resorcinol acts as a topical keratolytic and mild antibacterial agent and has established use in acne-related topical formulations.

Acne keloidalis nuchae involves follicular inflammation and excess keratin production leading to scarring (keloid-like) papules, typically on the posterior scalp/neck. Since resorcinol's keratolytic and mild antimicrobial action is already applied to acne, there is a superficial mechanistic overlap with acne keloid's keratinization/follicular-inflammation pathway.

However, the evidence pack itself flags this link as a **pharmacological analogy rather than direct evidence** — no trial or case-level data ties resorcinol specifically to acne keloidalis nuchae. The prediction should be read as hypothesis-generating, not as confirmed efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

NPRA records show resorcinol as **marketed** in Malaysia with **6 registered licenses**. However, this evidence pack does not include product-level details (license numbers, product names, dosage forms, or approved indication text) — all fields returned empty from the source query and would need to be re-pulled from NPRA directly.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data were not returned by the current query — DG001 flags this as a **Blocking** gap that prevents initial safety review (S1) until NPRA/TFDA package-insert data is obtained.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN model score (L5, no clinical trials or literature), and a Blocking data gap (missing package-insert warnings/contraindications) prevents any safety evaluation. There is insufficient evidence to advance this candidate at this time.

**To proceed, the following is needed:**
- NPRA/TFDA package insert (warnings, contraindications) — required to clear the S1 safety gate
- Confirmed mechanism of action from DrugBank or primary literature
- Any preclinical, case-report, or observational evidence specific to acne keloidalis nuchae
- Malaysia license-level product details (license numbers, dosage forms, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

