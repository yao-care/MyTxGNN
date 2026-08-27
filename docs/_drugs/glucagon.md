---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# GLUCAGON: From Acute Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a glucagon receptor (GCGR) agonist used to raise blood glucose in acute hypoglycemia; formal NPRA license text and DrugBank MOA fields are currently data gaps, so this indication description is derived from the drug's known pharmacology as referenced in the evidence pack. The TxGNN model predicts a **99.24%** score for **Irritable Bowel Syndrome (IBS)**, but none of the 11 clinical trials or 20 publications collected actually test glucagon itself in IBS — the supporting evidence is almost entirely about **GLP-1 receptor agonists**, a mechanistically distinct molecule. This strongly suggests the prediction may be a knowledge-graph node-confusion artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hypoglycemia (glucose-elevating rescue therapy) — formal NPRA label text not yet available (data gap) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 (mechanism/preclinical studies only — none on glucagon itself) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for glucagon (DB00040) is currently a documented data gap (DG002). Based on what is available in this evidence pack, glucagon is a **GCGR (glucagon receptor) agonist** used clinically to acutely raise blood glucose — the opposite pharmacological direction from what is implicated in the IBS literature below.

The supporting evidence in this pack is overwhelmingly about **GLP-1 (glucagon-like peptide-1) and its receptor agonists** (native GLP-1, exendin-4, liraglutide, ROSE-010) — molecules that, despite sharing the same *proglucagon* gene precursor, act on a **different receptor (GLP-1R)** with different downstream effects: they inhibit gut motility and modulate the gut-brain axis, which is the actual mechanistic thread connecting this literature to IBS.

Because TxGNN's knowledge graph appears to link entities by shared proglucagon lineage, the high score for glucagon may reflect a **node-confusion artifact** — the model associating glucagon with disease evidence that in fact belongs to its biosynthetic relative, GLP-1. With no clinical trial or publication in this pack directly testing glucagon (the drug) in IBS, and original MOA data still unverified, the mechanistic case for glucagon-specific repurposing is currently unsupported.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | Tested ROSE-010 (a GLP-1 analog, not glucagon) on gastric/colonic motility in constipation-predominant IBS |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 vs. its analog ROSE-010 on prandial GI motility; mechanism study, not a glucagon trial |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1RA) in chronic pouch dysfunction after IPAA — not IBS, not glucagon |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Completed | 66 | Exercise intensity effects on gut dysbiosis and GLP-1 hormone levels in IBS — no drug intervention |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Completed | 37 | Butyrate's role in colon health/IBS; unrelated to glucagon |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Completed | 12 | Reactive hypoglycemia prevalence and fructo-oligosaccharide effect on glucose variability; not glucagon-IBS |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | NA | Active, not recruiting | 375 | Small-intestinal organoid model for nutrient/therapeutic agent effects; no glucagon or IBS link specified |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | NA | Completed | 33 | Gut-microbiota nutritional intervention for barrier integrity at altitude; unrelated |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | NA | Completed | 33 | Whole-grain rye bread's effect on microbiota-gut-brain axis in healthy subjects; unrelated |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | NA | Completed | 41 | Eating rate of ultra-processed foods and metabolic response; unrelated |

**Note:** All 11 trials in the evidence pack were graded "C" (low relevance) or pending by the reviewer — none directly evaluate glucagon in IBS patients.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1RA) reduced pain during IBS attacks; subgroup analysis of responders |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review/Meta-analysis | Frontiers in Endocrinology | GLP-1RAs and ROSE-010 inhibit migrating motor complex and reduce GI motility in IBS |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Annals of Gastroenterology | Real-world prescription/discontinuation patterns of GLP-1RAs in IBS patients |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Proposes a role for GLP-1-secreting L-cells in IBS pathophysiology |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observational (clinical correlation) | Clinics and Research in Hepatology and Gastroenterology | Lower serum GLP-1 correlates with abdominal pain in constipation-predominant IBS |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical (rat model) | Neurogastroenterology and Motility | Exendin-4 (GLP-1RA) improved GI dysfunction in a Wistar Kyoto rat IBS model |
| [31311066](https://pubmed.ncbi.nlm.nih.gov/31311066/) | 2019 | Preclinical (rat model) | Neurogastroenterology and Motility | Ghrelin receptor agonism sensitizes rat colonic neurons to exendin-4, relevant to postprandial IBS symptoms |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Observational (dietary intervention) | Frontiers in Nutrition | Low FODMAP diet increased circulating GLP-1 in IBS patients |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | The Journal of Headache and Pain | Reviews GLP-1RA effects on pain/headache disorders via neuronal pathways |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review/Perspective | Advances in Experimental Medicine and Biology | Discusses aerosolized GLP-1 delivery for diabetes and IBS |

**Note:** All listed literature concerns GLP-1 or its analogs/receptor agonists — none study glucagon itself in IBS.

---

## Malaysia Market Information

NPRA confirms glucagon is marketed in Malaysia with 1 active registration, but detailed license fields (registration number, product name, dosage form, approved indication text) are currently a data gap in this evidence pack and could not be populated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the entire evidentiary base (11 trials, 20 publications) concerns GLP-1 receptor agonists, not glucagon — the drug under evaluation acts on a different receptor with opposite metabolic effects. This pattern is consistent with a knowledge-graph confusion between glucagon and GLP-1 (both proglucagon-derived), and no data directly support repurposing glucagon itself for IBS.

**To proceed, the following is needed:**
- Confirmed original MOA data for glucagon (DG002) to formally rule in/out the GCGR-vs-GLP-1R mechanistic distinction
- TFDA/NPRA label warnings and contraindications (DG001, currently blocking S1 safety review)
- Formal NPRA license text (registration number, approved indication, dosage form) to complete the Malaysia market profile
- Direct pharmacological or clinical evidence testing glucagon (not GLP-1 analogs) in IBS, if any exists, before this candidate can advance past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

