---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir: From HIV-1 Protease Inhibition to No Actionable New Indication Identified

## One-Sentence Summary

Darunavir (DrugBank DB01264) is a well-established HIV-1 protease inhibitor; the specific TFDA-approved indication text is not present in the current data extract, and mechanism-of-action detail is also missing pending a DrugBank API lookup. The TxGNN model's top-ranked prediction, **feline acquired immunodeficiency syndrome**, along with three other candidates, is supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic rationale for each candidate argues against clinical plausibility rather than for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current record (TFDA license indication text field is blank; darunavir is a class-recognized HIV-1 protease inhibitor) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available (flagged as a High-severity data gap, remediation: DrugBank API query). Based on general pharmacological knowledge, darunavir is a peptidomimetic HIV-1 protease inhibitor used to block viral maturation in human HIV-1 infection.

The top-ranked TxGNN prediction — feline acquired immunodeficiency syndrome (FIV) — is a **veterinary** disease outside the scope of human drug repurposing, and the model's own rationale undercuts the prediction: FIV protease has low sequence homology to HIV protease, and published veterinary pharmacology indicates most HIV protease inhibitors show little to no cross-inhibitory activity against FIV protease. The second-ranked candidate (SIV infection) is a non-human primate research/animal-model construct rather than a human clinical indication, so it cannot be translated into a human repurposing pathway despite theoretical protease homology. The third candidate (a rare neurodevelopmental disorder) has no known biological link to protease inhibition and is assessed as a likely knowledge-graph embedding artifact. The fourth candidate (familial combined hyperlipidemia) is directionally implausible: dyslipidemia is a well-documented **adverse effect** of HIV protease inhibitors as a class (via SREBP-1-mediated lipid metabolism effects), not a therapeutic target — the KG association most likely reflects a drug-adverse-event co-occurrence being misread as a treatment relationship, and the disease term itself is tagged "obsolete" in the underlying ontology.

None of the four candidates present a mechanistically sound, translatable human indication based on currently available evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Darunavir has 1 registered license and is currently marketed, but the license record in the current data extract does not include license number, product name, dosage form, or approved indication text — these fields are blank pending source verification.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: retrieval of the TFDA package insert warnings/contraindications is an open, Blocking-severity data gap — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted candidates are Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the model's own mechanistic rationale for each candidate either identifies a species/translation mismatch (veterinary or animal-model disease), a likely embedding artifact, or a reversed causal direction (known adverse effect misread as indication). There is no clinically actionable repurposing signal in this candidate set.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap (DG001); required before any S1 safety screening can occur
- Darunavir mechanism of action via DrugBank API — High-priority gap (DG002); required for mechanistic-link analysis
- Confirmed TFDA-approved indication text from the license record (currently blank)
- Re-screening of the TxGNN output beyond the current top 4 (ranks 806–10,598) for candidates with plausible human-disease relevance and non-zero trial/literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

