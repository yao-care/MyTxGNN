---
layout: default
title: Apalutamide
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 0
---

# Apalutamide
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

# Apalutamide: Androgen Receptor Inhibitor — Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

Apalutamide (Erleada®) is a non-steroidal androgen receptor (AR) signaling inhibitor approved for prostate cancer treatment, currently marketed in Malaysia under one registered licence.
However, **the current Evidence Pack contains no TxGNN-predicted new indications**, and critical data fields — including approved indication text, mechanism of action details, and safety warnings — are absent or incomplete.
As a result, **a full repurposing evaluation cannot be completed at this stage**; the recommended decision is **Hold** pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (based on known pharmacological class; approved indication text not retrieved from this Evidence Pack) |
| Predicted New Indication | — No TxGNN prediction available |
| TxGNN Prediction Score | — Not applicable |
| Evidence Level | L5 (model prediction not available; no supporting studies retrievable from this pack) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN-predicted new indication is present in the Evidence Pack (`predicted_indications: []`). Therefore, a mechanistic repurposing hypothesis cannot be formally evaluated at this time.

For background context: Apalutamide is a small-molecule androgen receptor inhibitor that binds directly to the ligand-binding domain of AR, blocking nuclear translocation, DNA binding, and transcriptional activation of androgen-responsive genes. It belongs to the same pharmacological class as enzalutamide and darolutamide. Its established efficacy in hormone-sensitive and castration-resistant prostate cancer is well documented in the SPARTAN and TITAN Phase 3 trials.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Pending completion of DrugBank MOA data retrieval (Data Gap DG002) and TxGNN scoring, a formal mechanistic bridge to any candidate new indication cannot be constructed.

---

## Clinical Trial Evidence

No TxGNN-predicted indication is available; therefore, targeted clinical trial evidence cannot be retrieved from the Evidence Pack.

Currently no related clinical trials are linked to a repurposing prediction for this candidate.

---

## Literature Evidence

Currently no related literature is available for a repurposing prediction in this Evidence Pack.

---

## Malaysia Market Information

The Evidence Pack confirms 1 registered licence in Malaysia; however, all licence detail fields (licence number, product name, dosage form, manufacturer, approved indication text) were returned as empty strings and could not be populated.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — (not retrieved) | — (not retrieved) | — (not retrieved) | — (not retrieved) |

> **Action required**: Download the NPRA product registration record to populate all licence fields.

---

## Cytotoxicity

Apalutamide is an **antiandrogen / androgen receptor signaling inhibitor** — it is classified as a targeted antineoplastic agent, not a conventional cytotoxic.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — non-steroidal androgen receptor inhibitor (not a conventional cytotoxic/DNA-damaging agent) |
| Myelosuppression Risk | Low (AR inhibitors do not typically cause significant myelosuppression; haematological monitoring still recommended) |
| Emetogenicity Classification | Minimal to low |
| Monitoring Items | CBC, liver function tests (LFTs), thyroid function (hypothyroidism reported), falls/fracture risk assessment, seizure history |
| Handling Protection | Follows standard oral antineoplastic handling precautions; avoid crushing tablets; use gloves when handling |

---

## Safety Considerations

Key warnings and contraindications were not retrievable from the current Evidence Pack (Data Gap DG001 — TFDA package insert not parsed). No drug–drug interaction data was found in the DDI query.

Please refer to the approved Malaysian package insert and the Erleada® prescribing information for complete safety information, including:

- Seizure risk (particularly in patients with predisposing factors)
- Falls and fractures
- Cardiovascular events
- Hypothyroidism
- Embryo-foetal toxicity (contraindicated in females of reproductive potential)
- Strong CYP3A4 and CYP2C19 induction (clinically significant DDI potential, despite `not_found` status in automated DDI query — manual review is essential)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Apalutamide (DB11901) is currently insufficient to support a repurposing evaluation: the `predicted_indications` array is empty, approved indication text was not retrieved, mechanism of action data is absent, and safety warnings/contraindications have not been parsed. No recommendation can be made without at minimum a TxGNN prediction score and a candidate new indication.

**To proceed, the following is needed:**

- [ ] **DG001 (Blocking)** — Download and parse the TFDA/NPRA package insert PDF to extract approved indication text, key warnings, and contraindications
- [ ] **DG002 (High)** — Query DrugBank API to retrieve mechanism of action (MOA) for DB11901
- [ ] **Re-run TxGNN prediction pipeline** — Confirm that Apalutamide (DB11901) is included in the KG prediction run and that `repurposing_candidates.csv` contains scored disease candidates
- [ ] **Populate licence details** — Retrieve full NPRA registration record (licence number, product name, dosage form, manufacturer)
- [ ] **Manual DDI review** — Despite the automated `not_found` result, Apalutamide is a potent CYP3A4/2C19/P-gp inducer; a manual DDI review against common co-medications is required before any repurposing protocol is initiated
- [ ] **Re-generate Evidence Pack** — Once DG001 and DG002 are resolved and TxGNN predictions are available, reissue Evidence Pack v5 for full evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

