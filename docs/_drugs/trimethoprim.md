---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 670
evidence_level: L5
indication_count: 5
---

# Trimethoprim
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

# Trimethoprim: From Bacterial Infections to Pneumocystosis (Pneumocystis Pneumonia)

## One-Sentence Summary

Trimethoprim is a folate-synthesis-inhibiting antibacterial, most widely used in combination with sulfamethoxazole (TMP-SMX / co-trimoxazole) for common bacterial infections such as urinary tract infections. The TxGNN model highlights **Pneumocystosis (Pneumocystis jirovecii pneumonia, PCP)** as its top-ranked predicted indication, and the evidence pack shows this is already an extensively studied, real-world use — supported by **dozens of clinical trials (including multiple completed Phase 3 RCTs)** and **20 publications**, though key Malaysia label safety data is still missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the NPRA license extract (all `approved_indication_text` fields are blank); literature within this evidence pack describes trimethoprim-sulfamethoxazole's classic approved uses as urinary tract infection, otitis media, shigellosis, and pneumocystosis (PMID 382841) |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 0.00% (as reported in the evidence pack) |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| Malaysia Market Status | Marketed (已上市) |
| Number of Registrations | 70 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trimethoprim is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the literature captured within this pack, trimethoprim is described as an "enzyme-specific inhibitor of bacterial folate synthesis" (PMID 382841), most often used as the fixed-dose combination trimethoprim-sulfamethoxazole (TMP-SMX / co-trimoxazole / Septra / Bactrim). This dual blockade of the folate pathway (trimethoprim inhibiting dihydrofolate reductase, sulfamethoxazole inhibiting dihydropteroate synthase) gives the combination broad-spectrum antimicrobial activity against bacteria and, notably, against the fungal-like organism *Pneumocystis jirovecii*.

