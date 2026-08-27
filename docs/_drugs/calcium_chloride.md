---
layout: default
title: Calcium Chloride
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 5
---

# Calcium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Calcium Chloride: From Electrolyte/Emergency Therapy to Hypercalcemia — A Contradictory Signal

## One-Sentence Summary

Calcium Chloride is a marketed injectable electrolyte with 90 product registrations in Malaysia, but the evidence pack does not contain a validated original-indication text or mechanism-of-action data (both flagged as data gaps). The TxGNN model's top-ranked prediction is **Hypercalcemia disease** — however, this is pharmacologically implausible, since administering calcium chloride *raises* serum calcium and would be expected to worsen, not treat, hypercalcemia. Across all 5 predicted indications in this pack, none reach a "Go" level of evidence; the strongest genuine signal is for **cardiac arrest** (Rank 2), supported by a completed Phase 2 RCT (the COCA trial), though that trial showed no benefit and a possible harm signal in unselected patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text found in current Malaysia licensing data (Data Gap DG001) |
| Predicted New Indication | Hypercalcemia disease (Rank 1) — flagged as mechanistically contradictory |
| TxGNN Prediction Score | 0.00% (Note: all 5 predicted indications in this pack show a score of 0.0, which likely reflects a scoring/normalization artifact rather than true near-zero confidence) |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 90 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Calcium Chloride in this evidence pack (Data Gap DG002). Based on the clinical trial and literature evidence collected, however, the *direction* of the proposed relationship can still be evaluated — and it does not support repurposing.

Calcium Chloride is a source of ionized calcium, used clinically to *raise* serum calcium and support myocardial contractility. Hypercalcemia is, by definition, a state of *excess* serum calcium. Pharmacologically, administering calcium chloride to a patient with hypercalcemia would be expected to aggravate the condition, not treat it — calcium salts are in fact **contraindicated** in the setting of hypercalcemia. The clinical trials and literature returned by the search largely reflect this: they describe hypercalcemia as a background diagnosis, monitored adverse event, or differential-diagnosis topic (e.g., in multiple myeloma, primary hyperparathyroidism, or paricalcitol safety monitoring), rather than testing Calcium Chloride as a treatment for it.

The most plausible explanation is that the TxGNN knowledge graph captured a **co-occurrence or comorbidity association** (e.g., calcium chloride appearing in records alongside hypercalcemia as a lab abnormality or contraindication) rather than a true therapeutic relationship. This candidate should therefore be interpreted as a **potential safety signal** — reinforcing that hypercalcemia is a risk to monitor during calcium chloride therapy — rather than as a genuine drug-repurposing opportunity.

---

## Clinical Trial Evidence

