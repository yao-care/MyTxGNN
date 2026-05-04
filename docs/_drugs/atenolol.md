---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 5
---

# Atenolol
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

# Atenolol: From Cardiovascular Disease to Hypertension

## One-Sentence Summary

Atenolol is a selective β1-adrenergic receptor blocker belonging to the beta-blocker class; detailed original indication records were not returned from the Malaysian NPRA registry in the current dataset, though it is broadly recognized as a core cardiovascular agent.
The TxGNN model ranks **Hypertension** as its top predicted indication, supported by **10+ relevant clinical trials** and **20 supporting publications** in the current evidence pack.
This is an exceptionally well-evidenced drug-indication pair at Evidence Level **L1**, representing both a strong TxGNN validation and a cornerstone of evidence-based antihypertensive therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current NPRA registry data |
| Predicted New Indication | Hypertension |
| TxGNN Prediction Score | N/A (score data pending in current dataset) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 30 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atenolol is a selective β1-adrenergic receptor antagonist. By blocking β1 receptors in the heart, it reduces heart rate and cardiac output, leading to a sustained fall in both systolic and diastolic blood pressure. This is a direct pharmacodynamic mechanism — not a distant inference — and the mechanistic link between β1 blockade and blood pressure reduction is one of the most thoroughly characterized relationships in clinical pharmacology.

Hypertension is a condition driven in large part by elevated sympathetic tone and excessive catecholamine stimulation of the heart and vasculature. Atenolol's cardioselectivity (minimal β2 activity at therapeutic doses) means it attenuates sympathetically-mediated blood pressure elevation while reducing the risk of bronchospasm associated with non-selective beta-blockers. This selectivity profile makes it particularly suitable for hypertensive patients with comorbid cardiac conditions such as coronary artery disease or post-myocardial infarction — further expanding its clinical applicability.

