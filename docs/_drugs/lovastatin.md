---
layout: default
title: Lovastatin
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 6
---

# Lovastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lovastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a first-generation HMG-CoA reductase inhibitor (statin) originally used to lower LDL-cholesterol in patients with primary hypercholesterolemia and mixed dyslipidemia. The TxGNN model predicts it may also be relevant for **Homozygous Familial Hypercholesterolemia (HoFH)**, a rare and severe genetic form of hypercholesterolemia, with **3 clinical trials** and **19 publications** currently identified in this direction — though the mechanistic evidence suggests the benefit is likely limited to a genetic subset of patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / mixed dyslipidemia (classic statin indication; NPRA label indication text was not returned in the current dataset) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack. Based on known pharmacology, lovastatin is a statin (HMG-CoA reductase inhibitor) that lowers LDL-cholesterol primarily by reducing hepatic cholesterol synthesis, which triggers **up-regulation of hepatic LDL receptors (LDLR)** to increase LDL clearance from plasma. Its efficacy in primary hypercholesterolemia is well established and mechanistically it could plausibly extend to other LDL-C-elevating disorders, including HoFH.

However, HoFH is caused by biallelic loss-of-function mutations in the LDL receptor gene, and patients are commonly classified as "receptor-negative" (little to no functional LDLR) or "receptor-defective" (partial LDLR function). Because lovastatin's mechanism *depends on* the LDLR pathway it upregulates, its effectiveness in HoFH is inherently genotype-dependent — a fundamentally different situation from its original indication, where residual receptor function is generally intact.

The literature in this evidence pack directly supports this caveat: studies in receptor-negative HoFH patients show **no meaningful reduction in LDL-C or LDL turnover** with lovastatin, whereas some receptor-defective patients and post-liver-transplant patients (whose receptor activity was restored) do respond. This means the TxGNN signal is mechanistically plausible only for a genetically-defined subgroup of HoFH patients, not for the HoFH population as a whole, and cannot be treated as a general "positive" repurposing signal without receptor-status stratification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (PCSK9 inhibitor, not lovastatin) in children/adolescents (8–17y) with HoFH on top of background therapy; confirms HoFH as an active pediatric research area but is not direct lovastatin evidence. |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term (24-month) open-label extension of ezetimibe 10mg added to atorvastatin or simvastatin in HoFH; supports statin + ezetimibe combination safety, not lovastatin monotherapy. |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Parent efficacy/safety study of ezetimibe co-administered with atorvastatin or simvastatin in HoFH; different drug, same disease population. |

**Note:** None of the identified trials tested lovastatin directly in HoFH; all three studied other agents (alirocumab, ezetimibe) in the same disease population, so they provide only indirect context for this repurposing candidate.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Cohort (small) | The Journal of Pediatrics | Lovastatin 2 mg/kg/day in 3 children with **receptor-negative** HoFH produced no decrease in LDL-C and no change in LDL turnover, showing lovastatin's dependence on functional LDL receptors. |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Cohort (small) | Anales Españoles de Pediatría | Combined lovastatin + probucol + cholestyramine in 2 HoFH patients reduced total cholesterol by 41.7%, with response linked to LDL-receptor analysis findings. |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case report | JAMA | Lovastatin (mevinolin) normalized cholesterol in a HoFH child **after liver transplantation** restored ~60% of LDL receptor activity — underscoring receptor-dependence of response. |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Case report | Anales Españoles de Pediatría | A HoFH patient with **residual (receptor-defective)** activity showed a promising response to combined cholestyramine + lovastatin therapy. |
| [8637439](https://pubmed.ncbi.nlm.nih.gov/8637439/) | 1996 | Case report | Metabolism | In a homozygous sitosterolemic girl with concurrent heterozygous FH, lovastatin and cholestyramine had **opposing effects** on plasma sterol levels, cautioning against generalizing statin response across genotypes. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | Review of pharmacologic/surgical treatments in dyslipidemic children, listing lovastatin among agents with variable success in FH. |
| [12091863](https://pubmed.ncbi.nlm.nih.gov/12091863/) | 2002 | Case report | The Journal of Pediatrics | 15-year combination of HELP apheresis and statins reduced LDL-C by 85% from baseline and prevented premature coronary atherosclerosis progression in a HoFH patient. |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Cohort | Arteriosclerosis, Thrombosis, and Vascular Biology | HoFH patients with identical LDLR mutations show variably expressed receptor function, explaining heterogeneous response to receptor-dependent therapies (statins, evolocumab). |
| [10146648](https://pubmed.ncbi.nlm.nih.gov/10146648/) | 1993 | Case series | Transfusion Science | Two girls with FH managed for 7 years by plasma exchange/LDL-apheresis, with statin (simvastatin) as adjunct — illustrating receptor-independent removal as a complement to statin therapy. |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case report | European Journal of Pediatrics | LDL plasmapheresis with and without lovastatin in a 7-year-old girl with HoFH; long-term treatment was well tolerated and led to regression of xanthomata. |

---

## Malaysia Market Information

NPRA registration records indicate **4 active licenses** for lovastatin in Malaysia (market status: Marketed), but the specific authorization numbers, product names, dosage forms, and approved indication text were not returned in the current dataset. Please consult the NPRA Quest3+ product database directly for these registration details.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data specific to this candidate were available in the current dataset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L3 (small cohort and case reports only, no RCTs testing lovastatin specifically in HoFH), and the mechanistic rationale itself indicates the effect is genotype-dependent — receptor-negative HoFH patients (a substantial proportion of this population) show little to no LDL-C response to lovastatin, so the signal cannot be generalized across the HoFH population without receptor-status stratification. Additionally, TFDA/NPRA-equivalent label warnings and contraindications data are marked as a **Blocking** data gap, which prevents this candidate from entering the S1 safety pre-screening stage regardless of the disease indication under consideration.

**To proceed, the following is needed:**
- NPRA label warnings/contraindications data (currently blocking safety pre-screening)
- Confirmed mechanism of action data from DrugBank
- Stratification of future evidence collection by LDL-receptor genotype (receptor-negative vs. receptor-defective) before drawing efficacy conclusions in HoFH
- For context: the related candidate indication **hyperlipoproteinemia** (rank 2 in this evidence pack) shows a stronger evidence base (L2, multiple completed RCTs, clear direct mechanistic link) and may be a more actionable near-term repurposing target worth a separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

