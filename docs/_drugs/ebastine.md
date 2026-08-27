---
layout: default
title: Ebastine
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 2
---

# Ebastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ebastine: From Unspecified Original Indication to Coronary Artery Disease

## One-Sentence Summary

Ebastine (DrugBank ID: DB11742) is currently marketed in Malaysia, though its originally approved indication is not available in the current evidence pack. The TxGNN model predicts potential relevance to **Coronary Artery Disease** (and, secondarily, myocardial ischemia), but this prediction is supported only by **0 clinical trials** and **1 tangentially related publication**, which does not study ebastine itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current records — TFDA/NPRA label text has not yet been retrieved (data gap, see below) |
| Predicted New Indication | Coronary Artery Disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for ebastine itself is not currently available in the evidence pack. Based on the repurposing rationale that is available, ebastine is metabolized primarily by **CYP2J2** (and CYP3A4) into its active metabolite, carebastine. CYP2J2 is highly expressed in cardiac tissue and physiologically converts arachidonic acid into epoxyeicosatrienoic acids (EETs), which have vasodilatory, anti-inflammatory, and cardioprotective properties — a pathway that is mechanistically related to coronary artery disease and, by extension, myocardial ischemia (the second predicted indication in this evidence pack, ranked #2 with a score of 99.10%).

However, this link is **indirect and associative**: the single literature reference supporting the prediction (PMID 18004755) is a structural homology-modeling and molecular dynamics study of the CYP2J2 enzyme itself. It does not investigate ebastine's pharmacological effects, nor does it report any cardiovascular outcome data for ebastine specifically. The connection here is limited to "ebastine and coronary artery disease share a metabolizing enzyme" — there is no ebastine-specific pharmacological, animal-model, or clinical evidence of a cardioprotective or disease-modifying effect.

Given the absence of any drug-specific pharmacology or clinical data, this should be regarded as a knowledge-graph-derived hypothesis based on entity co-occurrence (shared enzyme pathway), rather than a mechanistically validated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | Review | Proteins | Homology modeling and molecular dynamics study of CYP2J2, the enzyme that metabolizes ebastine into carebastine; CYP2J2's EET pathway is noted to relate to coronary artery disease, hypertension, and carcinogenesis. Does not study ebastine directly. |

*Note: The same publication is the sole evidence source for the secondary prediction, myocardial ischemia (rank 2, score 99.10%), via the identical CYP2J2 mechanistic argument.*

---

## Malaysia Market Information

NPRA records confirm **2 active marketing authorizations** for ebastine in Malaysia (market status: Marketed). However, detailed registration information — authorization numbers, product names, dosage forms, manufacturers, and approved indication text — is not yet available in the current data extract.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Retrieval of the TFDA/NPRA label warnings and contraindications is flagged as a **blocking data gap** (DG001) — this information must be obtained before any formal safety (S1) evaluation can proceed. Drug interaction data was queried but not found.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by Evidence Level L5 (model prediction only) — there are no clinical trials, and the single available publication does not study ebastine's effect on cardiovascular disease at all, only a shared metabolic enzyme. Combined with a blocking data gap in safety labeling (warnings/contraindications) and a missing MOA profile, this candidate cannot currently advance beyond the initial screening stage (S0).

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (resolve DG001 — required to enter S1 safety evaluation)
- Confirmed mechanism of action and original approved indication for ebastine (resolve DG002)
- Ebastine-specific pharmacology or preclinical data on cardiovascular/coronary effects (not merely shared-enzyme inference)
- Any real-world or observational data on cardiovascular outcomes in ebastine users, if available
- Complete Malaysia registration details (product names, dosage forms, approved indication text) for the 2 existing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

