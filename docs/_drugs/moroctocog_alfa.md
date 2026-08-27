---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Moroctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant, B-domain deleted Factor VIII (rFVIII) replacement therapy, used in the treatment of Hemophilia A (Factor VIII deficiency). The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this direction is currently supported by only **7 clinical trials — most graded as low relevance (Grade C) or unrelated patient populations** — and **no supporting literature**, suggesting the high TxGNN score may reflect a knowledge-graph co-occurrence artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A / Factor VIII deficiency (inferred from FVIII-replacement context across the evidence pack; Malaysia license text does not specify an indication) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for moroctocog alfa is not available in this evidence pack (flagged as a High-severity data gap). However, contextual information embedded in the trial and rationale data confirms moroctocog alfa is a recombinant, B-domain deleted Factor VIII (rFVIII) molecule, whose pharmacological action is exogenous replacement of coagulation Factor VIII in patients with Hemophilia A.

Primary release disorder of platelets, however, is a platelet-granule secretion defect — a qualitative platelet function disorder, not a coagulation factor deficiency. The evidence pack's own mechanistic assessment for this candidate states the link is weak: supplementing Factor VIII does not correct defective platelet granule release, and the high TxGNN score is more likely explained by shared "bleeding tendency" nodes in the knowledge graph than by a true pharmacological relationship. This candidate should therefore be treated as a **potential false positive** pending stronger mechanistic or clinical evidence.

By contrast, a lower-ranked candidate in the same evidence pack — *acquired coagulation factor deficiency* (rank 4, TxGNN score 99.88%, evidence level L2, decision stage S2, recommendation "Proceed with Guardrails") — has a directly plausible mechanistic link (FVIII replacement for non-inhibitor acquired FVIII deficiency) and stronger supporting evidence, including a Phase 2/3 trial of a structurally analogous B-domain-deleted rFVIII product. This may be a more promising direction for follow-up than the top-ranked candidate discussed here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Evaluates persistent post-COVID-19-vaccination syndrome symptoms; not a treatment trial for platelet release disorder (Grade C relevance). |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Observational coagulation/haematology profiling in acute myeloid leukemia patients; unrelated to moroctocog alfa (Grade C). |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | Efficacy/safety of PEGylated rFVIII (BAX 855) in severe Hemophilia A patients undergoing surgery; wrong patient population for this indication (Grade C). |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system effects on coagulation in acute-on-chronic liver failure; relevance not yet assessed. |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN) prophylaxis trial in severe Hemophilia A (≥12 years); same drug class but studied in the original indication, not the predicted one (Grade C). |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | Pediatric BIVV001 safety/efficacy trial in severe Hemophilia A; same limitation as above (Grade C). |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal hemostasis study in patients undergoing TIPS placement; relevance not yet assessed. |

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Moroctocog alfa has 4 active registrations in Malaysia (market status: Marketed), but authorization numbers, product names, dosage forms, and approved indication text are not populated in the current data extract.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/NPRA label warnings and contraindications are flagged as a **Blocking** data gap — required before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Factor VIII replacement and primary platelet release disorder is weak, nearly all supporting trials are low-relevance or study unrelated populations, and no literature evidence exists. The high TxGNN score likely reflects graph co-occurrence around bleeding-related nodes rather than a genuine pharmacological signal.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (Blocking gap — required for safety evaluation)
- Confirmed mechanism-of-action documentation for moroctocog alfa (High-priority gap)
- Complete Malaysia authorization details (product names, dosage forms, approved indication text)
- Preclinical or mechanistic evidence directly linking FVIII replacement to platelet granule release function, if this candidate is to be pursued further
- Consider prioritizing the *acquired coagulation factor deficiency* candidate (rank 4) instead, given its stronger mechanistic plausibility and L2 evidence level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

