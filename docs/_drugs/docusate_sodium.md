---
layout: default
title: Docusate Sodium
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 0
---

# Docusate Sodium
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

# Docusate Sodium: Drug Repurposing Evaluation — No New Indication Predicted

## One-Sentence Summary

Docusate Sodium is a well-known anionic surfactant stool softener, currently marketed in Malaysia with 1 registration.
The TxGNN model **did not predict any new repurposing indications** for this drug, and no candidate disease was identified for further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | (Not recorded in current dataset) |
| Predicted New Indication | **None** — no predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why Were No Predictions Generated?

Docusate Sodium (dioctyl sodium sulfosuccinate) is an anionic surfactant that acts as a stool softener. It lowers the surface tension of stool, allowing water and lipids to penetrate the faecal mass, thereby facilitating bowel movements. It is widely used as an over-the-counter laxative.

There are several possible reasons why TxGNN did not generate repurposing candidates for this drug:

1. **Missing DrugBank ID**: The Evidence Pack does not contain a DrugBank ID mapping for Docusate Sodium. Without this identifier, the drug cannot be located within the TxGNN knowledge graph, making it impossible to compute disease–drug prediction scores.

2. **Limited knowledge graph connectivity**: Even if mapped, Docusate Sodium is a simple surfactant with a non-specific physical mechanism of action (rather than a receptor- or enzyme-targeted pharmacological mechanism). Drugs with non-specific MOAs tend to have fewer edges in the knowledge graph, reducing the likelihood of meaningful repurposing predictions.

3. **Narrow therapeutic profile**: As a stool softener with localised gastrointestinal action and minimal systemic absorption, the pharmacological basis for cross-indication repurposing is inherently limited.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Not recorded) | (Not recorded) | (Not recorded) | (Not recorded) |

> **Note:** One registration was identified in the NPRA database, but detailed licence fields (authorization number, product name, dosage form, approved indication) were not captured in the current evidence pack. Manual verification on the [NPRA Quest3+ portal](https://quest3plus.bpfk.gov.my/) is recommended.

---

## Safety Considerations

> Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the current evidence pack.

---

## Data Gaps Identified

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Label Warnings / Contraindications | Blocking | Cannot perform S1 safety screening | Download and parse label PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No repurposing candidates were predicted by TxGNN for Docusate Sodium. The most likely root cause is the missing DrugBank ID mapping, which prevents the drug from being located in the knowledge graph. Additionally, as a non-specific surfactant laxative with minimal systemic exposure, Docusate Sodium has limited pharmacological rationale for cross-indication repurposing.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping**: Docusate Sodium corresponds to DrugBank ID **DB11089** (or **DB04352** for the dioctyl sulfosuccinate salt form). Re-run the mapping pipeline with corrected identifiers.
- **Re-execute TxGNN prediction** after DrugBank ID is successfully mapped to the knowledge graph.
- **Fill data gaps**: Obtain label warnings (DG001) and MOA information (DG002) to enable safety screening if predictions are subsequently generated.
- **If no predictions emerge after re-mapping**, classify this drug as **low-priority for repurposing** and archive.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

