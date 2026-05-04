---
layout: default
title: Antazoline Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 0
---

# Antazoline Hydrochloride
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

# Antazoline Hydrochloride: Drug Repurposing Evaluation — No TxGNN Prediction Available

## One-Sentence Summary

Antazoline hydrochloride is a first-generation H1 antihistamine with additional alpha-adrenergic blocking properties, classically used in ophthalmic formulations for allergic conjunctivitis.
The TxGNN model **did not generate any repurposing predictions** for this drug in the current run, likely due to missing DrugBank ID linkage required for knowledge graph traversal.
Without a prediction score or candidate indication, this evaluation is limited to a data-completeness and regulatory assessment only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current regulatory records |
| Predicted New Indication | None — TxGNN returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | Insufficient — no prediction generated |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Antazoline hydrochloride is a first-generation antihistamine (H1 receptor antagonist) that also exhibits moderate alpha-adrenergic blocking activity. It is typically formulated as ophthalmic drops (often combined with naphazoline or xylometazoline) for the relief of allergic conjunctivitis, and has historically been studied as a Class Ia antiarrhythmic agent.

The TxGNN knowledge graph engine maps drugs via their **DrugBank ID** to traverse disease–drug–gene–pathway relationships. In this Evidence Pack, `drugbank_id` is **null**, meaning the drug entity could not be anchored in the knowledge graph. Without this anchor, neither KG-based nor deep learning–based repurposing scores can be computed.

Additionally, the mechanism of action (MOA) data is unavailable in the current pack. Mechanistically, antihistamines in this class have been explored in contexts such as upper respiratory allergy, insomnia (sedating effect), and motion sickness — but these remain unconfirmed directions without a formal TxGNN prediction score to assess.

---

## Malaysia Market Information

Current regulatory data returned **1 active licence**, but the licence record fields (authorisation number, product name, dosage form, approved indication) were not populated in this Evidence Pack extraction. The market status is confirmed as **已上市 (Marketed)**.

| Item | Status |
|------|--------|
| Market Status | ✓ Marketed in Malaysia |
| Total Active Licences | 1 |
| Licence Detail | Record present but fields unpopulated — manual NPRA lookup required |

> To retrieve full licence details, search the NPRA Product Registration database at [https://www.npra.gov.my](https://www.npra.gov.my) using the active ingredient "ANTAZOLINE HYDROCHLORIDE".

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Both key warnings and contraindications are flagged as data gaps in this Evidence Pack (severity: **Blocking** and **High** respectively). No drug–drug interaction records were found in the DDI query. Resolving these gaps is required before any repurposing pathway can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no repurposing candidates for antazoline hydrochloride because the DrugBank ID linkage is missing, preventing knowledge graph traversal entirely. Without a prediction target, evidence assessment cannot be initiated.

**To proceed, the following is needed:**

- **[Critical — Blocking]** Resolve `drugbank_id`: Search DrugBank (https://www.drugbank.ca) for "antazoline" and confirm the correct ID (likely DB01114 or similar); update the Evidence Pack and re-run TxGNN prediction pipeline
- **[Critical — Blocking]** Retrieve TFDA/NPRA package insert: Download the approved product insert PDF and extract warnings, contraindications, and approved indication text to unblock the S1 safety screen
- **[High]** Populate MOA data: Query DrugBank API for pharmacodynamics and mechanism of action to enable mechanistic plausibility analysis once a predicted indication is available
- **[Medium]** Populate NPRA licence record fields: Confirm authorisation number, product name, dosage form, manufacturer, and approved indication text from the NPRA registry
- **[Follow-up]** Re-run Evidence Pack generation after DrugBank ID is confirmed and resubmit for full report evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

