---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Delamanid: From Multidrug-Resistant Tuberculosis to Tuberculosis, Bovine (Zoonotic *M. bovis* Infection)

## One-Sentence Summary

Delamanid is a nitro-dihydro-imidazooxazole antimycobacterial, publicly known for treating pulmonary multidrug-resistant tuberculosis (MDR-TB) in combination regimens — though this specific detail is not present in the current Malaysia (NPRA) license record. The TxGNN model predicts it may also be effective for **Tuberculosis, Bovine** (zoonotic infection caused by *Mycobacterium bovis*), with a very high model score but **no direct clinical trials and only one indirectly related publication** currently supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the current Malaysia (NPRA) license data (license text is blank); publicly known indication is pulmonary MDR-TB as part of combination therapy |
| Predicted New Indication | Tuberculosis, Bovine |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on publicly known pharmacology, Delamanid belongs to the nitro-imidazooxazole class and acts by inhibiting mycolic acid biosynthesis in the mycobacterial cell wall — the mechanism underlying its efficacy against *Mycobacterium tuberculosis* in MDR pulmonary TB.

*Mycobacterium bovis*, the causative organism of bovine tuberculosis, belongs to the same *M. tuberculosis* complex and shares the cell-wall biology that delamanid targets. Zoonotic infection of humans by *M. bovis* is clinically and pathologically similar to conventional human TB, so mechanistic extension of an anti-mycobacterial drug to this pathogen is biologically plausible.

This plausibility is reinforced by the broader prediction pattern: four of the top five TxGNN-ranked indications for delamanid (bovine TB, avian TB, tuberculoma, inactive TB) are all mycobacterial-disease manifestations, suggesting the model has correctly captured delamanid's core antimycobacterial mechanism rather than producing an isolated artifact. By contrast, the rank-6 prediction ("allergic urticaria") is supported only by an unrelated case report about a different drug (piperacillin-tazobactam) and should be treated as model noise, not a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Delamanid in Tuberculosis, Bovine.

*(Note: two ongoing Phase 2/3 trials of delamanid — [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) and [NCT03568383](https://clinicaltrials.gov/study/NCT03568383) — exist under the separate "inactive tuberculosis" prediction and may offer an alternative, more evidence-rich pathway for this drug within the TB disease cluster.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Genomic/epidemiological study | BMC Genomics | Whole-genome sequencing of zoonotic human TB caused by *M. bovis*, characterizing circulating genotypes and genomic drivers of virulence and drug resistance. Provides pathogen-level context but does not directly study delamanid. |

---

## Cytotoxicity

Not applicable — Delamanid is an antimycobacterial agent, not an antineoplastic/cytotoxic drug. This section is omitted.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings, contraindications, and drug-interaction data could not be retrieved and are flagged as a Blocking data gap — this must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The specific prediction (tuberculosis, bovine) has no direct clinical trial evidence and only one indirectly related publication that does not study delamanid itself.
- A Blocking data gap exists: no package-insert warnings, contraindications, or drug-interaction data are available, which prevents any preliminary safety assessment (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- Malaysia (NPRA) product label text — warnings, contraindications, dosage form, and approved indication (currently blank in the license record)
- DrugBank-sourced mechanism of action data
- Dedicated clinical or preclinical studies evaluating delamanid specifically against *M. bovis*/zoonotic TB, or a decision to instead prioritize the "inactive tuberculosis" prediction, which already has two active Phase 2/3 trials directly testing delamanid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

