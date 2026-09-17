---
layout: default
title: Sulpiride
parent: Low Evidence (L4-L5)
nav_order: 631
evidence_level: L5
indication_count: 9
---

# Sulpiride
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **9** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Sulpiride: From Psychiatric/Vertigo Indications to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Sulpiride is a benzamide-class D2/D3 dopamine receptor antagonist, clinically used for schizophrenia, depression, and vertigo. The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**, a congenital eye disorder, but currently **0 clinical trials** and **no sulpiride-specific publications** support this direction — the evidence pack's own rationale flags the biological link as unestablished.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, depression, vertigo (per drug-class description in evidence pack; official license indication text not returned) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for sulpiride was not retrieved from DrugBank in this pull (flagged as a High-severity data gap). Based on the drug-class information available in the evidence pack, sulpiride is a selective D2/D3 dopamine receptor antagonist of the benzamide class, used for schizophrenia, depression, and vertigo.

Retinal dystrophy with or without extraocular anomalies is a congenital, structural eye disorder typically driven by genetic developmental defects, not by dopaminergic signaling. The evidence pack's own mechanistic assessment states there is no known pathological connection between D2/D3 receptor antagonism and this disease, and that this conclusion would not change even if full MOA data were available.

Given the absence of a plausible biological rationale, this candidate should be treated as a likely false-positive signal from the knowledge-graph embedding model rather than a genuine repurposing opportunity — a caveat that also applies to the other 8 predicted indications in this evidence pack (hydranencephaly, polymicrogyria syndromes, CMT1G, X-linked myopia variants, CDG, glycine encephalopathy), all of which carry the same L5/Hold status with zero supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections/cellulitis staging secondary to sinusitis; does not discuss sulpiride |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Diagnostic approach to diplopia from ocular/neurologic/muscular causes; general clinical pearls |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Case Report/Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis classification (simple vs. complicated forms) and associated extraocular fibrosis |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and associated anterior segment dysgenesis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: vitreoretinal degeneration with systemic extraocular features |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging classification of pediatric orbital/ocular pathologies (congenital and developmental) |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia with orbital/globe malformation |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis, a cranial dysinnervation disorder |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | Congenital fibrosis of extraocular muscles with synergistic divergence/adduction |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case Report | Archives of Ophthalmology | Case series of orbital arteriovenous malformations |

**Note:** None of the retrieved articles study sulpiride or any pharmacologic intervention for this disease — they are general ophthalmology/radiology reviews and case reports on congenital eye/orbit anomalies, likely surfaced through keyword overlap ("congenital," "extraocular") rather than genuine drug-disease evidence.

## Malaysia Market Information

Malaysia (NPRA) records 3 active registrations for sulpiride (market status: Marketed), but license numbers, product names, dosage forms, and approved indication text were not returned in this data pull.

## Safety Considerations

Please refer to the package insert for safety information. (Note: retrieval of the TFDA/NPRA package insert — needed for warnings and contraindications — is an open, Blocking-severity data gap that must be resolved before any safety pre-assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or disease-specific literature evidence for this drug-disease pair, and the evidence pack's own mechanistic analysis finds no plausible biological link between D2/D3 dopamine antagonism and a congenital, genetically-driven retinal dystrophy — this is most likely a knowledge-graph embedding artifact. Safety pre-assessment (S1) is additionally blocked pending package insert retrieval.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (PDF) to resolve the Blocking warnings/contraindications data gap
- Confirmed mechanism of action via DrugBank API to close the MOA data gap
- Independent biological/genetic plausibility review, since the predicted target is a structural congenital disorder rather than a pharmacologically modulable pathway
- Given the pattern across all 9 predictions in this pack (uniform L5/Hold, zero trials/literature), consider deprioritizing this candidate set pending stronger signal from a future model iteration
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

