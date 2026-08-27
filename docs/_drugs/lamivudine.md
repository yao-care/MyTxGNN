---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 5
---

# Lamivudine
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

# Lamivudine: From an Undocumented Original Indication to HIV Infectious Disease

## One-Sentence Summary

Lamivudine (3TC, DrugBank DB00709) is a cytidine-analogue reverse transcriptase inhibitor; the Malaysia NPRA license records in this evidence pack do not contain a usable original-indication text (data gap), so its true labeled use cannot be quoted directly from this dataset. The TxGNN model's top prediction — **HIV infectious disease** — is supported by **50 clinical trials** and **20 publications**, but the evidence itself indicates this is very likely Lamivudine's own long-standing, already-approved antiretroviral indication rather than a genuinely novel repurposing signal (see caveat below). A second, equally well-supported signal, chronic hepatitis B virus infection, points to the same pattern.

> **Important caveat:** The evidence pack's own rationale field states that both "HIV infectious disease" and "chronic hepatitis B virus infection" are Lamivudine's already-approved historical indications (Epivir® for HIV; Epivir-HBV® / Zeffix® for HBV), and that the empty `original_indications` field should be read as a data gap, not as evidence these are new uses. Ranks 3–5 in the underlying prediction set are near-duplicates of ranks 1–2 (AIDS is a clinical stage of HIV infection, and ranks 4–5 repeat ranks 1–2), consistent with a data-pipeline artifact rather than five independent signals. This report should be read as a **data-completeness / confirmatory** case, not a discovery case.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current NPRA license extract (data gap — DG001/DG002). Per the evidence pack's own mechanistic notes, Lamivudine's actual approved uses are HIV-1 infection and chronic hepatitis B. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.00% (as recorded in the evidence pack — see note below) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 30 |
| Recommended Decision | Proceed with Guardrails |

*Note on the score:* the evidence pack records a TxGNN score of 0.0 for every ranked indication, which is atypical for a top-ranked candidate and may itself be an artifact of the same data gap affecting `original_indications`. This should be verified against the raw model output before the score is used in any downstream ranking.

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available in the DrugBank field of this evidence pack ([Data Gap] / DG002). However, the repurposing rationale attached to each ranked candidate does describe the mechanism: Lamivudine (3TC) is a cytidine nucleoside analogue that, after intracellular phosphorylation to lamivudine triphosphate, competitively inhibits HIV-1 reverse transcriptase and is incorporated into the growing viral DNA chain, causing chain termination. The same triphosphate also inhibits HBV DNA polymerase (which has reverse-transcriptase activity), blocking reverse transcription of the HBV pregenomic RNA.

Both of these are described in the source data as Lamivudine's **existing, already-approved indications** (HIV-1 infection as an NRTI backbone agent, and chronic hepatitis B under the Epivir-HBV/Zeffix brand names), not as newly discovered pharmacology. AIDS (rank 3) is simply the advanced clinical stage of HIV infection rather than a distinct disease entity, and it draws on the same evidence base as rank 1.

