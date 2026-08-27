---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 5
---

# Ezetimibe
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

# Ezetimibe: From Primary Hypercholesterolemia to Sitosterolemia

## One-Sentence Summary

Ezetimibe is a selective cholesterol-absorption inhibitor originally used to treat primary hypercholesterolemia (alone or combined with statins). The TxGNN model highlights **Sitosterolemia** as its strongest-evidence indication, currently supported by **10 clinical trials** and **17 publications**, several of which are Phase 2/3 randomized, double-blind, placebo-controlled trials conducted specifically in this rare disease population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary Hypercholesterolemia (well-established use; not confirmed in this data pull's TFDA license text) |
| Predicted New Indication | Sitosterolemia |
| TxGNN Prediction Score | 0.00% (score field returned as 0.0 for all ranked candidates in this data pull — likely incomplete scoring data, not a true 0% prediction) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 40 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ezetimibe selectively inhibits the NPC1L1 (Niemann-Pick C1-Like 1) cholesterol transporter at the brush border of the small intestine, blocking absorption of both dietary cholesterol and plant sterols (sitosterol, campesterol). This mechanism is not incidental to sitosterolemia — it maps directly onto the disease's core pathology.

Sitosterolemia is a rare autosomal recessive disorder caused by mutations in ABCG5/ABCG8, the transporters responsible for excreting plant sterols back into the intestinal lumen and bile. Loss of this efflux function causes excessive intestinal absorption and tissue accumulation of plant sterols, leading to xanthomas, hemolytic anemia, macrothrombocytopenia, and premature atherosclerosis. Because ezetimibe blocks the *absorption* side of the same sterol-trafficking pathway that ABCG5/ABCG8 fails to clear on the *excretion* side, the mechanistic fit is unusually direct — closer to an on-target rescue than a speculative repurposing hypothesis.

This mechanistic strength is reflected in the trial record: ezetimibe has already been studied as monotherapy and add-on therapy specifically in homozygous sitosterolemia patients since 2001, including multiple randomized, double-blind, placebo-controlled Phase 2/3 trials. In effect, TxGNN's prediction recovers a use that has substantial real-world clinical precedent, which is consistent with the L1 evidence level assigned.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00092820](https://clinicaltrials.gov/study/NCT00092820) | Phase 3 | Completed | 58 | Multicenter, randomized, double-blind, placebo-controlled trial of MK0653 (ezetimibe) added to current regimen in homozygous sitosterolemia; disease-specific efficacy/safety extension study. |
| [NCT00045812](https://clinicaltrials.gov/study/NCT00045812) | Phase 2 | Completed | 5 | Multicenter, randomized, double-blind, placebo-controlled study of SCH-58235 (ezetimibe) lowering sitosterol, plant sterol and cholesterol levels in homozygous sitosterolemia. |
| [NCT00092898](https://clinicaltrials.gov/study/NCT00092898) | Phase 3 | Completed | 30 | 6-month randomized, double-blind, placebo-controlled trial adding ezetimibe 30 mg to an ongoing 10 mg regimen in homozygous sitosterolemia. |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label, worldwide treatment-use study providing ezetimibe 10 mg/day to patients with homozygous familial hypercholesterolemia or homozygous sitosterolemia. |
| [NCT00092807](https://clinicaltrials.gov/study/NCT00092807) | Phase 3 | Completed | 37 | 1-year open-label extension evaluating long-term safety and cholesterol-lowering ability of ezetimibe in homozygous sitosterolemia. |
| [NCT01584206](https://clinicaltrials.gov/study/NCT01584206) | N/A | Completed | 8 | Pilot study assessing whether ezetimibe improves whole-body plant sterol and cholesterol homeostasis in sitosterolemia. |
| [NCT00099996](https://clinicaltrials.gov/study/NCT00099996) | Phase 3 | Completed | 3 | Small dose-escalation study (ezetimibe 30 mg added to 10 mg) evaluating safety/effectiveness in homozygous sitosterolemia. |
| [NCT01948648](https://clinicaltrials.gov/study/NCT01948648) | N/A | Unknown | 13 | Evaluates fish oil, colesevelam and ezetimibe combination therapy for further reduction of plasma plant sterols in sitosterolemia. |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completed | 1794 | Japan 52-week post-marketing observational study of Zetia mono/combination therapy in general lipid-lowering practice (not disease-specific). |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A | Completed | 11332 | Japan 12-week post-marketing observational study of Zetia mono/combination therapy in general practice (not disease-specific). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28340366](https://pubmed.ncbi.nlm.nih.gov/28340366/) | 2017 | Cohort | Atherosclerosis | Ezetimibe reduces plasma plant sterols and total cholesterol, and alters LDL/HDL subclass distribution in sitosterolemia patients. |
| [25444527](https://pubmed.ncbi.nlm.nih.gov/25444527/) | 2015 | Cohort | The Journal of Pediatrics | Ezetimibe improves platelet count and size while reducing plasma plant sterol levels in sitosterolemia. |
| [18822021](https://pubmed.ncbi.nlm.nih.gov/18822021/) | 2008 | 2-year extension study | Int J Clin Pract | Long-term (2-year) efficacy and safety of ezetimibe 10 mg in homozygous sitosterolemia patients. |
| [34969652](https://pubmed.ncbi.nlm.nih.gov/34969652/) | 2022 | Cohort | J Clin Lipidology | Clinical/genetic profiling and therapy evaluation in 55 children and 5 adults with sitosterolemia. |
| [36897412](https://pubmed.ncbi.nlm.nih.gov/36897412/) | 2023 | Review | Curr Atheroscler Rep | Updated summary of sitosterolemia pathophysiology (ABCG5/ABCG8), clinical features, and management. |
| [30033951](https://pubmed.ncbi.nlm.nih.gov/30033951/) | 2018 | Review | J Atheroscler Thromb | Reviews sitosterolemia, hypercholesterolemia, and coronary artery disease risk. |
| [24267242](https://pubmed.ncbi.nlm.nih.gov/24267242/) | 2013 | Review | Atherosclerosis | Evaluates sterol metabolism and therapeutic approaches (including ezetimibe) in sitosterolemia. |
| [35248527](https://pubmed.ncbi.nlm.nih.gov/35248527/) | 2022 | Case series | Clin Chim Acta | Clinical and genetic features of sitosterolemia in a Japanese cohort. |
| [24821603](https://pubmed.ncbi.nlm.nih.gov/24821603/) | 2014 | Review | Curr Atheroscler Rep | Diagnosis, investigation, and management overview of sitosterolemia. |
| [29984642](https://pubmed.ncbi.nlm.nih.gov/29984642/) | 2019 | Review | Curr Med Chem | Reviews diagnosis, hematological abnormalities, cardiovascular disease and management in sitosterolemia. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Sitosterolemia is supported by L1-level evidence — multiple completed, randomized, double-blind, placebo-controlled Phase 2/3 trials conducted specifically in homozygous sitosterolemia patients — and the mechanism (NPC1L1 inhibition blocking the same plant-sterol absorption pathway disrupted by ABCG5/ABCG8 loss-of-function) is directly on-target rather than speculative.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (flagged as a **Blocking** data gap — required before this candidate can enter the S1 safety pre-assessment stage)
- Confirmed mechanism-of-action data from DrugBank (currently unavailable at the drug level)
- Malaysia-specific product license and approved-indication text (the current data pull returned 40 total registrations but no populated license detail records)
- Drug–drug interaction (DDI) data (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

