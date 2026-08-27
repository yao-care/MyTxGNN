---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic broadly used to treat bacterial infections; the specific TFDA-approved indication wording is not available in this dataset.
The TxGNN model predicts it may be effective for **Bacterial Arthritis**,
with **0 registered clinical trials** and **20 retrieved publications** currently supporting this direction, including a case series and a synovial fluid pharmacokinetic study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the TFDA licensing records provided (all license `approved_indication_text` fields are blank in this evidence pack); clinically known as a broad-spectrum antibacterial |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Malaysia Market Status | 已上市 (Marketed) |
| Number of Registrations | 39 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for this evidence pack. Based on known pharmacology, Cefuroxime is a second-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs), producing bactericidal activity against a broad range of Gram-positive and Gram-negative organisms — this is consistent with the mechanistic rationale noted in the evidence pack.

Bacterial arthritis (septic arthritis) is caused by many of the same pathogens Cefuroxime already treats elsewhere in the body (notably *Staphylococcus aureus* and streptococci), so extending its use to joint infections is a direct extension of its existing antibacterial spectrum rather than a novel mechanism. A dedicated pharmacokinetic study (PMID 28784675) confirms that Cefuroxime penetrates synovial fluid at concentrations adequate for antimicrobial activity, which mechanistically supports its use in joint-space infections.

One important caveat: several retrieved publications concern Lyme borreliosis/Lyme arthritis rather than typical pyogenic bacterial arthritis. Lyme arthritis is a distinct entity for which doxycycline, amoxicillin, or ceftriaxone are the standard first-line agents — oral cefuroxime axetil is an approved *alternative* in early Lyme disease, but this should not be conflated with general bacterial (septic) arthritis evidence. This distinction should be preserved in any downstream clinical use case.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6695158](https://pubmed.ncbi.nlm.nih.gov/6695158/) | 1984 | Case series/Cohort | Scandinavian Journal of Infectious Diseases | Cefuroxime used in 17 patients with acute septic arthritis (mostly *S. aureus*), compared against cloxacillin/ampicillin; serum and joint fluid concentrations evaluated |
| [28784675](https://pubmed.ncbi.nlm.nih.gov/28784675/) | 2017 | PK study | Antimicrobial Agents and Chemotherapy | Confirms adequate Cefuroxime penetration into synovial fluid after a single 1,500 mg IV dose in patients undergoing knee arthroscopy |
| [34756070](https://pubmed.ncbi.nlm.nih.gov/34756070/) | 2021 | Network meta-analysis | Microbiology Spectrum | 40-year evidence review comparing oral/injectable antibiotics (incl. cefuroxime axetil) for Lyme disease, including Lyme arthritis |
| [24924733](https://pubmed.ncbi.nlm.nih.gov/24924733/) | 2014 | Guideline | Zeitschrift für Rheumatologie | German Society for Rheumatology recommendations for diagnosis and treatment of Lyme arthritis |
| [21393124](https://pubmed.ncbi.nlm.nih.gov/21393124/) | 2011 | Review | Journal of Antimicrobial Chemotherapy | 10-year review of adult native septic arthritis epidemiology, informing empirical antibiotic stewardship choices |
| [29290233](https://pubmed.ncbi.nlm.nih.gov/29290233/) | 2017 | Guideline | Archives de Pédiatrie | French Pediatric Infectious Disease Group proposals for antibiotic therapy of bone and joint infections in children |
| [23599360](https://pubmed.ncbi.nlm.nih.gov/23599360/) | 2013 | Cohort | Journal of Antimicrobial Chemotherapy | Retrospective comparison of penicillin, dicloxacillin, and cefuroxime as definitive therapy for penicillin-susceptible *S. aureus* bacteraemia |
| [17956820](https://pubmed.ncbi.nlm.nih.gov/17956820/) | 2007 | Review | Archives de Pédiatrie | PK/PD parameters predicting antibiotic efficacy in pediatric osteoarticular infections |
| [17113969](https://pubmed.ncbi.nlm.nih.gov/17113969/) | 2006 | Review | Clinics in Dermatology | Diagnosis, treatment, and prognosis of erythema migrans and Lyme arthritis |
| [28482848](https://pubmed.ncbi.nlm.nih.gov/28482848/) | 2017 | Review | Pediatric Rheumatology Online Journal | Review of Lyme arthritis in children, differential diagnosis from juvenile idiopathic arthritis |

## Malaysia Market Information

39 Cefuroxime registrations are recorded as marketed (已上市) in this dataset, but individual license number, product name, dosage form, and approved indication text fields were not populated in this data pull, so a per-product table cannot be presented without guessing.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence for Cefuroxime in bacterial arthritis is L3 (case series, cohort, PK data, and guideline-level support) rather than RCT-confirmed, but the mechanistic and pharmacokinetic basis is sound and consistent with an already-established off-label use pattern. No TFDA safety data was available to complete a formal safety gate review.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking (DG001)
- DrugBank mechanism-of-action record (DG002)
- Dedicated clinical outcome data for bacterial (non-Lyme) septic arthritis specifically, ideally comparative/RCT-level
- Clear separation of Lyme arthritis literature from general bacterial/septic arthritis literature before any clinical guardrail is finalized
- Verified TFDA-approved indication text per license number to establish the true "original indication" baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

