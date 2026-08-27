---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: From B-Cell Chronic Lymphocytic Leukemia to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine nucleoside analog historically used against B-cell chronic lymphocytic leukemia (CLL) and related indolent B-cell malignancies (regulatory-specific indication text was not returned in this data pull; this framing is drawn from the surrounding literature).
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma**, with **0 clinical trials** and **20 publications** currently associated with this pairing — but most of that literature describes fludarabine's role as a lymphodepleting/transplant-conditioning agent rather than a direct antimyeloma treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory data provided; literature context indicates B-cell chronic lymphocytic leukemia (CLL) and related indolent lymphoid malignancies |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Malaysia Market Status | 已上市 (Marketed) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Fludarabine in this evidence pack (`original_moa: [Data Gap]`). Based on the surrounding literature, fludarabine is a purine nucleoside analog that inhibits DNA polymerase and ribonucleotide reductase, producing both cytotoxic and profound immunosuppressive/lymphodepleting effects. This dual property is what links it to plasma cell myeloma in the TxGNN knowledge graph: fludarabine is a core component of reduced-intensity conditioning (RIC) regimens before allogeneic stem cell transplant and of lymphodepletion regimens before BCMA/CD19 CAR‑T cell infusion — both of which are used in relapsed/refractory multiple myeloma.

However, the evidence pack's own relevance grading is candid about a limitation: in nearly all 20 associated publications, fludarabine appears as an adjunctive immunosuppressive/conditioning agent enabling transplant or CAR‑T engraftment, not as a direct antimyeloma therapy in its own right. Only one study — a 2007 in vitro/in vivo report (PMID 17976186) — directly tested fludarabine's cytotoxic activity against myeloma cells, showing growth inhibition of the RPMI8226 myeloma cell line via reduced Akt/NF‑κB signaling. No clinical trial in this dataset was designed to test fludarabine as a standalone or combination antimyeloma agent. The mechanistic link is therefore plausible but indirect, and the model's high similarity score likely reflects fludarabine's dense co-occurrence with myeloma in transplant/CAR-T contexts rather than a validated direct pharmacologic effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (0 trials returned for the Fludarabine × Plasma Cell Myeloma query; see `query_log` id 3–4).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical (in vitro/in vivo) | European Journal of Haematology | Fludarabine directly inhibited growth of the RPMI8226 myeloma cell line, with decreased Akt phosphorylation — the only direct evidence of intrinsic antimyeloma cytotoxicity in this dataset |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Early report | European Journal of Haematology | Early clinical description of fludarabine activity in plasma cell leukemia, a myeloma-related entity |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 (Cohort) | American Journal of Clinical Oncology | Bortezomib + fludarabine + melphalan (± total marrow irradiation) as allogeneic HSCT conditioning for high-risk/relapsed myeloma — fludarabine used as immunosuppressive conditioning, not a standalone antitumor agent |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohort | Blood Cancer Journal | Compared bendamustine vs. fludarabine/cyclophosphamide lymphodepletion before BCMA CAR-T in multiple myeloma — fludarabine's role limited to pre-CAR-T lymphodepletion |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 (small cohort) | Leukemia Research Reports | Split-dose busulfan/fludarabine/cyclophosphamide as allogeneic SCT conditioning for myeloma and myelofibrosis (2 MM patients enrolled) |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective cohort | Bone Marrow Transplantation | Fludarabine + treosulfan reduced-toxicity conditioning before allogeneic SCT in 34 myeloma patients |
| [33784005](https://pubmed.ncbi.nlm.nih.gov/33784005/) | 2021 | Phase 1 | Clinical and Translational Medicine | Anti-BCMA CAR-T in relapsed/refractory MM and plasma cell leukemia; fludarabine/cyclophosphamide used for lymphodepletion prior to CAR-T infusion |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohort | Blood | Standard-of-care outcomes with ciltacabtagene autoleucel (cilta-cel) in R/R MM across 16 US centers; fludarabine-based conditioning typically precedes CAR-T infusion |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nature Medicine | First-in-human Phase 1 UNIVERSAL trial of allogeneic anti-BCMA CAR-T (ALLO-715) in R/R MM following lymphodepletion conditioning |
| [31058154](https://pubmed.ncbi.nlm.nih.gov/31058154/) | 2019 | Review | Frontiers in Medicine | Review of [18F]-fludarabine PET imaging for hematological malignancy staging — a diagnostic imaging application, not a therapeutic one |

---

## Malaysia Market Information

Malaysia NPRA records confirm **2 marketed registrations** for Fludarabine (market status: 已上市/Marketed), but the authorization number, product name, dosage form, and approved indication text for these registrations were not returned in this data pull — both license records in the evidence pack contain empty fields.

---

## Cytotoxicity

Fludarabine is a conventional cytotoxic chemotherapeutic agent (purine nucleoside antimetabolite), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must be handled per institutional cytotoxic/hazardous drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (DDI query returned no results), and TFDA/NPRA label warnings are flagged as a **Blocking** data gap (DG001) that must be resolved before any safety evaluation (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The plasma cell myeloma prediction is supported only by indirect evidence — fludarabine's established role as a lymphodepletion/conditioning agent for transplant and CAR-T procedures in myeloma, plus a single 2007 preclinical study showing direct antitumor activity. No clinical trial in this dataset tests fludarabine as an antimyeloma therapy, and the blocking safety data gap (DG001 — TFDA/NPRA label warnings and contraindications) prevents any progression to safety review.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications) to resolve DG001 before any S1 safety evaluation
- Confirmed mechanism of action data (DG002) via DrugBank to clarify whether fludarabine's antimyeloma activity is a genuine pharmacologic effect or an artifact of its conditioning-agent co-occurrence
- A study specifically testing fludarabine (alone or in combination) as an antimyeloma agent, rather than as transplant/CAR-T conditioning
- Complete Malaysia licence records (authorization number, product name, dosage form, approved indication text) for the 2 registered products

**Note:** within this same drug's prediction set, two other candidates carry materially stronger evidence — myelodysplastic syndrome (rank 7: L1, decision stage S3, "Proceed with Guardrails") and indolent plasma cell myeloma (rank 4: L2, decision stage S2, "Proceed with Guardrails") — and may warrant separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

