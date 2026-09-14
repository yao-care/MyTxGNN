---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
---

# Prednisolone Acetate
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

# Prednisolone Acetate: From Ophthalmic/Systemic Corticosteroid Use to Conjunctivitis

## One-Sentence Summary

Prednisolone acetate is a topical/ophthalmic corticosteroid; the specific original indication text was not captured in this evidence pull, though 6 NPRA marketing authorizations are on file in Malaysia. The TxGNN model predicts it may be effective for **Conjunctivitis**, and unlike most of the other candidate sub-diagnoses surfaced for this drug, this signal is already backed by **10 clinical trials** and **20 publications**, several using prednisolone acetate itself as the study drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (license indication text blank; drug class is a topical/systemic corticosteroid) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

Note: TxGNN's single highest-ranked prediction is actually "acute contagious conjunctivitis" (score 99.97%), but that candidate has **zero** supporting trials or literature and carries an explicit safety caution (steroids may worsen untreated infectious conjunctivitis). This report focuses on "Conjunctivitis" (rank 2) because it is the only candidate in this set with an actual evidentiary base and an actionable decision stage (S3).

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data (DrugBank MOA text) was not available in this evidence pack. Based on the pharmacology reflected in the evidence, prednisolone acetate is a glucocorticoid that suppresses inflammatory cytokine release and leukocyte infiltration — the standard mechanism by which topical ophthalmic corticosteroids control ocular surface inflammation.

This mechanism maps directly onto allergic and steroid-responsive forms of conjunctivitis (e.g., seasonal/perennial allergic conjunctivitis, vernal keratoconjunctivitis, giant papillary conjunctivitis), where the inflammatory process itself — rather than an active untreated pathogen — is the primary driver of symptoms. Several of the supporting trials use prednisolone acetate (or the closely related prednisolone sodium phosphate) as the active comparator in Conjunctival Allergen Challenge (CAC) models, directly testing the drug in this indication rather than in an analog.

