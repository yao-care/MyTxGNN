---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 608
evidence_level: L5
indication_count: 5
---

# Salicylic Acid
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

# Salicylic Acid: From Topical Keratolytic Use to Five TxGNN-Predicted Indications

## One-Sentence Summary

Salicylic acid (DrugBank DB00936) is a long-marketed topical beta-hydroxy acid (BHA) with 71 existing product licenses in Malaysia, though the specific original approved-indication text is not captured in the current registration data pull. TxGNN flags five candidate indications — **acne**, **plantar wart**, **acquired (actinic) keratosis**, **keratinization disease**, and **osteoarthritis** — with evidence quality ranging from strong, already-standard clinical use (acne and plantar wart: **L1**, 34 and 5 trials respectively) down to a largely historical/preclinical hypothesis (osteoarthritis: **L3**). This is best read as a portfolio of five separate repurposing/label-extension questions rather than a single new indication.

---

## Quick Overview

*Note: predicted_indications[0] by TxGNN rank ("keratinization disease") carries a score of 0.0 and the weakest supporting evidence (L3). The table below shows that entry plus a comparison of all five candidates, since the strongest, most actionable signal (acne, plantar wart) sits at rank 2–3, not rank 1.*

| Item | Content |
|------|------|
| Original Indication | Not specified in the registration data pull (all 5 sampled license records have blank `approved_indication_text`); salicylic acid is a long-marketed topical keratolytic/dermatological agent |
| Predicted New Indication (TxGNN rank 1) | Keratinization disease |
| TxGNN Prediction Score | Recorded as 0.0 for all 5 candidates — appears to be a data-population gap rather than a genuine near-zero confidence score; **not usable for ranking as-is** |
| Evidence Level (rank 1: keratinization disease) | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 71 |
| Recommended Decision (rank 1: keratinization disease) | Research Question |

### All Five Predicted Indications, Ranked by Evidence Strength

| Rank (TxGNN) | Disease | Evidence Level | Decision Stage | Recommendation | CT / Lit Count |
|---|---|---|---|---|---|
| 2 | Acne | **L1** | S3 | Proceed with Guardrails | 34 CT / 19 Lit |
| 3 | Plantar wart | **L1** | S3 | Proceed with Guardrails | 5 CT / 20 Lit |
| 4 | Acquired keratosis (incl. actinic keratosis) | L2 | S3 | Proceed with Guardrails | 0 CT / 19 Lit |
| 1 | Keratinization disease | L3 | S2 | Research Question | 1 CT / 19 Lit |
| 5 | Osteoarthritis | L3 | S1 | Research Question | 3 CT / 20 Lit |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in this evidence pack (flagged as data gap DG002, High severity). Based on established pharmacology, salicylic acid is a lipophilic beta-hydroxy acid (BHA) that, applied topically, acts as a **keratolytic/desmolytic agent**: it disrupts intercellular desmosomal adhesion in the stratum corneum, promoting shedding of abnormally thickened or cohesive keratin. This single mechanism plausibly explains four of the five predicted indications — **acne** (follicular hyperkeratosis + sebum plugging), **plantar wart** (HPV-infected hyperkeratotic epidermis), **acquired/actinic keratosis** (dysplastic hyperkeratotic epidermis, where salicylic acid enhances penetration of co-formulated 5-fluorouracil), and the broader **keratinization disease** category (palmoplantar keratodermas, Darier disease, ichthyoses) — all of which share hyperkeratosis as the core pathology.

The fifth candidate, **osteoarthritis**, relies on a mechanistically distinct pathway: salicylate salts (e.g., sodium salicylate) have systemic cyclooxygenase (COX)-inhibiting anti-inflammatory/analgesic activity, historically studied for joint pain before being superseded by modern NSAIDs. This is pharmacologically related to salicylic acid but is a different route/formulation question (systemic vs. topical) and is supported mostly by 1950s–1980s literature plus one 2025 preclinical nanoparticle study — a far weaker and more speculative link than the keratolytic indications.

