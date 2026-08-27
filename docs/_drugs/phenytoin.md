---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Phenytoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is a classic sodium-channel-blocking antiepileptic drug; the specific NPRA-approved indication text was not returned in this data pull. The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm** (score 99.99%), but the only supporting literature (**5 publications, 0 clinical trials**) discusses trigeminal *neuralgia* and Sturge-Weber syndrome rather than nerve tumors — the evidence pack itself flags this as a likely disease-ontology mapping error and recommends manual review before proceeding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available NPRA license extract (all license fields blank); Phenytoin is globally established as an antiepileptic/anticonvulsant agent |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned a blocking gap on this field). Based on generally established pharmacology, phenytoin is a voltage-gated sodium channel blocker classically used to suppress abnormal, high-frequency neuronal firing in epilepsy; this same mechanism underlies its long-standing off-label use in neuropathic pain syndromes involving neuronal hyperexcitability.

However, the specific rank-1 prediction — trigeminal nerve **neoplasm** — is not well supported by the retrieved evidence. All five associated publications concern trigeminal **neuralgia** (a pain/hyperexcitability disorder) or Sturge-Weber syndrome case reports, none of which describe nerve tumors. This mismatch strongly suggests a TxGNN disease-ontology mapping artifact (neuralgia mislabeled as neoplasm) rather than a genuine mechanistic signal for an oncologic indication, and it should be manually reconciled before any further evaluation.

Notably, this same evidence pack separately lists **trigeminal neuralgia** (rank 10, TxGNN score 99.97%) as a distinct predicted indication with markedly stronger support: a completed prospective clinical trial (NCT03712254) and an EAN clinical practice guideline. Sodium-channel blockade is the accepted therapeutic mechanism for trigeminal neuralgia (shared with carbamazepine), making that candidate mechanistically coherent in a way the neoplasm label is not.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for "trigeminal nerve neoplasm."

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurotherapeutics | Overview of trigeminal neuralgia treatments (medical and surgical); likely vascular compression etiology — concerns neuralgia, not neoplasm |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Review/Case report | J Assoc Physicians India | Sturge-Weber syndrome case with facial/orbital vascular malformation and seizures |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales Españoles de Pediatría | 14-case series of Sturge-Weber syndrome, clinical course and treatment response |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Not classified | Birth Defects Orig Article Series | Review of dermatologic disorders in institutionalized patients; only tangentially related |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Not classified | Trans Am Neurol Assoc | Fiber-size/conduction study relating to trigeminal root pain treatment; no abstract available |

None of these publications address trigeminal nerve neoplasm specifically.

---

## Malaysia Market Information

The regulatory extract indicates 5 active product registrations (`total_licenses = 5`) with market status **已上市 (Marketed)**, but individual license details — authorization numbers, product names, dosage forms, and approved indication text — were not returned in this data pull and cannot be reported here.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI queries all returned no data in this evidence pack — DG001 is flagged as a Blocking gap for safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction (trigeminal nerve neoplasm) has no clinical trial support and its literature base appears to reflect a disease-ontology mapping error rather than genuine evidence (L5/S0). Core inputs needed for even an initial safety screen — TFDA/NPRA package insert warnings (DG001, Blocking) and MOA data (DG002) — are also missing.

**To proceed, the following is needed:**
- Manual reconciliation of the "trigeminal nerve neoplasm" vs. "trigeminal neuralgia" disease-ontology mapping before re-scoring this candidate
- Retrieval of the TFDA/NPRA package insert (warnings, contraindications) — currently blocking
- Retrieval of DrugBank MOA and drug category data
- Retrieval of actual NPRA license register details (product names, dosage forms, approved indication text)
- Consider evaluating **trigeminal neuralgia** (rank 10 in this same pack, L3/S2, "Proceed with Guardrails," backed by a completed clinical trial and an EAN guideline) as the more substantively supported repurposing candidate for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

