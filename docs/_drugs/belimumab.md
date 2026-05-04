---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 6
---

# Belimumab
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a monoclonal antibody targeting BLyS (B-lymphocyte stimulator), originally approved for the treatment of systemic lupus erythematosus (SLE) and lupus nephritis. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but currently there are **no directly relevant clinical trials** and **no publications** supporting this specific repurposing direction. The mechanistic rationale is extremely weak, as platelet release disorders are structural/genetic defects unrelated to B-cell biology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus (SLE) (licence detail pending) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Belimumab (marketed as Benlysta by GSK) is a fully human IgG1λ monoclonal antibody that inhibits B-lymphocyte stimulator (BLyS, also known as BAFF). By blocking the binding of soluble BLyS to its receptors on B cells, belimumab reduces B-cell survival, differentiation into immunoglobulin-producing plasma cells, and ultimately decreases autoantibody production. This mechanism has proven clinically effective in systemic lupus erythematosus (SLE) and lupus nephritis, where pathogenic autoantibodies drive disease.

Primary release disorder of platelets (e.g., δ-storage pool deficiency) is a group of inherited conditions characterised by defective granule secretion from platelets during activation. These disorders arise from structural or genetic defects in platelet dense granules or alpha granules — a fundamentally different pathological mechanism from autoantibody-mediated disease. B-cell inhibition via BLyS blockade does not address the intrinsic platelet granule secretion machinery.

The only conceivable indirect link is that SLE patients can sometimes exhibit concomitant platelet dysfunction, but this represents co-morbidity rather than a causal relationship. The TxGNN model's high prediction score likely reflects topological proximity in the knowledge graph between belimumab's immunological neighbourhood and haematological nodes, rather than a genuine mechanistic pathway. **This prediction is not considered scientifically reasonable based on current understanding.**

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Belimumab in idiopathic membranous glomerulonephropathy (anti-PLA2R antibody positive). **Relevance Grade: C** — this trial investigates an autoimmune kidney disease, not platelet release disorders. Likely a data mapping error. |

> **Note:** The single trial retrieved is not relevant to the predicted indication. It examines belimumab in membranous nephropathy, an entirely different disease entity. Effectively, there are **no clinical trials** investigating belimumab for platelet release disorders.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Detail pending) | (Detail pending) | (Detail pending) | (Detail pending) |

> **Note:** Belimumab has 1 registered product in Malaysia with marketed status. Detailed licence information (product name, dosage form, approved indication text) was not available in the current data extract and requires supplementation from the NPRA database.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

## Additional Predicted Indications Overview

Since all 6 TxGNN-predicted indications share the same evidence level (L5) and predominantly "Hold" recommendations, the following summary table is provided for completeness:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Link | Evidence Level | Recommendation |
|------|---------------------|-------------|-----------------|----------------|----------------|
| 1 | Primary release disorder of platelets | 99.96% | Extremely weak | L5 | Hold |
| 2 | Pseudo-von Willebrand disease | 99.96% | None (GP1BA gene mutation) | L5 | Hold |
| 3 | Glanzmann thrombasthenia | 99.88% | Extremely weak (only via alloimmunization) | L5 | Hold |
| 4 | Fetal & neonatal alloimmune thrombocytopenia | 99.59% | Moderate (antibody-mediated, theoretical) | L5 | Research Question |
| 5 | Severe nonproliferative diabetic retinopathy | 99.05% | Extremely weak | L5 | Hold |
| 6 | Autosomal dominant macrothrombocytopenia | 99.04% | None (genetic megakaryocyte defect) | L5 | Hold |

> **Notable exception — Rank 4 (FNAIT):** Fetal and neonatal alloimmune thrombocytopenia is the only predicted indication with a plausible mechanistic rationale. FNAIT is driven by maternal IgG alloantibodies against fetal platelet antigens (typically HPA-1a), and BLyS inhibition could theoretically reduce alloantibody production. However, belimumab's safety in pregnancy is not established (animal studies suggest reduced neonatal B-cell counts), and the timing of intervention would be extremely challenging. This warrants further literature review as a **Research Question** only.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predicted indications lack clinical trial evidence and published literature directly supporting belimumab's use. Five of six predictions target genetic/structural platelet disorders where B-cell inhibition has no mechanistic basis. The TxGNN prediction scores are high but reflect graph topology rather than validated biology. Without any empirical evidence, these candidates cannot advance.

**To proceed, the following is needed:**
- **Mechanism of action data (MOA):** Retrieve detailed pharmacodynamic data from DrugBank to formally document BLyS inhibition pathway
- **Malaysia licence details:** Obtain complete registration information (authorization number, product name, dosage form, approved indication) from NPRA
- **Package insert safety data:** Download and parse the product insert for key warnings, contraindications, and drug interactions (currently a blocking data gap for S1 safety evaluation)
- **For FNAIT (Rank 4) only:** Conduct a targeted literature review on anti-BAFF therapy in alloimmune settings and belimumab pregnancy safety data before deciding whether to elevate to a formal research proposal
- **Re-evaluation:** Consider whether the TxGNN model's clustering of platelet-related predictions for an anti-BLyS antibody represents a systematic bias in the knowledge graph that should be investigated

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

