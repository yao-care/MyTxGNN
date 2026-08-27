---
layout: default
title: Calcifediol
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 4
---

# Calcifediol
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

Using the given v5 report‑prompt spec directly (it is itself the complete, self‑contained instruction set for this task — no other skill covers "write a repurposing evaluation report from a supplied Evidence Pack JSON"). Below is the report.

Two things worth flagging before the report itself, because they materially affect how it should be read:

1. **`predicted_indications[0]` ("obsolete vitamin D deficiency") is not a genuine new indication.** The pack's own `repurposing_rationale.mechanistic_link` for rank 1 states this outright: correcting vitamin D deficiency *is* calcifediol's core approved pharmacology, not a TxGNN "repurposing" signal. It also carries zero trial/literature evidence in this pack, which is inconsistent with the `L1` evidence-level label attached to it (L1 requires ≥2 completed Phase 3 RCTs). I did not silently transcribe that inconsistency — it's called out explicitly below.
2. Because this is a **multi-candidate pack** (`candidate_id: TW-DB00146-multi`, 4 ranked predictions), I extended the single-indication template with a comparison table and per-candidate subsections rather than reporting only rank 1 — otherwise the report would omit the only three candidates that are actually novel.

---

# Calcifediol: From Vitamin D Deficiency to Renal Tubular Acidosis, Hereditary Hypophosphatemic Rickets, and Vitamin D-Dependent Rickets

## One-Sentence Summary

> Calcifediol (25-hydroxyvitamin D3) is the principal circulating storage form of vitamin D and the direct precursor of active 1,25-dihydroxyvitamin D3; its approved use is correcting vitamin D deficiency/insufficiency.
> The TxGNN model's top-ranked output (**obsolete vitamin D deficiency**, 99.99%) simply restates that existing approved use rather than proposing a new one. The three genuine repurposing candidates it also surfaced — **Renal Tubular Acidosis**, **Hereditary Hypophosphatemic Rickets**, and **Vitamin D-Dependent Rickets** — are supported by **2 low-relevance clinical trials** and **31 publications** (predominantly case reports and mechanism studies), with evidence strength ranging from cautionary to genuinely mechanistically plausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin D deficiency/insufficiency (inferred from established pharmacology; NPRA license indication text was not available in this evidence pack) |
| Predicted New Indication (rank 1, per TxGNN) | Obsolete vitamin D deficiency — **see Data Quality Note below; this is not a novel indication** |
| TxGNN Prediction Score (rank 1) | 99.99% |
| Evidence Level (rank 1, as reported) | L1 *(flagged as inconsistent — see note)* |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision (overall) | **Hold** — blocked pending safety label data (see Conclusion) |

**⚠️ Data Quality Note:** The rank-1 prediction ("obsolete vitamin D deficiency") returned **zero** clinical trials and **zero** literature hits in this pack, yet is labeled Evidence Level L1 (which by the rules below requires ≥2 completed Phase 3 RCTs). This label almost certainly reflects the drug's real-world, well-established approved-use evidence sitting outside the scope of the collectors used here — not new trial data supporting a repurposing claim. Treat this candidate as **already-approved use, not a new indication**, and rely on the three candidates below for actual repurposing assessment.

### Candidate Comparison (all 4 predictions in this pack)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|----------------|-----------------|
| 1 | Obsolete vitamin D deficiency *(not novel — see note)* | 99.99% | L1* | S3 | Proceed with Guardrails* |
| 2 | Renal Tubular Acidosis | 99.86% | L4 | S1 | Hold |
| 3 | Hereditary Hypophosphatemic Rickets | 99.76% | L3 | S2 | Research Question |
| 4 | Vitamin D-Dependent Rickets | 99.18% | L4 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this pack (`original_moa: [Data Gap]`). Based on known pharmacology: **calcifediol is the hepatic hydroxylation product of vitamin D3** — the major circulating storage metabolite — and serves as the direct substrate for renal **1α-hydroxylase (CYP27B1)**, which converts it into the active hormone **1,25-dihydroxyvitamin D3 (calcitriol)**. Its efficacy in correcting vitamin D deficiency is well established; whether that substrate-supply role extends usefully to the three predicted conditions depends heavily on whether each condition's underlying defect sits *upstream* or *downstream* of calcifediol in this pathway.

**Renal Tubular Acidosis (rank 2):** The mechanistic link here is indirect. Proximal RTA can be *associated with* osteomalacia caused by vitamin D deficiency (as in the case reports below), and calcifediol would treat that secondary bone disease — but it does not address the tubular acid-base transport defect that defines RTA itself. This is treating a comorbidity, not the indication.

**Hereditary Hypophosphatemic Rickets / XLH (rank 3):** In X-linked hypophosphatemia, excess FGF23 suppresses (but does not eliminate) renal 1α-hydroxylase activity and causes renal phosphate wasting. Because the hydroxylase enzyme is only suppressed rather than absent, raising the 25(OH)D substrate pool with calcifediol has a plausible, if secondary, rationale — though standard practice still favors active-form analogues (calcitriol/alfacalcidol) plus phosphate supplementation, with calcifediol's role being adjunctive at best.

