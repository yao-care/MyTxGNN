---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indomethacin: From NSAID Anti-Inflammatory Therapy to Rheumatoid Arthritis

## One-Sentence Summary

Indomethacin is a long-established non-steroidal anti-inflammatory drug (NSAID) used broadly for inflammatory and musculoskeletal pain conditions. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, and the supporting literature (**20 publications**, no registered clinical trials in this pull) confirms this is in fact a well-documented, decades-old use rather than a genuinely novel indication — the model has reaffirmed an existing clinical practice with high confidence (99.98%).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not returned in this data pull (registry text fields were empty); Indomethacin is a well-established NSAID for inflammatory/musculoskeletal pain |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned for this drug in the current evidence pack. Based on known pharmacology, Indomethacin is a non-selective COX-1/COX-2 (cyclooxygenase) inhibitor that blocks prostaglandin synthesis, producing anti-inflammatory and analgesic effects. This mechanism is the pharmacological basis for its long-standing use as a first-line NSAID in inflammatory arthritides.

Importantly, this prediction should be interpreted with a caveat: Rheumatoid Arthritis is not a novel indication for Indomethacin — it is one of the drug's classical, textbook uses, evidenced by RCTs dating back to the 1960s–1990s. The high TxGNN score here reflects the model correctly recovering an already-consolidated drug-disease relationship rather than surfacing new repurposing potential. This strengthens confidence in the model's validity but limits the practical "new indication" value of this particular candidate.

Mechanistically, COX inhibition and suppression of prostaglandin-mediated joint inflammation directly addresses the synovitis and pain that characterize RA, which is consistent with decades of clinical experience summarized in the literature below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3365530](https://pubmed.ncbi.nlm.nih.gov/3365530/) | 1988 | RCT | British Journal of Rheumatology | Cross-over trial in 17 RA patients: high-dose indomethacin (150 mg/day) showed equianalgesic effects to low-dose indomethacin (50 mg/day) + paracetamol (4 g/day) |
| [71973](https://pubmed.ncbi.nlm.nih.gov/71973/) | 1977 | RCT | Current Medical Research and Opinion | Double-blind crossover in 30 RA patients: flurbiprofen 200 mg/day vs indomethacin 100 mg/day, no significant difference in pain, stiffness, or grip strength |
| [7004474](https://pubmed.ncbi.nlm.nih.gov/7004474/) | 1980 | RCT | British Journal of Clinical Pharmacology | Double-blind crossover in 13 RA patients comparing oral vs rectal indomethacin 100 mg nightly; both routes produced significant clinical improvement |
| [6380897](https://pubmed.ncbi.nlm.nih.gov/6380897/) | 1984 | RCT | Clinical Rheumatology | Crossover study in 30 RA patients: diclofenac vs indomethacin 100 mg suppositories, both improved disease status vs placebo |
| [12535392](https://pubmed.ncbi.nlm.nih.gov/12535392/) | 2003 | RCT (Cochrane systematic review) | Cochrane Database of Systematic Reviews | Systematic review comparing low-dose corticosteroids vs placebo/NSAIDs (including indomethacin) in RA |
| [25108](https://pubmed.ncbi.nlm.nih.gov/25108/) | 1978 | RCT | British Medical Journal | Comparative trial of indomethacin and alclofenac in RA (abstract not available) |
| [5333306](https://pubmed.ncbi.nlm.nih.gov/5333306/) | 1967 | RCT | British Medical Journal | Evaluation of indomethacin's anti-inflammatory efficacy and side effects in RA (abstract not available) |
| [14302557](https://pubmed.ncbi.nlm.nih.gov/14302557/) | 1965 | Case series/Review | Clinical Obstetrics and Gynecology | Review discussing RA management considerations, including anti-inflammatory therapy, during pregnancy |
| [35282742](https://pubmed.ncbi.nlm.nih.gov/35282742/) | 2022 | Preclinical | Journal of Drug Targeting | pH-responsive indomethacin-loaded nanoparticle (IND@PB@M@HA) combined with photothermal therapy for RA in preclinical models |
| [380913](https://pubmed.ncbi.nlm.nih.gov/380913/) | 1979 | Not yet classified | Current Medical Research and Opinion | Single-blind crossover in 24 RA patients: piroxicam, indomethacin, and ibuprofen compared; piroxicam superior to placebo, no significant difference among active drugs |

---

## Malaysia Market Information

NPRA records confirm **3 active marketing authorizations** for Indomethacin in Malaysia (market status: Marketed). However, this data pull did not return license numbers, product names, dosage forms, or approved indication text for these registrations — a follow-up query against the NPRA product database is needed to populate these details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple RCTs spanning 1967–2003 confirming indomethacin's efficacy in RA, but this is a reaffirmation of an existing, long-established use rather than a novel repurposing opportunity — its practical value as a "new indication" candidate is limited. More critically, the evidence pack flags a **Blocking** data gap (DG001: TFDA/NPRA label warnings and contraindications) that prevents this candidate from formally entering safety pre-assessment (S1), regardless of the strength of efficacy evidence.

**To proceed, the following is needed:**
- Retrieve and parse the official product label/insert for warnings, contraindications, and precautions (Blocking gap, DG001)
- Confirm mechanism of action via DrugBank API (High priority gap, DG002)
- Complete NPRA registration details (license numbers, product names, dosage forms, approved indication text) for the 3 Malaysia authorizations
- Given this indication is not novel, consider whether downstream resources are better allocated to genuinely new TxGNN-predicted candidates for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

