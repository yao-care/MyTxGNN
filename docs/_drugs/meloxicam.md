---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 5
---

# Meloxicam
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

# Meloxicam: From Established NSAID Use to Osteoarthritis (Confirmatory Signal, Not a Novel Candidate)

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID already used for inflammatory joint pain. The TxGNN pipeline's top-ranked candidate for this drug is **Osteoarthritis** — but the evidence pack's own rationale flags this as a re-identification of an existing, already-approved indication rather than a genuine repurposing signal, backed by **35 clinical trials** and **20 publications** in the underlying searches (with the TxGNN model score itself recorded as 0.0, which should be treated as a data-quality flag, not a true zero-confidence result).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis / Rheumatoid Arthritis / Ankylosing Spondylitis (per repurposing rationale — these are meloxicam's known, already-approved NSAID indications; no Malaysia license-level indication text was available to confirm this locally) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.00% (recorded as 0.0 in source data — likely a scoring/export anomaly rather than a genuine near-zero prediction; flag for data QA) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 24 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Meloxicam is a selective COX-2-preferential NSAID that inhibits prostaglandin synthesis, thereby reducing synovial inflammation and pain. This is meloxicam's **direct, original pharmacological mechanism** — not a novel mechanistic link discovered by the model.

Critically, the evidence pack's own rationale states this explicitly: *"此為藥物原始核准適應症之直接藥理機轉，非老藥新用推論——本節屬於「既有適應症再確認」而非新候選"* (this is the drug's original approved mechanism, not a repurposing inference — this candidate is an existing-indication reconfirmation, not a new one). The same applies to the second-ranked candidate, rheumatoid arthritis.

For contrast, two lower-ranked candidates in this same evidence pack — "osteoarthritis susceptibility" (a genetic-risk knowledge-graph node, not a treatable disease) and "juvenile arthritis due to LACC1 defect" (a rare monogenic autoinflammatory condition with no COX-2 pathway link) — were correctly scored **L5 / Hold**, with zero supporting trials or literature. This suggests the underlying TxGNN run for this drug is not surfacing genuinely novel, mechanistically-justified candidates at the top of the list; the true repurposing signal (if any) may lie beyond what's captured here.

