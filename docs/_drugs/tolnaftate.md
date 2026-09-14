---
layout: default
title: Tolnaftate
parent: 僅模型預測 (L5)
nav_order: 655
evidence_level: L5
indication_count: 5
---

# Tolnaftate
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

# Tolnaftate: Original Indication Undocumented — Predicted Application in Pityriasis Versicolor

## One-Sentence Summary

The evidence pack for this candidate does not record Tolnaftate's originally approved indication (NPRA license text and DrugBank fields are both empty — see data gaps DG001/DG002). The TxGNN model's top-ranked prediction is **Pityriasis versicolor**, supported by **0 registered clinical trials** and **18 publications**, though the reported TxGNN score of 0.0 appears to be a placeholder/pipeline artifact rather than a genuine confidence value and should be re-verified before use in decision-making.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — NPRA license records contain no approved-indication text in this pull (see DG001) |
| Predicted New Indication | Pityriasis versicolor |
| TxGNN Prediction Score | 0% (raw score = 0.0; likely a data/pipeline gap, not a true low-confidence result — needs re-validation) |
| Evidence Level | L2 (per evidence pack scoring) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in the drug-level record (`original_moa` is a documented data gap, DG002, High severity). However, the repurposing rationale attached to this candidate does describe the pharmacology: Tolnaftate is a thiocarbamate antifungal that inhibits squalene epoxidase, blocking ergosterol synthesis in the fungal cell membrane. This mechanism gives it activity against *Malassezia furfur*, the organism that causes pityriasis (tinea) versicolor.

Several of the candidate's other ranked predictions (tinea pedis, tinea corporis, tinea barbae, dermatophytosis of groin/perianal area) are all classic dermatophyte/superficial fungal infections — the same therapeutic class Tolnaftate is long established in clinically. The rationale text for pityriasis versicolor itself notes this is "a long-known clinical use" (為長期臨床已知用途) via the same mechanism as its use in tinea infections, meaning this "prediction" is best read as a within-class confirmation of an already well-characterized antifungal spectrum rather than a mechanistically novel repurposing signal.

Because the original approved indication is not recorded in this evidence pack, the reviewer cannot yet confirm whether pityriasis versicolor is already an approved/labeled use in Malaysia or represents a genuine label extension — this should be resolved before the candidate moves past guardrail review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5338033](https://pubmed.ncbi.nlm.nih.gov/5338033/) | 1966 | RCT (double-blind) | Dermatologica | Double-blind clinical evaluation of tolnaftate as a topical antifungal agent |
| [38874607](https://pubmed.ncbi.nlm.nih.gov/38874607/) | 2024 | Review | Dermatologie (Heidelberg) | Confirms tolnaftate among topical antifungals with activity against dermatophytes; notes pityriasis versicolor is treated topically with antimycotics |
| [2029718](https://pubmed.ncbi.nlm.nih.gov/2029718/) | 1991 | Review | Clinical Therapeutics | Comparator-drug review (oxiconazole) noting topical antifungals' established value in tinea (pityriasis) versicolor |
| [1379146](https://pubmed.ncbi.nlm.nih.gov/1379146/) | 1992 | Review | Drugs | Diagnosis/treatment overview of superficial fungal infections including tinea versicolor (Malassezia furfur) |
| [1037098](https://pubmed.ncbi.nlm.nih.gov/1037098/) | 1976 | Review | Cutis | Review of topical antifungal agents effective in tinea versicolor and cutaneous candidiasis |
| [4617272](https://pubmed.ncbi.nlm.nih.gov/4617272/) | 1974 | Cohort | Revista de investigación en salud pública | Clinical study of an antifungal (Hoe 296) in glabrous skin dermatophytosis and pityriasis versicolor |
| [14126266](https://pubmed.ncbi.nlm.nih.gov/14126266/) | 1964 | Cohort (preliminary report) | J Invest Dermatol | Early preliminary report on tolnaftate therapy of mycotic infections |
| [5844107](https://pubmed.ncbi.nlm.nih.gov/5844107/) | 1965 | Cohort | Am J Dis Child | Clinical experience with tolnaftate in superficial fungus infections |
| [14277312](https://pubmed.ncbi.nlm.nih.gov/14277312/) | 1964 | Cohort | Dermatologia Tropica et Ecologica Geographica | Early clinical characterization of tolnaftate as a potent topical fungicide |
| [1160934](https://pubmed.ncbi.nlm.nih.gov/1160934/) | 1975 | Cohort (comparator drug) | Mykosen | Comparator (miconazole) study in dermatomycosis treatment |

---

## Malaysia Market Information

NPRA records confirm **14 active registrations** under Marketed status, but the license-level fields (registration number, product name, dosage form, approved indication text) were not populated in this data pull — none of the 5 sampled license records contain values. This should be re-queried from the NPRA source before it is used to support a labeling decision.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for antifungal activity in pityriasis versicolor is sound and consistent with Tolnaftate's established pharmacology, but the evidence base for this specific ranked indication is thin (no clinical trials, evidence level L2, largely older literature) and the reported TxGNN score of 0.0 needs re-verification. Note also that a lower-ranked candidate in this same pack — tinea pedis (rank 2) — actually carries stronger evidence (L1, including an active recruiting Phase 2 trial and 2 completed RCTs) and may warrant priority review ahead of this one.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety screening)
- Confirmed mechanism-of-action documentation (DG002)
- Complete NPRA license-level data (product names, dosage forms, approved indication text) for all 14 registrations
- Verification of the TxGNN score of 0.0 for this candidate — confirm whether it is a genuine model output or a pipeline data gap
- Clarification of whether pityriasis versicolor is already within Tolnaftate's approved label in Malaysia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

