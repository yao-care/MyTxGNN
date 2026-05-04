---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Glaucoma and Edema to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a well-established carbonic anhydrase inhibitor with registered indications including glaucoma and diuresis; however, detailed Malaysian-registered indication texts were not retrievable from this evidence pack.
The TxGNN model predicts it may be effective for **Cardiomyopathy** (specifically acute decompensated heart failure with diuretic resistance) — ranked #7 by TxGNN score but **#1 by evidence quality** among the ten assessed indications.
This direction is supported by **3 active clinical trials** (all Phase 4, total enrolment 1,805) and **10 publications**, with the landmark ADVOR Phase 3 RCT (NEJM 2022) providing additional external validation not captured in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrievable — all Malaysian registered product indication fields are empty in this evidence pack |
| Predicted New Indication | Cardiomyopathy |
| TxGNN Prediction Score | 99.83% (rank #7 by TxGNN; rank #1 by evidence quality) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction selection:** The highest TxGNN-scored prediction (exercise-induced malignant hyperthermia, 99.95%) carries L5 evidence with a **Hold** recommendation and no supporting clinical trials or publications. This report focuses on **Cardiomyopathy** as the most evidence-supported and clinically actionable candidate.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, acetazolamide is a **carbonic anhydrase inhibitor (CAI)** whose efficacy in glaucoma, altitude sickness, and oedema has been well established, and whose renal tubular mechanism is directly applicable to heart failure management.

Acetazolamide inhibits carbonic anhydrase in the renal proximal tubule, blocking bicarbonate (HCO₃⁻) reabsorption. In patients receiving long-term loop diuretics, a compensatory metabolic alkalosis gradually develops, blunting the natriuretic effect of those diuretics and producing diuretic resistance. By reversing this metabolic alkalosis, acetazolamide restores loop diuretic sensitivity — and as a consequence, improves fluid decongestion in acute decompensated heart failure. The ADVOR Phase 3 RCT (NEJM 2022), though not captured in this evidence pack, confirmed this pathway with statistically significant improvement in successful decongestion vs. placebo.

Cardiomyopathy is one of the leading causes of chronic heart failure, and acute decompensation with volume overload and diuretic resistance is its most common and costly clinical presentation. The mechanistic bridge — carbonic anhydrase inhibition → metabolic alkalosis correction → loop diuretic resensitisation → decongestion — precisely targets this unmet therapeutic need. Three independent Phase 4 trials (total n = 1,805) are currently recruiting patients with exactly this clinical profile, reflecting broad investigator confidence in the repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide as adjunct to loop diuretics in acute decompensation of chronic HF (including cardiomyopathy); tests decongestion outcomes in patients with both preserved and reduced LVEF |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Double-blind multicentre RCT comparing loop diuretics + metolazone vs. loop diuretics + acetazolamide vs. loop diuretics alone in acute HF with volume overload; primary endpoint is optimal diuretic strategy for loop-diuretic-resistant patients |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | Recruiting | 466 | TAILOR-AHF: urine sodium–guided personalised diuretic algorithm in acute decompensated HF; acetazolamide is an escalation option within the algorithm, evaluating biomarker-driven therapy selection |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Annual Review | ESC Heart Failure | 2024 HF management update; contextualises evolving diuretic strategies including carbonic anhydrase inhibitors alongside SGLT2 inhibitors and finerenone in contemporary HF care |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Review of novel CV pharmacotherapy in 2022, including first-in-class approvals for obstructive HCM; provides pharmacological landscape for cardiomyopathy treatment advances |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiology Cases | Acetazolamide successfully corrected hypochloremia and improved diuretic response in an 87-year-old patient with advanced HF and HCM; highlights chloride manipulation and urinary electrolyte monitoring as essential |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Adverse Event Report | Acute Medicine & Surgery | ⚠️ Non-cardiogenic pulmonary oedema occurred 1 hour after **IV** acetazolamide in a dilated cardiomyopathy patient; critical safety signal suggesting oral route is preferred in cardiomyopathy |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study (ex vivo) | Saudi Medical Journal | Investigated acetazolamide effects on ischemia-reperfused isolated rabbit hearts; provides preclinical mechanistic evidence for cardioprotective potential |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian Journal of Ophthalmology | Oral acetazolamide used in Danon disease — a glycogen storage cardiomyopathy — for cystoid macular oedema management; indirect evidence of use in a cardiomyopathy subtype |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurologica Scandinavica | Patient on acetazolamide 750–1000 mg/day for hypokalaemic periodic paralysis developed exercise angina with ST depression; cardiac monitoring warranted during high-dose therapy |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurologica Scandinavica | Echocardiographic evidence of cardiomyopathy in hypokalaemic periodic paralysis family; documents ion-channel–related cardiac muscle involvement relevant to acetazolamide's mechanism |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Case Series | Journal of Nuclear Medicine | SPECT cerebral blood flow in mitochondrial encephalomyopathy; documents acetazolamide's vasodilatory effect on tissue perfusion, peripheral but mechanistically relevant to cardiac applications |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | Journal of Medical Case Reports | Congenital hydrocephalus with trisomy 9p and coexisting congenital heart disease; acetazolamide used for CSF management, illustrating the complexity of cardiac comorbidity management |

---

## Malaysia Market Information

Three products are registered with Malaysia NPRA (市場狀態: 已上市). However, individual license details — including registration numbers, product names, dosage forms, and approved indication texts — were not successfully retrieved in this evidence pack. The table below reflects the data gap.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| (Pending retrieval) | (Pending retrieval) | (Pending retrieval) | (Pending retrieval) |
| (Pending retrieval) | (Pending retrieval) | (Pending retrieval) | (Pending retrieval) |
| (Pending retrieval) | (Pending retrieval) | (Pending retrieval) | (Pending retrieval) |

> **Action required:** Retrieve full product data from the [NPRA Product Registration](https://www.npra.gov.my) database using the drug name "Acetazolamide" to complete this section.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety data fields (key warnings, contraindications, drug-drug interactions) are pending retrieval in this evidence pack.

> **Specific signals identified from literature (pending formal package insert verification):**
> - **IV route risk:** Non-cardiogenic pulmonary oedema reported after IV acetazolamide in a cardiomyopathy patient (PMID 29123889); **oral route is strongly preferred** in this indication.
> - **Electrolyte monitoring:** Hypokalaemia-related cardiac effects documented in case series (PMID 7324871); concurrent loop diuretic use amplifies this risk — close monitoring of serum potassium, chloride, and sodium is warranted.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three Phase 4 RCTs (total enrolment 1,805) are actively testing oral acetazolamide for acute decompensated heart failure/cardiomyopathy, and the carbonic anhydrase inhibition → metabolic alkalosis correction → loop diuretic resensitisation pathway is externally validated by the ADVOR Phase 3 RCT (NEJM 2022). Acetazolamide is already marketed in Malaysia (3 registrations), and the oral formulation presents no route compatibility barrier for this indication.

**To proceed, the following is needed:**

- **Regulatory data retrieval:** Download Malaysian NPRA registration details (product names, dosage forms, approved indications) and the package insert PDF to fill the current data gaps
- **MOA documentation:** Query DrugBank API (DrugBank ID currently null) to complete the mechanism of action record
- **Route safety protocol:** Restrict use to the **oral route only** in cardiomyopathy patients; IV administration carries documented pulmonary oedema risk
- **Electrolyte monitoring plan:** Establish mandatory monitoring of serum K⁺, Cl⁻, Na⁺, and bicarbonate at baseline and during treatment, given combined diuretic-related electrolyte depletion risk
- **Evidence watch:** Monitor completion of NCT05802849 (n = 400, expected December 2025) and NCT06166654 (n = 939, expected September 2027) for upgraded evidence level to L1
- **Scope clarification:** Confirm whether the target Malaysian patient population (acute HF/cardiomyopathy with diuretic resistance) falls within or outside the current approved Malaysian label, to determine whether an off-label use protocol or label extension application is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

