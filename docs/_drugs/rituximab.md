---
layout: default
title: Rituximab
parent: Low Evidence (L4-L5)
nav_order: 599
evidence_level: L5
indication_count: 5
---

# Rituximab
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

# Rituximab: From CD20+ B-Cell Malignancies to Five TxGNN-Predicted Indications (One Genuinely Novel)

## One-Sentence Summary

Rituximab is a chimeric anti-CD20 monoclonal antibody originally used to treat CD20-positive B-cell malignancies. TxGNN returned five predicted indications for this candidate, but four of them (non-Hodgkin lymphoma, rheumatoid arthritis, mantle cell lymphoma, and "B-cell neoplasm" broadly) are **already globally approved uses of rituximab** — the model is reproducing known labels rather than proposing something new — while only **Langerhans Cell Histiocytosis (LCH)** represents a genuinely novel repurposing candidate, and it is currently supported only by a handful of case reports (no dedicated clinical trials).

## Quick Overview

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Status vs. Rituximab |
|------|----------------------|-------------|-----------------|-----------------|-----------------|------------------------|
| 1 | Non-Hodgkin Lymphoma (familial) | 0.00%* | L1 | S3 | Proceed with Guardrails | Already-approved indication (model validation) |
| 2 | Rheumatoid Arthritis | 0.00%* | L1 | S3 | Proceed with Guardrails | Already-approved indication (model validation) |
| 3 | Mantle Cell Lymphoma | 0.00%* | L1 | S3 | Proceed with Guardrails | Already-approved indication (model validation) |
| 4 | B-cell Neoplasm (general) | 0.00%* | L1 | S3 | Proceed with Guardrails | Umbrella category covering multiple already-approved uses |
| 5 | Langerhans Cell Histiocytosis | 0.00%* | L4 | S1 | Research Question | **Genuinely novel candidate** — weak evidence |

\* All five `txgnn.score` values in the evidence pack are 0.0 — this looks like an unpopulated/placeholder field rather than a meaningful confidence score, and should be treated as a data-quality gap in the prediction pipeline rather than as "no signal."

