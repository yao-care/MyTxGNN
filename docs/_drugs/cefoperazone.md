---
layout: default
title: Cefoperazone
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Cefoperazone
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

# Cefoperazone: From Bacterial Infections to Pneumonia

## One-Sentence Summary

> Cefoperazone is an established third-generation cephalosporin antibiotic used for treating bacterial infections. Among the 10 candidate indications TxGNN surfaced for this drug, **Pneumonia** is the only one backed by substantive clinical and literature evidence — **2 clinical trials** (including a Phase 3 RCT) and a body of **20 supporting publications** — while the model's single highest-scoring candidate (sclerosing cholangitis) and several others are flagged in the evidence pack itself as likely knowledge-graph artifacts with zero supporting evidence. This report therefore centers on the pneumonia signal as the actionable candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (Cefoperazone is an established broad-spectrum antibacterial agent; specific TFDA-approved indication text was not returned in the current registration extract) |
| Predicted New Indication | Pneumonia (hospital-acquired / ventilator-associated / community-acquired) |
| TxGNN Prediction Score | 99.93% (internal rank #1438) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record is currently a data gap (DG002). Based on the mechanistic annotations already present in the evidence pack, Cefoperazone is a third-generation cephalosporin that inhibits penicillin-binding protein (PBP)-mediated bacterial cell wall synthesis, producing a bactericidal effect against a broad range of gram-negative pathogens (including *Acinetobacter baumannii*, *Pseudomonas aeruginosa*, *Klebsiella pneumoniae*) and some gram-positive organisms.

Because Cefoperazone's original use is as a broad-spectrum antibacterial, the "new indication" of pneumonia is not a cross-disease repurposing signal in the usual sense — it is a confirmation that an existing antibacterial's known spectrum covers the pathogens that commonly cause hospital-acquired and ventilator-associated pneumonia (HAP/VAP). Mechanistic plausibility here is very high precisely because no new mechanism is being proposed.

It's also worth noting explicitly: TxGNN's raw top-ranked candidates for this drug (sclerosing cholangitis, rare congenital syndromes, gout) all carry an "L5 / Hold" designation with the evidence pack's own rationale calling them likely embedding-noise (e.g., cefoperazone's biliary excretion co-occurring with cholangitis in the knowledge graph, with no actual therapeutic link). Pneumonia and its close relative bronchitis are the only candidates among the top 10 with real clinical/literature support, which is why this report treats pneumonia as the substantive finding rather than mechanically reporting the top TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02060149](https://clinicaltrials.gov/study/NCT02060149) | Phase 1/2 | Unknown | 90 | Multi-center RCT testing nebulized alkaline solution as an adjunct to cefoperazone-sulbactam + minocycline for extensively drug-resistant *A. baumannii* pneumonia; evaluates an adjunct intervention rather than cefoperazone monotherapy (indirect relevance) |
| [NCT01280461](https://clinicaltrials.gov/study/NCT01280461) | Phase 3 | Unknown | 142 | Open-label, randomized, comparative trial of cefoperazone/sulbactam vs. cefepime for hospital-acquired pneumonia (HAP) and healthcare-associated pneumonia (HCAP); directly evaluates the drug in the target indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31138577](https://pubmed.ncbi.nlm.nih.gov/31138577/) | 2019 | RCT | Antimicrobial Agents and Chemotherapy | Randomized noninferiority trial: cefoperazone-sulbactam vs. cefepime for HAP/HCAP in adults ≥18 years |
| [34168466](https://pubmed.ncbi.nlm.nih.gov/34168466/) | 2021 | RCT/Cohort | Infection and Drug Resistance | Cefoperazone-sulbactam vs. piperacillin-tazobactam for HAP and ventilator-associated pneumonia (VAP) |
| [6456894](https://pubmed.ncbi.nlm.nih.gov/6456894/) | 1981 | RCT | Drugs | Early parenteral cefoperazone trial in 15 pneumonia and 15 pyelonephritis cases; all isolated organisms were cefoperazone-sensitive |
| [1643821](https://pubmed.ncbi.nlm.nih.gov/1643821/) | 1992 | Comparative Trial | Diagnostic Microbiology and Infectious Disease | Multicenter randomized comparison of cefoperazone vs. ceftriaxone monotherapy for nosocomial pneumonia; equally effective (80% vs. 70% success) |
| [34871744](https://pubmed.ncbi.nlm.nih.gov/34871744/) | 2022 | Comparative Study | International Journal of Antimicrobial Agents | Cefoperazone-sulbactam vs. piperacillin-tazobactam for pneumonia specifically in elderly patients |
| [24726664](https://pubmed.ncbi.nlm.nih.gov/24726664/) | 2014 | Retrospective Cohort | International Journal of Infectious Diseases | Carbapenem-resistant *A. baumannii* HAP in elderly patients; in vitro benefit of cefoperazone/sulbactam combination therapy |
| [17120738](https://pubmed.ncbi.nlm.nih.gov/17120738/) | 2006 | Comparative Trial | J Huazhong Univ Sci Technol Med Sci | IV moxifloxacin vs. cefoperazone + azithromycin for community-acquired pneumonia (CAP) |
| [29319497](https://pubmed.ncbi.nlm.nih.gov/29319497/) | 2018 | Comparative Study | Int J Clin Pharmacol Ther | Tigecycline + high-dose cefoperazone-sulbactam vs. tigecycline monotherapy for VAP from extensively drug-resistant *A. baumannii* |
| [35685727](https://pubmed.ncbi.nlm.nih.gov/35685727/) | 2022 | Cohort | Evidence-Based Complementary and Alternative Medicine | Polymyxin B + cefoperazone-sulbactam + tigecycline for MDR *A. baumannii* pneumonia (**note: this article was later retracted**, PMID [38125170](https://pubmed.ncbi.nlm.nih.gov/38125170/), 2023) |
| [2671141](https://pubmed.ncbi.nlm.nih.gov/2671141/) | 1989 | Review | Infectious Disease Clinics of North America | Review of third-generation cephalosporins, including cefoperazone's activity against *Pseudomonas aeruginosa* and other resistant respiratory pathogens |

---

## Malaysia Market Information

8 marketing authorizations are on record for Cefoperazone (market status: **Marketed**), but the evidence extract returned empty values for all per-product fields (license number, product name, dosage form, approved indication text). Full registration particulars would need to be pulled separately from the source registry to populate this section.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings/contraindications and a formal DDI query are outstanding — see DG001, a blocking data gap for safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cefoperazone(-sulbactam)'s use in hospital-acquired and ventilator-associated pneumonia is supported by L1-level evidence — two head-to-head randomized trials (vs. cefepime, vs. piperacillin-tazobactam) plus a substantial cohort and comparative-trial literature base. However, this reflects confirmation of an already-known antibacterial spectrum rather than a novel mechanistic repurposing signal, and core safety/regulatory records are still missing.

**To proceed, the following is needed:**
- TFDA package insert warnings, contraindications, and drug-interaction data (blocking gap, DG001)
- Formal DrugBank mechanism-of-action record (DG002)
- Full Taiwan license particulars (product names, dosage forms, indication text) for the 8 registered products
- Confirmation of whether pneumonia already falls within Cefoperazone's existing approved label in Taiwan (if so, this is label-confirmation rather than a new indication)
- Secondary review of bronchitis (L2, also "Proceed with Guardrails") as a related, evidence-supported candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

