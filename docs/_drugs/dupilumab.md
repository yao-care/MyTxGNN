---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is a monoclonal antibody (anti-IL-4Rα) originally developed and approved for moderate-to-severe atopic dermatitis, later expanded to other Th2/type‑2 inflammatory conditions such as asthma.
The TxGNN model predicts it may be effective for **Bronchitis**, with **1 clinical trial** and **6 publications** currently retrieved — but nearly all of this evidence is drawn from a *related* condition (chronic rhinosinusitis, asthma, COPD) rather than bronchitis itself, so the signal should be treated as preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe Atopic Dermatitis *(based on Dupilumab's established drug class/first approval; Malaysia NPRA license indication text was not populated in this data extract — see Malaysia Market Information)* |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Dupilumab is a fully human monoclonal antibody that blocks the shared IL-4 receptor alpha (IL-4Rα) subunit, thereby inhibiting both IL-4 and IL-13 signaling — the key cytokines driving type‑2 (Th2)/eosinophilic inflammation. Its efficacy in atopic dermatitis (and later asthma, chronic rhinosinusitis with nasal polyps, and eosinophilic esophagitis) has been well established, and mechanistically this pathway may extend to eosinophilic or Th2-driven subtypes of bronchitis.

Bronchitis — particularly eosinophilic or "plastic" bronchitis — shares airway eosinophilic/Th2 inflammatory biology with asthma, which is one of dupilumab's core approved indications. This biological adjacency is likely why TxGNN scored bronchitis so highly (rank 1744 overall).

However, the evidence retrieved for this specific candidate needs cautious interpretation. The one clinical trial identified (NCT04362501) actually studies chronic rhinosinusitis without nasal polyps (CRSsNP), not bronchitis, and is only indirectly relevant (relevance grade B — "same mechanism, different disease entity"). The majority of the literature concerns dupilumab in asthma or COPD, with only a single pediatric case-level report directly addressing an eosinophilic bronchitis-adjacent condition (plastic bronchitis). Because TxGNN's knowledge graph likely places "bronchitis" near "asthma," there is a real possibility that the prediction score is inflated by this graph proximity rather than by disease-specific evidence. This should be treated as a hypothesis-generating signal rather than a validated repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in chronic rhinosinusitis without nasal polyps (CRSsNP) — a related Th2-driven upper-airway condition, **not bronchitis**. Findings on endotype-based patient selection may inform, but do not directly establish, efficacy in bronchitis. |

*Note: No trial in the current evidence pack directly enrolled bronchitis patients; the single retrieved trial is included only for its mechanistic overlap.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review/Meta-analysis | The Journal of Asthma | Meta-analysis of RCTs showing dupilumab improves efficacy and safety outcomes in uncontrolled asthma — a Th2-driven airway disease mechanistically related to eosinophilic bronchitis. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Small RCT/Imaging Substudy | Chest | MRI-based study showing anti-T2 biologic treatment (including dupilumab) improves lung ventilation defects in prednisone-dependent asthma with eosinophilic airway pathology. |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Open-label Extension (long-term safety) | The Lancet Respiratory Medicine | TRAVERSE study: long-term (beyond 1 year) safety and efficacy of dupilumab in moderate-to-severe asthma. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review (COPD) | Tuberculosis and Respiratory Diseases | Comprehensive review of pharmacologic therapies, including biologics, for preventing COPD exacerbations — bronchitis is a COPD-related phenotype. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Narrative Review | Expert Opinion on Pharmacotherapy | Discusses smoking-induced airway diseases (chronic bronchitis, emphysema) contributing to symptoms in asthma/ACO patients; does not directly test dupilumab in bronchitis. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review/Case-level | Pediatric Pulmonology | Discusses novel therapies for eosinophilic pediatric plastic bronchitis — the only literature item directly addressing a bronchitis subtype, at case-report/case-series level. |

---

## Malaysia Market Information

Malaysia (NPRA) records confirm **3 marketing authorizations** for Dupilumab, and market status is **Marketed**. However, product-level license details (authorization numbers, product names, dosage forms, and approved indication text) were not populated in the current data extract, so a detailed authorization table cannot be produced at this time. This is flagged as a data gap requiring retrieval from the NPRA product registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were not available in the current evidence pack — this is logged as a Blocking data gap (DG001) that must be resolved before any safety-related decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale linking dupilumab's IL-4/IL-13 blockade to eosinophilic/Th2-driven bronchitis is biologically plausible given its established efficacy in asthma, but no clinical trial has directly evaluated dupilumab in bronchitis patients — the single retrieved trial studies a different (related) disease entity, and most literature is extrapolated from asthma/COPD populations. Given the L3 evidence level, "Research Question" stage designation, and the possibility that the TxGNN score is inflated by knowledge-graph proximity to asthma, this candidate is not yet ready to advance beyond a research hypothesis.

**To proceed, the following is needed:**
- Dedicated clinical trials or case series evaluating dupilumab specifically in (eosinophilic/plastic) bronchitis populations
- Resolution of Blocking data gap DG001: TFDA/NPRA package insert warnings and contraindications
- Resolution of High-priority data gap DG002: detailed mechanism of action documentation from DrugBank
- Malaysia NPRA product-level license and approved-indication text (currently missing from all 3 registrations)
- A methodological review of the TxGNN scoring to rule out knowledge-graph proximity bias (bronchitis vs. asthma node adjacency)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

