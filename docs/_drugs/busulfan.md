---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Leukemia/HSCT-Conditioning Agent to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a classic bifunctional alkylating agent long used for chronic myeloid leukemia and, more broadly, as the core alkylating agent in myeloablative/reduced-intensity conditioning regimens prior to allogeneic hematopoietic stem cell transplantation (allo-HSCT). The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, with **50 clinical trials** and **20 publications** currently supporting this direction — though, as detailed below, this largely reflects an *already-established* standard-of-care use rather than a novel pharmacological hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in NPRA license records (approved indication text field is empty — see Data Gap DG001). Busulfan is classically an alkylating agent for chronic myeloid leukemia and is widely used as a myeloablative/reduced-intensity conditioning agent before allo-HSCT |
| Predicted New Indication | Myelodysplastic Syndrome |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Busulfan was not retrieved in this evidence pack (Data Gap DG002, severity High). Based on established pharmacological knowledge, Busulfan is a bifunctional alkylating agent (alkyl sulfonate class) that forms DNA cross-links, producing potent and durable myelosuppression. This cytotoxic effect on the bone marrow is deliberately exploited — at myeloablative or reduced-intensity doses, Busulfan (typically combined with fludarabine, cyclophosphamide, or melphalan) is used to eradicate the recipient's own hematopoietic and malignant/dysplastic clone immediately before allo-HSCT, creating the "space" and immunologic conditions needed for donor stem cells to engraft.

Importantly, the repurposing rationale captured in this evidence pack is explicit that Busulfan does **not** treat MDS through a new or speculative mechanism: it is not a direct disease-modifying therapy for MDS, but rather the conditioning backbone of a transplant procedure that is already the standard curative approach for eligible higher-risk MDS patients. In other words, TxGNN's "prediction" here largely re-identifies an already well-documented, guideline-supported clinical use rather than surfacing a genuinely novel indication.

