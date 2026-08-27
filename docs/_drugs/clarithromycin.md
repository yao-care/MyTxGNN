---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 5
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Respiratory Tract Infections to Maxillary Sinusitis

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic long used against susceptible bacterial infections of the respiratory tract, skin, and gastrointestinal tract (including H. pylori eradication). The TxGNN model flags **Maxillary Sinusitis** as a leading repurposing candidate, and unlike many novel predictions, this one is already backed by **1 clinical trial** and **20 publications**, several of which are historical Phase III randomized controlled trials directly testing clarithromycin in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial respiratory tract and other susceptible bacterial infections (general macrolide-class indication; specific Malaysia label text not available in this evidence pack) |
| Predicted New Indication | Maxillary Sinusitis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 28 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, clarithromycin is a semisynthetic 14-membered macrolide (a methylated derivative of erythromycin) that binds the bacterial 50S ribosomal subunit to inhibit protein synthesis, giving it bactericidal/bacteriostatic activity against common respiratory pathogens such as *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — the organisms most frequently implicated in acute maxillary sinusitis.

Maxillary sinusitis sits squarely within the spectrum of infections clarithromycin's class has always targeted, so the mechanistic link to its established use in respiratory tract infections is direct rather than speculative. This is reflected in the evidence base: several multicenter, randomized, double-blind Phase III trials from the 1990s–2000s directly compared clarithromycin against amoxicillin, amoxicillin-clavulanate, cefuroxime, sparfloxacin, and ciprofloxacin specifically for acute maxillary sinusitis, consistently reporting comparable or favorable clinical and bacteriological cure rates. In several other jurisdictions, clarithromycin (including its extended-release formulation) already carries an approved indication for acute maxillary sinusitis — reinforcing that the TxGNN signal here reflects strong pre-existing clinical validation rather than an untested hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01667692](https://clinicaltrials.gov/study/NCT01667692) | Phase 4 | Completed | 78 | Compared azithromycin- vs. clarithromycin-based triple therapy for H. pylori eradication; not specific to maxillary sinusitis, relevance to this indication should be confirmed |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11192134](https://pubmed.ncbi.nlm.nih.gov/11192134/) | 2000 | RCT (Phase III) | Clinical Therapeutics | Double-blind Phase III trial: clarithromycin extended-release vs. immediate-release, comparable efficacy in adults with acute maxillary sinusitis |
| [2140546](https://pubmed.ncbi.nlm.nih.gov/2140546/) | 1990 | RCT (Phase III) | Current Medical Research and Opinion | Open, Phase III multicentre study; clarithromycin vs. amoxycillin showed comparable efficacy and tolerability |
| [9923060](https://pubmed.ncbi.nlm.nih.gov/9923060/) | 1998 | RCT | Rhinology | Randomised, double-blind, multicentre trial (n=370): cefuroxime axetil vs. clarithromycin, comparable clinical response and safety |
| [10214783](https://pubmed.ncbi.nlm.nih.gov/10214783/) | 1999 | RCT | Annals of Otology, Rhinology & Laryngology | Multicenter, randomized, double-blind trial (n=560): ciprofloxacin vs. clarithromycin, clarithromycin showed numerically higher clinical resolution (91% vs. 84%) |
| [10211537](https://pubmed.ncbi.nlm.nih.gov/10211537/) | 1999 | RCT | Clinical Therapeutics | Randomized, double-masked, multicenter trial (n=504): sparfloxacin vs. clarithromycin in acute bacterial maxillary sinusitis |
| [8111512](https://pubmed.ncbi.nlm.nih.gov/8111512/) | 1993 | RCT | Archives of Family Medicine | Multicenter comparison of clarithromycin and amoxicillin for acute maxillary sinusitis, evaluating safety and efficacy |
| [8313865](https://pubmed.ncbi.nlm.nih.gov/8313865/) | 1993 | RCT | Ear, Nose & Throat Journal | Single-blind, randomized, multicenter study (n=497): clarithromycin vs. amoxicillin/clavulanate, similar clinical success rates |
| [1827106](https://pubmed.ncbi.nlm.nih.gov/1827106/) | 1991 | RCT | Journal of Antimicrobial Chemotherapy | Single-blind, multicentre outpatient trial (n=50): clarithromycin vs. amoxycillin, comparable clinical and bacteriological outcomes |
| [8763594](https://pubmed.ncbi.nlm.nih.gov/8763594/) | 1996 | RCT | Pathologie-Biologie | Open multicenter trial (n=280): clarithromycin vs. amoxicillin-clavulanate, no significant difference in clinical/radiologic outcomes |
| [16771618](https://pubmed.ncbi.nlm.nih.gov/16771618/) | 2006 | Review | Expert Review of Anti-infective Therapy | Reviews macrolide immunomodulatory effects alongside established bacteriological/clinical efficacy in acute maxillary sinusitis |

---

## Malaysia Market Information

Clarithromycin holds **28 active registrations** in the Malaysia market status feed (marketed status: ✓). Detailed per-license data (authorization numbers, product names, dosage forms, approved indication text) were not populated in this evidence pack and need to be pulled from source before use in regulatory submissions.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack currently has no populated warnings, contraindications, or drug-interaction data for clarithromycin — the DDI query also returned no results.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence for clarithromycin in maxillary sinusitis is strong and L1-grade — multiple completed Phase III RCTs directly support this indication, and the drug is already widely marketed. However, a blocking data gap on label warnings/contraindications means safety review (S1) cannot yet be completed, so full clearance should wait on that data.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, precautions, and contraindications (DG001, blocking)
- DrugBank-sourced mechanism of action detail to confirm the mechanistic rationale (DG002)
- Malaysia license-level detail (product names, dosage forms, approved indication text) currently blank in this pack
- Confirmation of whether NCT01667692 is genuinely relevant to maxillary sinusitis, given its focus on H. pylori eradication
- A re-run of the DDI query, which currently returned no interaction data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

