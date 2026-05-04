---
layout: default
title: Amoxycillin
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 0
---

# Amoxycillin
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

# Amoxycillin: Broad-Spectrum Antibiotic — TxGNN Repurposing Analysis Pending

---

## One-Sentence Summary

Amoxycillin is a widely-used aminopenicillin antibiotic indicated for a broad range of bacterial infections, with 66 registered products in Malaysia confirming strong market presence.
The TxGNN model has **not yet generated repurposing predictions** for this drug in the current Evidence Pack.
Without predicted indications, clinical trial and literature evidence searches have not been initiated, and a full repurposing evaluation cannot proceed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, urinary tract, skin and soft tissue, *H. pylori* eradication) |
| Predicted New Indication | Not yet generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not applicable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 66 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Amoxycillin is a broad-spectrum aminopenicillin in the beta-lactam antibiotic class. Its mechanism of action centres on binding to penicillin-binding proteins (PBPs) embedded in the bacterial cell membrane, blocking the final transpeptidation step of peptidoglycan cross-linking. This prevents cell wall synthesis, causing osmotic instability and bactericidal lysis. It is active against a wide range of Gram-positive organisms (e.g., *Streptococcus*, *Enterococcus*) and selected Gram-negative pathogens (e.g., *H. pylori*, *E. coli*, *H. influenzae*).

Clinically, amoxycillin is a first-line agent for community-acquired pneumonia, acute otitis media, urinary tract infections, dental infections, and *Helicobacter pylori* eradication as part of triple or quadruple therapy regimens. It is among the most prescribed antibiotics globally, with a decades-long safety and efficacy database across all age groups.

Because the current Evidence Pack contains **no TxGNN-predicted new indications**, a disease-specific mechanistic rationale for repurposing cannot be provided at this time. This section will be updated once the TxGNN prediction pipeline has been executed with the correct DrugBank identifier for Amoxycillin.

---

## Malaysia Market Information

The Malaysia NPRA database confirms **66 registered products** for Amoxycillin, indicating well-established market access across multiple manufacturers and dosage forms. However, the individual licence records were not populated in this version of the Evidence Pack.

| Authorisation Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | Not populated in current data pack | — | — |

> Full licence details (product names, dosage forms, manufacturers, and approved indication texts) can be retrieved from the **NPRA eBiz portal** (https://www.npra.gov.my/) by searching the active ingredient **"Amoxycillin"**.

---

## Safety Considerations

Safety data has not been populated in this Evidence Pack. Please refer to the approved Malaysian package insert for complete safety information.

Based on the well-established published literature, the following areas warrant attention during the formal safety review:

- **Hypersensitivity**: Penicillin-class allergy, including the risk of anaphylaxis, is the primary safety concern; cross-reactivity with cephalosporins should be assessed
- **Drug Interactions**: Clinically relevant interactions are well-described with warfarin (enhanced anticoagulant effect), methotrexate (reduced renal clearance), and combined oral contraceptives (theoretical reduced efficacy)
- **Contraindications**: Known hypersensitivity to penicillins or any beta-lactam antibiotic

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions are available in the current Evidence Pack, and the DrugBank ID — required as the primary model input — has not been confirmed. All downstream analysis (indication prediction, evidence collection, safety mapping) depends on completing these foundational data steps first.

**To proceed, the following is needed:**

- **Confirm DrugBank ID** (expected: DB01060) and retrieve full MOA data via the DrugBank API to resolve Data Gap DG002
- **Run TxGNN prediction pipeline** for Amoxycillin to generate ranked repurposing candidates
- **Download Malaysian package insert PDF** from the NPRA website and parse for warnings and contraindications, resolving Data Gap DG001
- **Retrieve complete licence details** from NPRA eBiz portal (product names, dosage forms, approved indication texts for all 66 registrations)
- **Once predictions are available**, re-run evidence collection from ClinicalTrials.gov and PubMed for the top-ranked predicted indications, then regenerate this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

