---
layout: default
title: Zidovudine
parent: Low Evidence (L4-L5)
nav_order: 695
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **6** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Zidovudine: From HIV/AIDS to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Zidovudine (AZT, DB00495) is the first antiretroviral nucleoside reverse transcriptase inhibitor (NRTI) approved for HIV-1 infection.
The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, a lentiviral disease of non-human primates, not a human indication.
This "prediction" is supported only by **20 preclinical/animal-model publications** and **zero human clinical trials**, indicating it reflects the drug's known antiretroviral mechanism rather than a genuine new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — well-established global indication; Malaysia-specific license indication text was not captured in this evidence pack (all sampled license fields are blank) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection — a veterinary/animal-model disease, not a human clinical indication |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical/animal-model studies only; no clinical trials) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, zidovudine is a thymidine-analogue NRTI that is phosphorylated intracellularly and incorporated into viral DNA by reverse transcriptase, causing chain termination — the mechanism underlying its approved use against HIV-1.

SIV is a lentivirus closely related to HIV that infects non-human primates and shares a homologous reverse transcriptase target, which is why zidovudine shows *in vitro* and *in vivo* antiviral activity in macaque models. However, this mechanistic overlap does not translate into a human "new indication": SIV infection is a disease of monkeys, used exclusively as a preclinical research model to study antiretroviral prophylaxis and pathogenesis, not a condition that occurs in humans.

The evidence pack's own repurposing rationale states this explicitly: *"SIV is a primate lentivirus, mechanistically related to HIV via shared reverse-transcriptase inhibition, but SIV infection is a non-human primate disease model, not a human clinical indication — it is used only to validate AZT's antiviral mechanism and pharmacological extrapolation to HIV/AIDS."* In other words, the TxGNN score here is a high-confidence signal of **mechanistic similarity**, not of **clinical repurposing opportunity**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (this candidate has no human trial data — all supporting evidence is from non-human primate models).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1489181](https://pubmed.ncbi.nlm.nih.gov/1489181/) | 1992 | Animal Model | Antimicrob Agents Chemother | Oral AZT prevented SIV infection in infant rhesus macaques when given prophylactically |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal Model | AIDS | Post-exposure prophylaxis with zidovudine + lamivudine + indinavir prevented vaginal SIV transmission in macaques |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | Animal Model | AIDS Res Hum Retroviruses | AZT altered kinetics of viral load and CD4/CD8 changes during acute SIV infection in macaques |
| [22713337](https://pubmed.ncbi.nlm.nih.gov/22713337/) | 2012 | Animal Model | Antimicrob Agents Chemother | Comparison of a novel NRTI vs. AZT-class agents against SIV in vitro and in vivo |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Animal Model | J Virol | Bone marrow hematopoiesis defects persisted in SHIV-infected macaques despite HAART (incl. AZT) viral suppression |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | Animal Model | Antimicrob Agents Chemother | Immediate AZT treatment protected SIV-infected newborn macaques from rapid-onset AIDS |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | Animal Model | J Infect Dis | AZT prolonged survival and reduced CNS viral load in perinatally SIV-infected rhesus macaques |
| [8101673](https://pubmed.ncbi.nlm.nih.gov/8101673/) | 1993 | Animal Model | Virology | Characterized acute HIV-1 infection susceptibility in pigtail macaques (SIV-related model) |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Model | J Virol | Quadruple antiretroviral therapy (incl. AZT) produced rapid viral decay in SIV-infected macaques |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | Animal Model (resistance) | Antimicrob Agents Chemother | An AZT-resistant SIV mutant (Q151M in reverse transcriptase) still caused AIDS in newborn macaques |

*Note: All 20 available publications for this candidate are animal-model or in vitro studies; none are human RCTs, reviews, or case reports.*

---

## Malaysia Market Information

Zidovudine has 9 registered licenses in the Malaysia (NPRA) market status database, but the detailed license fields (license number, product name, dosage form, manufacturer, approved indication text) were not populated in this evidence pack — all sampled entries are blank. This is a data gap that should be remediated by pulling the NPRA product register directly before any regulatory decision is finalized.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack (flagged as a **Blocking** data gap, DG001 — TFDA/NPRA label warnings and contraindications must be sourced before this candidate can enter safety review, S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (SIV infection) is not a human disease and cannot be pursued as a repurposing candidate — it reflects mechanistic similarity between HIV and SIV reverse transcriptase, not a clinical opportunity. More broadly, across all 6 predictions in this evidence pack, none represent an actionable, novel human indication: two (rank 3–4: neurodevelopmental disorder, obsolete hyperlipidemia term) have zero supporting evidence and are likely algorithmic noise; two (rank 1–2: SIV, FIV/FeLV) are veterinary disease models; and the two with strong human clinical evidence (rank 5: AIDS-related complex; rank 6: congenital/perinatal HIV transmission) are not true "repurposing" — they fall within zidovudine's already-approved HIV/AIDS label (e.g., the PACTG 076 mother-to-child transmission regimen).

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain TFDA/NPRA label warnings and contraindications
- Resolve High-severity data gap DG002: obtain confirmed MOA data from DrugBank API
- Complete Malaysia (NPRA) license records (license numbers, product names, approved indication text) for the 9 registered products
- If continuing this repurposing pipeline for zidovudine, re-screen the candidate list to exclude non-human disease terms and diseases already within the approved label, so any remaining candidates represent genuine novel human indications
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

