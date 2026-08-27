---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cholecalciferol: From Vitamin D Deficiency to Renal Osteodystrophy

> **Note on candidate selection**: This evidence pack contains 7 TxGNN-predicted indications for cholecalciferol (ranks 1–7). The highest-scoring candidate (familial isolated hypoparathyroidism, 99.79%) is flagged by its own generated rationale as mechanistically backwards (patients with impaired PTH secretion typically need active vitamin D/calcitriol, not the cholecalciferol precursor) and has zero supporting trials or literature. Ranks 2–4 are similarly unsupported (model noise on rare genetic syndromes). This report therefore centers on **renal osteodystrophy** (rank 6, L2 evidence), the candidate with the strongest direct clinical-trial support for cholecalciferol itself. A summary of all 7 candidates follows the Quick Overview.

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a nutritional secosteroid used to prevent and treat vitamin D deficiency and related bone disorders. The TxGNN model predicts a repurposing signal toward **Renal Osteodystrophy** (CKD-associated mineral and bone disorder), a use already partially reflected in clinical guidelines and supported by **32 clinical trials** and **20 publications**, several of which test cholecalciferol directly in CKD populations.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the TFDA/NPRA license extract (all license fields returned blank). Per established pharmacology, cholecalciferol is indicated for prevention and treatment of vitamin D deficiency and nutritional rickets/osteomalacia. |
| Predicted New Indication | Renal Osteodystrophy |
| TxGNN Prediction Score | 99.11% (rank 11,477 overall) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 800 |
| Recommended Decision | Proceed with Guardrails |

### Other Predicted Indications Considered

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------|------|------|
| 1 | Familial isolated hypoparathyroidism (impaired PTH secretion) | 99.79% | L4 | Research Question |
| 2 | Acromesomelic dysplasia, Campailla Martinelli type | 99.78% | L5 | Hold |
| 3 | Craniofacial conodysplasia | 99.75% | L5 | Hold |
| 4 | Dahlberg-Borer-Newcomer syndrome | 99.73% | L5 | Hold |
| 5 | Hypophosphatemic rickets | 99.20% | L2 | Proceed with Guardrails |
| **6** | **Renal osteodystrophy (selected)** | **99.11%** | **L2** | **Proceed with Guardrails** |
| 7 | Renal tubular acidosis | 99.06% | L3 | Research Question |

Ranks 1–4 are model-generated candidates for ultra-rare genetic diseases with no supporting trials or literature; the literature retrieved for rank 4 is explicitly flagged in the evidence pack as generic "vitamin D" keyword noise unrelated to that syndrome. Rank 5 (hypophosphatemic rickets) has a large trial base, but the great majority of those trials test **burosumab (KRN23)**, an anti-FGF23 antibody, not cholecalciferol — direct cholecalciferol evidence there is thin. Rank 7 (renal tubular acidosis) has only 2 trials, neither testing cholecalciferol directly.

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not returned for this drug in the current data pull. Based on established pharmacology, cholecalciferol (Vitamin D3) is a fat-soluble prohormone that undergoes 25-hydroxylation in the liver and 1α-hydroxylation in the kidney to form the biologically active hormone calcitriol (1,25-dihydroxyvitamin D), the principal regulator of intestinal calcium/phosphate absorption and a suppressor of parathyroid hormone (PTH) secretion.

Renal osteodystrophy — the bone component of chronic kidney disease–mineral and bone disorder (CKD-MBD) — arises largely because failing kidneys lose 1α-hydroxylase activity, leading to calcitriol deficiency, hypocalcemia, secondary hyperparathyroidism, and disordered bone turnover. Correcting underlying 25-hydroxyvitamin D (cholecalciferol-derived) insufficiency is a recommended first step in CKD-MBD management under KDIGO guidelines, ahead of or alongside active vitamin D analog therapy, particularly in earlier CKD stages where residual renal 1α-hydroxylase activity remains.

