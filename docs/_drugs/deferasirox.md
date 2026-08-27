---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 5
---

# Deferasirox
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

# Deferasirox: From Transfusional Iron Overload to Beta-Thalassemia and Related Diseases

## One-Sentence Summary

Deferasirox is an oral iron chelator originally used to manage chronic iron overload caused by frequent blood transfusions, most commonly in patients with beta-thalassemia. The TxGNN model's top prediction, **beta-thalassemia and related diseases**, is supported by **7 clinical trials** (including two completed Phase 3 RCTs) and **19 publications** — but this is largely an evidence extension within the drug's existing approved use rather than a genuinely new indication. Key safety data (warnings, contraindications, DDI) and full Malaysia license details are currently missing from this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic iron overload due to frequent blood transfusions (transfusional hemosiderosis), most commonly associated with beta-thalassemia — based on Deferasirox's globally known approved use; exact NPRA label text was not returned by this query (see Malaysia Market Information) |
| Predicted New Indication | Beta-thalassemia and related diseases |
| TxGNN Prediction Score | 0.00% *(note: all 5 predicted indications in this evidence pack report a score of 0.0 — this looks like a data/scoring pipeline anomaly and should be verified against the raw TxGNN output before being used for ranking)* |
| Evidence Level | L1 (≥2 completed Phase 3 trials support this disease area) |
| Malaysia Market Status | Marketed (已上市) |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action data is available for Deferasirox in this evidence pack. Based on well-established public pharmacology, Deferasirox is an oral, selective ferric iron (Fe³⁺) chelator that forms a 2:1 complex with iron for faecal excretion, and it is already proven effective for chronic transfusional iron overload in beta-thalassemia major.

Importantly, the evidence pack's own rationale flags that this "predicted new indication" largely overlaps with the drug's existing approved use: transfusional iron overload is, in practice, predominantly a beta-thalassemia complication. The predicted indication is therefore better understood as an **evidence extension within the current approved scope** (e.g., earlier/low-dose intervention, non-transfusion-dependent thalassemia subtypes, or expanded haemoglobinopathy coverage such as sickle cell disease and MDS) rather than a true repurposing into an unrelated disease area.

