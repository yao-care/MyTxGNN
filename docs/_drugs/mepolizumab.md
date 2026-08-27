---
layout: default
title: Mepolizumab
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 5
---

# Mepolizumab
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

# Mepolizumab: From Eosinophilic Diseases to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody used to treat eosinophilic conditions (severe eosinophilic asthma, EGPA, HES, CRSwNP, EoE). The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but this is currently supported by only **1 case report** and **no registered clinical trials**, and a Blocking data gap on TFDA/NPRA safety labeling means the candidate cannot yet enter formal safety review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic diseases (severe eosinophilic asthma, EGPA, HES, CRSwNP, EoE) — based on known drug-class information; Malaysia license text itself was not returned in this evidence pack |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as data gap DG002). Based on known information, mepolizumab is an anti-IL-5 monoclonal antibody that suppresses IL-5 signaling and reduces circulating/tissue eosinophil counts. Its approved indications are all eosinophil-driven diseases (severe eosinophilic asthma, EGPA, HES, CRSwNP, EoE), and its efficacy in those settings is well established.

The single supporting publication (PMID 28648630) describes a patient with steroid-resistant hypereosinophilic syndrome (HES) who developed a mixed thrombotic microangiopathy with immune-mediated blood cell destruction, which improved after mepolizumab controlled the underlying hypereosinophilia. This suggests the thrombocytopenia in that case was a **secondary consequence of eosinophil-driven tissue/marrow injury**, not a primary immune thrombocytopenia (ITP) process that mepolizumab directly targets. The TxGNN high score likely reflects an indirect knowledge-graph path (mepolizumab → HES → thrombocytopenia) rather than a validated direct mechanism against immune platelet destruction — the mechanistic plausibility is present only in the narrow context of HES-associated cytopenia, not for ITP broadly.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | Steroid-resistant hypereosinophilic syndrome with a mixed thrombotic microangiopathy resolved after mepolizumab controlled eosinophil-driven complement/tissue injury, alongside improvement of associated blood cell destruction |

## Malaysia Market Information

Mepolizumab holds 2 registered marketing authorizations in Malaysia (NPRA status: Marketed). Details such as license numbers, product names, dosage forms, and approved indication text were not returned by the NPRA query underlying this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication rests on a single case report describing thrombocytopenia as a secondary consequence of HES-driven tissue injury, not a validated primary-ITP mechanism, with zero clinical trials registered. In addition, a Blocking data gap (DG001: TFDA/NPRA label warnings/contraindications not yet available) prevents this candidate from entering the S1 safety review stage regardless of efficacy evidence. Note also that four lower-ranked candidates for mepolizumab (autoimmune thrombocytopenic, primary platelet release disorder, pseudo-von Willebrand disease, Glanzmann thrombasthenia) show even weaker or no evidence at all, reinforcing that the TxGNN signal here is likely driven by proximity to the single HES-thrombocytopenia case rather than a broad, robust drug-disease relationship.

**To proceed, the following is needed:**
- TFDA/NPRA package insert with warnings, contraindications, and DDI data (resolves Blocking gap DG001)
- Confirmed DrugBank mechanism-of-action data (resolves DG002)
- Targeted case series or mechanistic studies evaluating mepolizumab specifically in immune thrombocytopenia, distinct from HES-associated secondary cytopenia
- Complete Malaysia license detail (product names, dosage forms, approved indication text) to confirm current label scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

