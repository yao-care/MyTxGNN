---
layout: default
title: Amphotericin B
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 5
---

# Amphotericin B
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

# Amphotericin B: From Systemic Fungal Infections to Esophageal Candidiasis

## One-Sentence Summary

Amphotericin B is a broad-spectrum polyene antifungal agent, long established as a gold-standard treatment for serious invasive systemic fungal infections.
The TxGNN model predicts it may be effective for **Esophageal Candidiasis**,
with **2 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic fungal infections (registered product details not available in current system) |
| Predicted New Indication | Esophageal Candidiasis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, Amphotericin B is a polyene macrolide antifungal whose efficacy in treating serious invasive fungal infections has been well established over several decades. It is known to bind with high affinity to ergosterol — a sterol unique to fungal cell membranes — forming transmembrane pores that disrupt osmotic equilibrium and cause leakage of intracellular contents, leading to direct fungicidal activity against *Candida* species. Both intravenous formulations — conventional deoxycholate (Fungizone) and liposomal (AmBisome) — can achieve effective drug concentrations at esophageal mucosal tissue.

Esophageal candidiasis is caused by *Candida albicans* and, less commonly, other *Candida* species (*C. glabrata*, *C. tropicalis*, *C. krusei*). Because the disease pathogen is the very same target as Amphotericin B's mechanism of action, the mechanistic link is direct and well-established — this is not a leap across disease categories but an extension of proven antifungal activity to a specific anatomical site. The mucosal nature of esophageal disease is fully addressable by intravenous administration.