The caveat is that "conjunctivitis" is an etiologically heterogeneous label spanning allergic, viral, bacterial, and immune-mediated causes. The rationale explicitly flags that corticosteroid monotherapy is inappropriate for infectious conjunctivitis without concurrent antimicrobial/antiviral coverage, and that IOP and cataract risk require monitoring with prolonged use — hence the "Proceed with Guardrails" rather than "Go" recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00689078](https://clinicaltrials.gov/study/NCT00689078) | Phase 4 | Completed | 36 | Randomized, double-masked comparison of prednisolone acetate 1% vs. 0.12%, loteprednol etabonate 0.2%, and placebo in a modified conjunctival allergen challenge (CAC) model; direct efficacy evidence for the study drug itself. |
| [NCT01730872](https://clinicaltrials.gov/study/NCT01730872) | Phase 4 | Completed | 16 | Double-masked, placebo-controlled CAC evaluation of prednisolone sodium phosphate 1% ophthalmic solution for allergic inflammation (itching, redness). |
| [NCT01534195](https://clinicaltrials.gov/study/NCT01534195) | Phase 4 | Completed | 11 | Randomized, double-masked, placebo-controlled adaptive CAC trial of prednisolone sodium phosphate 1% in allergic conjunctivitis. |
| [NCT01120132](https://clinicaltrials.gov/study/NCT01120132) | Phase 2 | Completed | 716 | Multi-center trial of cyclosporine ± prednisolone acetate vs. components/vehicle in mild ocular allergic inflammation; large sample, indirect (combination) evidence. |
| [NCT00833495](https://clinicaltrials.gov/study/NCT00833495) | Phase 2 | Completed | 155 | Co-administration of cyclosporine with prednisolone acetate 0.12% (PredMild®) vs. prednisolone acetate 1% alone or vehicle in mild ocular allergic inflammation. |
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | N/A | Unknown | 180 | Comparative study of topical immunosuppressants (cyclosporine A vs. tacrolimus) as steroid-sparing alternatives in resistant spring catarrh; positions topical steroids as current standard of care. |
| [NCT03320434](https://clinicaltrials.gov/study/NCT03320434) | Phase 2 | Completed | 120 | Dose-ranging, vehicle- and active-controlled study of PRT-2761 for acute/chronic allergic conjunctivitis using the Ora-CAC® model; supports the CAC methodology used across this evidence set. |
| [NCT01437982](https://clinicaltrials.gov/study/NCT01437982) | Phase 4 | Completed | 140 | Post-marketing surveillance of Lotemax (loteprednol) 0.5% ophthalmic suspension; same-class safety/efficacy monitoring precedent. |
| [NCT00298272](https://clinicaltrials.gov/study/NCT00298272) | Phase 2 | Terminated | 54 | Rituximab + MTX combination trial in rheumatoid arthritis; not directly relevant to conjunctivitis. |
| [NCT00967226](https://clinicaltrials.gov/study/NCT00967226) | Phase 2 | Terminated | 19 | Propranolol vs. prednisolone for infant hemangiomas; different indication, not relevant to conjunctivitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24055903](https://pubmed.ncbi.nlm.nih.gov/24055903/) | 2013 | Comparative | Cornea | Compares topical cyclosporine A, epinastine, and prednisolone acetate 1% in an experimental allergic conjunctivitis model. |
| [32049186](https://pubmed.ncbi.nlm.nih.gov/32049186/) | 2020 | Comparative study | Acta Cirurgica Brasileira | Prednisolone vs. sodium diclofenac (both with ciprofloxacin) vs. artificial tears for signs/symptoms of acute viral conjunctivitis. |
| [6398026](https://pubmed.ncbi.nlm.nih.gov/6398026/) | 1984 | Randomized comparative | Annals of Ophthalmology | Fluorometholone acetate vs. prednisolone acetate 1.0% in external ocular inflammation, including conjunctivitis. |
| [15048138](https://pubmed.ncbi.nlm.nih.gov/15048138/) | 2004 | Retrospective case series | Bone Marrow Transplantation | Topical corticosteroid therapy for cicatricial conjunctivitis in chronic GVHD; graded clinical outcomes over treatment course. |
| [8619769](https://pubmed.ncbi.nlm.nih.gov/8619769/) | 1996 | Experimental/lab | Archives of Ophthalmology | Effects of Pred Forte (prednisolone acetate) on adenoviral replication in vitro and in a rabbit ocular model — informs the viral-conjunctivitis caution. |
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Cohort | Advances in Therapy | Impact of topical ophthalmic corticosteroids (loteprednol) on intraocular pressure — same-class safety monitoring relevance. |
| [12931748](https://pubmed.ncbi.nlm.nih.gov/12931748/) | 2003 | Review/epidemiology | Asian Pacific Journal of Allergy and Immunology | Vernal keratoconjunctivitis in Thailand; topical corticosteroids used in moderate-to-severe cases. |
| [9689636](https://pubmed.ncbi.nlm.nih.gov/9689636/) | 1998 | Experimental/lab | Ocular Immunology and Inflammation | Corticosteroid (Pred Forte) treatment in a compound 48/80-induced mouse conjunctivitis model, mechanistic (PLA2/iNOS) evidence. |
| [28792180](https://pubmed.ncbi.nlm.nih.gov/28792180/) | 2017 | Case report | The Journal of the Association of Physicians of India | Bilateral acute anterior uveitis and conjunctivitis after zoledronic acid, treated with topical prednisolone acetate 1% with resolution. |
| [33437893](https://pubmed.ncbi.nlm.nih.gov/33437893/) | 2021 | Case report | American Journal of Ophthalmology Case Reports | Presumed herpetic interstitial keratitis initially diagnosed as viral conjunctivitis, treated with valacyclovir plus topical prednisolone acetate. |

---

## Malaysia Market Information

NPRA records confirm the product is **Marketed** with **6 active licenses**, but license-level details (registration numbers, product names, dosage forms, and approved indication text) were not captured in this data pull — all corresponding fields in the evidence pack are blank.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Conjunctivitis is the only TxGNN-predicted indication in this candidate set with meaningful clinical trial and literature support (10 trials, several using prednisolone acetate itself in CAC models; 20 publications), reaching evidence level L1 and decision stage S3. However, "conjunctivitis" spans infectious and non-infectious etiologies, and the evidence base itself (e.g., the adenoviral-replication and acute-viral-conjunctivitis studies) warns that steroid monotherapy is inappropriate without excluding or co-treating infection — hence guardrails rather than an unconditional "Go."
- The other 9 predicted sub-diagnoses (acute contagious conjunctivitis, parasitic conjunctivitis, chronic follicular conjunctivitis, conjunctival folliculosis, serous conjunctivitis, papillary conjunctivitis, Angelucci syndrome, pseudomembranous conjunctivitis, acute hemorrhagic conjunctivitis) remain at L3–L5 / S0–S1 with "Hold" recommendations and should not be pursued on current evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, precautions, contraindications) — currently a Blocking data gap preventing safety pre-screening (S1).
- Confirmed mechanism-of-action and DrugBank classification data.
- License-level detail (indication text, dosage form) for the 6 Malaysia authorizations, to confirm whether an ophthalmic-route product already carries a conjunctivitis-adjacent label.
- A protocol requiring exclusion or concurrent treatment of infectious etiology before steroid use, plus a monitoring plan for IOP and cataract risk with extended use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

