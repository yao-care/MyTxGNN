---
layout: default
title: Thiotepa
parent: Low Evidence (L4-L5)
nav_order: 645
evidence_level: L5
indication_count: 5
---

# Thiotepa
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **5** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Thiotepa: From Established Antineoplastic Use to Non-Papillary Transitional Cell Carcinoma of the Bladder

## One-Sentence Summary

Thiotepa is a classic aziridine-class alkylating antineoplastic agent; the current evidence pack does not capture its original indication text or detailed mechanism of action (both flagged as data gaps). TxGNN's top-ranked prediction is **non-papillary transitional cell carcinoma of the bladder**, but this candidate currently has **zero supporting clinical trials or publications** in the dataset. By contrast, two lower-ranked candidates — **Hodgkin's lymphoma** and **non-Hodgkin lymphoma** — are backed by **50 clinical trials and 20 publications each**, reflecting thiotepa's well-established role in high-dose stem-cell-transplant conditioning regimens.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in current dataset (TFDA/NPRA indication text not extracted) |
| Predicted New Indication | Non-papillary transitional cell carcinoma of the bladder (TxGNN rank 1) |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

### Other Candidate Indications in This Evidence Pack

Because this pack evaluates five TxGNN-predicted indications simultaneously, the top-ranked candidate above should be read alongside the others:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------|------|------|------|
| 1 | Non-papillary transitional cell carcinoma of the bladder | 0.00% | L5 | S0 | Hold |
| 2 | Ovarian clear cell adenocarcinoma | 0.00% | L3 | S1 | Research Question |
| 3 | Hodgkin's lymphoma | 0.00% | L2 | S2 | Proceed with Guardrails |
| 4 | Non-Hodgkin lymphoma | 0.00% | L2 | S2 | Proceed with Guardrails |
| 5 | Lymphosarcoma | 0.00% | L2 | S1 | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (TFDA/DrugBank MOA extraction is flagged as a High-severity data gap, DG002). Based on known pharmacology captured in the repurposing rationale fields, thiotepa is a cell-cycle non-specific alkylating agent that produces DNA cross-links; historically its label already included superficial bladder tumours (intravesical instillation), which is mechanistically consistent with the TxGNN top prediction of non-papillary transitional cell carcinoma of the bladder. However, no clinical trials, ICTRP registrations, or PubMed literature in this dataset currently substantiate that specific prediction — the mechanistic plausibility is not yet matched by real-world evidence.

The other four candidates cluster around two very different biological rationales. Ovarian clear cell adenocarcinoma is supported only by trials/literature conducted in unselected epithelial ovarian cancer populations, not the clear-cell subtype specifically — this subtype is relatively chemoresistant to platinum agents, so extrapolation from general ovarian cancer data should be treated cautiously. Hodgkin's lymphoma, non-Hodgkin lymphoma, and lymphosarcoma, on the other hand, reflect an already-mainstream clinical practice: thiotepa is a standard component of high-dose conditioning regimens (e.g., TBC: thiotepa-busulfan-cyclophosphamide; MATRix: methotrexate-cytarabine-thiotepa-rituximab) prior to autologous or allogeneic stem cell transplantation, valued particularly for its blood-brain-barrier penetration in CNS-involved lymphoma. Note that "lymphosarcoma" is an obsolete diagnostic term now largely subsumed under non-Hodgkin lymphoma, so its evidence base substantially overlaps with, rather than adds to, the NHL candidate.

## Clinical Trial Evidence

### Non-Papillary Transitional Cell Carcinoma of the Bladder (Rank 1)

Currently no related clinical trials registered

### Ovarian Clear Cell Adenocarcinoma (Rank 2)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002977](https://clinicaltrials.gov/study/NCT00002977) | Phase 1 | Completed | 45 | Melphalan + thiotepa followed by autologous/syngeneic PBSC rescue in Stage III/IV epithelial ovarian cancer in complete remission; not clear-cell-specific, endpoint was transplant feasibility/toxicity rather than subtype efficacy |

