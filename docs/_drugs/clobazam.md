---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: From Epilepsy to Febrile Infection-Related Epilepsy Syndrome (FIRES)

## One-Sentence Summary

> Clobazam is a benzodiazepine originally used as an adjunctive anticonvulsant for epilepsy.
> The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**,
> but currently **0 clinical trials** and **0 publications** directly support this specific direction — the prediction rests on the computational model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (adjunctive therapy) — general drug knowledge; not confirmed by the data pack, as `original_indications` and the NPRA license indication text are both empty |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, DrugBank MOA field returned no data). Based on general pharmacological knowledge, clobazam is a 1,5-benzodiazepine that acts as a GABA-A receptor positive allosteric modulator, and its efficacy as an adjunctive antiepileptic (e.g., in Lennox-Gastaut syndrome) is well established. This class-level mechanism has not been independently verified for this candidate in the current evidence pack.

FIRES is a rare, severe epileptic encephalopathy that follows a febrile illness and presents as new-onset super-refractory status epilepticus, driven by excessive cortical excitatory-inhibitory imbalance. Benzodiazepines, including clobazam, are mechanistically positioned to dampen this excitability via GABAergic potentiation, which is consistent with why the TxGNN model links a GABA-A modulating anticonvulsant to a refractory seizure syndrome.

That said, this mechanistic plausibility is theoretical. No clinical trial or literature record in this evidence pack — nor in the underlying query log (0 results across ClinicalTrials.gov, ICTRP, and PubMed for the clobazam + FIRES search) — provides direct support. The prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Clobazam is confirmed as marketed in Malaysia under NPRA, with 1 active registration. Detailed license information (registration number, product name, dosage form, and approved indication text) was not returned by the data source and is unavailable in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data were not available from the queried sources — this is flagged as a Blocking data gap (DG001) that currently prevents safety screening for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but it is unsupported by any clinical trial or literature evidence (Evidence Level L5), and a Blocking data gap in safety labeling (DG001) means this candidate cannot yet pass an initial safety screen.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) to resolve DG001
- Confirmed mechanism of action from DrugBank to resolve DG002
- Broader literature/trial search using related terms (e.g., "super-refractory status epilepticus," "benzodiazepine + FIRES") given FIRES is a rare syndrome that may not be indexed under its exact name
- Original indication and Malaysia license detail confirmation, currently missing from both `drug.original_indications` and `taiwan_regulatory.licenses`
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

