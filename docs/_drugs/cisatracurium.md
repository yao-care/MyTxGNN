---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium: From Neuromuscular Blockade to Ten Low-Confidence TxGNN Predictions

## One-Sentence Summary

Cisatracurium (DrugBank DB00565) is a nondepolarizing neuromuscular blocking agent used as an adjunct to general anesthesia, to facilitate tracheal intubation and mechanical ventilation. TxGNN's knowledge-graph screening returned **10** candidate new indications, but evidence review found none clinically actionable: the top-scoring candidate (cauda equina syndrome) is very likely a **knowledge-graph false positive** with zero mechanism, trials, or literature support, and the only candidate with any real-world evidence — **preeclampsia** — is supported solely by studies about anesthesia management in obstetric patients, not by any disease-modifying effect of cisatracurium itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuromuscular blockade (skeletal muscle relaxation) as an adjunct to general anesthesia — enables tracheal intubation and mechanical ventilation. Taiwan/Malaysia license text was not populated in this data pull (see Malaysia Market Information below). |
| Predicted New Indication | Preeclampsia (the only candidate with supporting trials/literature; see rationale for why the top-ranked candidate is excluded) |
| TxGNN Prediction Score | 99.99% (preeclampsia, global rank 286 of all drug–disease pairs) |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

### Full TxGNN Candidate Screening Summary

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---|---|---|---|---|---|
| 1 | Cauda equina syndrome | 99.99% | L5 | S0 | Hold (likely graph noise/false positive) |
| 2 | Preeclampsia | 99.99% | L4 | S1 | Research Question |
| 3 | Obsolete neurogenic bladder (disease) | 99.99% | L5 | S0 | Hold |
| 4 | Migraine disorder | 99.98% | L5 | S0 | Hold |
| 5 | Thrombotic disease | 99.97% | L5 | S0 | Hold |
| 6 | Irritable bowel syndrome | 99.97% | L5 | S0 | Hold |
| 7 | Migraine with brainstem aura | 99.97% | L5 | S0 | Hold |
| 8 | Mild pre-eclampsia | 99.96% | L5 | S0 | Hold |
| 9 | Severe pre-eclampsia | 99.95% | L5 | S0 | Hold |
| 10 | Neurocirculatory asthenia | 99.95% | L5 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cisatracurium is not available in this data pack (DrugBank query returned a data gap, flagged High severity). Based on the evidence pack's own mechanistic annotations, cisatracurium is a peripheral, quaternary-ammonium neuromuscular blocker that acts selectively on nicotinic receptors at the skeletal-muscle neuromuscular junction, does not cross the blood–brain barrier, and is eliminated by organ-independent Hofmann elimination rather than hepatic/renal metabolism.

This mechanism explains why **8 of the 10 predictions are not biologically plausible**: cauda equina syndrome, obsolete neurogenic bladder, migraine (both variants), irritable bowel syndrome, thrombotic disease, and neurocirculatory asthenia all require either central nervous system penetration, disease-modifying/anticoagulant activity, or autonomic ganglion effects that cisatracurium does not have. All eight returned zero clinical trials and zero literature, consistent with these being TxGNN knowledge-graph co-occurrence artifacts rather than genuine signals.

The **preeclampsia family** (preeclampsia, mild pre-eclampsia, severe pre-eclampsia) is the only cluster with any supporting real-world evidence, but the link is indirect: preeclampsia/HELLP patients undergoing general anesthesia for cesarean delivery often have hepatic or renal impairment, making cisatracurium — whose elimination does not depend on liver or kidney function — a preferred neuromuscular blocker for *anesthetic management* of these patients. This is a **peri-operative drug-selection rationale**, not evidence that cisatracurium treats preeclampsia itself. The TxGNN score most likely reflects this co-occurrence in obstetric-anesthesia literature rather than a disease-modifying mechanism.

---

## Clinical Trial Evidence (Preeclampsia)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04645719](https://clinicaltrials.gov/study/NCT04645719) | Phase 3 | Unknown | 75 | Magnesium sulfate dosing in obese patients; evaluates eclampsia/pre-eclampsia control as one of several magnesium benefits. Not a cisatracurium intervention trial (relevance grade C). |
| [NCT04003688](https://clinicaltrials.gov/study/NCT04003688) | N/A | Completed | 74 | Magnesium sulfate dose-calculation strategy in obese patients; same context as above. Not a cisatracurium intervention trial (relevance grade C). |

Neither trial evaluates cisatracurium directly — both concern magnesium sulfate for eclampsia/pre-eclampsia in the general obstetric-anesthesia setting where cisatracurium may co-occur as an anesthetic agent.

## Literature Evidence (Preeclampsia)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | Cohort | Anesthesiology and Pain Medicine | Compares inflammatory cytokines (IL-6, leptin, adiponectin) after cesarean section under general vs. spinal anesthesia; does not evaluate cisatracurium's effect on preeclampsia. |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case series | Revista Española de Anestesiología y Reanimación | Remifentanil bolus for cesarean section in high-risk patients ineligible for spinal anesthesia; anesthesia-technique case series, not a cisatracurium efficacy study. |

No literature evaluates cisatracurium as a treatment for preeclampsia — both citations are general-anesthesia-technique studies in the obstetric setting.

**Cauda equina syndrome and the other 7 remaining candidates:** Currently no related clinical trials registered. Currently no related literature available.

---

## Malaysia Market Information

License-level detail (registration numbers, product names, dosage forms, approved indication text) was not populated for any of the 4 records in this data pull — all fields returned empty. The regulatory system confirms only the aggregate status: **4 active registrations, market status: Marketed**. Registration-level detail should be pulled directly from the NPRA product register before this is used for regulatory decision-making.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this data pull — this is flagged as a Blocking data gap and must be resolved before any safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the 10 TxGNN-predicted indications reach actionable evidence. The highest-scoring candidate (cauda equina syndrome) is mechanistically implausible and has zero supporting trials or literature, most consistent with a knowledge-graph false positive. The only candidate with any supporting evidence, preeclampsia, is backed solely by studies about anesthetic technique in obstetric patients, not by a disease-modifying effect of cisatracurium — this is a drug-selection rationale for existing anesthesia practice, not a new indication.

**To proceed, the following is needed:**
- TFDA/NPRA package-insert warnings and contraindications (Blocking data gap, DG001)
- Verified mechanism-of-action documentation from DrugBank (High-severity data gap, DG002)
- If the preeclampsia signal is pursued further: dedicated studies distinguishing "used during anesthesia for cesarean delivery in preeclamptic patients" from an actual disease-modifying effect
- Complete license-level regulatory detail (registration numbers, product names, dosage forms, approved indication text) from NPRA, currently blank in this data pull
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