**Vitamin D-Dependent Rickets (rank 4):** This candidate carries a genuine **mechanistic contradiction warning**. VDDR type 1 (classic) is caused by CYP27B1 (1α-hydroxylase) deficiency — the very enzyme calcifediol depends on for activation — so raising 25(OH)D levels would not be expected to help. VDDR type 2 is a vitamin D receptor defect, unresponsive to any form of vitamin D. However, one important nuance the pack's rationale text omits: **VDDR type 1B** (PMID 28548312) is caused by *CYP2R1 (25-hydroxylase)* deficiency — the hepatic enzyme that makes calcifediol *from* vitamin D3 in the first place. In that specific subtype, directly administering calcifediol would bypass the defective step entirely, which is mechanistically rational, unlike VDDR-1/-2. A 1978 case report (PMID 233695) is also notable: a familial 1,25(OH)2D-resistance syndrome was corrected with high-dose 25-hydroxyvitamin D, i.e., calcifediol. These findings suggest the "Hold" recommendation may be too blunt for the VDDR1B subgroup specifically, even though it is appropriate for VDDR type 1/2 as a whole.

---

## Clinical Trial Evidence

### Renal Tubular Acidosis / Hereditary Hypophosphatemic Rickets
Currently no related clinical trials registered.

### Vitamin D-Dependent Rickets

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03265483](https://clinicaltrials.gov/study/NCT03265483) | N/A | Completed | 180 | Studied magnesium supplementation's effect on vitamin D resistance; intervention was magnesium, not calcifediol. **Relevance graded C** — indirect, does not test calcifediol. |
| [NCT05214040](https://clinicaltrials.gov/study/NCT05214040) | N/A | Not yet recruiting | 300,000 | Epidemiological survey of vitamin D insufficiency in hospitalized inpatients; not a VDDR treatment trial and not calcifediol-specific. **Relevance graded C**. |

Neither trial directly tests calcifediol as a VDDR treatment — both are included here for transparency but should not be read as supportive trial evidence.

---

## Literature Evidence

### Renal Tubular Acidosis (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11372811](https://pubmed.ncbi.nlm.nih.gov/11372811/) | 2001 | Case Report | Southern Medical Journal | Proximal RTA in a vitamin-D-deficient quadriplegic patient with limited sun exposure, low bicarbonate, and osteomalacia. |
| [2737043](https://pubmed.ncbi.nlm.nih.gov/2737043/) | 1989 | Methodology study | Zhonghua Nei Ke Za Zhi | Assay validation for serum 25(OH)D; found markedly low levels in osteomalacia/rickets patients vs. controls. |
| [3671929](https://pubmed.ncbi.nlm.nih.gov/3671929/) | 1987 | Case Report | Revue Médicale de Bruxelles | Proximal tubular acidosis associated with deficiency osteomalacia in adults. |

### Hereditary Hypophosphatemic Rickets (Rank 3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Overview of rickets types and treatment with vitamin D and its analogues, including active metabolites. |
| [6253520](https://pubmed.ncbi.nlm.nih.gov/6253520/) | 1980 | Mechanism/Cohort | J Clin Investigation | Investigated the role of 1,25(OH)2D3 in XLH pathogenesis and treatment; found renal phosphate wasting alone does not explain the full disease spectrum. |
| [2804451](https://pubmed.ncbi.nlm.nih.gov/2804451/) | 1989 | Cohort | Bone and Mineral | Oral phosphate loading blunts the renal 25(OH)D-1α-hydroxylase response in XLH patients vs. normal controls. |
| [6976353](https://pubmed.ncbi.nlm.nih.gov/6976353/) | 1982 | Cohort | J Clin Endocrinol Metab | Evaluated efficacy of vitamin D2 plus oral phosphorus therapy in XLH and osteomalacia. |
| [22205508](https://pubmed.ncbi.nlm.nih.gov/22205508/) | 2012 | Case Report | Pediatric Nephrology | Linear nevus sebaceous syndrome with hypophosphatemic rickets and elevated FGF-23. |
| [20688626](https://pubmed.ncbi.nlm.nih.gov/20688626/) | 2010 | Case Report | Hormones (Athens) | Cinacalcet used for secondary hyperparathyroidism in XLH; standard treatment described as long-term phosphate + calcitriol. |
| [6097438](https://pubmed.ncbi.nlm.nih.gov/6097438/) | 1984 | Mechanism study | Endocrinologia Japonica | 1,25(OH)2D response to PTH stimulation studied in hypoparathyroid and renal tubular disorder patients, including hypophosphatemic vitamin-D-resistant rickets. |
| [6893581](https://pubmed.ncbi.nlm.nih.gov/6893581/) | 1980 | Animal study | Endocrinology | Abnormal vitamin D metabolism characterized in the X-linked hypophosphatemic (Hyp) mouse model. |
| [6600222](https://pubmed.ncbi.nlm.nih.gov/6600222/) | 1983 | Mechanism study | Endocrinology | Abnormal 24-hydroxylation of 25(OH)D in the Hyp mouse model, relevant to calcifediol catabolism in XLH. |
| [23026218](https://pubmed.ncbi.nlm.nih.gov/23026218/) | 2013 | Case Report | Gene | Enteral calcium infusion used successfully in a hereditary vitamin-D-resistant rickets case (note: this describes VDDR-II biology rather than XLH). |

### Vitamin D-Dependent Rickets (Rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9316302](https://pubmed.ncbi.nlm.nih.gov/9316302/) | 1997 | Review | Acta Paediatrica Japonica | Core review distinguishing VDDR type I (1α-hydroxylase deficiency) from type II (VDR defect) and their respective treatments. |
| [2982764](https://pubmed.ncbi.nlm.nih.gov/2982764/) | 1985 | Case Series | Israel J Medical Sciences | VDDR types I and II: diagnostic values of serum vitamin D metabolites and differential response to therapy. |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Case Report/Review | J Bone Mineral Research | Describes VDDR **type 1B**, caused by CYP2R1 (25-hydroxylase) deficiency — the enzyme that produces calcifediol itself, making this subtype mechanistically distinct from type 1/2. |
| [233695](https://pubmed.ncbi.nlm.nih.gov/233695/) | 1978 | Case Report | J Clin Endocrinol Metab | Familial syndrome of decreased sensitivity to 1,25(OH)2D; calcium malabsorption was correctable with **high-dose 25-hydroxyvitamin D (calcifediol)**. |
| [22145480](https://pubmed.ncbi.nlm.nih.gov/22145480/) | 2011 | Case Report | J Pediatr Endocrinol Metab | Two VDDR cases (type 1 and type 2) illustrating diagnostic and therapeutic difficulties. |
| [15972816](https://pubmed.ncbi.nlm.nih.gov/15972816/) | 2005 | Mechanism study | J Biological Chemistry | Structural/binding-site analysis of CYP27B1 mutations causing VDDR type 1. |
| [11416220](https://pubmed.ncbi.nlm.nih.gov/11416220/) | 2001 | Animal study | PNAS | CYP27B1 (1α-hydroxylase) knockout mouse model reproduces skeletal, reproductive, and immune dysfunction of VDDR type 1. |
| [6285251](https://pubmed.ncbi.nlm.nih.gov/6285251/) | 1982 | Case Report | Pädiatrie und Pädologie | Transient vitamin-D-dependent rickets case treated with 1α-hydroxycholecalciferol, with differential diagnosis discussion. |
| [26483391](https://pubmed.ncbi.nlm.nih.gov/26483391/) | 2015 | Review/Case Report | BMJ Case Reports | Rachitic lung as a life-threatening respiratory complication of severe rickets. |
| [8914979](https://pubmed.ncbi.nlm.nih.gov/8914979/) | 1996 | Basic science | FEBS Letters | Vitamin D3 metabolites elicit calcium responses in monocyte-derived macrophages from VDDR type II patients. |

---

## Malaysia Market Information

NPRA market status is **Marketed (已上市)** with **4 registered licenses**. However, this evidence pack does not contain license-level detail (authorization numbers, product names, dosage forms, or approved indication text) — all four license records were returned empty. This data gap should be closed by pulling the NPRA product register directly before any regulatory-facing use of this report.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DDI query status: not found, 0 interactions). Note that `meta.data_gaps` flags the missing NPRA label warnings/contraindications (DG001) as **Blocking severity**, explicitly because it prevents safety pre-screening (S1) — this is not a minor omission and should be resolved before any candidate advances (see below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 prediction is not a genuine repurposing signal — it restates the drug's existing approved indication, and its "L1" evidence label is inconsistent with the zero trials/literature actually returned for it in this pack.
- Of the three genuine candidates, two (Renal Tubular Acidosis, Vitamin D-Dependent Rickets) are recommended **Hold** by the model's own scoring, and the mechanistic case for VDDR types 1 and 2 is actually contradictory to calcifediol's mechanism (though the VDDR-1B subtype may be an exception worth separate evaluation).
- A **Blocking**-severity data gap (missing NPRA label warnings/contraindications) prevents even a basic S1 safety screen for any candidate, per the evidence pack's own gap log.

**To proceed, the following is needed:**
- Resolve DG001: obtain the NPRA package insert (warnings, contraindications) for calcifediol to complete an S1 safety screen.
- Resolve DG002: obtain confirmed DrugBank mechanism-of-action data to validate the substrate-reservoir reasoning used above.
- Clarify/correct the rank-1 evidence-level scoring anomaly (L1 label with zero supporting trials/literature) before this candidate is used in any decision document.
- If pursuing Hereditary Hypophosphatemic Rickets (rank 3, the strongest genuine candidate at "Research Question" stage), commission a targeted literature/mechanism review distinguishing calcifediol's adjunctive role from standard-of-care active-vitamin-D analogues.
- If VDDR is pursued further, restrict scope to the VDDR type 1B (CYP2R1-deficient) subgroup rather than VDDR broadly, given the mechanistic contradiction for types 1 and 2.
- Populate the missing NPRA license-level fields (product names, dosage forms, indication text) for the 4 registered products.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

