---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Nepafenac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nepafenac: From Ocular Inflammation (Cataract Surgery) to Eye Disease

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID (marketed as Nevanac/Ilevro) established for treating pain and inflammation associated with cataract surgery. The TxGNN model predicts it may be effective for the broader category **Eye Disease**, a prediction already substantially supported by **41 clinical trials** identified in this pack, though **no dedicated literature (PMID) evidence** was returned for this specific category.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular inflammation and pain associated with cataract surgery (derived from clinical trial evidence in this pack — e.g. NCT01109173, NCT01853072; NPRA/TFDA license indication text was not returned) |
| Predicted New Indication | Eye Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Nepafenac in this evidence pack. Based on the extensive clinical trial record collected here — over 40 studies spanning 2003 to 2026 — Nepafenac is well established as a topical ophthalmic non-steroidal anti-inflammatory drug (NSAID), used to prevent and treat ocular inflammation and pain following cataract surgery, and further studied in diabetic macular edema, post-vitrectomy inflammation, laser iridotomy, and PRK-related pain.

The predicted new indication, "Eye Disease," is a broad disease category that substantially overlaps with Nepafenac's already-established therapeutic domain rather than pointing to a genuinely novel organ system or disease mechanism. TxGNN assigning a very high score here is therefore expected: an ophthalmic anti-inflammatory drug is mechanistically linked to "eye disease" almost by definition. The clinical value of this specific prediction is limited as a repurposing signal — it largely confirms existing use rather than identifying an incremental indication.

That said, the underlying evidence base does show the drug's anti-inflammatory mechanism extending into related ocular conditions beyond the core cataract-surgery label — diabetic macular edema (NCT01331005, NCT00780780), post-vitrectomy/retinal detachment inflammation (NCT07162818), central serous chorioretinopathy (NCT05847049), and corneal dystrophy (NCT04843839) — which is where a more specific, actionable repurposing signal is likely to be found (see rank 2, "optic papillitis," for a narrower disease-specific example).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Pivotal registration study of Nepafenac 0.3% for prevention/treatment of ocular inflammation and pain after cataract surgery |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for post-cataract inflammation and pain |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once daily superior to vehicle in diabetic subjects after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Confirmatory trial: Nepafenac 0.3% superiority in diabetic subjects post-cataract surgery |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | NA | Completed | 662 | Nepafenac 0.3% adjunct to steroid for prevention of pseudophakic cystoid macular edema |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Bioequivalence of generic Nepafenac 0.3% vs Ilevro for pain/inflammation post-cataract surgery |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% superior to vehicle in Chinese subjects for post-cataract inflammation/pain |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | Terminated | 175 | Nevanac evaluated for macular edema incidence/severity reduction in diabetic retinopathy patients |
| [NCT01331005](https://clinicaltrials.gov/study/NCT01331005) | Phase 2 | Completed | 125 | Topical NSAID effects on retinal volume in non-central diabetic macular edema |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | Completed | 40 | Nepafenac 0.1% reduces macular volume after epiretinal membrane surgery vs placebo |

## Literature Evidence

Currently no related literature available for this specific indication (PubMed search returned 0 results for "Nepafenac" + "eye disease").

## Malaysia Market Information

Registration status confirms the product is marketed in Malaysia with 1 active registration; however, the detailed license record (license number, product name, dosage form, and approved indication text) was not returned in this data pull and could not be tabulated.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — resolving this is flagged as a blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (missing TFDA/NPRA label warnings and contraindications, DG001) prevents the required S1 safety pre-assessment. In addition, the top-ranked predicted indication, "Eye Disease," is too generic to constitute a clear incremental repurposing target given the drug's already-approved ophthalmic anti-inflammatory use.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action detail (DG002, High)
- Complete NPRA license record (license number, product name, dosage form, approved indication text)
- Re-scoring against more disease-specific predicted indications (e.g. rank 2, "optic papillitis," or the diabetic macular edema signal) rather than the generic "Eye Disease" category
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

