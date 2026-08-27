---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 512
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Obinutuzumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

Obinutuzumab is a humanized, glycoengineered type II anti-CD20 monoclonal antibody; trial-registry evidence in this pack identifies chronic lymphocytic leukemia (CLL) as its original approved indication.
The TxGNN model's top-ranked scored candidate is **Follicular Lymphoma**, supported by **50 clinical trials** (including 2 completed Phase 3 RCTs) and **19 publications**, making it the only decision-ready candidate in this pack.
*Note: TxGNN's two highest-ranked raw predictions (score 0.9921) are molecular sub-classifications of CLL/SLL — "IGHV-mutated CLL/SLL" and "pregerminal center CLL/SLL" — neither has any clinical trial or literature support (L5, decision stage S0, recommendation Hold), and both are prognostic/cell-of-origin labels rather than clinically actionable new indications. This report focuses on Follicular Lymphoma, the highest-scoring candidate with substantive evidence.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL) — referenced in trial-registry text within this evidence pack (NCT02877550); not recorded in the local NPRA license record, which is a data gap |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank/registry mechanism-of-action record is not available for obinutuzumab in this evidence pack (flagged as data gap DG002). Based on the mechanistic annotations included with the TxGNN predictions, obinutuzumab is a humanized, glycoengineered **type II anti-CD20 monoclonal antibody**. It clears CD20-positive B cells primarily through antibody-dependent cellular cytotoxicity (ADCC), antibody-dependent cellular phagocytosis (ADCP), and direct (non-apoptotic) cell death induction — a mechanism distinct from complement-dependent cytotoxicity, which dominates for type I anti-CD20 antibodies such as rituximab.

CLL and Follicular Lymphoma are both CD20-positive B-cell malignancies, so the mechanistic link is direct rather than inferential. This is corroborated by the literature and trial evidence within this pack itself: obinutuzumab has already received international regulatory approval for previously untreated FL (GALLIUM study, PMID 28976863, NEJM 2017) and for rituximab-refractory FL (in combination with bendamustine, PMID 28324270). In other words, FL is not a purely speculative repurposing target — it is a mechanistically consistent, clinically established indication for the same drug class/molecule, which is reflected in the L1 evidence level assigned here.

Because the drug-level MOA and safety fields are formally missing (DG001, DG002), the mechanistic description above should be treated as derived from the evidence pack's trial/literature annotations rather than a verified regulatory MOA statement, and should be confirmed against an authoritative source (e.g., DrugBank record or package insert) before clinical use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Completed | 1401 | GALLIUM trial: obinutuzumab + chemotherapy vs. rituximab + chemotherapy, with maintenance, in previously untreated advanced indolent NHL (predominantly FL) |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Completed | 413 | Bendamustine alone vs. bendamustine + obinutuzumab (GA101) in rituximab-refractory indolent NHL (GADOLIN) |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | ROSEWOOD: randomized trial of zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Recruiting | 190 | GAZEBO: local radiotherapy alone vs. combined with obinutuzumab in early-stage FL |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | EPCORE FL-2: epcoritamab + rituximab/lenalidomide vs. chemoimmunotherapy in previously untreated FL |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | Recruiting | 780 | Zanubrutinib + obinutuzumab vs. lenalidomide + rituximab in relapsed/refractory FL or marginal zone lymphoma |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A | Recruiting | 332 | Real-world efficacy and safety of obinutuzumab-based therapy in previously untreated FL |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | Completed | 133 | Obinutuzumab + polatuzumab vedotin + venetoclax in relapsed/refractory FL |
| [NCT03980171](https://clinicaltrials.gov/study/NCT03980171) | Phase 1/2 | Active, not recruiting | 50 | Lenalidomide + venetoclax + obinutuzumab in treatment-naïve FL |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | Recruiting | 36 | Obinutuzumab + CC-99282 in previously untreated, high tumor-burden FL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | GALLIUM primary results: obinutuzumab-based chemotherapy vs. rituximab-based chemotherapy for first-line FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM sub-analysis: impact of chemotherapy backbone (CHOP/CVP/bendamustine) on obinutuzumab efficacy and safety |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM final analysis: durable PFS benefit of obinutuzumab- vs. rituximab-based immunochemotherapy in FL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN: obinutuzumab + lenalidomide in relapsed/refractory FL |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood and Lymphatic Cancer: Targets and Therapy | Overview of obinutuzumab alone and in combination for FL |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish Journal of Haematology | Comprehensive review of FL staging, prognosis, and treatment including anti-CD20 therapy |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Review of obinutuzumab in rituximab-refractory/relapsed FL, including GADOLIN results |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology (Williston Park) | Current and emerging therapies for FL |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Frontiers in Pharmacology | Rapid review of efficacy, safety, and cost-effectiveness of obinutuzumab in FL |

---

## Malaysia Market Information

The NPRA registry confirms **1 active marketing authorization** for obinutuzumab (market status: Marketed), but the underlying record's authorization number, product name, dosage form, and approved indication text are not populated in this evidence pack. This is a data gap that should be resolved directly against the NPRA product register before finalizing local indication mapping.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (humanized, glycoengineered type II anti-CD20 monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Formal toxicity data is not available in this evidence pack; trial-registry text (NCT04918940) notes prolonged B-cell depletion and hypogammaglobulinemia as a known class effect of anti-CD20 maintenance therapy |
| Emetogenicity Classification | Low (monoclonal antibodies are generally minimally emetogenic; not formally classified in available data) |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not available in this evidence pack (data gap DG001, blocking severity).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (GALLIUM, GADOLIN) plus a substantial body of Phase 2 and real-world evidence support obinutuzumab's efficacy in Follicular Lymphoma, and the drug already holds international approval for this indication elsewhere — evidence strength is high (L1). However, local Malaysia (NPRA) license details and formal drug-level safety/MOA data are missing, so this cannot proceed without guardrails.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — resolves blocking data gap DG001
- DrugBank-verified mechanism-of-action record — resolves data gap DG002
- Complete local NPRA license record (authorization number, product name, dosage form, approved indication text)
- DDI screening specific to obinutuzumab given its immunosuppressive/B-cell-depleting profile (e.g., HBV reactivation risk, live vaccine contraindications) once safety data is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

