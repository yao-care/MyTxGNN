---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 5
---

# Norfloxacin
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

# Norfloxacin: From Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic; its TFDA-specific approved indication text is not available in current records, though it is a long-established antibacterial agent. The TxGNN model highlights **Paratyphoid Fever** as the top-ranked candidate indication, and this is already supported by **9 publications** — including three Cochrane systematic reviews and a randomized controlled trial — reflecting an established antibacterial application rather than a purely speculative prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current registry records (Norfloxacin is a fluoroquinolone antibiotic; TFDA label text is a data gap) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 0.00% (score not meaningful here — see note below) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

> Note: The TxGNN score of 0.0 is not informative for this candidate. The repurposing rationale itself notes this is an **already-established** antibacterial indication for fluoroquinolones, not a novel model-generated hypothesis.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a confirmed data gap). Based on known pharmacology, Norfloxacin is a fluoroquinolone-class antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV, giving it direct bactericidal activity against Gram-negative enteric pathogens, including *Salmonella enterica* serovar Paratyphi.

This mechanism aligns directly with the treatment of typhoid and paratyphoid fever (enteric fever). The World Health Organization has historically recommended fluoroquinolones as first-line therapy in regions with resistance to older agents (chloramphenicol, cotrimoxazole), and norfloxacin specifically has been evaluated head-to-head against chloramphenicol with favorable outcomes.

Because this mechanistic and clinical link is already well-documented in the literature, this candidate should be understood as validating an established antimicrobial use case rather than uncovering a genuinely new therapeutic area — which also explains why the supporting evidence is stronger (systematic reviews, RCT) than typical purely-predicted candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1781005](https://pubmed.ncbi.nlm.nih.gov/1781005/) | 1991 | RCT | Trans R Soc Trop Med Hyg | 40 patients with *S. typhi*/*S. paratyphi* infection randomized to norfloxacin or chloramphenicol; 7-day norfloxacin course cured drug-sensitive and drug-resistant cases with no side effects |
| [3137036](https://pubmed.ncbi.nlm.nih.gov/3137036/) | 1988 | RCT | Eur J Clin Microbiol Infect Dis | Pefloxacin (fluoroquinolone) vs. cotrimoxazole in 42 adults with typhoid fever; all patients cured without relapse |
| [21975746](https://pubmed.ncbi.nlm.nih.gov/21975746/) | 2011 | Review (Cochrane) | Cochrane Database Syst Rev | WHO recommends fluoroquinolones for typhoid/paratyphoid fever in areas with resistance to older first-line antibiotics |
| [18843659](https://pubmed.ncbi.nlm.nih.gov/18843659/) | 2008 | Review (Cochrane) | Cochrane Database Syst Rev | Fluoroquinolones are first-line therapy for enteric fever; comparative efficacy vs. other agents reviewed |
| [15846718](https://pubmed.ncbi.nlm.nih.gov/15846718/) | 2005 | Review (Cochrane) | Cochrane Database Syst Rev | Fluoroquinolones recommended as first-line therapy for typhoid/paratyphoid fever vs. cheaper alternatives |
| [11197787](https://pubmed.ncbi.nlm.nih.gov/11197787/) | 2000 | Cohort | Intern Med (Tokyo) | Oral fluoroquinolones evaluated for adverse reactions and therapeutic effect in typhoid/paratyphoid fever patients in Japan |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohort | J Indian Med Assoc | Prospective study of 145 pediatric enteric fever cases; documents antibiotic sensitivity patterns of *S. typhi*/*S. paratyphi* |
| [27188369](https://pubmed.ncbi.nlm.nih.gov/27188369/) | 2016 | Other | Zhonghua Liu Xing Bing Xue Za Zhi | Drug tolerance and molecular typing of *S. paratyphi* A isolates, Henan province, 2009–2015 |
| [17164172](https://pubmed.ncbi.nlm.nih.gov/17164172/) | 2006 | Other | Int J Environ Health Res | Rising prevalence of *S. paratyphi* A in Kolkata; isolates largely sensitive to gentamicin and norfloxacin |

---

## Malaysia Market Information

License-level details (registration numbers, product names, dosage forms, indication text) are not available in the current data extract. Malaysia market status is confirmed as **Marketed**, with **5 total registrations** on file.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA/NPRA label warnings, contraindications, and drug-drug interaction data are currently a confirmed data gap (blocking severity) and have not yet been retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link and supporting literature (three Cochrane systematic reviews plus RCT evidence) strongly support fluoroquinolone use in paratyphoid fever, but package insert safety data (warnings, contraindications, DDI) and formal MOA documentation are both missing, which blocks a full safety assessment.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data — warnings and contraindications (currently blocking)
- Detailed mechanism of action data from DrugBank
- Malaysia license-level product details (product names, dosage forms, approved indication text)
- Current local antimicrobial resistance data, given several cited studies note rising fluoroquinolone resistance in *Salmonella* and *Shigella* species
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

