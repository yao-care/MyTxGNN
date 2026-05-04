---
layout: default
title: Anidulafungin
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Anidulafungin
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

# Anidulafungin: Repurposing Evaluation (No TxGNN Predictions Currently Available)

---

## One-Sentence Summary

Anidulafungin (DB00362) is an echinocandin antifungal agent with one active registration in Malaysia.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug — the `predicted_indications` list is empty — meaning a standard repurposing evaluation cannot be completed at this stage.
Critical upstream data gaps in the original approved indication, mechanism of action, and safety profile must be resolved before the pipeline can produce actionable output.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions to evaluate |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Currently, detailed mechanism of action data is not available. Based on its DrugBank classification (DB00362), Anidulafungin belongs to the **echinocandin** class of antifungal agents. Echinocandins act by inhibiting 1,3-β-D-glucan synthase, an enzyme essential for fungal cell wall integrity that has no mammalian equivalent — giving this drug class a highly selective safety profile.

The absence of TxGNN predictions most likely stems from one or more of the following upstream failures:

1. **No approved indications were loaded** — `original_indications` is an empty list, which may have prevented the drug from being correctly anchored in the knowledge graph.
2. **MOA data is missing** — without mechanistic annotation, the graph-based traversal used by TxGNN may have scored no candidate disease nodes above the reporting threshold.
3. **Licence detail fields are blank** — even though 1 NPRA registration exists, all structured fields (product name, dosage form, approved indication text) returned empty strings, suggesting a parsing or data-retrieval failure at the NPRA query step.

Until these inputs are corrected and the prediction pipeline re-run, no repurposing candidates can be evaluated.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| Not returned | Not returned | Not returned | Not returned |

> Although the NPRA query on 2026-03-27 returned a `result_count` of 1, all structured fields within the licence record are blank. The raw response from NPRA should be inspected to determine whether the issue is a field-mapping mismatch in `config/fields.yaml` or an upstream data quality problem in the NPRA database itself.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug interactions) are currently flagged as data gaps or returned empty. The DDI query returned zero interactions with a status of `not_found`. No safety summary can be produced until the package insert is retrieved and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero repurposing candidates for Anidulafungin, and every critical data input — approved indication, mechanism of action, safety warnings, and NPRA licence details — is currently unavailable. There is no evidence base on which to make a repurposing recommendation.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download and parse the NPRA/TFDA package insert PDF to extract approved indications, key warnings, and contraindications; without this, safety pre-screening (S1 gate) cannot be entered
- **[High — DG002]** Query the DrugBank API for Anidulafungin's mechanism of action (DB00362) to enable mechanistic relevance analysis
- **[High]** Investigate why the single NPRA licence record returned all blank fields — check the field mapping in `config/fields.yaml` against the actual NPRA response structure and correct the parser in `scripts/process_fda_data.py`
- **[High]** Re-run `scripts/run_kg_prediction.py` after populating the original indication and MOA fields; verify that Anidulafungin (DB00362) is present and correctly mapped in `data/external/drugbank_vocab.csv`
- **[Medium]** Once predictions are available, collect clinical trial and PubMed literature evidence for the top-ranked predicted indication and re-issue this report at Evidence Level L2 or above before any go/no-go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

