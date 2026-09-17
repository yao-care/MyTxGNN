---
layout: default
title: Valsartan
parent: Low Evidence (L4-L5)
nav_order: 683
evidence_level: L5
indication_count: 5
---

# Valsartan
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

# Valsartan: From Hypertension to Hypertension — Confirmatory Signal, Not a Novel Repurposing Candidate

## One-Sentence Summary

Valsartan (DrugBank DB00177) is a widely-used angiotensin II receptor blocker; its predicted new indication from this Evidence Pack — **Hypertensive Disorder / Hypertension** — is the drug's own long-established primary indication rather than a genuinely new therapeutic use.
The prediction is backed by **50 clinical trials** and **20 publications**, but this evidence confirms valsartan's known antihypertensive efficacy rather than demonstrating repurposing into a new disease area.
Because the original-indication text and safety label data are both missing from this Evidence Pack, the candidate cannot yet clear a safety initial screen.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (all NPRA license `approved_indication_text` fields are empty) |
| Predicted New Indication | Hypertensive disorder (= Hypertension) |
| TxGNN Prediction Score | 0% (reported as 0.0 for all 5 candidates — likely a scoring/normalization data gap, not a true near-zero prediction) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs on valsartan in hypertension) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 46 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a gap). Based on well-established pharmacological knowledge, valsartan is an angiotensin II receptor blocker (ARB) that inhibits the AT1 receptor, reducing angiotensin II–induced vasoconstriction and aldosterone secretion — the mechanism underlying its decades-long use as a first-line antihypertensive.

All five ranked predictions in this Evidence Pack are variants of the same disease concept — "hypertensive disorder" and "hypertension" — which is valsartan's own textbook indication. This is not a case of mechanistic extrapolation from one disease area to an unrelated one (as would be expected in genuine repurposing); it is the model correctly re-identifying the drug's established use. The very large trial and literature base reflects decades of confirmatory antihypertensive research (including combination therapy with amlodipine, HCTZ, sacubitril, aliskiren, etc.) rather than exploratory evidence for a novel indication.

