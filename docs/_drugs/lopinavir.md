---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lopinavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lopinavir is an HIV protease inhibitor, typically co-administered with ritonavir (LPV/r), and is a cornerstone antiretroviral therapy for HIV-1 and HIV-2 infection in humans.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection)**,
with **0 clinical trials** and **0 publications** directly supporting this veterinary application — the prediction currently rests entirely on computational modelling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 / HIV-2 infection (detailed approved indication text not retrievable from current registry records) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Lopinavir inhibits the HIV aspartyl protease — an enzyme essential for cleaving the Gag-Pol polyprotein precursor into mature, functional viral proteins. Without this cleavage step, newly budded virions remain structurally immature and non-infectious. Lopinavir is always co-formulated with the pharmacokinetic booster ritonavir to maintain plasma concentrations above the inhibitory threshold.

Feline Immunodeficiency Virus (FIV) is a lentivirus within the same broad retroviral family as HIV. The TxGNN knowledge-graph model likely detected this taxonomic and protease-structural relatedness, and assigned a high prediction score based on that similarity. In principle, if FIV protease shares sufficient geometric complementarity with Lopinavir's binding pharmacophore, cross-species inhibition could occur — a concept already validated in the closely related SIV primate model (see rank-2 indication evidence below).

However, the mechanistic rationale provided in this Evidence Pack is cautionary: the substrate-binding pocket of FIV protease differs appreciably from that of HIV-1 protease, and known HIV protease inhibitors demonstrate markedly reduced binding affinity for FIV protease as a consequence. To date, **no in vitro or in vivo efficacy data** exist to bridge this theoretical gap for Lopinavir specifically in cats, making the prediction one of computational inference rather than observed biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the feline acquired immunodeficiency syndrome indication.

> **Note:** Three preclinical publications supporting Lopinavir activity in the closely related **Simian Immunodeficiency Virus (SIV)** primate model were identified for the rank-2 predicted indication (see below for context). These do not constitute evidence for the feline indication but are scientifically adjacent.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study (NHP) | Journal of Virology | Quadruple ART including Lopinavir in SIVmac251-infected cynomolgus macaques produced rapid viral decay kinetics, broadly consistent with HIV-1 dynamics |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal study (SHIV chimeric model) | Microbes and Infection | SHIV carrying an HIV-1-derived protease gene was fully suppressed by a protease inhibitor in cell culture and showed sustained low-level viraemia in rhesus macaques post-inoculation, validating the SHIV model for PI evaluation |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study (oral PK/PD, monkey) | Journal of Virological Methods | Oral LPV/RTV + AZT + 3TC HAART in SHIV89.6P-infected rhesus macaques suppressed viral load and partially restored CD4/CD8 ratios, demonstrating oral bioavailability and antiviral activity in an NHP model |

---

## Malaysia Market Information

Seven product registrations for Lopinavir are recorded with the National Pharmaceutical Regulatory Agency (NPRA). Detailed licence numbers, product names, dosage forms, and approved indication texts were not returned in the current dataset query; full registration details can be retrieved directly from the NPRA Product Registration database.

| Item | Detail |
|------|--------|
| Total Active Registrations | 7 |
| Market Status | ✓ Marketed |
| Data Availability | Licence-level details pending retrieval from NPRA |

---

## Safety Considerations

Detailed warnings, contraindications, and drug-drug interaction data were not available in this Evidence Pack. Please refer to the product package insert (Prescribing Information / Summary of Product Characteristics) for complete safety information, including the well-documented QTc prolongation risk, hepatotoxicity warnings, and the extensive CYP3A4-mediated drug interaction profile of Lopinavir/ritonavir.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high computational score to Lopinavir for feline AID syndrome based on lentiviral protease homology, but the FIV protease substrate pocket differs structurally from HIV-1 protease in ways that substantially reduce inhibitor binding affinity — and no experimental evidence (cell-based, animal, or clinical) currently exists to validate this repurposing hypothesis in cats.

**To proceed from Hold to an active research question, the following is needed:**

- **In vitro binding assay**: Determine the IC₅₀ of Lopinavir against recombinant FIV protease to establish whether biochemical inhibition is feasible at pharmacologically achievable concentrations
- **Cell culture efficacy study**: Test antiviral activity in FIV-infected feline lymphocyte lines (e.g., MYA-1 or FL-4 cells) using standard p24/p27 antigen reduction endpoints
- **MOA data retrieval**: Obtain full DrugBank / TFDA package insert data to complete the mechanistic link analysis and safety pre-screening (Data Gaps DG001 and DG002)
- **Veterinary pharmacokinetic data**: Lopinavir/ritonavir has been administered orally to cats during COVID-19 research; existing PK data from those studies should be reviewed for dose-exposure adequacy in felines
- **Regulatory pathway clarification**: Confirm whether this would be pursued as a veterinary medicinal product and identify the applicable regulatory authority (e.g., Council of Agriculture in Taiwan, or equivalent in Malaysia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

