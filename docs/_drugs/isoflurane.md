---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 7
---

# Isoflurane
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

# Isoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is a volatile halogenated general anesthetic used for the induction and maintenance of general anesthesia. The TxGNN model predicts a very high association with **Prinzmetal angina** (vasospastic angina), but currently **zero clinical trials** and **zero publications** support this specific drug-disease link — the signal rests on the prediction score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (induction/maintenance) — based on known pharmacology; TFDA/NPRA approved-indication text is not populated in the current dataset |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack. Based on known pharmacology, isoflurane is a volatile ether-type general anesthetic that acts primarily as a positive allosteric modulator of GABA-A receptors, with additional NMDA receptor antagonism, producing dose-dependent CNS depression. At the vascular level, isoflurane is also known to produce coronary and systemic vasodilation.

The theoretical link to Prinzmetal angina — a disease driven by coronary artery vasospasm — is that a coronary vasodilatory effect could, in principle, counteract vasospasm. However, this connection is speculative rather than evidence-based: Prinzmetal angina is a chronic, episodic condition managed with long-term outpatient therapy (typically calcium channel blockers/nitrates), whereas isoflurane is only administered under general anesthesia in a monitored perioperative setting. There is no plausible route to chronic or as-needed use for this indication.

Consistent with this, the evidence pack itself flags this specific prediction as likely **noise**: despite the top-ranked TxGNN score among this drug's candidates, it has no supporting clinical trials or literature at all. By contrast, two lower-ranked predictions for this drug — manic bipolar affective disorder (rank 3, L3) and migraine disorder (rank 7, L4) — do have case-report and mechanistic literature support (e.g., burst-suppression isoflurane anesthesia vs. ECT for refractory depression/mania; isoflurane suppression of cortical spreading depolarization and case reports of status migrainosus terminated by general anesthesia). Those signals, not Prinzmetal angina, appear to be the more promising leads within this dataset for further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Isoflurane is recorded as marketed in Malaysia with 2 NPRA registrations, but product name, dosage form, manufacturer, and approved-indication text are not populated in the current dataset for either registration.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the complete absence of any clinical trial or literature evidence, combined with a clinically implausible route to chronic use of a general anesthetic for an episodic outpatient condition, means this prediction cannot currently be distinguished from model noise.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data — key warnings, contraindications, and drug interactions (currently a blocking data gap, DG001)
- Verified mechanism-of-action data from DrugBank (DG002)
- If this specific indication is still to be pursued, dedicated preclinical/mechanistic studies on isoflurane in vasospastic angina, since no human data exists
- Consider prioritizing the drug's other predicted indications with stronger evidence (manic bipolar affective disorder, L3; migraine disorder, L4) for the next evaluation cycle instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

