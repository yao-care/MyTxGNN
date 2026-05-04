---
layout: default
title: Acalabrutinib Maleate
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Acalabrutinib Maleate
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

# ACALABRUTINIB MALEATE: Repurposing Evaluation — Insufficient Data to Complete Full Assessment

---

## One-Sentence Summary

Acalabrutinib maleate is a targeted anticancer agent (BTK inhibitor) currently registered in Malaysia, indicated for haematological malignancies such as chronic lymphocytic leukaemia and mantle cell lymphoma.
However, **no TxGNN predictions were generated** in this Evidence Pack due to missing DrugBank ID mapping, and critical data fields — including approved indication text, mechanism of action, and safety warnings — are absent.
A complete repurposing evaluation **cannot proceed** until these gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No predictions run yet |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The TxGNN repurposing pipeline requires a valid **DrugBank ID** to locate the drug node within the knowledge graph and compute drug–disease association scores. For this submission, `drugbank_id` is `null`, which means:

1. The drug could not be anchored in the TxGNN knowledge graph.
2. Neither the knowledge graph (KG) method nor the deep learning (DL) method produced candidate scores.
3. Without a scored candidate list, no ranked predicted indications can be reported.

Additionally, the mechanism of action (MOA) data is absent, preventing any mechanistic plausibility analysis even if a candidate indication were identified manually.

Acalabrutinib is known from published literature to be a **second-generation, covalent Bruton's tyrosine kinase (BTK) inhibitor**. BTK plays a central role in B-cell receptor signalling, making it relevant not only to its approved haematological indications but potentially to autoimmune and inflammatory conditions. However, these insights cannot be formally incorporated into a TxGNN report without completing the pipeline.

---

## Malaysia Market Information

The drug is confirmed as **marketed** in Malaysia (1 active registration via NPRA). However, the detailed licence record returned was empty — authorization number, product name, dosage form, and approved indication text were all absent from this Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| *(Not returned by query)* | *(Not returned)* | *(Not returned)* | *(Not returned)* |

> **Note:** NPRA query log confirms 1 result was found (query ID 1, status: success). The empty fields suggest a data extraction or parsing issue in the current pipeline run, not an absence of registration.

---

## Cytotoxicity

Acalabrutinib is an antineoplastic targeted therapy. The following applies pending full package insert retrieval:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — covalent BTK inhibitor |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low (typical for oral small-molecule targeted agents) |
| Monitoring Items | CBC with differential, liver function tests, renal function |
| Handling Protection | Follow institutional cytotoxic drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline did not produce any scored indications due to a missing DrugBank ID, and all safety and indication details from the regulatory record are absent — this Evidence Pack does not contain sufficient data to support a repurposing evaluation.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping**: Query DrugBank for "acalabrutinib" (the free base INN); the maleate salt form may not match directly. Expected ID: DB12116. Re-run `scripts/run_kg_prediction.py` after mapping.
- **Re-parse NPRA licence record**: The NPRA query returned 1 result but all fields are empty. Review the raw response in `data/raw/malaysia_fda_drugs.json` and fix the field extraction in `scripts/process_fda_data.py`.
- **Retrieve MOA from DrugBank**: Once the DrugBank ID is confirmed, pull `pharmacodynamics`, `mechanism-of-action`, and `categories` fields via the DrugBank API.
- **Download package insert PDF**: Obtain the NPRA-approved package insert to extract approved indications, key warnings, and contraindications. This is flagged as a **Blocking** data gap (DG001).
- **Re-run Evidence Pack generation** after the above four items are completed to produce a full L1–L5 evidence-graded report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

