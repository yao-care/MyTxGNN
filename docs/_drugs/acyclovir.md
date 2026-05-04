---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 5
---

# Acyclovir
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

# Acyclovir: From Herpes Simplex Infection to Herpes Zoster

## One-Sentence Summary

Acyclovir is a nucleoside analogue antiviral originally approved for the treatment of herpes simplex virus (HSV) infections, including genital herpes and mucocutaneous HSV disease. The TxGNN model's top-ranked prediction is **Herpes Zoster** (shingles), supported by multiple completed Phase 3 clinical trials and **20 indexed publications** confirming its first-line antiviral role in this condition. Notably, all five model predictions cover herpesvirus family diseases where Acyclovir already serves as a guideline-recommended treatment, reflecting strong mechanistic consistency across the herpesvirus spectrum.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (Malaysian NPRA license text fields were not captured in this Evidence Pack) |
| Predicted New Indication | Herpes Zoster |
| TxGNN Prediction Score | 0.00% (score data may not have been populated; rank 1 of 5 predictions) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 46 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack's DrugBank query. Based on established scientific knowledge, Acyclovir is a synthetic acyclic nucleoside analogue whose antiviral selectivity hinges entirely on **virus-encoded thymidine kinase (TK)**. Only virus-infected cells express the viral TK required to phosphorylate Acyclovir to its monophosphate form; host cell kinases then convert this intermediate to the active triphosphate (Acyclovir-TP). This two-step activation mechanism gives Acyclovir a therapeutic selectivity window of approximately 30–100 fold over host DNA polymerase — meaning it acts almost exclusively inside infected cells, sparing healthy tissue.

In the context of herpes zoster, the varicella-zoster virus (VZV) encodes a TK homolog (UL23) that efficiently phosphorylates Acyclovir. The resulting Acyclovir-TP competes with deoxyguanosine triphosphate and, upon incorporation into the growing viral DNA chain, acts as an obligate chain terminator, blocking further VZV replication. Clinically, early initiation of Acyclovir shortens the duration of active vesicular eruptions and significantly reduces the incidence and severity of postherpetic neuralgia (PHN) — the most debilitating long-term complication of herpes zoster.

