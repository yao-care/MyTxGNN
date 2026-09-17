---
layout: default
title: Propylthiouracil
parent: Low Evidence (L4-L5)
nav_order: 579
evidence_level: L5
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **3** 
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

# Propylthiouracil (PTU): From Hyperthyroidism to Three Predicted Thyroid-Related Indications

## One-Sentence Summary

> Propylthiouracil (PTU, DB00550) is a thionamide antithyroid drug historically used to treat **hyperthyroidism (Graves' disease)**. TxGNN identifies three candidate new indications — **resistance to thyroid hormone (TRβ mutation)** (score 99.66%), **neonatal thyrotoxicosis** (score 99.40%), and **hyperthyroxinemia** (score 99.08%) — with evidence quality ranging from a single Phase 3 trial + 20 publications (neonatal thyrotoxicosis, L2) down to mechanism-only literature (the other two, L4). A **Blocking data gap** on Malaysia NPRA labeling (warnings/contraindications) currently prevents any of the three from clearing initial safety screening (S1).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism (Graves' disease) — *not captured in the NPRA license text on file; based on PTU's established pharmacology* |
| Malaysia Market Status | ✓ Marketed (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision (overall) | **Hold** (blocked by missing TFDA/NPRA safety data — see below) |

### Predicted Indications Compared

| Rank | Predicted New Indication | TxGNN Score | Evidence Level | Decision Stage | Per-Indication Recommendation |
|---|---|---|---|---|---|
| 1 | Resistance to thyroid hormone (TRβ mutation) | 99.66% | L4 | S0 | Hold |
| 2 | Neonatal thyrotoxicosis | 99.40% | L2 | S2 | Proceed with Guardrails |
| 3 | Hyperthyroxinemia | 99.08% | L4 | S1 | Research Question |

---

## Why Is This Prediction Reasonable?

Detailed DrugBank MOA text is not available (data gap), but the mechanism is well characterized in the supporting literature: PTU inhibits **thyroid peroxidase (TPO)**, blocking iodide organification and iodotyrosine coupling, and also inhibits **peripheral deiodinase type 1**, reducing T4→T3 conversion. Both actions lower circulating thyroid hormone levels.

- **Neonatal thyrotoxicosis** is mechanistically the strongest fit: it typically results from transplacental transfer of maternal TSH-receptor-stimulating antibodies (Graves' disease) driving fetal/neonatal overproduction of T3/T4. PTU's hormone-synthesis-blocking action is already the established clinical approach for thyrotoxicosis in pregnancy (PTU preferred in the first trimester due to methimazole's teratogenicity risk), making this less a novel repurposing than a documented extension of existing practice.
- **Resistance to thyroid hormone (TRβ mutation)** and **hyperthyroxinemia** are mechanistically more indirect. Both conditions originate at the **receptor/binding level** (TRβ mutation causing reduced tissue responsiveness with impaired negative feedback, or elevated circulating T4 from causes such as RTH, MCT8 deficiency, or familial dysalbuminemic hyperthyroxinemia) rather than from excess hormone *synthesis*. Lowering hormone production with PTU does not correct the underlying receptor defect, and TRα-dominant tissues (heart, bone) may remain relatively unaffected — so a therapeutic benefit is plausible but not guaranteed. One case report (PMID 18334584) does show symptomatic benefit from PTU + L-thyroxine in an MCT8-mutation patient, offering a direct but single-case signal.

---

## Clinical Trial Evidence

### Resistance to Thyroid Hormone (TRβ mutation)
Currently no related clinical trials registered.

### Neonatal Thyrotoxicosis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03066076](https://clinicaltrials.gov/study/NCT03066076) | Phase 3 | Unknown | 60 | Randomized comparison of total thyroidectomy vs. thionamides (antithyroid drugs, incl. PTU-class) in Graves' ophthalmopathy patients; relevant to maternal-side thyrotoxicosis management but not designed for the neonatal population directly (relevance grade B) |

### Hyperthyroxinemia
Currently no related clinical trials registered.

---

## Literature Evidence

### Resistance to Thyroid Hormone (TRβ mutation) — 6 publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Review | Endocrinology | TRβ mutation causes dominant-negative effect on cardiac gene response to thyroid hormone |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Preclinical (mouse) | Endocrinology | TRβ mutant mouse model spontaneously develops follicular thyroid carcinoma |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Preclinical (mouse) | Oncogene | Thyroid hormone activates tumor proliferation in TRβ-mutant (PV) mouse model |
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case Report | Exp Clin Endocrinol Diabetes | TRβ mutation (P453A) identified in a Turkish family with RTH |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clinical Endocrinology | Neonatal thyrotoxicosis + maternal infertility linked to TRβ mutation (M313T); notes prior (ineffective) PTU treatment |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case Report | Endocrine Journal | De novo TRβ mutation (L330S) in a Thai patient previously treated with PTU under a mistaken thyrotoxicosis diagnosis |

### Neonatal Thyrotoxicosis — top 10 of 20 publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33349844](https://pubmed.ncbi.nlm.nih.gov/33349844/) | 2021 | Review | J Clin Endocrinol Metab | Testing/monitoring/treatment guidance for thyroid dysfunction in pregnancy |
| [31345521](https://pubmed.ncbi.nlm.nih.gov/31345521/) | 2019 | Review | Endocrinol Metab Clin North Am | PTU recommended in first trimester for high-risk Graves' disease, then transition to methimazole |
| [25747892](https://pubmed.ncbi.nlm.nih.gov/25747892/) | 2015 | Cohort | Thyroid | Gestational thyrotoxicosis, antithyroid drug use, and neonatal outcomes in an integrated health system |
| [32199749](https://pubmed.ncbi.nlm.nih.gov/32199749/) | 2020 | Review | Best Pract Res Clin Endocrinol Metab | Management approach for thyrotoxicosis during pregnancy |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Overview of hyperthyroidism in pregnancy and maternal/fetal risk |
| [6387489](https://pubmed.ncbi.nlm.nih.gov/6387489/) | 1984 | Review | N Engl J Med | Classic review of antithyroid drug pharmacology and mechanisms |
| [3271369](https://pubmed.ncbi.nlm.nih.gov/3271369/) | 1988 | Review | Rev Chil Pediatr | General review of hyperthyroidism (abstract unavailable) |
| [18558604](https://pubmed.ncbi.nlm.nih.gov/18558604/) | 2008 | Case Report | Endocr Pract | Persistent neonatal thyrotoxicosis from an activating TSHR mutation |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clinical Endocrinology | Neonatal thyrotoxicosis from TRβ mutation (M313T), prior maternal PTU exposure |
| [596245](https://pubmed.ncbi.nlm.nih.gov/596245/) | 1977 | Case Report/Cohort | Acta Med Scand | Postpartum exacerbation of hyperthyroidism linked to neonatal thyrotoxicosis |

*10 additional publications (mostly reviews/case reports on ATD use in pregnancy, e.g. PMID 36680759, 34335902, 25185644, 11298090) were deprioritized for this table but are available in the evidence pack.*

### Hyperthyroxinemia — top 10 of 13 publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7527990](https://pubmed.ncbi.nlm.nih.gov/7527990/) | 1994 | Review | Acta Med Austriaca | Overview of thyroxine excess in pregnancy |
| [2840057](https://pubmed.ncbi.nlm.nih.gov/2840057/) | 1988 | Cohort | Aust N Z J Med | PTU + potassium perchlorate combination for amiodarone-induced hyperthyroidism |
| [3097618](https://pubmed.ncbi.nlm.nih.gov/3097618/) | 1986 | Review | Pediatrics | Familial partial peripheral/pituitary resistance to thyroid hormone often misdiagnosed and mistreated with PTU |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Review | Endocrinology | TRβ mutation dominant-negative effect in cardiac tissue |
| [32101523](https://pubmed.ncbi.nlm.nih.gov/32101523/) | 2020 | Case Report | Endocrinol Diabetes Metab Case Rep | Familial dysalbuminemic hyperthyroxinemia complicating autoimmune thyroid disease management |
| [8574290](https://pubmed.ncbi.nlm.nih.gov/8574290/) | 1995 | Preclinical (mouse) | Endocrine Journal | Long-term PTU/thyroid hormone effects on lymphocyte subsets |
| [18334584](https://pubmed.ncbi.nlm.nih.gov/18334584/) | 2008 | Case Report | J Clin Endocrinol Metab | PTU + L-thyroxine combination benefits a patient with MCT8 mutation |
| [9436485](https://pubmed.ncbi.nlm.nih.gov/9436485/) | 1997 | Case Series | Annales d'Endocrinologie | Fetal hyperthyroidism from maternal TSH-receptor stimulating antibodies despite euthyroid mother |
| [16433073](https://pubmed.ncbi.nlm.nih.gov/16433073/) | 2005 | Preclinical (rat) | Neurosci Behav Physiol | Effects of thyroxine level changes on cataleptic freezing reactions in rats |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clinical Endocrinology | Neonatal thyrotoxicosis/TRβ mutation with prior PTU exposure |

---

## Malaysia Market Information

NPRA records confirm the drug is **marketed with 1 active registration**, but the license record on file has blank fields for authorization number, product name, dosage form, and approved indication text — these details still need to be retrieved directly from NPRA (see Conclusion).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all currently unavailable — flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The missing TFDA/NPRA package-insert data (warnings and contraindications) is a **Blocking** gap that prevents any of the three candidate indications from clearing initial safety screening (S1), regardless of how strong the underlying clinical/mechanistic evidence is. Neonatal thyrotoxicosis already has L2/S2-level support (an existing Phase 3 trial context plus 20 publications including cohort and review-tier evidence) and is closest to being actionable once safety data is filled in; the other two indications (RTH-beta, hyperthyroxinemia) remain mechanistically indirect (receptor-level pathology vs. PTU's hormone-synthesis-blocking action) and sit at L4 with single-case-level clinical signal.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA package insert (warnings, contraindications) — **Blocking (DG001)**
- Confirm PTU's mechanism of action from DrugBank/primary pharmacology sources (DG002)
- Complete NPRA license details (authorization number, product name, dosage form, approved indication text) — currently blank despite an active registration
- For neonatal thyrotoxicosis: formal relevance grading of the ~10 literature items still marked "pending" to firm up the existing L2/S2 assessment
- For RTH-beta and hyperthyroxinemia: endocrinology expert review of the receptor-vs-synthesis mechanistic mismatch before advancing beyond L4/Research Question
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

