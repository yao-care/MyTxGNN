---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 5
---

# Folic Acid
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

# Folic Acid: From Folate Deficiency to Microcytic Anemia

## One-Sentence Summary

Folic Acid (Vitamin B9) is a water-soluble vitamin classically used to treat and prevent folate-deficiency (megaloblastic) anemia. The TxGNN model's top-ranked prediction for this candidate is **Microcytic Anemia**, but the prediction carries a **TxGNN score of 0.00%** and is supported only by **2 loosely-related clinical trials** and **19 publications**, most of which do not evaluate folic acid directly against this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Folate deficiency / megaloblastic anemia (formal NPRA label text not available in this data pack) |
| Predicted New Indication | Microcytic Anemia |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 392 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Folic Acid is not available in this evidence pack. Based on known pharmacology, Folic Acid is a water-soluble B-vitamin required for one-carbon metabolism, DNA synthesis, and normal red blood cell maturation; its efficacy in correcting folate-deficiency anemia is well established.

However, the mechanistic fit between folic acid and **microcytic anemia** is weak and largely contradictory. Folate deficiency classically produces **macrocytic (megaloblastic)** anemia — enlarged red cells from impaired DNA synthesis — not microcytic anemia. Microcytic anemia is instead typically caused by iron deficiency, thalassemia trait, or anemia of chronic inflammation, none of which folic acid mechanistically addresses.

Consistent with this, the TxGNN model assigned a score of 0.0 to this prediction, indicating no meaningful model confidence in the link. The only literature reference describing folic acid in a "microcytic" context is a single 1948 case report of a rare, atypical folate-responsive anemia subtype — insufficient to establish a general mechanistic relationship. This candidate should be interpreted as a low-confidence/likely spurious model output rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06875947](https://clinicaltrials.gov/study/NCT06875947) | NA | Active, Not Recruiting | 59 | Evaluates Moringa oleifera leaf micronized powder (not folic acid) on hematological profile, hepcidin, and cytokines in pregnant women with iron deficiency anemia. Low relevance — folic acid is not the studied intervention. |
| [NCT05022979](https://clinicaltrials.gov/study/NCT05022979) | N/A | Completed | 341 | Observational study of micronutrient deficiency prevalence in pregnant women presenting with threatened delivery in French Guiana; non-interventional and not specific to microcytic anemia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27212091](https://pubmed.ncbi.nlm.nih.gov/27212091/) | 2016 | Review | Obstet Gynecol Clin North Am | States the three most common causes of microcytic anemia are iron deficiency, thalassemia trait, and anemia of inflammation — folate deficiency is explicitly associated with macrocytosis instead. |
| [10518398](https://pubmed.ncbi.nlm.nih.gov/10518398/) | 1999 | Review | Medicinski Pregled | Reviews anemia patterns (microcytic/macrocytic/normocytic) in hypothyroidism; not specific to folic acid therapy. |
| [26187724](https://pubmed.ncbi.nlm.nih.gov/26187724/) | 2015 | Cohort | J Formos Med Assoc | Assesses hematinic deficiencies in oral mucosal disease patients with folic acid deficiency (FAD); notes FAD may result in macrocytic, not microcytic, anemia. |
| [28291568](https://pubmed.ncbi.nlm.nih.gov/28291568/) | 2017 | Cohort | J Formos Med Assoc | Assesses anemia status and hematinic deficiencies in 240 patients with microcytosis; evaluates multiple hematinic causes, not folic acid treatment specifically. |
| [18103537](https://pubmed.ncbi.nlm.nih.gov/18103537/) | 1948 | Case Report | Minerva Medica | Historic case report describing folic acid response in two cases of microcytic, hypochromic, agastric anemia — the only literature directly linking folic acid to microcytic anemia, but a single rare case series. |
| [26045325](https://pubmed.ncbi.nlm.nih.gov/26045325/) | 2015 | Review | Ann Nutr Metab | Epidemiology of global micronutrient deficiencies (iron, iodine, folate, vitamin A, zinc); broad context, not disease-specific. |
| [11681780](https://pubmed.ncbi.nlm.nih.gov/11681780/) | 2001 | — | Am Fam Physician | General overview of anemia classification by MCV in children; identifies iron deficiency as the most common microcytic cause. |
| [39954228](https://pubmed.ncbi.nlm.nih.gov/39954228/) | 2025 | — | Indian J Gastroenterol | Comprehensive review of anemia in IBD; folate deficiency listed as one of several contributing causes alongside iron deficiency and chronic disease. |
| [40178543](https://pubmed.ncbi.nlm.nih.gov/40178543/) | 2025 | — | Innere Medizin | Practice-oriented rational assessment of anemia etiologies; general diagnostic framework, not folic acid-specific. |
| [19787825](https://pubmed.ncbi.nlm.nih.gov/19787825/) | 2009 | — | World J Gastroenterol | Classification of anemia (microcytic/macrocytic/normocytic) for gastroenterologists; general reference, not an efficacy study. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted link between folic acid and microcytic anemia is mechanistically inconsistent (folate deficiency causes macrocytic, not microcytic, anemia), the TxGNN score is 0.00%, and the supporting evidence consists only of a single 1948 case report and non-specific reviews. This does not meet the threshold to advance past initial screening (S0).

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications, approved indication text) — currently a blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank
- If pursuing folic acid repurposing further, evaluate the higher-evidence candidates already identified in this pack (e.g., "folic acid deficiency anemia," evidence level L1, though this reflects the drug's known original indication rather than a novel use; or "vitamin deficiency disorder," evidence level L3) rather than microcytic anemia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