Given this, the "prediction" is best interpreted as the model re-deriving a well-established use from the knowledge graph, most plausibly because the `original_indications` field was empty when the model ran (a data-entry gap rather than a true absence of indication). The clinical and literature evidence below is therefore extremely mature — trials span nearly three decades (1996–2028) — which is itself consistent with an established indication rather than an emerging one.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00038506](https://clinicaltrials.gov/study/NCT00038506) | Phase 4 | Completed | 100 | Open-label study of TRIZIVIR (abacavir/lamivudine/zidovudine) plus tenofovir intensification in HIV patients with early virologic failure |
| [NCT00053638](https://clinicaltrials.gov/study/NCT00053638) | Phase 3 | Completed | 345 | Efavirenz vs. tenofovir, each added to fixed-dose abacavir/lamivudine, in antiretroviral-naive HIV-1 patients |
| [NCT03205566](https://clinicaltrials.gov/study/NCT03205566) | Phase 4 | Completed | 38 | Raltegravir with or without lamivudine for protection against genital-tissue HIV infection; PK/PD decay profiling |
| [NCT01449929](https://clinicaltrials.gov/study/NCT01449929) | Phase 3 | Completed | 488 | Dolutegravir vs. darunavir/ritonavir, each with dual NRTI backbone (abacavir/lamivudine or tenofovir/emtricitabine), over 96 weeks in ART-naive adults |
| [NCT00197613](https://clinicaltrials.gov/study/NCT00197613) | Phase 3 | Completed | 650 | Tshepo Study — first large-scale antiretroviral resistance and treatment-outcome study in Botswana |
| [NCT00001083](https://clinicaltrials.gov/study/NCT00001083) | Phase 2 | Completed | 240 | PRAM-1: zidovudine+lamivudine vs. stavudine+ritonavir vs. triple combination in antiretroviral-experienced HIV-infected children |
| [NCT00002411](https://clinicaltrials.gov/study/NCT00002411) | N/A | Completed | N/A | Long-term suppression of plasma HIV RNA by triple-combination regimens (including zidovudine+lamivudine+nelfinavir) in treatment-naive subjects |
| [NCT00000887](https://clinicaltrials.gov/study/NCT00000887) | Phase 1 | Completed | 24 | Safety/PK of nelfinavir + zidovudine + lamivudine in HIV-infected pregnant women and infants |
| [NCT00000865](https://clinicaltrials.gov/study/NCT00000865) | Phase 1 | Completed | 32 | Steady-state PK, tolerance and safety of 1592U89 (abacavir) alone or with other antiretrovirals, including lamivudine-containing regimens, in HIV-infected children |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32504574](https://pubmed.ncbi.nlm.nih.gov/32504574/) | 2020 | RCT | The Lancet HIV | Week-144 results: bictegravir/emtricitabine/TAF non-inferior to dolutegravir-containing regimens in treatment-naive HIV patients |
| [39826566](https://pubmed.ncbi.nlm.nih.gov/39826566/) | 2025 | RCT | The Lancet HIV | D2ARLING trial: dolutegravir + lamivudine efficacy in treatment-naive HIV patients without baseline resistance testing |
| [40874763](https://pubmed.ncbi.nlm.nih.gov/40874763/) | 2026 | RCT | Clinical Infectious Diseases | DOLCE study: dolutegravir/lamivudine dual therapy in treatment-naive patients with CD4 <200/mm³ |
| [36094514](https://pubmed.ncbi.nlm.nih.gov/36094514/) | 2022 | RCT | J Acquir Immune Defic Syndr | Multicenter China cohort confirming virological efficacy and safety of simplified lamivudine + dolutegravir dual therapy |
| [29474268](https://pubmed.ncbi.nlm.nih.gov/29474268/) | 2018 | Review | J Acquir Immune Defic Syndr | 25-year retrospective on lamivudine's role and continued relevance in HIV-1 treatment |
| [24754315](https://pubmed.ncbi.nlm.nih.gov/24754315/) | 2014 | Review | Expert Opin Pharmacother | Review of dolutegravir/abacavir/lamivudine single-tablet regimen properties |
| [37832567](https://pubmed.ncbi.nlm.nih.gov/37832567/) | 2023 | Cohort | The Lancet HIV | DTG RESIST collaborative cohort analysis of resistance mutation patterns under dolutegravir-based ART |
| [31503008](https://pubmed.ncbi.nlm.nih.gov/31503008/) | 2019 | Cohort | Antiviral Therapy | Systematic review of pretreatment/acquired resistance mutations to lamivudine or rilpivirine |
| [11996639](https://pubmed.ncbi.nlm.nih.gov/11996639/) | 2002 | Review | Expert Opin Pharmacother | Overview of Trizivir (zidovudine/lamivudine/abacavir) combination tablet |
| [26517111](https://pubmed.ncbi.nlm.nih.gov/26517111/) | 2015 | Review | Expert Rev Clin Pharmacol | Review of Dutrebis (lamivudine/raltegravir) fixed-dose combination for HIV-1 treatment |

## Malaysia Market Information

The evidence pack reports **30 total NPRA registrations** with market status "Marketed," but the five license records included in this export contain no populated fields (license number, product name, dosage form, manufacturer, and indication text are all blank). This is a data-completeness gap in the current extract, not evidence of an empty registry — the aggregate count (30) confirms an active market presence, but individual license details need to be re-pulled from the NPRA source before they can be reported.

## Safety Considerations

Please refer to the package insert for safety information.

*Flag for reviewers:* the underlying evidence pack marks the missing TFDA/NPRA package-insert warnings and contraindications (DG001) as a **Blocking** severity data gap, explicitly noted as preventing entry into the S1 safety pre-assessment stage. This should be resolved before this candidate advances past the current stage, regardless of the clinical/literature evidence strength above.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical trial and literature base for lamivudine in HIV infection is extensive and mature (L1), but the evidence pack's own rationale indicates this is very likely a re-identification of Lamivudine's known, already-approved antiretroviral indication rather than a novel repurposing discovery — the "original indication" gap in the source data should be closed before this is treated as a genuine repurposing candidate. Separately, a Blocking-severity safety data gap (TFDA/NPRA warnings and contraindications) means the S1 safety pre-assessment cannot yet be completed.

**To proceed, the following is needed:**
- Resolve DG001: retrieve and parse the TFDA/NPRA package insert (warnings, contraindications) — currently blocking safety pre-assessment
- Resolve DG002: obtain a structured mechanism-of-action record from DrugBank
- Re-pull the NPRA license records with populated fields (license number, product name, dosage form, manufacturer, indication text) — the current five entries are empty
- Confirm whether `original_indications` was genuinely empty at prediction time, or whether this is a data-pipeline defect that caused known indications (HIV, HBV) to be surfaced as "predictions"
- De-duplicate the prediction set — ranks 1/4 (HIV) and ranks 2/5 (HBV) appear to be repeats, and rank 3 (AIDS) overlaps with rank 1; clarify whether this reflects five independent model outputs or a pipeline artifact before using rank counts in scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

