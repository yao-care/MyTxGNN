---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Paliperidone is an antipsychotic (active metabolite of risperidone) established for treating schizophrenia. The TxGNN model's top-ranked prediction for this drug is **retinal dystrophy with or without extraocular anomalies**, a group of inherited photoreceptor disorders — but the **15 supporting publications** are ophthalmology case reports/reviews unrelated to paliperidone's pharmacology, and **0 clinical trials** test this pairing, so this ranks as a low-confidence, likely spurious embedding-similarity artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (referenced in evidence pack; no structured original-indication or license-indication text was returned — see note below) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.92% (rank 1,661 of all drug-disease pairs) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

**Note:** `original_indications` and every `taiwan_regulatory.licenses` entry are blank in this evidence pack (see Data Gaps DG001/DG002). The "Schizophrenia" original indication above is inferred only from cross-referenced text in a lower-ranked candidate's rationale (`treatment-refractory schizophrenia`, rank 10), not from a structured TFDA/NPRA field — it should be confirmed against the package insert before use.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for paliperidone in this evidence pack (DG002, High severity). Based on information surfaced elsewhere in the pack, paliperidone (9-hydroxy-risperidone) is a central D2/5-HT2A receptor antagonist used for schizophrenia — a mechanism with no known connection to retinal dystrophy, which is typically a genetically driven photoreceptor/retinal pigment epithelium disorder (e.g., *RPE65*, *CRB1* mutations).

The model's own rationale for this candidate is explicit that no mechanistic link exists: it describes the association as arising from TxGNN's high-dimensional embedding similarity rather than real pharmacological evidence. Consistent with this, none of the 15 associated publications actually discuss paliperidone — they are general ophthalmology reviews and case reports on orbital infections, congenital ptosis, extraocular muscle anomalies, and related topics that likely co-occur with "retinal dystrophy" in keyword space but not in causal/mechanistic space.

Given this, the prediction should be treated as a hypothesis-generation artifact only. It does not currently meet the bar for further pharmacological investigation without independent, drug-specific mechanistic or preclinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infections secondary to sinusitis; no mention of paliperidone or retinal dystrophy pharmacology |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia from ocular/neurologic/muscle causes; unrelated to drug therapy |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis pathophysiology and evaluation; no drug relevance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies; developmental, not pharmacological |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler vitreoretinal degeneration syndrome complex; genetic, not drug-related |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging differential diagnosis of pediatric ocular pathologies; no drug relevance |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Unilateral cryptophthalmia case series; congenital, no drug link |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis case; no drug link |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | Congenital extraocular muscle fibrosis case; no drug link |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case Report | Archives of Ophthalmology | Orbital arteriovenous malformation series; no drug link |

*5 additional lower-relevance records (unclassified/pending) were excluded from this table.*

## Malaysia Market Information

License-level details (registration number, product name, dosage form, approved indication text) were not returned by this data pull — all five sampled `taiwan_regulatory.licenses` entries are blank. The evidence pack confirms paliperidone is marketed in Malaysia under **17 total registrations**, but individual product-level data needs to be re-queried from NPRA before it can be tabulated here.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data were all returned as data gaps — DG001, Blocking severity — and drug interaction lookup returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (retinal dystrophy with or without extraocular anomalies) has a high similarity score but no mechanistic rationale, no clinical trials, and literature that is topically adjacent rather than substantively relevant — the model's own annotation calls this likely embedding noise. This does not meet even the threshold for a "Research Question" stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) to close the Blocking data gap (DG001) before any further evaluation of *any* candidate for this drug
- Confirmed original indication and full license text (currently blank across all sampled entries)
- Verified MOA data from DrugBank (DG002) to properly assess mechanistic plausibility
- If pursuing this drug further, consider the pack's rank-10 candidate (**treatment-refractory schizophrenia**, score 99.80%, Evidence Level L2, decision stage S2/"Research Question") instead — it has a direct mechanistic link, 4 clinical trials (including a completed Phase 4 study specifically on paliperidone palmitate in schizophrenia), and 2 supporting reviews, making it a substantially stronger candidate than the current top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

