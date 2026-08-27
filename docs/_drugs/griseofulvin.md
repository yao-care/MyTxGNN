---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 5
---

# Griseofulvin
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

# Griseofulvin: From Dermatophytosis to Myiasis

## One-Sentence Summary

Griseofulvin is a long-established antifungal agent used to treat dermatophyte infections (fungal infections of skin, hair, and nails). The TxGNN model predicts it may be effective for **Myiasis** (fly larvae infestation of tissue), but this direction is currently supported by **0 clinical trials** and only **1 loosely related veterinary literature article**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatophytosis (fungal skin/hair/nail infections) — specific TFDA-approved indication text not available in current evidence pack |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Taiwan Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not yet available for this candidate. Based on known pharmacology, griseofulvin binds fungal microtubulin and disrupts the mitotic spindle during fungal cell division — an antifungal mechanism with no documented antiparasitic or insecticidal activity.

Myiasis is caused by fly larvae infesting living tissue; standard management is mechanical/surgical larval removal, with antiparasitic agents such as ivermectin used adjunctively. There is no known biological pathway connecting griseofulvin's antifungal action to killing or expelling fly larvae.

The TxGNN score of 99.41% is therefore most likely driven by an indirect knowledge-graph association — griseofulvin and myiasis may co-occur under a shared "skin/parasitic skin disease" node cluster — rather than a genuine pharmacological relationship. The same pattern holds for the other top-ranked candidates in this evidence pack (creeping myiasis, furuncular myiasis, wound myiasis, and echinococcosis), none of which have a plausible mechanistic link to griseofulvin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary record | Veterinary review of parasitic skin diseases in dogs and cats; no abstract available, and does not specifically address griseofulvin use in myiasis |

## Taiwan Market Information

6 marketed licenses are on record (market status: Marketed), but license-level details (authorization numbers, product names, dosage forms, approved indication text) are not populated in the current evidence pack and cannot be listed here.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications retrieval is flagged as a blocking data gap — see Next Steps.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score with no clinical trials and no mechanistically or clinically relevant literature — evidence level L5. The proposed mechanism (antifungal microtubule inhibition) has no known relevance to fly larvae infestation, so the association is more likely a knowledge-graph artifact than a true repurposing signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap — required before any S1 safety review)
- Confirmed mechanism of action via DrugBank API
- Any in vitro/in vivo evidence of antiparasitic or larvicidal activity for griseofulvin
- Human clinical or case-report evidence specific to myiasis, since the only literature hit is a veterinary review unrelated to this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

