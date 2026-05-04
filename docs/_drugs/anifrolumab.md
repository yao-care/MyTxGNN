---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 0
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to — (No TxGNN Prediction Data in This Evidence Pack)

---

## One-Sentence Summary

Anifrolumab (SAPHNELO) is a fully human monoclonal antibody targeting the type I interferon receptor (IFNAR1), approved for moderate-to-severe systemic lupus erythematosus (SLE) in adults.
This Evidence Pack contains **no TxGNN-predicted new indications**, and two critical data gaps — missing package insert safety information (Blocking) and missing mechanism of action data (High) — prevent a complete repurposing assessment.
**No repurposing recommendation can be issued** until these gaps are remediated and the prediction pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe systemic lupus erythematosus (SLE) |
| Predicted New Indication | No predictions available in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Reasonable to Evaluate

The `predicted_indications` field in this Evidence Pack is empty. Three likely causes:

1. **Pipeline not yet executed** — The TxGNN prediction run for DB11976 may not have been triggered or completed.
2. **DrugBank ID mapping failure** — If ANIFROLUMAB was not successfully matched to a node in the knowledge graph, no candidate diseases would be scored.
3. **Data staging issue** — Prediction outputs may exist upstream but were not merged into this v4 Evidence Pack.

In parallel, two data gaps block evaluation even if predictions were available:

| Gap ID | Item | Severity | Impact |
|--------|------|----------|--------|
| DG001 | Package insert warnings & contraindications | **Blocking** | Cannot complete S1 safety pre-screen |
| DG002 | Mechanism of action (MOA) | High | Cannot perform mechanistic rationale scoring |

---

## Drug Background: Known Mechanism of Action

Although the MOA field is marked as a data gap in this Evidence Pack, anifrolumab's mechanism is well characterised in the published literature and the DrugBank record for DB11976.

Anifrolumab is a fully human IgG1κ monoclonal antibody that binds to subunit 1 of the type I interferon receptor (**IFNAR1**), blocking signalling from **all type I interferons** (IFN-α, IFN-β, IFN-ω, and related subtypes). Type I IFN signalling is pathologically overactivated in approximately 60–80% of SLE patients, driving inflammatory cytokine production, dendritic cell activation, and B-cell autoreactivity. By occupying IFNAR1, anifrolumab suppresses the interferon gene signature (IFNGS) and attenuates downstream JAK1/TYK2-mediated transcription of pro-inflammatory genes.

This mechanism is not SLE-exclusive. Other conditions characterised by elevated type I IFN activity — including dermatomyositis, primary Sjögren's syndrome, systemic sclerosis, and ANCA-associated vasculitis — are biologically plausible targets. However, **none are confirmed via TxGNN prediction in this data pack**, and this background information is provided solely for context pending re-run of the prediction pipeline.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| (Not populated) | Anifrolumab — SAPHNELO | (Not populated) | Moderate-to-severe active SLE in adults (details not yet extracted into this Evidence Pack) |

> **Note:** The Evidence Pack records 1 registered licence with market status "已上市" (Marketed), but all licence detail fields — including licence number, product name, dosage form, manufacturer, and approved indication text — are unpopulated. Please verify directly against the NPRA online registry or retrieve the full licence record before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Alert (DG001 — Blocking):** Both the key warnings and contraindications fields are listed as [Data Gap] in this Evidence Pack. A formal safety assessment cannot be completed. Based on the drug class (anti-IFNAR1 biologic), clinicians should be aware that typical considerations for this category include: serious and opportunistic infections (including influenza and herpes zoster), live attenuated vaccine contraindication during treatment, infusion-related and hypersensitivity reactions, and potential immunosuppression in combination with other biologics. **These are general class considerations only and must be confirmed against the approved Malaysian package insert before any clinical decision.**

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is materially incomplete — no TxGNN repurposing predictions are present, critical safety data is absent at a blocking severity level, and licence detail fields are unpopulated. Issuing a repurposing recommendation under these conditions would not be scientifically defensible.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download and parse the NPRA/TFDA package insert PDF for SAPHNELO (anifrolumab) to extract approved warnings, contraindications, special population guidance, and handling requirements; populate the `safety.key_warnings` and `safety.contraindications` fields
- **[High — DG002]** Query DrugBank API for DB11976 to retrieve the full MOA text and populate the `drug.original_moa` field
- **[Pipeline]** Re-run the TxGNN KG + DL prediction pipeline with confirmed DrugBank ID DB11976 to populate `predicted_indications`
- **[Regulatory]** Retrieve complete licence detail record from NPRA (licence number, product name, dosage form, approved indication text) and populate `taiwan_regulatory.licenses[0]`
- **[Re-evaluation]** Once all four items above are resolved, resubmit the Evidence Pack (target v5) for a full L1–L5 evidence-level repurposing assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

