---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Merkel Cell Carcinoma to Human Herpesvirus 8-Related Tumor

---

## One-Sentence Summary

Avelumab is a fully human anti-PD-L1 monoclonal antibody (immune checkpoint inhibitor), approved for Merkel cell carcinoma and as first-line maintenance therapy for locally advanced or metastatic urothelial carcinoma following platinum-based chemotherapy.
The TxGNN model predicts it may be effective for **Human Herpesvirus 8-Related Tumor**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Merkel Cell Carcinoma / Urothelial Carcinoma (referenced in prediction rationale; licence record fields unpopulated) |
| Predicted New Indication | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Avelumab is a fully human IgG1 anti-PD-L1 monoclonal antibody that blocks the PD-1/PD-L1 immune checkpoint interaction, thereby restoring T cell-mediated anti-tumour surveillance. Its proven clinical efficacy in Merkel cell carcinoma (MCC) and urothelial carcinoma (UC) — both PD-L1-expressing malignancies — establishes the immunological framework from which the TxGNN knowledge graph extrapolates.

Human herpesvirus 8 (HHV-8) is the causative oncovirus behind Kaposi sarcoma and primary effusion lymphoma. Viral oncoproteins (e.g., vFLIP, K1) may transcriptionally upregulate PD-L1 on tumour cells, creating an immune-evasive microenvironment that PD-L1 blockade could theoretically reverse. At the class level, Pembrolizumab (another PD-1/PD-L1 inhibitor) has been explored in Phase 2 trials for Kaposi sarcoma, providing indirect precedent that this checkpoint axis is biologically relevant in HHV-8 tumours.

