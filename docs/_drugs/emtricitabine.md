---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) originally developed for HIV-1 antiretroviral therapy in humans. The TxGNN model's top prediction points to **Feline Acquired Immunodeficiency Syndrome (FIV, "feline AIDS")** with a **99.92% prediction score**, but the supporting clinical-trial evidence in this pack is actually drawn from human HIV-1 trials, not feline studies — only **1 publication** directly addresses the feline indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — TFDA/NPRA license text not available in this evidence pack |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (the 2 completed Phase 3 RCTs in this pack are for the *original* human HIV-1 indication, not FIV; direct feline evidence is limited to one preclinical/animal study) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this compound in the current evidence pack (flagged as a High-severity data gap). Based on known pharmacology, Emtricitabine is a cytidine-analog NRTI that terminates reverse-transcriptase-mediated viral DNA synthesis — the same mechanism class used to treat HIV-1 infection in humans.

The predicted new indication, feline AIDS, is caused by Feline Immunodeficiency Virus (FIV) — a lentivirus in the same *Retroviridae* family as HIV, also dependent on reverse transcriptase for replication. This shared enzymatic target is the most plausible mechanistic bridge for the TxGNN prediction: the model likely picked up on structural/functional similarity between the HIV and FIV disease nodes in the knowledge graph, given both diseases already share the same drug-class treatment paradigm.

Importantly, this is a **cross-species** repurposing signal (human drug → veterinary indication), not a new human indication. The clinical trial evidence attached to this prediction in the pack (dolutegravir vs. raltegravir, darunavir combination regimens, etc.) are all human HIV-1 studies that establish emtricitabine's *existing* antiretroviral use — they do not directly support efficacy in cats. The one study that does address FIV directly (Kim et al. 2023) is a small pharmacokinetic/immunophenotyping study in specific-pathogen-free cats, not a controlled efficacy trial.

---

## Clinical Trial Evidence

*(Evidence attached to this prediction pertains to emtricitabine's established human HIV-1 use, not to feline FIV specifically — included here as provided in the evidence pack.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir 50mg QD vs. raltegravir 400mg BID, both with dual NRTI (incl. FTC/TDF), in ART-naive HIV-1 adults |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla (efavirenz/emtricitabine/tenofovir) in ART-naive HIV-1 adults |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of dolutegravir with abacavir/lamivudine or tenofovir/emtricitabine in ART-naive HIV-1 adults |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs. darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in naive HIV-1 patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal/Preclinical Study | Viruses | Combination ART (dolutegravir, tenofovir, emtricitabine) evaluated for pharmacokinetics and immunophenotype outcomes in FIV-infected domestic cats; no definitive therapy currently exists for FIV |

---

## Malaysia Market Information

Detailed authorization data (license numbers, product names, dosage forms, approved indication text) is not available in this evidence pack — all license entries returned empty fields despite the registry reporting 12 total licenses. Market status is confirmed as "已上市" (Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings and contraindications for this drug are flagged as a Blocking-severity data gap — DG001 — meaning this evidence pack cannot currently support a safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Safety data (warnings, contraindications, DDI) has a Blocking-severity data gap, which by definition prevents entry into initial safety review (S1).
- The predicted indication is a veterinary condition (feline AIDS); the clinical trial evidence in this pack actually supports emtricitabine's *existing* human HIV-1 use rather than the predicted new indication, and only one small preclinical/animal study directly addresses FIV.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications, DDI) to clear the blocking safety data gap (DG001)
- DrugBank MOA detail to confirm mechanistic linkage (DG002)
- Clarification of scope: confirm whether a veterinary indication (FIV) is a valid target for this human-drug regulatory review, or should be excluded/routed to veterinary pharmacology channels
- Complete Malaysia license/authorization detail (currently blank despite 12 registered licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

