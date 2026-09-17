---
layout: default
title: Tenecteplase
parent: Low Evidence (L4-L5)
nav_order: 640
evidence_level: L5
indication_count: 10
---

# Tenecteplase
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Tenecteplase: From ST-Elevation Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

> Tenecteplase is a fibrin-specific thrombolytic agent with an approved indication in ST-elevation myocardial infarction (STEMI). The TxGNN model predicts it may also be effective for **Posterolateral Myocardial Infarction**, an anatomical subtype of MI, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ST-elevation myocardial infarction (STEMI) — inferred from evidence-pack rationale; not independently confirmed by registration text (see below) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tenecteplase is not yet available in this evidence pack (flagged as a High-severity data gap, DG002 — pending DrugBank API lookup). Based on the model's own repurposing rationale, tenecteplase's approved use is consistent with **STEMI**, where it acts by dissolving coronary artery thrombi (fibrinolysis).

Posterolateral myocardial infarction is not a distinct disease — it is an anatomical subtype of myocardial infarction, defined by the location of the culprit coronary lesion rather than a different pathophysiology. Mechanistically, thrombolysis should apply equally regardless of infarct territory, which is why the model's rationale describes the score as reflecting "the same mechanism as the already-approved STEMI indication, only subdivided by infarct location."

However, the rationale also cautions that this high score likely reflects the knowledge graph's general association with the broad "myocardial infarction" concept rather than independent evidence for this specific anatomical subtype — no clinical trial or publication in this pack targets posterolateral MI specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

The drug is registered in Malaysia (2 licenses, market status: Marketed), but detailed registration fields (license number, product name, dosage form, approved indication text) were not successfully extracted in this dataset and cannot be tabulated at this time.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA-equivalent label warnings and contraindications are marked as a Blocking data gap in this evidence pack (DG001) — this prevents the candidate from entering the S1 safety pre-screening stage regardless of prediction score.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (posterolateral MI) has no clinical trial or literature support — it is a model-score-only (L5) signal that likely reflects the general "myocardial infarction" cluster in the knowledge graph rather than subtype-specific evidence. Separately, the Blocking safety data gap (missing label warnings/contraindications) means the candidate cannot yet clear S1 safety review even if evidence improved.

**To proceed, the following is needed:**
- TFDA-equivalent label warnings and contraindications (DG001, Blocking — required before any safety pre-screening)
- Confirmed mechanism of action via DrugBank (DG002)
- Extraction of actual Malaysia registration details (license numbers, product names, approved indication text)
- Literature/trial search specifically targeting "posterolateral myocardial infarction" as a defined treatment population, rather than general MI/thrombolysis studies

**Note on other candidates in this pack:** among the 10 ranked predictions, *septal myocardial infarction* (rank 3, L4, decision stage S1, "Research Question") and *coronary stenosis* (rank 5, 1 completed Phase 2 trial + 12 PubMed hits, scoring not yet finalized) currently have materially more supporting evidence than the top-ranked candidate and may warrant separate, dedicated evaluation.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

