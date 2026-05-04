---
layout: default
title: Brimonidine Tartrate
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 0
---

# Brimonidine Tartrate
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

# Brimonidine Tartrate: Drug Repurposing Evaluation — Insufficient Data for Prediction

## One-Sentence Summary

Brimonidine tartrate is an alpha-2 adrenergic agonist widely used for the treatment of glaucoma and ocular hypertension. The TxGNN model has **not generated any predicted new indications** for this drug, and key data fields (DrugBank ID, MOA, approved indication text, safety data) remain unfilled. This report serves as a **data gap assessment** to guide next steps for completing the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *(Data not provided in evidence pack — known clinically for glaucoma / ocular hypertension)* |
| Predicted New Indication | **None** — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Why Was No Prediction Generated?

Brimonidine tartrate is a selective alpha-2 adrenergic receptor agonist. It reduces aqueous humour production and enhances uveoscleral outflow, thereby lowering intraocular pressure. It is also available in a topical dermal formulation for the treatment of persistent facial erythema associated with rosacea.

The TxGNN model returned an empty `predicted_indications` array, which typically indicates one or more of the following issues:

1. **Missing DrugBank ID mapping** — The evidence pack shows `drugbank_id: null`. Without a valid DrugBank identifier, the drug cannot be located in TxGNN's knowledge graph (`node.csv`), and no repurposing candidates can be scored. The query log shows a DrugBank query returned 1 result, but the ID was not populated into the evidence pack.

2. **Incomplete upstream data** — The `original_indications` array is empty and all licence records have blank fields, suggesting the NPRA data extraction did not successfully parse structured fields for this drug.

3. **Topical/ophthalmic route limitation** — Brimonidine is predominantly used as an ophthalmic or topical agent. The TxGNN knowledge graph may have limited representation of locally-acting drugs compared to systemic therapeutics.

Until the DrugBank ID is resolved and the drug is successfully mapped into the knowledge graph, no repurposing predictions can be generated.

---

## Clinical Trial Evidence

No predicted indication is available; therefore, no targeted clinical trial search was conducted.

---

## Literature Evidence

No predicted indication is available; therefore, no targeted literature search was conducted.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |

> **Note:** 9 registrations were identified by the NPRA query, but structured licence details (authorization number, product name, dosage form, approved indication) were not populated in the evidence pack. The raw NPRA data needs to be re-extracted and parsed.

---

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, drug interactions) are currently unpopulated in the evidence pack.

---

## Data Gap Summary

The following critical gaps must be resolved before this candidate can progress:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | Package insert warnings & contraindications | **Blocking** | Cannot enter S1 safety screening | Download package insert PDF from NPRA/TFDA and parse |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API (1 result already found) |
| — | DrugBank ID | **Blocking** | Cannot run TxGNN prediction without KG node | Map from DrugBank query result (DB00484) |
| — | NPRA licence details | High | Market information section is empty | Re-extract structured fields from NPRA |
| — | Original indication text | High | Cannot establish baseline for repurposing logic | Parse from NPRA approved indication field |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack is critically incomplete — no DrugBank ID mapping, no parsed licence details, no safety data, and consequently no TxGNN predictions were generated. There is insufficient information to evaluate any repurposing opportunity at this time.

**To proceed, the following is needed:**
- **Resolve DrugBank ID mapping** — The query log indicates 1 DrugBank result was found; populate `drugbank_id` (likely **DB00484** for brimonidine) and re-run TxGNN prediction
- **Re-extract NPRA licence data** — Parse authorization numbers, product names, dosage forms, and approved indication text for all 9 registrations
- **Obtain package insert** — Download and parse warnings, contraindications, and drug interaction information
- **Query DrugBank API for MOA** — Retrieve mechanism of action, pharmacodynamics, and toxicity data
- **Re-run TxGNN pipeline** — Once DrugBank ID is mapped, execute `run_kg_prediction.py` to generate repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