Clinically, Amphotericin B has long served as an alternative or salvage therapy for esophageal candidiasis, particularly in immunocompromised patients (HIV/AIDS, haematological malignancies) and in those with azole-refractory disease. A completed clinical trial (NCT00002041) directly evaluated Amphotericin B in biopsy-proven *Candida* esophagitis, and multiple randomised controlled trials have included AmB as an active comparator arm against newer agents such as caspofungin and anidulafungin — collectively confirming its established role in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00002041](https://clinicaltrials.gov/study/NCT00002041) | Phase NA | Completed | N/A | Directly evaluated Amphotericin B for biopsy-proven *Candida* esophagitis in immunocompromised patients; assessed optimal treatment duration and compared two dose levels for efficacy and nephrotoxicity |
| [NCT00041704](https://clinicaltrials.gov/study/NCT00041704) | Phase 2 | Completed | 19 | Phase 2 study of anidulafungin for azole-refractory mucosal candidiasis; Amphotericin B included as an alternative comparator, reflecting its salvage role in fluconazole-resistant esophageal disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8804799](https://pubmed.ncbi.nlm.nih.gov/8804799/) | 1996 | RCT | Chemotherapy | Randomised trial of oral fluconazole vs IV Amphotericin B (0.3 mg/kg) in 31 cancer patients with endoscopy-confirmed esophageal candidiasis; both agents produced rapid resolution of dysphagia and odynophagia |
| [11796357](https://pubmed.ncbi.nlm.nih.gov/11796357/) | 2002 | RCT | Antimicrobial Agents and Chemotherapy | Phase 2 randomised double-blind multicentre study comparing caspofungin vs Amphotericin B (0.5 mg/kg/day IV) for oropharyngeal and esophageal candidiasis; established AmB as the active comparator benchmark |
| [41226935](https://pubmed.ncbi.nlm.nih.gov/41226935/) | 2025 | Clinical Pharmacotherapy Review | Journal of Clinical Medicine | Comprehensive review of pharmacological management of oral and esophageal candidiasis from a clinical pharmacotherapy perspective; positions Amphotericin B within current treatment algorithms |
| [10839593](https://pubmed.ncbi.nlm.nih.gov/10839593/) | 2000 | Clinical Trial | AIDS | ACTG Study 295; evaluated Amphotericin B oral suspension for fluconazole-refractory oral candidiasis in HIV-positive patients, demonstrating AmB's utility in azole-resistant mucosal disease |
| [35699443](https://pubmed.ncbi.nlm.nih.gov/35699443/) | 2022 | Animal/Preclinical | Antimicrobial Agents and Chemotherapy | Evaluated cochleated oral formulation of Amphotericin B in mucocutaneous candidiasis mouse models and azole-resistant CMC patients; supports feasibility of non-parenteral AmB for mucosal candidiasis |
| [7811544](https://pubmed.ncbi.nlm.nih.gov/7811544/) | 1994 | Cohort/Resistance Review | AIDS Research and Human Retroviruses | Reviewed fluconazole-resistant mucosal candidiasis patterns in HIV patients; discusses Amphotericin B as a key salvage option for azole-resistant esophageal and oropharyngeal disease |
| [11590489](https://pubmed.ncbi.nlm.nih.gov/11590489/) | 2000 | Review | HIV Clinical Trials | Reviewed therapeutic options for oropharyngeal and esophageal candidiasis in HIV/AIDS patients; contextualises Amphotericin B's role relative to azoles and echinocandins |
| [10959741](https://pubmed.ncbi.nlm.nih.gov/10959741/) | 2000 | Cohort Study | Pediatric Infectious Disease Journal | Investigated clinical presentation and risk factors of esophageal candidiasis in a large prospectively monitored cohort of HIV-infected children at the National Cancer Institute |
| [11363911](https://pubmed.ncbi.nlm.nih.gov/11363911/) | 1996 | Review | Journal of the International Association of Physicians in AIDS Care | Overview of candidiasis — including esophageal involvement — in immunocompromised hosts; includes discussion of Amphotericin B therapy |
| [3181663](https://pubmed.ncbi.nlm.nih.gov/3181663/) | 1983 | Original Article | Digestive Diseases and Sciences | Early clinical characterisation of *Candida* esophagitis including odynophagia, dysphagia, and GI bleeding; establishes antifungal treatment (including Amphotericin B) as standard of care |

---

## Malaysia Market Information

The evidence pack confirms **2 registered products** in Malaysia with market status **已上市 (Marketed)**. However, detailed registration data — including licence numbers, product names, dosage forms, and approved indication text — are not available in the current evidence pack. Please refer to the [NPRA registration database](https://www.npra.gov.my/) for full product details.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not retrievable in this evidence pack (Data Gap DG001 — Blocking severity). Remediation: download and parse the NPRA-approved package insert PDF. Known class-level concerns for Amphotericin B include infusion-related reactions and nephrotoxicity with the deoxycholate formulation; liposomal formulations carry a significantly improved tolerability profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amphotericin B's antifungal mechanism directly targets the causative pathogen of esophageal candidiasis (*Candida* spp. via ergosterol binding), making this a mechanistically sound application. A completed clinical trial has directly evaluated AmB in biopsy-confirmed *Candida* esophagitis, multiple published RCTs include AmB as the active comparator, and a 2025 clinical pharmacotherapy review positions it within current treatment guidelines — collectively meeting the L2 evidence threshold for a Proceed with Guardrails recommendation.

**To proceed, the following is needed:**

- **Safety data retrieval (Blocking):** Download and parse the NPRA package insert PDF to extract key warnings, contraindications, and drug interaction data (DG001)
- **Mechanism of action data:** Query the DrugBank API to obtain the full MOA profile for Amphotericin B (DG002)
- **Registered dosage forms:** Confirm which of the 2 registered Malaysian products is the deoxycholate vs. liposomal formulation, as these differ substantially in safety profile and dosing
- **Safety monitoring protocol:** Define nephrotoxicity monitoring plan (serum creatinine, electrolytes) and infusion-related reaction management, particularly for the conventional formulation
- **Azole-resistance context:** Clarify the local Malaysian epidemiology of fluconazole-resistant *Candida* to position AmB's role relative to echinocandins as first-line alternatives in resistant cases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

