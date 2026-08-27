---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Mefenamic Acid: From Analgesic/Anti-Inflammatory Use to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class NSAID established for pain and inflammation control. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, a use already supported by a body of historical randomized trials — **0 registered clinical trials** but **20 PubMed publications**, several from double-blind RCTs conducted in the 1960s–1980s.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the current NPRA license extract (all license fields returned empty); mefenamic acid is a known fenamate NSAID used for mild-to-moderate pain and inflammatory conditions |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 36 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is not available (flagged as a High-severity data gap). Based on known pharmacology, mefenamic acid is a fenamate-class NSAID that directly inhibits COX-1/COX-2, reducing prostaglandin synthesis — a mechanism that underlies both analgesic and anti-inflammatory activity.

Because COX inhibition is the core pharmacological basis for controlling joint pain and inflammation in rheumatoid arthritis, this prediction is not really a "novel" repurposing signal — it reflects a long-recognized, mechanistically direct extension of NSAID activity into a classic inflammatory joint disease, and is consistent with mefenamic acid's approved use in some markets.

The supporting literature is high in mechanistic plausibility but dated: the available RCTs comparing mefenamic acid against ibuprofen, flurbiprofen, and sulindac in RA were conducted between the late 1960s and late 1970s, predating clinicaltrials.gov-style trial registries — which explains why zero registered clinical trials appear despite Tier-1 RCT literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT | Current Medical Research and Opinion | Double-blind crossover trial (n=24): mefenamic acid, flurbiprofen and sulindac all significantly superior to placebo on pain score, joint tenderness, and morning stiffness |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | The Journal of International Medical Research | Randomized double-blind within-patient study (n=40): mefenamic acid and ibuprofen showed comparable analgesic/anti-inflammatory effect; similar side-effect profile |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT | The Medical Journal of Australia | Double-blind crossover trial: mefenamic acid (1500mg/day) compared favorably with ibuprofen (1200mg/day) added to maintenance salicylate therapy; mild, mostly GI side effects |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Cohort/Clinical Study | Annals of the Rheumatic Diseases | Early clinical study establishing use of mefenamic acid in rheumatoid arthritis |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Reviews the clinical place of mefenamic acid in RA treatment |
| [5333309](https://pubmed.ncbi.nlm.nih.gov/5333309/) | 1966 | Review | British Medical Journal | Early review of mefenamic acid pharmacology and clinical use |
| [20668](https://pubmed.ncbi.nlm.nih.gov/20668/) | 1977 | Review | Seminars in Arthritis and Rheumatism | Broader review of anti-inflammatory drugs including fenamates |
| [5676955](https://pubmed.ncbi.nlm.nih.gov/5676955/) | 1968 | Case Series (Safety) | British Medical Journal | Three RA patients developed autoimmune haemolytic anaemia (warm-antibody type) during mefenamic acid therapy; resolved after drug withdrawal — relevant long-term safety signal |
| [29548675](https://pubmed.ncbi.nlm.nih.gov/29548675/) | 2018 | Case-crossover Study | The American Journal of Cardiology | Evaluated stroke/AMI risk with NSAID use (including fenamates) specifically in RA patients — relevant to cardiovascular safety monitoring in this population |
| [16223958](https://pubmed.ncbi.nlm.nih.gov/16223958/) | 2006 | Preclinical | Molecular Pharmacology | Mechanistic study showing mefenamic acid's neuroprotective/COX-inhibition effects, supporting long-term anti-inflammatory rationale (epidemiologic link between NSAID use in RA and reduced Alzheimer's risk) |

## Market Information

Total of 36 registrations are on file under NPRA, and market status is confirmed as Marketed. However, per-license details (license number, product name, dosage form, approved indication text) were not returned in this data pull — all five sampled license records came back empty, so individual product listings cannot be reported here.

## Safety Considerations

Please refer to the package insert for safety information. (Structured warnings, contraindications, and DDI data were not available in this data pull — TFDA/NPRA label warnings are flagged as a Blocking-severity data gap.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple double-blind RCTs from the 1960s–1980s support mefenamic acid's efficacy in rheumatoid arthritis, and the mechanism (COX-1/COX-2 inhibition) is directly applicable — but the evidence base is decades old, predates modern trial registries, and carries an unresolved autoimmune haemolytic anaemia signal plus a cardiovascular risk signal specific to RA patients.

**To proceed, the following is needed:**
- TFDA/NPRA-approved label warnings and contraindications (Blocking data gap — required before any S1 safety review can proceed)
- Confirmed DrugBank mechanism-of-action detail
- Modern real-world or comparative-effectiveness data, given all supporting RA trials predate current registries and current NSAID/DMARD standard-of-care benchmarks
- Individual NPRA license/product listings to confirm current approved indication wording and dosage forms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

