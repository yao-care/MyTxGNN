---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 2
---

# Tazobactam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Tazobactam: From Combination Antibacterial Therapy to Pneumonia

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor with no standalone antibacterial activity; it is marketed only in fixed combinations with partner beta-lactams (e.g., piperacillin, ceftolozane) to restore activity against beta-lactamase–producing pathogens. The TxGNN model flags **Pneumonia** as a high-scoring association, supported by **50 clinical trials** and **20 publications** — though most of this evidence reflects pneumonia's status as an *already-established* indication for tazobactam-containing combinations rather than a genuinely novel repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No standalone indication — tazobactam is a beta-lactamase inhibitor sold only as fixed combinations (e.g., piperacillin/tazobactam, ceftolozane/tazobactam); Malaysia-specific licensed indication text is not available in this data pull |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed standalone mechanism-of-action data for tazobactam is not available from DrugBank in this evidence pack (data gap DG002). Based on the model's repurposing rationale, tazobactam is a beta-lactamase inhibitor that has no independent bactericidal activity; it irreversibly inhibits bacterial beta-lactamases (including many ESBL variants), thereby protecting a co-administered beta-lactam partner — piperacillin or ceftolozane — from enzymatic hydrolysis and restoring bactericidal activity against beta-lactamase-producing Gram-negative organisms, including *Pseudomonas aeruginosa*.

Because tazobactam only exists as part of fixed combinations, its relationship to pneumonia is not exploratory: piperacillin/tazobactam and ceftolozane/tazobactam are already labeled for hospital-acquired and ventilator-associated bacterial pneumonia caused by beta-lactamase-producing Enterobacterales and *P. aeruginosa*. The mechanistic link is therefore very strong, but the "prediction" largely reconfirms known pharmacology rather than uncovering a new therapeutic use — this distinction matters for how the evidence should be weighted in a repurposing decision.

The same caveat applies to the model's second-ranked signal, urinary tract infection (score 99.12%, also L1/Proceed with Guardrails), which is likewise an existing combination-product indication (e.g., ceftolozane/tazobactam in complicated UTI/pyelonephritis).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | IV ceftolozane/tazobactam vs. meropenem in ventilated nosocomial pneumonia (VABP/HABP); non-inferiority on Day 28 all-cause mortality |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP; non-inferiority on all-cause mortality |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational trial of imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin 750mg OD vs. piperacillin/tazobactam 4g/500mg q8h in mild-to-moderate hospital-acquired pneumonia |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recruiting | 20,000 | REMAP-CAP adaptive platform trial evaluating multiple interventions (including beta-lactam arms) in community-acquired pneumonia |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Safety, tolerability, and PK of ceftolozane/tazobactam in pediatric nosocomial pneumonia |
| [NCT06422533](https://clinicaltrials.gov/study/NCT06422533) | N/A | Recruiting | 226 | Ceftolozane/tazobactam vs. piperacillin/tazobactam for bacteremia in hemato-oncology patients with febrile neutropenia |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Short vs. prolonged infusion of ceftolozane/tazobactam in ventilator-associated pneumonia due to *P. aeruginosa* |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | Unknown | 50 | Dosing optimization (prolonged vs. intermittent infusion) of piperacillin/tazobactam for nosocomial pneumonia with higher-MIC pathogens |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Phase 1 | Completed | 37 | Plasma PK and lung penetration of IV ceftolozane/tazobactam in critically ill patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | Piperacillin-tazobactam vs. meropenem for ceftriaxone-resistant *E. coli*/*K. pneumoniae* bloodstream infection; 30-day mortality outcomes |
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs. meropenem for Gram-negative nosocomial pneumonia, phase 3 non-inferiority |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial of imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohort | Clin Infect Dis | Resistance emergence: ceftazidime-avibactam vs. ceftolozane-tazobactam in MDR *P. aeruginosa* bacteremia/pneumonia |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Cohort | Lancet Infect Dis | CACTUS study: real-world effectiveness of ceftazidime-avibactam vs. ceftolozane-tazobactam for MDR *P. aeruginosa* |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Review | Int J Antimicrob Agents | Systematic review of PK/PD for novel beta-lactam/beta-lactamase inhibitor combinations in carbapenem-resistant Gram-negative pneumonia |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Review of ceftolozane/tazobactam for hospital-acquired pneumonia |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Review | Clin Microbiol Infect | Network meta-analysis of empiric antibiotic regimens for non-ventilator HAP |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Review of ceftolozane-tazobactam pharmacology and use in nosocomial pneumonia |

## Safety Considerations

Please refer to the package insert for safety information. (No warnings, contraindications, or drug-interaction data were retrievable in this pull — flagged as blocking data gap DG001 for TFDA/NPRA label warnings/contraindications, and the DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1: multiple completed Phase 3 RCTs), but this largely confirms an existing indication for tazobactam-containing combinations rather than a novel repurposing hypothesis, and safety-critical data (label warnings, contraindications, DDI, standalone MOA) needed for an S1 safety evaluation are currently missing.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications) — currently blocking (DG001)
- DrugBank mechanism-of-action record for tazobactam — high priority (DG002)
- Malaysia-specific license/product data (registration numbers, dosage forms, approved indication text per product) — not populated in current pull
- Clarification of which specific combination product(s) (piperacillin/tazobactam vs. ceftolozane/tazobactam) the pneumonia indication would apply to, since safety and spectrum differ between them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

