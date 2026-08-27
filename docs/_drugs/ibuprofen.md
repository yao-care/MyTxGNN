---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 5
---

# Ibuprofen
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

# Ibuprofen: From Pain and Inflammation to Osteoarthritis

## One-Sentence Summary

> Ibuprofen is a classic non-selective COX-1/COX-2 inhibitor NSAID, widely used for pain, fever, and inflammation.
> The TxGNN model's top-ranked candidate indication is **Osteoarthritis**, but this is already a globally established, standard use of ibuprofen rather than a novel repurposing target —
> supported by **50 clinical trials** and **19 publications** in this dataset, including a very large (N=24,081) cardiovascular-safety RCT (PRECISION).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain, fever, and inflammation (general NSAID use; specific TFDA-approved label indication text not available in this dataset) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.00% *(score field returned as 0.0 in this dataset — likely incomplete/placeholder; not used as the basis for the recommendation below)* |
| Evidence Level | L1 |
| Market Status | ✓ Marketed |
| Number of Registrations | 43 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available (marked as a data gap in this evidence pack). Based on known pharmacology, ibuprofen is a non-selective COX-1/COX-2 inhibitor that blocks conversion of arachidonic acid to prostaglandins (notably PGE2), reducing synovial inflammation and joint pain — a standard NSAID class effect.

Importantly, this is not a case of mechanistic extrapolation to a new disease area: osteoarthritis is already one of ibuprofen's long-standing, globally approved core indications. The evidence pack itself notes that this reflects ibuprofen's "existing standard indication rather than a novel mechanistic inference." The large body of clinical trials and literature below therefore functions as **confirmatory evidence of an established use**, not as exploratory repurposing evidence.