Mechanistically this still makes sense: any condition producing chronic iron accumulation from repeated transfusions or ineffective erythropoiesis (beta-thalassemia major/intermedia, other haemoglobinopathies, MDS) shares the same underlying pathology that Deferasirox's chelation mechanism addresses, which is why the strongest trial evidence (Phase 3, n=595 and n=336, both completed) clusters around this disease group.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00061750](https://clinicaltrials.gov/study/NCT00061750) | Phase 3 | Completed | 595 | Randomized, open-label trial comparing long-term Deferasirox (ICL670) vs deferoxamine in beta-thalassemia patients with transfusional hemosiderosis; core registration evidence |
| [NCT02604433](https://clinicaltrials.gov/study/NCT02604433) | Phase 3 | Completed | 336 | Double-blind, placebo-controlled trial in transfusion-dependent β-thalassemia — **note: this trial evaluates Luspatercept, not Deferasirox**; included here as disease-area context rather than direct drug evidence |
| [NCT01709838](https://clinicaltrials.gov/study/NCT01709838) | Phase 4 | Completed | 134 | Long-term efficacy/safety of Deferasirox in non-transfusion-dependent thalassemia (NTDT) based on liver iron concentration change over 260 weeks |
| [NCT00873041](https://clinicaltrials.gov/study/NCT00873041) | Phase 2 | Completed | 166 | Randomized, double-blind, placebo-controlled trial (THALASSA study) of Deferasirox in NTDT patients with iron overload |
| [NCT00061763](https://clinicaltrials.gov/study/NCT00061763) | Phase 2 | Completed | 175 | One-year study of Deferasirox effect on liver iron content in chronic anemias with transfusional hemosiderosis unable to use deferoxamine |
| [NCT00390858](https://clinicaltrials.gov/study/NCT00390858) | Phase 2 | Completed | 40 | 4-year extension study of long-term safety, tolerability, PK and liver iron concentration effects of Deferasirox in pediatric transfusion-dependent β-thalassemia major |
| [NCT03920657](https://clinicaltrials.gov/study/NCT03920657) | Phase 2 | Terminated | 11 | Early, low-dose Deferasirox to suppress non-transferrin-bound iron in lower-risk MDS; terminated, small sample — hypothesis-generating only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16627763](https://pubmed.ncbi.nlm.nih.gov/16627763/) | 2006 | Review | Blood | Reviews new data on Deferasirox and deferiprone for transfusional iron overload in thalassemia major, highlighting cardiac disease as leading cause of death without adequate chelation |
| [18042472](https://pubmed.ncbi.nlm.nih.gov/18042472/) | 2007 | Review | Clinical Therapeutics | Clinical review of Deferasirox for transfusion-related iron overload, covering mechanism, dosing and safety profile |
| [24083402](https://pubmed.ncbi.nlm.nih.gov/24083402/) | 2013 | Review | Expert Review of Hematology | Reviews efficacy/safety of Deferasirox specifically in non-transfusion-dependent thalassemia (NTDT) |
| [35014065](https://pubmed.ncbi.nlm.nih.gov/35014065/) | 2022 | Cohort | Vox Sanguinis | Dual chelation therapy with Deferasirox and deferoxamine in beta-thalassemia major to overcome monotherapy tolerability/toxicity limits |
| [20007138](https://pubmed.ncbi.nlm.nih.gov/20007138/) | 2010 | Registry/Cohort | Haematologica | French National Registry data on complications and treatment (including chelation) in beta-thalassemia patients |
| [27606437](https://pubmed.ncbi.nlm.nih.gov/27606437/) | 2016 | Cohort | J Pediatr Hematol Oncol | Case-control study of health-related quality of life in children/adolescents with beta-thalassemia major on different iron chelators |
| [29451226](https://pubmed.ncbi.nlm.nih.gov/29451226/) | 2018 | Cohort | Acta Bio-Medica | Final adult height and endocrine complications in beta-thalassemia major patients with vs without oral iron chelation |
| [28404539](https://pubmed.ncbi.nlm.nih.gov/28404539/) | 2018 | Registry | Turkish J Haematology | Turkish National Hemoglobinopathy Registry data on thalassemia demographics and disease control program outcomes |
| [38519604](https://pubmed.ncbi.nlm.nih.gov/38519604/) | 2024 | Registry | Annals of Hematology | Spanish REHem-AR registry on demographics, complications and management of TDT/NTDT β-thalassemia patients |
| [26613264](https://pubmed.ncbi.nlm.nih.gov/26613264/) | 2016 | Review | Expert Review of Hematology | Clinical monitoring and management of chelation-related complications (DFO, DFP, DFX) in β-thalassemia patients |

---

## Malaysia Market Information

NPRA records confirm **14 registered licenses** for Deferasirox with a market status of **已上市 (Marketed)**. However, this query did not return the underlying license details (authorization numbers, product names, dosage forms, or approved indication text — all fields came back empty). Full registration details should be re-verified directly against the NPRA QUEST3+ database or product label before this data is used for regulatory decision-making.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were returned for this query (all marked as data gaps in the evidence pack), and retrieving the TFDA/NPRA package insert is flagged as a **blocking** gap for safety pre-screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is supported by strong trial evidence (L1: two completed Phase 3 trials) and is mechanistically close to Deferasirox's existing approved use, so the efficacy case is reasonably solid. However, it is more accurately framed as an indication/subtype extension (e.g., NTDT, early intervention, broader haemoglobinopathy coverage) than a novel repurposing, and a blocking safety data gap prevents a full go/no-go decision at this time.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications, drug interactions) — currently blocking safety pre-screening (DG001)
- Deferasirox mechanism-of-action data from DrugBank (DG002)
- Complete NPRA license details (authorization numbers, product names, dosage forms, approved indication text) for the 14 registered products
- Verification of the TxGNN prediction scores, which currently show 0.0 across all candidate indications — likely a data pipeline issue rather than a true model output
- Clarification on whether NCT02604433 (a Luspatercept trial) should remain in the Deferasirox evidence set, or be reclassified as disease-context rather than drug-specific evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

