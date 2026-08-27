---
layout: default
title: Perphenazine
parent: 僅模型預測 (L5)
nav_order: 540
evidence_level: L5
indication_count: 10
---

# Perphenazine
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

Using the drug-repurposing evidence pack directly (no skill match for this — it's a template-driven content generation task), here's the report:

# Perphenazine: From Psychotic Disorders to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

> Perphenazine is a phenothiazine antipsychotic classically used for schizophrenia and related psychotic disorders. The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but this signal is supported by **zero clinical trials** and **15 publications that never mention perphenazine** — the evidence pack itself flags it as likely knowledge-graph embedding noise from a sparsely connected rare-disease node.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this data pull (TFDA/NPRA license record exists but is blank); Perphenazine is a phenothiazine antipsychotic classically indicated for schizophrenia/psychotic disorders |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.96% (rank 932) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate pair is not available (DG002, High severity). Based on what is known, Perphenazine is a typical phenothiazine antipsychotic with D2 dopamine receptor antagonism, 5-HT2A antagonism, and sedative activity, used clinically for schizophrenia and related psychotic disorders.

No plausible pharmacological link connects this action profile to retinal dystrophy or extraocular developmental anomalies, which are congenital/genetic ophthalmologic conditions (lens malformation, orbital structural anomalies, cranial dysinnervation disorders, etc.). The retrieved literature confirms this: all 15 publications discuss congenital eye/orbit pathology and **do not mention perphenazine at all**. The evidence pack's own rationale explicitly characterizes this as likely TxGNN knowledge-graph embedding noise, probably arising from sparse connectivity around this rare-disease node rather than a genuine pharmacological signal.

For context, a lower-ranked candidate in the same evidence pack — **anxiety disorder** (rank 10, score 99.53%) — shows a substantially more credible signal: multiple historical double-blind RCTs and two registered trials, consistent with the well-documented off-label anxiolytic use of low-dose phenothiazines (e.g., the historical perphenazine-amitriptyline combination product Triavil/Etrafon). That candidate carries an L2 evidence level and a "Proceed with Guardrails" recommendation, in contrast to the L5/Hold status of the top-ranked retinal dystrophy prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infection stages secondary to sinusitis; no drug relevance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Diagnostic approach to diplopia from ocular/neurologic/muscle disorders |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis pathophysiology and levator muscle fibrosis |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies and associated ocular dysgenesis |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia with orbital malformation |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis case |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler vitreoretinal degeneration syndrome complex |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric congenital ocular pathologies |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optometry and Vision Science | Congenital extraocular muscle fibrosis with synergistic divergence |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | Clinical features and management of orbital arteriovenous malformations |

None of the above discuss perphenazine or any pharmacological intervention — all are purely ophthalmologic/congenital-anomaly literature retrieved on disease-term overlap.

---

## Malaysia Market Information

A license record exists (total registrations: 1) under NPRA, but the registration number, product name, dosage form, and approved indication text were not captured in this data pull (part of DG001, Blocking severity). This needs to be sourced from the NPRA product label before market-status claims can be finalized.

---

## Safety Considerations

Key warnings, contraindications, and drug-interaction data were not captured in this evidence pack (DG001, Blocking — required before safety screening can proceed). Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (retinal dystrophy with/without extraocular anomalies) has a high TxGNN score but no clinical trials, no relevant literature, and no plausible mechanistic link — it is L5 evidence (model prediction only) and the evidence pack itself flags it as likely embedding noise.

**To proceed, the following is needed:**
- TFDA/NPRA label data — key warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action (DG002, High)
- If this specific signal is pursued: dedicated preclinical/pharmacological rationale linking perphenazine to retinal or extraocular developmental pathways
- Consider re-scoping this candidacy toward the **anxiety disorder** signal (rank 10, L2, Proceed with Guardrails), which has materially stronger clinical and literature support within the same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

