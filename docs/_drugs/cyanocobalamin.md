---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 5
---

# Cyanocobalamin
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Microcytic Anemia

## One-Sentence Summary

Cyanocobalamin is the synthetic form of vitamin B12, established as replacement therapy for vitamin B12 deficiency states (pernicious anemia, malabsorption, dietary deficiency). The TxGNN model's top-ranked candidate is **microcytic anemia**, but with a **prediction score of 0.0** and only **2 clinical trials** and **20 publications** returned — none of which directly support a B12-microcytic anemia link, and the mechanistic rationale in the evidence pack itself flags this as a poor fit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency (megaloblastic/pernicious anemia) — established core indication; not captured in the sampled Malaysia license records (all 5 sampled entries are blank) |
| Predicted New Indication | Microcytic Anemia |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 428 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, DrugBank MOA query pending). Based on known pharmacology, cyanocobalamin is a synthetic vitamin B12 analog used as a cofactor-replacement therapy — its efficacy in vitamin B12 deficiency and pernicious anemia is well established and forms the drug's original/core indication.

However, the mechanistic case for microcytic anemia is weak. B12 deficiency classically causes **macrocytic/megaloblastic** anemia (elevated MCV) through impaired DNA synthesis in erythroid precursors — the opposite morphology of **microcytic** anemia, which is driven primarily by iron deficiency, thalassemia trait, or chronic disease. The evidence pack's own scoring reflects this: the TxGNN model assigned a prediction score of **0.0** (no model confidence), and the supporting clinical trials retrieved (oral iron supplementation studies, a general micronutrient-deficiency survey in pregnant women) are iron-focused and do not test cyanocobalamin as an intervention.

Given this mismatch, the mechanistic plausibility for this specific candidate is low, and the evidence pack's internal recommendation for this indication is **Hold**.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05022979](https://clinicaltrials.gov/study/NCT05022979) | N/A | Completed | 341 | Prevalence survey of micronutrient deficiencies in pregnant women (French Guiana); not a B12 intervention, not specific to microcytic anemia |
| [NCT05185024](https://clinicaltrials.gov/study/NCT05185024) | N/A | Completed | 152 | Comparison of three oral iron-containing supplements for correcting mild microcytic anemia; unrelated to cyanocobalamin's mechanism |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26926814](https://pubmed.ncbi.nlm.nih.gov/26926814/) | 2016 | Review | American Family Physician | Iron deficiency is the most common cause of microcytic anemia in infants/children |
| [8930231](https://pubmed.ncbi.nlm.nih.gov/8930231/) | 1996 | Review | Archives of Family Medicine | Combined iron + cobalamin deficiency anemia; RBC morphology varies with relative degree of each deficiency |
| [27212091](https://pubmed.ncbi.nlm.nih.gov/27212091/) | 2016 | Pending classification | Obstet Gynecol Clin North Am | MCV-based anemia classification: B12/folate deficiency causes macrocytosis, not microcytosis |
| [28291568](https://pubmed.ncbi.nlm.nih.gov/28291568/) | 2017 | Pending classification | J Formos Med Assoc | Anemia and hematinic deficiencies in oral mucosal disease patients with microcytosis |
| [28972879](https://pubmed.ncbi.nlm.nih.gov/28972879/) | 2017 | Pending classification | Discovery Medicine | Challenging clinical presentations of pernicious anemia |
| [33906782](https://pubmed.ncbi.nlm.nih.gov/33906782/) | 2021 | Pending classification | J Formos Med Assoc | B12 deficiency and anemia in 140 Taiwanese lacto-vegetarian women |
| [39954228](https://pubmed.ncbi.nlm.nih.gov/39954228/) | 2025 | Pending classification | Indian J Gastroenterol | Review of anemia in IBD; B12/folate deficiency listed among etiologies |
| [28314600](https://pubmed.ncbi.nlm.nih.gov/28314600/) | 2017 | Pending classification | J Formos Med Assoc | Anemia/hematinic deficiencies in GPCA+/- microcytosis patients |
| [36105468](https://pubmed.ncbi.nlm.nih.gov/36105468/) | 2022 | Pending classification | Heliyon | Magnitude and morphological types of anemia in under-five children |
| [37258053](https://pubmed.ncbi.nlm.nih.gov/37258053/) | 2023 | Pending classification | Comparative Medicine | Severe anemia in rats after Roux-en-Y gastric bypass |

None of the above literature directly demonstrates cyanocobalamin efficacy in microcytic anemia; most describe iron deficiency as the dominant cause or discuss B12 deficiency in the context of macrocytic/pernicious anemia instead.

---

## Malaysia Market Information

Malaysia registration data confirms the product is marketed (428 total registrations), but the sampled license records returned by the query contain no populated fields (license number, product name, dosage form, manufacturer, and approved indication text are all blank). Detailed authorization-level information is not currently available and requires re-query against the source registry.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings and contraindications are flagged as a **blocking data gap** — DG001 — pending retrieval and parsing of the official product insert; no drug-drug interaction records were found in the current query.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigned this candidate a prediction score of 0.0, and both the mechanistic rationale and retrieved evidence point to a morphological mismatch — vitamin B12 deficiency classically causes macrocytic, not microcytic, anemia. The supporting clinical trials involve iron supplementation rather than cyanocobalamin, and no literature directly evaluates cyanocobalamin efficacy in microcytic anemia. Additionally, a blocking safety data gap (TFDA/NPRA warnings and contraindications) prevents this candidate from advancing to initial safety review regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain and parse the official Malaysia product insert for warnings/contraindications
- Resolve DG002: obtain mechanism of action data from DrugBank
- Re-query Malaysia license records to obtain populated product/authorization details (current sample is entirely blank)
- Note for portfolio review: the same evidence pack shows **vitamin B12 deficiency** (rank 3, evidence level L1, decision stage S3, recommendation "Proceed with Guardrails") as a much stronger-evidence candidate — but this is the drug's already-established core indication rather than a novel repurposing target, and should be treated as a scope/coverage question rather than a new indication filing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

