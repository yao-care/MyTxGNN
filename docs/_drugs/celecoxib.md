---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 5
---

# Celecoxib
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

# Celecoxib: From NSAID Pain/Inflammation Management to Osteoarthritis (Already-Approved Use — Not a Novel Indication)

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor already marketed for pain and inflammation control; the TxGNN model's top output for this candidate is **Osteoarthritis**, but the evidence pack's own rationale confirms this is celecoxib's existing, long-approved indication rather than a genuine repurposing hypothesis. **50 clinical trials** and **20 publications** exist for celecoxib in osteoarthritis, but this volume reflects decades of label-confirming research, not new-use discovery — the model appears to have re-surfaced a known indication rather than found a repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from source records (all 5 TFDA/NPRA license entries returned empty `approved_indication_text`); per the evidence pack's own rationale, celecoxib is already indicated for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis pain/inflammation |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 22 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this candidate is flagged as a data gap (`original_moa: [Data Gap]`). Based on information embedded in the evidence pack's repurposing rationale, celecoxib is a selective COX-2 inhibitor that blocks prostaglandin synthesis to relieve joint inflammation and pain — the standard pharmacological mechanism underlying its use in osteoarthritis (OA), rheumatoid arthritis (RA), and ankylosing spondylitis (AS).

However, the rationale text explicitly notes that this mechanistic link is **not a novel hypothesis**: "Celecoxib (Celebrex) is itself an FDA-approved OA drug; this represents an existing indication rather than a repurposing candidate." The same conclusion applies to the model's other four ranked outputs — rheumatoid arthritis and ankylosing spondylitis are also existing, guideline-recommended celecoxib indications, while "spondyloarthropathy, susceptibility to" and "osteoarthritis susceptibility" are GWAS/OMIM genetic-susceptibility entries, not treatable clinical disease entities, and carry only weak, largely coincidental literature support (case reports, unrelated cohort studies).

