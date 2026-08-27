---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic originally used to treat serious Gram-positive infections such as skin/soft-tissue infections, bacteraemia, and right-sided endocarditis. The TxGNN model predicts it may be effective for **Osteoarthritis**, but the supporting literature (10 publications, 0 clinical trials) is almost entirely about daptomycin treating *osteoarticular infections* (e.g., prosthetic joint infection) — a mechanistically distinct condition from degenerative osteoarthritis — suggesting this prediction is likely a knowledge-graph node-confusion artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Malaysia licence records; literature context indicates serious Gram-positive infections (skin infection, bacteraemia, right-sided endocarditis) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for daptomycin is not available in this evidence pack (data gap). Based on information found in the supporting literature, daptomycin is a cyclic lipopeptide that calcium-dependently binds and depolarises the cell membrane of Gram-positive bacteria, producing rapid bactericidal activity — a purely antimicrobial mechanism with no known direct link to the cartilage degeneration and joint inflammation pathways underlying osteoarthritis.

Critically, all 10 supporting publications describe daptomycin's use in treating **osteoarticular infections** — prosthetic joint infection (PJI), septic arthritis, and implant-associated bone/joint infection caused by Gram-positive organisms — not osteoarthritis as a degenerative disease. One case report (PMID 32206362) even describes a patient referred for total knee arthroplasty with a pre-existing osteoarthritis diagnosis who was subsequently found to have a chronic *Corynebacterium* joint infection, illustrating how these two concepts get conflated in source text.

Taken together, this pattern is best explained by TxGNN's knowledge graph merging or closely embedding the "osteoarticular infection" and "osteoarthritis" disease nodes, rather than a real pharmacological signal. No mechanistic or clinical rationale currently supports repurposing daptomycin for osteoarthritis itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

**Note:** the publications below discuss daptomycin's established use for Gram-positive *osteoarticular infections* (PJI, septic arthritis), not degenerative osteoarthritis — included here for transparency per the evidence pack, but they should not be read as efficacy evidence for osteoarthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | International orthopaedics | High-dose daptomycin + rifampicin evaluated for safety/efficacy in Gram-positive osteoarticular infections |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Case Series | J Antimicrob Chemother | Daptomycin experience in knee/hip periprosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone/joint and implant-associated infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro susceptibility | J Antibiotics | Daptomycin susceptibility of S. aureus/S. epidermidis from prosthetic joint infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs. standard therapy outcomes in osteoarticular infections with S. aureus bacteraemia |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | Case Rep Orthop | Chronic Corynebacterium striatum septic arthritis in a patient referred for TKA, initially read as osteoarthritis |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey/Review | Int J Antimicrob Agents | Emerging Infections Network survey on current PJI management practices |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry Cohort | Medicina clínica | EU-CORE registry: daptomycin use experience in Spain |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Retrospective microbiology | Surgical infections | 10-year evolution of Staphylococcal susceptibility profile in osteoarticular infections |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | ASM Case Reports | First reported synovial fluid isolation of Corynebacterium propinquum causing septic arthritis |

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications and DDI data are currently unavailable — flagged as a Blocking data gap; see Next Steps.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction is supported only by literature on a mechanistically unrelated condition (osteoarticular infection), with zero clinical trials and no plausible MOA linkage — consistent with the assigned L5 evidence level and a likely knowledge-graph artifact rather than a real repurposing signal.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking data gap (DG001)
- DrugBank-confirmed mechanism of action — High-priority data gap (DG002)
- If pursuing this drug further, redirect attention to **rheumatoid arthritis** (rank 2, L4/S1), which has an actual mechanistic lead: a 2025 animal study (PMID 39571268) shows daptomycin suppresses inflammatory cytokines/NF-κB in a collagen-induced arthritis model — a materially stronger starting hypothesis than the osteoarthritis signal reviewed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