Unlike a typical "repurposing" candidate with only mechanistic plausibility, pneumocystosis is not a novel hypothesis for this drug — TMP-SMX is already the internationally recognized first-line agent for both treatment and prophylaxis of PCP, as reflected by the volume and maturity of the clinical trial record (spanning from early AIDS-era trials in the late 1980s/1990s through active studies in 2024-2026). This strengthens confidence in the TxGNN signal but also means the primary value of this evaluation lies in confirming Malaysia-specific regulatory alignment (label indication, dosing, safety warnings) rather than establishing novel efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000727](https://clinicaltrials.gov/study/NCT00000727) | Phase 3 | Completed | 322 | SMX-TMP (oral) vs. aerosolized pentamidine for secondary PCP prophylaxis in AIDS patients on AZT |
| [NCT00001014](https://clinicaltrials.gov/study/NCT00001014) | Phase 3 | Completed | 302 | Trimetrexate+leucovorin vs. TMP/SMX for moderately severe PCP in AIDS/HIV patients |
| [NCT00001013](https://clinicaltrials.gov/study/NCT00001013) | Phase 3 | Completed | 364 | Trimetrexate+leucovorin vs. TMP/SMX for moderately severe PCP in AIDS/HIV patients |
| [NCT00000748](https://clinicaltrials.gov/study/NCT00000748) | Phase 3 | Completed | 2500 | Daily vs. thrice-weekly TMP/SMX (TMS) dosing for PCP prophylaxis in HIV-infected patients |
| [NCT00000816](https://clinicaltrials.gov/study/NCT00000816) | Phase 4 | Completed | 370 | Gradual vs. routine initiation of SMX/TMP for primary PCP prophylaxis, assessing adverse-reaction reduction |
| [NCT00000655](https://clinicaltrials.gov/study/NCT00000655) | Phase 2 | Completed | 300 | Atovaquone vs. Septra (TMP/SMX) for mild-to-moderate PCP treatment in AIDS patients |
| [NCT03978559](https://clinicaltrials.gov/study/NCT03978559) | Phase 4 | Unknown | 122 | Caspofungin + TMP-SMX vs. TMP-SMX alone as first-line therapy in non-HIV severe PCP |
| [NCT00302341](https://clinicaltrials.gov/study/NCT00302341) | Phase 3 | Terminated | 48 | Pafuramidine (DB289) vs. TMP-SMX for acute PCP in HIV/AIDS (non-inferiority trial) |
| [NCT04851015](https://clinicaltrials.gov/study/NCT04851015) | Phase 3 | Recruiting | 416 | Low-dose vs. standard-dose TMP-SMX for PCP treatment, targeting reduced adverse events |
| [NCT06499233](https://clinicaltrials.gov/study/NCT06499233) | Phase 4 | Recruiting | 800 | Efficacy/safety of prophylactic TMP-SMX for PCP in autoimmune inflammatory rheumatic disease patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37358837](https://pubmed.ncbi.nlm.nih.gov/37358837/) | 2023 | Review | JAMA | Clinical review on prophylaxis against Pneumocystis jirovecii pneumonia in adults |
| [37574166](https://pubmed.ncbi.nlm.nih.gov/37574166/) | 2024 | Retrospective Cohort | Chest | Low-dose vs. conventional-dose TMP-SMX treatment for PCP in non-HIV patients; comparable efficacy, fewer adverse events |
| [29092853](https://pubmed.ncbi.nlm.nih.gov/29092853/) | 2018 | Cohort | Annals of the Rheumatic Diseases | TMP-SMX as primary PCP prophylaxis in rheumatic disease patients on high-dose glucocorticoids |
| [39389264](https://pubmed.ncbi.nlm.nih.gov/39389264/) | 2025 | Retrospective Cohort | J Infect Chemother | Low-dose vs. standard-dose sulfamethoxazole/trimethoprim for PCP prevention using a large EMR database |
| [37797822](https://pubmed.ncbi.nlm.nih.gov/37797822/) | 2024 | Retrospective Cohort | J Infect Chemother | ST discontinuation causes and thrombocytopenia during PCP prophylaxis, single-center study |
| [32000290](https://pubmed.ncbi.nlm.nih.gov/32000290/) | 2020 | Review | Semin Respir Crit Care Med | Overview of Pneumocystis jiroveci biology, transmission, and disease in immunocompromised hosts |
| [15190141](https://pubmed.ncbi.nlm.nih.gov/15190141/) | 2004 | Review | New England Journal of Medicine | Comprehensive review of Pneumocystis pneumonia pathophysiology and management |
| [21653531](https://pubmed.ncbi.nlm.nih.gov/21653531/) | 2011 | Review | Proc Am Thorac Soc | Review of HIV-associated PCP epidemiology and treatment gaps |
| [24617414](https://pubmed.ncbi.nlm.nih.gov/24617414/) | 2014 | Review | Expert Rev Anti Infect Ther | Mini-review from Latin American/Portuguese-speaking expert meeting on Pneumocystis and pneumocystosis |
| [6600803](https://pubmed.ncbi.nlm.nih.gov/6600803/) | 1983 | Review | Mayo Clinic Proceedings | Review of trimethoprim-sulfamethoxazole antimicrobial spectrum, including pneumocystosis use |

---

## Malaysia Market Information

The evidence pack confirms **70 total NPRA registrations** for trimethoprim (Market Status: Marketed), but the license-level fields (license number, product name, dosage form, manufacturer, approved indication text) are all blank in the current data extract — no individual authorizations can be listed at this time. Obtaining these details from the NPRA product register is recommended before finalizing the label-alignment assessment.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — flagged as a Blocking-severity data gap requiring TFDA/NPRA label retrieval, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical evidence for pneumocystosis is strong (L1 — multiple completed Phase 3 RCTs plus a mature 50-year literature base), and TMP-SMX is already the internationally recognized standard of care for this indication. However, the evidence pack flags a **Blocking**-severity data gap (DG001: TFDA/NPRA label warnings and contraindications) that explicitly prevents entry into the S1 safety initial-assessment stage. Efficacy evidence alone cannot support a "Proceed" decision until this safety gate is cleared.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, precautions, contraindications) — download and parse per DG001 remediation plan
- DrugBank-sourced mechanism-of-action detail (DG002)
- Malaysia license-level detail (product names, dosage forms, approved indication text) for the 70 registered products
- Route-of-administration compatibility confirmation (oral vs. IV) for PCP treatment vs. prophylaxis use cases
- Drug-drug interaction data (current DDI query returned no results)

---

## Other Predicted Indications (Same Evidence Pack)

For completeness, this multi-indication evidence pack (TW-DB00440-multi) also scored four additional TxGNN-predicted indications for trimethoprim:

| Rank | Disease | Evidence Level | Decision Stage | Recommendation |
|------|---------|----------------|-----------------|-----------------|
| 2 | Urinary tract infection | L1 | S3 | Proceed with Guardrails |
| 3 | Infectious otitis media | L2 | S2 | Research Question |
| 4 | Conjunctivitis | pending | pending | pending |
| 5 | Acute contagious conjunctivitis | L5 | S0 | Hold |

Urinary tract infection (rank 2) is notable: it already carries L1 evidence and a "Proceed with Guardrails" scoring in the source data, reflecting trimethoprim's long-established classic use in UTI — a separate report may be warranted for that indication specifically.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

