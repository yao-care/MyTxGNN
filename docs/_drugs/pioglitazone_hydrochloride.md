---
layout: default
title: Pioglitazone Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 0
---

# Pioglitazone Hydrochloride
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

# Pioglitazone Hydrochloride: Repurposing Evaluation (TxGNN Prediction Pending)

## One-Sentence Summary

Pioglitazone hydrochloride is a thiazolidinedione-class PPARγ agonist widely used for Type 2 Diabetes Mellitus management, with 6 active registrations in Malaysia.
This Evidence Pack does not yet contain TxGNN repurposing predictions — the evaluation below is therefore preliminary, and a **Hold** decision is recommended until the data pipeline is completed.
Once predictions are generated, the drug's insulin-sensitising and anti-inflammatory mechanisms make it a promising repurposing candidate for metabolic and inflammatory conditions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from drug class; NPRA details pending) |
| Predicted New Indication | Not available — TxGNN prediction not yet generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacological knowledge, pioglitazone hydrochloride belongs to the thiazolidinedione (TZD) class and acts as a selective agonist of **peroxisome proliferator-activated receptor gamma (PPARγ)** — a nuclear receptor that regulates genes involved in glucose metabolism, adipogenesis, lipid homeostasis, and inflammatory signalling. This pleiotropic mechanism is the pharmacological basis for most repurposing hypotheses.

PPARγ activation influences pathways relevant to a range of conditions beyond Type 2 Diabetes, including non-alcoholic steatohepatitis (NASH), polycystic ovary syndrome (PCOS), neurodegenerative diseases, and certain inflammatory or fibrotic conditions. The breadth of PPARγ's downstream effects means that pioglitazone has mechanistic rationale for multiple therapeutic areas — making it a classically attractive repurposing candidate.

Because the TxGNN model has not yet produced predictions for this drug in the current Evidence Pack, no specific new indication can be formally evaluated at this stage. Once predictions are available, the mechanistic link between PPARγ agonism and the top-ranked predicted indications can be assessed in detail.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

> **Note:** This reflects the absence of TxGNN-predicted indications, not the global literature. Once a target indication is confirmed, ClinicalTrials.gov and ICTRP queries should be re-run against that specific indication.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

> **Note:** Same caveat as above — evidence collection is indication-specific and requires a confirmed TxGNN prediction first.

---

## Malaysia Market Information

The NPRA query (2026-03-27) confirmed **6 active registrations** for pioglitazone hydrochloride. However, individual product records were returned without populated detail fields. A follow-up data pull is required to retrieve full licence information.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | Details not retrieved in this Evidence Pack |
| — | — | — | Details not retrieved in this Evidence Pack |
| — | — | — | Details not retrieved in this Evidence Pack |
| — | — | — | Details not retrieved in this Evidence Pack |
| — | — | — | Details not retrieved in this Evidence Pack |

> 6 registrations confirmed by NPRA query. Full licence details (product names, dosage forms, approved indication text) require a follow-up NPRA data enrichment step.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not retrieved in this Evidence Pack (Data Gap DG001 — Blocking severity).

> **Class-level caution (domain knowledge, not yet confirmed via package insert):** Thiazolidinediones as a class are associated with fluid retention and risk of congestive heart failure exacerbation, potential increased risk of bladder cancer with prolonged use, and bone fracture risk particularly in women. These must be formally confirmed by parsing the official Malaysia package insert before any clinical or regulatory assessment proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is critically incomplete — no TxGNN repurposing predictions have been generated, all individual NPRA licence detail fields are unpopulated, and safety data retrieval has failed. A meaningful repurposing evaluation cannot be produced with the current data, and proceeding without resolving the Blocking data gap (DG001) would be inappropriate.

**To proceed, the following is needed:**

- **[Critical — Blocking]** Download and parse the Malaysia package insert PDF to extract warnings, contraindications, and drug interactions (resolves Data Gap DG001)
- **[Critical]** Complete the TxGNN knowledge graph prediction run for pioglitazone hydrochloride to generate a ranked list of repurposing candidates
- **[High]** Query DrugBank API to retrieve DrugBank ID, full MOA description, drug categories, and DDI data (resolves Data Gap DG002)
- **[High]** Re-run NPRA data enrichment to populate all 6 licence records with product names, dosage forms, and approved indication text
- **[Standard]** Re-run clinical trial (ClinicalTrials.gov / ICTRP) and PubMed evidence collection against the top-ranked TxGNN-predicted indication once confirmed
- **[Standard]** Confirm whether pioglitazone hydrochloride has any antineoplastic classification — if not, the Cytotoxicity section can be formally omitted from the final report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

