---
layout: default
title: Testosterone
parent: Low Evidence (L4-L5)
nav_order: 643
evidence_level: L5
indication_count: 5
---

# Testosterone
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **5** 
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

# Testosterone: From Androgen Deficiency to Congenital Hypogonadotropic Hypogonadism

## One-Sentence Summary

Testosterone is the reference androgen replacement compound; the Malaysia registry (NPRA) confirms it is marketed under 4 licenses, but the specific approved indication text was not captured in this evidence pack.
The TxGNN model ranks **Congenital Hypogonadotropic Hypogonadism (CHH)** as its top predicted indication, supported by **15 clinical trials** and **19 publications** — though the reported TxGNN score of 0.00% for this rank appears to be a data artifact rather than a true confidence value.
Mechanistically this is not a distant "new use": CHH is a testosterone-deficiency disorder, and testosterone replacement is the expected direct therapy for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in registry data (all 4 NPRA license records have blank indication text) |
| Predicted New Indication | Congenital Hypogonadotropic Hypogonadism |
| TxGNN Prediction Score | 0.00% (reported as 0.0 — likely a scoring/data pipeline issue, see caveat below) |
| Evidence Level | L3 (completed Phase 4 comparative/observational studies + guideline-level reviews; no completed Phase 3 RCTs specific to this indication) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

**Caveat:** All five ranked predictions in this evidence pack (rank 1–5) carry an identical `txgnn.score` of 0.0, which is inconsistent with a meaningful ranked-confidence output. This should be verified against the raw TxGNN scoring pipeline before the score is used in any go/no-go calculation.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Testosterone is not available in this evidence pack (`original_moa: [Data Gap]`), and no original indication text was captured from the Malaysia registry. Based on general pharmacological classification, Testosterone is an endogenous androgen and the reference agent for androgen/testosterone replacement therapy.

Congenital Hypogonadotropic Hypogonadism is, by definition, a condition of insufficient endogenous testosterone production caused by hypothalamic-pituitary dysfunction (impaired GnRH/gonadotropin signaling). Exogenous testosterone replacement is therefore the direct, mechanistically expected corrective therapy for this deficiency state — this is closer to a **label-consistent use** than a novel off-target repurposing signal. That distinction matters for evidence interpretation: the clinical trial and literature base below largely documents dosing, formulation, and downstream metabolic/bone effects of testosterone therapy in CHH patients, rather than establishing efficacy in a previously unrelated disease.

