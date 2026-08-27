---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 520
evidence_level: L5
indication_count: 5
---

# Omeprazole
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

# Omeprazole: From Gastroesophageal Reflux Disease to Hyperinsulinism

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI), long established for gastroesophageal reflux disease (GERD) and peptic ulcer disease.
The TxGNN model's top-ranked new-indication prediction is **Hyperinsulinism**, but the prediction score is **0%**, and none of the **5 clinical trials** or **7 publications** identified directly test this hypothesis — evidentiary support is essentially absent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal Reflux Disease (GERD) / Peptic Ulcer Disease (PPI class; specific Malaysia label indication text not present in evidence pack) |
| Predicted New Indication | Hyperinsulinism |
| TxGNN Prediction Score | 0% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 45 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, omeprazole is a proton pump inhibitor that irreversibly binds gastric parietal cell H+/K+-ATPase, suppressing acid secretion — its efficacy in GERD and peptic ulcer disease is well established (see esophagitis, gastric ulcer, and duodenal ulcer entries in this same evidence pack, all scored L1/S3).

For Hyperinsulinism specifically, the mechanistic story is contradictory rather than supportive. On one hand, long-term omeprazole use induces hypergastrinemia, and gastrin has a trophic effect on pancreatic islet cells that could theoretically stimulate insulin secretion — a plausible adverse-direction link. On the other hand, animal studies show omeprazole *combined with* GLP-1 agonists (exendin-4) improves insulin sensitivity — a plausible therapeutic-direction link, but only in combination, not as monotherapy. No identified trial or study directly tests "omeprazole treats hyperinsulinism"; the trials in this evidence set use omeprazole only as a background drug or CYP2C19 probe. The TxGNN score of 0.0 itself indicates the model does not meaningfully support this pairing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01654549](https://clinicaltrials.gov/study/NCT01654549) | Phase 2 | Completed | 40 | H. pylori eradication effect on liver fat in non-diabetic NAFLD; omeprazole not the intervention (Grade C) |
| [NCT02291666](https://clinicaltrials.gov/study/NCT02291666) | Phase 4 | Completed | 73 | T2D effects on CYP450 activity; omeprazole used only as a CYP2C19 probe drug (Grade C) |
| [NCT01759628](https://clinicaltrials.gov/study/NCT01759628) | Phase 2 | Completed | 100 | H. pylori eradication effect on liver function in NAFLD; omeprazole not the intervention (Grade C) |
| [NCT01712711](https://clinicaltrials.gov/study/NCT01712711) | Phase 2 | Completed | 40 | H. pylori eradication effect on liver fat in diabetic NAFLD patients; omeprazole not the intervention (Grade C) |
| [NCT01876108](https://clinicaltrials.gov/study/NCT01876108) | Phase 2 | Completed | 100 | H. pylori eradication effect on liver fat in NAFLD; weak relevance to hyperinsulinism (Grade C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38884019](https://pubmed.ncbi.nlm.nih.gov/38884019/) | 2024 | Cohort/Observational | BioMed Research International | Long-term omeprazole induces hypergastrinemia and alters glucose homeostasis and pancreatic gene expression in mice |
| [22830490](https://pubmed.ncbi.nlm.nih.gov/22830490/) | 2013 | Animal study (db/db mice) | Journal of Diabetes | Omeprazole enhances anti-obesity/antidiabetic effects of exendin-4 in db/db mice |
| [24145087](https://pubmed.ncbi.nlm.nih.gov/24145087/) | 2013 | Animal study | Pharmacological Reports | Omeprazole + GLP-1 agonist combination improves insulin sensitivity and hepatic antioxidant activity in type 1 diabetic mice |
| [28780229](https://pubmed.ncbi.nlm.nih.gov/28780229/) | 2017 | Cohort | Diabetes & Metabolic Syndrome | H. pylori eradication effects on metabolic syndrome parameters in functional dyspepsia; omeprazole not the primary variable |
| [27480449](https://pubmed.ncbi.nlm.nih.gov/27480449/) | 2016 | RCT (H. pylori eradication, not omeprazole efficacy) | Nutrition, Metabolism and Cardiovascular Diseases | RCT of H. pylori eradication effect on glucose homeostasis in T2D patients |
| [22389003](https://pubmed.ncbi.nlm.nih.gov/22389003/) | 2014 | Case Report | Acta Diabetologica | Esomeprazole-induced transient diabetes/hepatitis; illustrates liver inflammation's role in insulin resistance |
| [18028533](https://pubmed.ncbi.nlm.nih.gov/18028533/) | 2007 | Methodology paper (no efficacy data) | BMC Gastroenterology | Study design paper for a GERD natural-history cohort; no direct relevance |

## Malaysia Market Information

The NPRA record confirms Omeprazole holds **45 active registrations** and is currently marketed ("已上市"), but detailed authorization records (license number, product name, dosage form, manufacturer, approved indication text) are not populated in this evidence pack and cannot be listed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for omeprazole-hyperinsulinism is 0.0, no clinical trial or publication directly tests this hypothesis, and the proposed mechanistic link is internally contradictory (hypergastrinemia can plausibly push glucose homeostasis in either direction). Evidence level L4 with decision stage S0 does not support advancing this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap — DG001)
- Confirmed mechanism of action data for omeprazole (currently High-severity data gap — DG002)
- A dedicated preclinical or clinical study testing omeprazole monotherapy (not combination or background-drug use) on insulin secretion/hyperinsulinism endpoints
- Resolution of the directional conflict between the hypergastrinemia/insulin-trophic pathway and the GLP-1-combination insulin-sensitizing pathway before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