In short: the abundance of clinical and literature evidence here confirms celecoxib's established efficacy in OA/RA/AS, but it does not support a new-use repurposing claim. This candidate should likely be flagged for exclusion from the active repurposing pipeline rather than advanced.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01554163](https://clinicaltrials.gov/study/NCT01554163) | Phase 3 | Completed | 239 | Etoricoxib 30 mg vs. celecoxib 200 mg in Korean OA patients — non-inferiority/safety comparison |
| [NCT02528188](https://clinicaltrials.gov/study/NCT02528188) | Phase 3 | Completed | 3021 | Long-term tanezumab vs. NSAID (incl. celecoxib background) safety/efficacy in hip/knee OA |
| [NCT00476034](https://clinicaltrials.gov/study/NCT00476034) | Phase 3 | Completed | 1312 | 39-week extension of core trial comparing lumiracoxib vs. celecoxib 200 mg in knee OA |
| [NCT00373685](https://clinicaltrials.gov/study/NCT00373685) | Phase 4 | Completed | 8067 | GI-REASONS: GI safety of celecoxib vs. non-selective NSAIDs in OA patients |
| [NCT00145301](https://clinicaltrials.gov/study/NCT00145301) | Phase 3 | Completed | 3036 | 52-week retention/safety/efficacy comparison of lumiracoxib doses vs. celecoxib 200 mg in OA |
| [NCT00640627](https://clinicaltrials.gov/study/NCT00640627) | Phase 4 | Completed | 380 | Celebrex (celecoxib) vs. placebo in knee OA non-responsive to naproxen/ibuprofen |
| [NCT00092768](https://clinicaltrials.gov/study/NCT00092768) | Phase 3 | Completed | 500 | Etoricoxib 30 mg vs. celecoxib 200 mg safety/efficacy in hip/knee OA |
| [NCT00630929](https://clinicaltrials.gov/study/NCT00630929) | Phase 4 | Completed | 388 | Celebrex once-daily vs. ibuprofen three-times-daily vs. placebo in knee OA |
| [NCT00581685](https://clinicaltrials.gov/study/NCT00581685) | Phase 3 | Completed | 31 | Celecoxib + pregabalin for post-total-hip-arthroplasty pain control |
| [NCT00565500](https://clinicaltrials.gov/study/NCT00565500) | Phase 4 | Completed | 24 | Aspirin–celecoxib interaction study in OA patients with stable ischemic heart disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27196460](https://pubmed.ncbi.nlm.nih.gov/27196460/) | 2016 | Meta-Analysis | Medicine | Meta-analysis confirming efficacy and safety of celecoxib (COX-2 inhibitor) in osteoarthritis |
| [16495392](https://pubmed.ncbi.nlm.nih.gov/16495392/) | 2006 | RCT | New England Journal of Medicine | GAIT trial — glucosamine/chondroitin vs. celecoxib-controlled arm for knee OA pain |
| [34932581](https://pubmed.ncbi.nlm.nih.gov/34932581/) | 2021 | Systematic Review | PLoS One | Cardiovascular safety of celecoxib in RA and OA patients |
| [30575881](https://pubmed.ncbi.nlm.nih.gov/30575881/) | 2018 | Systematic Review/Meta-analysis | JAMA | Long-term pain control across pharmacologic agents (incl. celecoxib) in knee OA |
| [25560713](https://pubmed.ncbi.nlm.nih.gov/25560713/) | 2015 | Review/Network Meta-analysis | Annals of Internal Medicine | Comparative effectiveness of pharmacologic interventions for knee OA |
| [28530031](https://pubmed.ncbi.nlm.nih.gov/28530031/) | 2017 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | "Celecoxib for osteoarthritis" — formal Cochrane review |
| [25589511](https://pubmed.ncbi.nlm.nih.gov/25589511/) | 2016 | RCT | Annals of the Rheumatic Diseases | Non-inferiority trial: chondroitin+glucosamine vs. celecoxib for painful knee OA |
| [26576862](https://pubmed.ncbi.nlm.nih.gov/26576862/) | 2015 | Meta-analysis | Scientific Reports | Effectiveness/safety of glucosamine, chondroitin, combination, or celecoxib in knee OA |
| [10804043](https://pubmed.ncbi.nlm.nih.gov/10804043/) | 2000 | Review | Drugs | Foundational review of celecoxib use in OA, RA, and acute pain |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Review | Drugs | Celecoxib review covering OA, RA, and ankylosing spondylitis symptomatic relief |

---

## Malaysia Market Information

Individual license-level fields (authorization number, product name, dosage form, manufacturer, approved indication text) were all returned empty by the source query and cannot be tabulated. What is confirmed: **22 active registrations** are on file and the product's overall market status is **✓ Marketed** in Malaysia.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were all returned as data gaps in this evidence pack; the DDI query itself returned `not_found`.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate does not represent a genuine repurposing opportunity. The top-ranked prediction (osteoarthritis) and the third-ranked prediction (rheumatoid arthritis) are already-approved celecoxib indications, and the fifth-ranked prediction (ankylosing spondylitis) is also standard guideline-recommended use — the abundant clinical/literature evidence confirms existing efficacy rather than a new hypothesis. The two remaining candidates ("spondyloarthropathy, susceptibility to" and "osteoarthritis susceptibility") are genetic-susceptibility ontology entries, not treatable diseases, and are supported only by incidental case-report/cohort literature (Evidence Level L4, Decision Stage S0). All five entries in this evidence pack independently arrive at a "Hold" recommendation.

**To proceed, the following is needed:**
- Recommend flagging candidate `TW-DB00482-multi` for exclusion from the active repurposing pipeline rather than advancing it, since no candidate here clears S1 (osteoarthritis/RA/AS are label overlap; the two susceptibility entries are non-actionable ontology artifacts)
- If label-expansion or safety-monitoring work is pursued regardless, DG001 (TFDA/NPRA package-insert warnings and contraindications) is a **Blocking** gap and must be resolved before any S1 safety screening
- DG002 (mechanism-of-action confirmation via DrugBank API) should be resolved to replace the rationale-text-derived MOA summary used in this report with a verified source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

