---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to IGHV-Mutated CLL/SLL Subtype

## One-Sentence Summary

Ofatumumab is a human anti-CD20 monoclonal antibody originally approved for chronic lymphocytic leukemia (CLL), including relapsed/refractory disease.
The TxGNN model's top-ranked prediction points to **chronic lymphocytic leukemia/small lymphocytic lymphoma with IGHV somatic hypermutation** (a molecularly-defined CLL/SLL subtype) with a **99.77% prediction score**,
but currently **no clinical trials or publications are indexed specifically for this subtype** — the evidence base is inferred by transfer from the drug's well-established parent CLL/SLL indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic lymphocytic leukemia (CLL), incl. disease refractory to fludarabine and alemtuzumab — inferred from associated trial/literature evidence in this pack; the Malaysia (NPRA) license record itself has no indication text on file |
| Predicted New Indication | Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation (IGHV-mutated CLL/SLL) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 (per model scoring; no trials/literature are directly indexed to this subtype — evidence is transferred from the parent CLL/SLL entity, see below) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank-level mechanism-of-action data is flagged as a data gap in this pack (DG002). However, the associated literature evidence consistently describes ofatumumab as a fully human IgG1κ anti-CD20 monoclonal antibody that binds a membrane-proximal epitope on CD20 and depletes CD20-positive B cells primarily through complement-dependent cytotoxicity (CDC) and antibody-dependent cell-mediated cytotoxicity (ADCC).

IGHV-mutated CLL/SLL is not a separate disease — it is a prognostic molecular subtype of CLL/SLL defined by immunoglobulin heavy-chain variable-region somatic hypermutation status. Since CD20 expression and the CDC/ADCC-based mechanism of ofatumumab are shared across CLL/SLL regardless of IGHV status, the mechanistic case for activity in this subtype follows directly from the drug's already-approved CLL/SLL indication rather than representing a novel biological hypothesis.

This also explains the evidence gap: registration trials for ofatumumab in CLL/SLL (e.g., the Phase 3 DUO trial, NCT02004522, and the RESONATE comparator trials) generally did not stratify enrollment or reporting by IGHV mutation status, so no study is indexed specifically to this subtype. The parent CLL/SLL indication (see predicted_indications rank 5 in this pack) carries much stronger direct evidence — L1, 34 clinical trials including multiple completed Phase 3 studies, and 20 publications — and the scoring engine explicitly notes that this is ofatumumab's original, already-approved indication rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for the IGHV-mutated CLL/SLL subtype.

## Literature Evidence

Currently no related literature available specifically for the IGHV-mutated CLL/SLL subtype.

## Malaysia Market Information

Malaysia (NPRA) records confirm the product is marketed, with 1 registered license. However, the underlying license record (authorization number, product name, dosage form, and approved indication text) is not populated in the source data and constitutes a data gap.

## Cytotoxicity

Ofatumumab's original indication is an oncologic condition (CLL/SLL), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to Moderate — literature describes an overall favorable toxicity profile relative to conventional chemoimmunotherapy, though neutropenia has been reported, particularly in combination regimens |
| Emetogenicity Classification | Low (monoclonal antibody class) |
| Monitoring Items | CBC with differential, infusion-related reaction monitoring, hepatitis B reactivation screening (standard precaution for anti-CD20 agents), renal and hepatic function |
| Handling Protection | Standard biologic infusion precautions (premedication, infusion-reaction monitoring) apply; conventional cytotoxic drug handling regulations are not required as ofatumumab is not a DNA-damaging/alkylating cytotoxic agent |

Detailed institution-specific toxicity data (e.g., DrugBank toxicity fields) were not available in this pack — please refer to the package insert warnings and precautions for full detail.

## Safety Considerations

Please refer to the package insert for safety information. TFDA/NPRA-level warnings, contraindications, and drug interaction data are all flagged as data gaps in this pack (DG001, Blocking severity), and the DDI query returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (IGHV-mutated CLL/SLL) has no direct clinical trial or literature evidence — it is a mechanistically plausible extension of an already-approved indication rather than a novel repurposing signal, and the missing safety label data (DG001, Blocking) prevents even an initial S1 safety screen.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (仿單) PDF for warnings, contraindications, and drug interactions (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- IGHV-status-stratified subgroup analysis from existing CLL/SLL Phase 3 data (e.g., re-analysis of the DUO trial, NCT02004522) to generate direct evidence for this subtype
- Malaysia-specific license and approved-indication text for the marketed product

**Note:** A separate candidate in this pack, **follicular lymphoma** (rank 3, score 99.70%), carries substantially stronger independent evidence — 15 clinical trials (including a terminated Phase 3 head-to-head study) and 20 publications — and represents a more genuine repurposing opportunity outside ofatumumab's original CLL/SLL indication; it may warrant its own dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

