---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal, classically used to treat systemic fungal infections (e.g., aspergillosis, histoplasmosis, candidiasis) in immunocompromised patients. The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis pneumonia)**, with **0 clinical trials** and **20 publications** currently identified — though the literature itself contains a notable caution against this prediction (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in source data (TFDA/NPRA label text not yet collected — DG001). Itraconazole is generally known as a broad-spectrum triazole antifungal for systemic fungal infections. |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002). Based on general pharmacological knowledge, itraconazole is a triazole-class antifungal that inhibits fungal cytochrome P450-dependent 14α-demethylase, blocking ergosterol synthesis in the fungal cell membrane. Its proven efficacy is in systemic mycoses (aspergillosis, histoplasmosis, blastomycosis, candidiasis) in the same immunocompromised populations (HIV/AIDS, transplant recipients, hematologic malignancy) who are also at highest risk for Pneumocystis pneumonia (PCP) — this population overlap is the likely basis for the TxGNN association.

However, the literature evidence itself raises an important caveat: one mechanistic study (PMID 12606318) reports that *Pneumocystis carinii* possesses a lanosterol 14α-demethylase (Erg11) with sequence differences from azole-resistant fungi, and states that *Pneumocystis carinii* is "intrinsically resistant to treatment with azole antifungal medications." This directly challenges the biological plausibility of itraconazole as a treatment for pneumocystosis, even though it supports itraconazole's established role in *preventing other* fungal co-infections in the same at-risk patients. The one identified randomized controlled trial (PMID 11737382) tested itraconazole prophylaxis for "deep fungal infections" broadly in HIV patients, not pneumocystosis specifically.

Given this contradiction between the TxGNN prediction and the mechanistic literature, the association is best interpreted as reflecting shared risk-population co-occurrence in the knowledge graph rather than a direct pharmacological mechanism against *Pneumocystis*.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled Phase III trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected patients (not PCP-specific) |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanism study | Am J Respir Cell Mol Biol | Characterized *Pneumocystis carinii* lanosterol 14α-demethylase; concludes PC is intrinsically resistant to azole antifungals — a key caution against this indication |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Reviews therapy/prophylaxis for *Pneumocystis carinii*, *Toxoplasma*, and other opportunistic pathogens, incl. antifungal agent mechanisms |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary/secondary prophylaxis of opportunistic infections in HIV, including PCP |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Topics Infect Dis | Prophylaxis/treatment of infection (incl. fungal) in bone marrow transplant recipients |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infection (incl. fungal/PCP) after lung transplantation |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational | Indian J Med Microbiol | Profile of respiratory fungal pathogens in immunocompetent vs immunocompromised hosts by CD4 count |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Observational | Transplantation Proceedings | Invasive fungal infections after kidney transplantation, single-center experience |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Frontiers in Immunology | *Talaromyces marneffei* and *Pneumocystis jirovecii* coinfection in a child with STAT1 mutation |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case report | Annals of Internal Medicine | Uveitis associated with rifabutin prophylaxis and itraconazole therapy (safety signal) |

---

## Malaysia Market Information

NPRA records show **8 registered licenses** for itraconazole with market status "已上市 (Marketed)". Individual license numbers, product names, dosage forms, and approved indication text were not returned in this data pull — retrieval from NPRA is needed before this table can be populated.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack (DG001 — blocking gap for safety screening).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is not supported by direct clinical evidence (no clinical trials on itraconazole for pneumocystosis), and the strongest mechanistic literature found actually argues against biological plausibility (*Pneumocystis* is reported as intrinsically azole-resistant). Combined with a blocking safety data gap (TFDA/NPRA label warnings and contraindications unavailable), this candidate cannot proceed to S1 safety evaluation as-is.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (warnings, contraindications) to close the blocking safety gap (DG001)
- Confirmed drug mechanism of action data from DrugBank (DG002)
- Targeted literature/clinical search specifically on itraconazole efficacy against *Pneumocystis jirovecii* (rather than general fungal-infection prophylaxis in the same risk population), to resolve the resistance concern raised by PMID 12606318
- NPRA license-level detail (product names, indications, dosage forms) for the 8 registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

