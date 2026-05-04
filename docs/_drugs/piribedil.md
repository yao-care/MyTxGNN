---
layout: default
title: Piribedil
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 5
---

# Piribedil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Piribedil: From Parkinson's Disease to Retinal Dystrophy with or Without Extraocular Anomalies

## One-Sentence Summary

Piribedil is a dopamine D2/D3 receptor agonist approved for Parkinson's disease in France and several Asian markets, with one active registration in Malaysia.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or Without Extraocular Anomalies**, supported by **0 clinical trials** and **15 retrieved publications** — none of which appear to directly investigate this drug-disease combination.
The mechanistic link is very weak, and the high prediction score likely reflects a knowledge graph artefact rather than genuine biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Malaysia regulatory data (internationally known indication: Parkinson's disease) |
| Predicted New Indication | Retinal Dystrophy with or Without Extraocular Anomalies |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Piribedil is a dopamine D2/D3 receptor agonist (with additional alpha-2 adrenoceptor antagonist properties), whose efficacy in Parkinson's disease has been clinically established through direct stimulation of dopaminergic pathways in the nigrostriatal system. It is approved in France and several Asian countries as a first- or adjunct-line agent for Parkinson's motor symptoms.

The mechanistic link to retinal dystrophy with or without extraocular anomalies is theoretically very weak. Hereditary retinal dystrophies are caused by mutations affecting ciliary function, photoreceptor structure, or retinal pigment epithelium biology — pathways entirely unrelated to dopaminergic signalling. While the retina does contain dopaminergic amacrine cells that modulate light adaptation, their involvement does not translate into a plausible therapeutic pathway for progressive photoreceptor degeneration.

The high TxGNN score (99.34%) is most likely an artefact of knowledge graph over-generalization: the "dopaminergic → neurodegeneration" connectivity in the graph is broad enough to span structurally unrelated diseases such as hereditary retinopathy. This interpretation is supported by the fact that the 15 retrieved publications describe orbital anatomy, extraocular muscle disorders, and congenital ocular anomalies — none of which directly investigate Piribedil in the context of retinal dystrophy. By contrast, the Rank 2 and Rank 4–5 predictions (juvenile-onset Parkinson syndromes and PLA2G6-associated neurodegeneration with parkinsonism) carry substantially stronger mechanistic rationale and warrant prioritization over this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ **Relevance Notice**: The following 15 publications were retrieved by keyword matching on "retinal dystrophy with or without extraocular anomalies." After review, **none of the papers directly investigate Piribedil** in this condition. All relevance assessments remain pending. The publications primarily address orbital pathology, congenital extraocular muscle disorders, and developmental ocular anomalies that are unrelated to this drug-disease pairing.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis of pediatric orbital lesions, covering congenital and developmental ocular pathologies including microphthalmos, coloboma, and Coats disease |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies; discusses structural and developmental defects with potential association to anterior segment dysgenesis |
| [37408430](https://pubmed.ncbi.nlm.nih.gov/37408430/) | 2023 | Review | Chinese Journal of Ophthalmology | Structure and innervation of extraocular muscles; pulley tissue abnormalities and their role in strabismus |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Research Article | International Journal of Molecular Sciences | Optic nerve and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM); explores whether KIF21A/TUBB3 mutations extend beyond the oculomotor system |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Classification of congenital cranial dysinnervation disorders (CCDDs); ophthalmoplegia subtypes and diagnostic confirmation strategies |
| [27930425](https://pubmed.ncbi.nlm.nih.gov/27930425/) | 2017 | Anatomical Study | Ophthalmic Plastic and Reconstructive Surgery | Description of the anomalous gracillimus orbitis accessory extraocular muscle found in cadaver dissections |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis: levator muscle fatty dystrophy, fibrosis, and association with refractive errors and binocular vision disturbance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Clinical Guide | Seminars in Neurology | Systematic history-taking and examination approach to diplopia; differential diagnosis of ocular, neurologic, and extraocular muscle disorders |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review/Case Series | Seminars in Ultrasound, CT, and MR | Orbital infections: five-stage classification of periorbital cellulitis secondary to sinusitis; systemic predisposing conditions |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case Series | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: vitreoretinal degeneration, myopia, and extraocular manifestations including sensorineural deafness and skeletal dysplasia |

---

## Malaysia Market Information

The regulatory data confirms 1 active registration for Piribedil in Malaysia (NPRA status: Marketed). However, specific authorization details — including authorization number, product name, dosage form, and approved indication text — are not available in the current evidence pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Details not available in current evidence pack; please verify via NPRA official portal |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 99.34%, there is no clinical trial evidence and no directly relevant literature supporting Piribedil use in hereditary retinal dystrophies. The dopamine D2/D3 agonist mechanism of Piribedil does not address the ciliary dysfunction or photoreceptor degeneration underlying this condition, and the high score most likely reflects over-generalization within the knowledge graph's neurodegeneration node cluster.

**To proceed, the following is needed:**
- Retrieve the Malaysia NPRA package insert to confirm the approved indication text and complete safety profile (key warnings, contraindications)
- Obtain full MOA data from DrugBank (DB12478) to enable proper mechanistic analysis
- Conduct a targeted literature search specifically combining "piribedil" AND ("retinal dystrophy" OR "photoreceptor" OR "retinitis pigmentosa") to exclude any overlooked direct evidence
- Re-examine the TxGNN graph topology to determine whether the prediction arises from an overgeneralized "dopaminergic → neurodegeneration" pathway, and consider down-weighting this edge type for ophthalmological indications
- **Prioritize the higher-plausibility predictions instead**: Rank 2 (Hunt's juvenile paralysis agitans), Rank 4 (PLA2G6-associated neurodegeneration/PARK14), and Rank 5 (juvenile onset Parkinson disease 19A) all involve dopaminergic pathway dysfunction and carry meaningfully stronger mechanistic rationale for Piribedil repurposing — these should be advanced to the next evaluation stage ahead of the retinal dystrophy indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

