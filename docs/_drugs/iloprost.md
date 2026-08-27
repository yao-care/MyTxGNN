---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Iloprost: From Pulmonary Arterial Hypertension to HIV-Associated Pulmonary Arterial Hypertension

## One-Sentence Summary

> Iloprost is a synthetic prostacyclin (PGI2) analog already established as a treatment for pulmonary arterial hypertension (PAH). Among nine TxGNN-predicted indications for this drug, the strongest evidence supports **PAH associated with HIV infection** — a recognized WHO Group 1 PAH subtype — backed by **1 completed Phase 3 RCT** and **4 supporting publications**. Several top-ranked predictions by raw model score (e.g., scalp hypotrichosis, alopecia areata) have no mechanistic plausibility or supporting evidence and are flagged in the pack itself as likely knowledge-graph embedding noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (per repurposing rationale references to "existing PAH indication"; official TFDA/NPRA label text itself is a data gap) |
| Predicted New Indication | Pulmonary Arterial Hypertension associated with HIV infection |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is a flagged gap in this pack (DG002). However, the evidence pack's own repurposing rationale consistently describes iloprost as a **synthetic prostacyclin (PGI2) analog** with pulmonary vasodilator and antiplatelet/antithrombotic activity — the core pharmacological class used to treat WHO Group 1 PAH.

HIV-associated PAH is formally classified as a Group 1 PAH subtype under current pulmonary hypertension nosology, sharing the same underlying pulmonary vascular pathology (endothelial dysfunction, vasoconstriction, vascular remodeling) as the drug's existing PAH indication. Because of this, the rationale text explicitly notes this is **not** a cross-indication extrapolation but a direct application of iloprost's established mechanism to a specific etiological subgroup that may not be explicitly named on the current label.

This also explains the pattern across the other predicted candidates: PAH subtypes associated with congenital heart disease, connective tissue disease, chronic hemolytic anemia, and schistosomiasis all score highly for the same mechanistic reason (all are Group 1 PAH). By contrast, the two highest raw-score predictions — scalp hypotrichosis and alopecia areata — involve hair-follicle/immune pathology with no known connection to prostacyclin pharmacology, and both are explicitly flagged in the pack as suspected model noise with zero supporting trials or literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Multicenter, double-blind, randomized, placebo-controlled crossover study of a single dose of Iloprost Power 15 on exercise capacity in symptomatic PAH patients, including HIV-associated PAH; graded "A" relevance — direct, completed Phase 3 evidence for this subgroup. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Cohort/Registry | Terapevticheskii arkhiv | National PAH registry analysis (6-year observation) covering prevalence, clinical course, therapy, and mortality. |
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | Mt Sinai J Med | Overview of HIV-related pulmonary arterial hypertension pathogenesis and presentation. |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | Am J Respir Med | Review of prostanoid therapy across PAH etiologies, including HIV infection. |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Review of prostacyclin/prostanoid controlled trials across PAH subtypes including HIV infection. |

---

## Malaysia Market Information

Iloprost is currently marketed in Malaysia with 1 active registration, but the license number, product name, dosage form, manufacturer, and approved indication text are not available in this evidence pack (data gap DG001 — TFDA/NPRA label details not yet retrieved).

---

## Other Predicted Indications (Same Drug)

For context, the full evidence pack evaluates 9 TxGNN-predicted indications for iloprost. Ranked by evidence strength rather than raw model score:

| Predicted Indication | Evidence Level | Recommendation |
|---|---|---|
| PAH associated with HIV infection | L1 | Proceed with Guardrails |
| PAH associated with connective tissue disease | L2 | Proceed with Guardrails |
| PAH associated with congenital heart disease | L2 | Research Question |
| PAH associated with schistosomiasis | L4 | Research Question |
| Pulmonary arteriovenous malformation | L4 | Hold |
| PAH associated with chronic hemolytic anemia | L5 | Hold |
| Hypotrichosis simplex of the scalp | L5 | Hold (suspected embedding noise) |
| Congenital hypotrichosis milia | L5 | Hold (suspected embedding noise) |
| Diffuse alopecia areata | L5 | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this evidence pack — key warnings, contraindications, and drug interactions — are unresolved data gaps; DG001 flags TFDA label warnings/contraindications as a **Blocking** gap that must be closed before a formal S1 safety review.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
HIV-associated PAH has the strongest evidentiary support among the predicted candidates — a completed Phase 3 RCT plus corroborating literature — and represents a mechanistically direct extension of iloprost's existing PAH indication rather than a novel repurposing hypothesis. Other PAH-subtype candidates (connective tissue disease, congenital heart disease) are directionally supportive but lower-powered (L2), while the top raw-score candidates (hypotrichosis, alopecia) lack any mechanistic or evidentiary basis and should be held.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): retrieve TFDA/NPRA label warnings, contraindications, and full registration details
- Resolve DG002: obtain formal DrugBank MOA record to confirm the mechanistic linkage used above
- Confirm whether the current Malaysia label already covers HIV-associated PAH explicitly, or whether this represents a labeling gap rather than a new indication
- Classify remaining relevance="pending" literature entries to firm up the evidence tier for lower-ranked candidates before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

