---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Biotin: From Nutritional Supplement to Dyspepsia

## One-Sentence Summary

Biotin (Vitamin B7) is a water-soluble B-vitamin widely used as a nutritional supplement for biotin deficiency and related conditions.
The TxGNN model predicts it may be effective for **Dyspepsia**,
however the evidence base is extremely thin — **0 relevant clinical trials** and only **1 marginally relevant publication** — making this a model-prediction-only candidate at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nutritional supplement (Vitamin B7 / biotin deficiency) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 338 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, biotin (Vitamin B7) is an essential coenzyme for carboxylase enzymes involved in fatty acid synthesis, gluconeogenesis, and amino acid catabolism. It functions as a cofactor for acetyl-CoA carboxylase, pyruvate carboxylase, propionyl-CoA carboxylase, and 3-methylcrotonyl-CoA carboxylase. There is no established pharmacological mechanism through which biotin would directly treat dyspepsia.

The TxGNN high score (99.43%) likely reflects the proximity of biotin's metabolic pathways to gastrointestinal system nodes in the knowledge graph. Biotin is absorbed in the small intestine and is associated with GI tract physiology, which may create graph-based "neighbourhood effects" that artificially inflate the prediction score. Notably, biotin deficiency can cause GI symptoms including nausea and anorexia, but this represents a deficiency-replacement relationship rather than a genuine drug repurposing opportunity.

The mechanistic rationale provided in the evidence pack itself characterises the link as "extremely weak" — dyspepsia involves acid secretion dysregulation, gastric motility disorders, visceral hypersensitivity, and H. pylori infection, none of which are plausibly modulated by a carboxylase cofactor. This prediction should be regarded with significant scepticism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs pregabalin as preemptive analgesia for postoperative pain. **Relevance: Grade C** — unrelated to biotin or dyspepsia; false-positive capture. |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption post-bariatric surgery. **Relevance: Grade C** — biotin was only one component of a multivitamin patch; dyspepsia was not an outcome. |

> **Note:** Neither trial directly investigates biotin for dyspepsia. Both were graded as **irrelevance (Grade C)** during evidence curation. Effectively, there are **zero relevant clinical trials** for this drug–indication pair.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical Study | Minerva Gastroenterol Dietol | Evaluated a food supplement containing sodium alginate, calcium carbonate, pineapple, papaya, ginger, α-galactosidase, and fennel in functional dyspepsia after H. pylori eradication. Biotin was not a component; tangential relevance only. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | J Dermatol | Biotin deficiency in a 5-month-old infant diagnosed with dyspepsia and fed amino acid formula. Demonstrates that dyspepsia was a *cause* of biotin deficiency, not that biotin treats dyspepsia. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Investigated stomach antral endocrine cells in IBS patients. No connection to biotin; relates to GI endocrine pathology. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endosc | Studied endocrine cell types in oxyntic mucosa of IBS patients. No biotin involvement. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review | Eksp Klin Gastroenterol | Evaluated a prebiotic supplement (containing inulin, oligofructose, vitamins including biotin, and minerals) for intestinal microbiocenosis in pulmonary patients on antibiotics. Biotin was a minor component; dyspepsia was not the target. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Basic Research | J Clin Pathol | IL-10 localisation in H. pylori-associated gastritis. No connection to biotin. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Basic Research | Kidney Int | Small bowel T cells and HLA class II antigen in IgA nephropathy. No relevance to biotin or dyspepsia. |

> **Note:** No publication directly investigates biotin as a treatment for dyspepsia. The literature results are predominantly false-positive retrievals from keyword co-occurrence.

---

## Malaysia Market Information

Biotin is registered with **338 licences** in Malaysia and is actively marketed. However, specific licence details (authorisation numbers, product names, dosage forms, and approved indications) were not available in the evidence pack.

> Detailed registration information should be retrieved from the NPRA database for a complete assessment.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

**Known general considerations for high-dose biotin:**
- High-dose biotin (e.g., 5–10 mg/day) can significantly interfere with biotin-streptavidin immunoassays, leading to falsely abnormal results for troponin, TSH, and other laboratory tests.
- This lab interference risk should be communicated to patients and clinicians if high doses are considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is numerically high (99.43%), but there is essentially **no supporting evidence** — zero relevant clinical trials, zero publications directly studying biotin for dyspepsia, and no plausible mechanistic link between a carboxylase cofactor vitamin and the pathophysiology of dyspepsia. The evidence pack's own mechanistic assessment rates the link as "extremely weak" and attributes the high score to graph-based proximity artefacts in the knowledge graph. This candidate does not warrant further investment at this time.

**To proceed, the following would be needed:**
- Identification of a credible mechanistic hypothesis linking biotin to any dyspepsia pathway (acid secretion, motility, visceral sensitivity)
- At least one preclinical study demonstrating biotin's effect on gastric function
- Retrieval of detailed MOA data from DrugBank to confirm absence of GI-relevant targets
- Resolution of safety data gaps (NPRA package insert warnings and contraindications)
- Consideration of whether the TxGNN signal may be a graph artefact warranting model recalibration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

