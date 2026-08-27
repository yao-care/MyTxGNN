---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 534
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase (DrugBank DB00059) is a pegylated asparaginase already established as a core component of acute lymphoblastic leukemia (ALL) therapy internationally, per the literature captured in this evidence pack. The TxGNN model's top prediction — **precursor lymphoblastic lymphoma/leukemia** — is the same disease family as this established use rather than a genuinely new indication, and is backed by **50 clinical trials** (including multiple Phase 3 studies with thousands of patients) and **20 publications**. This is best read as a validation of the model rather than a novel repurposing opportunity; see the caveat below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (per literature evidence in this pack, e.g. PMID 31030380, 30823860; NPRA/Malaysia formal label text not yet retrieved — data gap) |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

**⚠️ Important caveat**: "Precursor lymphoblastic lymphoma/leukemia" is clinically synonymous with/overlapping the drug's own well-established indication (ALL/lymphoblastic lymphoma). The evidence pack's own rationale for this candidate states this is "not a speculative link but the core, already-established mechanism of asparaginase-class drugs," and the parallel candidate at rank 5 ("acute lymphoblastic leukemia," also L1/S3) is explicitly flagged as "a duplicate of an already-approved use, not a repurposing hypothesis." Treat this as confirmation of model validity rather than a new market opportunity, pending regulatory clarification of what Malaysia's current label actually covers.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this pack (marked as a data gap, DG002). Based on the literature evidence collected alongside this candidate, pegaspargase is a pegylated *E. coli*-derived L-asparaginase that depletes circulating asparagine. Lymphoblasts in precursor B/T-cell ALL and lymphoblastic lymphoma characteristically lack asparagine synthetase and cannot synthesize their own asparagine, so systemic depletion selectively starves and kills these malignant cells while sparing most normal tissue.

Because this biochemical vulnerability is the defining feature of precursor lymphoblastic malignancies, the TxGNN prediction is mechanistically well-founded rather than a distant repurposing hypothesis — it converges with pegaspargase's existing global indication for ALL. This is corroborated by the scale of clinical evidence: dozens of completed and ongoing Phase 3 trials in pediatric and adult B-ALL/T-ALL and lymphoblastic lymphoma consistently use pegaspargase as a backbone agent.

