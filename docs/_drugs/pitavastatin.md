---
layout: default
title: Pitavastatin
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Pitavastatin
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

# Pitavastatin: From Hyperlipidemia to HIV-Associated Cardiovascular Disease Prevention

## One-Sentence Summary

Pitavastatin is a fully synthetic HMG-CoA reductase inhibitor (statin) registered in Malaysia and approved globally for the management of dyslipidemia and elevated LDL-cholesterol.
The TxGNN model generated 10 predicted new indications; the most clinically impactful novel finding is cardiovascular event prevention in people living with **HIV infectious disease**, currently supported by **2 Phase 3 clinical trials** (including the landmark REPRIEVE trial, n=7,769) and **20 publications** — an application the FDA approved in 2023, making pitavastatin the first statin with a dedicated HIV cardiovascular prevention indication.
Evidence strength across all 10 predictions ranges from L1 (HIV, hyperlipoproteinemia) to L5 (model-only predictions with no clinical data).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dyslipidemia / hypercholesterolemia (specific text not available in dataset) |
| Predicted New Indication | HIV Infectious Disease — cardiovascular event prevention |
| TxGNN Prediction Score | 99.97% (rank 9/10) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs; REPRIEVE n=7,769) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN rankings:** The top-ranked TxGNN prediction (rank 1, score 99.9978%) maps to "obsolete familial combined hyperlipidemia" — a deprecated disease ontology term no longer in active clinical use, carrying zero supporting evidence (L5, Hold). The HIV infectious disease prediction (rank 9) represents the most clinically meaningful novel application with the strongest external evidence base, and is therefore featured as the primary repurposing candidate throughout this report.

---

## Why is This Prediction Reasonable?

Pitavastatin inhibits HMG-CoA reductase, the rate-limiting enzyme in the mevalonate/cholesterol biosynthetic pathway. This reduces hepatic cholesterol production, triggering compensatory upregulation of hepatocyte LDL receptors (LDLR), which markedly increases LDL-C clearance from the circulation — achieving LDL-C reductions of 39–45% at standard therapeutic doses. Beyond lipid-lowering, pitavastatin exerts well-documented pleiotropic effects through cholesterol-independent mechanisms involving Rho GTPase and isoprenoid pathway inhibition, including clinically meaningful reductions in IL-6, hsCRP, and soluble CD14 (sCD14) — a monocyte activation marker chronically elevated in HIV infection.

People living with HIV (PLWH) on antiretroviral therapy (ART) face approximately 50% excess cardiovascular risk compared to HIV-negative adults. This elevated risk is driven by persistent immune activation, chronic low-grade inflammation, and direct arterial injury — even when viral load is fully suppressed. Pitavastatin offers a pharmacokinetic advantage uniquely suited to this population: it undergoes primary metabolism via CYP2C9 with minimal CYP3A4 involvement. This circumvents the major interaction pathway of protease inhibitors (PIs) and NNRTIs, which are potent CYP3A4 inhibitors or inducers, making pitavastatin the statin with the lowest drug-drug interaction burden among PLWH compared to atorvastatin, simvastatin, or lovastatin.

The REPRIEVE Phase 3 trial (NCT02344290; n=7,769; 49 countries; median follow-up 5.1 years) directly tested pitavastatin 2 mg/day versus placebo in PLWH with low-to-moderate ASCVD risk on stable ART, demonstrating a 35% relative reduction in major adverse cardiovascular events (MACE; HR 0.65, 95% CI 0.48–0.90), published in *The New England Journal of Medicine* (2023). Mechanistic substudies confirmed reductions in noncalcified coronary plaque volume, lowered inflammatory biomarkers, and procollagen pathway modulation consistent with plaque stabilisation. The FDA approved pitavastatin specifically for cardiovascular risk reduction in PLWH in 2023. Together, these data provide a compelling mechanistic and clinical rationale fully consistent with the TxGNN prediction.

**Overview of all 10 TxGNN predicted indications:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|------------|---------------|----------|
| 1 | Obsolete familial combined hyperlipidemia *(deprecated term)* | 99.9978% | L5 | Hold |
| 2 | Homozygous familial hypercholesterolemia | 99.9960% | L4 | Hold |
| 3 | Hyperlipoproteinemia | 99.9952% | L1 | Proceed with Guardrails |
| 4 | Hyperlipidemia, familial combined, LPL-related | 99.9944% | L5 | Hold |
| 5 | Familial hypercholesterolemia | 99.9882% | L2 | Proceed with Guardrails |
| 6 | Cholesterol-ester transfer protein deficiency | 99.9783% | L5 | Hold |
| 7 | Hypercholesterolemia, autosomal dominant | 99.9749% | L2 | Proceed with Guardrails |
| 8 | Hypercholesterolemia due to CYP7A1 deficiency *(ultra-rare, <50 global cases)* | 99.9748% | L5 | Hold |
| **9** | **HIV infectious disease** *(FDA-approved 2023)* | **99.9669%** | **L1** | **Proceed with Guardrails** |
| 10 | Neurodevelopmental disorder with ataxic gait and absent speech | 99.9539% | L5 | Hold |

