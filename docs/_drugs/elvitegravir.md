---
layout: default
title: Elvitegravir
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

# Elvitegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Elvitegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), historically used as part of antiretroviral combination therapy for HIV-1 infection.
> The TxGNN model's top prediction links it to **Simian Immunodeficiency Virus (SIV) Infection**, supported by **7 publications** and **0 clinical trials** —
> but this evidence describes elvitegravir's *known* antiretroviral pharmacology being studied in non-human primate models, not a genuinely new human indication.

*Note: This evidence pack contains three ranked predictions (candidate ID `TW-DB09101-multi`). This report focuses on the top-ranked prediction (SIV infection) and briefly addresses the other two below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from literature evidence in this pack — not formally documented in regulatory/DrugBank records provided; see data gap below) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical/mechanism studies only — no clinical trials identified) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field for elvitegravir is not available in this evidence pack (flagged as data gap DG002, High severity). However, the literature evidence retrieved for this prediction consistently describes elvitegravir as an **HIV-1 integrase strand transfer inhibitor (INSTI)**: it blocks integration of viral cDNA into host chromosomal DNA by inhibiting the strand-transfer step of the retroviral integrase enzyme (PMID 17977962).

This mechanism is not unique to HIV-1 — the integrase enzyme and its catalytic mechanism are highly conserved across lentiviruses, a family that includes HIV-1 (infects humans), SIV (infects non-human primates), and FIV (infects cats). This conservation is almost certainly why TxGNN links elvitegravir to SIV infection: the association reflects **target/mechanism homology across related viruses**, rather than a distinct new therapeutic opportunity in a human patient population.

Importantly, when the underlying literature is examined, none of it describes elvitegravir being used to treat a disease called "SIV infection" in the sense of a new clinical indication. Instead, the papers use SIV- or SHIV-infected macaques and humanized mice as **surrogate/preclinical models** to study elvitegravir's resistance profile, antiviral activity, and prevention potential (e.g., topical/vaginal microbicide inserts) — research that ultimately supports HIV-1 prevention and treatment in humans, not a new disease target. This distinction matters for repurposing decisions: the "new indication" here is an animal model system, not a human disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal study (macaque) | J Infect Dis | Tenofovir alafenamide/elvitegravir vaginal inserts gave extended post-exposure protection against vaginal SHIV infection in macaques |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Animal study (humanized mouse) | Front Immunol | Describes a dual-purpose humanized mouse model for testing antiviral strategies against both SIV and HIV |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro / resistance study | Antimicrob Agents Chemother | Compares bictegravir/cabotegravir activity against INSTI-resistant SIVmac239 and HIV-1; elvitegravir referenced as an established INSTI comparator |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro / resistance study | J Virol | Characterizes drug resistance profiles of integrase strand transfer inhibitors (including elvitegravir) in SIVmac239 |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Model/methods study | Antimicrob Agents Chemother | Establishes a simian-tropic HIV model to study integrase inhibitor drug resistance |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | In vitro / resistance study | J Virol | HIV-1 integrase resistance mutations introduced into SIVmac239 and tested for INSTI susceptibility, including elvitegravir |
| [17977962](https://pubmed.ncbi.nlm.nih.gov/17977962/) | 2008 | In vitro / pharmacology | J Virol | Original characterization of elvitegravir (JTK-303/GS-9137) as a broad-spectrum HIV-1 integrase inhibitor and its resistance profile |

*Note: All entries above are classified by content of the abstract, since automated study-type classification for these records was not yet completed ("pending") in the source data.*

---

## Malaysia Market Information

Elvitegravir is recorded as marketed in Malaysia (1 registration), but the detailed authorization number, product name, dosage form, and approved indication text for this license were not populated in this evidence pack — this is a data gap (DG001, Blocking severity) that must be resolved via the official product label before any safety review can proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack — resolving DG001 by retrieving the official TFDA/NPRA package insert is required before proceeding.)*

---

## Other Predicted Indications (Lower Priority)

This evidence pack ranked three candidate indications for elvitegravir. For completeness:

- **Rank 2 — Feline Acquired Immunodeficiency Syndrome (FIV)**: Same TxGNN score (99.89%) as the top prediction, but with **zero** supporting clinical trials or literature. Like SIV, FIV is a veterinary/animal disease, not a human indication. Evidence Level: **L5** (model prediction only, no supporting studies). Recommendation: **Hold**.
- **Rank 3 — Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter**: A rare genetic neurodevelopmental disorder with no plausible mechanistic link to elvitegravir's antiretroviral activity, and no supporting trials or literature. The evidence pack itself flags this as a likely **spurious statistical association** from the knowledge graph embedding space. Evidence Level: **L5**. Recommendation: **Hold**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) and the second-ranked prediction (FIV) are both animal/veterinary diseases rather than human clinical indications — the underlying literature confirms elvitegravir's known antiretroviral mechanism is being studied in these species as *models* for HIV-1 research, not as a new disease to treat in patients. Combined with the absence of any clinical trials, a Blocking data gap on TFDA/NPRA safety labeling (DG001), and a High-severity gap on confirmed mechanism of action (DG002), there is currently no actionable human repurposing opportunity to advance.

**To proceed, the following is needed:**
- Retrieve the official Malaysia (NPRA) package insert to resolve DG001 (warnings/contraindications) before any S1 safety screening can occur
- Confirm elvitegravir's mechanism of action and original approved indication via DrugBank/regulatory sources to resolve DG002
- Obtain complete Malaysia license details (authorization number, product name, dosage form, approved indication text)
- If pursuing this lead further, clarify with a subject-matter expert whether the SIV/FIV associations have any translatable human application (e.g., informing HIV pre-exposure prophylaxis or microbicide research) — otherwise these should be deprioritized as non-human artifacts of the knowledge graph
- No further action needed on the Rank 3 (neurodevelopmental disorder) prediction absent new mechanistic evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