However, no specific clinical or preclinical data exists for Avelumab in HHV-8-related tumours. The high TxGNN score (99.97%, model rank #736) most likely reflects knowledge graph node clustering between "PD-L1 inhibitor" and "virally-driven tumour with immune evasion", rather than direct experimental evidence. Without supporting data, this prediction cannot be responsibly extrapolated from Avelumab's approved indications at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | — |

> The Evidence Pack records 1 active licence and market status as "Marketed", but all licence detail fields (authorization number, product name, dosage form, approved indication) were not populated in this data extract. Please verify complete registration details directly via the **National Pharmaceutical Regulatory Agency (NPRA) Malaysia** database.

---

## All Predicted Indications — Summary

This is a multi-indication candidate pack (TW-DB11945-multi). The following table summarises all 10 TxGNN predictions and their current evidence status:

| Rank | Disease | TxGNN Score | KG Rank | Evidence Level | Recommendation |
|------|---------|------------|---------|----------------|----------------|
| 1 | Human Herpesvirus 8-Related Tumor | 99.97% | #736 | L5 | Hold |
| 2 | Middle Ear Neuroendocrine Tumor | 99.97% | #742 | L5 | Hold |
| 3 | Malignant Cutaneous Granular Cell Skin Tumor | 99.97% | #810 | L5 | Hold |
| 4 | Ectomesenchymoma | 99.97% | #829 | L5 | Hold |
| 5 | Adenosine Deaminase Deficiency | 99.95% | #1143 | L5 | Hold |
| 6 | Reticular Dysgenesis | 99.94% | #1241 | L5 | Hold |
| 7 | Immunoerythromyeloid Hypoplasia | 99.94% | #1291 | L5 | Hold |
| 8 | Non-Severe Combined Immunodeficiency | 99.92% | #1717 | L5 | Hold |
| 9 | Prostatic Urethra Urothelial Carcinoma | 99.92% | #1745 | L4 | Research Question |
| 10 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.91% | #1765 | L4 | Research Question |

**Key observations across the prediction set:**

- **Ranks 1–4 (oncology):** All involve rare tumours (HHV-8, middle ear NET, malignant granular cell tumour, ectomesenchymoma) with plausible but unsubstantiated PD-L1 rationale. Zero supporting evidence found.
- **Ranks 5–8 (non-malignant immune deficiency):** ADA deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, and non-SCID are non-neoplastic conditions. PD-L1 inhibition lacks any mechanistic target in these diseases, and application could carry safety risks. These predictions likely reflect systematic over-clustering of immune-pathway nodes in the KG model.
- **Ranks 9–10 (urothelial carcinoma subtypes — strongest biological rationale):** Both are histological subtypes of urothelial carcinoma (UC), directly connected to Avelumab's JAVELIN Bladder 100-approved indication. Rank 10 additionally has 1 observational study (NCT05431777, N=79, completed) evaluating Avelumab in Japanese UC patients, providing initial real-world data. These two candidates merit prioritised follow-up.

---

**Supporting Trial for Rank 10:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05431777](https://clinicaltrials.gov/study/NCT05431777) | N/A (Observational) | Completed | 79 | Retrospective multicentre study evaluating treatment patterns, safety, and outcomes of first-line Avelumab maintenance in Japanese patients with locally advanced or metastatic urothelial carcinoma. Provides descriptive real-world data; not a controlled efficacy trial for the sarcomatoid subtype specifically. |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — PD-L1 Immune Checkpoint Inhibitor (non-cytotoxic monoclonal antibody) |
| Myelosuppression Risk | Low (direct bone marrow suppression is not a primary mechanism; immune-related haematological events such as immune thrombocytopenia are possible but uncommon) |
| Emetogenicity Classification | Minimal (intravenous antibody infusion; emetogenicity not a primary concern) |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST/bilirubin), thyroid function (TSH, free T4), renal function (creatinine), fasting glucose, cortisol — to detect immune-related adverse events (irAEs); infusion reaction monitoring during each administration |
| Handling Protection | Standard biologics handling procedures apply; dedicated cytotoxic containment facilities not required for this drug class |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings and contraindications were not populated in this Evidence Pack. The NPRA-registered package insert should be consulted for complete prescribing information. As a class-level note, PD-L1 inhibitors carry well-characterised risks of immune-related adverse events (irAEs), including immune-mediated pneumonitis, colitis, hepatitis, endocrinopathies (thyroiditis, adrenal insufficiency), nephritis, and infusion-related reactions. These class effects are relevant irrespective of the indication being evaluated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (HHV-8-related tumour) is supported exclusively by model-derived inference (L5 evidence), with zero clinical trials and zero publications identified. While a theoretical immunological mechanism can be constructed, proceeding without any corroborating preclinical or clinical data would constitute an evidence-free extrapolation that cannot be responsibly evaluated for repurposing at this stage.

**To proceed, the following is needed:**

- **Immediate data gaps:** Obtain and parse the NPRA/TFDA package insert to retrieve key warnings and contraindications (Data Gap DG001, Blocking severity)
- **Mechanism clarification:** Query DrugBank API to retrieve Avelumab's full mechanism of action and target profile (Data Gap DG002, High severity)
- **Evidence search for top prediction:** Conduct a targeted literature search (PubMed, Embase) for PD-L1 expression data and checkpoint inhibitor studies in HHV-8-related tumours (Kaposi sarcoma, primary effusion lymphoma), including Pembrolizumab Phase 2 data as class-level precedent
- **Reprioritisation consideration:** Given that Ranks 9–10 (urothelial carcinoma subtypes) share direct histological continuity with Avelumab's JAVELIN Bladder 100-approved indication and carry L4 evidence (Research Question), it is strongly recommended to rerun the primary analysis with **Prostatic Urethra Urothelial Carcinoma** or **Kidney Pelvis Sarcomatoid TCC** as the lead candidate indication
- **Populate Malaysia licence record:** Contact NPRA to retrieve the complete registration details for the 1 active licence on file
- **Exclude ranks 5–8 from further analysis:** The immune deficiency predictions (ADA deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, non-SCID) are mechanistically implausible for PD-L1 inhibition and should be flagged as likely KG false positives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

