---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 654
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody, originally developed and approved for rheumatoid arthritis and other IL-6-driven inflammatory conditions. The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, with **9 clinical trials** and **19 publications** currently available — however, the two pivotal Phase 3 trials in this indication (BUILDER-1/BUILDER-2) were **terminated early**, and the published results suggest the efficacy signal was not strong enough to support the indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (well-established indication for tocilizumab; not recorded in this evidence pack — see Data Gaps) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Malaysia Market Status | Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, tocilizumab is a humanized monoclonal antibody that blocks the interleukin-6 (IL-6) receptor, inhibiting IL-6-mediated signaling. It is an established treatment for rheumatoid arthritis, systemic and polyarticular juvenile idiopathic arthritis, and giant cell arteritis — all conditions where IL-6 plays a central pathogenic role.

Ankylosing spondylitis (AS) shares broad pathophysiological features with these approved indications: chronic synovial/axial inflammation, elevated inflammatory cytokines, and a similar treatment ladder (NSAIDs → biologic DMARDs). This overlap is a reasonable basis for the TxGNN model's high prediction score, and is reinforced by the fact that two other candidates in this same prediction run — polyarticular juvenile rheumatoid arthritis (rank 7) and juvenile idiopathic arthritis (rank 9) — are indications where tocilizumab is *already* approved, indicating the model correctly recovers known truths alongside novel candidates.

However, AS pathogenesis is now understood to be driven predominantly by the IL-17/IL-23 and TNF axes rather than IL-6, which is the most likely biological explanation for why dedicated tocilizumab trials in AS did not succeed. This is a case where mechanistic plausibility exists, but the disease-specific biology differs enough from tocilizumab's proven indications that clinical validation is essential — and in this case, that validation has already returned a negative signal (see Clinical Trial Evidence below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | **Terminated** | 113 | RCT of tocilizumab (8 mg/kg or 4 mg/kg IV) vs placebo in AS patients with inadequate response to prior TNF antagonist therapy |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | **Terminated** | 306 | RCT of tocilizumab vs placebo in TNF-naïve AS patients who failed NSAIDs; two-part design evaluating signs/symptoms and structural damage |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean nationwide registry tracking real-world safety of biologics/targeted synthetic DMARDs in RA, AS, and PsA |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Multi-centre observational study profiling blood cytokine biomarkers across systemic inflammatory diseases |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | National real-world registry of patients treated with Inflectra (infliximab biosimilar); indirect comparator context |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large-scale study of incident immune-mediated inflammatory disease (IMID) risk in patients on biologics/immunosuppressants |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper and B cell maturation in RA patients |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Secukinumab (not tocilizumab) in Takayasu arteritis; tangential IL-6 pathway relevance |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty |

**Note:** The two disease-specific Phase 3 RCTs in AS were both **terminated**, not completed as planned — this is the most important signal in the evidence base and directly affects the evidence level and recommendation below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Annals of the Rheumatic Diseases | BUILDER-1/BUILDER-2: assessed short-term symptomatic efficacy of tocilizumab in AS; corresponds to the two terminated Phase 3 trials above |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-analysis | Medicine | Comparative effectiveness of biologic therapy regimens for AS across RCTs |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Short review on antagonizing IL-6 specifically in AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clinical Rheumatology | Risk of serious infections with biologics in AS/non-radiographic axial SpA |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporosis International | Systemic bone effects of biologic therapies in RA and AS |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Review | Open Access Rheumatology | Overview of biologics in RA, AS, and PsA |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clinical and Experimental Rheumatology | Biologics in RA and AS treatment, mechanistic differences |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Current Opinion in Rheumatology | Treatment alternatives for AS refractory to TNF inhibition |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Second-line biologic therapy optimization in RA, PsA, AS |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case Report | Joint Bone Spine | Tocilizumab in a patient with AS and Crohn's disease refractory to TNF antagonists |

---

## Malaysia Market Information

NPRA records show tocilizumab as **Marketed** in Malaysia with **2 registrations**, but this evidence pack does not contain license numbers, product names, dosage forms, or approved-indication text for either registration — these fields were returned empty by the source query and would need to be re-pulled from NPRA directly.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack has a **Blocking** data gap (DG001: TFDA/NPRA label warnings and contraindications not yet retrieved), which means the safety profile for this drug has not been reviewed and no S1 safety screening can be completed until it is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale for AS is plausible but weaker than tocilizumab's proven IL-6-driven indications, and this is borne out clinically: both dedicated Phase 3 RCTs in AS (BUILDER-1/BUILDER-2) were **terminated** rather than completed, with the published report only assessing short-term symptomatic efficacy — consistent with a program that did not reach its efficacy bar.
- Safety review cannot proceed because the required TFDA/NPRA label data (warnings, contraindications) is a **Blocking** data gap and has not been supplied.

**To proceed, the following is needed:**
- Retrieval of the full BUILDER-1/BUILDER-2 primary results (ASAS20/ASAS40 outcomes) to confirm the reason for termination and the magnitude of the efficacy shortfall
- TFDA/NPRA package insert (warnings, contraindications) per DG001, before any S1 safety evaluation can begin
- DrugBank-sourced mechanism of action data per DG002, to strengthen the mechanistic rationale write-up
- Malaysia license-level detail (product names, dosage forms, approved indication text) for the 2 existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

