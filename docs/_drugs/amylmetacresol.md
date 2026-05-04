---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Throat Infections to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol (AMC) is a phenolic antiseptic used as an active ingredient in over-the-counter throat lozenges for the relief of sore throat and minor oral/pharyngeal infections.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome** (top-ranked indication), alongside 9 other predicted conditions spanning ocular anterior segment diseases and systemic functional disorders.
However, **no clinical trials or published literature** currently support any of the 10 predictions — all are rated at evidence level **L5** — and mechanistic analysis consistently identifies these as likely knowledge graph artefacts rather than genuine drug–disease relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Sore throat / Pharyngitis (topical oral antiseptic; detailed NPRA registration data unavailable in current dataset) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological information, Amylmetacresol is a cresol-class phenolic compound whose antimicrobial activity arises from disruption of bacterial cell membranes and surface protein denaturation, conferring broad-spectrum antibacterial and mild antifungal effects. Its clinical use is restricted to the topical oral route — typically as a lozenge ingredient (e.g., Strepsils) — for symptomatic management of sore throat, pharyngitis, and minor mouth infections. Systemic bioavailability is negligible by design.

Cauda equina syndrome (CES), the top-ranked predicted indication, is a neurosurgical emergency caused by acute mechanical compression of the lumbosacral nerve roots, typically managed with urgent decompressive surgery. There is no known biological pathway connecting AMC's antiseptic membrane-disruption mechanism to the pathophysiology of CES. The Evidence Pack's own mechanistic analysis explicitly identifies the high TxGNN score as probable **knowledge graph indirect-association noise** — possibly arising via infection-related neurological damage pathways — rather than a true mechanistic signal.

Across all 10 predicted indications, two recurring clusters emerge: (1) **ocular anterior segment diseases** (ciliary body disease, panuveitis, iris disease, infectious anterior uveitis, uveitis, ciliary body cancer, benign neoplasm of ciliary body) and (2) **unrelated systemic / functional conditions** (cauda equina syndrome, neurogenic bladder, irritable bowel syndrome). This bimodal clustering pattern — with scores converging between 0.9945 and 0.9999 — is a recognised signature of **systematic ontology node over-association** within the TxGNN knowledge graph, not independent mechanistic evidence. Among the 10 predictions, infectious anterior uveitis carries the most tenuous (yet still speculative) biological link, as AMC's antibacterial properties could theoretically apply to bacterial anterior uveitis if a suitable ophthalmic formulation existed — but no such formulation or safety data exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered across all 10 predicted indications.

---

## Literature Evidence

Currently no related literature available across all 10 predicted indications.

---

## Malaysia Market Information

Amylmetacresol has **20 registered products** in Malaysia. However, individual registration details (authorization numbers, product names, dosage forms, and approved indication text) were not returned in the current dataset.

> **Note:** AMC is typically marketed as a component of OTC throat lozenge formulations. Complete authorization records may be retrieved directly from the [NPRA Malaysia Product Search](https://www.npra.gov.my/) portal for full regulatory due diligence.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are rated L5 (model prediction only), zero supporting clinical or preclinical evidence was retrieved across all 30 evidence queries, and mechanistic analysis consistently identifies absent or implausible biological rationale connecting AMC's topical antiseptic mechanism to the predicted conditions. The observed prediction clustering strongly suggests systematic knowledge graph over-association rather than actionable repurposing opportunities.

**To proceed, the following is needed:**

- **Mechanism of action data**: Retrieve comprehensive MOA from DrugBank (DrugBank ID currently null) to enable formal mechanistic plausibility assessment for any candidate indication
- **NPRA registration details**: Download full product information (approved indications, dosage forms, package inserts) from the Malaysia NPRA database to complete the regulatory baseline — this is classified as a **Blocking** data gap (DG001)
- **Safety data**: Obtain package insert warnings and contraindications from NPRA or manufacturer to enable S1 safety screening — also **Blocking** (DG001)
- **Targeted preclinical literature review**: If any indication is to be advanced, the highest-priority candidate is **infectious anterior uveitis** (Rank 7); a focused search for any in vitro antibacterial ophthalmic data on AMC should be conducted before further investment
- **Knowledge graph audit**: Assess whether the observed ocular disease cluster and the high-score / zero-evidence pattern across all 10 predictions represents a systematic false-positive bias requiring TxGNN model recalibration or ontology node correction prior to further AMC analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

