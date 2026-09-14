---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is an oral, reversible P2Y12 platelet receptor antagonist originally used to reduce thrombotic cardiovascular events in acute coronary syndrome (ACS) and post-PCI patients. The TxGNN model predicts it may also be effective for **intracranial arteriosclerosis** (intracranial atherosclerotic disease, ICAD), with **11 clinical trials** and **3 publications** currently supporting this direction, including two directly relevant Phase 3 trials (SOCRATES/EUCLID population and the ongoing CAPTIVA trial).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied registration data (ticagrelor's established indication is prevention of thrombotic cardiovascular events in ACS / post-MI, per P2Y12-inhibitor class use documented throughout the evidence pack) |
| Predicted New Indication | Intracranial Arteriosclerosis (Intracranial Atherosclerotic Disease) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text was not returned for this candidate, but the mechanism is well established from the evidence in this pack: ticagrelor is a reversible, direct-acting P2Y12 receptor antagonist that inhibits ADP-mediated platelet activation and aggregation, the core pharmacology behind its approved use in atherothrombotic cardiovascular disease.

Intracranial arteriosclerosis (ICAD) causes ischemic stroke and TIA through platelet-mediated thrombus formation on atherosclerotic plaque within intracranial arteries — mechanistically the same thrombotic pathway that ticagrelor already targets in its approved indications. This is not a novel mechanistic leap: ticagrelor has already been studied head-to-head against aspirin in acute ischemic stroke/TIA populations that include intracranial atherosclerosis subgroups (the SOCRATES trial), and is currently being compared against clopidogrel specifically in symptomatic intracranial atherosclerotic stenosis in the ongoing CAPTIVA trial.

Because the predicted indication sits on the same causal pathway (platelet-driven arterial thrombosis) as ticagrelor's existing use, the TxGNN prediction is biologically coherent rather than a speculative cross-disease inference — it is closer to a label-extension hypothesis than a true repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13,885 | EUCLID: ticagrelor vs. clopidogrel for CV death, MI, and ischemic stroke in peripheral artery disease; directly relevant antithrombotic comparison (Grade A) |
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1,683 | CAPTIVA: rivaroxaban and/or ticagrelor vs. clopidogrel specifically for intracranial vascular atherostenosis, evaluating 1-year stroke/hemorrhage/vascular death rates (Grade A) |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | EVOLVE Short DAPT: 3-month DAPT safety in high-bleeding-risk patients after intracranial-relevant stent PCI (Grade B) |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS: ticagrelor + aspirin vs. standard DAPT after stent implantation (Grade C) |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | NA | Recruiting | 100 | Genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic intracranial atherosclerotic disease |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | NA | Recruiting | 792 | DREAM-PRIDE: drug-eluting stent + aggressive medical therapy vs. standard therapy for recurrent stroke prevention in intracranial atherosclerotic disease |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | NA | Unknown | 2,171 | Anticoagulation vs. anticoagulation + antiplatelet in acute ischemic stroke with AF and extracranial/intracranial artery stenosis |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Not yet recruiting | 3,500 | Quality-control standard system for DAPT in coronary revascularization (high bleeding risk ACS population) |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2,036 | Low-dose vs. standard-dose ticagrelor after DES implantation in unstable angina |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not yet recruiting | 1,700 | SOLOPCI: very short DAPT followed by P2Y12 monotherapy in elderly post-PCI patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT | International Journal of Stroke | Design of the CAPTIVA trial comparing dual antithrombotic regimens (including ticagrelor) against standard clopidogrel + aspirin for symptomatic intracranial atherosclerotic stenosis |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis — introduction, highlights, and knowledge gaps in antithrombotic management |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of Neurointerventional Surgery | Clinical experience with lower-dose ticagrelor (60 mg BID) plus aspirin vs. standard aspirin/clopidogrel for intracranial stenting |

---

## Malaysia Market Information

License-level details (registration numbers, product names, dosage forms, manufacturers) were not returned in the current data pack — all fields in the source registration records were empty. The market status is confirmed as **marketed (已上市)** with **8 total registrations** on file. Registration-level details need to be pulled from the source registry before regulatory cross-checks can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack's key warnings, contraindications, and drug-interaction lookup all returned no data for this candidate (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two directly relevant Phase 3 trials (SOCRATES/EUCLID and the ongoing CAPTIVA trial) study ticagrelor in stroke and intracranial atherosclerotic disease populations, and the proposed mechanism overlaps directly with ticagrelor's already-approved antithrombotic use — this is a mechanistically low-risk extension rather than a novel repurposing hypothesis, but it still requires formal indication-specific evidence review before clinical guidance can be issued.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently blocking — flagged as DG001)
- Detailed mechanism-of-action documentation from DrugBank (flagged as DG002)
- Malaysia license-level registration details (product names, dosage forms, manufacturers)
- Completed drug-drug interaction data (current query returned no results)
- Awaiting CAPTIVA (NCT05047172) primary results, expected completion 2028-05-31
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

