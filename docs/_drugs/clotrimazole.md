---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 5
---

# Clotrimazole
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

# Clotrimazole: From Original Indication Not Specified to Pityriasis Versicolor

## One-Sentence Summary

The evidence pack does not contain clotrimazole's original approved indication text (registry field empty) or its DrugBank mechanism of action (flagged as a High-severity data gap). TxGNN's top-ranked prediction is **Pityriasis Versicolor**, supported by **2 clinical trials** and **20 publications** — though as discussed below, this "new" indication likely already overlaps with clotrimazole's long-established antifungal use rather than representing a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in source data (registry `original_indications` empty; NPRA license indication text not retrieved for any of the 5 sampled records) |
| Predicted New Indication | Pityriasis Versicolor |
| TxGNN Prediction Score | 0.00% (raw score value returned by the model; given the drug's well-documented antifungal spectrum against the causative organism, this likely reflects a scoring/pipeline gap rather than genuine near-zero confidence) |
| Evidence Level | L3 (no completed Phase 3 RCTs registered on ClinicalTrials.gov, but a substantial body of comparative/double-blind literature spanning 1973–2024) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 64 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

DrugBank mechanism-of-action data was not retrieved for this bundle (Data Gap DG002, High severity). However, the literature already collected in this evidence pack independently confirms clotrimazole's pharmacology: it is a synthetic imidazole antifungal that "impairs the synthesis of ergosterol... in susceptible organisms, including yeast (Candida and Cryptococcus spp.), fungi, and dermatophytes" (PMID 6309466), and is described as displaying "fungistatic antimycotic activity by targeting the biosynthesis of ergosterol, thereby inhibiting fungal growth," with established topical use against *Candida albicans* and dermatophytes (PMID 24863842).

Pityriasis versicolor is caused by *Malassezia furfur* (formerly *Pityrosporum orbiculare*), a yeast within clotrimazole's known susceptible spectrum. This mechanistic overlap explains why TxGNN surfaces the indication — and it is consistent with decades of published clinical use: the earliest study in this pack, "The topical therapy of pityriasis versicolor with clotrimazole" (Gip L, 1974, PMID 4619458), predates most modern trial registries.

**Important caveat**: because `original_indications` is empty in this evidence pack, we cannot confirm whether pityriasis versicolor already sits within clotrimazole's current approved label in Malaysia. Given that clotrimazole has been used for this condition since at least the 1970s per the literature above, this prediction may represent confirmation of an existing, long-standing use rather than a genuinely novel repurposing candidate. Notably, the model's other top-ranked predictions for this drug (cutaneous candidiasis, tinea pedis, oral candidiasis, vulvovaginal candidiasis) follow the same pattern — all are established, textbook indications for topical/topical-mucosal clotrimazole — which reinforces this interpretation rather than suggesting a broad, unexpected therapeutic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07331792](https://clinicaltrials.gov/study/NCT07331792) | Phase 1, Phase 2 | Not yet recruiting | 86 | Direct comparison of topical 1% clotrimazole vs. oral itraconazole for pityriasis versicolor; not yet recruiting, no results available |
| [NCT04007237](https://clinicaltrials.gov/study/NCT04007237) | Phase 4 | Completed | 100 | Compares selenium sulfide 1.8% shampoo vs. ketoconazole 2% shampoo for pityriasis versicolor — comparator trial; clotrimazole is not an arm of this study, only tangentially relevant as PV-treatment background |

**Note**: Neither registered trial provides completed, clotrimazole-specific efficacy data for pityriasis versicolor. The one trial directly testing clotrimazole (NCT07331792) has not started recruitment.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38364431](https://pubmed.ncbi.nlm.nih.gov/38364431/) | 2024 | RCT | Dermatology Practical & Conceptual | Compares topical liposomal amphotericin B vs. topical clotrimazole for pityriasis versicolor to address recurrence |
| [28120351](https://pubmed.ncbi.nlm.nih.gov/28120351/) | 2017 | RCT | Mycoses | Single-blind RCT comparing topical tacrolimus vs. clotrimazole for PV, including effect on PV-induced hypopigmentation |
| [20649710](https://pubmed.ncbi.nlm.nih.gov/20649710/) | 2010 | RCT | The Journal of Dermatology | Double-blind RCT: single-dose oral fluconazole (400mg) vs. topical clotrimazole for PV |
| [19882007](https://pubmed.ncbi.nlm.nih.gov/19882007/) | 2008 | RCT | Indian Journal of Dermatology | Randomized comparative trial of Artemisia sieberi 5% lotion vs. clotrimazole 1% lotion for PV |
| [20948094](https://pubmed.ncbi.nlm.nih.gov/20948094/) | 1996 | RCT | Indian J Dermatol Venereol Leprol | Double-blind comparison of 2% ketoconazole vs. 1% clotrimazole for PV — 90% vs. 85% cure rates, no significant difference |
| [3607817](https://pubmed.ncbi.nlm.nih.gov/3607817/) | 1987 | RCT | Clinical Therapeutics | 8-week comparative study of tioconazole vs. clotrimazole lotion in 32 patients with tinea versicolor |
| [3332758](https://pubmed.ncbi.nlm.nih.gov/3332758/) | 1987 | RCT | The Australasian Journal of Dermatology | Comparison of sulconazole nitrate 1% solution vs. clotrimazole 1% solution for PV |
| [326197](https://pubmed.ncbi.nlm.nih.gov/326197/) | 1977 | RCT | Archives of Dermatology | Double-blind trial of 1% clotrimazole cream vs. Whitfield ointment for PV |
| [4582719](https://pubmed.ncbi.nlm.nih.gov/4582719/) | 1973 | Comparative study | The British Journal of Dermatology | Compares clotrimazole cream, Whitfield's ointment and Nystatin ointment for ringworm, PV, erythrasma and candidiasis |
| [4619458](https://pubmed.ncbi.nlm.nih.gov/4619458/) | 1974 | Early clinical study | Postgraduate Medical Journal | "The topical therapy of pityriasis versicolor with clotrimazole" — foundational study establishing this use |

---

## Malaysia Market Information

NPRA confirms clotrimazole is marketed in Malaysia with **64 active registrations**, but the individual authorization records (license number, product name, dosage form, and approved indication text) were not populated in the 5 sampled entries in this evidence pack — all fields returned blank. A license-level lookup is needed before this data can be tabulated or used to confirm whether pityriasis versicolor is already on-label.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were retrieved for this bundle (DDI query status: not found, 0 interactions returned). This is flagged in the source evidence pack as a **Blocking**-severity data gap (DG001) that prevents a formal safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The source evidence pack has a Blocking-severity gap on TFDA/NPRA label warnings and contraindications, which by definition prevents safety pre-screening. In addition, the drug's original approved indication and MOA are both unavailable, making it impossible to confirm whether pityriasis versicolor represents a genuine repurposing opportunity or simply an existing, already-approved use of clotrimazole.

**To proceed, the following is needed:**
- Retrieve the NPRA product label (PDF) for clotrimazole to obtain warnings and contraindications (per remediation for DG001)
- Query the DrugBank API for confirmed mechanism-of-action text (per remediation for DG002)
- Pull approved indication text for at least one Malaysia-registered clotrimazole product to determine whether pityriasis versicolor is already on-label
- Monitor NCT07331792 (topical clotrimazole vs. oral itraconazole for PV) once it begins recruiting, as it is the only registered trial directly testing this indication
- Re-run the TxGNN scoring step for this candidate, since the reported score (0.0) is inconsistent with the volume of supporting literature and should be treated as a data-quality issue rather than a true confidence estimate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

