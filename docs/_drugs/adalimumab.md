---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 5
---

# Adalimumab
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

# Adalimumab: From Rheumatoid Arthritis to Inflammatory Bowel Disease

## One-Sentence Summary

Adalimumab (Humira; DrugBank DB00051) is a fully human monoclonal antibody targeting TNF-α, first approved for the treatment of rheumatoid arthritis (FDA, 2002), and is one of the best-selling biologics worldwide.
The TxGNN model ranks **Inflammatory Bowel Disease (IBD)** — encompassing Crohn's Disease (CD) and Ulcerative Colitis (UC) — as its top predicted repurposing indication.
With **50 registered clinical trials** and **20 publications** identified in this evidence pack, and FDA approvals already in place for CD (2007) and UC (2012), the evidence base is among the most robust in biological therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis (Malaysia registration details unavailable in current data) |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's Disease & Ulcerative Colitis) |
| TxGNN Prediction Score | N/A (raw score data unavailable) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 12 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Adalimumab is a fully human IgG1 monoclonal antibody that binds with high affinity to both soluble and transmembrane forms of TNF-α, blocking its interaction with TNFR1 and TNFR2 receptors. This blockade suppresses downstream NF-κB pathway activation, reducing pro-inflammatory cytokine production and immune cell recruitment. Originally developed for rheumatoid arthritis — a Th1/TNF-α–driven disease of synovial tissue — the exact same molecular pathway is central to IBD pathophysiology.

In both Crohn's Disease and Ulcerative Colitis, TNF-α is overproduced by activated macrophages and Th1 cells within the intestinal lamina propria, driving mucosal epithelial barrier damage, sustained immune cell infiltration, and progressive intestinal fibrosis. The mechanistic overlap between articular and intestinal TNF-α–mediated chronic inflammation is well established, providing a strong scientific rationale for efficacy across both organ systems.