Because `original_indications` is empty and MOA is a data gap, this review cannot confirm whether CHH/androgen deficiency is already Testosterone's labeled indication in the Malaysia registry — that confirmation is one of the key outstanding items before this can be scored as genuine repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01454011](https://clinicaltrials.gov/study/NCT01454011) | Phase 4 | Completed | 140 | Compared HDL cholesterol subgroups in CHH patients vs. healthy controls; assessed effect of testosterone replacement on HDL subgroup distribution |
| [NCT02111434](https://clinicaltrials.gov/study/NCT02111434) | Phase 4 | Completed | 150 | Effect of testosterone treatment on visceral adiposity index and triglyceride/HDL ratio in CHH |
| [NCT02111473](https://clinicaltrials.gov/study/NCT02111473) | Phase 4 | Completed | 49 | Effect of testosterone replacement on FGF-23, endothelial dysfunction, and bone mineral metabolism in CHH |
| [NCT02171390](https://clinicaltrials.gov/study/NCT02171390) | Phase 4 | Completed | 130 | Endothelial dysfunction, inflammation, and insulin resistance in CHH; compared two testosterone replacement regimens |
| [NCT02880280](https://clinicaltrials.gov/study/NCT02880280) | Phase 4 | Unknown | 40 | hMG + hCG vs. hCG alone for therapeutic efficacy in adolescent boys with CHH |
| [NCT03687606](https://clinicaltrials.gov/study/NCT03687606) | Phase 4 | Unknown | 210 | Long-term hCG vs. hCG+hMG efficacy/safety in isolated hypogonadotropic hypogonadism (open RCT) |
| [NCT00064987](https://clinicaltrials.gov/study/NCT00064987) | Phase 2 | Terminated | 19 | Role of FSH in gonadal development in men with IHH/Kallmann syndrome |
| [NCT00392756](https://clinicaltrials.gov/study/NCT00392756) | Phase 1 | Completed | 624 | Gonadotropin pulsation patterns in reversal of hypogonadotropic hypogonadism (Kallmann/IHH) |
| [NCT00623116](https://clinicaltrials.gov/study/NCT00623116) | N/A | Unknown | 50 | Epidemiology, clinical and genetic characterization of Kallmann syndrome in Finland |
| [NCT01511588](https://clinicaltrials.gov/study/NCT01511588) | N/A | Completed | 111 | Role of gonadotropin pulsations in regulation of puberty and fertility, including hypogonadal subjects |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31147553](https://pubmed.ncbi.nlm.nih.gov/31147553/) | 2019 | Review | Nature Reviews Disease Primers | Comprehensive review of paediatric and adult-onset male hypogonadism, including CHH pathophysiology and management |
| [35353710](https://pubmed.ncbi.nlm.nih.gov/35353710/) | 2022 | Clinical Practice Guideline | European Journal of Endocrinology | Endo-ERN guideline on pubertal induction and adult sex hormone replacement for congenital pituitary/gonadal hormone deficiency |
| [32445446](https://pubmed.ncbi.nlm.nih.gov/32445446/) | 2021 | Review | Current Pharmaceutical Design | Review of gonadotropin treatment for male hypogonadotropic hypogonadism; testosterone as treatment of choice when fertility not required |
| [38683021](https://pubmed.ncbi.nlm.nih.gov/38683021/) | 2024 | Review | J Clin Res Pediatr Endocrinol | Current perspective on delayed puberty management, including hypogonadotropic hypogonadism classification |
| [35674463](https://pubmed.ncbi.nlm.nih.gov/35674463/) | 2022 | Review | Expert Opinion on Pharmacotherapy | Pharmacological considerations for male congenital hypogonadotropic hypogonadism |
| [32748610](https://pubmed.ncbi.nlm.nih.gov/32748610/) | 2020 | Review | Minerva Pediatrica | Review of delayed puberty diagnosis and management approach |
| [24815726](https://pubmed.ncbi.nlm.nih.gov/24815726/) | 2014 | Review | Annales d'Endocrinologie | CHH and Kallmann syndrome as models for studying hormonal regulation of testicular endocrine function |
| [32010061](https://pubmed.ncbi.nlm.nih.gov/32010061/) | 2019 | Review | Frontiers in Endocrinology | Review of hypogonadism and cryptorchidism, androgen role in testicular descent |
| [38437850](https://pubmed.ncbi.nlm.nih.gov/38437850/) | 2024 | Observational (cross-sectional, multi-centre) | The Lancet Diabetes & Endocrinology | Cross-sectional study of six international referral centres identifying predictors/classes of CHH reversal |
| [30851011](https://pubmed.ncbi.nlm.nih.gov/30851011/) | 2019 | Observational study | Andrology | Testosterone replacement in CHH maintains bone density but has limited osteoanabolic effect |

---

## Malaysia Market Information

Malaysia (NPRA) market status is confirmed as **already marketed** with **4 total license records**. However, none of the individual license fields (license number, product name, dosage form, manufacturer, approved indication text) were populated in this evidence pack — all 4 entries returned blank strings. This is a data-completeness gap in the NPRA extract, not evidence that the licenses lack this information; the underlying license records should be re-queried/re-parsed before this section can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** This evidence pack flags TFDA/NPRA warning and contraindication data as a **Blocking** data gap (DG001) — its absence prevents this candidate from entering the S1 preliminary safety assessment stage. No drug-drug interaction records were found (`ddi.query_status: not_found`, 0 interactions returned), which should not be read as "no interactions exist," only that none were retrieved by this query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (CHH) is mechanistically plausible almost by definition — testosterone is the deficient hormone in this condition — but the underlying evidence pack has a **Blocking** safety data gap (TFDA/NPRA warnings and contraindications, DG001) that prevents any preliminary safety screening, and an anomalous 0.00% TxGNN score that undermines confidence in the ranking itself. Until these are resolved, this cannot be progressed past Hold regardless of the clinical trial/literature volume.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap DG001)
- DrugBank mechanism of action data (High priority gap DG002)
- Complete NPRA license record details (license numbers, product names, dosage forms, approved indication text) for the 4 existing registrations
- Verification of the TxGNN scoring pipeline — all 5 ranked predictions show an identical 0.0 score, which needs explanation before being used in decision-making
- Confirmation of Testosterone's currently labeled indication(s) in Malaysia, to determine whether CHH is already covered by the existing label rather than a true repurposing candidate
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