---

## Clinical Trial Evidence

**HIV Infectious Disease (rank 9 — primary novel indication):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02344290](https://clinicaltrials.gov/study/NCT02344290) | Phase 3 | Completed | 7,769 | **REPRIEVE:** Pitavastatin 2 mg/day vs placebo in PLWH on ART across 49 countries; median follow-up 5.1 years. Primary endpoint MACE: HR 0.65 (95% CI 0.48–0.90), 35% relative risk reduction. Published NEJM 2023. Formed the basis for 2023 FDA approval of pitavastatin for HIV cardiovascular prevention. |
| [NCT06317051](https://clinicaltrials.gov/study/NCT06317051) | Phase 3/4 | Active, not recruiting | 300 | Factorial double-blind RCT in INSTI-based ART patients with elevated metabolic risk: pitavastatin vs rosuvastatin/ezetimibe and dapagliflozin vs placebo. Confirms pitavastatin's status as standard comparator in HIV cardiometabolic research (completion expected December 2026). |

**Hyperlipoproteinemia (rank 3 — L1 lipid disorder evidence):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01256476](https://clinicaltrials.gov/study/NCT01256476) | Phase 4 | Completed | 328 | Randomised double-blind 12-week active-controlled study: pitavastatin 4 mg vs pravastatin 40 mg daily in primary hyperlipidemia or mixed dyslipidemia. Direct head-to-head superiority data. |
| [NCT02056847](https://clinicaltrials.gov/study/NCT02056847) | Phase 4 | Completed | 313 | Pitavastatin 2 mg vs 4 mg in hyperlipidemic patients with impaired fasting glucose (IFG); evaluated HbA1c impact of intensive vs standard lipid-lowering over approximately 4 years. |
| [NCT01166633](https://clinicaltrials.gov/study/NCT01166633) | Phase 4 | Completed | 200 | Randomised dose-titration open-label study: pitavastatin vs atorvastatin in hypercholesterolemia with mild-to-moderate hepatic impairment; demonstrates hepatic safety profile for a particularly relevant subgroup. |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | Unknown | 120 | Renal transplant recipients: pitavastatin-based regimen vs evolocumab (PCSK9 inhibitor) for post-transplant dyslipidemia management; addresses a drug-interaction-constrained population relevant to Malaysian clinical practice. |
| [NCT01386853](https://clinicaltrials.gov/study/NCT01386853) | Phase 3 | Unknown | 200 | 12-week randomised double-blind active-controlled non-inferiority study: pitavastatin (Livalo®) vs atorvastatin (Lipitor®) in high-risk hypercholesterolemic patients. |
| [NCT00711919](https://clinicaltrials.gov/study/NCT00711919) | Not applicable | Unknown | 300 | PEARL study: pitavastatin aggressive vs conventional lipid-lowering and effect on carotid intima-media thickness (IMT) regression in hyperlipidemia; cardiovascular structural surrogate endpoint. |

---

## Literature Evidence

**HIV Infectious Disease (rank 9):**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37486775](https://pubmed.ncbi.nlm.nih.gov/37486775/) | 2023 | RCT — primary outcome (REPRIEVE) | N Engl J Med | Pitavastatin 2 mg/day reduced MACE by 35% (HR 0.65) vs placebo in 7,769 PLWH on ART over median 5.1 years. Established the HIV cardiovascular prevention indication; basis for 2023 FDA approval. |
| [38381407](https://pubmed.ncbi.nlm.nih.gov/38381407/) | 2024 | Mechanistic sub-study (RCT) | JAMA Cardiology | REPRIEVE mechanistic substudy: pitavastatin significantly reduced noncalcified coronary plaque volume and systemic inflammatory biomarkers (IL-6, hsCRP), confirming pleiotropic anti-atherosclerotic activity in PLWH independent of LDL-C lowering. |
| [39661372](https://pubmed.ncbi.nlm.nih.gov/39661372/) | 2025 | Secondary analysis (RCT) | JAMA Cardiology | Pitavastatin modulated procollagen pathway activity and stabilised coronary plaque in REPRIEVE; provides mechanistic explanation for MACE reduction beyond LDL-C lowering alone. |
| [39374532](https://pubmed.ncbi.nlm.nih.gov/39374532/) | 2024 | Secondary analysis (RCT) — diabetes risk | Ann Intern Med | REPRIEVE diabetes substudy: pitavastatin did not significantly increase new-onset diabetes risk in PLWH with low-to-moderate ASCVD risk, contrasting with reported diabetogenic risk of other statins in the general population. |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT | Lancet HIV | INTREPID Phase 4 trial (n=252): pitavastatin superior to pravastatin in LDL-C reduction in HIV adults with dyslipidemia on ART; confirmed favourable DDI profile vs antiretrovirals over 12 and 52 weeks. |
| [36849967](https://pubmed.ncbi.nlm.nih.gov/36849967/) | 2023 | Randomised crossover | AIDS Res Ther | Pitavastatin reduced atherosclerotic inflammatory biomarkers in PLWH on ritonavir-boosted atazanavir, confirming clinical anti-inflammatory efficacy with PI-based ART commonly used in Asia. |
| [40482662](https://pubmed.ncbi.nlm.nih.gov/40482662/) | 2025 | Longitudinal cohort analysis (RCT) | Lancet HIV | REPRIEVE follow-up: pitavastatin efficacy in reducing MACE was consistent across different ART regimens, including INSTI-based therapy now predominant in Malaysia. |
| [38294226](https://pubmed.ncbi.nlm.nih.gov/38294226/) | 2025 | Review | Cardiology in Review | Comprehensive review of pitavastatin's role in HIV cardiovascular prevention: DDI advantages (CYP2C9 pathway), pleiotropic anti-inflammatory mechanisms, and full analysis of REPRIEVE outcomes. |
| [38198667](https://pubmed.ncbi.nlm.nih.gov/38198667/) | 2023 | Clinical review | Topics Antivir Med | Post-REPRIEVE practical guidance: pitavastatin is now the preferred statin for PLWH with low-to-moderate ASCVD risk; prescribing recommendations across ART regimen types. |
| [39435321](https://pubmed.ncbi.nlm.nih.gov/39435321/) | 2024 | Secondary analysis (RCT) | Open Forum Infect Dis | REPRIEVE COVID-19 substudy: pitavastatin did not significantly reduce COVID-19 incidence or severity in PLWH, clarifying the boundaries of its pleiotropic anti-infectious scope. |

---

## Malaysia Market Information

The NPRA (National Pharmaceutical Regulatory Agency) database confirms **3 registered products** for Pitavastatin with market status **Marketed**. However, licence-level details — including registration numbers, product names, dosage forms, manufacturer information, and approved indication text — were not populated in this dataset.

| Item | Details |
|------|---------|
| Total registrations | 3 products |
| Market status | ✓ Marketed |
| Licence numbers | Not available in dataset |
| Product names | Not available in dataset |
| Dosage forms | Not available in dataset |
| Approved indication text | Not available in dataset |

Full registration details can be retrieved from the NPRA product search portal: [https://www.npra.gov.my/](https://www.npra.gov.my/)

---

## Safety Considerations

Please refer to the package insert for safety information.

**Unresolved data gaps affecting safety assessment:**
- Package insert warnings and contraindications were not retrieved for this report (Blocking data gap — required before any clinical decision or formulary review can proceed).
- DrugBank MOA and toxicity data were not retrieved (High severity gap), though publicly available pharmacology has been drawn upon in the mechanistic sections above.

**Drug interaction context relevant to HIV use:**
Pitavastatin's primary metabolic route is CYP2C9 with minimal CYP3A4 involvement. This pharmacokinetic profile confers a substantially lower DDI burden compared to atorvastatin or simvastatin when co-administered with PI-class antiretrovirals (e.g., ritonavir, cobicistat-boosted regimens) or NNRTIs that strongly modulate CYP3A4. Nonetheless, a formal DDI review against the individual patient's specific ART regimen remains essential before prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For the HIV cardiovascular prevention indication, the evidence base is exceptionally strong: the REPRIEVE Phase 3 RCT (n=7,769, 49 countries, NEJM 2023) demonstrated a 35% reduction in MACE with pitavastatin versus placebo in PLWH on ART, leading to FDA approval in 2023. Pitavastatin is already marketed in Malaysia with 3 registered products, providing a regulatory and supply foundation. Its minimal CYP3A4 metabolism makes it particularly well-suited to PLWH receiving ART in Malaysian clinical settings where PI- and INSTI-based regimens are common, reducing clinically significant DDI risk compared to other statins.

**To proceed, the following is needed:**
- Retrieve and review the Malaysian product monograph (package insert) for locally approved indication, black-box warnings, contraindications, and dosing recommendations — this is a **Blocking** prerequisite before any clinical application
- Confirm approved indication text for all 3 registered pitavastatin products in Malaysia via the NPRA portal and assess whether HIV cardiovascular prevention is included or requires a label variation
- Evaluate the size and ART profile of the HIV patient population in Malaysia, and map current cardiovascular risk management practices against post-REPRIEVE international guidelines
- Conduct a structured DDI review against ART regimens currently used in Malaysian HIV clinics (particularly INSTI-based and PI/r-based combinations)
- Establish a monitoring protocol (fasting lipid panel, LFTs, CPK, HbA1c) appropriate for Malaysian PLWH at baseline and follow-up intervals
- Assess whether the REPRIEVE cohort (predominantly non-Asian populations) provides sufficient generalisability to the Malaysian HIV demographic, or whether regional real-world evidence is required to support local clinical guideline adoption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

