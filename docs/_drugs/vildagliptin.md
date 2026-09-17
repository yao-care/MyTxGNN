---
layout: default
title: Vildagliptin
parent: High Evidence (L1-L2)
nav_order: 688
evidence_level: L2
indication_count: 10
---

# Vildagliptin
{: .fs-9 }

Tahap bukti: **L2** | Indikasi diramal: **10** 
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

Using the drug-repurposing report template supplied in the task instructions to structure this output.

A note on source selection before the report: TxGNN returned 10 ranked candidates, but the evidence pack's own `repurposing_rationale` explicitly labels ranks 1–9 (stiff limb syndrome, stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, four lipodystrophy variants, and pancreatic agenesis) as having **no mechanistic link and no supporting evidence** — these look like embedding-space artifacts rather than real repurposing signals, and all carry `Hold`/L5/S0. Only **rank 10, Type 1 Diabetes Mellitus (T1DM)**, has an actual evidence base (L2/S1) and a plausible mechanism, so this report is built around that candidate rather than the top raw TxGNN score.

---

# Vildagliptin: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Vildagliptin is a DPP-4 inhibitor originally used to improve glycemic control in **Type 2 Diabetes Mellitus**. Among TxGNN's ranked candidates, the only one with real supporting evidence is **Type 1 Diabetes Mellitus**, where DPP-4 inhibition may help preserve residual β-cell function — supported by **1 completed RCT** and **9 relevant publications**, though it cannot address the underlying autoimmune disease process.

> ⚠️ Note: TxGNN's top 9 ranked predictions (stiff limb/stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, four lipodystrophy subtypes, pancreatic agenesis) all scored >99.7% but have **zero clinical or literature evidence** and no plausible mechanism per the evidence pack's own analysis. They are excluded from this report as likely model artifacts.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (established in cited literature; not disclosed in the Malaysia NPRA license extract for this pull) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned from DrugBank for this pull (flagged as data gap DG002). Based on the published literature captured in the evidence pack, vildagliptin is a competitive inhibitor of dipeptidyl peptidase-4 (DPP-4), the enzyme that degrades the incretin hormones GLP-1 and GIP. By blocking this degradation, vildagliptin raises endogenous GLP-1/GIP levels, which enhances glucose-dependent insulin secretion and suppresses inappropriate glucagon release — its established mechanism in Type 2 Diabetes.

Type 1 and Type 2 diabetes differ fundamentally in etiology (autoimmune β-cell destruction vs. insulin resistance/relative deficiency), but they share downstream glucose-regulatory physiology. Several trials and mechanistic studies in the evidence pack (e.g., PMID 22855332, PMID 18597213, PMID 33124663) show that vildagliptin can still modulate glucagon counterregulation and, in combination with rapamycin, partially restore β-cell function even in long-standing T1DM. This supports a plausible, evidence-anchored rationale for exploring vildagliptin as an **adjunct** in T1DM.

Importantly, the rationale field for this candidate explicitly notes vildagliptin **does not target the autoimmune process** that destroys β-cells in T1DM — it can only support residual β-cell function or glucagon regulation, not halt disease progression. This tempers the prediction to an adjunctive/research role rather than a primary treatment candidate, unlike the mechanistically implausible predictions ranked above it.

## Clinical Trial Evidence

Note: several NCT trials returned by the search were flagged by the evidence pack itself as likely indexing mismatches (titled/summarized as Type 2 Diabetes studies despite being tagged under this T1DM query, e.g. NCT00099853, NCT01472432, NCT02475499 — all graded "C" for relevance). Only trials genuinely studying T1DM populations are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01147276](https://clinicaltrials.gov/study/NCT01147276) | Phase 4 | Completed | 28 | Examined whether DPP-4 inhibition by vildagliptin affects glucagon counterregulatory response to hypoglycemia in patients with Type 1 Diabetes |
| [NCT06021119](https://clinicaltrials.gov/study/NCT06021119) | Phase 3 | Completed | 50 | Vildagliptin as add-on therapy for Ramadan Iftar-related glycemic excursions in adolescents/young adults with T1DM on an advanced hybrid closed-loop insulin system |
| [NCT06348706](https://clinicaltrials.gov/study/NCT06348706) | Phase 3 | Completed | 60 | Effect of DPP-4 inhibitor supplementation on non-alcoholic steatohepatitis (NASH) in adolescents with T1DM |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT | J Clin Endocrinol Metab | Double-blind RCT: rapamycin plus vildagliptin investigated for restoring β-cell function in long-standing Type 1 Diabetes |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | RCT | Diabetes Obes Metab | RCT of vildagliptin add-on therapy on MMP-14, liver stiffness, and subclinical atherosclerosis in adolescents with T1DM and NASH |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | RCT | Diabetol Metab Syndr | RCT of adjunctive oral vildagliptin to mitigate Ramadan Iftar-related glycemic excursions in T1DM patients on closed-loop insulin delivery |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Review | Expert Opin Investig Drugs | Review of DPP-4 inhibitors modulating β-cell function in T1DM and diabetic kidney disease, including protective effects against immune-mediated β-cell destruction |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | Mechanistic study | Front Endocrinol | Mechanistic review of how vildagliptin sustains elevated GLP-1/GIP levels and improves β-cell glucose sensitivity |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | Clinical study | J Clin Endocrinol Metab | Vildagliptin reduces glucagon during hyperglycemia while preserving glucagon counterregulation during hypoglycemia in T1DM |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | Clinical study | Horm Metab Res | Effect of vildagliptin on glucagon concentration during meals in patients with Type 1 Diabetes |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Preclinical/Animal | Curr Pharm Biotechnol | Vildagliptin induced β-cell neogenesis and improved lipid profile in a later phase of experimental Type 1 Diabetes (rat model) |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Preclinical/Animal | Arch Med Res | Vildagliptin ameliorated oxidative stress and pancreatic β-cell destruction in Type 1 diabetic rats |
| [29510081](https://pubmed.ncbi.nlm.nih.gov/29510081/) | 2018 | Preclinical/Animal | Can J Physiol Pharmacol | Vildagliptin/pioglitazone combination improved overall glycemic control in Type 1 diabetic rats |

## Malaysia Market Information

License-level detail (authorization numbers, product names, dosage forms, approved indication text) was not returned in this data pull — all 12 NPRA license records came back with empty fields. Market status confirms vildagliptin is **currently marketed** in Malaysia with **12 total registrations**, but a fresh NPRA data extraction is needed to populate product-level detail.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were returned for this candidate in the current pull (safety.ddi query status: not found).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only mechanistically and evidentially supportable candidate — Type 1 Diabetes Mellitus — has just one completed RCT specifically targeting T1DM outcomes (rapamycin + vildagliptin, tier 1) plus supportive mechanistic and preclinical data, but the drug cannot address the autoimmune pathology underlying T1DM and would at best serve an adjunctive role. Formal safety screening (S1) cannot proceed because the package insert warnings/contraindications data is currently missing (data gap DG001, severity: Blocking).

**To proceed, the following is needed:**
- Package insert / NPRA warnings and contraindications data (DG001, blocking)
- Confirmed drug mechanism-of-action documentation from DrugBank (DG002)
- Malaysia license-level detail (product names, dosage forms, approved indication text) — current pull returned empty fields
- Re-verification of clinical trial indexing, since several retrieved NCT records were mismatched to Type 2 Diabetes populations despite being tagged for this T1DM query
- Additional T1DM-specific RCTs beyond the single completed rapamycin + vildagliptin trial before considering further evaluation stages
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