This is corroborated by the depth of the evidence base: 50 clinical trials and 20 publications spanning three decades (from NCT00002547, 1987, through NCT06247917, 2024) consistently studying Busulfan-containing conditioning regimens (Bu/Cy, Bu/Flu, Bu/Mel, Bu/Flu/ATG, etc.) specifically in MDS and MDS-related AML populations undergoing allo-HSCT. Several of these are large, completed, randomized Phase 2/3 or Phase 3 trials, which is why the evidence level is rated L1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | Randomized comparison of G-CSF+decitabine+Busulfan/Cyclophosphamide vs Busulfan/Cyclophosphamide conditioning for RAEB-1, RAEB-2, and MDS-secondary AML undergoing allo-HSCT (Grade A relevance) |
| [NCT00475020](https://clinicaltrials.gov/study/NCT00475020) | Phase 2 | Completed | 63 | Reduced-intensity Busulfan + Fludarabine + ATG conditioning for myelofibrosis/MDS patients undergoing allo-HSCT (Grade A relevance) |
| [NCT01471444](https://clinicaltrials.gov/study/NCT01471444) | Phase 3 | Completed | 256 | Randomized trial: Fludarabine-Clofarabine vs Fludarabine alone, both combined with IV Busulfan, before allo-HSCT for AML/MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | G-CSF+DAC+BUCY vs G-CSF+DAC+BF conditioning regimens compared in high-risk MDS patients undergoing allo-HSCT |
| [NCT00629798](https://clinicaltrials.gov/study/NCT00629798) | Phase 2 | Completed | 64 | Busulfan + Melphalan + Fludarabine with peri-transplant Palifermin for T-cell depleted HSCT in advanced MDS/AML (Grade B relevance) |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | Completed | 68 | Addition of azacitidine to Busulfan/Fludarabine/ATG reduced-intensity conditioning for high-risk MDS and older AML patients |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Completed | 47 | G-CSF and Plerixafor with Busulfan and Fludarabine for allo-HSCT in AML, MDS, and CML |
| [NCT00002502](https://clinicaltrials.gov/study/NCT00002502) | Phase 2 | Completed | N/A | Busulfan + Cyclophosphamide cytoreduction for leukemias and MDS undergoing allo-BMT when total-body irradiation cannot be used |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | Unknown | 59 | FLU-BU-MEL conditioning regimen for allo-HSCT in untreated MDS-EB / IPSS-R intermediate-to-very-high-risk patients |
| [NCT01062490](https://clinicaltrials.gov/study/NCT01062490) | Phase 2 | Completed | 45 | Treosulfan + Fludarabine conditioning benchmarked against historical IV Busulfan outcomes in MDS patients undergoing allo-HSCT |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (Phase 3) | The Lancet Haematology | Non-inferiority trial: Treosulfan+Fludarabine vs reduced-intensity Busulfan+Fludarabine conditioning in older/comorbid AML/MDS patients undergoing allo-HSCT |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (Phase 3) | The Lancet Haematology | Open-label, multicentre, randomised trial: G-CSF+decitabine+Busulfan/Cyclophosphamide reduces relapse vs Busulfan/Cyclophosphamide alone in MDS-RAEB/secondary AML undergoing allo-HSCT |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (Phase 3) | Journal of Clinical Oncology | Randomized trial comparing myeloablative vs reduced-intensity conditioning (including Busulfan-based regimens) for AML/MDS allo-HSCT |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Cohort (final RCT analysis) | American Journal of Hematology | Final analysis confirming Treosulfan-based conditioning improves outcomes versus reduced-intensity Busulfan in older AML/MDS patients |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic Review/Meta-analysis | Frontiers in Oncology | Meta-analysis of Treosulfan- vs Busulfan-based conditioning regimens showing comparable/favorable long-term outcomes in MDS/AML |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | Contemporary review of allogeneic HSCT for myelofibrosis and MDS, discussing Busulfan-based conditioning strategies |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohort (registry, PS-matched) | Bone Marrow Transplantation | Propensity-matched comparison of Fludarabine/Busulfan vs Busulfan/Cyclophosphamide myeloablative conditioning for MDS |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Cohort (registry, PS-matched) | Transplantation and Cellular Therapy | Propensity-matched comparison of myeloablative vs reduced-intensity Fludarabine/Busulfan conditioning for MDS |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Cohort (retrospective, PS-matched) | Transplantation and Cellular Therapy | Single-center retrospective study: Treosulfan- vs Busulfan-based conditioning outcomes in MDS/CMML allo-HSCT |
| [23562738](https://pubmed.ncbi.nlm.nih.gov/23562738/) | 2013 | Cohort (retrospective) | Biology of Blood and Marrow Transplantation | Busulfan dose-intensity (3.2 vs 6.4 mg/kg) and outcomes in reduced-intensity allo-HSCT for MDS/AML |

---

## Malaysia Market Information

NPRA records confirm Busulfan is currently marketed in Malaysia (market status: ✓ Marketed) under **2 active registrations**. However, this query did not return the specific authorization number, product name, dosage form, or approved indication text for either registration (Data Gap DG001, severity: **Blocking** — this gap blocks progression to the S1 safety pre-assessment stage noted in the evidence pack metadata).

**Recommended action:** Retrieve the full NPRA product label/insert (via the NPRA QUEST3+ portal) to confirm the exact approved indication wording, available dosage forms/routes (oral vs IV), and manufacturer(s) before this candidate proceeds further.

---

## Cytotoxicity

Busulfan is a conventional cytotoxic alkylating agent and is classified here as antineoplastic (Category 3: known cytotoxic chemotherapy class — alkyl sulfonate).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent — alkyl sulfonate class) |
| Myelosuppression Risk | High — profound, dose-dependent, and often prolonged myelosuppression is the intended pharmacologic effect when Busulfan is used as a myeloablative/reduced-intensity conditioning agent before HSCT |
| Emetogenicity Classification | High at myeloablative/HSCT-conditioning (IV) doses; low-to-moderate at low oral doses historically used for chronic myeloid leukemia |
| Monitoring Items | CBC with differential; hepatic function (risk of hepatic veno-occlusive disease/sinusoidal obstruction syndrome); pulmonary function (risk of pulmonary fibrosis with cumulative exposure); seizure prophylaxis (Busulfan lowers seizure threshold — anticonvulsant prophylaxis is standard); therapeutic drug monitoring of plasma Busulfan levels for IV formulations |
| Handling Protection | Yes — Busulfan must be handled under cytotoxic/hazardous drug handling regulations (PPE, closed-system transfer devices, spill kits) |

*Note: DrugBank-sourced detailed MOA/toxicity data was not retrieved in this evidence pack (Data Gap DG002). The classification above reflects established pharmacological knowledge for this drug class; confirm specifics against the current package insert.*

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not returned by the current queries — see Data Gap DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The clinical trial and literature base for Busulfan-based conditioning in MDS is extensive and mature — 50 trials and 20 publications, including at least two completed randomized Phase 2/3–3 trials (NCT01471444, NCT02744742) and multiple Phase 3 RCTs in the literature (PMID 31606445, 36702138, 28380315) — supporting an L1 evidence level.
- However, this predicted "new indication" substantially overlaps with an already-established standard-of-care role (HSCT conditioning agent) rather than representing a novel disease-modifying use; any external communication should frame it as reinforcing existing clinical practice, not as a new therapeutic claim.
- Drug-level safety data (package insert warnings/contraindications) and detailed MOA remain unresolved data gaps (DG001 Blocking, DG002 High) that must be closed before a full safety (S1) assessment can be completed.

**To proceed, the following is needed:**
- Retrieve the NPRA-approved package insert/label text for Busulfan (resolves DG001 — currently blocking)
- Retrieve DrugBank MOA, toxicity, and drug-interaction details (resolves DG002)
- Confirm actual dosage forms/routes registered in Malaysia (oral vs IV) against the routes required for HSCT conditioning use
- Clarify messaging so the MDS "prediction" is presented as supporting an established conditioning-regimen role rather than a de novo indication

**Other predicted indications in this evidence pack (for context, not actioned here):** Refractory cytopenia of childhood (L2, Research Question) and unclassified MDS (L3, Research Question) are directionally consistent with the MDS signal above but have thinner evidence. Five candidates — 5q- deletion syndrome, severe congenital sideroblastic anemia, HIV infection, a rare neurodevelopmental disorder, and seborrheic keratosis, plus simian immunodeficiency virus infection — returned no clinical trial or literature support (L5, Hold) and, per the evidence pack's own annotations, several (seborrheic keratosis, SIV infection) are likely knowledge-graph noise rather than genuine repurposing signals; none warrant further investment without new independent evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

