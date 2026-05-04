---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
---

# Benralizumab
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

# Benralizumab: From Severe Eosinophilic Asthma to Dermatitis

## One-Sentence Summary

Benralizumab is an anti-IL-5 receptor alpha (IL-5Rα) monoclonal antibody, originally approved for the add-on maintenance treatment of severe eosinophilic asthma. The TxGNN model predicts it may be effective for **Dermatitis** (ranked 2nd among 5 predicted indications), with **6 clinical trials** and **20 publications** available — however, the pivotal Phase 2 HILLIER trial demonstrated a **lack of clinical effect**, making this a cautionary example of model prediction contradicted by clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe eosinophilic asthma (add-on maintenance treatment) |
| Predicted New Indication | Dermatitis (Rank 2); Thrombocytopenia due to immune destruction (Rank 1) |
| TxGNN Prediction Score (Rank 1) | 99.34% (thrombocytopenia — no supporting evidence) |
| TxGNN Prediction Score (Rank 2) | 99.16% (dermatitis — negative Phase 2 RCT) |
| Evidence Level | **L2** (dermatitis: 1 completed Phase 2 RCT); **L5** (all other indications) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** — Primary Phase 2 RCT produced definitive negative results |

---

## All Predicted Indications Overview

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|---------------|---------------|
| 1 | Thrombocytopenia due to immune destruction | 99.34% | L5 | Hold |
| 2 | Dermatitis | 99.16% | L2 | Hold (negative RCT) |
| 3 | Acne keloid | 99.13% | L5 | Hold |
| 4 | Neonatal dermatomyositis | 99.05% | L5 | Hold |
| 5 | Amyopathic dermatomyositis | 99.03% | L5 | Hold |

> **Note:** Among the 5 TxGNN predictions, only **dermatitis** (Rank 2) has any clinical or literature evidence. The remaining 4 predictions rely solely on the model with zero supporting studies. This report focuses on dermatitis as the most informative indication for evaluation.

---

## Why is This Prediction Reasonable?

Benralizumab is a humanised anti-IL-5Rα monoclonal antibody that depletes eosinophils and basophils through antibody-dependent cell-mediated cytotoxicity (ADCC). It was originally developed and approved for severe eosinophilic asthma, where eosinophil-driven inflammation plays a central pathogenic role. The TxGNN model assigned high scores to multiple immune-mediated conditions, likely reflecting the graph proximity between eosinophil-related disease nodes in the knowledge graph.

For **dermatitis** (specifically atopic dermatitis, AD), the mechanistic rationale is moderate but ultimately insufficient. Eosinophils are indeed present in AD skin lesions, and benralizumab has been shown to effectively deplete IL-5Rα-bearing cells in the skin of AD patients (PMID 40781582). However, the core driver of AD is the Th2-polarised IL-4/IL-13 axis, which leads to epidermal barrier disruption and the itch-scratch cycle. Eosinophil depletion alone does not interrupt this central pathogenic loop — a conclusion confirmed by the HILLIER trial's negative results.

For **thrombocytopenia due to immune destruction** (Rank 1, highest TxGNN score), the mechanistic link is weak. ITP is driven by anti-platelet autoantibodies (anti-GPIIb/IIIa, anti-GPIb/IX) and T-cell-mediated platelet destruction. Eosinophils are not key players in ITP pathogenesis. The high TxGNN score likely reflects proximity of immune disease nodes in the knowledge graph rather than genuine therapeutic potential. The remaining predictions (acne keloid, neonatal dermatomyositis, amyopathic dermatomyositis) share similarly weak mechanistic rationales — the pathogenic drivers (fibroblast activation/TGF-β for keloids; type I interferon/complement for dermatomyositis) are unrelated to eosinophil biology.

---

