---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 5
---

# Albendazole
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

# Albendazole: From Intestinal Helminthiasis to Echinococcus granulosus Infectious Disease

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole anthelmintic primarily used for the treatment of intestinal helminthiasis and tissue-invasive parasitic infections.
The TxGNN model predicts it may be effective for **Echinococcus granulosus Infectious Disease** (cystic hydatid disease),
supported by **1 registered clinical trial** and **20 publications**, including multiple systematic reviews that position albendazole as the standard pharmacological option for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiparasitic — broad-spectrum anthelmintic for intestinal and tissue helminthiasis |
| Predicted New Indication | Echinococcus granulosus Infectious Disease (Cystic Echinococcosis / Hydatid Disease) |
| TxGNN Prediction Score | Not available (raw score: 0.0 — score extraction pending) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 29 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Albendazole belongs to the benzimidazole class of anthelmintics. Its mechanism of action involves selective binding to parasite β-tubulin, inhibiting polymerisation into functional microtubules. This disrupts the parasite's cytoskeletal architecture, impairs intracellular glucose transport and energy metabolism, and ultimately leads to parasite immobilisation and death. The pharmacologically active metabolite — albendazole sulphoxide (ABZ-SO) — is generated through hepatic first-pass metabolism and is responsible for systemic antiparasitic activity. (Note: detailed MOA data from DrugBank has been flagged as a data gap and is pending retrieval.)

*Echinococcus granulosus* is a tapeworm (cestode) causing cystic echinococcosis in humans, primarily affecting the liver and lungs. The parasite's dependence on tubulin-based cell division and cytoskeletal integrity makes it a biologically plausible target for benzimidazole drugs. Multiple pharmacokinetic studies have confirmed that ABZ-SO penetrates into hydatid cysts, where it exerts a parasitostatic effect — slowing cyst development and reducing parasite viability. While albendazole does not consistently achieve complete parasitocidal activity (particularly in large or calcified cysts), it remains the only widely available, guideline-supported medical therapy for this disease.

