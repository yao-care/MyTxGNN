---
layout: default
title: Mometasone Furoate
parent: 僅模型預測 (L5)
nav_order: 489
evidence_level: L5
indication_count: 5
---

# Mometasone Furoate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the evidence pack as given — note upfront: `original_indications` and all `licenses[].approved_indication_text` fields are empty, and every `predicted_indications[*].txgnn.score` is 0.0. I'm reporting these as-is rather than inferring values, and flagging the gaps explicitly instead of using `[Data Gap]` tags.

---

# Mometasone Furoate: From Corticosteroid-Responsive Skin Conditions to Neurodermatitis

## One-Sentence Summary

Mometasone Furoate is a synthetic corticosteroid marketed in Malaysia across 36 registrations, though its specific NPRA-approved indication text was not returned in this evidence pack. The TxGNN model's top-ranked prediction is **Neurodermatitis** (lichen simplex chronicus), but this ranking currently carries **0 clinical trials** and only **1 tangentially related publication** — the weakest evidence profile among the five predictions in this pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — NPRA license indication text was not returned for any of the 36 registrations |
| Predicted New Indication | Neurodermatitis |
| TxGNN Prediction Score | 0.00% (as recorded in source data) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 36 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate (DG002). Based on general pharmacology, Mometasone Furoate is a synthetic glucocorticoid used in topical, intranasal, and inhaled formulations, acting via the glucocorticoid receptor to suppress local inflammatory and immune responses. This class of drug is broadly used across corticosteroid-responsive dermatoses.

Neurodermatitis (lichen simplex chronicus) is a chronic, pruritic inflammatory skin condition, and topical corticosteroids are an established first-line treatment class for it — so the mechanistic plausibility of the prediction is reasonable on class grounds. However, the single literature record returned for this specific disease pairing (PMID 25608275) does not actually study mometasone furoate; it evaluates silk-fabric underwear as an adjuvant for vulvar lichen simplex chronicus. It is drug-adjacent evidence, not direct evidence of mometasone furoate's efficacy in neurodermatitis.

It's also worth noting that within this same evidence pack, three other predicted indications — **atopic eczema** (10 trials, 20 papers), **asthma** (20 papers), and **exanthem** (1 trial, 5 papers) — have substantially stronger and more direct evidence bases for mometasone furoate specifically. See Conclusion for a prioritization recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25608275](https://pubmed.ncbi.nlm.nih.gov/25608275/) | 2015 | RCT | Menopause (New York, N.Y.) | Double-blind RCT evaluating silk fabric underwear as an adjuvant tool in managing vulvar lichen simplex chronicus (a neurodermatitis subtype); does not directly test mometasone furoate |

## Malaysia Market Information

NPRA/market data confirms 36 active registrations for Mometasone Furoate in Malaysia (market status: 已上市), but this evidence pack did not return product-level detail — license numbers, product names, dosage forms, and approved indication text were all blank for every record queried. This should be pulled directly from NPRA before any decision is finalized.

## Safety Considerations

Please refer to the package insert for safety information. (DG001: TFDA/NPRA label warnings and contraindications were not retrieved — this is flagged as a **Blocking** gap that prevents a formal safety (S1) assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (neurodermatitis) has a 0.00% TxGNN score, no clinical trials, and only one drug-adjacent (not drug-specific) publication — insufficient evidence to proceed. A Blocking data gap (missing label warnings/contraindications) also prevents any safety pre-screen regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve DG001: retrieve NPRA package insert (warnings, contraindications) before any S1 safety review can start
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank
- Obtain NPRA license-level detail (product names, dosage forms, approved indication text) for the 36 registrations
- Direct clinical evidence connecting mometasone furoate specifically to neurodermatitis/lichen simplex chronicus
- **Reprioritize candidate selection**: within this same evidence pack, atopic eczema (rank 4, 10 trials incl. completed Phase 2/4 studies, 20 publications) and asthma (rank 5, 20 publications including Phase 3 RCTs) have far stronger evidence bases than the current rank-1 neurodermatitis prediction and warrant separate evaluation as the lead repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

