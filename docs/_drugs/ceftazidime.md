---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 5
---

# Ceftazidime
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

# Ceftazidime: From Bacterial Infections to Peritonitis

## One-Sentence Summary

> Ceftazidime is a third-generation cephalosporin antibiotic already used for gram-negative bacterial infections (including *Pseudomonas aeruginosa*).
> The TxGNN model's top-ranked prediction is **Peritonitis** — a use case that overlaps substantially with its existing antibacterial spectrum rather than representing a novel mechanism —
> with **13 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (gram-negative, incl. *Pseudomonas aeruginosa*) — inferred from drug class; NPRA-registered indication text was not returned in this data pull (data gap) |
| Predicted New Indication | Peritonitis |
| TxGNN Prediction Score | 0.00% *(as returned by source data — see note below)* |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 11 |
| Recommended Decision | Proceed with Guardrails |

**Note on TxGNN score**: the evidence pack returns `0.0` for this candidate's prediction score across all five ranked indications. This looks like a data quality issue rather than a genuine near-zero score (peritonitis is ranked #1 and carries L1 evidence). Recommend re-querying the TxGNN scoring pipeline before relying on this number.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this candidate (data gap). Based on known pharmacology, Ceftazidime is a third-generation cephalosporin that inhibits bacterial cell-wall synthesis by binding penicillin-binding proteins (PBPs), giving it strong bactericidal activity against gram-negative organisms, including *Pseudomonas aeruginosa*.

Peritonitis — particularly CAPD (continuous ambulatory peritoneal dialysis)-associated peritonitis and spontaneous bacterial peritonitis (SBP) — is commonly caused by the same gram-negative organisms Ceftazidime already covers. The evidence pack's own mechanistic rationale notes that this overlap is strong enough that the prediction is less a novel "drug repurposing" signal and more an **extension of an already-established use pattern**: ceftazidime (often combined with cefazolin or vancomycin) is a standard empiric agent in international peritoneal dialysis-related peritonitis guidelines.

