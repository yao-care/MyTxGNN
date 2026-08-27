---
layout: default
title: Clavulanic Acid
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 5
---

# Clavulanic Acid
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

# Clavulanic Acid: From Beta-Lactamase Inhibitor Combination Therapy to Streptococcal Pneumonia

## One-Sentence Summary

Clavulanic acid has negligible antibacterial activity on its own; it is used exclusively as a fixed-dose combination partner (most commonly with amoxicillin, as in Augmentin) to protect penicillins from bacterial beta-lactamase enzymes.
The TxGNN model's top-ranked prediction is **Streptococcal Pneumonia**, but the mechanistic case is weak since *S. pneumoniae* itself rarely produces beta-lactamase.
No clinical trials specific to this pairing were retrieved; support comes from **20 publications**, mostly indirect literature on amoxicillin/clavulanate use in respiratory infections.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA registration records retrieved; clavulanic acid is marketed only as a combination product (e.g., with amoxicillin) for bacterial infections |
| Predicted New Indication | Streptococcal Pneumonia |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clavulanic acid is a beta-lactam-derived, irreversible inhibitor of bacterial beta-lactamases (particularly TEM-1). It has little intrinsic antibacterial activity itself; its clinical role is to restore the activity of co-administered penicillins (typically amoxicillin, sometimes ticarcillin) against beta-lactamase-producing strains. It is never marketed as a standalone antibiotic.

For the top-ranked prediction, streptococcal pneumonia, the evidence pack itself flags a caveat: *S. pneumoniae* is not typically a beta-lactamase producer, so clavulanic acid's contribution here is largely indirect — it broadens amoxicillin/clavulanate's coverage against beta-lactamase-producing co-pathogens (e.g., *H. influenzae*) commonly found alongside *S. pneumoniae* in community-acquired pneumonia (CAP), rather than acting on the pneumococcus directly. Amoxicillin/clavulanate is nonetheless an established first-line empirical option for CAP, which is why the combination shows up repeatedly in the literature even though the mechanistic link for clavulanic acid specifically is indirect.

Worth noting: among the other candidate indications in this evidence pack, urinary tract infection (rank 3) has a substantially stronger and more direct mechanistic rationale — clavulanic acid's beta-lactamase inhibition directly restores amoxicillin activity against beta-lactamase-producing uropathogens — and carries the highest evidence level (L1) of the five candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1854164](https://pubmed.ncbi.nlm.nih.gov/1854164/) | 1991 | RCT | Antimicrobial Agents and Chemotherapy | Amoxicillin-clavulanic acid effective against experimental *S. pneumoniae* respiratory infection in mice; ciprofloxacin failed to clear infection |
| [15303634](https://pubmed.ncbi.nlm.nih.gov/15303634/) | 2004 | RCT | Respiratory Medicine | Gemifloxacin (7-day) vs. amoxicillin/clavulanic acid (10-day) for CAP of suspected pneumococcal origin |
| [10501315](https://pubmed.ncbi.nlm.nih.gov/10501315/) | 1999 | Review | Seminars in Respiratory Infections | Treatment of pneumococcal pneumonia amid rising penicillin and macrolide resistance |
| [9711451](https://pubmed.ncbi.nlm.nih.gov/9711451/) | 1998 | Review | Drugs | Review of azithromycin in pediatric respiratory infections, contextualizing beta-lactam alternatives |
| [15212560](https://pubmed.ncbi.nlm.nih.gov/15212560/) | 2004 | Review | Drugs | Cefdinir review; covers activity against penicillin-susceptible *S. pneumoniae* |
| [16137193](https://pubmed.ncbi.nlm.nih.gov/16137193/) | 2005 | Review | Treatments in Respiratory Medicine | Amoxicillin/clavulanic acid extended-release formulation for respiratory infections, including reduced-susceptibility pneumococcal strains |
| [14979735](https://pubmed.ncbi.nlm.nih.gov/14979735/) | 2004 | Review | Drugs & Aging | Antibacterial choice for lower respiratory tract infections in elderly patients; *S. pneumoniae* most common isolate |
| [9793046](https://pubmed.ncbi.nlm.nih.gov/9793046/) | 1998 | Review | Presse Médicale | Commentary on whether ampicillin monotherapy suffices for community-acquired pneumonia |
| [2227080](https://pubmed.ncbi.nlm.nih.gov/2227080/) | 1990 | Cohort | J International Medical Research | Open study of amoxicillin+clavulanic acid in children with respiratory tract infections, including bronchopneumonia |
| [36086715](https://pubmed.ncbi.nlm.nih.gov/36086715/) | 2022 | Cohort | Medicine | Cross-sectional study of CAP-causing bacteria and antibiotic resistance in Vietnamese patients |

## Malaysia Market Information

20 products containing clavulanic acid (as combination therapy) are registered as Marketed with NPRA. License numbers, product names, dosage forms, and approved indication text were not returned in this dataset and cannot be listed here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amoxicillin/clavulanate is a well-established CAP treatment, but for streptococcal pneumonia specifically, clavulanic acid's mechanistic contribution is indirect (covering co-pathogens rather than the pneumococcus itself), and no clinical trials directly targeting this pairing were found — evidence rests on L2-level literature only.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (flagged as a **blocking** data gap — safety pre-evaluation cannot proceed without this)
- Mechanism of action documentation from DrugBank
- NPRA license-level detail (product names, dosage forms, approved indication text) to confirm which registered products and formulations are relevant
- Consider prioritizing the urinary tract infection candidate (L1 evidence, direct mechanistic link) alongside this indication for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

