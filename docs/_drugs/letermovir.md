---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: From Cytomegalovirus (CMV) Prophylaxis to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is a CMV terminase complex inhibitor clinically used for cytomegalovirus (CMV) prophylaxis after allogeneic hematopoietic stem cell transplantation. The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**, but currently **no clinical trials and no publications** support this direction — the prediction rests on knowledge-graph similarity alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the structured registry field (data gap); known clinical use is Cytomegalovirus (CMV) prophylaxis in allogeneic HSCT recipients |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record. Based on known pharmacological information, Letermovir inhibits the CMV terminase complex (pUL51/pUL56/pUL89), blocking cytomegalovirus DNA packaging and cleavage. It has proven efficacy for CMV prophylaxis after allogeneic HSCT.

This mechanism has no known or plausible overlap with the pathophysiology of vulvovaginal candidiasis, a fungal infection driven by targets such as ergosterol synthesis, fungal cell wall chitin, and biofilm formation. There is no mechanistic bridge between a viral DNA-packaging inhibitor and antifungal activity.

Given the very high TxGNN score (99.88%) combined with the complete absence of mechanistic rationale, clinical trials, or literature, this prediction should be treated as a **high-probability false positive** arising from pure knowledge-graph embedding similarity rather than a biologically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Letermovir has 2 active registrations on file with NPRA (Malaysia), market status "Marketed." Product-level details (authorization number, product name, dosage form, approved indication text) are not available in the current data extract and require direct retrieval from NPRA records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature support this indication, and the known mechanism of action shows no plausible link to candidiasis pathophysiology — the prediction cannot pass initial mechanistic or evidentiary screening.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed original indication and detailed MOA from DrugBank (DG002)
- Any preclinical or mechanistic evidence linking terminase inhibition to antifungal activity, should this candidate be revisited
- Full product-level Malaysia registration details (license numbers, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

