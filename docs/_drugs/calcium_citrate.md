---
layout: default
title: Calcium Citrate
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 4
---

# Calcium Citrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the **txgnn-pipeline** domain skill isn't a fit here since this is a one-off report-generation task fully specified by the v5 prompt itself (not model training/deployment work), so I'm producing the report directly per the instructions.

A few things worth flagging before the report: the Evidence Pack's `taiwan_regulatory.licenses` array contains 5 entries but **every field is an empty string** — there's no usable license number, product name, dosage form, or indication text to populate the "Original Indication" or "Malaysia Market Information" tables. I've followed the "don't fabricate" rule and stated that gap explicitly rather than inventing values. I also pulled forward the `repurposing_rationale.mechanistic_link` text (which candidly flags this as a likely knowledge-graph string-collision artifact around "citrate") since it's directly relevant to the Hold recommendation and the CLAUDE.md rule against guessing.

---

# Calcium Citrate: From Calcium Supplementation to Hemoglobinopathy

## One-Sentence Summary

> Calcium Citrate (DrugBank DB11093) is a calcium mineral supplement marketed in Malaysia under 48 NPRA registrations, though no specific approved-indication text or mechanism-of-action data is currently available in this evidence pack.
> The TxGNN model's top prediction suggests possible relevance to **Hemoglobinopathy**, with a **99.37% confidence score**, but this is currently supported by only **4 publications** (mostly involving unrelated citrate-containing drugs) and **0 clinical trials**.
> Evidence quality is the lowest tier (L5), and the evidence review itself flags this prediction as likely a knowledge-graph artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current NPRA registration data (all `approved_indication_text` fields are empty); Calcium Citrate is generically classified as an oral calcium supplement |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 48 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Calcium Citrate is not currently available (data gap DG002, High severity). Based on general pharmacological classification, Calcium Citrate is a calcium salt formulation used as an oral calcium supplement — typically for calcium deficiency, adjunct osteoporosis prevention, or correction of hypocalcemia. Because the original approved-indication text was not populated in the current Malaysia NPRA extract (data gap, Blocking severity — see DG001 below), a direct textual comparison between the original and predicted indications cannot be made at this time.

More importantly, the evidence review itself casts doubt on the mechanistic plausibility of this specific prediction. Although TxGNN assigns hemoglobinopathy a very high confidence score (99.37%), no identifiable direct pathway links calcium citrate supplementation to hemoglobinopathies such as sickle cell disease or thalassemia. Three of the four supporting publications concern structurally unrelated compounds that merely share the word "citrate" in their name — cetiedil citrate and sildenafil citrate — or describe citrate's role as an anticoagulant during erythrapheresis, not calcium citrate acting as a therapeutic agent. This pattern is consistent with a string/embedding co-occurrence artifact in the knowledge graph (multiple unrelated "citrate"-named drugs clustering near hemoglobinopathy-related nodes), rather than a biologically grounded repurposing hypothesis.

The other three candidate indications in this evidence pack (myocardial infarction, thrombotic disease, and a chromosomal deletion syndrome) show a similar pattern — high TxGNN scores without a coherent, unidirectional mechanistic story (see "Other Candidate Predictions" below). Taken together, this suggests the current prediction set for Calcium Citrate should be treated as hypothesis-generating only, not as a basis for further clinical development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15820939](https://pubmed.ncbi.nlm.nih.gov/15820939/) | 2005 | Clinical study (unrelated drug: sildenafil citrate) | Haematologica | Reports sildenafil citrate (a PDE5 inhibitor, not calcium citrate) for pulmonary hypertension in thalassemia/sickle cell disease patients |
| [18067651](https://pubmed.ncbi.nlm.nih.gov/18067651/) | 2007 | Cohort/Case series | Transfusion Medicine | Examines QTc interval changes during erythrapheresis (a citrate-anticoagulated blood-separation procedure) in sickle cell disease patients; does not test calcium citrate as a treatment |
| [23050671](https://pubmed.ncbi.nlm.nih.gov/23050671/) | 2013 | Animal study | Drug and Chemical Toxicology | Investigates iron uptake pathways in β-thalassemic mouse cardiomyocytes; concludes uptake is not calcium-channel mediated, i.e., a negative finding for calcium-pathway relevance |
| [3119675](https://pubmed.ncbi.nlm.nih.gov/3119675/) | 1987 | In vitro study (unrelated drug: cetiedil citrate) | Journal of Clinical Pathology | Tests cetiedil citrate (an unrelated vasoactive drug) and oxpentifylline on dehydrated sickle erythrocyte deformability in vitro |

---

## Malaysia Market Information

Individual product-level registration details (license numbers, product names, manufacturers, dosage forms, and approved-indication text) were not populated in the current NPRA data extract for any of the 5 sampled licenses. Only aggregate figures are available from NPRA: **48 total registrations** and a **marketed** status (see Quick Overview above). Retrieving the underlying label PDFs would be required to complete this table (see data gap DG001 in the Conclusion below).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other Candidate Predictions

For completeness, three additional TxGNN predictions were reviewed alongside hemoglobinopathy. None currently support a decision beyond Hold:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Caveat |
|------|----------------------|-------------|-----------------|-----------------|------------|
| 2 | Myocardial Infarction | 99.18% | L4 | Hold | Clinical trials involve IV calcium during cardiac surgery/dialysis, not oral calcium citrate supplementation; some cited literature raises a cardiovascular *risk* signal for calcium supplements rather than benefit |
| 3 | Partial deletion of short arm of chromosome 16 (16p−) | 99.09% | L5 | Hold | Zero trials, zero literature; a chromosomal structural disorder with no known link to calcium metabolism — likely a knowledge-graph false positive |
| 4 | Thrombotic Disease | 99.07% | L4 | Hold | Supporting literature concerns citrate as a regional *anticoagulant* (chelating calcium) — the opposite mechanistic direction from calcium *supplementation*, which theoretically promotes coagulation; internally contradictory signal |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hemoglobinopathy) sits at the lowest evidence tier (L5 — model prediction only), with zero clinical trials and literature support that traces back to unrelated "citrate"-named drugs rather than calcium citrate itself, suggesting the TxGNN score is likely an embedding/string-collision artifact rather than a genuine signal. Separately, a **Blocking**-severity data gap (missing TFDA/NPRA label warnings and contraindications, DG001) means this candidate cannot yet even complete an initial safety screen (S1), independent of the efficacy question.

**To proceed, the following is needed:**
- Retrieve the official product label/insert warnings and contraindications for Malaysia-registered calcium citrate products (DG001, Blocking — currently blocks S1 safety screening)
- Obtain detailed mechanism-of-action data from DrugBank or another authoritative pharmacology source (DG002, High)
- Confirm the original approved indication(s) by re-querying NPRA with complete field extraction (current license records returned empty indication text)
- Run a targeted, disambiguated literature search on "calcium citrate" AND "sickle cell disease"/"thalassemia" (excluding unrelated citrate-salt drugs) to determine whether any genuine signal exists beneath the apparent knowledge-graph artifact
- If any candidate is advanced, prioritize resolving the internally contradictory mechanistic direction seen in the thrombotic disease prediction before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