The mechanistic bridge between the original indication (HSV infections) and herpes zoster is direct and well-characterised: both HSV and VZV are alpha-herpesviruses that share TK-dependent activation of Acyclovir. This explains why TxGNN ranked herpes zoster, herpes simplex encephalitis, herpes labialis, genital herpes, and broad HSV infectious disease as its five top predictions — all share the same fundamental pharmacological target. The model's output is consistent with Acyclovir's regulatory approval profile across these indications in the United States (FDA) and Europe (EMA).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03134196](https://clinicaltrials.gov/study/NCT03134196) | Phase 4 | Completed | 527 | Multi-centre, double-masked, placebo-controlled trial of suppressive Valacyclovir (Acyclovir prodrug) for one year in immunocompetent patients with Herpes Zoster Ophthalmicus (keratitis, uveitis); assesses long-term suppression safety and efficacy |
| [NCT01959841](https://clinicaltrials.gov/study/NCT01959841) | Phase 3 | Completed | 751 | Double-blind Valaciclovir-controlled study comparing ASP2151 (Amenamevir) 200 mg and 400 mg vs Valaciclovir 3000 mg/day in herpes zoster patients; Valaciclovir serves as the gold-standard active comparator |
| [NCT00002315](https://clinicaltrials.gov/study/NCT00002315) | Phase 3 | Completed | 400 | Double-blind multicenter study comparing oral 882C87 vs oral Acyclovir for localized herpes zoster in immunocompromised patients; directly tests Acyclovir's efficacy and tolerance in this high-risk population |
| [NCT01327144](https://clinicaltrials.gov/study/NCT01327144) | Phase 3 | Completed | 177 | Prospective randomised multicenter study comparing Famciclovir 500 mg vs Aciclovir 400 mg in herpes zoster; direct head-to-head comparative efficacy and safety data for Acyclovir |
| [NCT00209352](https://clinicaltrials.gov/study/NCT00209352) | Phase 3 | Completed | 120 | Randomised trial of long-term oral Acyclovir to prevent VZV reactivation during the first year after allogeneic bone marrow transplant; establishes prophylactic benefit in the highest-risk immunosuppressed population |
| [NCT00000953](https://clinicaltrials.gov/study/NCT00000953) | Phase 2 | Completed | 180 | Sorivudine (Brovavir) vs oral Acyclovir for localized herpes zoster in HIV-infected patients; one of the pivotal trials confirming Acyclovir's standard-of-care role specifically in HIV co-infected individuals |
| [NCT00487682](https://clinicaltrials.gov/study/NCT00487682) | Phase 2 | Completed | 403 | Dose-finding study of ASP2151 vs Valacyclovir hydrochloride in herpes zoster; Valacyclovir serves as active control providing dose-comparative PK and efficacy data |
| [NCT00652184](https://clinicaltrials.gov/study/NCT00652184) | Phase 2/3 | Unknown | 300 | Four-arm, double-blind, placebo-controlled comparison of topical Sorivudine cream 3% vs oral Valaciclovir vs combination vs placebo for herpes zoster in immunocompetent adults; Valaciclovir arm provides n=300 active-controlled efficacy benchmark |
| [NCT00900783](https://clinicaltrials.gov/study/NCT00900783) | Phase 2 | Completed | 373 | Randomised double-blind study of FV-100 at two doses vs Valacyclovir in acute herpes zoster; compares pain resolution and lesion healing with Valacyclovir as the active standard |
| [NCT01254630](https://clinicaltrials.gov/study/NCT01254630) | Phase 3 | Completed | 5305 | Large placebo-controlled trial of inactivated VZV vaccine (V212) in adult cancer patients receiving chemotherapy; documents the substantial herpes zoster disease burden in immunocompromised populations and the clinical necessity for antiviral prevention strategies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3941520](https://pubmed.ncbi.nlm.nih.gov/3941520/) | 1986 | Clinical Review | JAMA | Landmark review of Acyclovir's therapeutic advantages and adverse effects specifically in herpes zoster; summarises early controlled trials showing accelerated lesion healing and pain reduction |
| [27566094](https://pubmed.ncbi.nlm.nih.gov/27566094/) | 2016 | Comparative Study | In Vivo | Head-to-head prophylactic efficacy comparison of Acyclovir vs Valaciclovir against herpes zoster in immunocompromised haematological patients; includes cost-effectiveness simulation supporting Acyclovir as a cost-efficient prophylactic option |
| [8809466](https://pubmed.ncbi.nlm.nih.gov/8809466/) | 1996 | Review | Clin Microbiol Rev | Comprehensive review of VZV virology, epidemiology, and clinical management; documents the clinical evidence base for antiviral therapy including Acyclovir in herpes zoster across immunocompetent and immunocompromised hosts |
| [12449270](https://pubmed.ncbi.nlm.nih.gov/12449270/) | 2002 | Clinical Review | Am Fam Physician | Evaluation and management guidelines for Herpes Zoster Ophthalmicus; discusses the role of oral Acyclovir and its prodrugs in preventing ocular complications including keratitis and uveitis |
| [10794584](https://pubmed.ncbi.nlm.nih.gov/10794584/) | 2000 | Review | Am Fam Physician | Clinical management review of herpes zoster and postherpetic neuralgia; addresses antiviral therapy with Acyclovir as the cornerstone of treatment and its role in reducing PHN incidence |
| [6355050](https://pubmed.ncbi.nlm.nih.gov/6355050/) | 1983 | Review | J Antimicrob Chemother | Early evidence review: intravenous Acyclovir significantly resolved acute zoster skin rash; topical Acyclovir controlled herpes zoster kerato-uveitis; established the antiviral principle for both systemic and ocular manifestations |
| [12118839](https://pubmed.ncbi.nlm.nih.gov/12118839/) | 2002 | Review | Sem Pediatr Infect Dis | Reviews antiviral therapy for varicella and herpes zoster across paediatric populations; identifies Acyclovir as drug of choice with dosing guidance by immunological status and route of administration |
| [9675639](https://pubmed.ncbi.nlm.nih.gov/9675639/) | 1997 | Review | Intervirology | Reviews clinical trial evidence for Acyclovir and its prodrugs (Valaciclovir, Famciclovir) in acute herpes zoster; summarises efficacy on zoster-associated pain and lesion healing from large multicentre trials |
| [34137062](https://pubmed.ncbi.nlm.nih.gov/34137062/) | 2021 | Case Study | J Dermatol | Documents a case of Acyclovir-resistant herpes zoster infection successfully treated by Amenamevir; highlights the clinical importance of resistance surveillance and the need for second-line options in Acyclovir-refractory cases |
| [9707315](https://pubmed.ncbi.nlm.nih.gov/9707315/) | 1998 | Case Report | Eur J Clin Microbiol Infect Dis | Two HIV-infected patients with herpes zoster leukoencephalitis who achieved complete clinical recovery and full MRI lesion resolution after Acyclovir treatment; supports Acyclovir's CNS penetration and efficacy in severe neurological VZV complications |

---

## Malaysia Market Information

Acyclovir is confirmed as **marketed in Malaysia** with **46 product registrations** on file with NPRA (National Pharmaceutical Regulatory Agency of Malaysia). Individual registration records were not captured in this Evidence Pack data run; all five sampled license entries returned empty fields. The following reflects the available aggregate data:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | (46 registrations confirmed; individual product details not captured in this data run) | — | Please refer to NPRA Product Registration Search at npra.gov.my |

> **Note**: To obtain complete product listing including MAL numbers, brand names, dosage forms, and approved indication texts, query the [NPRA Product Registration database](https://www.npra.gov.my/) using "Acyclovir" as the active ingredient. Given 46 registrations, multiple oral (tablet/capsule), intravenous (powder for injection), topical (cream/ointment), and ophthalmic dosage forms are expected to be represented.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields in this Evidence Pack — including key warnings, contraindications, and drug interaction data — were recorded as data gaps. Formal safety assessment requires retrieval of the Malaysian package insert (仿單 / product information leaflet) from NPRA and/or the DrugBank safety profile for DB00787.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
All five TxGNN predictions for Acyclovir represent herpesvirus indications with L1 evidence strength (multiple completed Phase 3 randomised controlled trials). Acyclovir has over four decades of real-world clinical use, established global regulatory approvals (FDA, EMA, and 46 Malaysian registrations), and its mechanism of action is thoroughly characterised in the scientific literature. The model predictions align precisely with known pharmacology, confirming high mechanistic credibility rather than speculative repurposing.

**To proceed, the following is needed:**

- **NPRA license data retrieval**: Download and parse individual MAL registration records to populate product names, dosage forms, approved indication texts, and marketing authorisation numbers for all 46 registered products
- **Package insert safety review**: Retrieve and extract key warnings, contraindications, and special population precautions from the Malaysian product information leaflets to complete the safety assessment (currently blocking — classified as DG001 Severity: Blocking)
- **DrugBank MOA data retrieval**: Query DrugBank API for DB00787 to obtain formal mechanism of action, drug categories, and toxicity classifications (DG002 Severity: High)
- **TxGNN score validation**: Investigate why all five prediction scores are recorded as 0.0; this likely reflects a data pipeline issue rather than actual model output — correct score values are needed to accurately rank and compare prediction confidence across indications
- **Acyclovir-resistant strain monitoring plan**: Given evidence of TK-mutant Acyclovir-resistant VZV and HSV strains in immunocompromised populations, any clinical use expansion should include a resistance surveillance protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

