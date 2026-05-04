---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Alfuzosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor blocker primarily used for treating benign prostatic hyperplasia (BPH) by relaxing smooth muscle in the prostate and bladder neck.
The TxGNN model predicts it may have activity against **Ambras Type Hypertrichosis Universalis Congenita**, a rare genetic disorder causing excessive whole-body hair growth.
Currently, **0 clinical trials** and **0 publications** directly support this repurposing direction — this is a model-only prediction (Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) *(NPRA indication text not available in current data pack)* |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available in this evidence pack. Based on established pharmacology, alfuzosin is a selective alpha-1 adrenergic receptor antagonist that competitively blocks post-synaptic alpha-1 receptors in the smooth muscle of the prostate gland and bladder neck. This relaxation facilitates urine outflow, making it effective in BPH. Alpha-1 receptors are also expressed in hair follicle dermal papilla cells — this shared receptor biology represents the likely node connection that TxGNN exploited to generate this prediction.

However, a critical directional contradiction undermines the biological plausibility of this prediction. Hypertrichosis universalis congenita (Ambras type) is a condition of *excessive* hair growth, associated with mutations in the TRPS1 gene or chromosomal rearrangements at 8q22. If alpha-1 receptor activation were to stimulate hair growth, then *blocking* this receptor with alfuzosin would be expected to *suppress* hair growth — the opposite of a treatment for excessive hair growth. The mechanistic direction is therefore contradictory, not supportive.

A notable pattern emerges across the full top-10 prediction list: 6 of the 10 highest-ranked indications are hair or hair follicle-related conditions (Ambras hypertrichosis, hypertrichosis, isolated hair shaft abnormality, familial trichomegaly, hypotrichosis simplex, congenital hypotrichosis milia). This clustering strongly suggests a systematic knowledge-graph artefact — TxGNN appears to be over-representing the adrenergic–hair follicle node neighbourhood rather than capturing genuine therapeutic signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 3 prediction (periodontal syndrome):** The evidence pack includes 20 PubMed references retrieved against the search query for "malformation syndrome with odontal and/or periodontal component." These are all general periodontology publications (scaling/root planing, guideline documents, microbiome studies) with no connection to alfuzosin whatsoever. This is a confirmed false-positive match based on disease-name string overlap in the retrieval pipeline, not evidence of pharmacological relevance.

---

## Malaysia Market Information

Five drug registrations for alfuzosin are on record with the Malaysian National Pharmaceutical Regulatory Agency (NPRA), and the product is confirmed as **Marketed**. Individual registration details (authorization numbers, product names, dosage forms, and approved indication texts) were not returned in the current data pack.

For full registration details, please consult the NPRA product register directly: [https://www.npra.gov.my](https://www.npra.gov.my)

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** Detailed warnings, contraindications, and drug–drug interaction data were not available in this evidence pack (classified as Blocking data gap DG001). Retrieval and parsing of the full NPRA prescribing information PDF is required before any clinical or research use assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is extremely high (99.999%), but this reflects proximity within the knowledge graph's adrenergic receptor neighbourhood rather than any genuine therapeutic signal. The mechanistic direction is directly contradictory to treating the predicted condition, no supporting clinical or preclinical studies exist, and a systematic model bias toward hair follicle diseases is evident across the top-10 list.

**To proceed, the following is needed:**

- **Resolve Blocking Data Gap (DG001):** Download and parse the NPRA package insert PDF to obtain approved indications, warnings, and contraindications before any safety screening can begin
- **Resolve High Data Gap (DG002):** Query the DrugBank API for alfuzosin's complete MOA, pharmacodynamics, and toxicity profile
- **Retrieve NPRA registration details:** Obtain full product list (authorization numbers, dosage forms, approved indication texts) from the NPRA database
- **Investigate model artefact:** Assess whether TxGNN systematically over-predicts hair follicle diseases for all alpha-1 blocker class drugs — if confirmed, this cluster of predictions should be filtered at the pipeline level rather than evaluated individually
- **Mechanistic direction audit:** For any future re-evaluation of alfuzosin candidates, prioritise indications where alpha-1 *blockade* (vasodilation, smooth muscle relaxation) has a logically consistent therapeutic direction — such as **Rank 8: Persistent Fetal Circulation Syndrome (PPHN)**, where pulmonary vascular smooth muscle relaxation is the desired effect, although neonatal safety data remain absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

