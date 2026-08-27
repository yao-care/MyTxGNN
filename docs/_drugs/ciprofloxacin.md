---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 5
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic originally used against a wide range of bacterial infections. The TxGNN model highlights **Paratyphoid Fever** as its top-ranked candidate indication, and while the TxGNN numerical score for this candidate is reported as 0.00% (likely a data artifact rather than a true low-confidence signal), the surrounding evidence base is unusually strong: **1 relevant clinical trial** and **20 publications**, including a Cochrane systematic review specifically on fluoroquinolones for enteric fever.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack (TFDA/NPRA license indication text is blank); ciprofloxacin is broadly known as a fluoroquinolone antibiotic indicated for various bacterial infections (e.g., urinary, respiratory, gastrointestinal) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 0.00% (reported value; appears inconsistent with the supporting clinical/literature evidence — flagged for data QA) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 42 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, ciprofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, blocking DNA replication in susceptible gram-negative and some gram-positive organisms; its efficacy across a range of bacterial infections is well established, and mechanistically it is active against *Salmonella enterica* serovar Paratyphi, the causative organism of paratyphoid fever.

Paratyphoid fever (together with typhoid fever, collectively "enteric fever") is caused by *Salmonella* species that are classically susceptible to fluoroquinolones. This is not a novel mechanistic leap from an unrelated indication — ciprofloxacin has long been used clinically as an oral single-agent treatment for enteric fever, and WHO guidance lists fluoroquinolones among recommended options where resistance patterns allow. This is corroborated by a Cochrane systematic review in the evidence pack (PMID 21975746) specifically evaluating fluoroquinolones for typhoid and paratyphoid fever, and by an older randomized trial of ciprofloxacin regimens in enteric fever (PMID 7573719).

The main caveat raised repeatedly across the literature is emerging fluoroquinolone resistance in *Salmonella* Typhi/Paratyphi, particularly in South Asia, which limits ciprofloxacin's reliability as first-line therapy in some regions and should be factored into any local positioning of this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04349826](https://clinicaltrials.gov/study/NCT04349826) | Phase 4 | Completed | 2150 | Compared azithromycin+cefixime vs. azithromycin alone for outpatient treatment of suspected/confirmed uncomplicated typhoid fever in South Asia; background notes ciprofloxacin as one of the established single-agent oral options for enteric fever, though the trial itself did not test ciprofloxacin as an arm. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7573719](https://pubmed.ncbi.nlm.nih.gov/7573719/) | 1995 | RCT | Am J Trop Med Hyg | Randomized comparison of 10-day vs. 14-day ciprofloxacin regimens in 69 enteric fever patients (52% MDR strains); similar time to defervescence in both arms. |
| [21975746](https://pubmed.ncbi.nlm.nih.gov/21975746/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews fluoroquinolones (including ciprofloxacin) for typhoid/paratyphoid fever, per WHO recommendations in areas with resistance to older first-line agents. |
| [36420914](https://pubmed.ncbi.nlm.nih.gov/36420914/) | 2022 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Evaluates cephalosporins for enteric fever; notes WHO recommends azithromycin, ciprofloxacin, or ceftriaxone given widespread resistance to older agents, with regional fluoroquinolone resistance limiting ciprofloxacin use in South Asia. |
| [40914181](https://pubmed.ncbi.nlm.nih.gov/40914181/) | 2025 | Review | Lancet | Comprehensive overview of enteric fever epidemiology, transmission, clinical course, and complications. |
| [16271634](https://pubmed.ncbi.nlm.nih.gov/16271634/) | 2005 | Review | Lancet | General review of typhoid and paratyphoid fever. |
| [16271635](https://pubmed.ncbi.nlm.nih.gov/16271635/) | 2005 | Review | Lancet | General review of typhoid and paratyphoid fever (companion article). |
| [40934281](https://pubmed.ncbi.nlm.nih.gov/40934281/) | 2025 | Genomic/Surveillance | PLoS Negl Trop Dis | Documents a marked rise in domestically acquired paratyphoid fever (*S.* Paratyphi A) in Taiwan since 2022, with genomic investigation of transmission routes. |
| [35871037](https://pubmed.ncbi.nlm.nih.gov/35871037/) | 2022 | Retrospective Cohort | J Formos Med Assoc | Reviews 37 indigenous/imported enteric fever cases (including 13 paratyphoid) at two Taiwan medical centers, 2010–2020. |
| [32050286](https://pubmed.ncbi.nlm.nih.gov/32050286/) | 2020 | Review | Z Gastroenterol | Overview of typhoid/paratyphoid fever diagnosis and management, noting near-exclusive acquisition outside Europe. |
| [38387472](https://pubmed.ncbi.nlm.nih.gov/38387472/) | 2024 | Observational | Lancet Microbe | Investigates the relationship between ciprofloxacin prescribing and emerging non-susceptibility in *Salmonella* Typhi in Malawi — a key resistance-risk signal for this indication. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ciprofloxacin's use in paratyphoid/enteric fever is supported by a Cochrane systematic review and direct randomized trial data, and reflects an already well-established clinical role rather than a mechanistically speculative repurposing — but the reported TxGNN score (0.00%) is inconsistent with this evidence and should be reconciled, and multiple sources flag rising fluoroquinolone resistance as a material constraint on efficacy.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/NPRA package insert warnings and contraindications before any S1 safety assessment
- Resolve DG002 (High): obtain confirmed mechanism-of-action data from DrugBank
- Confirm whether existing Malaysia product licenses already cover enteric/paratyphoid fever in their approved indication text (license data was not populated in this evidence pack)
- Investigate the apparent TxGNN score anomaly (0.00% despite supporting SR/RCT evidence) before using it in decision scoring
- Assess local/regional fluoroquinolone resistance data for *Salmonella* Paratyphi before recommending first-line use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

