---
layout: default
title: Blinatumomab
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 0
---

# Blinatumomab
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

# BLINATUMOMAB: Drug Repurposing Evaluation Report

## One-Sentence Summary

Blinatumomab (DB09052) is a bispecific T-cell engager (BiTE) antibody approved for the treatment of B-cell precursor acute lymphoblastic leukaemia (ALL). The current Evidence Pack contains **no TxGNN predicted indications**, and critical data gaps exist in mechanism of action, safety warnings, and licence details, preventing a meaningful repurposing evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | *(Data not provided in evidence pack — known: B-cell precursor ALL)* |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions, no supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, blinatumomab is a bispecific CD19-directed CD3 T-cell engager — it simultaneously binds CD19 on B-lineage cells and CD3 on T cells, redirecting the patient's own T cells to lyse CD19-positive malignant B cells. Its efficacy in relapsed/refractory B-cell precursor acute lymphoblastic leukaemia has been well established.

However, the TxGNN model has **not generated any predicted new indications** for blinatumomab in this evidence pack. This may be attributable to several factors: (1) blinatumomab is a large-molecule biologic with a highly specific mechanism that may not map well onto the knowledge graph used by TxGNN; (2) the drug–disease edges in the KG may be sparse for bispecific antibodies; or (3) the prediction pipeline may not have been executed for this drug.

Without a predicted indication, no mechanistic plausibility analysis can be performed. This report serves as a baseline documentation of the drug's regulatory status in Malaysia, pending completion of the prediction pipeline and resolution of data gaps.

---

## Clinical Trial Evidence

Currently no predicted indication is available, therefore no targeted clinical trial search was performed.

---

## Literature Evidence

Currently no predicted indication is available, therefore no targeted literature search was performed.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|-------------|-------------|---------------------|
| *(Not provided)* | *(Not provided)* | *(Not provided)* | *(Not provided)* |

> **Note:** One registration record exists in the NPRA database, but the licence details (authorization number, product name, dosage form, and approved indication text) were not populated in the evidence pack. These fields need to be retrieved from the NPRA portal.

---

## Cytotoxicity

Blinatumomab is an antineoplastic agent (bispecific immunotherapy).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy (Bispecific T-cell engager, not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — neutropenia, febrile neutropenia, and leukopenia reported |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function (ALT, AST, bilirubin), renal function, cytokine levels (CRS monitoring), neurological status |
| Handling Protection | Standard biologic handling; does not require cytotoxic drug handling precautions as it is not a conventional cytotoxic agent. Follow institutional biologic handling protocols. |

> *Note: The above is based on generally known pharmacological properties. Please refer to the package insert for complete prescribing information, as the evidence pack safety fields contain data gaps.*

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields in the current evidence pack (key warnings, contraindications, drug interactions) are unpopulated. Known major safety concerns for blinatumomab from the published literature include:
> - **Cytokine Release Syndrome (CRS)** — potentially life-threatening; requires stepwise dosing and monitoring
> - **Neurological toxicity** — including seizures, encephalopathy, confusion, tremor
> - **Infections** — due to B-cell depletion and immunosuppression
>
> These must be confirmed via the official package insert before any evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications were generated for blinatumomab, and multiple critical data gaps (MOA, safety warnings, licence details) remain unresolved. A repurposing evaluation cannot proceed without both a candidate indication and baseline safety data.

**To proceed, the following is needed:**
- **Run TxGNN prediction pipeline** for blinatumomab (DB09052) to generate candidate indications
- **Resolve DG001 (Blocking):** Retrieve package insert from NPRA/TFDA and extract warnings and contraindications
- **Resolve DG002 (High):** Query DrugBank API for detailed mechanism of action
- **Complete NPRA licence record:** Populate authorization number, product name, dosage form, and approved indication text
- **Once a predicted indication is available:** Conduct clinical trial search (ClinicalTrials.gov, ICTRP) and literature search (PubMed) for the drug–indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

