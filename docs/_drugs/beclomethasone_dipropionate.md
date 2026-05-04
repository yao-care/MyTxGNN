---
layout: default
title: Beclomethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 5
---

# Beclomethasone Dipropionate
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

# Beclomethasone Dipropionate: From Inhaled Corticosteroid Therapy to Asthma

## One-Sentence Summary

Beclomethasone Dipropionate (BDP) is a synthetic inhaled corticosteroid (ICS) widely used for managing chronic airway inflammation.
The TxGNN model predicts it may be effective for **Asthma**,
with **50 clinical trials** and **20 publications** currently supporting this direction — making it one of the most extensively validated predictions in the dataset.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | (Approved indication text not available in current dataset; BDP is a well-established ICS for respiratory inflammatory conditions) |
| Predicted New Indication | Asthma |
| TxGNN Prediction Score | 0.00% (rank 1) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 27 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Beclomethasone Dipropionate is an inhaled glucocorticosteroid (ICS) that acts directly on airway epithelial cells and immune cells. Its active metabolite, beclomethasone-17-monopropionate (B17MP), binds to intracellular glucocorticoid receptors, suppressing the transcription of pro-inflammatory cytokines, reducing eosinophilic infiltration, decreasing mucus secretion, and attenuating bronchial hyperresponsiveness. This mechanism is squarely aligned with the Th2-mediated eosinophilic inflammation that characterises asthma.

BDP was in fact the first corticosteroid found to be clinically effective when delivered by aerosol inhalation, representing a landmark advance in asthma therapy since the early 1970s. The TxGNN prediction reflects an exceptionally strong mechanistic match: the drug's anti-inflammatory action on the airway is the direct causal mechanism by which asthma symptoms are controlled. This prediction effectively serves as a positive validation of the model, as the drug–disease pairing is already well-established in clinical practice worldwide.