Landmark cardiovascular outcome trials have firmly established atenolol's antihypertensive role. The INVEST trial (n=22,000) used atenolol as the comparator arm for hypertension with coronary artery disease, and the ASCOT trial (n=19,257) evaluated atenolol-based versus amlodipine-based strategies, both generating high-quality long-term evidence. While more recent guidelines have debated the relative merits of atenolol versus newer agents (particularly ARBs and CCBs), its role in blood pressure management remains well-supported and clinically relevant.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT00133692](https://clinicaltrials.gov/study/NCT00133692) | Phase 4 | Completed | 22,000 | INVEST trial: large-scale RCT comparing verapamil SR/trandolapril vs atenolol-based strategy in hypertensive patients with coronary artery disease; provides major long-term cardiovascular outcome data for atenolol |
| [NCT01499511](https://clinicaltrials.gov/study/NCT01499511) | N/A | Completed | 1,718 | ASCOT-10: 10-year post-trial follow-up of ASCOT UK survivors; tested whether benefits from amlodipine-based vs atenolol-based antihypertensive strategies persist beyond the original trial period |
| [NCT00262236](https://clinicaltrials.gov/study/NCT00262236) | Phase 3 | Completed | 693 | 12-week Phase 3 RCT comparing aliskiren alone and combined with atenolol in essential hypertension; directly evaluated atenolol's antihypertensive efficacy in a robust controlled setting |
| [NCT00389168](https://clinicaltrials.gov/study/NCT00389168) | Phase 2/3 | Completed | 115 | Randomized comparison of irbesartan vs atenolol on cardiac and vascular structural changes (LV dimensions) in hypertensive patients with LVH; evaluated organ-protective effects |
| [NCT00246519](https://clinicaltrials.gov/study/NCT00246519) | Phase 4 | Completed | 1,701 | PEAR pharmacogenomic study: identified genetic determinants of antihypertensive response to atenolol vs hydrochlorothiazide; foundational precision medicine data for atenolol |
| [NCT01251146](https://clinicaltrials.gov/study/NCT01251146) | Phase 4 | Completed | 177 | Multicentric RCT comparing bisoprolol vs atenolol effects on resting heart rate and sympathetic nervous system activity in essential hypertension |
| [NCT01762436](https://clinicaltrials.gov/study/NCT01762436) | Phase 4 | Completed | 109 | Compared bisoprolol vs atenolol on sympathetic nervous activity and central aortic pressure in essential hypertension; differential hemodynamic profiles characterized |
| [NCT01939509](https://clinicaltrials.gov/study/NCT01939509) | Phase 4 | Completed | 80 | Head-to-head comparison of bisoprolol vs atenolol hemodynamics and arterial stiffness in hypertension with metabolic syndrome |
| [NCT00529750](https://clinicaltrials.gov/study/NCT00529750) | Phase 4 | Completed | 108 | Compared irbesartan vs atenolol on endothelial function and oxidative stress in hypertensive patients with metabolic syndrome |
| [NCT00147563](https://clinicaltrials.gov/study/NCT00147563) | Phase 4 | Completed | 34 | Compared eplerenone vs atenolol on resistance artery remodeling in mild-to-moderate primary hypertension; assessed vascular structural changes as a surrogate endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15530629](https://pubmed.ncbi.nlm.nih.gov/15530629/) | 2004 | Review/Meta-analysis | *Lancet* | Systematic review of atenolol as reference drug in hypertension RCTs; assessed cardiovascular morbidity and mortality data — key reference for contextualizing atenolol's comparative efficacy |
| [31259](https://pubmed.ncbi.nlm.nih.gov/31259/) | 1979 | RCT | *Clin Pharmacol Ther* | Crossover trial of atenolol vs three nonselective beta-blockers (propranolol, oxprenolol, pindolol) in established hypertension; demonstrated advantages of cardioselectivity |
| [6805588](https://pubmed.ncbi.nlm.nih.gov/6805588/) | 1982 | RCT | *BMJ* | Once-daily atenolol (50 mg/100 mg) vs metoprolol SR in 9 hypertensive outpatients; blood pressure and heart rate measured after 3 weeks per treatment arm |
| [1104047](https://pubmed.ncbi.nlm.nih.gov/1104047/) | 1975 | RCT | *BMJ* | Double-blind crossover trial of atenolol alone (200/400 mg) and combined with bendrofluazide in 24 hypertensive patients; atenolol produced significantly greater BP reduction than diuretic alone |
| [9759992](https://pubmed.ncbi.nlm.nih.gov/9759992/) | 1998 | RCT | *J Hum Hypertens* | Valsartan 160 mg vs atenolol 100 mg once daily in 103 severe primary hypertension patients over 6 weeks; both drugs reduced DBP with comparable efficacy |
| [2216994](https://pubmed.ncbi.nlm.nih.gov/2216994/) | 1990 | RCT | *Postgrad Med J* | Enalapril vs atenolol in 67 essential hypertension patients (single-blind crossover); atenolol normalized BP in a substantial proportion across severity grades |
| [7340890](https://pubmed.ncbi.nlm.nih.gov/7340890/) | 1981 | RCT | *Br J Clin Pharmacol* | Open randomized crossover of atenolol vs metoprolol at 50, 100, and 200 mg once daily; measured BP and heart rate at rest and during exercise in mild-to-moderate essential hypertension |
| [26425837](https://pubmed.ncbi.nlm.nih.gov/26425837/) | 2015 | Pharmacogenomics | *J Hypertens* | GWAS identified PTPRD gene SNPs significantly associated with systolic BP response to atenolol and with resistant hypertension; supports precision prescribing |
| [7903118](https://pubmed.ncbi.nlm.nih.gov/7903118/) | 1993 | Clinical Study | *Minerva Cardioangiol* | Review of fixed-combination slow-release nifedipine/atenolol (Niften) for hypertension and angina; demonstrated superior efficacy of the combination vs either agent alone |
| [3602015](https://pubmed.ncbi.nlm.nih.gov/3602015/) | 1986 | RCT | *Pharmatherapeutica* | Prospective double-blind study comparing atenolol+nifedipine vs atenolol+diuretic (amiloride/HCTZ) in 98 patients inadequately controlled on atenolol alone; evaluated BP control at 8 weeks |

---

## Malaysia Market Information

The NPRA registry query confirmed **30 registered products** for Atenolol in Malaysia with market status **Marketed (已上市)**. However, detailed product-level information — including license numbers, product names, dosage forms, and approved indication text — was not returned in the current dataset.

Please consult the official NPRA registry at [https://www.npra.gov.my](https://www.npra.gov.my) for complete registration details of individual atenolol-containing products.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The current Evidence Pack flagged two blocking data gaps: (1) NPRA package insert warnings and contraindications (DG001 — Blocking severity), and (2) DrugBank mechanism of action data (DG002 — High severity). Both should be resolved before proceeding to clinical implementation review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3/4 RCTs with large sample sizes — including INVEST (n=22,000), PEAR (n=1,701), and the aliskiren combination trial (n=693) — confirm atenolol's antihypertensive efficacy at L1 evidence level. Thirty active NPRA registrations confirm market availability in Malaysia.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Download and parse the NPRA package insert PDF to extract key warnings, contraindications, and drug interaction information (DG001)
- **MOA data (High):** Query the DrugBank API for complete mechanism of action, pharmacodynamics, and pharmacokinetic profile for Atenolol (DB00335) (DG002)
- **NPRA registration details:** Retrieve license numbers, approved indication text, and dosage forms for all 30 registered products from the NPRA registry
- **Metabolic risk assessment:** Given existing literature evidence of atenolol's impact on glucose/insulin sensitivity and lipid profile (PMID 9140673, PMID 00607347), include a metabolic monitoring protocol for high-risk patient populations (diabetic, obese, metabolic syndrome)
- **Comparator positioning:** Given the ASCOT and LIFE trial data showing atenolol's inferiority to newer agents (amlodipine, ARBs) in certain endpoints, clarify the clinical positioning of atenolol within current Malaysian hypertension treatment guidelines (e.g., as a first-line option or in specific subgroups)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

