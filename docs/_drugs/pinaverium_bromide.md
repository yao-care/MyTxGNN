---
layout: default
title: Pinaverium Bromide
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 0
---

# Pinaverium Bromide
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

# Pinaverium Bromide: Drug Repurposing Evaluation — Pending Data Resolution

## One-Sentence Summary

Pinaverium bromide is a calcium-selective antispasmodic agent primarily indicated for functional gastrointestinal disorders, including irritable bowel syndrome (IBS).
The TxGNN repurposing pipeline was **unable to generate predicted new indications** for this drug, as two critical upstream data gaps — missing DrugBank ID and mechanism of action (MOA) — prevent knowledge graph traversal.
This report documents the current assessment status and the specific remediation steps required before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Functional gastrointestinal disorders / IBS (general pharmacological knowledge; not confirmed in current Evidence Pack) |
| Predicted New Indication | No predictions available — pipeline incomplete |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Malaysia Market Information

The NPRA query (2026-03-27) confirmed **2 active registrations** in Malaysia. However, the detailed license fields (authorization numbers, product names, dosage forms, and approved indications) were not populated in the current data extract and require a follow-up retrieval.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Not available in current extract |
| — | — | — | Not available in current extract |

> To retrieve full license details, query the NPRA Product Registration database directly using the search term "PINAVERIUM BROMIDE".

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug-drug interactions were identified (DDI query status: not found, 0 interactions). Key warnings and contraindications are currently unavailable pending package insert retrieval (Data Gap DG001 — Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN knowledge graph prediction pipeline requires a valid DrugBank ID to map Pinaverium Bromide onto the drug–disease knowledge graph. Without this mapping, no repurposing candidates can be scored or ranked, making a meaningful evidence evaluation impossible at this stage.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve the Malaysia-approved package insert from NPRA or the Dicetel® product label to extract approved indications, key warnings, and contraindications; this is required before safety pre-screening (Stage S1) can be initiated
- **[DG002 — High]** Obtain the DrugBank ID and full MOA description — search DrugBank for "pinaverium" (expected entry: DB06716) — to enable knowledge graph traversal and generate TxGNN repurposing candidates
- **Re-run the TxGNN pipeline** after resolving DG001 and DG002; expected outputs include repurposing candidate rankings, supporting clinical trial evidence, and literature citations
- **Populate NPRA license details** (authorization numbers, product names, dosage forms, approved indications) from the NPRA registration portal to complete the Malaysia regulatory section
- **Verify market status and indication scope** through official NPRA records to confirm whether current Malaysian approvals already cover any predicted new indications (which would simplify the regulatory pathway)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

