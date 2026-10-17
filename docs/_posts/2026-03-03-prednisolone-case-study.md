---
layout: default
title: "Case Study: Prednisolone - Known Uses vs. Predicted New Indications"
description: "How MyTxGNN separates Prednisolone's known uses in the knowledge graph from the 5 predicted new indications listed on its drug page."
date: 2026-03-03
categories: [L4]
tags: [Corticosteroids, Case Study]
drugs: Prednisolone
---

# Case Study: Prednisolone

<p class="key-answer" data-question="Does Prednisolone have thousands of new predictions?">
No. Prednisolone has many uses already recorded in the TxGNN knowledge graph. Those are known uses and are excluded. After that check, the MyTxGNN drug page lists 5 predicted new indications, all at evidence level L4.
</p>

---

## Quick Overview

| Attribute | Value |
|-----------|-------|
| **Drug Name** | Prednisolone |
| **DrugBank ID** | DB00860 |
| **Drug Class** | Corticosteroid |
| **Predicted New Indications** | 5 |
| **Evidence Level** | L4 |

---

## Known Uses Are Not Predictions

Corticosteroids like Prednisolone act on many inflammatory and immune pathways, so the knowledge graph already links them to many diseases. MyTxGNN treats those links as known uses:

- Indications and contraindications already recorded for the drug in the knowledge graph are excluded
- Only TxGNN deep learning predictions with a score of at least 0.99 that remain after this check are listed

---

## Predicted New Indications

| Predicted Indication |
|---------------------|
| Erythema multiforme |
| Lymphosarcoma |
| Disease of orbital region |
| Leukemia, lymphocytic, susceptibility to |
| Rheumatic heart disease |

See the [Prednisolone drug page]({{ '/drugs/prednisolone/' | relative_url }}) for evidence and the pharmacist review.

---

## Key Learnings

<div class="key-takeaway">
A prediction that survives the known-use check can still be part of clinical practice. For erythema multiforme, published reviews and case reports already describe systemic corticosteroid treatment, so the prediction mostly confirms existing practice rather than a new discovery.
</div>

### What This Teaches Us

1. **Exclude known uses first**: Counting known uses as predictions inflates the numbers
2. **Check the literature**: Use PubMed and clinical trial registries to see whether a prediction is already in use
3. **Consider safety**: Long-term corticosteroid use carries risks such as osteoporosis and metabolic effects

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This case study is for educational purposes. Prednisolone should only be used under medical supervision. Drug repurposing predictions require clinical validation before application.
</div>
