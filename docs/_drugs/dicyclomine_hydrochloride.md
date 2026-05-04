---
layout: default
title: Dicyclomine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 0
---

# Dicyclomine Hydrochloride
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

# Dicyclomine Hydrochloride: Drug Repurposing Evaluation Report

## One-Sentence Summary

Dicyclomine Hydrochloride is an anticholinergic/antispasmodic agent currently marketed in Malaysia with 4 registered products. No TxGNN model predictions for new indications are available at this time, and critical data gaps in mechanism of action, approved indication details, and safety information must be addressed before any repurposing assessment can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, no TxGNN predictions have been generated for Dicyclomine Hydrochloride, so a mechanistic plausibility assessment cannot be performed at this stage.

Dicyclomine Hydrochloride is known to be an antimuscarinic (anticholinergic) antispasmodic agent commonly used for functional gastrointestinal disorders such as irritable bowel syndrome (IBS). However, the Evidence Pack does not contain a confirmed DrugBank ID or detailed mechanism of action data. Without a DrugBank mapping, the drug cannot be linked into the TxGNN knowledge graph, which is a prerequisite for generating repurposing predictions.

Resolving the DrugBank ID mapping (likely **DB00804** based on the INN) and populating the mechanism of action data are essential first steps before the TxGNN prediction pipeline can be executed for this compound.

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication available for evidence search.

## Literature Evidence

Currently no related literature available — no predicted indication available for evidence search.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Not available) | (Not available) | (Not available) | (Not available) |
| (Not available) | (Not available) | (Not available) | (Not available) |
| (Not available) | (Not available) | (Not available) | (Not available) |
| (Not available) | (Not available) | (Not available) | (Not available) |

> **Note:** 4 product registrations were confirmed via NPRA query (2026-03-27), but detailed license information (authorization numbers, product names, dosage forms, and approved indications) has not yet been populated into the Evidence Pack.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data have not yet been collected for this Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evaluation cannot proceed because critical foundational data is missing: (1) no DrugBank ID mapping has been confirmed, preventing TxGNN knowledge graph integration; (2) no predicted indications have been generated; and (3) approved indication text, safety warnings, and contraindications are all absent.

**To proceed, the following is needed:**

1. **Confirm DrugBank mapping** — Query DrugBank for "Dicyclomine Hydrochloride" (expected: DB00804) and populate `drug.drugbank_id`
2. **Populate mechanism of action** — Retrieve MOA from DrugBank (anticholinergic/antimuscarinic, smooth muscle relaxant)
3. **Collect NPRA license details** — Download full registration records from NPRA to populate authorization numbers, product names, dosage forms, and approved indication text
4. **Run TxGNN prediction pipeline** — Once DrugBank ID is mapped, execute KG + DL prediction to generate repurposing candidates
5. **Collect safety data** — Parse package insert PDFs for key warnings, contraindications, and drug interactions
6. **Re-run evidence collection** — After predictions are available, query ClinicalTrials.gov, PubMed, and ICTRP for supporting evidence

---

*This report is for research reference only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