Because the mechanistic fit is driven by antibacterial spectrum rather than a new biological pathway, the "prediction" should be read as evidence consolidation for an existing off-label/guideline-supported use, not a discovery of new pharmacology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01455246](https://clinicaltrials.gov/study/NCT01455246) | Phase 2/3 | Terminated | 32 | Daptomycin+Meropenem vs. Ceftazidime for nosocomial spontaneous bacterial peritonitis (direct comparative evidence) |
| [NCT02443285](https://clinicaltrials.gov/study/NCT02443285) | Phase 3 | Unknown | 100 | Evaluates whether 3rd-generation cephalosporins (incl. ceftazidime) remain effective for spontaneous bacterial peritonitis amid rising resistance |
| [NCT04367974](https://clinicaltrials.gov/study/NCT04367974) | N/A | Unknown | 20 | PK study of ceftazidime vs. cefazolin in CAPD-related peritonitis |
| [NCT02593201](https://clinicaltrials.gov/study/NCT02593201) | Phase 4 | Completed | 358 | Prolonged antibiotic therapy to prevent relapsing peritonitis in PD patients with high bacterial DNA fragment levels |
| [NCT03790176](https://clinicaltrials.gov/study/NCT03790176) | Phase 1 | Unknown | 20 | PK of ceftazidime/avibactam in plasma, ELF, and intraperitoneal fluid in critically ill and PD patients |
| [NCT02872038](https://clinicaltrials.gov/study/NCT02872038) | Phase 4 | Completed | 154 | Cefepime monotherapy vs. cefazolin+ceftazidime combination for empirical CAPD-associated peritonitis |
| [NCT01785641](https://clinicaltrials.gov/study/NCT01785641) | N/A | Completed | 300 | Single vs. combined antibiotic therapy for bacterial peritonitis in CAPD patients |
| [NCT02787057](https://clinicaltrials.gov/study/NCT02787057) | N/A | Completed | 80 | IP vancomycin+oral moxifloxacin vs. IP vancomycin+IP ceftazidime for PD-related peritonitis |
| [NCT04077996](https://clinicaltrials.gov/study/NCT04077996) | N/A | Completed | 64 | Automated vs. ambulatory peritoneal dialysis treatment application for peritonitis |
| [NCT05971537](https://clinicaltrials.gov/study/NCT05971537) | Phase 4 | Recruiting | 46 | Antibiotic-lock in Tenckhoff catheter for relapsing/repeat peritonitis |

*3 additional lower-relevance trials (Zavicefta/avibactam surveillance study, pediatric appendicitis antibiotic-vs-surgery trial, ascitic fluid pathogen ID study) were excluded from this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2644565](https://pubmed.ncbi.nlm.nih.gov/2644565/) | 1989 | RCT | Nephron | Vancomycin + ceftazidime in CAPD peritonitis — 83% cure rate with this regimen |
| [9360685](https://pubmed.ncbi.nlm.nih.gov/9360685/) | 1997 | RCT | Advances in Peritoneal Dialysis | Cefazolin+netilmycin vs. vancomycin+ceftazidime for CAPD peritonitis |
| [40688946](https://pubmed.ncbi.nlm.nih.gov/40688946/) | 2025 | Systematic Review / Meta-Analysis | Cureus | Ceftazidime-avibactam+metronidazole vs. meropenem for intra-abdominal infections |
| [34052357](https://pubmed.ncbi.nlm.nih.gov/34052357/) | 2022 | Cohort | Am J Kidney Dis | Variation in PD-related peritonitis cure outcomes (PDOPPS) |
| [38044852](https://pubmed.ncbi.nlm.nih.gov/38044852/) | 2023 | PK Study | Renal Failure | PK of ceftazidime and cefazolin in CAPD-related peritonitis treatment |
| [32063189](https://pubmed.ncbi.nlm.nih.gov/32063189/) | 2020 | Cohort | Perit Dial Int | Plasma/dialysate ceftazidime+cefazolin concentrations during short-dwell exchange in PD peritonitis |
| [37301439](https://pubmed.ncbi.nlm.nih.gov/37301439/) | 2023 | PK Study | Clin Microbiol Infect | Plasma and intraperitoneal PK of ceftazidime/avibactam in PD patients |
| [14703199](https://pubmed.ncbi.nlm.nih.gov/14703199/) | 2003 | PK Study | Perit Dial Int | PK of ceftazidime in CAPD-related peritonitis (Thai cohort) |
| [11587402](https://pubmed.ncbi.nlm.nih.gov/11587402/) | 2001 | Clinical Study | Perit Dial Int | Effective treatment of PD-associated peritonitis with cefazolin+ceftazidime in children |
| [3886227](https://pubmed.ncbi.nlm.nih.gov/3886227/) | 1985 | Clinical Study | Clin Nephrol | Intraperitoneal vancomycin+ceftazidime in 64 episodes of CAPD peritonitis |

---

## Malaysia Market Information

NPRA records show **11 active registrations** for Ceftazidime in Malaysia (market status: 已上市 / Marketed). However, the authorization-level details returned in this data pull — license numbers, product names, dosage forms, and approved indication text — were all blank. This is a data gap requiring a direct NPRA product-registration lookup before authorization specifics can be reported.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were all flagged as data gaps in this evidence pack — see DG001 below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Peritonitis has the strongest evidence among the five predicted indications (L1, decision stage S3), reflecting an already well-established clinical use pattern (ceftazidime as part of standard PD-peritonitis/SBP antibiotic regimens) rather than a novel mechanistic hypothesis. However, this is contingent on resolving a **Blocking** drug-level safety data gap before any initial safety screening (S1) can be completed.

**To proceed, the following is needed:**
- **[DG001 – Blocking]** TFDA/NPRA product label (warnings, contraindications) — required before S1 safety screening can even begin; currently no package insert data available
- **[DG002 – High]** DrugBank mechanism-of-action data — needed to formally support the mechanistic-link rationale
- NPRA registration details (license numbers, product names, dosage forms, approved indication text) for the 11 Malaysia listings — currently blank
- Resolution of the TxGNN score anomaly (0.00% across all ranked indications) before using it in formal scoring
- Clarify whether peritonitis should be tracked as "repurposing" or as guideline-alignment/label-extension documentation, given the existing off-label/standard-of-care use pattern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