Given this, the practical value of this candidate lies less in "should Valsartan be repurposed for hypertension" (already true) and more as a signal that the TxGNN pipeline should exclude same-indication matches, or that upstream `original_indications` data needs to be populated so true novelty can be assessed.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00696436](https://clinicaltrials.gov/study/NCT00696436) | Phase 3 | Completed | 1291 | Azilsartan medoxomil vs. placebo, valsartan, and olmesartan in essential hypertension |
| [NCT06236061](https://clinicaltrials.gov/study/NCT06236061) | Phase 3 | Completed | 718 | LCZ696 (sacubitril/valsartan)/amlodipine combination vs. LCZ696 monotherapy in grade 1–2 hypertension |
| [NCT00413049](https://clinicaltrials.gov/study/NCT00413049) | Phase 3 | Completed | 698 | Valsartan/amlodipine 80/5 mg vs. amlodipine 5 mg monotherapy in mild-to-moderate hypertension |
| [NCT00311740](https://clinicaltrials.gov/study/NCT00311740) | Phase 3 | Completed | 582 | Factorial study of valsartan + hydrochlorothiazide combined and alone in essential hypertension |
| [NCT00171093](https://clinicaltrials.gov/study/NCT00171093) | Phase 3 | Completed | 369 | Valsartan (320mg) + simvastatin (80mg) combination vs. monotherapies in hypertension and hypercholesterolemia |
| [NCT00338936](https://clinicaltrials.gov/study/NCT00338936) | Phase 3 | Completed | 362 | 52-week extension study of valsartan/HCTZ combination long-term safety and efficacy |
| [NCT07116863](https://clinicaltrials.gov/study/NCT07116863) | Phase 3 | Completed | 286 | KDF1901 (valsartan/amlodipine/chlorthalidone triple combination) in inadequately controlled essential hypertension |
| [NCT00392262](https://clinicaltrials.gov/study/NCT00392262) | Phase 3 | Completed | 224 | Valsartan 160mg + amlodipine 5mg in patients not responding to amlodipine/felodipine monotherapy |
| [NCT00360178](https://clinicaltrials.gov/study/NCT00360178) | Phase 3 | Completed | 198 | Fixed-dose valsartan 160mg + HCTZ 25mg vs. free combination of candesartan + HCTZ |
| [NCT00171028](https://clinicaltrials.gov/study/NCT00171028) | Phase 3 | Completed | 90 | Dose-response and safety of valsartan in pediatric hypertension patients aged 1–5 years |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632589](https://pubmed.ncbi.nlm.nih.gov/39632589/) | 2025 | RCT | J Clin Hypertens | PARASOL study: sacubitril/valsartan noninferior to amlodipine in Japanese essential hypertension |
| [35058583](https://pubmed.ncbi.nlm.nih.gov/35058583/) | 2022 | RCT | Hypertens Res | Phase 3 RCT: sacubitril/valsartan vs. olmesartan in Japanese essential hypertension (n=1161) |
| [28093466](https://pubmed.ncbi.nlm.nih.gov/28093466/) | 2017 | RCT | Hypertension | PARAMETER study: sacubitril/valsartan vs. olmesartan on central hemodynamics in elderly systolic hypertension |
| [40739095](https://pubmed.ncbi.nlm.nih.gov/40739095/) | 2025 | RCT (Phase 2) | Nature Communications | REVERSE-LVH trial: sacubitril/valsartan vs. valsartan for hypertensive heart disease fibrosis |
| [39927814](https://pubmed.ncbi.nlm.nih.gov/39927814/) | 2025 | Meta-analysis | J Hypertens | Efficacy/safety of sacubitril-valsartan in hypertensive dialysis patients (19 studies, n=1597) |
| [35672897](https://pubmed.ncbi.nlm.nih.gov/35672897/) | 2022 | Systematic review/meta-analysis | Ann Palliat Med | Sacubitril/valsartan in middle-aged and elderly hypertensive patients |
| [22352121](https://pubmed.ncbi.nlm.nih.gov/22352121/) | 2011 | Post-marketing surveillance | Blood Press Suppl | Efficacy and safety of valsartan in hypertensive Taiwanese patients |
| [30664018](https://pubmed.ncbi.nlm.nih.gov/30664018/) | 2022 | Review | Am J Ther | Overview of sacubitril/valsartan efficacy in hypertension |
| [25604204](https://pubmed.ncbi.nlm.nih.gov/25604204/) | 2014 | Review | Anadolu Kardiyol Derg | Review of RAS blockade and valsartan in hypertension management |
| [10353300](https://pubmed.ncbi.nlm.nih.gov/10353300/) | 1999 | Review | Drugs | Valsartan/hydrochlorothiazide combination pharmacology and clinical trial review |

## Malaysia Market Information

Detailed licence-level fields (licence number, product name, dosage form, manufacturer, approved indication text) were not populated in this Evidence Pack, despite 46 total registrations being on record. Licence-level detail needs to be re-pulled from the source registry before it can be reported here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Blocking-severity data gap (DG001: TFDA/NPRA label warnings and contraindications) prevents the S1 safety initial screen from being completed. Separately, the "predicted new indication" in this candidate is the same disease as valsartan's well-known original indication, so this record does not currently represent a validated novel repurposing opportunity — it more likely reflects a data-pipeline artifact (missing `original_indications`, and a uniformly 0.0 TxGNN score across all five candidates suggests a scoring issue rather than a true near-zero signal).

**To proceed, the following is needed:**
- Populate `original_indications` and NPRA `approved_indication_text` so true indication novelty can be assessed against the prediction
- Retrieve TFDA/NPRA product label warnings and contraindications to complete the S1 safety screen (DG001)
- Query DrugBank for mechanism of action (DG002)
- Investigate why TxGNN score is reported as 0.0 for all ranked candidates and re-run scoring if this is a pipeline defect
- Re-evaluate whether this candidate should be filtered out of the repurposing queue as a same-indication (non-novel) match
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

