---
layout: default
title: Bedaquiline
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Bedaquiline
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

# Bedaquiline: From Pulmonary MDR-TB Treatment to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Bedaquiline is a diarylquinoline antimycobacterial agent approved for the treatment of pulmonary multidrug-resistant tuberculosis (MDR-TB) as part of combination therapy.
The TxGNN model predicts it to be effective for **Multidrug-Resistant Tuberculosis** with a score of 99.98%, which effectively validates the drug's existing approved indication.
With **50 clinical trials** and **20 publications** supporting this direction, the evidence base is exceptionally strong — and the model further identifies potential extensions to **inactive tuberculosis**, **tuberculoma**, **bovine tuberculosis**, and **cutaneous tuberculosis** as repurposing candidates.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary multidrug-resistant tuberculosis (MDR-TB), as part of combination therapy |
| Predicted New Indication | Multidrug-resistant tuberculosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Bedaquiline (formerly TMC207) is a first-in-class diarylquinoline that selectively inhibits the mycobacterial F₀F₁-ATP synthase, blocking the oxidative phosphorylation pathway that *Mycobacterium tuberculosis* depends on for energy production. This novel mechanism of action is distinct from all existing anti-TB drugs and is effective against both actively replicating and dormant bacilli, making it particularly valuable against drug-resistant strains that have acquired resistance to conventional agents like isoniazid and rifampicin.

The TxGNN model's top prediction of multidrug-resistant tuberculosis for bedaquiline serves as a strong **model validation signal** — the algorithm independently identifies the drug's already-approved indication with near-perfect confidence (99.98%). This finding confirms the model's ability to detect genuine drug-disease relationships through knowledge graph analysis.

