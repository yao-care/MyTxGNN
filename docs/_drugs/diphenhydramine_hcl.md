---
layout: default
title: Diphenhydramine Hcl
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 0
---

# Diphenhydramine Hcl
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

# Diphenhydramine HCl: Drug Repurposing Evaluation — No Predicted Indications

## One-Sentence Summary

Diphenhydramine HCl is a first-generation antihistamine (H1 receptor antagonist) widely used for allergic symptoms, motion sickness, and as a sleep aid. The TxGNN model currently has **no predicted new indications** for this drug, and the evidence pack contains significant data gaps in regulatory details, safety information, and mechanism of action documentation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antihistamine (allergy, motion sickness, insomnia — specific approved indication text not available in data) |
| Predicted New Indication | None (no TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 21 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

There are currently **no TxGNN-predicted new indications** for Diphenhydramine HCl, so a mechanistic plausibility assessment cannot be performed at this time.

For background, Diphenhydramine is a first-generation antihistamine that acts as an inverse agonist at the histamine H1 receptor. It also exhibits anticholinergic, antitussive, antiemetic, and mild sedative properties. These multi-receptor activities have historically made it useful across allergy, cold symptoms, motion sickness, and short-term insomnia management.

The absence of TxGNN predictions may result from several factors: (1) the drug's DrugBank ID was not mapped (recorded as `null`), which would prevent the knowledge graph from linking Diphenhydramine to its molecular targets and disease associations; (2) incomplete integration of regulatory and pharmacological metadata. Resolving the DrugBank mapping is a prerequisite for generating meaningful repurposing predictions.

## Clinical Trial Evidence

Currently no predicted indication available — clinical trial evidence search was not performed.

## Literature Evidence

Currently no predicted indication available — literature evidence search was not performed.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (not available) | (not available) | (not available) | (not available) |

> **Note:** 21 registrations were identified for Diphenhydramine HCl in the NPRA database, but detailed license information (authorization numbers, product names, dosage forms, and approved indications) was not populated in the evidence pack. This data gap should be remediated by re-querying the NPRA database.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** Key warnings, contraindications, and drug interaction data were not available in the evidence pack. As a widely used OTC antihistamine, Diphenhydramine's well-known safety concerns include sedation/drowsiness, anticholinergic effects (dry mouth, urinary retention, constipation), and risk of confusion in elderly patients. A full safety review from the package insert and DrugBank is recommended before any repurposing evaluation proceeds.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications are available for Diphenhydramine HCl. The evidence pack has critical data gaps — missing DrugBank ID mapping, empty license details, and absent safety data — that prevent any meaningful repurposing evaluation.

**To proceed, the following is needed:**
- **DrugBank ID mapping**: Resolve the `null` DrugBank ID (Diphenhydramine is DB01075 in DrugBank) to enable knowledge graph linkage
- **Re-run TxGNN prediction**: Once the DrugBank mapping is established, re-execute the KG and DL prediction pipelines
- **Populate NPRA license details**: Re-query the NPRA database to fill in authorization numbers, product names, dosage forms, and approved indication text for all 21 registrations
- **Safety data collection**: Download and parse the package insert to extract key warnings, contraindications, and drug interactions
- **MOA documentation**: Retrieve mechanism of action details from DrugBank (H1 receptor inverse agonist, anticholinergic properties)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

