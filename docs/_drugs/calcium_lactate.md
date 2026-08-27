---
layout: default
title: Calcium Lactate
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 2
---

# Calcium Lactate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Calcium Lactate: From Calcium Supplementation to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium lactate (DrugBank DB13231) is a calcium salt widely used as an oral calcium/electrolyte supplement, though this evidence pack contains no documented original indication text or mechanism-of-action data. The TxGNN model assigns a very high association score to **Calcium-Alkali Syndrome** — but the supporting evidence (13 clinical trials, 1 publication) largely describes this condition as a *complication of* calcium supplementation rather than a disease that calcium lactate would be used to treat, so this should be read as a caution flag rather than a repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (calcium lactate is generally used as a calcium/electrolyte supplement) |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 36 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for calcium lactate. Based on general pharmacological knowledge, calcium lactate is an oral calcium salt used to replenish serum calcium in states of calcium deficiency; its "mechanism" is simple ionic replacement rather than a receptor- or enzyme-mediated effect.

Importantly, the predicted association here is with **Calcium-Alkali Syndrome (CAS)**, formerly known as milk-alkali syndrome. This is not a disease that calcium supplementation treats — it is a well-recognized **adverse consequence of excessive calcium (often combined with alkali or vitamin D) intake**, characterized by hypercalcemia, metabolic alkalosis, and renal impairment. The single literature citation retrieved for this pair (Kuroya et al., 2020) describes CAS as a complication arising *in patients receiving high-dose calcium supplementation* for post-thyroidectomy hypoparathyroidism, not as a condition that calcium lactate would be repurposed to treat.

This strongly suggests the TxGNN knowledge-graph edge reflects a **drug-induced adverse-event relationship** rather than a genuine therapeutic repurposing signal. Such patterns are a known risk in KG-based drug-repurposing models, where high co-occurrence between a drug and a condition it can *cause* is scored similarly to a genuine drug-disease treatment edge. This candidate should therefore be treated as a signal requiring careful clinical interpretation, not a straightforward repurposing lead.

---

## Clinical Trial Evidence

None of the 13 retrieved trials are topically specific to calcium lactate or calcium-alkali syndrome; all show `relevance.grade = "pending"` (not yet triaged) and, based on their titles/summaries, appear to be unrelated keyword matches (HIV/HBV antivirals, epilepsy, cardiac rehabilitation, dialysis anticoagulation). They are listed below for completeness, but should not be interpreted as supporting evidence until manual relevance review is completed.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02981602](https://clinicaltrials.gov/study/NCT02981602) | Phase 2 | Completed | 31 | IONIS-HBVRx safety/tolerability in chronic HBV — unrelated to CAS/calcium lactate |
| [NCT03816696](https://clinicaltrials.gov/study/NCT03816696) | Phase 1 | Completed | 16 | GSK3640254–dolutegravir PK interaction in healthy subjects — unrelated |
| [NCT01668654](https://clinicaltrials.gov/study/NCT01668654) | Phase 3 | Terminated | 4 | Retigabine/ezogabine long-term safety in pediatric seizures — unrelated |
| [NCT03984825](https://clinicaltrials.gov/study/NCT03984825) | Phase 1 | Completed | 23 | GSK3640254 effect on oral contraceptive PK — unrelated |
| [NCT04263142](https://clinicaltrials.gov/study/NCT04263142) | Phase 1 | Completed | 39 | GSK3640254 tablet vs. capsule bioavailability/food effect — unrelated |
| [NCT05393362](https://clinicaltrials.gov/study/NCT05393362) | N/A | Completed | 65 | Cardiac rehabilitation program in elderly heart failure patients — unrelated |
| [NCT04563845](https://clinicaltrials.gov/study/NCT04563845) | Phase 1 | Completed | 50 | GSK3640254 cardiac conduction (QTc) study — unrelated |
| [NCT00711009](https://clinicaltrials.gov/study/NCT00711009) | Phase 3 | Completed | 206 | Lopinavir/ritonavir-based HIV regimens comparison — unrelated |
| [NCT01839578](https://clinicaltrials.gov/study/NCT01839578) | N/A | Unknown | 30 | Regional citrate vs. heparin anticoagulation in CRRT for septic shock — tangential (citrate/calcium chelation) but not calcium lactate or CAS |
| [NCT04857892](https://clinicaltrials.gov/study/NCT04857892) | Phase 1 | Completed | 41 | GSK3640254/dolutegravir fixed-dose combination bioavailability — unrelated |

*(3 additional trials in the evidence pack were omitted for brevity; none appeared topically relevant.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31968342](https://pubmed.ncbi.nlm.nih.gov/31968342/) | 2020 | Observational study | American Journal of Nephrology | Investigated the incidence of hypercalcemia, renal impairment, and calcium-alkali syndrome in patients receiving high-dose calcium + vitamin D supplementation for hypoparathyroidism after total thyroidectomy — CAS is presented as a treatment complication, not a therapeutic target |

---

## Malaysia Market Information

Calcium lactate holds **36 active registrations** with NPRA (market status: marketed). However, the evidence pack's license-level fields (product name, dosage form, manufacturer, approved indication text) were not populated in this data pull, so a detailed per-product table cannot be presented at this time. This should be re-queried from the NPRA product database before any regulatory decision is finalized.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data were retrievable in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (calcium-alkali syndrome) is clinically implausible as a *treatment target* for calcium lactate — available literature indicates it is instead a known adverse complication of calcium supplementation. Combined with the absence of TFDA/NPRA label safety data (Blocking gap) and MOA data (High-severity gap), and the lack of any genuinely relevant clinical trial evidence, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001: obtain NPRA label warnings/contraindications for calcium lactate
- Resolve DG002: confirm mechanism of action via DrugBank
- Complete relevance triage on the 13 retrieved clinical trials to formally confirm none support this indication
- Clarify with the TxGNN/KG team whether the "calcium-alkali syndrome" edge represents an adverse-event association rather than a therapeutic one, and consider filtering such edges in future prediction runs
- If a genuine therapeutic rationale for this or the secondary candidate (primary bone dysplasia with defective bone mineralization, score 99.71%, currently no supporting trials or literature) emerges, re-evaluate with updated evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