Beyond this validation, the model identifies several biologically plausible repurposing candidates within the tuberculosis spectrum: inactive (latent) tuberculosis (rank 5, L2 evidence), tuberculoma (rank 6, L4), bovine tuberculosis (rank 2, L4), and cutaneous tuberculosis (rank 10, L4). These predictions are mechanistically coherent, as all involve *Mycobacterium* species sharing the conserved ATP synthase target. Notably, the prediction for inactive tuberculosis is actively being tested in a landmark Phase 2/3 trial (BREACH-TB, NCT06568484, n=2,530), further validating the model's predictive utility.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02754765](https://clinicaltrials.gov/study/NCT02754765) | Phase 3 | Completed | 754 | endTB trial: largest multi-country RCT evaluating five all-oral shortened regimens containing bedaquiline for MDR-TB efficacy and safety |
| [NCT02409290](https://clinicaltrials.gov/study/NCT02409290) | Phase 3 | Completed | 588 | STREAM Stage 2: evaluated standard treatment regimens including bedaquiline-containing arm for MDR-TB |
| [NCT02589782](https://clinicaltrials.gov/study/NCT02589782) | Phase 2/3 | Completed | 552 | TB-PRACTECAL: multi-arm RCT evaluating bedaquiline + pretomanid combination regimens for MDR-TB; demonstrated superiority of BPaL-based regimens |
| [NCT04062201](https://clinicaltrials.gov/study/NCT04062201) | Phase 3 | Completed | 402 | BEAT-TB: 6-month BDQ+DLM+LZD+LVX+CFZ regimen vs. South African standard of care for RR-TB |
| [NCT03896685](https://clinicaltrials.gov/study/NCT03896685) | Phase 3 | Completed | 323 | endTB-Q: two all-oral shortened regimens for MDR-TB with fluoroquinolone resistance |
| [NCT00910871](https://clinicaltrials.gov/study/NCT00910871) | Phase 2 | Completed | 241 | C209 pivotal open-label trial: bedaquiline + individualized background regimen for MDR-TB; key efficacy and safety data supporting regulatory approval |
| [NCT00449644](https://clinicaltrials.gov/study/NCT00449644) | Phase 2 | Completed | 208 | C208: first randomized, placebo-controlled trial demonstrating bedaquiline's antibacterial activity superiority over placebo in newly diagnosed MDR-TB |
| [NCT03086486](https://clinicaltrials.gov/study/NCT03086486) | Phase 3 | Completed | 181 | ZeNix trial: optimized linezolid dosing within BPaL regimen for XDR-TB and treatment-intolerant MDR-TB |
| [NCT02333799](https://clinicaltrials.gov/study/NCT02333799) | Phase 3 | Completed | 109 | Nix-TB: BPaL regimen (bedaquiline + pretomanid + linezolid) for XDR/treatment-intolerant MDR-TB; results led to pretomanid FDA approval |
| [NCT05081401](https://clinicaltrials.gov/study/NCT05081401) | Phase 3 | Recruiting | 1,050 | INSPIRE-TB: pragmatic RCT evaluating seven 9-month oral regimens for RR-TB, the largest ongoing bedaquiline combination trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32130813](https://pubmed.ncbi.nlm.nih.gov/32130813/) | 2020 | Landmark Trial | N Engl J Med | BPaL regimen achieved high treatment success in highly drug-resistant pulmonary TB with historically poor outcomes |
| [35649043](https://pubmed.ncbi.nlm.nih.gov/35649043/) | 2022 | Systematic Review / Meta-Analysis | J Bras Pneumol | Bedaquiline-containing regimens for MDR-TB demonstrated high treatment success rates across pooled studies |
| [40172415](https://pubmed.ncbi.nlm.nih.gov/40172415/) | 2025 | Systematic Review / Meta-Analysis | J Bras Pneumol | Meta-analysis confirmed bedaquiline + linezolid regimens enhance MDR-TB treatment outcomes |
| [32192585](https://pubmed.ncbi.nlm.nih.gov/32192585/) | 2020 | IPD Meta-Analysis | Lancet Respir Med | Individual patient data analysis of drug-associated adverse events in MDR-TB treatment, informing risk-benefit assessment |
| [36331978](https://pubmed.ncbi.nlm.nih.gov/36331978/) | 2023 | Systematic Review / Meta-Analysis | Clin Infect Dis | Concomitant bedaquiline + delamanid use showed favorable treatment outcomes with manageable QTc prolongation risk |
| [31526739](https://pubmed.ncbi.nlm.nih.gov/31526739/) | 2019 | Review | Lancet | Comprehensive management of drug-resistant TB, positioning bedaquiline as a cornerstone of modern MDR-TB regimens |
| [39431709](https://pubmed.ncbi.nlm.nih.gov/39431709/) | 2024 | Narrative Review | J Clin Lab Anal | Overview of bedaquiline and delamanid antimicrobial characteristics, resistance mechanisms, synergism, and side effects |
| [32700565](https://pubmed.ncbi.nlm.nih.gov/32700565/) | 2020 | Clinical Review | Future Microbiol | Clinician's perspective on bedaquiline and delamanid use in drug-resistant TB, summarizing observational and trial evidence |
| [33837767](https://pubmed.ncbi.nlm.nih.gov/33837767/) | 2021 | Cohort Study | Clin Infect Dis | Real-world comparison of bedaquiline vs. delamanid treatment outcomes in MDR/RR-TB patients in South Korea |
| [39537610](https://pubmed.ncbi.nlm.nih.gov/39537610/) | 2024 | Basic Science | Nat Commun | Catalase activity deficiency sensitizes MDR-TB to bedaquiline, elucidating a novel mechanism for enhanced efficacy against isoniazid-resistant strains |

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Registration number not available) | Bedaquiline product | (Not specified) | (Indication text not available in registry data) |

> **Note:** Bedaquiline is registered and marketed in Malaysia (1 authorization). Detailed product information including authorization number, product name, dosage form, and approved indication text were not available in the current data extraction. Please refer to the NPRA database for complete registration details.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Known class concerns based on published literature** (not from registry data):
> - **QTc prolongation**: Bedaquiline is associated with QT interval prolongation; ECG monitoring is recommended during treatment
> - **Hepatotoxicity**: Liver function monitoring is advised
> - **Drug interactions**: As a CYP3A4 substrate, co-administration with strong CYP3A4 inducers (e.g., rifampicin) significantly reduces bedaquiline exposure; co-administration with CYP3A4 inhibitors may increase exposure
> - **Mortality signal**: An early Phase 2 trial (C208) noted a numerical imbalance in deaths in the bedaquiline arm, though subsequent larger studies have not confirmed a causal relationship
>
> ⚠️ *Formal safety data (package insert warnings, contraindications, DDI) were not available in the evidence pack. The above points are derived from published clinical literature and should be verified against the approved prescribing information.*

## Additional Repurposing Candidates

Beyond the primary validation prediction, the TxGNN model identified the following repurposing candidates of potential clinical interest:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Rationale |
|------|---------|-------------|---------------|----------------|---------------|
| 2 | Bovine tuberculosis | 99.96% | L4 | Research Question | *M. bovis* shares highly conserved ATP synthase with *M. tuberculosis*; in vitro activity confirmed but no clinical data |
| 5 | Inactive (latent) tuberculosis | 99.96% | L2 | Proceed with Guardrails | Dormant *M. tuberculosis* relies on oxidative phosphorylation; a landmark Phase 2/3 trial (BREACH-TB, n=2,530) is underway |
| 6 | Tuberculoma | 99.96% | L4 | Research Question | Granulomatous TB lesion; case reports support BPaL regimen use, but CNS/tissue penetration data needed |
| 10 | Cutaneous tuberculosis | 99.70% | L4 | Research Question | Same pathogen; skin drug penetration and local concentration require verification |

> **Note:** Predictions for vulvovaginal candidiasis (rank 7), fascioliasis (rank 8), and urea cycle disorder (rank 9) lack mechanistic rationale and are classified as **Hold** — bedaquiline's ATP synthase inhibition is highly selective for mycobacteria and has no established basis for activity against fungi, parasites, or metabolic disorders.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for bedaquiline in MDR-TB is a strong model validation case, supported by L1-level evidence including multiple completed Phase 3 RCTs (endTB, STREAM, TB-PRACTECAL, BEAT-TB, ZeNix, Nix-TB) enrolling thousands of patients. Bedaquiline is already a WHO-recommended cornerstone of modern MDR-TB treatment. The more novel and actionable repurposing opportunity lies in **inactive (latent) tuberculosis prevention**, which has L2-level evidence and a major ongoing Phase 2/3 trial (BREACH-TB).

**To proceed, the following is needed:**
- **Complete Malaysia regulatory data**: Obtain full NPRA registration details (authorization number, product name, approved indication text)
- **Package insert safety data**: Download and parse the approved prescribing information for formal warnings, contraindications, and drug-drug interactions
- **Mechanism of action documentation**: Retrieve detailed MOA data from DrugBank (ATP synthase subunit c inhibition)
- **Latent TB indication development**: Monitor BREACH-TB trial (NCT06568484) results for potential label expansion to tuberculosis preventive therapy
- **Pharmacokinetic gap analysis**: For tissue-specific indications (tuberculoma, cutaneous TB), assess drug penetration data in granuloma, CNS, and skin compartments

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

