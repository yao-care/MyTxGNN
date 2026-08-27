---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 3
---

# Clonazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clonazepam: Toward a New Indication in Restless Legs Syndrome

> Original approved indication text is not available in this evidence pack (TFDA/NPRA license records exist but indication fields were not captured), so the title follows a "toward new indication" format rather than the standard "From X to Y."

## One-Sentence Summary

Clonazepam is a marketed benzodiazepine (4 registrations, currently on the market) whose original approved indication is not captured in this dataset. The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**, with a prediction score of **99.65%**, but this evidence pack currently contains **no clinical trials and no literature** specifically supporting this repurposing — the rationale rests on known drug-class pharmacology and existing off-label clinical practice rather than dataset-verified studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (data gap) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 (mechanism/known clinical practice, no dataset-verified trials or literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for clonazepam is flagged as a data gap in this evidence pack. However, the model's own repurposing rationale identifies clonazepam as a **GABA-A receptor positive allosteric modulator** (benzodiazepine class), which suppresses excessive excitability in sensorimotor circuits.

Benzodiazepines — clonazepam in particular — are already listed in several RLS treatment guidelines as a second/third-line adjunct, typically reserved for patients with an inadequate response to dopaminergic therapy or with prominent sleep disruption. This is existing off-label clinical practice rather than a novel mechanistic hypothesis, which is consistent with the model's very high prediction score (99.65%).

That said, this evidence pack contains **zero clinical trials and zero publications** specifically linking clonazepam to RLS (all ClinicalTrials.gov, ICTRP, and PubMed queries returned 0 results). The prediction should therefore be read as "consistent with known pharmacology and existing off-label use," not as newly discovered or dataset-confirmed evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Clonazepam is marketed in Malaysia with **4 active registrations**, but the license-level fields (registration number, product name, dosage form, approved indication text) were not populated in this evidence pack, so a per-product table cannot be produced without fabricating data.

---

## Safety Considerations

Please refer to the package insert for safety information.

**⚠ Note:** Package insert warnings/contraindications (DG001) are flagged as a **Blocking** data gap in this evidence pack — this specifically prevents the case from entering the S1 safety pre-assessment stage. This gap must be closed before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The RLS prediction is biologically plausible and aligned with known off-label clinical use, but is supported only by mechanistic reasoning — no clinical trials or literature in this dataset confirm it, and TFDA/NPRA package insert safety data (warnings, contraindications) is missing and blocking (DG001), so no safety pre-assessment (S1) can currently be completed.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA package insert PDF and extract warnings/contraindications (resolves DG001, blocking)
- Query DrugBank for confirmed mechanism-of-action data (resolves DG002)
- Populate license-level fields (registration numbers, approved indication text, dosage forms) for the 4 Malaysia registrations
- Targeted literature/trial search using RLS-specific synonyms (e.g., "Willis-Ekbom disease") in case standard terms undercount existing evidence
- **QA note:** A third predicted indication in this pack, *trigeminal nerve neoplasm* (rank 3, score 99.30%), is flagged by the rationale itself as a likely knowledge-graph embedding confusion with *trigeminal neuralgia* — recommend manual KG mapping review before this candidate is used for any downstream decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

