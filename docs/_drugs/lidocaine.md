---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 5
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Dermatitis

## One-Sentence Summary

Lidocaine is a well-established local anesthetic and class Ib antiarrhythmic, widely used for procedural pain management and ventricular arrhythmia treatment.
The TxGNN model predicts it may be effective for **dermatitis** as its top-ranked new indication (rank #1), supported by **8 clinical trials** and **20 publications**; four additional predicted indications — hemorrhoid, premature ejaculation, urethritis, and mite infestation — are also evaluated in this report.
Evidence strength spans from **L1** (premature ejaculation, EMA-approved product already exists) to **L5** (mite infestation, model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia; ventricular arrhythmia (class Ib antiarrhythmic) |
| Primary Predicted Indication (TxGNN Rank #1) | Dermatitis |
| TxGNN Prediction Score | Not available in current release (extraction pending) |
| Evidence Level (Dermatitis) | L3 — Mechanistic studies, observational data, small exploratory trials |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 56 |
| Recommended Decision (Dermatitis) | Hold |

---

## Why is This Prediction Reasonable?

Lidocaine is a voltage-gated sodium channel blocker acting on Nav1.1–Nav1.9 subtypes, inhibiting membrane depolarisation and preventing action potential propagation in both peripheral neurons and cardiac tissue. This mechanism underlies its local anesthetic and antiarrhythmic properties. Although detailed MOA data was not available in the Evidence Pack (Data Gap DG002), lidocaine's pharmacology is extensively characterised in the literature.

For atopic dermatitis, the repurposing rationale centres on neuro-immune crosstalk. Atopic dermatitis involves aberrant signalling between sensory neurons and immune cells: Nav1.7 and Nav1.8 — the dominant sodium channel subtypes in nociceptive C-fibres — mediate both pruritus and neurogenic inflammation. A 2023 mechanistic study (*British Journal of Pharmacology*, PMID 36521846) demonstrated that intravenous lidocaine alleviates atopic dermatitis inflammation and pruritus by blocking these sensory neuron subpopulations and suppressing Th2 cytokines (IL-4, IL-13, TSLP). A complementary 2016 study (*J Allergy Clin Immunol*, PMID 26371835) showed that lidocaine also modulates regulatory T cell (Treg) activity in atopic dermatitis, suggesting an immunomodulatory dimension beyond analgesia alone.

Topical lidocaine formulations have been used in dermatology for decades (EMLA cream for procedures; ORTODERMINA® for wound-related skin pain), providing a well-understood safety and delivery framework. The gap between established procedural analgesia and disease-modifying therapy for dermatitis remains real, but the mechanistic bridge — sensory neuron blockade reducing neuro-immune amplification — is biologically coherent. A properly powered Phase 2 RCT is the logical next step.

---

## Clinical Trial Evidence

*Trials for Dermatitis — TxGNN rank #1*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07067541](https://clinicaltrials.gov/study/NCT07067541) | N/A | Completed | 25 | Direct study of topical Lidocaine cream ± moisturizing cream for atopic dermatitis; twice-daily 4-week bilateral-limb design; most directly relevant trial identified |
| [NCT03720119](https://clinicaltrials.gov/study/NCT03720119) | N/A | Completed | 78 | ORTODERMINA® (Lidocaine HCl) for wound pain and skin inflammation; multicenter observational study supporting topical Lidocaine for skin inflammatory conditions |
| [NCT03630198](https://clinicaltrials.gov/study/NCT03630198) | Phase 4 | Completed | 31 | Lidocaine as adjunct to intralesional corticosteroid injection in dermatology; safety confirmed and pain reduction quantified |
| [NCT06387212](https://clinicaltrials.gov/study/NCT06387212) | N/A | Recruiting | 20 | HA35 hyaluronan fragment combined with negative pressure microneedle for chronic skin inflammation; Lidocaine used as procedural anesthetic only |
| [NCT05145959](https://clinicaltrials.gov/study/NCT05145959) | N/A | Unknown | 30 | Meibomian gland probing in Stevens-Johnson Syndrome/TEN; Lidocaine as procedural anesthetic; no direct dermatitis treatment data |

> No completed Phase 2 or Phase 3 RCT directly evaluating Lidocaine as a disease-modifying treatment for dermatitis was identified in the current evidence set.

---

## Literature Evidence

*Literature for Dermatitis — TxGNN rank #1*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36521846](https://pubmed.ncbi.nlm.nih.gov/36521846/) | 2023 | Mechanistic Study | British Journal of Pharmacology | IV lidocaine alleviates atopic dermatitis inflammation and pruritus by blocking Nav1.7/Nav1.8 sensory neurons; Th2 cytokines (IL-4, IL-13, TSLP) suppressed; core mechanistic rationale for this prediction |
| [26371835](https://pubmed.ncbi.nlm.nih.gov/26371835/) | 2016 | Experimental | J Allergy & Clin Immunol | Lidocaine modulates regulatory T cells in atopic dermatitis; immunomodulatory effect beyond pure channel blockade |
| [41046125](https://pubmed.ncbi.nlm.nih.gov/41046125/) | 2026 | Review | Ann Allergy Asthma Immunol | Comprehensive 2026 update on chronic pruritus mechanisms; TH2 cytokines, C-fibre/Aδ-fibre pathways directly relevant to lidocaine mechanism |
| [38809527](https://pubmed.ncbi.nlm.nih.gov/38809527/) | 2024 | Review | JAMA | Chronic pruritus review; 22% lifetime prevalence; discusses role of neuro-immune pathways and management gaps |
| [29551371](https://pubmed.ncbi.nlm.nih.gov/29551371/) | 2023 | Case Series | JAAD | 2% topical Lidocaine gel for peristomal dermatitis; novel technique for localized inflammatory skin lesion |
| [21847539](https://pubmed.ncbi.nlm.nih.gov/21847539/) | 2012 | Pilot Study | Support Care Cancer | Topical amitriptyline/ketamine/lidocaine (AKL) combination for neuropathic pain from radiation dermatitis; pilot feasibility confirmed |
| [2563603](https://pubmed.ncbi.nlm.nih.gov/2563603/) | 1989 | Clinical Study | Acta Derm Venereol | EMLA absorption on normal vs diseased skin; significantly faster uptake on eczematous and inflamed skin — critical dosing and safety implication |
| [38934159](https://pubmed.ncbi.nlm.nih.gov/38934159/) | 2025 | Case Report | Dermatitis | Allergic contact dermatitis caused by Lidocaine and sodium metabisulfite — key safety signal for the dermatitis repurposing indication |

---

## Additional Predicted Indications

---

### Indication 2: Mite Infestation (TxGNN Rank #2)

- **Evidence Level**: L5 — Model prediction only
- **Clinical Trials**: None identified
- **Literature**: 1 tangentially related reference (PMID 1664794, 1991 paediatric dermatology review; no lidocaine-mite content)
- **Mechanistic Rationale**: No established direct mechanism. Theoretical sodium channel effects on arthropod neurology are entirely unsubstantiated by any preclinical or clinical data.
- **Decision: Hold** — No biological or clinical rationale supports pursuing this prediction. Preclinical evidence of anti-mite activity would be a prerequisite for any further evaluation.

---

### Indication 3: Urethritis (TxGNN Rank #3)

- **Evidence Level**: L3 — Multiple RCTs and meta-analyses for urethral procedural analgesia; no direct evidence for treating urethritis as a disease entity

**Key Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33759297](https://pubmed.ncbi.nlm.nih.gov/33759297/) | 2021 | Meta-Analysis | Int J Clin Practice | Systematic review: lidocaine gel vs plain lubricant for female urethral catheterisation; efficacy assessment |
| [28917955](https://pubmed.ncbi.nlm.nih.gov/28917955/) | 2017 | Meta-Analysis | J Pediatrics | Lidocaine gel vs non-anesthetic gel for paediatric bladder catheterisation; efficacy and safety confirmed |
| [31307254](https://pubmed.ncbi.nlm.nih.gov/31307254/) | 2019 | RCT | J Int Med Res | Dispogel vs Cathejell (2% lidocaine formulations) in cystoscopy; both effective for procedural pain |
| [19701033](https://pubmed.ncbi.nlm.nih.gov/19701033/) | 2009 | RCT | Obstetrics & Gynecology | Lidocaine jelly vs plain gel for urethral catheterisation; lidocaine significantly more effective |
| [29944227](https://pubmed.ncbi.nlm.nih.gov/29944227/) | 2016 | Pilot / Case Series | Clin Exp Obstet Gynecol | Urethral instillation of clobetasol + lidocaine for urethral pain syndrome; promising symptom improvement |

- **Mechanistic Rationale**: Sodium channel blockade reduces urethral pain and voiding discomfort; anti-inflammatory action may attenuate mucosal inflammation; alkalised formulations improve mucosal penetration (PMID 11371877). This is symptomatic treatment, not pathogen-directed therapy.
- **Decision: Hold** — Lidocaine's established role in urethral procedural analgesia does not constitute evidence for treating urethritis. A targeted pilot study in urethral pain syndrome or post-infectious urethral symptom management is required before advancing.

---

### Indication 4: Hemorrhoid (TxGNN Rank #4)

- **Evidence Level**: L2 — Multiple completed Phase 2 RCTs and one large prospective real-world study (n=1,000); multiple combination products globally marketed

**Key Clinical Trials:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03757078](https://clinicaltrials.gov/study/NCT03757078) | N/A | Completed | 1,000 | Fluocortolone + Lidocaine (Relief Pro®) for acute hemorrhoids; largest real-world study; significant symptom improvement over 3 visits |
| [NCT05348200](https://clinicaltrials.gov/study/NCT05348200) | Phase 2 | Completed | 304 | CITI-002 (novel Lidocaine formulation) for Grade II/III hemorrhoids; randomized double-blind dose-ranging RCT; completed 2023 |
| [NCT02689856](https://clinicaltrials.gov/study/NCT02689856) | Phase 2 | Completed | 211 | Lidocaine HCl ± hydrocortisone acetate for Grade I/II hemorrhoids; 14-day twice-daily RCT; dose-response characterised |
| [NCT04276298](https://clinicaltrials.gov/study/NCT04276298) | Phase 2/3 | Completed | 192 | Topical metronidazole vs diltiazem vs Lidocaine for post-haemorrhoidectomy pain; multicenter double-blind RCT |
| [NCT01961739](https://clinicaltrials.gov/study/NCT01961739) | Phase 2/3 | Unknown | 138 | Topical 2% Lidocaine for symptomatic hemorrhoids; CORRECTS scale primary endpoint |
| [NCT07295886](https://clinicaltrials.gov/study/NCT07295886) | N/A | Recruiting | 80 | Nifedipine 0.3% + Lidocaine 1.5% for acute uncomplicated hemorrhoidal disease; observational study with 30-day follow-up |
| [NCT06420388](https://clinicaltrials.gov/study/NCT06420388) | N/A | Recruiting | 400 | 2% Lidocaine gel for post-haemorrhoidectomy pain; large randomized double-blind controlled trial |

**Key Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40824576](https://pubmed.ncbi.nlm.nih.gov/40824576/) | 2025 | Review | JAMA | Hemorrhoidal disease review (~10 million US patients); lidocaine-containing topicals included in current management framework |
| [27383331](https://pubmed.ncbi.nlm.nih.gov/27383331/) | 2016 | Evidence Synthesis | Eur Rev Med Pharmacol Sci | Tribenoside + Lidocaine (Procto-Glyvenol®) for hemorrhoids; decades of clinical use and evidence summarised |
| [39945661](https://pubmed.ncbi.nlm.nih.gov/39945661/) | 2025 | Review | Minerva Surgery | Nifedipine + Lidocaine ointment for hemorrhoidal disease and anal fissure; established role in anorectal conditions confirmed |
| [40581544](https://pubmed.ncbi.nlm.nih.gov/40581544/) | 2025 | Retrospective Cohort | The Surgeon | Comparative efficacy of lidocaine-based vs nifedipine-based conservative therapies in acute hemorrhoidal disease |
| [31555338](https://pubmed.ncbi.nlm.nih.gov/31555338/) | 2019 | Clinical Review | Drugs in Context | Tribenoside + Lidocaine (Procto-Glyvenol®) in women with hemorrhoids; sex-specific evidence and clinical guidance |

- **Mechanistic Rationale**: Sodium channel blockade provides direct acute pain relief; anti-inflammatory effect (prostaglandin suppression, neurogenic inflammation reduction) reduces oedema; synergistic action with vasodilators (nifedipine → sphincter relaxation) or corticosteroids (fluocortolone → inflammation control) underpins the multi-component formulations already in use.
- **Decision: Proceed with Guardrails** — Multiple combination products (Procto-Glyvenol®, Ultraproct®, nifedipine/lidocaine ointment) are registered globally. A completed Phase 2 RCT (n=304) and the largest real-world study (n=1,000) provide sufficient regulatory foundation. Pathway in Malaysia: evaluate registration of an existing Lidocaine combination hemorrhoid product.

---

### Indication 5: Premature Ejaculation (TxGNN Rank #5)

- **Evidence Level**: L1 — Multiple completed Phase 2/3 RCTs, published systematic reviews and meta-analyses, and an EMA-approved product (Fortacin™) specifically for this indication

**Key Clinical Trials:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00556478](https://clinicaltrials.gov/study/NCT00556478) | Phase 2/3 | Completed | 256 | PSD502 (lidocaine/prilocaine topical spray) vs placebo for PE; multicenter RCT; primary IELT endpoint significantly met |
| [NCT04062357](https://clinicaltrials.gov/study/NCT04062357) | Phase 2 | Completed | 150 | Lidocaine 5% spray vs placebo for lifelong PE; randomized single-blind; significant IELT prolongation with good tolerability |
| [NCT03578783](https://clinicaltrials.gov/study/NCT03578783) | Phase 2 | Completed | 121 | PSD502 vs placebo using PEBEQ patient questionnaire; multicenter double-blind; patient-reported outcomes confirmed |
| [NCT02241460](https://clinicaltrials.gov/study/NCT02241460) | Phase 3 | Unknown | 120 | Promescent (lidocaine spray) vs placebo for PE; Phase 3 efficacy and safety |
| [NCT04703127](https://clinicaltrials.gov/study/NCT04703127) | Phase 3 | Unknown | 60 | Dapoxetine + Lidocaine 5% spray vs dapoxetine + tadalafil for dapoxetine-resistant lifelong PE |

**Key Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37664322](https://pubmed.ncbi.nlm.nih.gov/37664322/) | 2023 | Meta-Analysis | Cureus | Topical anesthetics (lidocaine-containing) vs placebo for PE; IELT significantly prolonged; pooled RCT evidence |
| [26599522](https://pubmed.ncbi.nlm.nih.gov/26599522/) | 2016 | Systematic Review | Sexual Health | EMLA and topical anesthetics for PE; multiple RCT evidence reviewed; efficacy and safety confirmed |
| [35314817](https://pubmed.ncbi.nlm.nih.gov/35314817/) | 2023 | RCT | Int J Impotence Research | Prilocaine/lidocaine spray (Fortacin™) dose- and time-finding study; guidance for clinical practice optimisation |
| [31896832](https://pubmed.ncbi.nlm.nih.gov/31896832/) | 2021 | RCT | Int J Impotence Research | Lidocaine 5% spray for lifelong PE (n=150); placebo-controlled; significant IELT improvement confirmed |
| [39935900](https://pubmed.ncbi.nlm.nih.gov/39935900/) | 2025 | RCT | Int J Sexual Health | On-demand tadalafil alone vs combined with lidocaine spray for comorbid ED and PE; combination benefit demonstrated |
| [33828264](https://pubmed.ncbi.nlm.nih.gov/33828264/) | 2022 | Retrospective Cohort | Int J Impotence Research | Real-life Fortacin™ use in 198 PE patients; treatment retention and patient satisfaction in clinical practice |
| [28408390](https://pubmed.ncbi.nlm.nih.gov/28408390/) | 2017 | Drug Review | Drug & Therapeutics Bulletin | Lidocaine/prilocaine spray for PE; regulatory context and evidence base summarised |

- **Mechanistic Rationale**: Penile hypersensitivity — heightened Nav channel activity in dorsal penile sensory nerve endings — is a proposed primary mechanism in lifelong PE. Topical lidocaine reduces penile sensitivity by blocking Nav channels, prolonging intravaginal ejaculatory latency time (IELT) without impairing erection. Fortacin™ (lidocaine 150 mg/mL + prilocaine 50 mg/mL metered-dose topical spray) received EMA approval in 2013 and is included in EAU/AUA treatment guidelines.
- **Decision: Proceed with Guardrails** — The strongest repurposing opportunity in this pack. Regulatory precedent exists (EMA-approved Fortacin™). Direct registration pathway available via NPRA abridged application referencing EMA approval.

---

## Malaysia Market Information

The NPRA database confirms **56 registered Lidocaine products** in Malaysia as of the query date (2026-03-04), confirming an active and established market presence. However, product-level details (authorisation numbers, product names, dosage forms, approved indications) were not returned in the current Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | Detailed registration data not returned in this release | — | — |

> **Recommended Action**: Request a full NPRA product registry extract for Lidocaine to: (1) identify current dosage forms on market (injectable, topical gel, spray, suppository); (2) determine whether any existing registration carries anorectal or sexual dysfunction labelling; (3) confirm whether Fortacin™ or equivalent is already registered.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical Safety Signals Identified from Evidence Literature**
>
> Two signals are directly relevant to this repurposing evaluation and must be addressed in any development plan:
>
> - **Allergic Contact Dermatitis Caused by Lidocaine** (PMIDs [38934159](https://pubmed.ncbi.nlm.nih.gov/38934159/), [16487290](https://pubmed.ncbi.nlm.nih.gov/16487290/), [19054423](https://pubmed.ncbi.nlm.nih.gov/19054423/)): Lidocaine is a recognised contact allergen. For the dermatitis repurposing indication, this is a critical paradox — the treatment agent may itself trigger or worsen the target disease. Patch testing prior to enrolment in any dermatitis trial is essential.
>
> - **Accelerated Systemic Absorption Through Atopic Skin** (PMIDs [2563603](https://pubmed.ncbi.nlm.nih.gov/2563603/), [27397059](https://pubmed.ncbi.nlm.nih.gov/27397059/)): EMLA application on eczematous/inflamed skin results in significantly faster lidocaine absorption compared to intact skin. A case of generalised seizures and methemoglobinemia was reported in a child with atopic dermatitis after topical EMLA. This limits the usable dose range and body surface area for topical dermatitis applications.

---

## Conclusion and Next Steps

### Decision Summary

| Indication | TxGNN Rank | Evidence Level | Decision |
|-----------|-----------|---------------|---------|
| Dermatitis | #1 | L3 | Hold |
| Mite Infestation | #2 | L5 | Hold |
| Urethritis | #3 | L3 | Hold |
| **Hemorrhoid** | **#4** | **L2** | **Proceed with Guardrails** |
| **Premature Ejaculation** | **#5** | **L1** | **Proceed with Guardrails** |

> Note: TxGNN rank reflects model prediction order, not clinical evidence strength. For premature ejaculation (rank #5), the evidence base is the strongest in this pack by a wide margin.

---

### Priority 1: Premature Ejaculation

**Decision: Proceed with Guardrails**

**Rationale:**
Fortacin™ (lidocaine 150 mg/mL + prilocaine 50 mg/mL topical spray) received EMA approval specifically for lifelong premature ejaculation, and multiple Phase 2/3 RCTs demonstrate significant IELT improvement. This represents the most immediately actionable pathway among all five predicted indications.

**To proceed, the following is needed:**
- Verify whether Fortacin™ or an equivalent lidocaine/prilocaine PE spray is already among the 56 registered products in Malaysia; if not, initiate NPRA abridged NDA referencing EMA approval
- Confirm that the metered-dose topical spray dosage form is covered under existing regulatory categories
- Obtain full Lidocaine package insert (Gap DG001) for local safety labelling adaptation
- Clarify whether scoring/recommendation fields for this indication (currently "pending") should be updated to L1 / Proceed with Guardrails

---

### Priority 2: Hemorrhoid

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Lidocaine combination products are marketed globally for hemorrhoidal disease with solid Phase 2 evidence and a large real-world dataset (n=1,000). A recently completed Phase 2 dose-ranging RCT (NCT05348200, n=304) provides a strong regulatory foundation.

**To proceed, the following is needed:**
- Audit all 56 registered Malaysia Lidocaine products for any anorectal or hemorrhoid labelling
- Evaluate regulatory pathway for registering a combination product (tribenoside+lidocaine or nifedipine+lidocaine formulation)
- Resolve Gap DG002 (DrugBank MOA data) to support mechanism documentation in regulatory submission
- Identify a local clinical champion for any bridging study, if required by NPRA

---

### Lower Priority Indications

- **Dermatitis (L3 — Hold)**: Mechanistically plausible (Nav1.7/Nav1.8 blockade, Th2 suppression), but the only directly relevant clinical trial enrolled just 25 patients with no comparative arm. The allergic contact dermatitis risk from Lidocaine adds complexity. A Phase 2 RCT with patch-test pre-screening and controlled dosing on limited body surface area is needed before advancing.
- **Urethritis (L3 — Hold)**: Procedural analgesia evidence is robust but does not translate to disease treatment. An exploratory study in urethral pain syndrome would bridge this gap.
- **Mite Infestation (L5 — Hold)**: No viable pathway identified. Deprioritise pending any preclinical signal.

---

### Pending Data Gaps

| Gap ID | Item | Priority | Recommended Action |
|--------|------|---------|-------------------|
| DG001 | NPRA package insert warnings and contraindications | Blocking | Download and parse Lidocaine NPRA monograph PDF |
| DG002 | Mechanism of action (MOA) data | High | Query DrugBank API for DB00281 |
| — | Full product-level NPRA registration details (56 products) | Medium | Full NPRA registry query with dosage form and indication fields |
| — | TxGNN prediction scores (all showing 0.0) | Low | Rerun TxGNN model with score export enabled |
| — | Scoring and recommendation fields for Premature Ejaculation (rank #5) | Medium | Populate evidence_level (L1), decision_stage (S2), and recommendation (Proceed with Guardrails) in Evidence Pack |

---

> **Disclaimer**: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. YMYL notice: All content is for research reference only and must not be used as a basis for clinical decisions without formal regulatory and medical review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

