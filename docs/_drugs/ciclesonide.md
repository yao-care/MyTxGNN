---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 6
---

# Ciclesonide
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

# Ciclesonide: From Inhaled Corticosteroid Therapy to Atopic Eczema

## One-Sentence Summary

> Ciclesonide is a corticosteroid prodrug marketed in Malaysia as an inhaled/intranasal formulation (no NPRA indication text is available in the current dataset, but ciclesonide is an established inhaled corticosteroid, e.g. Alvesco/Omnaris, for asthma and allergic rhinitis).
> The TxGNN model predicts it may be effective for **Atopic Eczema**,
> with **no clinical trials** and **no publications** currently supporting this specific indication — the prediction stands on mechanism alone, and a route-of-administration mismatch (no topical dermatological formulation exists) needs to be resolved before this can advance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA license records provided (ciclesonide is a known inhaled corticosteroid, typically indicated for asthma/allergic rhinitis) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ciclesonide is not available in this dataset (flagged as a High-severity data gap). Based on known information, ciclesonide is an inhaled corticosteroid prodrug: after deposition in the lung it is activated by esterases to des-ciclesonide, which binds the glucocorticoid receptor and suppresses airway inflammation. This is the shared mechanism of the inhaled corticosteroid (ICS) class rather than evidence specific to ciclesonide.

The proposed link to atopic eczema rests entirely on this same anti-inflammatory glucocorticoid mechanism — corticosteroids are, in general, effective for atopic dermatitis when applied topically. However, the evidence pack explicitly flags a critical gap between mechanism and feasibility: **ciclesonide currently exists only as an inhaled and intranasal formulation, with no approved topical/dermatological product.** Without a skin-appropriate formulation, the mechanistic plausibility cannot translate into a deliverable therapy as-is, and this prediction should be read as a class-level hypothesis rather than an actionable, drug-specific signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*Note: No clinical trials or publications were found specifically studying ciclesonide in atopic eczema/dermatitis. This ranks the prediction at L5 (model prediction only).*

---

## Malaysia Market Information

Five NPRA licenses are on record for ciclesonide (market status: ✓ Marketed), but the license number, product name, dosage form, manufacturer, and approved indication text were not populated in the current dataset for any of the 5 entries. Retrieving the underlying NPRA/label PDFs is needed before this information can be reported.

---

## Safety Considerations

No structured TFDA/NPRA key warnings, contraindications, or drug-interaction data are currently available for ciclesonide (DG001, Blocking severity — retrieval of the official label PDF is pending).

**Literature safety signal (class-relevant):** A case report (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), *Contact Dermatitis*, 2012) describes systemic allergic dermatitis caused by inhaled budesonide, with cross-reactivity to ciclesonide confirmed on patch testing. This is a drug-*causing*-dermatitis safety signal for the ICS class, not evidence of ciclesonide treating dermatitis — but it is directly relevant here: it suggests ICS-class corticosteroids, including ciclesonide, carry a documented (if rare) risk of contact/systemic allergic dermatitis via cross-reactivity, which warrants specific attention if a dermatological repurposing pathway is ever pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The atopic eczema prediction has no supporting clinical trials or literature (L5, model-prediction-only) and a formulation/route mismatch that the mechanistic rationale itself identifies as unresolved. Combined with a Blocking-severity gap in TFDA/NPRA safety labeling data (DG001), this candidate cannot yet enter even initial (S1) safety screening.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (key warnings, contraindications, DDI) to close DG001 and unblock S1 safety screening
- Confirmed DrugBank MOA record to close DG002
- A feasibility assessment of whether a topical/dermatological ciclesonide formulation exists or is developable, since none is currently marketed
- Preclinical or mechanistic studies specific to atopic dermatitis, given the corticosteroid class carries a documented cross-reactive allergic dermatitis risk (PMID 22957490)
- For context: a related candidate, **bronchitis** (rank 4, L4, decision stage S1, "Research Question"), is mechanistically closer to ciclesonide's existing respiratory use and has at least guideline-level literature support — it may be a more tractable next candidate to investigate than atopic eczema.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

