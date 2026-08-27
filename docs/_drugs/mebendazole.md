---
layout: default
title: Mebendazole
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 1
---

# Mebendazole
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

# Mebendazole: From Parasitic Infections to Acne

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic, originally used to treat parasitic worm infections by inhibiting parasite β-tubulin polymerization. The TxGNN model predicts it may be effective for **Acne**, but this direction is currently supported by only **0 clinical trials** and **1 loosely related publication** (a case report that merely mentions "acne-like lesions" as a symptom of an unrelated parasitic disease, not actual anti-acne evidence).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parasitic infections (anthelmintic use) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mebendazole is a benzimidazole-class anthelmintic that acts by inhibiting β-tubulin polymerization in parasites, disrupting their microtubule-dependent glucose uptake and cellular structure. No original indication text was retrievable from the Malaysia registration records for this evaluation.

There is currently no known pharmacological rationale linking this microtubule-inhibition mechanism to acne pathophysiology (sebaceous gland inflammation, sebum production, or *C. acnes* bacterial colonization). The TxGNN score of 99.20% reflects a structural association within the knowledge graph rather than a mechanistically validated relationship, and should be interpreted as a hypothesis-generating signal only, not as evidence of clinical efficacy.

The single literature record identified (PMID 7072899) is a 1982 case report of human proliferative sparganosis — an unrelated parasitic disease — in which "acne-like lesions" is used only as a descriptive term for the patient's skin nodules, not as evidence that mebendazole treats acne. This underscores that the prediction currently lacks any direct supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case Report | The American Journal of Tropical Medicine and Hygiene | Case report of human proliferative sparganosis with "acne-like" skin nodules as a symptom descriptor; not a study of mebendazole treating acne |

## Malaysia Market Information

Mebendazole is marketed in Malaysia with 13 active registrations, but detailed product-level records (license number, product name, dosage form, approved indication text) are not available in the current data set.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a knowledge-graph score with no supporting clinical trials and no directly relevant literature; the one retrieved publication is unrelated to acne treatment. Safety data (warnings, contraindications) are also missing, which blocks any initial safety assessment (S1).

**To proceed, the following is needed:**
- TFDA/NPRA package insert data — warnings and contraindications (currently blocking)
- Detailed mechanism of action (MOA) data from DrugBank
- Original indication text from Malaysia registration records
- Dedicated preclinical or clinical evidence directly evaluating mebendazole in acne, rather than incidental literature mentions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