### Hodgkin's Lymphoma / Non-Hodgkin Lymphoma / Lymphosarcoma (Ranks 3–5, evidence bases overlap substantially)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01182415](https://clinicaltrials.gov/study/NCT01182415) | Phase 2 | Completed | 30 | High-dose thiotepa, busulfan, cyclophosphamide, rituximab + autologous SCT for CNS involvement by NHL or primary CNS lymphoma |
| [NCT06625359](https://clinicaltrials.gov/study/NCT06625359) | Phase 2 | Terminated | 17 | Thiotepa-busulfan-cyclophosphamide high-dose chemotherapy before autologous SCT for primary/secondary CNS lymphoma |
| [NCT00801216](https://clinicaltrials.gov/study/NCT00801216) | Phase 2 | Completed | 40 | High-dose sequential chemotherapy with rituximab (R-HDS), including thiotepa, for systemic B-cell lymphoma with CNS involvement |
| [NCT00143559](https://clinicaltrials.gov/study/NCT00143559) | Phase 2 | Completed | 17 | Haploidentical HSCT with partial T-cell depletion for hematologic malignancies; thiotepa part of conditioning |
| [NCT02790515](https://clinicaltrials.gov/study/NCT02790515) | Phase 2 | Active, not recruiting | 170 | Naive T-cell depleted haploidentical HCT for relapsed/refractory hematologic malignancies; thiotepa-containing reduced-intensity conditioning |
| [NCT00186823](https://clinicaltrials.gov/study/NCT00186823) | Phase 3 | Completed | 57 | Haploidentical SCT with purified CD34+ cells for hematologic malignancies; thiotepa as conditioning component |
| [NCT03509961](https://clinicaltrials.gov/study/NCT03509961) | Phase 2 | Recruiting | 95 | Non-TBI-based conditioning for MRD-negative B-ALL pre-allogeneic HCT; thiotepa-containing regimen |

## Literature Evidence

### Non-Papillary Transitional Cell Carcinoma of the Bladder (Rank 1)

Currently no related literature available

### Ovarian Clear Cell Adenocarcinoma (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19395997](https://pubmed.ncbi.nlm.nih.gov/19395997/) | 2009 | Cohort | Int J Gynecol Cancer | Survival after second-line intraperitoneal therapy for epithelial ovarian cancer; GOG experience, not subtype-specific |
| [9072220](https://pubmed.ncbi.nlm.nih.gov/9072220/) | 1996 | Cohort (older, non-English) | Likars'ka sprava | Morphological chemotherapy response study in ovarian carcinoma by histological type |

### Hodgkin's Lymphoma / Non-Hodgkin Lymphoma / Lymphosarcoma (Ranks 3–5)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27132696](https://pubmed.ncbi.nlm.nih.gov/27132696/) | 2016 | Phase 2 RCT (IELSG-32) | Lancet Haematology | MATRix regimen (methotrexate, cytarabine, thiotepa, rituximab) in primary CNS lymphoma; first randomisation results |
| [33513372](https://pubmed.ncbi.nlm.nih.gov/33513372/) | 2021 | Phase 2 trial (MARIETTA) | Lancet Haematology | MATRix-RICE + autologous HSCT in DLBCL with secondary CNS involvement |
| [38301670](https://pubmed.ncbi.nlm.nih.gov/38301670/) | 2024 | Phase 2 trial (MARTA) | Lancet Haematology | High-dose chemotherapy + autologous HSCT in older, fit patients with primary CNS DLBCL |
| [29035395](https://pubmed.ncbi.nlm.nih.gov/29035395/) | 2018 | Cohort | Bone Marrow Transplant | TECAM (thiotepa-based) vs. conventional BEAM conditioning in B-cell lymphoma ASCT, n=125 |
| [39937333](https://pubmed.ncbi.nlm.nih.gov/39937333/) | 2025 | Cohort | Int J Hematol | Thiotepa-busulfan conditioning vs. other regimens for relapsed/refractory systemic DLBCL ASCT |
| [23697844](https://pubmed.ncbi.nlm.nih.gov/23697844/) | 2014 | Cohort | Leuk Lymphoma | Busulfan-melphalan-thiotepa conditioning improves outcomes in relapsed/refractory Hodgkin lymphoma autoSCT (n=100) |
| [35459424](https://pubmed.ncbi.nlm.nih.gov/35459424/) | 2022 | Cohort | Leuk Lymphoma | High-dose thiotepa-busulfan-melphalan-rituximab conditioning improves outcomes in secondary CNS lymphoma (n=62) |
| [21928053](https://pubmed.ncbi.nlm.nih.gov/21928053/) | 2012 | Phase 1/2 report | Clin Exp Med | High-dose thiotepa-etoposide-carboplatin conditioning for autologous SCT in high-risk NHL |
| [37702537](https://pubmed.ncbi.nlm.nih.gov/37702537/) | 2023 | Review | Blood | "How I treat" secondary CNS involvement by aggressive lymphomas |
| [34271311](https://pubmed.ncbi.nlm.nih.gov/34271311/) | 2021 | Review | ESMO Open | "How we treat" primary CNS lymphoma |

## Malaysia Market Information

NPRA records confirm **3 active registrations** for Thiotepa (market status: Marketed), but the evidence pack does not include the individual license numbers, product names, dosage forms, or approved indication text for these registrations — this level of detail was not captured during data collection and needs to be sourced directly from NPRA/product package inserts before further use.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, aziridine/ethylenimine class) |
| Myelosuppression Risk | High — inferred from trial design: essentially every conditioning-regimen trial in this pack requires autologous or allogeneic stem cell rescue after thiotepa-based high-dose chemotherapy, indicating severe expected myeloablation |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, viral/fungal/bacterial infection surveillance (elevated infection risk reported after thiotepa-busulfan-cyclophosphamide conditioning), liver and renal function |
| Handling Protection | Yes — standard cytotoxic drug handling precautions apply as this is an alkylating antineoplastic agent |

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/NPRA package-insert warnings and contraindications are a **Blocking** data gap (DG001) — this must be resolved before any Stage 1 (S1) safety pre-assessment can proceed for the candidates currently at S1 or beyond (ovarian clear cell adenocarcinoma, Hodgkin's/non-Hodgkin lymphoma, lymphosarcoma).

## Conclusion and Next Steps

**Decision: Hold** (for the TxGNN top-ranked candidate, bladder cancer) — **Proceed with Guardrails** (for the lymphoma-conditioning candidates, as a secondary track)

**Rationale:**
- The model's top prediction (non-papillary bladder carcinoma) has no supporting trials or literature in this pack — mechanistically plausible but currently unverifiable, so it stays at Hold per the L5 evidence rule.
- The lymphoma candidates (Hodgkin's, non-Hodgkin) are supported by numerous completed Phase 2 trials and RCT-level literature (MATRix, MARIETTA, MARTA), but this reflects an already-established clinical use (transplant conditioning) rather than a novel repurposing signal — still useful for guardrail-based monitoring rather than a new-indication filing.
- Lymphosarcoma's evidence set duplicates the non-Hodgkin lymphoma results almost entirely due to obsolete-term mapping and should not be counted as independent corroboration.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, contraindications, and DDI data (Blocking gap, DG001)
- Confirmed mechanism of action from DrugBank (High-severity gap, DG002)
- Subtype-specific evidence for ovarian clear cell adenocarcinoma (current data is drawn from unselected epithelial ovarian cancer populations)
- De-duplication of the Hodgkin's/non-Hodgkin lymphoma/lymphosarcoma evidence sets before any formal evidence-level upgrade
- Original (pre-repurposing) indication text from NPRA licensing records, currently missing from this dataset
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

