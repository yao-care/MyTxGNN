---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

> **Note on candidate selection**: TxGNN's top-ranked hit by raw score (*congenital hypotrichosis with juvenile macular dystrophy*, 99.65%) has zero supporting trials or literature and is explicitly flagged in the evidence pack as a likely knowledge-graph artifact — as are 3 other L5 candidates (seborrheic keratosis, osteoarthritis susceptibility, vulvar inverted follicular keratosis, pseudoachondroplasia). This report instead evaluates **Rheumatoid Arthritis**, the candidate with the strongest actual evidence (6 trials, 20 publications). **Osteoarthritis** (rank 2, L4) is also evidence-backed via a 2024 mechanistic study and is worth tracking, but has zero clinical trials.

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid) is the active metabolite of sulfasalazine and is established for inflammatory bowel disease. TxGNN and the literature suggest a link to **Rheumatoid Arthritis**, since sulfasalazine — which is cleaved into mesalazine and sulfapyridine — is a long-established DMARD for RA. However, older pharmacology studies attribute the RA effect mainly to the sulfapyridine moiety, not mesalazine itself, so the case rests on indirect (parent-compound) evidence with **6 clinical trials** (only 2 directly relevant, both terminated) and **20 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis (inferred from literature evidence; formal NPRA-approved indication text is a data gap — see below) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mesalazine is not available (data gap). Based on known pharmacology, mesalazine is the 5-ASA cleavage product of sulfasalazine (sulfasalazine → sulfapyridine + 5-ASA/mesalazine via colonic bacterial azoreductases). Sulfasalazine has been used as a second-line DMARD for RA since the 1940s, with proposed mechanisms including NF-κB inhibition, PPARγ activation, and suppression of prostaglandin/leukotriene and inflammatory cytokine (IL-1β, TNF-α) release in synovial tissue.

The key uncertainty is **which component drives the RA effect**. Multiple head-to-head studies from the 1980s–1990s (PMID 2860942, 2877851, 8535642) directly compared sulfapyridine vs. 5-ASA/mesalazine in RA patients and found sulfapyridine to be the more active antirheumatic moiety, with mesalazine alone showing only weak effects. This means the bulk of RA clinical experience is with sulfasalazine (the combined molecule), not mesalazine in isolation — the mechanistic link is plausible but not confirmed for mesalazine specifically.

By contrast, the osteoarthritis candidate (rank 2, not the focus of this report) has more direct support: a 2024 *Nature Communications* study identifies an OSCAR-PPARγ mechanism by which 5-ASA itself (not sulfasalazine) suppresses cartilage-degrading inflammation, making it mechanistically the cleaner of the two hypotheses, despite having no clinical trials yet.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | Sulfasalazine vs. leflunomide-based combination DMARD therapy in RA patients failing methotrexate monotherapy — the most directly relevant trial, but terminated early |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Steady-state pharmacokinetics of sulfasalazine delayed-release tablets in pediatric juvenile idiopathic arthritis; terminated with n=2, not a treatment-efficacy trial |

4 additional trials returned by the keyword search (NCT05580861, NCT03591770, NCT00514982, NCT06201793) were excluded — they involve AML induction therapy, UC-related vaccine immunogenicity, Hermansky-Pudlak colitis, and minocycline for UC respectively, none of which relate to mesalazine in RA.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Review/Mechanistic | BMJ (Clin Res Ed) | Sulphapyridine, not 5-ASA, showed the pronounced second-line antirheumatic effect in RA; 5-ASA only weak first-line effect |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | — | Drugs | Open study: sulphasalazine improved RA disease activity; 5-ASA alone did not |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | — | Br J Rheumatol | Evidence favors sulphapyridine over 5-ASA as the active RA moiety of sulphasalazine |
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Comprehensive review of sulfasalazine pharmacology and efficacy as a DMARD in RA |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | — | J Rheumatol | Sulfasalazine and its metabolites (incl. 5-ASA) reduce inflammatory cytokine and MMP mRNA in RA synovial fibroblasts |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Cohort | J Rheumatol | Sulfasalazine normalizes abnormal lymphocyte function in RA patients after 12 weeks |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance | Gut | Re-evaluation of serious adverse reactions to sulphasalazine and mesalazine |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2025 | — | Intern Med (Tokyo) | Case report: 5-ASA-induced colitis in an RA patient on sulfasalazine/mesalazine — safety signal relevant to repurposing |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | Pharmacokinetics of slow-acting antirheumatic drugs including sulphasalazine |
| [17708602](https://pubmed.ncbi.nlm.nih.gov/17708602/) | 2007 | Review | World J Gastroenterol | Notes 5-ASA therapy was originally designed to treat RA before its UC use was discovered |

## Malaysia Market Information

16 products are registered with NPRA (marketed status: 已上市), but the evidence pack does not contain product-level detail — license numbers, product names, dosage forms, and approved indication text are all blank in the current data set (data gap). This information needs to be pulled directly from NPRA before further evaluation.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack (flagged as **Blocking** in the data-gap log — DG001), which prevents progression to the safety initial-assessment stage (S1) regardless of efficacy evidence.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA hypothesis is mechanistically plausible through the sulfasalazine-DMARD precedent, but multiple head-to-head pharmacology studies suggest mesalazine's contribution to that effect is weak relative to sulfapyridine, and the one directly relevant Phase 3 trial (NCT02930343) was terminated. Combined with a blocking safety data gap (no TFDA/NPRA warnings or contraindications on file), the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- NPRA package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data for mesalazine specifically (DG002)
- Clarification of active-moiety attribution (mesalazine vs. sulfapyridine) for the RA effect
- NPRA product-level registration details (license numbers, dosage forms, approved indication text)
- Consider parallel tracking of the osteoarthritis candidate (rank 2), which has a more direct 2024 mechanistic study for 5-ASA itself, despite lacking clinical trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