Currently, detailed formal mechanism-of-action documentation (DrugBank MOA field) is also unavailable for this candidate — flagged as a High-severity data gap (DG002) in the evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00239395](https://clinicaltrials.gov/study/NCT00239395) | Phase 3 | Completed | 168 | IM vs. oral meloxicam 7.5mg once daily in OA — direct on-label efficacy/safety comparison (Grade A) |
| [NCT01799213](https://clinicaltrials.gov/study/NCT01799213) | Phase 2 | Completed | 490 | Discontinuing NSAIDs (incl. meloxicam) in veterans with knee OA — GI/CV risk-focused (Grade B) |
| [NCT02183064](https://clinicaltrials.gov/study/NCT02183064) | Phase 3 | Completed | 1309 | Meloxicam 7.5mg vs. usual-care NSAIDs in OA of hip/knee/hand/spine — treatment success/failure and healthcare utilization |
| [NCT01787188](https://clinicaltrials.gov/study/NCT01787188) | Phase 3 | Completed | 403 | Meloxicam SoluMatrix capsules for OA pain of knee/hip — placebo-controlled efficacy/safety |
| [NCT01801735](https://clinicaltrials.gov/study/NCT01801735) | Phase 3 | Completed | 600 | 52-week safety study of Meloxicam SoluMatrix capsules in OA of knee/hip |
| [NCT02183129](https://clinicaltrials.gov/study/NCT02183129) | Phase 4 | Completed | 91 | Meloxicam 7.5mg vs. diclofenac 100mg SR in knee OA over 8 weeks |
| [NCT02183116](https://clinicaltrials.gov/study/NCT02183116) | Phase 4 | Completed | 30 | Meloxicam 7.5mg efficacy/safety in knee OA over 56 days |
| [NCT01430559](https://clinicaltrials.gov/study/NCT01430559) | N/A | Completed | 408 | Meloxicam vs. placebo in mainland Chinese knee OA patients; WOMAC tool validation |
| [NCT02180516](https://clinicaltrials.gov/study/NCT02180516) | N/A | Completed | 9984 | Large observational safety cohort — meloxicam GI adverse event rate vs. other NSAIDs across RA/OA/related conditions |
| [NCT00612885](https://clinicaltrials.gov/study/NCT00612885) | N/A | Completed | 425 | Korean PMS study of Mobic® IM injection safety/efficacy in OA and RA patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12387696](https://pubmed.ncbi.nlm.nih.gov/12387696/) | 2002 | Review | Expert Opinion on Pharmacotherapy | Overview of meloxicam's COX-2-preferential profile and approved use in OA, RA, ankylosing spondylitis |
| [32164967](https://pubmed.ncbi.nlm.nih.gov/32164967/) | 2020 | Review | Profiles of Drug Substances, Excipients and Related Methodology | Comprehensive drug substance profile; confirms OA/RA/ankylosing spondylitis/JIA as established indications |
| [18405470](https://pubmed.ncbi.nlm.nih.gov/18405470/) | 2008 | Systematic Review / HTA | Health Technology Assessment | Systematic review and economic evaluation of COX-2 selective NSAIDs (incl. meloxicam) for OA and RA |
| [8882380](https://pubmed.ncbi.nlm.nih.gov/8882380/) | 1996 | Review | Drugs | Foundational monograph establishing meloxicam's anti-inflammatory profile in RA and OA |
| [26963155](https://pubmed.ncbi.nlm.nih.gov/26963155/) | 2016 | Drug Bulletin | The Medical Letter on Drugs and Therapeutics | Independent evaluation of low-dose meloxicam (Vivlodex) for OA pain |
| [23918578](https://pubmed.ncbi.nlm.nih.gov/23918578/) | 2013 | Clinical Study | Yonsei Medical Journal | Efficacy of meloxicam + pregabalin combination for knee OA pain |
| [35399845](https://pubmed.ncbi.nlm.nih.gov/35399845/) | 2022 | Clinical Study | Journal of Healthcare Engineering | Warm acupuncture combined with meloxicam for knee OA pain/joint function |
| [37348266](https://pubmed.ncbi.nlm.nih.gov/37348266/) | 2023 | Preclinical (rat) | Colloids and Surfaces B: Biointerfaces | Meloxicam emulgel formulation suppresses cartilage degradation in rat knee OA model |
| [36816604](https://pubmed.ncbi.nlm.nih.gov/36816604/) | 2023 | Preclinical / Formulation | Materials Today Bio | Meloxicam liposome intra-articular formulation for TMJ osteoarthritis |
| [37180348](https://pubmed.ncbi.nlm.nih.gov/37180348/) | 2023 | Chemistry | IUCrData | Crystal structure characterization of meloxicam hydrochloride |

---

## Malaysia Market Information

The evidence pack confirms meloxicam holds **24 active registrations** with market status "已上市" (Marketed) in Malaysia, but none of the individual license records (license number, product name, dosage form, manufacturer, approved indication text) contain usable data — all fields returned empty from the source query. Registration-level detail cannot be reported until this is re-queried against the NPRA source.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured safety data (warnings, contraindications, or drug interactions) is currently populated for this candidate — the drug-drug interaction query also returned no results (`not_found`, 0 interactions).

**Note:** the evidence pack flags the missing TFDA/NPRA label warnings and contraindications as a **Blocking**-severity data gap (DG001), stating this specifically prevents entry into the S1 safety initial-screening stage. This gap should be resolved before any downstream safety decision is made, independent of the efficacy evidence above.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence for meloxicam in osteoarthritis is extensive (L1, multiple completed Phase 3 RCTs) — but this reflects meloxicam's existing, already-approved use rather than a novel repurposing opportunity, so it does not warrant a "Go" for new-indication development. The Blocking-severity safety data gap (DG001) means no first-pass safety review has actually occurred yet.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the Malaysia NPRA package insert for warnings/contraindications before any safety sign-off
- Resolve DG002 (High): obtain a formal DrugBank/label mechanism-of-action statement
- Re-query NPRA license records — current 24 registrations have no populated product/indication detail
- Re-verify the TxGNN score of 0.0 for this candidate; treat as a possible pipeline/export defect rather than a true prediction value
- Given this candidate largely reconfirms an existing indication, consider whether pipeline resources are better directed at genuinely novel candidates for this drug (the current rank 3 and 5 candidates were correctly screened out at L5/Hold)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

