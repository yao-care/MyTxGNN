---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

Using the report as directly requested (a data-synthesis/writing task, not a coding or research task requiring a skill) — proceeding to generate the evaluation report from the provided Evidence Pack.

A note before the report: the Evidence Pack itself flags severe data-quality problems in this batch (disease-label/literature mismatches in ranks 4, 5, 6, 8, 10, and zero evidence for the #1-ranked candidate). I've written the report honestly rather than presenting the top TxGNN score as if it were well-supported — that's what a repurposing expert's evaluation is supposed to protect the reader from.

---

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

> Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor; within this evidence pack's own literature it is repeatedly documented as the treatment for **ALK-positive non-small cell lung cancer (NSCLC)** (e.g., the CROWN trial series), though this is not yet reflected in the Malaysia regulatory record fields. The TxGNN model's top-ranked candidate is **Gingival Fibromatosis**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic assessment states there is no known biological link. This top-ranked signal should be treated as model noise, not a genuine repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) — inferred from literature evidence in this pack (see rank #4/#5 rationale); not present in the Malaysia regulatory license text, which is currently empty |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 (license-level detail fields are currently empty in the dataset) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on information embedded in this evidence pack's literature (not on the empty regulatory fields), Lorlatinib is a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor, with its approved use being ALK-positive NSCLC, supported by multiple Phase 3 RCTs (CROWN study and its updates).

Gingival fibromatosis is a benign, non-neoplastic overgrowth of gingival connective tissue, most commonly hereditary or drug-induced (e.g., by phenytoin, cyclosporine, calcium-channel blockers). It has no established relationship to ALK signaling or receptor tyrosine kinase biology. The evidence pack's own mechanistic assessment for this candidate is explicit: *"no clinical trial or literature evidence exists; gingival fibromatosis has no known mechanistic link to the ALK pathway — this is a pure TxGNN knowledge-graph embedding similarity artifact, lacking biological support."* There is no plausible pharmacological bridge between the original indication and this prediction, and no supporting data of any kind.

It is worth noting for the record that this candidate batch shows a broader, recurring pattern: several other TxGNN-ranked candidates (ranks #4, #5, #6, #8, #10) returned literature that, on inspection, describes a *different* disease than the one nominally being evaluated (e.g., rank #5 "lung benign neoplasm" returned 20 papers that are actually about malignant ALK+ NSCLC/CROWN trial data; rank #6 "lung germ cell tumor" returned papers that are actually about ALK-driven pediatric neuroblastoma, including a real Phase 1 trial, PMID 37012551; rank #8 and #10 returned literature entirely unrelated to the nominal disease, including one batch that was actually a set of Lorlatinib adverse-event case reports). This suggests a disease-ontology/label mapping issue somewhere upstream in the retrieval pipeline for this candidate set, and it means TxGNN score/rank alone cannot be used to judge evidence quality for this batch — each candidate's literature must be manually re-verified against its stated disease label before further action. Of that set, rank #6 (mislabeled candidate, real disease = ALK-driven neuroblastoma) is the only one with a genuine biological rationale and actual trial data, and is flagged separately below as worth re-evaluating under the correct disease label rather than being discarded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The dataset confirms Lorlatinib holds **2 active registrations** in Malaysia and a market status of **✓ Marketed**, but the license-level fields (authorization number, product name, dosage form, approved indication text) are all currently empty in this evidence pack and cannot be populated without fabrication.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *Not available in current dataset* | *Not available* | *Not available* | *Not available* |
| *Not available in current dataset* | *Not available* | *Not available* | *Not available* |

---

## Cytotoxicity

Lorlatinib is an antineoplastic agent (ALK/ROS1 tyrosine kinase inhibitor used in NSCLC treatment, per literature within this pack), so this section applies. No structured DrugBank toxicity data was returned for this query; the entries below are drawn from the adverse-event literature present in this evidence pack (PMIDs 38554546, 30890623, 40287137, 39537504, 33789526, 31985497) rather than from a formal toxicity monograph — this should be confirmed against the product insert once available.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — literature does not identify myelosuppression as a characteristic toxicity; dominant reported toxicities are metabolic and CNS-related |
| Emetogenicity Classification | Low (consistent with oral targeted kinase inhibitors generally) |
| Monitoring Items | Lipid panel (cholesterol, triglycerides — hyperlipidemia/dyslipidemia repeatedly reported), body weight, CNS/mood effects, renal function (rare nephrotic syndrome case reports), pulmonary symptoms (particularly if co-administered with anti-GD2 monoclonal antibody therapy, per PMID 40551396) |
| Handling Protection | Oral antineoplastic agent — handle per institutional hazardous/oral-chemotherapy handling policy; does not require infusional cytotoxic-drug preparation precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable in this dataset — DDI query returned no results, and this is flagged as a **Blocking** data gap (DG001) that prevents this candidate from proceeding to the S1 safety pre-screening stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Gingival Fibromatosis) has zero supporting clinical trials, zero literature, and no plausible mechanistic link to Lorlatinib's known ALK-inhibitory activity — the evidence pack itself characterizes it as knowledge-graph noise (L5).
- A Blocking data gap (missing product-insert warnings/contraindications, DG001) independently prevents this candidate from entering safety pre-evaluation regardless of efficacy evidence.

**To proceed, the following is needed:**
- Obtain the Malaysia (NPRA) product insert — warnings, contraindications, and full DDI profile (resolves Blocking gap DG001)
- Obtain structured DrugBank MOA and toxicity data (resolves High-severity gap DG002)
- Populate the missing Malaysia license-level fields (product name, dosage form, indication text) for the 2 existing registrations
- Before relying on this candidate batch's rankings at all, have the data pipeline re-verify the disease-label-to-literature mapping — at least 5 of the 10 ranked candidates in this batch returned literature describing a different disease than the one labeled
- Separately re-evaluate rank #6 under its correct underlying disease (ALK-driven pediatric neuroblastoma, not "lung germ cell tumor") — this is the only candidate in the batch with genuine mechanistic plausibility and real trial data (PMID 37012551), and merits its own S2 research-question workup rather than being folded into this noisy ranking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

