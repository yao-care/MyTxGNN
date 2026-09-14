---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 3
---

# Probenecid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Probenecid: From Gout (Hyperuricemia) to Renal Hypouricemia

## One-Sentence Summary

Probenecid is a classic uricosuric agent long used to treat gout/hyperuricemia (and historically as an adjunct to prolong penicillin plasma levels). The TxGNN model predicts a link to **Renal Hypouricemia**, but the supporting literature (20 publications, no clinical trials) mostly describes probenecid as a **diagnostic challenge agent** used to characterize the urate-transporter defect in these patients, rather than as a treatment — an important distinction for interpreting this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout / hyperuricemia (uricosuric agent); note — Malaysia registration text is not populated in this evidence pack (see Data Gaps) |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 (observational case reports/series + 1 review; no RCTs, no clinical trials) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this evidence pack is not available (Data Gap DG002). Based on known pharmacology, probenecid inhibits the URAT1/OAT organic-anion transporters in the renal proximal tubule, blocking urate reabsorption and **increasing** urinary uric acid excretion — the mechanism it uses to lower serum urate in gout.

Renal hypouricemia is the opposite clinical picture: patients have **loss-of-function mutations in SLC22A12 (URAT1)**, causing excessive urate loss and abnormally low serum urate. Because probenecid acts on the same transporter, the literature link TxGNN is picking up is largely **diagnostic, not therapeutic** — multiple retrieved papers (e.g. PMID 854144, PMID 8302413, PMID 7099326) describe the classic "probenecid test," where a blunted uricosuric response to probenecid/pyrazinamide is used to subtype the tubular defect in renal hypouricemia, not to treat it.

This mechanistic mismatch does not necessarily invalidate the prediction (probenecid pharmacology is genuinely central to understanding and diagnosing renal hypouricemia, and shared URAT1 biology is a real link), but it means the current evidence base supports a **diagnostic/mechanistic association** far more than a **treatment indication**. This should be explicitly flagged before any further repurposing evaluation proceeds.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia etiology and workup for rheumatologists; covers renal hypouricemia as a major cause |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort study | J Am Soc Nephrol | Sequenced SLC22A12 in 32 Japanese renal hypouricemia patients; correlated URAT1 genotype with urate clearance phenotype |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Molecular Genetics and Metabolism | Overview of hereditary renal hypouricemia (HRH), SLC22A12/URAT1 loss-of-function as principal cause |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report + review | American Journal of Kidney Diseases | Case of exercise-induced acute renal failure in renal hypouricemia; discusses prevention strategies and reviews prior literature |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | American Journal of Kidney Diseases | Two brothers with hereditary renal hypouricemia and exercise-induced ARF |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case series | Archives of Internal Medicine | 7 maturity-onset diabetic patients with renal hypouricemia; increased pyrazinamide-suppressible urate clearance |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case series | Nephron | 14 Type 1 diabetics with renal hypouricemia vs. 14 controls; characterized uricosuric mechanisms |
| [9583212](https://pubmed.ncbi.nlm.nih.gov/9583212/) | 1998 | Case report | Acta Paediatrica Japonica | 10-year-old girl with exercise-induced ARF and renal hypouricemia |
| [8533596](https://pubmed.ncbi.nlm.nih.gov/8533596/) | 1995 | Case report | Acta Paediatrica Japonica | 15-year-old boy with renal hypouricemia and exercise-induced ARF; probenecid/pyrazinamide test used to characterize the tubular defect |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho (Japanese Journal of Clinical Medicine) | Classification of urate metabolism abnormalities, including renal hypouricemia subtypes |

(10 of 20 retrieved publications shown, prioritized by evidence type; remaining are additional case reports.)

---

## Malaysia Market Information

Detailed authorization records (license number, product name, dosage form, approved indication text) are not populated in this evidence pack — only the aggregate count (1 registration, marketed status) is available. Registration-level detail should be pulled from source before this candidate advances.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/NPRA label warnings and contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety (S1) evaluation can proceed, and no drug-drug interaction records were found in this pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap on label warnings/contraindications (DG001) prevents any safety assessment, and the supporting literature for renal hypouricemia is composed entirely of case reports/series describing probenecid as a **diagnostic probe** for the URAT1 defect rather than as a therapeutic agent — evidence quality and mechanistic direction do not currently support a repurposing case.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF parsed for warnings and contraindications (resolves DG001)
- Confirmed mechanism of action via DrugBank (resolves DG002)
- Malaysia registration detail (license number, product name, approved indication text) for the single existing registration
- A targeted literature/clinical review to determine whether any therapeutic (vs. diagnostic) rationale for probenecid in renal hypouricemia exists, given the mechanistic contradiction noted above
- Reassessment of the two lower-ranked candidates (Lesch-Nyhan syndrome, rank 2; HGPRT partial deficiency, rank 3) — both are purine-metabolism disorders with sparse or no evidence, and likely reflect the same diagnostic-probe association rather than independent treatment signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

