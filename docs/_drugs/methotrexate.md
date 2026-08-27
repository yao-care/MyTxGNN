---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 477
evidence_level: L5
indication_count: 5
---

# Methotrexate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Methotrexate: From Malignant Neoplasms to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Methotrexate is a folate antagonist historically used as a component of antineoplastic and immunosuppressive regimens; specific original-indication text is not recorded in the current NPRA data extract.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm** (head and neck cancer).
No clinical trials are currently registered specifically for this indication, but **20 publications** — including a Phase 3 RCT and a Phase II trial — document methotrexate's historical use in this cancer type.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current NPRA registration extract |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 0.00% (as reported — score field returned 0.0 for all ranked candidates; likely an incomplete model export) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for methotrexate is not available in the structured drug record (MOA field flagged as a data gap). Based on the mechanistic rationale associated with this specific prediction, methotrexate's antifolate mechanism — inhibiting dihydrofolate reductase and thereby blocking purine/pyrimidine synthesis — can suppress rapidly proliferating cells in upper aerodigestive tract squamous cell carcinoma.

Historically, methotrexate has been used as monotherapy or within combination regimens (e.g., MTX-vinblastine-cisplatin, MTX-vinblastine-bleomycin) for head and neck squamous cell carcinoma. The mechanistic link is established and supported by older clinical trials, though modern standard-of-care has shifted toward platinum-based chemotherapy combined with immunotherapy; methotrexate today is used mainly in recurrent or palliative settings for this tumor type. This shift explains why supporting evidence is concentrated in older literature rather than active trial registrations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2419292](https://pubmed.ncbi.nlm.nih.gov/2419292/) | 1986 | RCT | Int J Radiat Oncol Biol Phys | Randomized trial of induction chemotherapy (bleomycin + methotrexate) vs. standard therapy in 83 patients with locally advanced Stage III–IV upper aerodigestive tract squamous cell carcinoma |
| [12001121](https://pubmed.ncbi.nlm.nih.gov/12001121/) | 2002 | Phase II Trial | Cancer | MVAC regimen (methotrexate, vinblastine, doxorubicin, cisplatin) evaluated for antitumor activity and toxicity in recurrent/metastatic head and neck squamous cell carcinoma |
| [7198935](https://pubmed.ncbi.nlm.nih.gov/7198935/) | 1981 | Cohort | Cancer Treat Rep | High-dose oral methotrexate (250 mg divided doses q2 weeks) in 9 patients; 2 partial responses in head and neck squamous carcinoma |
| [16299796](https://pubmed.ncbi.nlm.nih.gov/16299796/) | 2005 | Cohort | J Surg Oncol | Radiochemotherapy with vinblastine, methotrexate, and bleomycin explored as an alternative to surgery in verrucous carcinoma of the head and neck |
| [632138](https://pubmed.ncbi.nlm.nih.gov/632138/) | 1978 | Review | Int J Radiat Oncol Biol Phys | Review of methotrexate combined with radiation therapy |
| [2299365](https://pubmed.ncbi.nlm.nih.gov/2299365/) | 1990 | Review | J Clin Oncol | Review of leucovorin rescue in high-dose methotrexate therapy |
| [91591](https://pubmed.ncbi.nlm.nih.gov/91591/) | 1978 | Review | Head Neck Surg | Methotrexate identified as the best single agent (≈50% response rate) for advanced head and neck cancer previously treated with surgery/radiation |
| [36269850](https://pubmed.ncbi.nlm.nih.gov/36269850/) | 2023 | Review | Cancer Investigation | Mechanistic review of low-dose methotrexate + celecoxib as metronomic chemotherapy for oral squamous cell carcinoma |
| [30509741](https://pubmed.ncbi.nlm.nih.gov/30509741/) | 2019 | Review | Lancet | Review of PD-1 antibodies in head and neck cancer (context for methotrexate's evolving role) |
| [28759389](https://pubmed.ncbi.nlm.nih.gov/28759389/) | 2017 | Case Report | Lancet Oncol | Case report: "Tumour d'emblee" |

---

## Malaysia Market Information

Detailed registration-level data (authorization numbers, product names, dosage forms, approved indication text) is not available in the current NPRA extract — all license record fields returned empty. Malaysia market status is confirmed as **Marketed**, with **6 total registrations** on file.

---

## Cytotoxicity

Methotrexate is an antimetabolite (antifolate) chemotherapeutic agent, historically used in cytotoxic combination regimens for head and neck malignancies, warranting cytotoxicity assessment.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite / antifolate — dihydrofolate reductase inhibitor) |
| Myelosuppression Risk | High, particularly with high-dose regimens — literature on related indications documents grade ≥3 mucositis and cytopenias requiring active monitoring |
| Emetogenicity Classification | Low-to-moderate at conventional oral/low-dose regimens; moderate-to-high with high-dose IV administration |
| Monitoring Items | CBC with differential, renal function (creatinine clearance), liver function, serum methotrexate levels (especially for high-dose regimens), mucositis assessment |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is sound and historically supported by one Phase 3 RCT and one Phase II trial in upper aerodigestive tract cancer, but no active clinical trials currently target this specific indication, and modern practice has moved past methotrexate as a primary regimen for this tumor type — evidence is meaningful but dated.

**To proceed, the following is needed:**
- Confirmed original indication and NPRA license details (current extract has empty fields)
- Detailed mechanism of action (MOA) data for methotrexate
- TFDA/NPRA package insert warnings, contraindications, and drug interaction data (currently unavailable)
- Clarification of the TxGNN prediction score, which returned 0.0 across all candidates
- Updated evidence review to confirm whether methotrexate has a role alongside current platinum/immunotherapy-based standards of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

