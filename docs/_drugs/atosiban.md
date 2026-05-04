---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: From Preterm Labour to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban is an oxytocin receptor antagonist registered in Malaysia as a tocolytic agent for inhibiting preterm labour. The TxGNN model places **Primary Hereditary Glaucoma** as its top predicted new indication, with a prediction score of 99.92%. However, this prediction is supported by **no clinical trials and no published literature**, and the proposed mechanism is directionally contradictory to the therapeutic goal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inhibition of preterm labour (tocolysis) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atosiban is a competitive antagonist of the oxytocin (OT) receptor and the vasopressin V1b receptor. Clinically, it suppresses uterine contractions by blocking OT receptors in the myometrium, making it the standard pharmacological option for threatened preterm labour. Detailed mechanism of action data from DrugBank was not retrieved in this evidence pack (DrugBank ID unavailable), but its pharmacological class is well-established in clinical practice.

The TxGNN prediction for primary hereditary glaucoma most likely derives from the known presence of OT receptors in the trabecular meshwork of the anterior eye. Some basic research suggests that endogenous OT may facilitate aqueous humour outflow, potentially contributing to intraocular pressure (IOP) regulation. Primary hereditary glaucoma — driven by mutations in genes such as MYOC and CYP1B1 — involves progressive optic nerve damage caused by chronically elevated IOP.

**However, a critical mechanistic contradiction undermines this prediction.** Atosiban *blocks* OT/OTR signalling, which would theoretically *impair* aqueous outflow and *raise* IOP — the exact opposite of what glaucoma treatment requires. Furthermore, hereditary glaucoma is a monogenic, structurally driven disease with no established direct link to OT signalling pathways. This prediction most likely reflects a graph-proximity artefact within the TxGNN knowledge graph (shared OTR-network nodes), rather than a genuine therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Atosiban in primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for Atosiban in primary hereditary glaucoma.

---

## Malaysia Market Information

Atosiban holds **2 registrations** in Malaysia with a current market status of **Marketed**. Registration details — including authorization numbers, product names, dosage forms, and approved indication texts — were not retrieved in this data pack. These should be verified directly through the National Pharmaceutical Regulatory Agency (NPRA) database before any further regulatory assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Note:** Both key warnings and contraindications are currently flagged as blocking-level data gaps in this evidence pack. NPRA/TFDA package insert retrieval is required before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication is at L5 (model prediction only), with zero supporting clinical trials or peer-reviewed literature. More critically, Atosiban's core mechanism — OT receptor *antagonism* — is directionally opposed to the therapeutic goal in primary hereditary glaucoma, where OT *agonism* would be needed to promote aqueous outflow and reduce IOP. This same mechanistic contradiction was identified across **all 10 of the top predicted indications** reviewed in this pack:

| Indication | Contradiction |
|---|---|
| Primary hereditary glaucoma | OT blocks outflow → raises IOP |
| Open-angle glaucoma | Same as above |
| Alopecia / Hypotrichosis variants | OT promotes hair follicle growth cycle; antagonist may worsen |
| Diffuse alopecia areata | OT has anti-inflammatory/immune-modulatory role; antagonist is counterproductive |
| Vascular disease | All 17 retrieved literature papers document OT *agonist* cardioprotection; Atosiban blocks this pathway |
| Thoracic outlet syndromes (venous/arterial) | Anatomical/structural disease; no OT pathway relevance |
| Visceral calciphylaxis | Calcium-phosphate vascular disease; no OT pathway relevance |

The single clinical trial retrieved (NCT03570294, linked to venous thoracic outlet syndrome) was correctly identified as a data-mapping error — it is an Atosiban tocolysis safety study with no relevance to the listed indication.

**To proceed, the following is needed:**

- Retrieve NPRA registration details for Atosiban (authorization numbers, product names, dosage forms, and approved indications) from the NPRA database
- Obtain full mechanism of action and safety profile from DrugBank (DrugBank ID is currently unavailable)
- Download and parse the TFDA/NPRA package insert to address the blocking-level safety data gap (warnings and contraindications)
- Conduct a hypothesis-driven literature search specifically investigating whether OT receptor *antagonism* — not agonism — could have any IOP-lowering or neuroprotective effect in glaucoma models
- Consider evaluating OT *agonists* (rather than Atosiban) as more mechanistically rational repurposing candidates for glaucoma, cardioprotection, or alopecia indications, where the existing evidence base points in that direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