Furthermore, the evidence base spans over five decades of clinical research, including multiple large-scale Phase 3 randomised controlled trials, meta-analyses, and real-world effectiveness studies. BDP has been studied across diverse populations — from preschool children to elderly adults, from mild persistent to severe corticosteroid-dependent asthma — reinforcing the robustness of this drug–indication relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00861926](https://clinicaltrials.gov/study/NCT00861926) | Phase 3 | Completed | 2,079 | 48-week multinational RCT comparing Foster (BDP/formoterol) for maintenance and reliever vs fixed-dose maintenance plus salbutamol reliever in asthmatics ≥18 years |
| [NCT02676089](https://clinicaltrials.gov/study/NCT02676089) | Phase 3 | Completed | 1,433 | 52-week RCT comparing extrafine BDP/FF/GB triple therapy vs BDP/FF dual therapy ± tiotropium in uncontrolled asthma on high-dose ICS/LABA |
| [NCT02676076](https://clinicaltrials.gov/study/NCT02676076) | Phase 3 | Completed | 1,153 | 52-week RCT comparing extrafine BDP/FF/GB triple therapy vs BDP/FF dual therapy in uncontrolled asthma on medium-dose ICS/LABA |
| [NCT01345916](https://clinicaltrials.gov/study/NCT01345916) | Phase 3 | Completed | 932 | 8-week Phase 3 demonstrating CHF 1535 NEXT DPI non-inferior to pMDI and superior to BDP DPI alone in morning PEF |
| [NCT00476268](https://clinicaltrials.gov/study/NCT00476268) | Phase 3 | Completed | 824 | 24-week study evaluating efficacy and tolerability of BDP/formoterol in moderate to severe persistent asthma |
| [NCT02513160](https://clinicaltrials.gov/study/NCT02513160) | Phase 3 | Completed | 713 | 6-week RCT assessing BDP BAI at 320 or 640 mcg/day vs placebo in persistent asthma aged ≥12 years |
| [NCT02040766](https://clinicaltrials.gov/study/NCT02040766) | Phase 3 | Completed | 628 | 12-week RCT of BDP 80/160 mcg/day via BAI or MDI in pediatric patients aged 4–11 with persistent asthma |
| [NCT03084718](https://clinicaltrials.gov/study/NCT03084718) | Phase 2 | Completed | 610 | 8-week dose-ranging study of 3 doses of CHF 718 pMDI (HFA-BDP) to identify optimal dose in asthmatics |
| [NCT00094016](https://clinicaltrials.gov/study/NCT00094016) | Phase 3 | Completed | 440 | 12-week Phase 3 comparing QVAR Easi-Breathe 100 and 200 mcg/day vs placebo on FEV1 in asthmatic children |
| [NCT01450774](https://clinicaltrials.gov/study/NCT01450774) | Phase 3 | Completed | 72 | Double-blind crossover comparing CHF1535 (BDP/formoterol) fixed combination vs free combination on safety (knemometry, urinary cortisol) in asthmatic children |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9519232](https://pubmed.ncbi.nlm.nih.gov/9519232/) | 1998 | Meta-analysis | Respir Med | Meta-analysis of 14 trials: fluticasone at half the mcg dose of BDP or budesonide achieves equivalent clinical efficacy, with BDP serving as the standard comparator |
| [6381025](https://pubmed.ncbi.nlm.nih.gov/6381025/) | 1984 | Systematic Review | Drugs | Decade-long reappraisal confirming BDP 400–800 mcg/day reduces oral steroid need in most asthma patients; doses up to 2000 mcg may add benefit in severe cases |
| [8334070](https://pubmed.ncbi.nlm.nih.gov/8334070/) | 1993 | Comparative Study (RCT) | Br J Clin Pract | Consensus of multiple studies: BDP and budesonide are of equivalent therapeutic efficacy in asthma; B17MP active metabolite contributes to bronchial activity |
| [10193530](https://pubmed.ncbi.nlm.nih.gov/10193530/) | 1998 | Comparative Study | Respir Med | Comparison of BDP and budesonide efficacy in asthma treatment, confirming comparable clinical outcomes |
| [40219730](https://pubmed.ncbi.nlm.nih.gov/40219730/) | 2025 | Review | Ther Adv Respir Dis | Review of extrafine BDP/FF/G single-inhaler triple therapy (SITT) as add-on strategy for difficult-to-treat and severe asthma |
| [36573485](https://pubmed.ncbi.nlm.nih.gov/36573485/) | 2022 | Review | Recent Prog Med | BDP as first ICS molecule (1970s); effective via nebulizers and pMDI in reducing asthma symptom frequency and severity with high safety profile |
| [9657561](https://pubmed.ncbi.nlm.nih.gov/9657561/) | 1998 | RCT | Eur Respir J | Low-dose BDP (336 mcg/day) significantly improves asthma control and reduces airway inflammation markers vs placebo in mild–moderate asthma |
| [3194866](https://pubmed.ncbi.nlm.nih.gov/3194866/) | 1988 | RCT | Thorax | Crossover study in chronic asthma: inhaled BDP 1200 mcg/day equivalent to oral prednisone 12.5 mg/day in reducing bronchial hyperresponsiveness |
| [6792963](https://pubmed.ncbi.nlm.nih.gov/6792963/) | 1981 | Review | Ann Intern Med | 5-year clinical experience confirming BDP as effective topical corticosteroid; most steroid-dependent asthmatics controllable; dose-dependent therapeutic effect |
| [1095170](https://pubmed.ncbi.nlm.nih.gov/1095170/) | 1975 | Clinical Report | Can Med Assoc J | In 41 perennial asthma patients, 12/31 steroid-dependent patients discontinued oral prednisone; 15/31 reduced maintenance dose with BDP aerosol |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |
| (Details not available) | — | — | — |

> **Note:** A total of 27 registrations are recorded as marketed in Malaysia, but the detailed license information (authorization numbers, product names, dosage forms, approved indications) was not available in the current dataset. Please consult the NPRA database for full details.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

---

## Additional Predicted Indications

Beyond the primary prediction, TxGNN also identified the following related indications for BDP:

| Rank | Disease | Evidence Level | Clinical Trials | Publications | Recommendation |
|------|---------|---------------|----------------|-------------|----------------|
| 2 | Allergic Asthma | L1 | 8 | 20 | Proceed with Guardrails |
| 3 | Rhinitis | L1 | 23 | 20 | Proceed with Guardrails |
| 4 | Intrinsic Asthma | L3 | 0 | 15 | Proceed with Guardrails |
| 5 | Vasomotor Rhinitis | L3 | 0 | 15 | Proceed with Guardrails |

**Key observations:**

- **Allergic Asthma (Rank 2):** BDP's mechanism perfectly matches the Th2/IgE-mediated eosinophilic inflammation underlying allergic asthma. Multiple Phase 3 RCTs (e.g., NCT00988247, N=529) directly support this indication.
- **Rhinitis (Rank 3):** BDP intranasal spray is already a first-line therapy for allergic rhinitis. Six completed Phase 3 trials with over 3,000 total subjects provide robust evidence.
- **Intrinsic Asthma (Rank 4):** No registered clinical trials but 15 publications including direct clinical studies (PMID 1841740, PMID 329663) demonstrate efficacy of high-dose BDP in corticosteroid-dependent intrinsic asthma. The broader anti-inflammatory mechanism applies, though effect may be less consistent than in eosinophilic asthma.
- **Vasomotor Rhinitis (Rank 5):** No registered clinical trials but controlled studies (PMID 782135, PMID 782136) from the 1970s demonstrate BDP significantly reduces symptoms of vasomotor rhinitis vs placebo. A 2009 systematic review (PMID 24228841) confirms intranasal corticosteroids' role in VMR.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
BDP is one of the most extensively studied inhaled corticosteroids in the history of respiratory medicine. The TxGNN prediction for asthma aligns perfectly with over 50 years of clinical evidence, including dozens of completed Phase 3 RCTs with thousands of patients. All five predicted indications fall within the established pharmacological profile of this drug, effectively serving as a strong positive validation of the TxGNN model.

**To proceed, the following is needed:**
- Complete the Malaysia NPRA registration details (27 licenses identified but specifics are missing)
- Obtain detailed mechanism of action (MOA) data from DrugBank to formalise the mechanistic rationale
- Retrieve package insert safety information (key warnings, contraindications, drug interactions) from the NPRA database
- For intrinsic asthma and vasomotor rhinitis (L3 evidence), consider systematic literature review to consolidate existing evidence before formal repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