This gives the prediction a direct and clinically plausible mechanistic basis, though its practical value is dose- and stage-dependent: in advanced CKD/ESRD, renal 1α-hydroxylation is severely impaired, and active vitamin D analogs (calcitriol, doxercalciferol, paricalcitol) — rather than cholecalciferol itself — are typically required to achieve pharmacologic effect. This distinction should be preserved when interpreting the trial evidence below, since several retrieved trials studied these active analogs rather than cholecalciferol.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03063190](https://clinicaltrials.gov/study/NCT03063190) | Phase 4 | Withdrawn (n=0) | 0 | Direct cholecalciferol supplementation trial in CKD patients with restless leg syndrome; withdrawn before enrollment, no data generated |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | N/A | Completed | 55 | Cholecalciferol vs. doxercalciferol for secondary hyperparathyroidism in CKD stage 3–4; direct head-to-head cholecalciferol trial |
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D trial: cholecalciferol substitution in vitamin D–deficient kidney transplant recipients, evaluating renal function and rejection outcomes |
| [NCT00560300](https://clinicaltrials.gov/study/NCT00560300) | Phase 2 | Completed | 61 | Effects of active vitamin D (calcitriol, doxercalciferol) and phosphate binders on bone disease in children with kidney failure |
| [NCT01799317](https://clinicaltrials.gov/study/NCT01799317) | Phase 4 | Unknown | 60 | Vitamin D2/1α-hydroxyvitamin D2 combination for bone mineralization defects in pediatric secondary hyperparathyroidism on peritoneal dialysis |
| [NCT01149291](https://clinicaltrials.gov/study/NCT01149291) | N/A | Completed | 511 | Post-marketing observational study of selective vitamin D receptor activators for secondary hyperparathyroidism in hemodialysis patients |
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Effect of active vitamin D plus etelcalcetide on osteoclasts in CKD-MBD patients |
| [NCT00859612](https://clinicaltrials.gov/study/NCT00859612) | N/A | Completed | 464 | "Renal Osteodystrophy: A Fresh Approach" — DXA vs. QCT for diagnosing bone loss and defining bone-turnover subtype in CKD-5 |
| [NCT00108394](https://clinicaltrials.gov/study/NCT00108394) | Phase 4 | Completed | N/A | Osteopenia/renal osteodystrophy evaluation and management study (pamidronate for adynamic bone disease) |
| [NCT00527085](https://clinicaltrials.gov/study/NCT00527085) | Phase 2 | Completed | 45 | Oral calcimimetic (cinacalcet) effects on renal osteodystrophy in hemodialysis patients with secondary hyperparathyroidism (comparator/context trial, not vitamin D) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2747771](https://pubmed.ncbi.nlm.nih.gov/2747771/) | 1989 | Review | New England Journal of Medicine | Foundational review of renal osteodystrophy pathophysiology and vitamin D's role in mineral homeostasis |
| [9684690](https://pubmed.ncbi.nlm.nih.gov/9684690/) | 1998 | Review | Artificial Organs | Diagnostic and treatment framework for renal osteodystrophy in dialysis patients, including native vitamin D deficiency correction |
| [12944733](https://pubmed.ncbi.nlm.nih.gov/12944733/) | 2003 | Review | Blood Purification | Pathogenesis and treatment of renal osteodystrophy; distinguishes high-turnover (osteitis fibrosa) vs. low-turnover (adynamic) disease |
| [16970258](https://pubmed.ncbi.nlm.nih.gov/16970258/) | 2006 | Review | Saudi J Kidney Dis Transplant | Comprehensive review of renal osteodystrophy spectrum and treatment approaches |
| [12430093](https://pubmed.ncbi.nlm.nih.gov/12430093/) | 2002 | Review | Seminars in Nephrology | Renal osteodystrophy in chronic renal failure; role of calcitriol deficiency in disease progression |
| [12386262](https://pubmed.ncbi.nlm.nih.gov/12386262/) | 2002 | Review | Nephrol Dial Transplant | Secondary hyperparathyroidism mechanisms including reduced calcitriol/calcium-sensing receptor density |
| [3909812](https://pubmed.ncbi.nlm.nih.gov/3909812/) | 1985 | Review | Am J Med Sciences | Early review of renal osteodystrophy pathogenesis and vitamin D-based treatment |
| [1338454](https://pubmed.ncbi.nlm.nih.gov/1338454/) | 1992 | Review | J Nutr Sci Vitaminol | Cellular mechanisms of vitamin D derivatives in uremic hyperparathyroidism |
| [26119320](https://pubmed.ncbi.nlm.nih.gov/26119320/) | 2015 | Review | Clinical Calcium | Nutritional management of renal osteodystrophy, including mineral/vitamin D control |
| [203416](https://pubmed.ncbi.nlm.nih.gov/203416/) | 1977 | Review | Clinical Endocrinology | Classic review of vitamin D metabolism relevant to bone mineralization in renal disease |

## Malaysia Market Information

800 cholecalciferol-containing products are registered and marketed in Malaysia (NPRA status: 已上市 / Marketed). This data pull did not return individual license-level detail (registration numbers, product names, dosage forms, or approved indication text) — those fields came back empty for all sampled records and would need to be re-queried from the NPRA product database before a formulation-specific safety or route assessment can be completed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among the 7 TxGNN-predicted indications for cholecalciferol, renal osteodystrophy has the strongest combination of direct clinical-trial evidence (including head-to-head cholecalciferol trials) and an already-established mechanistic and guideline basis (KDIGO CKD-MBD management). The remaining candidates are either evidence-free rare-disease predictions likely reflecting model noise (ranks 1–4, Hold) or rely predominantly on trials of a different drug class, burosumab (rank 5), or have minimal trial support (rank 7).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications — currently blocking (DG001), required before any safety pre-assessment
- Structured mechanism-of-action documentation (DG002)
- License-level detail for the 800 Malaysia registrations (dosage form, strength, approved indication text) to assess route/formulation compatibility with a CKD population
- Clarification of dosing strategy by CKD stage, since renal 1α-hydroxylation impairment may limit cholecalciferol's own efficacy relative to active vitamin D analogs in advanced disease
- A dedicated evidence pull isolating cholecalciferol-specific (vs. calcitriol/doxercalciferol/paricalcitol/burosumab) trials, to avoid conflating results across pharmacologically distinct agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

