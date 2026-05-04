---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 8
---

# Chlorambucil
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

# Chlorambucil: From Chronic Lymphocytic Leukemia to CLL/SLL with IGHV Somatic Hypermutation

## One-Sentence Summary

Chlorambucil is a well-established alkylating agent with a long history of use as frontline therapy for chronic lymphocytic leukemia (CLL) and related B-cell lymphoid malignancies. The TxGNN model predicts it may be effective for **CLL/SLL with immunoglobulin heavy-chain variable-region gene (IGHV) somatic hypermutation** — a molecularly defined, favorable-prognosis subtype — with the current targeted evidence search returning **0 clinical trials** and **0 publications** specifically addressing this molecular subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Malaysian regulatory record (license details not captured at time of extraction) |
| Predicted New Indication | CLL/SLL with IGHV somatic hypermutation |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (no subtype-specific studies retrieved) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from DrugBank at the time of this report. Based on known pharmacology, chlorambucil is a nitrogen mustard–derived alkylating agent. It forms covalent cross-links between and within DNA strands, effectively halting DNA replication and transcription. This cytotoxic mechanism is particularly effective against proliferating lymphocytes, which explains the drug's decades-long use as a first-line therapy in B-cell lymphoid malignancies including CLL.

CLL/SLL is biologically stratified into two major subtypes based on the mutational status of the immunoglobulin heavy-chain variable region (IGHV) gene. Tumour cells carrying IGHV somatic hypermutation — the predicted indication here — are derived from post-germinal centre B cells and typically show a more indolent disease course and better response to conventional chemoimmunotherapy. Chlorambucil-based regimens (e.g., chlorambucil + obinutuzumab, chlorambucil + rituximab) have been validated in Phase 3 trials enrolling CLL patients broadly, with meaningful response rates observed across IGHV-mutated cohorts in subgroup analyses.

The TxGNN prediction therefore reflects a mechanistically coherent and clinically plausible scenario. Chlorambucil's well-characterised B-cell cytotoxicity aligns with the biology of IGHV-mutated CLL, which remains sensitive to DNA-damaging agents. The high TxGNN score (99.72%) likely reflects strong pathway connectivity between chlorambucil's known targets and the molecular drivers of this CLL subtype in the knowledge graph. However, no dedicated prospective studies specifically enrolling IGHV-mutated CLL as a distinct stratum were retrieved in this evidence pack, which limits formal evidence grading.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for CLL/SLL with IGHV somatic hypermutation specifically.

> **Contextual note:** Three completed Phase 3 trials involving chlorambucil in CLL broadly were identified in a parallel search query within this evidence pack. These include a randomised study of lenalidomide versus chlorambucil as first-line therapy in elderly B-CLL patients (NCT00910910; n=450), a safety evaluation of obinutuzumab with or without chemotherapy in previously untreated or relapsed/refractory CLL (NCT01905943; n=979), and a head-to-head comparison of alemtuzumab versus chlorambucil as frontline therapy in progressive B-CLL (NCT00046683; n=284). While none of these prospectively stratified by IGHV status as a primary endpoint, they establish a substantial Phase 3 evidence base for chlorambucil in CLL overall and may contain subgroup data relevant to IGHV-mutated disease.

---

## Literature Evidence

Currently no related literature available for CLL/SLL with IGHV somatic hypermutation specifically.

> **Contextual note:** One publication retrieved under the closely related rank-2 prediction (pregerminal centre CLL/SLL) describes the discovery of two distinct CLL subtypes — the IGHV-unmutated pre-germinal centre type and the IGHV-mutated post-germinal centre type — and discusses risk-adapted treatment approaches (PMID [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/), *Ned Tijdschr Geneeskd*, 2003). This paper directly contextualises the biological basis of the rank-1 prediction.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | — |

The Malaysian regulatory record confirms **1 active registration** for chlorambucil (market status: marketed). However, detailed product information — including the MAL authorization number, product name, dosage form, and approved indication text — was not captured in the data extracted at the time of this report. These details can be retrieved directly from the NPRA product search portal.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent — Nitrogen mustard class) |
| Myelosuppression Risk | High — dose-dependent bone marrow suppression; neutropenia, thrombocytopenia, and anaemia are common and may be cumulative with repeated cycles |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (CBC with differential) before each cycle and at nadir; liver function tests; renal function; monitoring for secondary malignancy with long-term use |
| Handling Protection | Must comply with cytotoxic drug handling regulations; oral tablet/capsule formulation requires caregiver education on safe handling, storage, and disposal |

---

## Safety Considerations

Please refer to the package insert for safety information.

> The safety data fields (key warnings, contraindications, and drug–drug interactions) were all identified as data gaps in this evidence pack. The NPRA-approved product monograph should be obtained and reviewed before any clinical or formulary decision is made. Known class-level concerns for alkylating agents include myelosuppression, secondary leukaemia risk with prolonged use, teratogenicity, and carcinogenicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or publications specifically addressing chlorambucil in the molecularly defined subtype *CLL/SLL with IGHV somatic hypermutation* were retrieved, resulting in an L5 evidence level for this prediction. Although extensive Phase 3 evidence exists for chlorambucil in CLL broadly — and the mechanistic rationale is sound — the IGHV-mutated subtype has not been independently validated as a distinct treatment target in this evidence pack.

**To proceed, the following is needed:**

- **Subgroup data extraction:** Obtain IGHV-mutated subgroup analyses from existing Phase 3 chlorambucil-in-CLL trials (e.g., CLL11 obinutuzumab study, RESONATE-2 comparator arm) to determine whether the benefit–risk profile holds specifically for this molecular subset.
- **MOA data completion:** Retrieve full DrugBank entry for chlorambucil (DB00291) to complete mechanistic link analysis and confirm pathway plausibility at the molecular level.
- **Safety documentation:** Download the NPRA-approved Malaysian product monograph (仿單) to extract approved indication text, warnings, contraindications, and dosing recommendations; this is a blocking prerequisite for the S1 safety screening stage.
- **Regulatory review:** Assess whether the IGHV-mutated CLL subtype would require a new indication filing or falls within the scope of the existing Malaysian approval; consult NPRA guidance on precision oncology label extensions.
- **Market intelligence:** Clarify the current therapeutic landscape in Malaysia — whether BTK inhibitors (ibrutinib, acalabrutinib) or BCL-2 inhibitors (venetoclax) have displaced chlorambucil as standard of care, which would affect the repurposing value proposition.

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application to patient care.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