| Item | Content |
|------|------|
| Original Indication | CD20-positive B-cell Non-Hodgkin Lymphoma (globally established original indication; the evidence pack's own `drug.original_indications` and Malaysia license `approved_indication_text` fields are empty, so this is not confirmed against local label text) |
| Malaysia Market Status | Marketed (Marketed) |
| Number of Registrations | 9 |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`, flagged as data gap DG002/High severity). Based on well-established public information, rituximab is a chimeric murine/human anti-CD20 monoclonal antibody that binds CD20 on the surface of B lymphocytes and depletes them via complement-dependent cytotoxicity, antibody-dependent cellular cytotoxicity, and direct apoptosis. Its efficacy in CD20-positive B-cell malignancies is well proven, and the same B-cell-depletion mechanism is mechanistically applicable to autoimmune conditions driven by pathogenic B-cell/autoantibody activity.

**Indications 1–4 (NHL, RA, MCL, B-cell neoplasm)** are not novel predictions — they are indications for which rituximab already holds regulatory approval internationally (NHL/CLL/MCL since the late 1990s–2000s; RA in combination with methotrexate since 2006). The evidence pack's own `repurposing_rationale.mechanistic_link` field explicitly flags this for every one of these four entries, describing them as the model "reproducing known labels" rather than proposing something new. These are useful as **model-validation evidence** (TxGNN correctly recovers known drug–disease pairs) but should not be scored as repurposing opportunities.

**Indication 5 (Langerhans Cell Histiocytosis)** is the one genuinely novel candidate. LCH is a clonal proliferation of myeloid dendritic/histiocytic cells rather than a B-cell malignancy, so CD20 is not a primary therapeutic target in the lesion itself — the mechanistic link is indirect, hypothesized to act via depletion of reactive B-cell/lymphoid aggregates around lesions or via effects on LCH-associated neurodegenerative/autoimmune-like complications. This is reflected in the much lower evidence level (L4) and decision stage (S1, "Research Question").

## Clinical Trial Evidence

### Indication 1: Non-Hodgkin Lymphoma (familial)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Phase 3 | Active, not recruiting | 650 | B-NHL 2013: NHL-BFM/NOPHO standard-of-care protocol evaluating rituximab's role in mature aggressive B-cell NHL/leukemia in children and adolescents |
| [NCT06230224](https://clinicaltrials.gov/study/NCT06230224) | Phase 3 | Recruiting | 216 | OLYMPIA-4: odronextamab vs. rituximab-containing standard of care in relapsed/refractory aggressive B-NHL — rituximab regimen used as active comparator |
| [NCT04680052](https://clinicaltrials.gov/study/NCT04680052) | Phase 3 | Active, not recruiting | 654 | Tafasitamab + lenalidomide + rituximab vs. lenalidomide + rituximab in R/R follicular/marginal zone lymphoma |
| [NCT05171647](https://clinicaltrials.gov/study/NCT05171647) | Phase 3 | Active, not recruiting | 208 | Mosunetuzumab + polatuzumab vs. rituximab + gemcitabine/oxaliplatin (R-GemOx) in R/R aggressive B-NHL |
| [NCT03570892](https://clinicaltrials.gov/study/NCT03570892) | Phase 3 | Active, not recruiting | 331 | BELINDA: tisagenlecleucel vs. standard of care (post rituximab/anthracycline failure) in R/R aggressive B-NHL |
| [NCT02285062](https://clinicaltrials.gov/study/NCT02285062) | Phase 3 | Completed | 570 | Lenalidomide + R-CHOP (R2-CHOP) vs. placebo + R-CHOP in untreated ABC-type DLBCL |
| [NCT01200589](https://clinicaltrials.gov/study/NCT01200589) | Phase 3 | Terminated | 438 | Ofatumumab vs. rituximab monotherapy in indolent B-NHL relapsed after rituximab-containing therapy |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Phase 3 | Active, not recruiting | 510 | Zanubrutinib + rituximab vs. bendamustine + rituximab in untreated mantle cell lymphoma (transplant-ineligible) |
| [NCT04745832](https://clinicaltrials.gov/study/NCT04745832) | Phase 3 | Terminated | 82 | COASTAL: zandelisib + rituximab vs. standard immunochemotherapy in relapsed indolent NHL |
| [NCT00072449](https://clinicaltrials.gov/study/NCT00072449) | Phase 2 | Terminated | 12 | Rituximab monotherapy for refractory/relapsed primary CNS lymphoma |

### Indication 2: Rheumatoid Arthritis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00422383](https://clinicaltrials.gov/study/NCT00422383) | Phase 3 | Completed | 378 | Randomized double-blind study of MabThera re-treatment regimens + methotrexate in RA with inadequate response to MTX |
| [NCT00299104](https://clinicaltrials.gov/study/NCT00299104) | Phase 3 | Completed | 755 | Rituximab + MTX vs. MTX alone in MTX-naive active RA (registration-grade international study) |
| [NCT00443651](https://clinicaltrials.gov/study/NCT00443651) | Phase 3 | Completed | 578 | Open-label safety study of rituximab + other DMARDs in active RA with inadequate DMARD response |
| [NCT01272908](https://clinicaltrials.gov/study/NCT01272908) | Phase 3 | Completed | 120 | RESET: rituximab safety/effectiveness in RA after inadequate response to one prior anti-TNF agent |
| [NCT00299130](https://clinicaltrials.gov/study/NCT00299130) | Phase 3 | Completed | 511 | Placebo-controlled study of rituximab + MTX vs. MTX monotherapy in active RA |
| [NCT01332994](https://clinicaltrials.gov/study/NCT01332994) | Phase 3 | Completed | 519 | MIRAI: sequential tocilizumab then rituximab in DMARD-inadequate-responder RA |
| [NCT01382940](https://clinicaltrials.gov/study/NCT01382940) | Phase 4 | Completed | 351 | Safety of a more rapid rituximab infusion rate in moderate-to-severe RA |
| [NCT03853746](https://clinicaltrials.gov/study/NCT03853746) | Phase 4 | Completed | 10 | Short-term B-cell depletion and long-term disease activity/immune tolerance (also studied in MS) |
| [NCT01640548](https://clinicaltrials.gov/study/NCT01640548) | N/A | Completed | 320 | Retrospective chart review of biologic monotherapy (including rituximab) in RA |
| [NCT01557348](https://clinicaltrials.gov/study/NCT01557348) | N/A | Completed | 1239 | Global observational study of rituximab/alternative TNF-inhibitors in RA non-responders to a single TNF-inhibitor |

### Indication 3: Mantle Cell Lymphoma

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04566887](https://clinicaltrials.gov/study/NCT04566887) | Phase 2 | Recruiting | 105 | Acalabrutinib + R-CHOP in previously untreated MCL prior to autologous transplant |
| [NCT05245656](https://clinicaltrials.gov/study/NCT05245656) | Phase 2 | Recruiting | 90 | Randomized comparison of rituximab/bendamustine (RB) alternating with RB/cytarabine (RBAC) vs. RB alone in elderly transplant-ineligible MCL |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Phase 3 | Recruiting | 182 | Glofitamab monotherapy vs. investigator's choice (rituximab + bendamustine, or lenalidomide + rituximab) in R/R MCL |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Phase 3 | Active, not recruiting | 510 | Zanubrutinib + rituximab vs. bendamustine + rituximab in untreated, transplant-ineligible MCL |
| [NCT03567876](https://clinicaltrials.gov/study/NCT03567876) | Phase 2 | Completed | 141 | Addition of venetoclax to rituximab/bendamustine/cytarabine (V-RBAC) in high-risk elderly MCL |
| [NCT04849715](https://clinicaltrials.gov/study/NCT04849715) | Phase 3 | Withdrawn | 0 | Parsaclisib + bendamustine/rituximab vs. placebo + BR as first-line MCL therapy |
| [NCT06482684](https://clinicaltrials.gov/study/NCT06482684) | Phase 2 | Recruiting | 150 | Rituximab + ibrutinib induction followed by CAR-T consolidation vs. standard of care in high-risk MCL |
| [NCT00376961](https://clinicaltrials.gov/study/NCT00376961) | Phase 2 | Completed | 68 | R-CHOP + bortezomib induction followed by bortezomib maintenance in newly diagnosed MCL |
| [NCT00114738](https://clinicaltrials.gov/study/NCT00114738) | Phase 2 | Completed | 53 | EPOCH-rituximab-bortezomib induction with bortezomib maintenance vs. observation in untreated MCL |
| [NCT01389427](https://clinicaltrials.gov/study/NCT01389427) | Phase 1/2 | Completed | 41 | Temsirolimus + rituximab-based regimens (R-CHOP/R-FC/R-DHA) in relapsed/refractory MCL |

### Indication 4: B-cell Neoplasm (general)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02005471](https://clinicaltrials.gov/study/NCT02005471) | Phase 3 | Completed | 389 | Venetoclax + rituximab vs. bendamustine + rituximab in relapsed/refractory CLL (key registration trial) |
| [NCT01808599](https://clinicaltrials.gov/study/NCT01808599) | Phase 2 | Active, not recruiting | 112 | Chlorambucil + subcutaneous rituximab, then rituximab maintenance, in MALT lymphoma |
| [NCT03391466](https://clinicaltrials.gov/study/NCT03391466) | Phase 3 | Completed | 359 | ZUMA-7: axicabtagene ciloleucel vs. standard of care (rituximab-based) in R/R DLBCL |
| [NCT04361279](https://clinicaltrials.gov/study/NCT04361279) | Phase 3 | Completed | 421 | Rituximab biosimilar (SIBP-02) + CHOP vs. rituximab + CHOP in untreated CD20+ DLBCL |
| [NCT00312845](https://clinicaltrials.gov/study/NCT00312845) | Phase 3 | Completed | 676 | Bortezomib + rituximab vs. rituximab alone in relapsed/refractory follicular B-NHL |
| [NCT04212013](https://clinicaltrials.gov/study/NCT04212013) | Phase 3 | Active, not recruiting | 23 | Ibrutinib + rituximab vs. placebo + rituximab in treatment-naive marginal zone lymphoma |
| [NCT03777085](https://clinicaltrials.gov/study/NCT03777085) | Phase 3 | Unknown | 230 | TQB2303 + CHOP vs. rituximab + CHOP in untreated CD20+ DLBCL |
| [NCT04623541](https://clinicaltrials.gov/study/NCT04623541) | Phase 1/2 | Active, not recruiting | 195 | Epcoritamab (± venetoclax/pirtobrutinib) in R/R CLL and Richter's syndrome |
| [NCT02158091](https://clinicaltrials.gov/study/NCT02158091) | Phase 1/2 | Active, not recruiting | 32 | IPI-145 + fludarabine/cyclophosphamide/rituximab (FCR) in untreated, younger CLL |
| [NCT04980859](https://clinicaltrials.gov/study/NCT04980859) | Phase 3 | Unknown | 45 | Zanubrutinib + limited-course immunochemotherapy in newly treated CLL without 17p- |

### Indication 5: Langerhans Cell Histiocytosis

Trial coverage is sparse and largely off-target — none of the four trials returned by the search are dedicated rituximab-in-LCH trials:

| Trial Number | Phase | Status | Enrollment | Key Findings / Relevance Caveat |
|---------|------|------|------|---------|
| [NCT07270835](https://clinicaltrials.gov/study/NCT07270835) | Phase 4 | Recruiting | 40 | Zanubrutinib + rituximab for **secondary hemophagocytic lymphohistiocytosis (HLH) in B-cell lymphoma** — tangential to LCH itself (HLH can occur as an LCH complication, but this trial's population is B-cell lymphoma, not LCH) |
| [NCT01818908](https://clinicaltrials.gov/study/NCT01818908) | Phase 2 | Unknown | 50 | DA-EPOCH for NHL-associated HLH — graded "C" (low relevance), population is NHL, not LCH |
| [NCT03096782](https://clinicaltrials.gov/study/NCT03096782) | Phase 2 | Completed | 6 | Cord blood transplant engineering for leukemia/lymphoma — graded "C", unrelated to rituximab-LCH question |
| [NCT01471067](https://clinicaltrials.gov/study/NCT01471067) | Phase 1 | Completed | 33 | Cord blood fucosylation for hematologic malignancies — unrelated to LCH |

**No trial in this evidence pack directly tests rituximab in LCH.**

## Literature Evidence

### Indication 1: Non-Hodgkin Lymphoma (familial)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27345636](https://pubmed.ncbi.nlm.nih.gov/27345636/) | 2016 | RCT (Tier 1) | Lancet Oncology | GADOLIN: obinutuzumab + bendamustine vs. bendamustine alone in rituximab-refractory indolent NHL |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review (Tier 1) | Advances in Therapy | 20-year clinical experience review of rituximab across B-cell hematologic malignancies |
| [38010876](https://pubmed.ncbi.nlm.nih.gov/38010876/) | 2023 | Systematic Review (Tier 1) | Hematology | Meta-analysis of efficacy/safety of subcutaneous rituximab in NHL |
| [39234863](https://pubmed.ncbi.nlm.nih.gov/39234863/) | 2025 | RCT (Tier 2) | Haematologica | Real-life experience with rituximab + lenalidomide in relapsed/refractory indolent NHL |
| [32135128](https://pubmed.ncbi.nlm.nih.gov/32135128/) | 2020 | Systematic Review | Lancet Haematology | Cardiovascular adverse events with CHOP vs. R-CHOP in NHL — meta-analysis |
| [25499449](https://pubmed.ncbi.nlm.nih.gov/25499449/) | 2015 | Review | Blood | Transformed follicular NHL — natural history and outcomes |
| [37860948](https://pubmed.ncbi.nlm.nih.gov/37860948/) | 2024 | Retrospective | J Chemotherapy | Characteristics/predictors of infusion-related reactions to rituximab in B-NHL |
| [21958083](https://pubmed.ncbi.nlm.nih.gov/21958083/) | 2012 | Review | Leukemia & Lymphoma | Maintenance rituximab in follicular NHL — facts and controversies |
| [32303486](https://pubmed.ncbi.nlm.nih.gov/32303486/) | 2020 | Review | Clin Lymphoma Myeloma Leuk | Management of adverse events from rituximab + lenalidomide in indolent/low-grade NHL |
| [40749164](https://pubmed.ncbi.nlm.nih.gov/40749164/) | 2025 | Preclinical | Blood | Glofitamab (CD20×CD3 T-cell engager) combinations — preclinical NHL models |

### Indication 2: Rheumatoid Arthritis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31099191](https://pubmed.ncbi.nlm.nih.gov/31099191/) | 2019 | Systematic Review (Tier 1) | Int J Rheum Dis | Infection risk of rituximab vs. non-rituximab treatment in RA |
| [41004196](https://pubmed.ncbi.nlm.nih.gov/41004196/) | 2025 | Systematic Review (Tier 1) | Expert Opin Biol Ther | Efficacy/safety of rituximab in RA-associated interstitial lung disease |
| [31446557](https://pubmed.ncbi.nlm.nih.gov/31446557/) | 2019 | Systematic Review/Meta-analysis (Tier 1) | BioDrugs | Comparative efficacy/safety of biosimilar vs. originator rituximab in RA and NHL |
| [19758217](https://pubmed.ncbi.nlm.nih.gov/19758217/) | 2009 | Cohort (Tier 2) | Ann NY Acad Sci | Long-term clinical, biologic, and pharmacogenetic effects of rituximab in RA |
| [33638167](https://pubmed.ncbi.nlm.nih.gov/33638167/) | 2021 | Pharmacokinetic study | Fundam Clin Pharmacol | Variability of rituximab and tocilizumab trough concentrations in RA |
| [16920570](https://pubmed.ncbi.nlm.nih.gov/16920570/) | 2006 | Review | Autoimmunity Reviews | Treatment of RA with rituximab — early update and possible indications |
| [17896839](https://pubmed.ncbi.nlm.nih.gov/17896839/) | 2007 | Review | BioDrugs | Rituximab in RA — pivotal placebo-controlled trial summary |
| [26692536](https://pubmed.ncbi.nlm.nih.gov/26692536/) | 2016 | Network Meta-analysis | Int J Rheum Dis | Bayesian NMA comparing tocilizumab, rituximab, abatacept, tofacitinib in TNF-inadequate-responder RA |
| [21925447](https://pubmed.ncbi.nlm.nih.gov/21925447/) | 2011 | Systematic Review | Reumatologia Clinica | Systematic review of rituximab efficacy and safety in RA |
| [38693680](https://pubmed.ncbi.nlm.nih.gov/38693680/) | 2024 | Survey | Musculoskeletal Care | Patient/rheumatologist perceptions on rituximab dose reduction in RA |

### Indication 3: Mantle Cell Lymphoma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38669626](https://pubmed.ncbi.nlm.nih.gov/38669626/) | 2024 | RCT (Tier 1) | Blood | LyMa-101: obinutuzumab vs. rituximab in transplant-eligible MCL, long-term outcome |
| [30348538](https://pubmed.ncbi.nlm.nih.gov/30348538/) | 2018 | RCT Phase 3 (Tier 1) | Lancet Oncology | VR-CAP vs. R-CHOP in transplant-ineligible untreated MCL — final OS results |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | RCT (Tier 1) | Lancet | ENRICH: ibrutinib + rituximab vs. standard immunochemotherapy in untreated MCL (age 60+) |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | RCT Phase 3 (Tier 1) | Future Oncology | Zanubrutinib + rituximab vs. bendamustine + rituximab in transplant-ineligible MCL |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Pooled analysis | Blood Advances | Rituximab/bendamustine and rituximab/cytarabine induction for transplant-eligible MCL |
| [36469833](https://pubmed.ncbi.nlm.nih.gov/36469833/) | 2023 | RCT long-term follow-up | J Clin Oncol | European MCL Network trial — high-dose cytarabine + ASCT, long-term follow-up |
| [30033656](https://pubmed.ncbi.nlm.nih.gov/30033656/) | 2018 | Systematic Review/Meta-analysis | Am J Hematol | Rituximab maintenance therapy for MCL — systematic review and meta-analysis |
| [39023870](https://pubmed.ncbi.nlm.nih.gov/39023870/) | 2024 | Commentary | Blood | "Is rituximab retro in mantle cell lymphoma?" — perspective on evolving standard of care |
| [38678093](https://pubmed.ncbi.nlm.nih.gov/38678093/) | 2024 | RCT Phase 3 | Leukemia | Addition of bortezomib to rituximab/cytarabine/dexamethasone in R/R MCL |
| [28988912](https://pubmed.ncbi.nlm.nih.gov/28988912/) | 2017 | Commentary | Lancet Oncology | Maintenance rituximab in mantle-cell lymphoma |

### Indication 4: B-cell Neoplasm (general)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20647199](https://pubmed.ncbi.nlm.nih.gov/20647199/) | 2010 | RCT (Tier 1) | NEJM | RAVE trial: rituximab vs. cyclophosphamide for ANCA-associated vasculitis |
| [33661537](https://pubmed.ncbi.nlm.nih.gov/33661537/) | 2021 | Review (Tier 1) | Am J Hematol | 2021 update on DLBCL — risk stratification and management, R-CHOP as mainstay |
| [32482755](https://pubmed.ncbi.nlm.nih.gov/32482755/) | 2020 | Review (Tier 2, mechanistic) | Haematologica | Regulation and function of CD20 — biology underlying anti-CD20 therapy |
| [32933335](https://pubmed.ncbi.nlm.nih.gov/32933335/) | 2021 | Review | Expert Opin Biol Ther | Anti-CD20 treatment for B-cell malignancies — current status and future directions |
| [28983819](https://pubmed.ncbi.nlm.nih.gov/28983819/) | 2017 | Review | Advances in Therapy | Subcutaneous rituximab for B-cell hematologic malignancies — scientific rationale |
| [18240027](https://pubmed.ncbi.nlm.nih.gov/18240027/) | 2008 | Review | Clin Rev Allergy Immunol | Rituximab beyond simple B-cell depletion — relevance to autoimmune B-cell disorders |
| [12710588](https://pubmed.ncbi.nlm.nih.gov/12710588/) | 2002 | Review | Anti-Cancer Drugs | Rituximab in B-cell disorders other than NHL |
| [20194898](https://pubmed.ncbi.nlm.nih.gov/20194898/) | 2010 | Preclinical | Blood | Engineering of GA101 (obinutuzumab) as enhanced next-gen anti-CD20 antibody vs. rituximab |
| [25499448](https://pubmed.ncbi.nlm.nih.gov/25499448/) | 2015 | Review | Blood | DLBCL — optimizing outcome in the context of clinical/biologic heterogeneity |
| [33171490](https://pubmed.ncbi.nlm.nih.gov/33171490/) | 2021 | Review | Blood | Treatment of Burkitt lymphoma in adults |

### Indication 5: Langerhans Cell Histiocytosis

Literature specific to rituximab in LCH is very limited; most items returned by the broader "histiocytosis" search are about unrelated non-Langerhans disorders (Rosai-Dorfman disease, necrobiotic xanthogranuloma, Erdheim-Chester disease) and are only tangentially relevant:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30596314](https://pubmed.ncbi.nlm.nih.gov/30596314/) | 2018 | Case series (Tier 3) | Pediatr Hematol Oncol | **The only directly on-topic paper**: rituximab therapy for LCH-associated neurologic dysfunction |
| [18351339](https://pubmed.ncbi.nlm.nih.gov/18351339/) | 2008 | Case report | Ann Hematol | LCH mimicking relapse in a follicular lymphoma patient — diagnostic overlap, not treatment evidence |
| [23256832](https://pubmed.ncbi.nlm.nih.gov/23256832/) | 2012 | Case series | Vnitrni Lekarstvi | Lenalidomide (not rituximab) in rare blood disorders including LCH — background only |
| [22681714](https://pubmed.ncbi.nlm.nih.gov/22681714/) | 2013 | Case report | Actas Dermosifiliogr | Juvenile xanthogranuloma (non-Langerhans) + follicular lymphoma treated with chemo + rituximab |
| [15561688](https://pubmed.ncbi.nlm.nih.gov/15561688/) | 2004 | Review | Hematology Am Soc Hematol Educ Program | Overview of atypical cellular/histiocytic disorders including LCH |

## Malaysia Market Information

Per NPRA data, rituximab has **9 total registrations** and is currently **marketed** in Malaysia. However, the license-level fields returned in this evidence pack (authorization numbers, product names, dosage forms, manufacturers, approved indication text) are all empty — this appears to be an extraction gap in the NPRA data source rather than an absence of registrations, and should be re-pulled before this candidate proceeds further.

## Cytotoxicity

Rituximab's predicted/established uses span both oncology (NHL, CLL, MCL) and non-oncology autoimmune disease (RA), so a cytotoxicity profile is included given the oncology use cases.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Low-to-moderate; primary hematologic effect is B-lymphocyte depletion rather than broad myelosuppression, though neutropenia (including delayed-onset) is reported, particularly in combination regimens (e.g., R-CHOP, R-bendamustine) |
| Emetogenicity Classification | Low (as monotherapy); infusion-related reactions (fever, chills, hypotension) are the more clinically significant acute-administration risk — see PMID 37860948 above |
| Monitoring Items | CBC with differential, immunoglobulin levels, hepatitis B status/reactivation risk (per known anti-CD20 class risk), infusion-related reaction monitoring during administration |
| Handling Protection | As a biologic monoclonal antibody, standard hazardous-drug/biologic handling precautions apply; does not require conventional cytotoxic chemotherapy handling protocols |

Detailed toxicity data specific to this evidence pack was not available — please refer to the package insert warnings and precautions for definitive guidance.

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack's safety fields (`key_warnings`, `contraindications`, `ddi.interactions`) were not populated (data gap DG001, flagged as **Blocking severity** — "cannot enter S1 safety pre-screening" — remediation: retrieve and parse the TFDA/NPRA package insert PDF).

## Conclusion and Next Steps

**Decision: Mixed — see per-indication breakdown**

**Rationale:**
- Indications 1–4 (NHL, RA, MCL, B-cell neoplasm) are **already-approved uses of rituximab**, not novel repurposing candidates — TxGNN is validating known drug–disease pairs here, which is useful confirmation of model reliability but should not be counted as new pipeline opportunities. These carry L1 evidence and a "Proceed with Guardrails" label only in the sense of confirming existing clinical practice, not exploring something new.
- Indication 5 (Langerhans Cell Histiocytosis) is the only genuinely novel candidate, but evidence is currently limited to a single pediatric case series (L4, "Research Question" stage) with no supporting clinical trials directly testing rituximab in LCH.

**To proceed, the following is needed:**
- Resolve the Blocking-severity safety data gap (DG001): retrieve and parse the TFDA/NPRA package insert for warnings, contraindications, and DDI data before any S1 safety pre-screening can occur.
- Resolve the MOA data gap (DG002) via DrugBank API query to confirm mechanism-of-action classification.
- Re-pull Malaysia NPRA license-level detail (authorization numbers, product names, indication text) — all 9 registrations currently have empty records.
- Investigate the `txgnn.score = 0.0` anomaly across all five predictions — this field appears unpopulated and should not be interpreted as a real confidence score.
- If pursuing LCH specifically: commission a targeted literature/trial search restricted to "Langerhans cell histiocytosis" + "rituximab" (the current broad "histiocytosis" query returned mostly off-target results for unrelated non-Langerhans disorders) and consider whether a dedicated pilot study is warranted given the case-report-only evidence base.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

