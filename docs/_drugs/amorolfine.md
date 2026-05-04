---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Amorolfine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Amorolfine: From Onychomycosis to Drug-Induced Osteoporosis

## One-Sentence Summary

Amorolfine is a topical antifungal agent of the morpholine class, primarily used for the treatment of onychomycosis (fungal nail infections) by disrupting the fungal cell membrane through inhibition of ergosterol biosynthesis.
The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction rests entirely on model output, placing it at Evidence Level **L5** — the lowest tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infections) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Amorolfine belongs to the morpholine class of antifungals. It works by inhibiting two key fungal enzymes — Δ14-reductase and Δ7-Δ8-isomerase — in the ergosterol biosynthesis pathway. This causes toxic sterol intermediates to accumulate in the fungal cell membrane, ultimately leading to cell death. Critically, this pathway is specific to fungi and does not exist in mammalian cells.

The proposed link to drug-induced osteoporosis is mechanistically weak. Bone metabolism in humans is governed by the balance between osteoblasts (bone formation) and osteoclasts (bone resorption), a process that has no known connection to ergosterol biosynthesis. A superficial analogy might be drawn to certain azole antifungals (e.g., voriconazole), which have been associated with periostitis and bone abnormalities — however, that effect is mediated by systemic CYP450 inhibition and fluoride accumulation, a mechanism entirely inapplicable to amorolfine. Amorolfine is administered exclusively as a topical nail lacquer with negligible systemic absorption, meaning it cannot exert systemic pharmacological effects on bone tissue.

In summary, while the TxGNN model assigned a high prediction score (likely reflecting structural or graph-embedding proximity in the knowledge graph), no biologically plausible pathway currently connects amorolfine's antifungal mechanism to drug-induced osteoporosis. This prediction should not be advanced without first identifying a credible mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Amorolfine has **3 registered products** with NPRA in Malaysia (market status: Marketed). Detailed product information — including authorization numbers, product names, dosage forms, and approved indication text — has not yet been populated in this Evidence Pack. This data should be retrieved directly from the NPRA product search portal.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| *(Pending retrieval)* | *(Pending retrieval)* | *(Pending retrieval)* | *(Pending retrieval)* |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings and contraindications have been flagged as data gaps in this Evidence Pack (severity: Blocking and High respectively). Full safety review cannot proceed until the NPRA package insert (SmPC) has been downloaded and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported solely by a TxGNN model prediction (Evidence Level L5) with zero registered clinical trials and zero published literature. Furthermore, the mechanistic link between amorolfine's fungal-specific ergosterol inhibition and drug-induced osteoporosis is not biologically plausible — the drug has negligible systemic exposure, and the proposed target pathway does not exist in mammalian bone tissue.

**To proceed, the following is needed:**
- Retrieve full NPRA registration details (authorization numbers, product names, dosage forms, approved indications) for all 3 registered products
- Download and parse the NPRA package insert PDF to populate safety data (key warnings, contraindications) — currently a **Blocking** data gap
- Query DrugBank API (DB09056) to obtain the complete mechanism of action (MOA) — currently a **High** severity data gap
- Conduct a broader preclinical literature search to determine whether any morpholine-class compounds (beyond antifungals) have demonstrated bone metabolism activity
- If any preclinical signal emerges, design a targeted in vitro study before considering clinical advancement
- Re-evaluate the prediction rationale: if no mechanistic link can be established after the above steps, formally close this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