Because the mechanism (COX inhibition → reduced PGE2 → reduced joint inflammation/pain) is already proven and the indication is already in wide clinical use, the main open questions for this candidate are not efficacy questions but **safety-documentation completeness** — specifically, the TFDA label warnings/contraindications data gap flagged as "Blocking" in this evidence pack (see Conclusion below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00613106](https://clinicaltrials.gov/study/NCT00613106) | Phase 3 | Completed | 179 | Long-term safety follow-on for HZT-501 (ibuprofen 800mg/famotidine 26.6mg) in patients requiring long-term NSAID treatment |
| [NCT00450216](https://clinicaltrials.gov/study/NCT00450216) | Phase 3 | Completed | 906 | HZT-501 reduces development of ibuprofen-associated ulcers vs. ibuprofen alone |
| [NCT00450658](https://clinicaltrials.gov/study/NCT00450658) | Phase 3 | Completed | 627 | Companion Phase 3 trial confirming HZT-501 reduces ibuprofen-associated GI ulcers |
| [NCT00346216](https://clinicaltrials.gov/study/NCT00346216) | Phase 4 | Completed | 24,081 | Large-scale cardiovascular safety RCT (PRECISION): celecoxib vs. naproxen and ibuprofen in OA/RA patients with CV risk |
| [NCT00269191](https://clinicaltrials.gov/study/NCT00269191) | Phase 3 | Completed | 528 | Etoricoxib 30mg vs. ibuprofen 2400mg/day: safety and efficacy in hip/knee osteoarthritis |
| [NCT01066676](https://clinicaltrials.gov/study/NCT01066676) | Phase 4 | Completed | 482 | Dexibuprofen vs. ibuprofen 400mg oral suspension: tolerability and efficacy in hip/knee OA |
| [NCT05318521](https://clinicaltrials.gov/study/NCT05318521) | Phase 3 | Unknown | 500 | Ibuprofen modified-release 800mg vs. placebo for chronic knee OA pain |
| [NCT00784810](https://clinicaltrials.gov/study/NCT00784810) | Phase 4 | Completed | 247 | Oxycodone/naloxone vs. codeine/paracetamol for chronic low back pain or OA pain, with ibuprofen as supplemental analgesic |
| [NCT00792818](https://clinicaltrials.gov/study/NCT00792818) | Phase 3 | Completed | 367 | Curcuma domestica extract vs. ibuprofen, multicenter RCT for knee osteoarthritis |
| [NCT00630929](https://clinicaltrials.gov/study/NCT00630929) | Phase 4 | Completed | 388 | Celecoxib (once daily) vs. ibuprofen (three times daily) vs. placebo in knee osteoarthritis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27959716](https://pubmed.ncbi.nlm.nih.gov/27959716/) | 2016 | RCT | New England Journal of Medicine | Cardiovascular safety of celecoxib vs. naproxen/ibuprofen in arthritis patients (PRECISION trial) |
| [25560713](https://pubmed.ncbi.nlm.nih.gov/25560713/) | 2015 | Review | Annals of Internal Medicine | Network meta-analysis comparing pharmacologic interventions for knee osteoarthritis |
| [22471358](https://pubmed.ncbi.nlm.nih.gov/22471358/) | 2012 | Review | J Pharm Pharmacol | Review of ibuprofen pharmacokinetics/pharmacodynamics as first-line hip/knee OA therapy |
| [28035387](https://pubmed.ncbi.nlm.nih.gov/28035387/) | 2017 | Review | Molecular Medicine Reports | Mechanistic study comparing ibuprofen, prednisone, and betamethasone in OA chondrocyte models |
| [22149579](https://pubmed.ncbi.nlm.nih.gov/22149579/) | 2012 | Review | Expert Rev Gastroenterol Hepatol | GI protection of ibuprofen/famotidine (HZT-501/DUEXIS) in RA and OA |
| [25141246](https://pubmed.ncbi.nlm.nih.gov/25141246/) | 2014 | Pooled Analysis | Postgraduate Medicine | Pooled analysis: GI ulcer risk with ibuprofen/famotidine vs. ibuprofen alone in OA |
| [35234840](https://pubmed.ncbi.nlm.nih.gov/35234840/) | 2022 | Analysis | Eur Heart J Cardiovasc Pharmacother | Cardiorenal risk of celecoxib vs. naproxen/ibuprofen — insights from the PRECISION trial |
| [320671](https://pubmed.ncbi.nlm.nih.gov/320671/) | 1977 | RCT | Southern Medical Journal | Double-blind multiclinic trial: ibuprofen vs. aspirin vs. placebo in osteoarthritis (N=437) |
| [24672232](https://pubmed.ncbi.nlm.nih.gov/24672232/) | 2014 | RCT | Clinical Interventions in Aging | Multicenter trial: Curcuma domestica extract vs. ibuprofen in knee osteoarthritis |
| [38937394](https://pubmed.ncbi.nlm.nih.gov/38937394/) | 2024 | Review | Drugs | Systematic review/meta-analysis: paracetamol combination therapy for back pain and osteoarthritis |

---

## Market Information

Detailed license-level records (authorization number, product name, dosage form, approved indication text) are not populated in this dataset — the 5 sample license entries returned are blank. What is confirmed: ibuprofen is **marketed** with **43 total registrations** on record. License-level detail should be re-pulled from the regulatory source before this candidate proceeds further.

---

## Safety Considerations

Please refer to the package insert for safety information. *(No key warnings, contraindications, or DDI data were returned in this evidence pack — DDI query status: not found, 0 interactions.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Osteoarthritis is already an established, long-standing indication for ibuprofen with strong supporting evidence (L1: multiple completed Phase 3/4 RCTs, including the large PRECISION trial), so efficacy is not in question.
- However, this evidence pack flags a **Blocking-severity data gap (DG001)**: TFDA label warnings/contraindications are missing, which the pack itself states prevents completion of initial safety screening (S1). Guardrails are therefore driven by regulatory/safety documentation completeness, not by uncertainty about the drug-disease link.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (DG001, Blocking — retrieve and parse the official label PDF)
- Structured mechanism-of-action data from DrugBank (DG002)
- Confirmed license-level market data (authorization numbers, approved indication text) to replace the currently blank entries
- Clarification that this candidate represents consolidation of an existing approved use rather than a novel repurposing opportunity, so it should be routed accordingly in the review pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

