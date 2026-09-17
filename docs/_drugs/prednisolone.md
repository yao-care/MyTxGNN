---
layout: default
title: Prednisolone
parent: Low Evidence (L4-L5)
nav_order: 568
evidence_level: L5
indication_count: 5
---

# Prednisolone
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

Using the evidence pack as given (no skill applies to this reporting task — it's a direct write-up against a fixed template), here's the report.

Note upfront: `taiwan_regulatory.licenses` contains 5 entries but every field is an empty string (no license numbers/product names/indication text were actually captured), and `drug.original_indications` is an empty array. I could not fabricate an "Original Indication" from this, so I've labeled it accordingly rather than inventing a value.

---

# Prednisolone: From Corticosteroid-Responsive Conditions to Erythema Multiforme

## One-Sentence Summary

Prednisolone is a systemic corticosteroid used broadly for inflammatory, allergic, and autoimmune conditions; the specific original indication text is not available in the current NPRA extract. The TxGNN model's top-ranked prediction is **Erythema Multiforme**, supported by **14 clinical trials** and **20 publications** in the evidence pack — though on closer review only 2 of the 14 trials and roughly half of the literature are directly on-topic, with the rest being keyword-driven false hits (e.g., prednisone as an incidental component of unrelated cancer chemotherapy regimens).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in current NPRA license extract (all 5 license records are blank; drug-level original indication field is also empty) |
| Predicted New Indication | Erythema Multiforme |
| TxGNN Prediction Score | 0.00% (evidence pack reports a uniform 0.0 score across all 5 candidates — appears to be a placeholder rather than a discriminating value; ranking below is based on the qualitative evidence review, not this score) |
| Evidence Level | L3 (observational studies / case series; no EM-specific high-quality RCT yet) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 38 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Prednisolone in this evidence pack (marked as a data gap). Based on general pharmacological knowledge, Prednisolone is a synthetic glucocorticoid with anti-inflammatory and immunosuppressive activity, widely used across corticosteroid-responsive inflammatory, allergic, and autoimmune conditions.

Erythema multiforme (EM) is understood to result from keratinocyte apoptosis driven by a type IV hypersensitivity reaction (T-cell-mediated cytotoxicity), most commonly triggered by HSV infection or drug exposure. Prednisolone's immunosuppressive and anti-inflammatory action could theoretically reduce inflammation and limit cytotoxic keratinocyte damage in this setting.

This mechanistic rationale reflects a long-standing dermatological practice pattern rather than a novel hypothesis — systemic corticosteroids are already used off-label/empirically for severe EM in clinical practice. However, high-quality RCTs specific to EM itself (as distinct from its more severe cousins SJS/TEN) are lacking; the evidence base is mainly case series, case reports, and clinical consensus.

## Clinical Trial Evidence

Of the 14 trials returned by the search, only 2 are directly relevant to erythema multiforme or its clinical spectrum (SJS/TEN); the remaining 12 are keyword-driven matches where prednisone/prednisolone appears as an incidental component of unrelated oncology or dermatology regimens (e.g., abiraterone + prednisone for prostate cancer, vitiligo repigmentation studies) and are excluded below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06266221](https://clinicaltrials.gov/study/NCT06266221) | Phase 3 | Not yet recruiting | 96 | Randomized controlled trial comparing a short systemic corticosteroid regimen to placebo in the acute established phase of severe erythema multiforme — the only EM-specific RCT identified |
| [NCT06119490](https://clinicaltrials.gov/study/NCT06119490) | Early Phase 1 | Recruiting | 30 | Evaluates methylprednisolone combined with JAK inhibitors (abrocitinib/tofacitinib) for toxic epidermal necrolysis, a disease on the same immune-mediated mucocutaneous spectrum as EM |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35274741](https://pubmed.ncbi.nlm.nih.gov/35274741/) | 2022 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Reviews systemic interventions (including glucocorticoids) for SJS/TEN/overlap syndrome; highlights unmet need for efficacy data across this spectrum |
| [26281815](https://pubmed.ncbi.nlm.nih.gov/26281815/) | 2015 | Review | J Emerg Med | General clinical review of erythema multiforme diagnosis and management |
| [8566721](https://pubmed.ncbi.nlm.nih.gov/8566721/) | 1995 | Review/case series | Allergy Proc | Virus-induced EM and SJS; reports treatment success with acyclovir plus prednisolone |
| [15599469](https://pubmed.ncbi.nlm.nih.gov/15599469/) | 2004 | Cohort | J Microbiol Immunol Infect | Clinical characteristics of childhood EM, SJS, and TEN in Taiwanese/regional children — locally relevant outcome data |
| [30189985](https://pubmed.ncbi.nlm.nih.gov/30189985/) | 2018 | Review | Dent Clin North Am | Reviews painful oral vesiculoerosive diseases including EM; topical/systemic corticosteroids as mainstay treatment |
| [40454868](https://pubmed.ncbi.nlm.nih.gov/40454868/) | 2025 | Case report + literature review | J Chemother | EM following pembrolizumab; tapering-dose prednisolone resolved the rash without discontinuing immunotherapy |
| [38962048](https://pubmed.ncbi.nlm.nih.gov/38962048/) | 2024 | Mechanistic/translational | Int Cancer Conf J | PD-L1/CD4+ T-cell infiltration predicts severe pembrolizumab-induced EM; steroid ointment alone was ineffective in the severe case |
| [21675930](https://pubmed.ncbi.nlm.nih.gov/21675930/) | 2011 | Case-based review | Cutan Ocul Toxicol | Describes EMPACT syndrome (phenytoin-induced EM with cranial irradiation) |
| [28101031](https://pubmed.ncbi.nlm.nih.gov/28101031/) | 2016 | Case report | Case Rep Oncol | Alectinib-induced EM with successful rechallenge after treatment |
| [15608841](https://pubmed.ncbi.nlm.nih.gov/15608841/) | 2004 | Case report | Ann Acad Med Singap | Recurrent EM managed with corticosteroids; patient developed iatrogenic Cushing's syndrome from prolonged use — relevant to long-term safety |

## Malaysia Market Information

License-level detail (registration numbers, product names, dosage forms, approved indication text) was not captured in the current NPRA data extract — all 5 retrieved license records are blank. NPRA registration confirms **38 active licenses** for Prednisolone products and a "Marketed" status, but specific product/indication text needs to be re-pulled from source before it can be reported here.

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack currently has no usable key warnings, contraindications, or DDI data (all marked as data gaps), and this is flagged as a **blocking** gap (DG001) — full label warnings/contraindications must be retrieved from the NPRA package insert before this candidate can pass an initial safety review (S1).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Corticosteroid use for erythema multiforme is an established, mechanistically plausible dermatological practice, and one EM-specific Phase 3 RCT (NCT06266221) is underway — but current evidence is otherwise limited to case series/reports (L3), and the label-level safety data needed for a proper risk assessment is currently missing.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently blocking (DG001)
- Detailed mechanism of action confirmation from DrugBank (DG002)
- Malaysia license/indication text re-extraction (current records are blank despite 38 registrations)
- Results from NCT06266221 (EM-specific Phase 3 RCT, not yet recruiting) once available
- DDI data completion (currently "not_found" with zero interactions on record)
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

