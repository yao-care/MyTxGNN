---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for treating HIV-1 infection (used as a component of combination regimens such as Atripla). The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV-related disease in cats)**, but this direction is currently supported by only **2 clinical trials (both of low direct relevance)** and **1 preclinical literature report**, and the underlying mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from trial context; NPRA-registered label text not available in current dataset) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known information, Efavirenz is an NNRTI used in combination antiretroviral therapy for HIV-1 infection — this is confirmed indirectly in the evidence pack itself, where Efavirenz appears as part of the Atripla comparator regimen (Efavirenz/Emtricitabine/Tenofovir) in HIV-1 antiretroviral-naïve trials (NCT01263015). Its core mechanism is direct inhibition of the HIV-1 reverse transcriptase (RT) enzyme.

The TxGNN model links Efavirenz to Feline Acquired Immunodeficiency Syndrome because Feline Immunodeficiency Virus (FIV) is, like HIV-1, a lentivirus that depends on reverse transcriptase for replication — a plausible knowledge-graph association based on shared viral machinery. However, the supporting literature (PMID 38031646) is a structural/biochemical comparison study specifically undertaken *because* FIV RT differs significantly in sequence and structure from HIV-1 RT, meaning human NNRTIs — including Efavirenz — generally show weak or negligible natural inhibitory activity against FIV RT. The study's purpose was to explore whether structural modification of the NNRTI class could produce FIV activity, not to demonstrate that Efavirenz itself is effective against FIV.

In addition, this predicted indication is a veterinary use case (cats), which follows a fundamentally different development and regulatory pathway than human drug repurposing. The mechanistic plausibility is therefore weak, and the two cited clinical trials are both human HIV-1 trials of unrelated drugs (dolutegravir), included only through indirect knowledge-graph association rather than direct evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of GSK1349572 (dolutegravir, an integrase inhibitor) in human HIV-1 patients; not related to Efavirenz or FIV — flagged as low relevance (Grade C), included only via therapeutic-area co-occurrence. |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | SINGLE study comparing dolutegravir + abacavir/lamivudine vs. Atripla (which contains Efavirenz) in human HIV-1 patients; confirms Efavirenz's established HIV-1 role but has no bearing on FIV — flagged as low relevance (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural comparison | Journal of Veterinary Science | Compared NNRTIs (nevirapine, efavirenz, rilpivirine) against feline and human immunodeficiency virus RT; found FIV RT differs structurally from HIV-1 RT, explaining why NNRTIs developed for HIV-1 are not effective treatments for FIV as-is — no approved FIV treatment currently exists. |

---

## Malaysia Market Information

Detailed authorization records (license number, product name, dosage form, approved indication text) are not available in the current dataset — all license entries returned blank fields. NPRA query records confirm Efavirenz has **11 registered products** with **Marketed** status in Malaysia (query date: 2026-03-27), but the underlying label text has not yet been retrieved.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are currently unavailable in this dataset — retrieval of the NPRA/TFDA product label is required before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Feline Acquired Immunodeficiency Syndrome) is supported only by preclinical/mechanistic evidence (L4) at decision stage S0, both cited clinical trials are of low direct relevance (Grade C, unrelated drug/species), and the sole literature source indicates that Efavirenz's parent drug class is *not* naturally effective against FIV reverse transcriptase. Combined with a **Blocking** data gap on TFDA/NPRA label warnings and contraindications, this candidate cannot yet proceed to a safety pre-assessment (S1).

**To proceed, the following is needed:**
- NPRA-approved product label data (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- DrugBank/mechanism-of-action detail for Efavirenz — currently a High-severity data gap (DG002)
- If this veterinary indication is pursued, structural/PK evidence on whether Efavirenz (or an analog) can be modified for FIV RT activity, plus clarification of the applicable veterinary regulatory pathway (distinct from human drug repurposing)
- Note: a related knowledge-graph prediction for Efavirenz in Simian Immunodeficiency Virus infection (rank 2, evidence level L3) shows substantially stronger literature support (16 publications, including direct in vivo efavirenz dosing in RT-SHIV-infected macaques), though that model itself represents a translational HIV research tool rather than a standalone human clinical indication — it may be a more productive research question to pursue in parallel.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