Of the 26 clinical trials returned for "Calcium Chloride + hypercalcemia," none directly test Calcium Chloride as a treatment for hypercalcemia. Three trials were assessed as tangentially relevant (Grade C); the remaining ~23 (e.g., multiple myeloma chemotherapy protocols, HIV PrEP studies, thyroidectomy studies) were unrelated background trials returned via knowledge-graph association and are not reproduced here.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03772990](https://clinicaltrials.gov/study/NCT03772990) | Phase 4 | Completed | 818 | ICARUS trial: calcium administration during cardiac surgery/CPB weaning to *maintain* normal calcium — opposite clinical intent (avoiding hypocalcemia, not treating hypercalcemia) |
| [NCT06859580](https://clinicaltrials.gov/study/NCT06859580) | Phase 4 | Recruiting | 140 | Bisphosphonate (zoledronic acid) vs. placebo before parathyroidectomy for primary hyperparathyroidism-related hypercalcemia — treatment tested is a bisphosphonate, not Calcium Chloride |
| [NCT01134315](https://clinicaltrials.gov/study/NCT01134315) | N/A | Terminated | 61 | Paricalcitol safety study in pediatric CKD; hypercalcemia monitored as an adverse event, not a treatment target |

**No trials were found testing Calcium Chloride as a therapeutic intervention for hypercalcemia.**

---

## Literature Evidence

The 20 literature results are predominantly general reviews on the causes, diagnosis, and differential diagnosis of hypercalcemia. None discuss Calcium Chloride as a treatment option — consistent with the mechanistic contradiction noted above.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36282253](https://pubmed.ncbi.nlm.nih.gov/36282253/) | 2022 | Review | JAMA | Comprehensive review of hypercalcemia epidemiology, severity thresholds, and management; does not reference calcium chloride as therapy |
| [28806048](https://pubmed.ncbi.nlm.nih.gov/28806048/) | 2017 | Review | FP Essentials | Overview of calcium electrolyte disorders; treatment of hypercalcemia centers on hydration and antiresorptive agents, not calcium salts |
| [15698586](https://pubmed.ncbi.nlm.nih.gov/15698586/) | 2005 | Review | Clinica Chimica Acta | Laboratory screening approach to hyperparathyroidism-associated hypercalcemia |
| [482179](https://pubmed.ncbi.nlm.nih.gov/482179/) | 1979 | Review | Postgraduate Medicine | Causes of hypercalcemia, including drug-induced causes (vitamin D, thiazides) |
| [1763670](https://pubmed.ncbi.nlm.nih.gov/1763670/) | 1991 | Pending classification | J Bone Miner Res | Differential diagnosis of hypercalcemia (hyperparathyroidism vs. malignancy) |
| [6386333](https://pubmed.ncbi.nlm.nih.gov/6386333/) | 1984 | Pending classification | Crit Rev Clin Lab Sci | Differential laboratory diagnosis of hypercalcemia |
| [25158579](https://pubmed.ncbi.nlm.nih.gov/25158579/) | 2014 | Pending classification | Duodecim | Diagnostic workup of hypercalcemia |
| [8029686](https://pubmed.ncbi.nlm.nih.gov/8029686/) | 1994 | Pending classification | Schweiz Med Wochenschr | Pathophysiology of severe hypercalcemia |

---

## Malaysia Market Information

Calcium Chloride is confirmed as **Marketed (已上市)** in Malaysia with **90 total registrations**. However, the current data pull did not populate license-level details (authorization number, product name, dosage form, manufacturer, or approved indication text) — all fields were returned empty. Detailed registration information should be re-queried from the source registry before this is used for regulatory decision-making.

---

## Safety Considerations

Safety data for this candidate is currently incomplete. Both `key_warnings` and `contraindications` are marked as data gaps, and no drug–drug interaction records were found (`query_status: not_found`). Notably, this gap is flagged in the evidence pack as **Blocking** (DG001 — "TFDA 仿單警語/禁忌"), meaning it prevents this candidate from proceeding to the S1 safety pre-screening stage.

> Please refer to the package insert for safety information. Obtaining the official product label (warnings, contraindications, DDI) is a prerequisite before any further evaluation of this candidate.

---

## Additional Predicted Indications (Ranks 2–5)

This evidence pack includes 5 TxGNN-predicted indications for Calcium Chloride. For completeness and transparency, the other four are summarized below:

| Rank | Disease | Evidence Level | Decision Stage | Recommendation | Key Note |
|------|---------|----------------|-----------------|-----------------|----------|
| 2 | Cardiac arrest | L2 | S1 | Research Question | Genuine RCT evidence exists (COCA trial, [NCT04153435](https://clinicaltrials.gov/study/NCT04153435), n=397; [PMID 34847226](https://pubmed.ncbi.nlm.nih.gov/34847226/)), but showed **no improvement** in ROSC/survival for unselected out-of-hospital cardiac arrest, with a possible harm signal. Calcium chloride remains standard-of-care only for arrest caused by hyperkalemia, calcium-channel-blocker toxicity, or hypocalcemia — not for cardiac arrest broadly. |
| 3 | Phosphorus metabolism disease | L3 | S1 | Research Question | Mechanistically plausible (calcium salts can bind intestinal phosphate), but direct evidence is limited to one 1994 veterinary/dietary comparison study ([PMID 7871700](https://pubmed.ncbi.nlm.nih.gov/7871700/)); no human RCTs identified. |
| 4 | Potassium deficiency disease | L5 | S0 | Hold | No mechanistic link identified; zero supporting literature; clinical trials returned are unrelated (HIV, oncology, PK studies). Likely a knowledge-graph false positive. |
| 5 | Nephrocalcinosis | L5 | S0 | Hold | Literature points in the **opposite** direction — chloride/calcium loading is associated with *increased* nephrocalcinosis risk, not treatment benefit. Should be tracked as a safety signal, not a repurposing candidate. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hypercalcemia) is mechanistically contradictory — Calcium Chloride would be expected to worsen, not treat, hypercalcemia — and no clinical trial or literature evidence supports a therapeutic relationship. Combined with a **Blocking** data gap on TFDA safety labeling (warnings/contraindications unavailable), this candidate cannot proceed to S1 safety screening. Of the remaining four predictions, none reach a "Go" threshold; cardiac arrest (Rank 2) has the most substantive evidence but a completed Phase 2 RCT showed no net benefit in the general population.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- DrugBank mechanism-of-action data — currently a High-severity data gap (DG002)
- Re-verification of Malaysia license-level data (product names, dosage forms, approved indication text), all of which were empty in this pull
- If pursuing further research, reframe the cardiac-arrest signal as a **defined research question** (e.g., subgroup analysis by etiology — hyperkalemia/CCB-toxicity vs. undifferentiated arrest) rather than a general indication-expansion request
- Flag hypercalcemia and nephrocalcinosis findings internally as **pharmacovigilance/safety signals** rather than repurposing leads
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

