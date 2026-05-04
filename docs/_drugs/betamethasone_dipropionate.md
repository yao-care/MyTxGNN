---
layout: default
title: Betamethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 0
---

# Betamethasone Dipropionate
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

# Betamethasone Dipropionate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Betamethasone Dipropionate is a potent synthetic corticosteroid widely used for inflammatory and pruritic dermatological conditions. The TxGNN model has **not generated any predicted new indications** for this drug at this time. There are currently **no clinical trials or publications** linked to a repurposing candidate, and several critical data gaps remain to be resolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *(Data not available in current evidence pack — see note below)* |
| Predicted New Indication | **None** (no TxGNN predictions generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — Model prediction only; no candidate identified |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 41 |
| Recommended Decision | **Hold** |

> **Note on Original Indication:** The 41 licence records returned by NPRA all have empty indication text fields. Based on established pharmacological knowledge, Betamethasone Dipropionate is a high-potency topical corticosteroid indicated for the relief of inflammatory and pruritic manifestations of corticosteroid-responsive dermatoses (e.g., eczema, psoriasis, dermatitis).

---

## Why is This Prediction Reasonable?

There is **no TxGNN prediction to evaluate** at this time. The `predicted_indications` array is empty, meaning the model did not return any drug-repurposing candidates for Betamethasone Dipropionate.

This may be due to one or more of the following reasons:
- **Missing DrugBank ID mapping**: The evidence pack shows `drugbank_id: null`. Without a valid DrugBank identifier, the TxGNN knowledge graph cannot anchor the drug node and therefore cannot generate repurposing predictions.
- **Topical corticosteroid limitations**: Betamethasone Dipropionate is predominantly used as a topical agent. Drugs with primarily local (non-systemic) mechanisms may have fewer knowledge-graph connections to systemic disease nodes, reducing the likelihood of high-scoring predictions.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, Betamethasone Dipropionate is a synthetic fluorinated corticosteroid that exerts anti-inflammatory, antipruritic, and vasoconstrictive effects by binding to intracellular glucocorticoid receptors, suppressing pro-inflammatory cytokine release, and inhibiting phospholipase A2 activity. This mechanism is well-characterised but the MOA field should be populated from DrugBank to enable proper mechanistic analysis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication to query against).

---

## Literature Evidence

Currently no related literature available (no predicted indication to query against).

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |
| *(empty)* | *(empty)* | *(empty)* | *(empty)* |

> **Data Quality Issue:** All 41 NPRA licence records were returned with empty fields (licence number, product name, dosage form, and approved indication text are all blank). The raw NPRA query was successful (`result_count: 41`), but the structured data was not parsed into the evidence pack. This must be remediated before the report can be completed.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety data fields (key warnings, contraindications, drug interactions) are currently unavailable. The DDI query returned zero interactions. These data gaps are classified as **Blocking** severity — the evaluation cannot proceed to Stage 1 safety screening without them.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated because (1) no TxGNN repurposing predictions were generated, likely due to a missing DrugBank ID mapping, and (2) the NPRA licence data, safety warnings, and mechanism of action are all missing or empty. There is no predicted indication to assess.

**To proceed, the following is needed:**

1. **Resolve DrugBank ID mapping** — Query DrugBank for "Betamethasone Dipropionate" (the query log shows a successful DrugBank hit with `result_count: 1`; the ID should be captured and populated as `drugbank_id` — expected: [DB04315](https://go.drugbank.com/drugs/DB04315) or parent compound [DB00443](https://go.drugbank.com/drugs/DB00443) for Betamethasone)
2. **Re-parse NPRA licence records** — The 41 registrations were found but all fields are empty; re-download and parse the structured data
3. **Populate MOA from DrugBank** — Once the DrugBank ID is resolved, retrieve the mechanism of action
4. **Retrieve safety data** — Download and parse package insert PDFs from the NPRA/TFDA website for warnings, contraindications, and drug interactions
5. **Re-run TxGNN prediction** — With a valid DrugBank ID mapped into the knowledge graph, re-execute the KG and DL prediction pipelines to generate repurposing candidates
6. **Re-generate evidence pack** — Once the above gaps are filled, produce a v5 evidence pack and re-run this report

---

*This report was generated on 2026-04-09 based on Evidence Pack v4 (candidate ID: TW-UNKNOWN-multi). Results are for research purposes only and do not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

