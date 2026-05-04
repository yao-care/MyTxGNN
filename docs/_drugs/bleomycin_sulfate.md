---
layout: default
title: Bleomycin Sulfate
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 0
---

# Bleomycin Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Bleomycin Sulfate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bleomycin Sulfate is a marketed antineoplastic glycopeptide antibiotic historically used in the treatment of various malignancies including lymphomas, squamous cell carcinomas, and testicular cancer. The TxGNN model **has not yet generated predicted new indications** for this drug, and the Evidence Pack currently contains significant data gaps in regulatory details, safety information, and mechanism of action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (known use: lymphomas, squamous cell carcinomas, testicular cancer) |
| Predicted New Indication | **None — no TxGNN predictions available** |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No model predictions or supporting studies in this dataset) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN predictions have been generated for Bleomycin Sulfate. The `predicted_indications` field is empty, meaning the knowledge graph and deep learning models have not yet returned candidate indications for repurposing evaluation.

Bleomycin Sulfate is a well-established cytotoxic antibiotic that exerts its antineoplastic effect by binding to DNA and inducing single- and double-strand breaks via an iron-dependent free radical mechanism. Its clinical use spans Hodgkin lymphoma (as part of the ABVD regimen), squamous cell carcinomas of the head and neck, cervix, and vulva, testicular germ cell tumours, and malignant pleural effusions (as a sclerosing agent). Detailed mechanism of action data was not included in the current Evidence Pack and is flagged as a high-severity data gap (DG002).

Before meaningful repurposing predictions can be generated, the following prerequisite data must be populated: DrugBank ID mapping, approved indication text from regulatory licenses, and mechanism of action details. Without these inputs, the TxGNN model cannot produce reliable candidate indications.

---

## Clinical Trial Evidence

Currently no TxGNN-linked clinical trials available, as no predicted indications have been generated.

---

## Literature Evidence

Currently no TxGNN-linked literature available, as no predicted indications have been generated.

---

## Malaysia Market Information

Bleomycin Sulfate has **2 registered licenses** with a market status of "Marketed" (已上市). However, the detailed registration information (authorization numbers, product names, dosage forms, and approved indication text) is not available in the current dataset.

> **Note:** License details need to be retrieved from the NPRA database to complete this section.

---

## Cytotoxicity

Bleomycin Sulfate is a conventional cytotoxic antineoplastic agent. The following information is based on established pharmacological knowledge:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Glycopeptide antibiotic / DNA-damaging agent) |
| Myelosuppression Risk | **Low** (Bleomycin is notably mild on bone marrow compared to other cytotoxics; myelosuppression is uncommon) |
| Emetogenicity Classification | **Low** |
| Monitoring Items | **Pulmonary function tests** (DLCO, CXR — pulmonary toxicity is dose-limiting); renal function (creatinine clearance, as renal impairment increases pulmonary toxicity risk); CBC; liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations (closed-system transfer, PPE, biological safety cabinet) |

> ⚠️ **Critical Safety Note:** Bleomycin carries a well-known risk of **pulmonary fibrosis**, which is cumulative and dose-dependent (typically at cumulative doses >400 units). Pulmonary function must be monitored throughout treatment. Please refer to the package insert for full warnings and precautions.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug-drug interactions) was not available in the current Evidence Pack. These are flagged as a blocking data gap (DG001).

> Please refer to the package insert for safety information. As a priority, the TFDA package insert PDF should be retrieved and parsed to populate warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions have been generated for Bleomycin Sulfate, and the Evidence Pack contains critical data gaps (DrugBank ID, approved indication text, MOA, safety warnings). There is insufficient data to evaluate any repurposing opportunity at this time.

**To proceed, the following is needed:**

1. **DrugBank ID mapping** — Query DrugBank API for Bleomycin Sulfate (expected: [DB00290](https://go.drugbank.com/drugs/DB00290)) and populate `drugbank_id`
2. **Regulatory license details** — Retrieve full registration information from NPRA (authorization numbers, product names, dosage forms, approved indications)
3. **Mechanism of action (MOA)** — Retrieve from DrugBank to enable mechanistic plausibility analysis (DG002)
4. **Package insert safety data** — Download and parse TFDA package insert PDF to extract warnings and contraindications (DG001, Blocking)
5. **Re-run TxGNN prediction pipeline** — Once DrugBank ID and indication mappings are populated, execute `run_kg_prediction.py` to generate repurposing candidates
6. **Evidence collection** — After predictions are available, run ClinicalTrials.gov and PubMed collectors to gather supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

