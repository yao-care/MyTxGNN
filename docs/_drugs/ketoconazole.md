---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 5
---

# Ketoconazole
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

# Ketoconazole: From Fungal Infections to Chromomycosis

## One-Sentence Summary

Ketoconazole is an orally active imidazole antifungal historically used against a broad range of fungal infections. The TxGNN model's top-ranked prediction is **Chromomycosis**, a rare disfiguring subcutaneous fungal disease, with **0 registered clinical trials** and **20 publications** — mostly 1980s case series and reviews — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — the 5 NPRA licence records in this pack have no indication text populated, and DrugBank MOA/indication data is flagged as a data gap |
| Predicted New Indication | Chromomycosis |
| TxGNN Prediction Score | 0.00% (score field returned 0.0 for all 5 candidates in this pack; ranking reflects TxGNN rank order, not score magnitude) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 33 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as data gap DG002, High severity). Based on the literature included in this evidence pack, ketoconazole is an orally active imidazole derivative that impairs fungal ergosterol synthesis in the cell membrane (PMID 6309466), and it was historically approved by the FDA for a broad range of fungal infections — including candidiasis, coccidioidomycosis, histoplasmosis, **and chromomycosis itself** (PMID 6301794).

Chromomycosis is a chronic subcutaneous mycosis caused by dematiaceous (pigmented) fungi such as *Fonsecaea pedrosoi* and *Phialophora* species. These organisms fall within ketoconazole's known antifungal spectrum, and the pack's own rationale (`repurposing_rationale.mechanistic_link`) describes the mechanistic link as direct. However, no clinical trials have ever been registered for this combination — the supporting evidence is limited entirely to case series, case reports, and reviews from the 1980s (PMID 6252105, 6298285, 3842101).

It is also worth noting that current treatment guidance has largely moved past ketoconazole for this indication: a 2025 paper in this same pack (PMID 40183549) states itraconazole is now considered first-line therapy for chromoblastomycosis, with terbinafine, voriconazole, and posaconazole as alternatives. This should temper enthusiasm despite the mechanistically direct rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6301794](https://pubmed.ncbi.nlm.nih.gov/6301794/) | 1983 | Review | Drug Intell Clin Pharm | Confirms historical FDA approval of ketoconazole for chromomycosis among other mycoses |
| [6309466](https://pubmed.ncbi.nlm.nih.gov/6309466/) | 1982 | Review | Clinical Pharmacy | Reviews pharmacology/mechanism (ergosterol synthesis inhibition), clinical use, and DDIs |
| [6252105](https://pubmed.ncbi.nlm.nih.gov/6252105/) | 1980 | Case Series | Int J Dermatol | 7 chromomycosis cases among 47 patients treated with oral ketoconazole 200–400 mg/day |
| [6298285](https://pubmed.ncbi.nlm.nih.gov/6298285/) | 1983 | Case Series | J Am Acad Dermatol | Ketoconazole + 5-fluorocytosine combination succeeded after ketoconazole monotherapy failed; in vitro synergy shown against *Fonsecaea pedrosoi* |
| [3842101](https://pubmed.ncbi.nlm.nih.gov/3842101/) | 1985 | Case Report | Ceylon Med J | Treatment of chromomycosis with ketoconazole + 5-fluorocytosine combination |
| [6325087](https://pubmed.ncbi.nlm.nih.gov/6325087/) | 1984 | Review | Connecticut Medicine | General ketoconazole review |
| [3325708](https://pubmed.ncbi.nlm.nih.gov/3325708/) | 1987 | Review | Med Cutan Ibero Lat Am | 25-year chromomycosis case (Mozambique); poor prognosis despite ketoconazole/amphotericin |
| [6255545](https://pubmed.ncbi.nlm.nih.gov/6255545/) | 1980 | Case Series | Rev Infect Dis | Brief summary of ketoconazole treatment across paracoccidioidomycosis, candidosis, chromomycosis, lobomycosis, mycetoma |
| [8077517](https://pubmed.ncbi.nlm.nih.gov/8077517/) | 1994 | Review | J Am Acad Dermatol | Reviews treatment of tropical subcutaneous/deep mycoses including chromoblastomycosis |
| [20952879](https://pubmed.ncbi.nlm.nih.gov/20952879/) | 1995 | Review | Indian J Dermatol Venereol Leprol | 28-year chromoblastomycosis case with multi-organ involvement despite ketoconazole and amphotericin B |

---

## Malaysia Market Information

License-level detail (product name, dosage form, approved indication text) was not populated for any of the 5 sampled records in this evidence pack. The register confirms **33 total NPRA licences** for ketoconazole with an overall market status of **✓ Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps in this pack — including a **Blocking**-severity gap on TFDA/NPRA label warnings, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between ketoconazole and dematiaceous fungi is direct, and historical case-series evidence shows clinical benefit. However, evidence is dated (pre-1990), no clinical trials have ever been registered, and modern guidance favors itraconazole as first-line therapy — so any guardrail pathway should require an updated comparative-efficacy check against current standard of care.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap, DG001) — required before any S1 safety screen
- DrugBank mechanism-of-action confirmation (High-severity gap, DG002)
- Populated Malaysia licence indication text (all 5 sampled records are currently blank)
- A current-standard-of-care comparison against itraconazole/terbinafine given PMID 40183549

**Note:** This pack also contains 4 other candidate indications for ketoconazole with independently scored evidence — notably **tinea pedis** (L1, S3, "Proceed with Guardrails," supported by 5 completed Phase 3 trials, one with n=831) and **paracoccidioidomycosis** (L2, S2, supported by an RCT, PMID 12230222). Those carry materially stronger evidence than chromomycosis and may warrant a separate evaluation if the goal is to prioritize by evidence strength rather than TxGNN rank order.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

