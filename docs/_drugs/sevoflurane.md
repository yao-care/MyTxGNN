---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 613
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Sevoflurane is a volatile inhalational general anesthetic; the specific Malaysia-approved indication wording is not available in the current dataset. The TxGNN model's top-ranked prediction is **Prinzmetal angina**, but this direction is supported by **no clinical trials and no literature** — and the only mechanistic commentary available argues the opposite (case reports describe sevoflurane *triggering or worsening* coronary spasm, not treating it).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (induction/maintenance) — specific NPRA-approved indication text not available in dataset |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sevoflurane is not available in this evidence pack (flagged as a High-severity data gap). Sevoflurane is broadly known as a halogenated ether inhalational anesthetic acting via GABA-A potentiation and NMDA receptor antagonism to produce central nervous system depression — a pharmacology unrelated to coronary vasospasm, which is the underlying pathophysiology of Prinzmetal angina.

There is no mechanistic bridge between general anesthesia and Prinzmetal angina in the supplied rationale. On the contrary, the evidence annotation explicitly notes case reports of sevoflurane-associated coronary spasm — i.e., the drug may move risk in the direction opposite to therapeutic benefit for this condition. No clinical trials, ICTRP records, or PubMed literature were found linking sevoflurane to Prinzmetal angina; the prediction rests solely on TxGNN graph-similarity scoring (L5), with no corroborating clinical signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Sevoflurane holds **6 active NPRA registrations** (market status: Marketed). License-level detail (authorization numbers, product names, dosage forms, approved indication text) is not populated in the current dataset and cannot be tabulated at this time.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/NPRA label warnings and contraindications for sevoflurane are currently marked as a **Blocking** data gap — this alone prevents a preliminary (S1) safety assessment for any repurposing candidate for this drug, independent of efficacy evidence.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prinzmetal angina) has no clinical or literature support, and the available mechanistic commentary suggests sevoflurane may exacerbate rather than treat coronary vasospasm. Combined with a blocking gap in label-level safety data, there is currently no basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications) — required before any S1 safety screening
- DrugBank mechanism-of-action data to properly assess mechanistic plausibility
- License-level Malaysia registration detail (product names, approved indication text)
- Note: other TxGNN candidates for this drug (e.g., migraine disorder, tendinitis, fibromyalgia) also lack direct treatment evidence — the associated trials/literature address sevoflurane's use *during* anesthesia for patients with these conditions, not its use *to treat* them. None currently meet criteria to advance beyond Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

