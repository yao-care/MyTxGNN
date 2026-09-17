---
layout: default
title: Ritonavir
parent: Low Evidence (L4-L5)
nav_order: 598
evidence_level: L4
indication_count: 3
---

# Ritonavir
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **3** 
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

# Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Ritonavir is a well-established HIV-1 protease inhibitor, most often used today as a pharmacokinetic booster in combination antiretroviral regimens. TxGNN's top-ranked prediction — **feline acquired immunodeficiency syndrome (FIV)** — appears to be a disease-ontology string-matching artifact ("...immunodeficiency syndrome") rather than a genuine mechanistic signal, and its only linked clinical trial is unrelated (human HIV-1 patients, not cats). None of the three candidates in this evidence pack currently support moving forward.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (TFDA label pending — see Data Gap DG001) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (MOA field flagged as a High-severity data gap). Based on the supporting evidence in this pack, ritonavir is known as an HIV-1 protease inhibitor and CYP3A4 inhibitor; its efficacy in HIV-1 infection is well established, and mechanistically a related lentiviral protease target (feline immunodeficiency virus, FIV) could in principle be plausible.

However, the evidence attached to this specific prediction does not support that link. The single linked clinical trial (NCT02770508) enrolled human HIV-1 patients on a boosted darunavir/lamivudine regimen — it has no connection to feline disease. The rationale notes explicitly that FIV and HIV-1 proteases are not structurally homologous, and there is no direct evidence that ritonavir inhibits FIV protease. This strongly suggests the prediction is driven by disease-label string overlap ("acquired immunodeficiency syndrome") in the knowledge graph rather than a real biological signal.

A more mechanistically coherent (but still not human-relevant) candidate exists at rank 2: **simian immunodeficiency virus (SIV) infection**, where in vitro and animal-model literature confirms ritonavir has cross-reactive protease-inhibitory activity against SIV, consistent with its known HIV-1 mechanism. This is a re-confirmation of an already-known pharmacological effect in a non-human primate infection model, not a new human indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared ritonavir-boosted darunavir + lamivudine vs. boosted darunavir + FTC/TDF or 3TC/TDF in treatment-naïve **human** HIV-1 patients. Not relevant to feline disease — flagged as a likely disease-mapping artifact rather than supporting evidence. |

## Literature Evidence

Currently no related literature available for this indication.

## Additional Predicted Indications (Context, Not Primary)

Two lower-priority TxGNN candidates were also returned and are worth noting for completeness, though both are also recommended **Hold**:

- **Simian immunodeficiency virus infection** (rank 2, score 99.92%, L3/S1): 12 PubMed records support ritonavir's known cross-reactive anti-protease activity against SIV in vitro and in macaque ART-combination models. This confirms existing pharmacology in an animal infection model — it is not a novel human indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (rank 3, score 99.92%, L5/S0): a rare genetic white-matter disorder with no clinical, literature, or mechanistic link to ritonavir's known pharmacology — pure embedding-similarity output.

## Malaysia Market Information

Ritonavir is registered in Malaysia with 12 active licenses (market status: ✓ Marketed), but individual license details (product name, dosage form, approved indication text) are not populated in the current dataset. This needs to be sourced from NPRA product listings before market-context claims can be made.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings, contraindications, and drug interaction data are currently missing from this evidence pack — see Data Gap DG001, which is flagged as Blocking.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (feline AIDS) is most likely a disease-ontology mismatch, not a genuine repurposing signal, and its only clinical trial evidence is irrelevant.
- The mechanistically credible candidate (SIV infection) only reconfirms ritonavir's known antiretroviral activity in a non-human animal model — it is not a new human indication.
- Data Gap DG001 (TFDA label warnings/contraindications) is Blocking and prevents any Stage 1 safety evaluation regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the TFDA/NPRA package insert for warnings, contraindications, and DDI data
- Resolve DG002: confirm ritonavir's MOA and CYP3A4 interaction profile via DrugBank
- Correct the underlying disease-ontology mapping for "feline acquired immunodeficiency syndrome" in the TxGNN pipeline to prevent recurrence of this artifact
- If pursuing any lentivirus-related angle, reassess against a genuine human indication rather than an animal infection model
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