By contrast, several other predictions in this evidence pack for related-sounding but biologically distinct entities (e.g., CLL/SLL subtypes, follicular lymphoma, classical Hodgkin lymphoma, methylcobalamin deficiency) lack asparagine-synthetase deficiency and have zero or mismatched supporting evidence — these should be treated with far more skepticism than this top candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9,350 | Risk-adapted chemotherapy regimens for newly diagnosed standard-risk B-ALL / localized B-lineage lymphoblastic lymphoma; pegaspargase is standard-of-care component |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6,136 | International collaborative treatment protocol for children/adolescents with ALL, comparing combination chemotherapy regimens |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Head-to-head comparison of calaspargase pegol vs. pegaspargase (Oncaspar) in high-risk pediatric ALL |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Active, not recruiting | 6,720 | Blinatumomab added to chemotherapy (incl. pegaspargase) for newly diagnosed standard-risk B-ALL / B-LLy |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Phase 3 | Recruiting | 5,951 | Inotuzumab ozogamicin added to risk-adapted post-induction therapy for high-risk B-ALL |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2,044 | French pediatric/adolescent ALL protocol optimizing L-asparaginase (ASNase) dosing strategy |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | Completed | 600 | Total Therapy XVI: high-dose vs. conventional-dose PEG-asparaginase during continuation therapy |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | Completed | 650 | NOPHO protocol comparing intermittent vs. continuous PEG-asparaginase dosing for asparagine depletion |
| [NCT02013167](https://clinicaltrials.gov/study/NCT02013167) | Phase 3 | Terminated | 405 | TOWER study: blinatumomab vs. standard chemotherapy in relapsed/refractory B-precursor ALL |
| [NCT00506597](https://clinicaltrials.gov/study/NCT00506597) | N/A | Completed | 33 | Erwinia asparaginase (Erwinase) as replacement therapy for patients allergic to E. coli/pegylated asparaginase |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231 Phase III trial testing bortezomib in newly diagnosed T-ALL/T-lymphoblastic lymphoma |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001: efficacy/toxicity of pegaspargase vs. calaspargase pegol in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Advances | GIMEMA LAL1913: pegaspargase-modified risk-oriented program for adult Ph-negative ALL/LL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert panel consensus on recognizing/preventing/managing pegaspargase-associated adverse events in adults |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review | Blood | "How I treat" review of pegaspargase toxicities in adult ALL |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Comprehensive review of pegaspargase's role in ALL treatment |
| [21454191](https://pubmed.ncbi.nlm.nih.gov/21454191/) | 2011 | Cohort | Clin Lymphoma Myeloma Leuk | Augmented hyper-CVAD with dose-intensified vincristine/dexamethasone/asparaginase in adult ALL salvage therapy |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Review of PEG-asparaginase pharmacology and clinical role in acute leukemia |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Review | Ann Pharmacother | Early review of pegaspargase chemistry, pharmacology, and clinical activity |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Cohort | Int J Hematol | Phase 2 multicenter study of pegaspargase in Japanese patients with untreated ALL |

---

## Malaysia Market Information

Malaysia market status is confirmed as **Marketed (已上市)** with **1 registered license**. However, the license record in this evidence pack has no populated detail fields (license/registration number, product name, dosage form, or approved indication text) — this is part of the blocking data gap (DG001) noted below and needs to be pulled directly from NPRA before further use.

---

## Cytotoxicity

Pegaspargase is a cytotoxic antineoplastic agent (asparagine-depleting enzyme used as chemotherapy for lymphoblastic malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — antimetabolic enzyme therapy (asparagine-depleting agent), distinct from DNA-damaging cytotoxics |
| Myelosuppression Risk | Low–Moderate as a single agent; asparaginase is not itself primarily myelosuppressive, but risk rises when combined with vincristine/corticosteroids/anthracyclines in standard ALL regimens (per combination-trial evidence above) |
| Emetogenicity Classification | Low to Moderate (general asparaginase-class characterization; NPRA-specific package insert data not available — data gap) |
| Monitoring Items | CBC with differential; liver function (AST/ALT/bilirubin) — hepatotoxicity is well documented in the literature above; coagulation panel (fibrinogen, PT/INR) — thrombosis/bleeding risk; lipase/amylase — pancreatitis risk; triglycerides and glucose — hypertriglyceridemia/hyperglycemia risk; close monitoring for hypersensitivity during/after infusion |
| Handling Protection | Must follow institutional cytotoxic/hazardous drug handling protocols (PPE, spill precautions) as with other antineoplastic agents |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data for pegaspargase were not returned by the NPRA/DrugBank queries in this pack (query_status: not_found). This is flagged in the evidence pack as a **Blocking** data gap (DG001 — "TFDA 仿單警語/禁忌"), explicitly noted as preventing entry into the S1 safety pre-screening stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is exceptionally strong (asparagine depletion → selective lymphoblast killing) and is backed by L1-level evidence (multiple completed/ongoing Phase 3 RCTs, thousands of patients). However, this candidate largely overlaps with pegaspargase's already-known indication rather than representing a novel repurposing opportunity, and a **blocking safety data gap** (DG001) currently prevents formal safety pre-screening.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the NPRA/Malaysia package insert for warnings, contraindications, and DDI data — required before S1 safety review can begin
- Resolve DG002 (High): query DrugBank API for confirmed mechanism of action data
- Pull complete NPRA license details (registration number, product name, dosage form, full approved indication text) to replace the currently empty license record
- Clarify with the regulatory/clinical team whether "precursor lymphoblastic lymphoma/leukemia" already falls under Malaysia's existing approved indication for this product, since this materially changes whether this is a repurposing case at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