The TxGNN knowledge graph prediction is strongly consistent with established clinical practice: WHO guidelines and international expert consensus already recognise albendazole as the first-line pharmacological agent for cystic echinococcosis, used either as monotherapy for inoperable cases or as perioperative adjuvant treatment. This prediction therefore serves as a mechanistic and evidence-level validation signal, confirming that the knowledge graph correctly captures the drug–disease relationship. The main repurposing opportunity in the Malaysian context relates to whether the local product labels formally include this indication — a point requiring label verification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Recruiting | 43 | Evaluates a new multiplex qPCR technique for echinococcosis diagnosis; albendazole is cited as the standard benzimidazole treatment backbone for cystic echinococcosis (CE) alongside surgery, described as parasitostatic only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clinical Microbiology Reviews | Comprehensive state-of-the-art review of echinococcosis; confirms albendazole as the cornerstone pharmacological treatment for both CE and alveolar echinococcosis (AE) |
| [27085708](https://pubmed.ncbi.nlm.nih.gov/27085708/) | 2016 | Systematic Review | Parasitology Research | Individual patient data meta-analysis of intra-cystic ABZ-SO concentrations; demonstrates drug penetration into hydatid cysts and identifies cyst size and location as key determinants of exposure |
| [29976137](https://pubmed.ncbi.nlm.nih.gov/29976137/) | 2018 | Systematic Review & Meta-analysis | BMC Infectious Diseases | Systematic review of medical treatment options for CE; analyses efficacy data across four treatment modalities; highlights albendazole as the primary pharmacological backbone despite variable response rates |
| [2256768](https://pubmed.ncbi.nlm.nih.gov/2256768/) | 1990 | Clinical Series | Annals of Tropical Medicine and Parasitology | Pioneer study treating 50 patients with hydatid cysts (105 cysts total) with albendazole 10–12 mg/kg/day for 3 months; 4 healed, 31 improved; side effects were non-severe |
| [24778101](https://pubmed.ncbi.nlm.nih.gov/24778101/) | 2014 | Clinical Study | Croatian Medical Journal | Plasma and intra-cyst ABZ-SO concentrations investigated in liver hydatidosis patients; drug exposure in cyst fluid predicts parasitological response and disease recurrence |
| [36384195](https://pubmed.ncbi.nlm.nih.gov/36384195/) | 2022 | In Vitro Study | Experimental Parasitology | Albendazole-loaded β-cyclodextrin nanocarriers show enhanced protoscolicidal activity against *E. granulosus* s.s. compared to standard formulation; addresses the poor oral bioavailability limitation |
| [31586448](https://pubmed.ncbi.nlm.nih.gov/31586448/) | 2020 | Animal Study | Acta Tropica | Combination of IL-12 + IFN-γ cytokines with albendazole shows superior efficacy for CE prophylaxis and treatment in Balb/c mice compared to albendazole monotherapy |
| [31123477](https://pubmed.ncbi.nlm.nih.gov/31123477/) | 2019 | Laboratory Study | Iranian Journal of Parasitology | Solid lipid nanoparticle formulation of albendazole evaluated for protoscolicidal effects in vitro and in vivo; nanoformulation significantly improves efficacy over standard albendazole |
| [22509076](https://pubmed.ncbi.nlm.nih.gov/22509076/) | 2012 | Review | World Journal of Gastroenterology | Clinical and therapeutic review of hepatic echinococcosis; describes surgery combined with perioperative albendazole as the management standard; discusses prognostic factors |
| [39195613](https://pubmed.ncbi.nlm.nih.gov/39195613/) | 2024 | Review | Tropical Medicine and Infectious Disease | Receptor tyrosine kinase signalling as a novel therapeutic target in hepatic echinococcosis; positions albendazole as current preferred drug while identifying mechanistic limitations and resistance challenges |

---

## Malaysia Market Information

The Evidence Pack retrieved **29 active registrations** from the Malaysian NPRA database for Albendazole. However, detailed product-level information — including product names, dosage forms, manufacturers, and approved indication text — was not available in the current data extract (all fields returned empty).

**Action required:** Please query the NPRA product register directly at [https://www.npra.gov.my](https://www.npra.gov.my) to retrieve individual authorisation details for the 29 registered Albendazole products, and to confirm whether echinococcosis/hydatid disease is listed as an approved indication in Malaysian product labels.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety warnings, contraindications, and drug interaction data were not retrieved in this Evidence Pack. This has been flagged as a **blocking data gap (DG001)** — resolution requires downloading the official Malaysian product label from the NPRA website. Until this is resolved, formal safety pre-screening for this indication cannot be completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole is already registered and marketed in Malaysia with 29 active licences, and the global evidence base — including WHO guidelines, multiple systematic reviews, and decades of clinical experience — firmly supports its use as the first-line pharmacological therapy for cystic echinococcosis caused by *E. granulosus*. The TxGNN model prediction is directly consistent with this established evidence, confirming strong mechanistic plausibility. The primary outstanding question is whether this indication is already formally approved on Malaysian product labels, rather than whether the drug works.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve all 29 Malaysian product labels (package inserts) from the NPRA website to confirm currently approved indications, contraindications, and warnings
- **[High — DG002]** Obtain complete MOA data from DrugBank (DB00518) to formally document the tubulin-binding mechanism for the regulatory dossier
- Retrieve detailed NPRA licence records (product names, dosage forms, manufacturers) for the 29 registered Albendazole products
- Confirm whether echinococcosis / hydatid disease is already an approved indication in the existing Malaysian product labels; if so, this is a label confirmation rather than a new repurposing application
- If the indication is not currently approved locally, prepare a label extension application supported by WHO treatment guidelines and the available systematic review data
- Clarify the TxGNN prediction score extraction issue (all scores returning as 0.0) to ensure correct ranking and confidence calibration for downstream decision-making

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