## Clinical Trial Evidence (Dermatitis)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | **Terminated** | 194 | **HILLIER Study**: Multinational, randomised, double-blind, placebo-controlled trial in moderate-to-severe AD. **Terminated due to lack of efficacy.** Published results (PMID 37178404) explicitly report "Lack of effect" of benralizumab on signs and symptoms of AD. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Mechanistic study: Benralizumab successfully depleted IL-5Rα-bearing cells (eosinophils, basophils, ILC2s) in AD skin lesions, but this biological effect **did not translate into clinical improvement**. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not yet recruiting | 96 | Targets DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms), a distinct entity from typical AD. Eosinophils play a more prominent role in DRESS. Worth monitoring but not directly applicable to AD. |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Phase 2 | Recruiting | 30 | Studies **dupilumab** (not benralizumab) as add-on for HES. Indirect relevance only. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A | Completed | 28 | Observational retrospective study of benralizumab in severe eosinophilic asthma patients in Spain. Not designed for dermatitis evaluation. |
| [NCT04763447](https://clinicaltrials.gov/study/NCT04763447) | Phase 4 | Recruiting | 234 | Studies **omalizumab** withdrawal in asthma. No direct relevance to benralizumab or dermatitis. |

> ⚠️ **Critical finding:** The only two directly relevant trials (HILLIER and NCT03563066) both demonstrate that while benralizumab achieves its biological target (eosinophil depletion in skin), this does **not** result in clinical benefit for atopic dermatitis.

---

## Clinical Trial Evidence (Other Predicted Indications)

Currently no related clinical trials registered for:
- Thrombocytopenia due to immune destruction
- Acne keloid
- Neonatal dermatomyositis
- Amyopathic dermatomyositis

---

## Literature Evidence (Dermatitis)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | **Phase 2 RCT** | JEADV | **HILLIER trial results: "Lack of effect of benralizumab on signs and symptoms of moderate-to-severe atopic dermatitis."** Definitive negative evidence. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Phase 2 RCT (secondary) | Immunotherapy | Plain language summary of HILLIER trial, confirming benralizumab did not improve AD outcomes. |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Translational study | Clin Transl Allergy | Benralizumab depletes IL-5Rα-bearing cells in AD skin lesions, but biological effect does not correlate with clinical improvement. |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | Translational study | JACI Global | Evaluated effect of benralizumab on skin inflammation after intradermal allergen challenge in AD patients. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie select | Comprehensive update on biologics for atopic diseases; contextualises benralizumab among other IL-5-targeting agents. |
| [37201737](https://pubmed.ncbi.nlm.nih.gov/37201737/) | 2023 | Basic science review | Pharmacol Ther | Reviews pathogenic Th2 cells as therapeutic targets; explains why IL-4/IL-13 blockade (not IL-5Rα) is the effective pathway for AD. |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | Review | Dermatol Ther | Discusses combination of dupilumab with other biologics; benralizumab mentioned in context of atopic comorbidities. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Case report (AE) | Therapie | **Adverse event report**: Benralizumab-induced interstitial granulomatous dermatitis — a paradoxical skin reaction. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Safety review | JACI In Practice | Safety of biologics (including benralizumab) for atopic diseases during pregnancy. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Safety review | Immunol Allergy Clin N Am | Biologics for allergic rhinitis, asthma, and AD during pregnancy and lactation. |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Registration details pending) | Benralizumab | — | Severe eosinophilic asthma |

> The NPRA registry confirms 1 active registration. Detailed licence information (product name, dosage form, full indication text) was not available in the evidence pack at the time of this report.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** Key warnings, contraindications, and drug interaction data were not available in the current evidence pack (Data Gap DG001). To proceed to safety evaluation (Stage S1), the package insert PDF should be obtained from the NPRA website and parsed for warnings, contraindications, and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite high TxGNN prediction scores (>99%) across all 5 predicted indications, the clinical evidence directly contradicts the most evidence-supported prediction. The HILLIER trial (Phase 2, n=194, randomised, double-blind, placebo-controlled) definitively showed **lack of effect** of benralizumab in moderate-to-severe atopic dermatitis. Translational studies confirmed that while benralizumab achieves its biological target (eosinophil depletion in skin), this does not translate into clinical improvement — demonstrating that eosinophils are not the rate-limiting pathogenic factor in AD. The remaining 4 predictions (thrombocytopenia, acne keloid, neonatal/amyopathic dermatomyositis) have zero supporting evidence and weak mechanistic rationale.

**This case serves as an important validation example:** a high TxGNN graph-proximity score does not guarantee therapeutic efficacy. The model likely assigned high scores based on the clustering of immune-mediated disease nodes, rather than capturing the specific mechanistic requirements of each disease.

**To proceed, the following is needed:**
- ❌ **Dermatitis**: No further development warranted — definitive negative Phase 2 evidence
- ⏸️ **Thrombocytopenia (ITP)**: Requires preclinical evidence of eosinophil involvement in ITP pathogenesis before any clinical exploration can be justified
- ⏸️ **Acne keloid / Dermatomyositis**: Requires basic science establishing eosinophil/IL-5Rα role in pathogenesis
- 📋 **General**: Obtain NPRA package insert for complete safety profile (Data Gap DG001); obtain detailed MOA data from DrugBank (Data Gap DG002)
- 👁️ **Monitor**: NCT06734884 (benralizumab in DRESS) — if positive, may reopen discussion for eosinophil-driven dermatological conditions distinct from AD
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

