---
layout: default
title: Magnesium Sulfate
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Magnesium Sulfate
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

# Magnesium Sulfate: From Electrolyte/Anticonvulsant Therapy to Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium Sulfate is a long-established electrolyte and anticonvulsant agent with multiple clinical uses; detailed original-indication and mechanism data were not returned in this evidence pack. The TxGNN model predicts high relevance to **Preeclampsia/Eclampsia**, and this is supported by **50 clinical trials** and **20 publications** — though as noted below, this largely reflects confirmation of an already-established standard of care rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Malaysia registration data provided (license indication text not returned in this extract) |
| Predicted New Indication | Preeclampsia/Eclampsia |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this extract (flagged as a High-severity data gap). Based on known pharmacology, Magnesium Sulfate acts as an NMDA receptor antagonist and calcium-channel blocker: it suppresses neuronal hyperexcitability (anticonvulsant effect) and induces relaxation of cerebral and peripheral vascular smooth muscle.

This mechanism maps directly onto the pathophysiology of preeclampsia/eclampsia, where seizure activity and cerebral vasospasm are the central clinical problems. Importantly, this is **not an exploratory repurposing finding** — Magnesium Sulfate is already the internationally recognized standard of care for eclampsia prophylaxis and treatment (ACOG, WHO guidelines). The TxGNN prediction here should be read as a validation/completeness check of the evidence base rather than discovery of a new use, which is reflected in the very high volume of supporting trials and literature below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | RCT comparing continuation vs. discontinuation of postpartum MgSO4 in severe preeclampsia |
| [NCT02835339](https://clinicaltrials.gov/study/NCT02835339) | Phase 4 | Completed | 66 | RCT on MgSO4 pharmacokinetics/dosing in obese preeclamptic women |
| [NCT01846156](https://clinicaltrials.gov/study/NCT01846156) | Phase 3 | Completed | 240 | RCT comparing MgSO4 protocols for severe pre-eclampsia |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | RCT: 1g vs 2g/hr IV maintenance dose efficacy/safety in severe pre-eclampsia |
| [NCT04387565](https://clinicaltrials.gov/study/NCT04387565) | N/A | Completed | 210 | Observational study of maternal Mg/vanadium levels in preeclampsia (mechanistic support) |
| [NCT01492608](https://clinicaltrials.gov/study/NCT01492608) | Phase 3 | Completed | 560 | MASP-STUDY: antenatal MgSO4 for prevention of cerebral palsy/death in preterm infants |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1114 | Multicenter RCT on postpartum MgSO4 duration in severe preeclampsia |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | RCT on novel postpartum MgSO4 protocol (6h vs 24h) |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | N/A | Completed | 114 | RCT: low-dose MgSO4 vs standard Pritchard regimen for severe preeclampsia/eclampsia |
| [NCT06126068](https://clinicaltrials.gov/study/NCT06126068) | N/A | Completed | 120 | RCT comparing loading-dose MgSO4 with Pritchard regimen in a low-resource setting |

*(50 total clinical trials were identified for this indication; the above 10 are the highest-quality, most directly relevant completed RCTs.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT | PLoS One | Springfusor pump vs. standard IM administration acceptability trial |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | Review of efficacy, benefits and risks of MgSO4 seizure prophylaxis |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | American Journal of Obstetrics and Gynecology | MgSO4 as the ideal anticonvulsant in preeclampsia-eclampsia |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | Review/Mechanism | Stroke | Mechanistic review: MgSO4 action via cerebral vasospasm relief |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstetrical & Gynecological Survey | Cerebral hemodynamics rationale for MgSO4 use |
| [41054655](https://pubmed.ncbi.nlm.nih.gov/41054655/) | 2025 | Review | Cureus | Pharmacology and clinical applications of MgSO4 across settings |
| [39110688](https://pubmed.ncbi.nlm.nih.gov/39110688/) | 2024 | Qualitative Study | PLoS One | Nurse-midwife perspectives on MgSO4 administration (Tanzania) |
| [31527059](https://pubmed.ncbi.nlm.nih.gov/31527059/) | 2019 | Commentary | Global Health: Science and Practice | Systems-level barriers to MgSO4 use in resource-limited settings |
| [490496](https://pubmed.ncbi.nlm.nih.gov/490496/) | 1979 | Historical/Clinical | The Journal of Reproductive Medicine | Pritchard's original description of MgSO4 use in preeclampsia-eclampsia |
| [1566765](https://pubmed.ncbi.nlm.nih.gov/1566765/) | 1992 | Animal/Mechanism | American Journal of Obstetrics and Gynecology | Central anticonvulsant effects of MgSO4 on hippocampal seizures |

*(20 total publications were identified for this indication.)*

---

## Malaysia Market Information

Malaysia registration data confirms **12 registered products** with market status ✓ Marketed. However, per-product details (registration number, product name, dosage form, approved indication text) were not returned in this data extract — this is flagged as a **Blocking** data gap (DG001) requiring an NPRA label lookup before final safety/indication confirmation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 (multiple completed Phase 3/4 RCTs) strongly supports Magnesium Sulfate's efficacy in preeclampsia/eclampsia, consistent with its status as international standard of care (ACOG/WHO). However, Malaysia-specific label data (warnings, contraindications, registered indication text) is currently missing and blocks a full local safety assessment.

**To proceed, the following is needed:**
- NPRA package insert / label retrieval to resolve the Blocking data gap (DG001) — warnings, contraindications, and confirmed registered indication text
- DrugBank mechanism-of-action detail (DG002) to complete the mechanistic linkage documentation
- Per-product license detail (registration numbers, product names, dosage forms) for the 12 registered Malaysia products
- Confirmation of whether local clinical guidelines already recognize this indication, since global evidence indicates this is established practice rather than a novel repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

