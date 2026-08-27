---
layout: default
title: Iron
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 5
---

# Iron
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

# Iron: From Iron Deficiency to Microcytic Anemia

## One-Sentence Summary

Iron (DrugBank DB01592) is an essential mineral and hematinic agent broadly used to treat and prevent iron-deficiency states. The TxGNN model predicts it may be directly effective for **Microcytic Anemia**, with **13 clinical trials** and **20 publications** currently supporting this direction — though microcytic anemia can also arise from non-iron-deficiency causes (e.g. thalassemia), so differential diagnosis remains essential before treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency (general hematinic/replacement indication; specific NPRA-approved label text was not available in this data extract) |
| Predicted New Indication | Microcytic Anemia |
| TxGNN Prediction Score | 0.00% (as recorded in this data extract) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 80 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Iron is a core hematinic agent — a cofactor essential for heme synthesis and hemoglobin production — and its efficacy in correcting iron deficiency has been proven for decades across oral and intravenous formulations; mechanistically this same iron-repletion action may be directly applicable to microcytic anemia.

Microcytic anemia is, in the large majority of cases, caused by iron deficiency itself. Iron supplementation is therefore not so much a "new" indication as the direct etiological treatment of the most common subtype of this condition — the mechanistic link is immediate and well-established rather than inferential.

That said, microcytic anemia is a morphological classification, not a single disease: it can also result from non-iron-deficiency causes such as thalassemia trait, sideroblastic anemia, or anemia of chronic disease, none of which respond to (and may even be worsened by) iron therapy. Several of the trials identified below concern differentiating iron-deficiency anemia from thalassemia rather than treating it — this distinction should be built into any clinical guardrails for this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06252103](https://clinicaltrials.gov/study/NCT06252103) | Phase 4 | Completed | 40 | Lactoferrin + ferrous gluconate vs. ferrous gluconate alone for iron deficiency anemia in pregnancy |
| [NCT06670963](https://clinicaltrials.gov/study/NCT06670963) | Phase 4 | Recruiting | 200 | Epoetin alfa + iron derisomaltose for anemia in ICU patients with sepsis/septic shock |
| [NCT03212781](https://clinicaltrials.gov/study/NCT03212781) | Phase 3 | Completed | 66 | Total-dose IV iron dextran vs. oral iron for iron deficiency anemia in pregnant women |
| [NCT05185024](https://clinicaltrials.gov/study/NCT05185024) | N/A | Completed | 152 | 12-week comparison of three oral iron formulations for correcting iron status and mild microcytic anemia |
| [NCT03202615](https://clinicaltrials.gov/study/NCT03202615) | Phase 4 | Unknown | 130 | Bovine lactoferrin vs. ferrous sulphate for iron deficiency anemia in pregnancy |
| [NCT03771092](https://clinicaltrials.gov/study/NCT03771092) | N/A | Completed | 148 | Comparison of sucrosomal ferric pyrophosphate, SunActive Fe, and IV ferric gluconate for sideropenic microcytic hypochromic anemia |
| [NCT04713943](https://clinicaltrials.gov/study/NCT04713943) | N/A | Completed | 94 | Double-blind, placebo-controlled trial of iron syrup in children with iron deficiency ± mild microcytic anemia |
| [NCT03868306](https://clinicaltrials.gov/study/NCT03868306) | N/A | Unknown | 100 | RDW Index vs. RDW as a discriminating tool between iron deficiency anemia and beta-thalassemia trait |
| [NCT03822585](https://clinicaltrials.gov/study/NCT03822585) | N/A | Unknown | 100 | Detection of β-thalassemia carriers among relatives of thalassemia children — differential diagnosis relevance, not an iron-therapy trial |
| [NCT00481221](https://clinicaltrials.gov/study/NCT00481221) | N/A | Unknown | 30000 | Automated red-cell-parameter method to detect β-thalassemia carriers — differential diagnosis relevance, not an iron-therapy trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36725875](https://pubmed.ncbi.nlm.nih.gov/36725875/) | 2023 | RCT | Scientific Reports | Alternate-day vs. daily oral iron dosing for iron deficiency anemia — alternate-day dosing showed comparable/better efficacy with improved absorption |
| [39519457](https://pubmed.ncbi.nlm.nih.gov/39519457/) | 2024 | Guideline/Review | Nutrients | Polish multi-society recommendations on diagnosis and treatment of iron deficiency and iron deficiency anemia in children and adolescents |
| [39985323](https://pubmed.ncbi.nlm.nih.gov/39985323/) | 2025 | Expert Opinion | British Journal of Haematology | Treatment guidance for iron-refractory iron deficiency anaemia (IRIDA), a rare hereditary microcytic anemia unresponsive to oral iron |
| [35289581](https://pubmed.ncbi.nlm.nih.gov/35289581/) | 2022 | Review | American Family Physician | Rapid evidence review of alpha- and beta-thalassemia, emphasizing distinction from iron-deficiency microcytic anemia |
| [22942439](https://pubmed.ncbi.nlm.nih.gov/22942439/) | 2012 | Review | Canadian Veterinary Journal | Overview of iron deficiency anemia pathophysiology, presenting as microcytic, hypochromic anemia |
| [38960649](https://pubmed.ncbi.nlm.nih.gov/38960649/) | 2024 | Review | Rinsho Ketsueki | Diagnosis and treatment of iron deficiency anemia, including atrophic gastritis and TMPRSS6-related refractory cases |
| [26935626](https://pubmed.ncbi.nlm.nih.gov/26935626/) | 2016 | Review | Rinsho Ketsueki | Iron-refractory iron deficiency anemia: causes including menstrual loss, H. pylori infection, and TMPRSS6 mutations |
| [17375513](https://pubmed.ncbi.nlm.nih.gov/17375513/) | 2007 | Review | American Family Physician | Epidemiology and clinical management of iron deficiency anemia, including screening recommendations |
| [25271605](https://pubmed.ncbi.nlm.nih.gov/25271605/) | 2014 | Review | New England Journal of Medicine | Clinical review of microcytic anemia diagnosis and management |
| [9166144](https://pubmed.ncbi.nlm.nih.gov/9166144/) | 1997 | Review | American Family Physician | Differential diagnosis of microcytic anemia, distinguishing iron deficiency from chronic disease and thalassemia |

## Malaysia Market Information

Iron is registered with NPRA under **80 total authorizations**, confirming established market presence in Malaysia. However, product-level details (authorization numbers, product names, dosage forms, and approved indication text) were not populated in this data extract and cannot be reported without fabricating values.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Iron's role in correcting iron-deficiency-driven microcytic anemia is mechanistically direct and supported by an L1 evidence level, including Phase 3/4 RCT data (NCT03212781, NCT06252103, NCT06670963). However, since microcytic anemia can also stem from non-iron-deficiency causes (notably thalassemia), guardrails requiring confirmatory iron-status testing before treatment are warranted.

**To proceed, the following is needed:**
- NPRA package insert data (key warnings/contraindications) — currently blocking (DG001)
- DrugBank mechanism-of-action documentation — currently a high-severity gap (DG002)
- Malaysia product-level license details (brand names, dosage forms, specific approved indication text)
- A diagnostic guardrail requiring exclusion of thalassemia/non-iron-deficiency causes prior to treatment under this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

