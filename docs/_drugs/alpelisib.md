---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Alpelisib: From Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (Piqray) is a selective PI3Kα inhibitor originally approved for PIK3CA-mutated HR+/HER2− advanced breast cancer treatment.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, scoring 99.03% confidence;
however, the current evidence base consists of **1 peripherally related observational study** and **2 publications** — neither of which directly supports this repurposing direction, and significant mechanistic safety concerns are present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | PIK3CA-mutated HR+/HER2− advanced breast cancer |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Alpelisib is a highly selective oral inhibitor of PI3Kα (phosphoinositide 3-kinase alpha), a lipid kinase that sits at the hub of the PI3K/AKT/mTOR signalling cascade. In breast cancer, PIK3CA-activating mutations drive tumour proliferation; alpelisib blocks this pathway to suppress cancer cell growth. The theoretical bridge to pulmonary hypertension (PH) lies in the same PI3K/AKT/mTOR axis: dysregulated PI3Kα signalling is implicated in the pathological proliferation and migration of pulmonary artery smooth muscle cells (PASMCs) — the cellular hallmark of vascular remodelling in PH. In this sense, the mechanistic hypothesis has a logical foundation.

However, the same PI3Kα pathway is essential for maintaining normal cardiac function, particularly right ventricular (RV) mass and contractility. A 2019 preclinical study demonstrated that pharmacological PI3Kα inhibition combined with doxorubicin produced biventricular atrophy and RV dysfunction in animal models — a potentially catastrophic outcome in PH patients, whose disease is already defined by RV failure. Furthermore, alpelisib carries a known risk of inducing interstitial lung disease (ILD), which could directly worsen pulmonary vascular pathology.

In summary, while the mechanistic hypothesis is intellectually coherent, the on-target cardiovascular and pulmonary toxicities of alpelisib pose risks that are disproportionate to the speculative benefit in this indication. The TxGNN model's high prediction score reflects pathway proximity, not clinical safety or efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Real-world retrospective cohort of HR+/HER2− advanced/metastatic breast cancer patients treated with ribociclib or alpelisib (Jan 2018–Sep 2021); primary endpoints were oncological outcomes. **Not designed to evaluate pulmonary hypertension.** Any PH-relevant data would be limited to passively captured pulmonary adverse event signals only. |

> **Note:** No clinical trials directly investigating alpelisib for pulmonary hypertension were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | *J Oncol Pharm Pract* | Single patient case of alpelisib-induced interstitial lung disease (ILD) in advanced breast cancer. Highlights pulmonary toxicity as a known adverse event — directly relevant as a **safety signal** that could worsen PH pathology, rather than as therapeutic evidence. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical Study | *J Am Heart Assoc* | Animal/in vitro study demonstrating that PI3Kα pathway inhibition combined with doxorubicin causes biventricular atrophy and **right ventricular dysfunction**. Mechanistically argues *against* alpelisib use in PH patients who are already at high risk of RV failure. |

---

## Malaysia Market Information

Three registrations for alpelisib have been confirmed with the Malaysian National Pharmaceutical Regulatory Agency (NPRA). Detailed authorisation numbers, product names, dosage forms, and approved indication texts were not available in the current data pack.

> To obtain full registration details, please query the NPRA Product Registration database directly at: [https://www.npra.gov.my](https://www.npra.gov.my)

---

## Cytotoxicity

Alpelisib is classified as an antineoplastic targeted therapy (PIK3CA inhibitor) used in cancer treatment.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kα inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate (neutropenia may occur, but not a primary toxicity profile; hyperglycaemia and severe cutaneous reactions are more characteristic) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Fasting plasma glucose and HbA1c (hyperglycaemia is a class-defining toxicity), CBC with differential, liver and renal function, pulmonary function / chest imaging if respiratory symptoms develop |
| Handling Protection | Should follow institutional cytotoxic drug handling protocols; oral formulation requires appropriate dispensing precautions |

---

## Safety Considerations

Detailed warnings and contraindications from the Malaysian approved prescribing information were not available in the current evidence pack.

The available literature highlights two specific safety signals directly relevant to pulmonary hypertension repurposing:

- **Pulmonary toxicity**: Alpelisib-induced ILD has been reported (PMID 35730191). In PH patients with already-compromised pulmonary vasculature, drug-induced pneumonitis may be life-threatening.
- **Cardiovascular toxicity**: Preclinical evidence indicates PI3Kα inhibition can cause biventricular atrophy and RV dysfunction (PMID 31039672). PH patients with compensated RV failure represent a particularly vulnerable population.

> For complete safety information including all warnings, contraindications, and drug interactions, please refer to the approved Malaysian package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for alpelisib in pulmonary hypertension is limited to model prediction only (L5), with no clinical trials or human studies directly addressing this indication. More critically, two key mechanistic safety signals — drug-induced ILD and PI3Kα-dependent right ventricular atrophy — indicate that alpelisib could *worsen* the primary disease pathology in PH patients, making the risk-benefit profile unfavourable at this stage.

**To revisit this decision, the following would be needed:**

- **Preclinical PH-specific data**: In vitro studies in human PASMCs and in vivo PH animal models (e.g., MCT or SU5416/hypoxia rat models) using clinically relevant alpelisib concentrations, with rigorous RV function monitoring
- **MOA clarification**: Quantitative comparison of PI3Kα inhibition concentrations required for PASMC anti-proliferative effect vs. concentrations associated with cardiomyocyte atrophy, to determine whether a therapeutic window exists
- **Full safety data retrieval**: Download and parse the NPRA-approved package insert to obtain complete warnings and contraindications (Data Gap DG001)
- **DrugBank MOA data**: Retrieve structured mechanism and target data to enable systematic pathway analysis (Data Gap DG002)
- **Expert consultation**: Pulmonary hypertension specialist and clinical pharmacologist review of the preclinical cardiac safety data before any human study design is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