Because none of the four keratolytic-pathway indications represent a truly novel mechanism, the practical question for this candidate set is less "is repurposing biologically plausible" and more "how much of this is already standard-of-care/labeling-alignment (acne, plantar wart) versus genuinely under-evidenced (rare keratinization disorders, osteoarthritis)."

---

## Clinical Trial Evidence

### Acne (TxGNN rank 2, L1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT02052752](https://clinicaltrials.gov/study/NCT02052752) | Phase 4 | Completed | 90 | Randomized double-blind study assessing how quickly a topical salicylic acid acne product produces visible lesion improvement over 5 days |
| [NCT05821296](https://clinicaltrials.gov/study/NCT05821296) | N/A | Completed | 42 | "Crystal Peel," a salicylic-acid-based peel, evaluated for lesion-count efficacy in mild facial acne vulgaris |
| [NCT06179056](https://clinicaltrials.gov/study/NCT06179056) | N/A | Completed | 48 | Compared anti-biofilm activity of salicylic acid, isotretinoin, and N-acetylcysteine against C. acnes, and effect on antibiotic susceptibility |
| [NCT03071549](https://clinicaltrials.gov/study/NCT03071549) | Phase 3 | Completed | 34 | Split-face RCT: salicylic + azelaic acid combination vs. 25% TCA peel for mild-to-moderate acne |
| [NCT00624676](https://clinicaltrials.gov/study/NCT00624676) | N/A | Completed | 80 | RCT comparing a lipophilic salicylic acid derivative (LHA) with 5% benzoyl peroxide for facial acne vulgaris |
| [NCT01446237](https://clinicaltrials.gov/study/NCT01446237) | N/A | Completed | 125 | Open-label 12-week study of benzoyl peroxide 2.5% + salicylic acid 0.5% combination system for moderate-to-severe acne |
| [NCT02755545](https://clinicaltrials.gov/study/NCT02755545) | Phase 4 | Completed | 127 | Multi-center 24-week trial comparing two acne treatments in adults with mild-to-moderate facial acne |
| [NCT03832647](https://clinicaltrials.gov/study/NCT03832647) | Phase 4 | Completed | 200 | Double-blind RCT of a dermo-cosmetic plus adapalene/benzoyl peroxide vs. adapalene/BPO plus standard moisturizer |
| [NCT05712837](https://clinicaltrials.gov/study/NCT05712837) | N/A | Completed | 60 | RCT: 25% TCA peel vs. 30% salicylic acid peel in mild-to-moderate acne vulgaris |
| [NCT05497323](https://clinicaltrials.gov/study/NCT05497323) | Phase 1 | Unknown | 284 | Combination cream containing salicylic acid + niacinamide + other actives as adjuvant therapy for mild-to-moderate acne |

### Plantar Wart (TxGNN rank 3, L1) — all 5 registered trials shown

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT05617950](https://clinicaltrials.gov/study/NCT05617950) | N/A | Unknown | 174 | Head-to-head RCT: salicylic acid vs. cryotherapy for HPV-1-induced plantar warts |
| [NCT06958237](https://clinicaltrials.gov/study/NCT06958237) | N/A | Completed | 30 | Post-market performance/safety evaluation of a salicylic acid wart patch (medical device) for common and plantar warts |
| [NCT01712295](https://clinicaltrials.gov/study/NCT01712295) | Phase 4 | Unknown | 100 | New salicylate formulation (with ethyl pyruvate) vs. standard-of-care 17% salicylate for plantar warts |
| [NCT05588999](https://clinicaltrials.gov/study/NCT05588999) | Phase 1 | Completed | 70 | Cryotherapy alone vs. cryotherapy + salicylic acid dressing for plantar warts |
| [NCT02151630](https://clinicaltrials.gov/study/NCT02151630) | Phase 2/3 | Unknown | 60 | Compared 70% pyruvic acid vs. compound salicylic acid solution (16.7% SA + lactic acid) for plantar warts |

### Acquired Keratosis (TxGNN rank 4, L2)

Currently no related clinical trials registered for this exact disease term. (Supporting RCT evidence for the specific 5-FU/salicylic-acid combination product exists in the literature table below.)

### Keratinization Disease (TxGNN rank 1, L3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT05536193](https://clinicaltrials.gov/study/NCT05536193) | Phase 4 | Unknown | 34 | Split-face study of topical metformin emulgel vs. salicylic acid peeling for acne vulgaris — relevance to broad "keratinization disease" is indirect (acne-specific trial, graded C) |

### Osteoarthritis (TxGNN rank 5, L3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT03277573](https://clinicaltrials.gov/study/NCT03277573) | Phase 1 | Completed | 40 | Safety/tolerability/PK study of salsalate (a salicylate) in mild-to-moderate Alzheimer's disease — not an OA trial; included only for salicylate-class relevance, needs manual confirmation |
| [NCT04066426](https://clinicaltrials.gov/study/NCT04066426) | Phase 4 | Completed | 200 | Naproxen-based analgesic comparison for myofascial/TMD pain — naproxen is the intervention, not salicylic acid; indirect NSAID-class relevance only |
| [NCT07350239](https://clinicaltrials.gov/study/NCT07350239) | N/A | Not yet recruiting | 20 | Observational characterization of severe TMJ pathology — no salicylic acid intervention |

None of the three registered "osteoarthritis" trials are direct salicylic-acid efficacy trials in OA; this indication rests almost entirely on older salicylate-class literature and one 2025 preclinical study (see below).

---

## Literature Evidence

### Acne

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38300170](https://pubmed.ncbi.nlm.nih.gov/38300170/) | 2024 | Guideline | J Am Acad Dermatol | AAD guidelines of care for acne vulgaris management |
| [35789996](https://pubmed.ncbi.nlm.nih.gov/35789996/) | 2022 | Systematic Review/NMA | Br J Dermatol | Network meta-analysis of topical/oral/physical/combined acne treatments |
| [40682377](https://pubmed.ncbi.nlm.nih.gov/40682377/) | 2025 | RCT | J Cosmet Dermatol | 21-day prospective study: salicylic-acid gel improves acne lesions while preserving skin barrier function |
| [30972839](https://pubmed.ncbi.nlm.nih.gov/30972839/) | 2019 | Mechanistic | Exp Dermatol | Salicylic acid suppresses AMPK/SREBP1 pathway in sebocytes, reducing sebum production |
| [26347269](https://pubmed.ncbi.nlm.nih.gov/26347269/) | 2015 | Review | Clin Cosmet Investig Dermatol | Comprehensive review of salicylic acid as a peeling/comedolytic agent |
| [34812859](https://pubmed.ncbi.nlm.nih.gov/34812859/) | 2021 | Review | JAMA | General review of acne vulgaris management, including topical BHA therapy |
| [33034949](https://pubmed.ncbi.nlm.nih.gov/33034949/) | 2020 | Cochrane Review (abridged) | J Evid Based Med | Evidence-based review of azelaic/salicylic acid, nicotinamide, sulfur, zinc, fruit acid for acne |
| [32356369](https://pubmed.ncbi.nlm.nih.gov/32356369/) | 2020 | Cochrane Systematic Review | Cochrane Database Syst Rev | Full Cochrane review of topical azelaic acid, salicylic acid, and related agents for acne |
| [39420562](https://pubmed.ncbi.nlm.nih.gov/39420562/) | 2024 | Review | Expert Opin Pharmacother | Update on pharmacological management of acne vulgaris |
| [30550830](https://pubmed.ncbi.nlm.nih.gov/30550830/) | 2019 | Review | J Am Acad Dermatol | Review of superficial and medium-depth chemical peels, including salicylic acid peels |

### Plantar Wart

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33263934](https://pubmed.ncbi.nlm.nih.gov/33263934/) | 2021 | Systematic Review | Dermatol Ther | Systematic review of topical treatments for plantar warts |
| [40743833](https://pubmed.ncbi.nlm.nih.gov/40743833/) | 2025 | Multicentre pragmatic RCT | Ann Dermatol Venereol | Compared 50% salicylic acid, cryotherapy, 5-FU cream, and imiquimod in previously treated plantar warts |
| [21652750](https://pubmed.ncbi.nlm.nih.gov/21652750/) | 2011 | RCT | BMJ | Randomized trial: cryotherapy vs. salicylic acid for plantar warts |
| [3377974](https://pubmed.ncbi.nlm.nih.gov/3377974/) | 1988 | Double-blind RCT | Br J Dermatol | Monochloroacetic acid + 60% salicylic acid superior to placebo for simple plantar warts (66% vs 18% cure) |
| [16281635](https://pubmed.ncbi.nlm.nih.gov/16281635/) | 2004 | Systematic Review/Meta-analysis | J Dtsch Dermatol Ges | Efficacy of 5-FU/salicylic acid preparation for common and plantar warts |
| [29379975](https://pubmed.ncbi.nlm.nih.gov/29379975/) | 2018 | Review | J Am Osteopath Assoc | Epidemiology, pathophysiology, and clinical management of plantar warts |
| [39295250](https://pubmed.ncbi.nlm.nih.gov/39295250/) | 2024 | Retrospective case series (n=48) | J Med Virol | Cantharidin/podophyllin/salicylic acid (CPS) formulation in recalcitrant plantar warts |
| [27072919](https://pubmed.ncbi.nlm.nih.gov/27072919/) | 2016 | Retrospective (n=75) | Dermatol Ther | Safety/effectiveness of CPS treatment for recalcitrant plantar warts |
| [12852385](https://pubmed.ncbi.nlm.nih.gov/12852385/) | 2003 | Cohort/case report | J Drugs Dermatol | Combination imiquimod + salicylic acid pad for plantar wart |
| [40526950](https://pubmed.ncbi.nlm.nih.gov/40526950/) | 2024 | Review | Dermatol Online J | Updated review of topical cantharidin use, including CPS formulations for warts |

### Acquired Keratosis (incl. Actinic Keratosis)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27995485](https://pubmed.ncbi.nlm.nih.gov/27995485/) | 2017 | Phase III RCT | Dermatol Ther | 5-FU 0.5%/salicylic acid 10% superior to vehicle for field-directed actinic keratosis treatment |
| [32478958](https://pubmed.ncbi.nlm.nih.gov/32478958/) | 2020 | Cohort | Dermatol Ther | Dermoscopy/RCM monitoring of 5-FU/SA lesion-directed therapy for actinic keratosis |
| [27223248](https://pubmed.ncbi.nlm.nih.gov/27223248/) | 2016 | Product review | Skin Therapy Lett | Review of Actikerall (5-FU 0.5%/SA 10%) for patient-directed AK treatment |
| [35435128](https://pubmed.ncbi.nlm.nih.gov/35435128/) | 2022 | Observational cohort | J Dermatolog Treat | Early clinical response to 5-FU/SA topical solution for head/neck actinic keratoses |
| [36902419](https://pubmed.ncbi.nlm.nih.gov/36902419/) | 2023 | Review | Int J Mol Sci | Review of pharmacological agents (incl. 5-FU/SA) for actinic keratosis prevention/treatment |
| [38351246](https://pubmed.ncbi.nlm.nih.gov/38351246/) | 2024 | Review | Am J Clin Dermatol | Field cancerization therapies for actinic keratosis management |
| [25495775](https://pubmed.ncbi.nlm.nih.gov/25495775/) | 2015 | Cost-effectiveness analysis | Expert Rev Pharmacoecon Outcomes Res | Cost-effectiveness of 5-FU/SA for actinic keratosis in Spain |
| [24472429](https://pubmed.ncbi.nlm.nih.gov/24472429/) | 2014 | Review (safety) | J Am Acad Dermatol | Review of toxicity/salicylism risk from topical salicylic acid preparations |
| [32886029](https://pubmed.ncbi.nlm.nih.gov/32886029/) | 2022 | Systematic Review | J Dermatolog Treat | Treatment options (incl. keratolytics) for keratosis pilaris and variants |
| [17298101](https://pubmed.ncbi.nlm.nih.gov/17298101/) | 2007 | Review | Am J Clin Dermatol | Review of acquired palmoplantar keratoderma management |

### Keratinization Disease (broad category — mostly case-based evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23986157](https://pubmed.ncbi.nlm.nih.gov/23986157/) | 2013 | Double-blind RCT | J Drugs Dermatol | 20% alpha/poly hydroxy acid cream reduces scaling in chronic plaque psoriasis |
| [30972839](https://pubmed.ncbi.nlm.nih.gov/30972839/) | 2019 | Mechanistic | Exp Dermatol | Salicylic acid effects on follicular over-keratinization pathway (AMPK/SREBP1) |
| [41231204](https://pubmed.ncbi.nlm.nih.gov/41231204/) | 2025 | Preclinical (mouse) | J Drug Target | Salicylic-acid gel component in nanoemulsion for imiquimod-induced psoriasis model |
| [29077501](https://pubmed.ncbi.nlm.nih.gov/29077501/) | 2017 | Review (case-based) | J Am Podiatr Med Assoc | Management of plantar keratodermas, lessons from Pachyonychia Congenita |
| [11976541](https://pubmed.ncbi.nlm.nih.gov/11976541/) | 2002 | Review | Ann Dermatol Venereol | Review of xerosis and disordered keratinization pathophysiology |
| [29500825](https://pubmed.ncbi.nlm.nih.gov/29500825/) | 2018 | Case report | J Dermatol | Punctate palmoplantar keratoderma type I treated with acitretin + topical salicylic acid |
| [36812285](https://pubmed.ncbi.nlm.nih.gov/36812285/) | 2022 | Case report | Acta Dermatovenerol Croat | Segmental Darier disease case |
| [17511940](https://pubmed.ncbi.nlm.nih.gov/17511940/) | 2007 | Case report | Dermatol Online J | Keratosis follicularis (Darier-White disease) with unusual palmoplantar keratoderma |
| [31364784](https://pubmed.ncbi.nlm.nih.gov/31364784/) | 2019 | Case report | Dermatol Ther | Pachyonychia congenita responding to combined surgical/medical (incl. topical) therapy |
| [28223752](https://pubmed.ncbi.nlm.nih.gov/28223752/) | 2017 | Case report | Ann Dermatol | Terra firma-forme dermatosis treated with salicylic acid alcohol peeling |

### Osteoarthritis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14592543](https://pubmed.ncbi.nlm.nih.gov/14592543/) | 2003 | Mechanistic Review | Thromb Res | Historical review of aspirin/salicylate mechanism of action |
| [20547600](https://pubmed.ncbi.nlm.nih.gov/20547600/) | 2010 | RCT | Postgrad Med J | Subcutaneous sodium salicylate injection for thumb osteoarthritis pain |
| [41394718](https://pubmed.ncbi.nlm.nih.gov/41394718/) | 2025 | Preclinical (animal) | bioRxiv (preprint) | Poly-salicylic-acid particles reduce pain and structural damage in post-traumatic OA model |
| [38785813](https://pubmed.ncbi.nlm.nih.gov/38785813/) | 2024 | Preclinical (rat) | Biology | Salicylic-acid-iron-oxide nanoparticles alleviate histological lesions in MIA-induced knee OA |
| [7361087](https://pubmed.ncbi.nlm.nih.gov/7361087/) | 1980 | Double-blind comparative | Schweiz Med Wochenschr | Diflunisal vs. acetylsalicylic acid in hip/knee osteoarthritis (12-week comparison) |
| [331427](https://pubmed.ncbi.nlm.nih.gov/331427/) | 1977 | RCT (historical) | Rev Med Chile | Fenbufen vs. acetylsalicylic acid in osteoarthritis treatment |
| [17688170](https://pubmed.ncbi.nlm.nih.gov/17688170/) | 2007 | Small RCT | Niger Q J Hosp Med | TENS vs. sodium salicylate iontophoresis for knee osteoarthritis |
| [6988202](https://pubmed.ncbi.nlm.nih.gov/6988202/) | 1980 | Review | Drugs | Diflunisal (salicylate derivative) pharmacology and use in OA pain |
| [2754669](https://pubmed.ncbi.nlm.nih.gov/2754669/) | 1989 | In vitro | J Rheumatol | Sodium salicylate effects on proteoglycan metabolism of osteoarthritic cartilage |
| [12244878](https://pubmed.ncbi.nlm.nih.gov/12244878/) | 2002 | Review | Wien Med Wochenschr | Willow bark extract (natural salicylate source) pharmacology/clinical use review |

*Preclinical/mechanistic evidence noted (tier "pending"/unclassified in source) should be independently verified before citation in any regulatory submission.*

---

## Malaysia Market Information

Total registrations: **71 licenses**, market status **Marketed**. Individual authorization records (license number, product name, dosage form, approved indication text) were returned as blank fields in this data pull and are not available for tabulation — this should be resolved by re-querying NPRA registration data before any label-alignment decision is made.

---

## Safety Considerations

No populated safety fields (key warnings, contraindications, or drug–drug interactions) were returned in this data pull — flagged as data gap DG001 (**Blocking severity**: "cannot proceed to S1 safety pre-assessment"). Please refer to the package insert for safety information.

One safety-relevant point does emerge from the literature evidence itself and is worth flagging independently of the missing safety fields: topical salicylic acid carries a documented, if uncommon, risk of **salicylism (salicylate toxicity)** with high-concentration or large-surface-area/prolonged use (PMID [24472429](https://pubmed.ncbi.nlm.nih.gov/24472429/)) — relevant to any expanded indication involving larger treatment areas (e.g., truncal acne, extensive keratoderma) or pediatric/renal-impaired populations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (acne, plantar wart, acquired/actinic keratosis) / Hold (keratinization disease, osteoarthritis)**

**Rationale:**
- Acne and plantar wart already have L1 evidence (34 and 5 trials respectively, including head-to-head RCTs) and reflect well-established clinical/OTC use — the main remaining work is regulatory label alignment, not new efficacy research.
- Acquired/actinic keratosis (L2) is supported by an existing approved combination product (5-FU 0.5%/SA 10%, e.g., Actikerall) in other markets — a viable Malaysia label-extension candidate pending local safety data.
- Keratinization disease (L3, rank 1 by TxGNN score) and osteoarthritis (L3) rest on case reports, small/dated trials, or 2024–2025 preclinical work only — real repurposing hypotheses, but not yet actionable without dedicated studies.
- The TxGNN score field itself (0.0 across all five candidates) appears to be a data-population defect and should not be used to prioritize among these five indications until corrected.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain actual NPRA label warnings/contraindications before any S1 safety assessment
- Resolve DG002 (High): obtain a verified DrugBank/literature-sourced MOA statement
- Re-query NPRA registration data to populate individual license records (product name, dosage form, approved indication text) — current records are blank
- Confirm/correct the TxGNN score field (currently 0.0 for all candidates, likely a pipeline defect)
- For osteoarthritis specifically: manually verify NCT03277573 and NCT04066426, as neither trial's listed intervention is unambiguously salicylic acid itself
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

