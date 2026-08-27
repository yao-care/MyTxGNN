---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 3
---

# Febuxostat
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

# Febuxostat: From Hyperuricemia to Renal Hypouricemia, HPRT Deficiency and Lesch-Nyhan Syndrome

## One-Sentence Summary

Febuxostat is a xanthine oxidase (XO) inhibitor whose established use is lowering uric acid in hyperuricemia/gout. The TxGNN model surfaced three related purine-metabolism disorders as repurposing candidates — **Renal Hypouricemia**, **HPRT Partial Deficiency (Kelley-Seegmiller syndrome)**, and **Lesch-Nyhan Syndrome** — but the strength and even the direction of the rationale differ sharply between them: the top-ranked candidate (Renal Hypouricemia) is mechanistically counter-intuitive and supported only by one low-relevance trial and two review articles, while the two lower-ranked candidates fit the drug's known mechanism directly but rest on case-report-level evidence only, with no registered clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia / Gout (uric acid-lowering therapy) — inferred from mechanism text in the evidence pack; TFDA license indication text itself was not returned (data gap) |
| Predicted Indications Evaluated | 3 (see comparison table below) |
| Top-Ranked Prediction | Hypouricemia, Renal (score 99.99%) — direction of effect is mechanistically counter-intuitive, see rationale |
| Most Mechanistically Coherent Prediction | HPRT Partial Deficiency / Lesch-Nyhan Syndrome |
| Evidence Level | L3 (rank 1) / L4 (rank 2, 3) |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 11 |
| Recommended Decision | **Hold** (blocked — see rationale) |

### Predicted Indications Comparison

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---|---|---|---|---|---|
| 1 | Hypouricemia, renal | 99.99% | L3 | S1 | Research Question |
| 2 | Hypoxanthine-guanine phosphoribosyltransferase (HPRT) partial deficiency | 99.98% | L4 | S2 | Proceed with Guardrails |
| 3 | Lesch-Nyhan syndrome | 99.68% | L4 | S2 | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The `drug.original_moa` field is marked as a data gap, but the mechanism can be reconstructed from the evidence pack's own rationale text: Febuxostat is a **selective xanthine oxidase (XO) inhibitor** that blocks the conversion of hypoxanthine/xanthine to uric acid — the mechanistic basis of its approved use in hyperuricemia and gout.

For **Renal Hypouricemia (rank 1)**, the link is not straightforward: this is a condition of *low* serum urate, and a uric-acid-*lowering* drug is not a direct treatment for it — treating hypouricemia with febuxostat would be mechanistically contradictory. The actual hypothesis surfaced in the literature (PMID 36754409) is narrower and different: in renal hypouricemia patients who develop exercise-induced acute kidney injury (EIAKI), XO activity spikes during exercise and generates reactive oxygen species (ROS); XO inhibitors may protect the kidney by suppressing ROS generation, independent of any further urate-lowering effect. This is a plausible but indirect and unconfirmed mechanistic path, and the single supporting trial (NCT04398251) provides no usable detail on population or endpoints (Relevance Grade C, status Unknown).

For **HPRT Partial Deficiency (rank 2)** and **Lesch-Nyhan Syndrome (rank 3)**, the mechanistic fit is direct and conventional: both are caused by reduced/absent HPRT enzyme activity, which shunts purine metabolism through the XO pathway and causes severe hyperuricemia, gout, and renal complications. Febuxostat's XO-inhibiting mechanism acts squarely on this downstream pathology, and it is already used clinically as an allopurinol alternative in exactly this patient population — this is a case of the model recovering a known, mechanistically sound off-label use pattern for rare purine-metabolism disorders rather than a novel discovery.

---

## Clinical Trial Evidence

| Indication | Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---------|------|------|------|---------|
| Hypouricemia, renal | [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Single-center (Shanghai Xu-hui Central Hospital, Urology) study of uric acid control on stone recurrence and renal function in hyperuricemic calculi patients; title/summary do not confirm relevance to renal hypouricemia specifically (Relevance Grade C) |

HPRT Partial Deficiency and Lesch-Nyhan Syndrome: **Currently no related clinical trials registered.**

---

## Literature Evidence

| Indication | PMID | Year | Type | Journal | Key Findings |
|---|------|-----|------|------|---------|
| Hypouricemia, renal | [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia etiology and clinical relevance for rheumatologists |
| Hypouricemia, renal | [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review/Case | Internal Medicine (Tokyo) | Case of familial renal hypouricemia (URAT1 mutation) with recurrent EIAKI; proposes non-purine XO inhibitors (incl. febuxostat) as prophylaxis via ROS suppression |
| HPRT partial deficiency | [32128695](https://pubmed.ncbi.nlm.nih.gov/32128695/) | 2020 | Case report | CEN Case Reports | Novel HPRT1 p.V35M mutation causing partial HPRT deficiency presenting as familial juvenile gout |
| HPRT partial deficiency | [26073243](https://pubmed.ncbi.nlm.nih.gov/26073243/) | 2015 | Case report | Internal Medicine (Tokyo) | Novel HPRT gene mutation combined with known variants, presenting as hyperuricemia/gout in a 15-year-old |
| Lesch-Nyhan syndrome | [40763966](https://pubmed.ncbi.nlm.nih.gov/40763966/) | 2025 | Case report/series | Zhonghua Yi Xue Yi Chuan Xue Za Zhi | Clinical, genetic, and treatment characteristics of two pediatric Lesch-Nyhan syndrome cases |
| Lesch-Nyhan syndrome | [32128695](https://pubmed.ncbi.nlm.nih.gov/32128695/) | 2020 | Case report | CEN Case Reports | Same HPRT1 mutation case as above, relevant to the broader HPRT-deficiency spectrum including Lesch-Nyhan syndrome |

---

## Malaysia Market Information

The evidence pack confirms Febuxostat is **Marketed** in Malaysia with **11 total registrations**, but the individual license records (license number, product name, dosage form, approved indication text) were all returned empty in this data pull — a data gap requiring a direct NPRA/TFDA re-query before this can be used for regulatory review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and `ddi` are all marked as data gaps in this evidence pack. This is flagged as a **Blocking** gap (DG001) — it directly prevents completion of the S1 safety screening stage for any of the three candidate indications, independent of their individual evidence strength.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Regardless of how promising the mechanistic case is for HPRT Partial Deficiency and Lesch-Nyhan Syndrome, the pack's own data-gap log marks the missing TFDA label warnings/contraindications (DG001) as **Blocking severity** — it explicitly prevents entry into the S1 safety initial-review stage. No indication can be advanced past this gate until that data is supplied. Separately, the top-ranked candidate (Renal Hypouricemia) has a mechanistically indirect rationale and only Grade C trial evidence, and should not be prioritized even once the safety gate clears.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications, DDI) — required to clear the Blocking S1 safety gate
- Detailed original MOA documentation from DrugBank (currently a High-severity data gap)
- Full NPRA license-level detail (product name, dosage form, indication text) for the 11 registrations
- Clarification of the NCT04398251 trial's actual population/endpoints to confirm or rule out relevance to renal hypouricemia
- Given the rarity of HPRT deficiency and Lesch-Nyhan syndrome, real-world/registry evidence should be sought to supplement the case-report-only literature base before any guardrailed use is finalized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

