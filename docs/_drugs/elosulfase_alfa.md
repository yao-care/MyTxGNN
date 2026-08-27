---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
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

# Elosulfase Alfa: From Morquio A Syndrome (Mucopolysaccharidosis IVA) to Scheie Syndrome

## One-Sentence Summary

Elosulfase alfa is an enzyme replacement therapy whose approved use — established through its own clinical literature — is Morquio A syndrome (Mucopolysaccharidosis IVA, MPS IVA), caused by N-acetylgalactosamine-6-sulfatase (GALNS) deficiency. The TxGNN model predicts potential efficacy in **Scheie syndrome**, but this signal is currently supported by **0 clinical trials** and only **2 publications**, neither of which studies elosulfase alfa or Scheie syndrome directly. Evidence strength is minimal, and the drug's own regulatory safety data (Malaysia label warnings/contraindications) is not yet available for review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Morquio A syndrome (Mucopolysaccharidosis IVA) — inferred from embedded literature evidence; formal Malaysia label text not yet retrieved |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for elosulfase alfa is not yet available in this evidence pack (flagged as a High-severity data gap). Based on information embedded in the supporting literature, elosulfase alfa is a recombinant human GALNS enzyme replacement therapy indicated for Morquio A syndrome (MPS IVA), where deficiency of the GALNS enzyme causes accumulation of keratan sulfate and chondroitin-6-sulfate, driving skeletal dysplasia and multi-organ disease.

Scheie syndrome, by contrast, is the mild/attenuated end of the Mucopolysaccharidosis type I (MPS I) spectrum, caused by deficiency of α-L-iduronidase (IDUA), a different enzyme acting on a different substrate (dermatan sulfate/heparan sulfate) than the keratan sulfate pathway targeted by elosulfase alfa. Both conditions fall under the broader "mucopolysaccharidosis" disease family and share overlapping clinical features (skeletal, joint, and connective tissue involvement), which likely explains why a knowledge-graph model would place them close together in embedding space. However, there is no shared enzymatic target between the two conditions, so the mechanistic basis for repurposing is weak.

Overall, this looks more like a disease-family proximity signal (MPS I vs. MPS IVA) than a genuine mechanistic repurposing opportunity. The supporting literature confirms this: both cited papers are general MPS-cohort molecular characterization studies, not studies of elosulfase alfa treatment or of Scheie syndrome specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Cohort (disease characterization, not a drug study) | Human Mutation | Molecular/genetic characterization of 302 Iranian MPS patients across multiple MPS subtypes; does not evaluate elosulfase alfa or treatment outcomes in Scheie syndrome. |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Cohort (disease characterization, not a drug study) | Pathologie-biologie | Describes clinical features and consanguinity patterns in Tunisian MPS I (Hurler) and MPS IVA (Morquio A) patients; contrasts the IDUA deficiency of MPS I with the GALNS deficiency of MPS IVA — no elosulfase alfa intervention data. |

---

## Malaysia Market Information

Elosulfase alfa is recorded as marketed in Malaysia with 1 registered license; however, detailed authorization number, product name, dosage form, manufacturer, and approved indication text are not currently available in this evidence pack (data gap). This should be obtained directly from the NPRA product registry before any regulatory-facing use of this report.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: retrieval of the Malaysia label's warnings/contraindications is flagged as a **Blocking** data gap in this evidence pack — this must be resolved before any Stage 1 (S1) safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between elosulfase alfa and Scheie syndrome has an L5 evidence level (model prediction only) — there are no clinical trials and no literature that actually studies elosulfase alfa in Scheie syndrome. The two enzymes involved (GALNS for Morquio A vs. IDUA for Scheie/MPS I) act on different substrates, so the mechanistic rationale is weak and the signal is best interpreted as a disease-family embedding artifact rather than a genuine repurposing lead.

**To proceed, the following is needed:**
- Malaysia (NPRA) label warnings/contraindications for elosulfase alfa (currently a Blocking data gap preventing safety pre-assessment)
- Confirmed mechanism-of-action documentation from DrugBank or the manufacturer
- Complete NPRA license/registration details (authorization number, product name, dosage form, approved indication text)
- Any preclinical or biochemical data specifically addressing cross-reactivity or potential benefit of GALNS-targeted ERT in IDUA-deficient (MPS I/Scheie) disease, if such a hypothesis is to be pursued further
- A review of the underlying disease-vocabulary mapping used by the prediction pipeline — other candidate indications in this same evidence pack showed clear literature-to-disease mismatches (e.g., Morquio A-specific elosulfase alfa trials indexed under an unrelated "Sanfilippo syndrome" label), suggesting this data source should be validated before being used for further decision-making
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