This prediction has been clinically validated: adalimumab received FDA approval for moderate-to-severe Crohn's Disease in 2007, followed by Ulcerative Colitis in 2012, based on pivotal Phase 3 RCTs. Single-cell transcriptomic studies have further characterised the cellular changes in IBD gut tissue following adalimumab treatment — identifying 109 distinct cell states and revealing disease-specific immune modulation across CD and UC subtypes. The TxGNN model's top-ranked prediction for IBD thus directly aligns with the drug's established clinical approval landscape, confirming mechanistic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00408629](https://clinicaltrials.gov/study/NCT00408629) | Phase 3 | Completed | 518 | Pivotal randomised, double-blind, placebo-controlled RCT demonstrating efficacy and safety of adalimumab for induction and maintenance of remission in moderately-to-severely active Ulcerative Colitis |
| [NCT00409617](https://clinicaltrials.gov/study/NCT00409617) | Phase 3 | Completed | 945 | Large-scale open-label study evaluating safety, quality-of-life outcomes, fistula healing, and extra-intestinal manifestations of adalimumab in moderate-to-severe Crohn's Disease |
| [NCT00055497](https://clinicaltrials.gov/study/NCT00055497) | Phase 3 | Completed | 276 | Randomised, double-blind, placebo-controlled trial demonstrating adalimumab's efficacy in maintenance of clinical remission in Crohn's Disease up to 56 weeks |
| [NCT02065557](https://clinicaltrials.gov/study/NCT02065557) | Phase 3 | Completed | 101 | Multicenter RCT evaluating efficacy, safety, and pharmacokinetics of adalimumab subcutaneous injection in paediatric patients with moderate-to-severe Ulcerative Colitis |
| [NCT00055523](https://clinicaltrials.gov/study/NCT00055523) | Phase 2 | Completed | 300 | Early placebo-controlled study demonstrating adalimumab's ability to induce clinical remission in active Crohn's Disease versus placebo, forming the foundational Phase 2 evidence base |
| [NCT02738125](https://clinicaltrials.gov/study/NCT02738125) | N/A | Completed | 265 | Large real-world observational study assessing long-term effectiveness of adalimumab in UC patients using a time-to-event approach for loss of clinical benefit |
| [NCT06269185](https://clinicaltrials.gov/study/NCT06269185) | N/A | Completed | 271 | Retrospective multicenter cohort comparing short- and long-term efficacy of infliximab versus adalimumab in UC patients; meta-analyses suggest comparable real-world outcomes despite IFX superiority in RCT induction |
| [NCT03917303](https://clinicaltrials.gov/study/NCT03917303) | Phase 4 | Recruiting | 158 | Ongoing Phase 4 trial evaluating episodic adalimumab monotherapy as first-line treatment in Crohn's Disease to determine whether step-up therapy can prevent overtreatment of low-risk patients |
| [NCT05598684](https://clinicaltrials.gov/study/NCT05598684) | N/A | Unknown | 600 | Prospective multicentre cohort (n=600) identifying predictive factors for treatment persistence on adalimumab biosimilar (Fresenius Kabi) in chronic inflammatory diseases including IBD |
| [NCT03710486](https://clinicaltrials.gov/study/NCT03710486) | N/A | Completed | 409 | Real-world comparative effectiveness study of vedolizumab versus anti-TNF agents (including adalimumab as comparator) in both UC and CD patients at ≥6 months post-initiation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38985232](https://pubmed.ncbi.nlm.nih.gov/38985232/) | 2024 | Systematic Review/Meta-analysis | Inflammopharmacology | Comprehensive meta-analysis comparing efficacy and safety of infliximab and adalimumab in both UC and CD; both agents demonstrated significant clinical benefit in moderate-to-severe IBD |
| [40088372](https://pubmed.ncbi.nlm.nih.gov/40088372/) | 2025 | Systematic Review/Meta-analysis | Inflammopharmacology | Head-to-head systematic review and meta-analysis comparing efficacy, safety, and treatment persistence of vedolizumab versus adalimumab across IBD populations |
| [39438660](https://pubmed.ncbi.nlm.nih.gov/39438660/) | 2024 | Cohort (Single-cell) | Nature Immunology | Therapeutic atlas of ~1 million single-cell transcriptomes from 216 gut biopsies in 41 IBD subjects treated with adalimumab (anti-TNF); identified 109 cell states and CD/UC-specific differences in treatment response |
| [27567553](https://pubmed.ncbi.nlm.nih.gov/27567553/) | 2018 | Mechanism Review | Cytokine | Comparative analysis of molecular mechanisms of anti-TNF-α agents, elucidating the differential binding profiles of adalimumab, infliximab, golimumab, certolizumab, and etanercept to soluble vs. transmembrane TNF-α |
| [31039560](https://pubmed.ncbi.nlm.nih.gov/31039560/) | 2019 | Cohort | Digestive Diseases | Demonstrated relationship between adalimumab serum trough levels and clinical efficacy in IBD; established therapeutic drug monitoring (TDM) framework for dose optimisation |
| [32032073](https://pubmed.ncbi.nlm.nih.gov/32032073/) | 2020 | Systematic Review/Meta-analysis | American Journal of Gastroenterology | Meta-analysis evaluating TB risk in IBD patients receiving infliximab or adalimumab; risk is dependent on local TB disease burden — directly relevant to Malaysia's TB epidemiology |
| [34388361](https://pubmed.ncbi.nlm.nih.gov/34388361/) | 2021 | Review | Lancet Gastroenterology & Hepatology | Expert commentary on adalimumab biosimilars in IBD, addressing clinical interchangeability, switching safety, and pharmacoeconomic access implications |
| [37847820](https://pubmed.ncbi.nlm.nih.gov/37847820/) | 2024 | Cohort | Inflammatory Bowel Diseases | Patterns of anti-TNF use (including adalimumab) in very early onset IBD (<6 years old); reported comparable safety and efficacy signals despite lack of formal paediatric approvals in this subgroup |
| [30864505](https://pubmed.ncbi.nlm.nih.gov/30864505/) | 2019 | Review | Current Pharmaceutical Design | Comprehensive review on adalimumab biosimilar readiness in IBD clinical practice, including extrapolation evidence across indications and switching protocol considerations |
| [37070385](https://pubmed.ncbi.nlm.nih.gov/37070385/) | 2023 | Cohort | Expert Opinion on Biological Therapy | Australian real-world comparison of originator versus biosimilar adalimumab in IBD; highlights differences in injection device design, citrate-free formulations, and patient satisfaction factors relevant to prescriber decision-making |

---

## Malaysia Market Information

The National Pharmaceutical Regulatory Agency (NPRA) records indicate Adalimumab holds **12 active registrations** in Malaysia with a confirmed marketed status. However, individual product details — including authorisation numbers, product names, dosage forms, manufacturers, and approved indication texts — were not available in the current data extract.

Please consult the NPRA online database (https://www.npra.gov.my/) directly to retrieve complete registration details and confirm which specific IBD indications (Crohn's Disease and/or Ulcerative Colitis) are included in the locally approved prescribing information.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note for clinical use:** Detailed key warnings, contraindications, and drug interaction data were identified as data gaps in this evidence pack. Prior to any clinical or formulary decision, the following anti-TNF class-level safety signals should be verified against the current NPRA-approved prescribing information:
>
> - **Serious infections and TB reactivation**: Mandatory TB screening before initiation; risk heightened in Malaysia's intermediate TB-burden setting (see PMID [32032073](https://pubmed.ncbi.nlm.nih.gov/32032073/))
> - **Malignancy (lymphoma, NMSC)**: Long-term post-marketing surveillance data flag increased risk, particularly with concomitant immunosuppressants (thiopurines)
> - **Heart failure**: Contraindicated in NYHA Class III/IV heart failure
> - **Hepatitis B reactivation**: Screen all patients for HBV before initiation
>
> *Source: NPRA product insert retrieval is listed as a required next step (see below).*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Adalimumab's efficacy in Inflammatory Bowel Disease is supported by multiple completed Phase 3 RCTs and confirmed by FDA approvals for both Crohn's Disease (2007) and Ulcerative Colitis (2012) — placing this at the highest tier of clinical evidence (L1). The 12 active Malaysia registrations confirm commercial availability; however, full safety and indication data for the local label must be verified before any formulary or treatment access decision is finalised.

**To proceed, the following is needed:**

- **[Critical]** Download and parse NPRA product insert PDFs for all 12 registered Adalimumab products to extract approved indications, key warnings, and contraindications (resolves DG001)
- **[High]** Query DrugBank API for DB00051 to retrieve the complete mechanism of action, pharmacodynamic profile, and drug interaction data (resolves DG002)
- **[Required]** Confirm whether IBD indications (CD and UC separately) are explicitly listed in Malaysia-approved labelling, or whether off-label use protocols apply
- **[Recommended]** Given Malaysia's TB burden, establish a local TB pre-screening protocol aligned with national TB guidelines before any adalimumab initiation for IBD
- **[Recommended]** For paediatric IBD or pregnant patients, compile a specific population risk-benefit summary drawing on PMID [37847820](https://pubmed.ncbi.nlm.nih.gov/37847820/) and NCT02065557 data

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This document should be reviewed by qualified clinical pharmacists and physicians prior to any treatment or formulary decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

