---
layout: default
title: Magnesium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 5
---

# Magnesium Hydroxide
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

Using the drug-repurposing evaluation report template to generate the report from the supplied Evidence Pack.

# Magnesium Hydroxide: From Antacid/Laxative Use to Esophagitis

## One-Sentence Summary

Magnesium Hydroxide (DrugBank DB09104) is a well-established over-the-counter antacid and osmotic laxative (the active ingredient in "Milk of Magnesia"), currently marketed in Malaysia under **41 registrations**. The TxGNN model's top-ranked candidate indication is **Esophagitis**, supported by **1 clinical trial** and **19 publications** — but the trial was terminated, most literature concerns magnesium/aluminum-hydroxide *combination* antacids rather than magnesium hydroxide alone, and the model's own prediction score for this candidate is **0.00%**, which is a material caveat that should not be glossed over.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extracted in this evidence pack — all sampled NPRA/TFDA license `approved_indication_text` fields were empty. Magnesium hydroxide is generically recognized as an OTC antacid / osmotic laxative, but this specific dataset provides no confirmed label text (see Data Gap DG001/DG002 below) |
| Predicted New Indication | Esophagitis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 41 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this record in DrugBank. Based on general pharmacological knowledge, magnesium hydroxide dissociates in gastric fluid to release hydroxide ions that neutralize hydrochloric acid, rapidly raising intragastric and (transiently) intra-esophageal pH; at higher, poorly absorbed luminal doses it also draws water into the bowel osmotically, which underlies its separate use as a laxative.

Esophagitis is predominantly an acid-mediated mucosal injury process — whether driven by gastroesophageal reflux, direct chemical irritation, or (in the one directly relevant trial) radiation therapy. Because magnesium hydroxide's antacid action directly targets the acid component of that injury pathway, a mechanistic link to esophagitis is plausible. However, the strength of this specific candidate is limited: the only directly relevant registered trial, NCT01336530, tested **Tepilta®** — a fixed combination of oxetacaine (a topical anesthetic) and antacids — for radiation-induced esophagitis, not magnesium hydroxide as a single agent, and the trial was terminated before completion. Most supporting literature likewise studies magnesium hydroxide in combination with aluminum hydroxide (e.g., Mylanta, Maalox-type products) rather than as monotherapy. Combined with the TxGNN score of 0.00% for this candidate, the mechanistic plausibility is reasonable but the model confidence and trial-level evidence specific to esophagitis are both weak.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01336530](https://clinicaltrials.gov/study/NCT01336530) | Phase 3 | Terminated | 40 | Randomized, double-blind, placebo-controlled adaptive trial of Tepilta® (oxetacaine + antacid) vs. its individual components vs. placebo for radiation-induced esophagitis; designed to show superiority of the combination but was terminated before full enrollment, limiting conclusiveness. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2986275](https://pubmed.ncbi.nlm.nih.gov/2986275/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Sucralfate vs. alginate/antacid in a 6-week randomized trial for reflux esophagitis; ~70% of patients in both arms improved, esophagitis healed completely in 53% on sucralfate. |
| [6250928](https://pubmed.ncbi.nlm.nih.gov/6250928/) | 1980 | RCT (crossover) | J Int Med Res | Crossover trial comparing Liquid Gaviscon to a magnesium/aluminum hydroxide antacid gel for heartburn; Gaviscon gave faster, more complete relief than the Mg/Al antacid. |
| [8047802](https://pubmed.ncbi.nlm.nih.gov/8047802/) | 1994 | RCT | Scand J Gastroenterol | Double-blind trial in 80 children with GER comparing domperidone + Mg(OH)2/Al(OH)3, domperidone + alginate, domperidone alone, and placebo; combination arms showed clinical and pH-monitoring improvement. |
| [1798406](https://pubmed.ncbi.nlm.nih.gov/1798406/) | 1991 | Cohort | Minerva Pediatrica | 15 children with GER treated with Mg(OH)2/Al(OH)3 for 8 weeks; 12/15 cured, 3/15 improved, with reduced esophageal acid exposure time on pH monitoring. |
| [11854825](https://pubmed.ncbi.nlm.nih.gov/11854825/) | 1995 | Cohort/comparative | American Journal of Therapeutics | Single-blind crossover in 83 heartburn subjects comparing Al(OH)3/Mg(OH)2 vs. CaCO3 vs. placebo on esophageal/gastric pH after a refluxogenic meal. |
| [25419906](https://pubmed.ncbi.nlm.nih.gov/25419906/) | 2014 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Review of pharmacological treatment (including antacids) for pediatric gastro-esophageal reflux; highlights limited high-quality evidence overall. |
| [10908549](https://pubmed.ncbi.nlm.nih.gov/10908549/) | 2000 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Review of cisapride for pediatric GOR, noting safety concerns (QTc prolongation, arrhythmia) with prokinetic alternatives to antacid therapy. |
| [24355558](https://pubmed.ncbi.nlm.nih.gov/24355558/) | 2014 | Review | Gastroenterología y Hepatología | Update on GERD management, noting ~1/3 of non-erosive patients respond unsatisfactorily to PPIs, motivating interest in adjunct/alternative acid-neutralizing therapies. |
| [10848650](https://pubmed.ncbi.nlm.nih.gov/10848650/) | 2000 | Review | Alimentary Pharmacology & Therapeutics | Review of alginate raft-forming formulations (e.g., Gaviscon, often combined with antacids) for heartburn and esophagitis, describing their distinct gel-raft mechanism. |
| [1783346](https://pubmed.ncbi.nlm.nih.gov/1783346/) | 1991 | Double-blind comparative study | Fortschritte der Medizin | Multicenter double-blind study in 97 patients comparing a smectite/Al(OH)3/Mg(OH)2 antacid combination against a standard aluminum hydroxide antacid for gastritis, esophagitis, and functional upper-abdominal symptoms. |

---

## Malaysia Market Information

Malaysia market status is recorded as **Marketed (已上市)** with **41 total registrations**, but the individual license records supplied in this evidence pack (license number, product name, dosage form, manufacturer, approved indication text) were all returned empty — this appears to be a data-extraction gap rather than an absence of registrations, and should be remediated before this information is used in any regulatory or safety assessment (see Data Gap DG001).

---

## Safety Considerations

Please refer to the package insert for safety information — structured `key_warnings`, `contraindications`, and DDI data were all returned as data gaps (DG001, marked Blocking severity) and no interaction records were found.

**Additional note from literature evidence (not from structured safety data):** two independent case reports identified elsewhere in this evidence pack — [38152602](https://pubmed.ncbi.nlm.nih.gov/38152602/) (fatal hypermagnesemia in patients taking magnesium hydroxide, 2023) and [9533062](https://pubmed.ncbi.nlm.nih.gov/9533062/) (antacid-induced hypermagnesemia in a patient with normal renal function and bowel obstruction) — flag a real hypermagnesemia risk with magnesium hydroxide, particularly in renal impairment or reduced GI motility. This should be treated as a priority safety item for any repurposing pathway, even though it did not surface in the formal `safety` fields.

---

## Other Predicted Indications (Same Evidence Pack)

This evidence pack ("TW-DB09104-multi") evaluated five candidate indications together. For context, the other four ranked candidates are:

| Rank | Disease | Evidence Level | Decision Stage | Recommendation |
|------|---------|----------------|----------------|-----------------|
| 2 | Constipation disorder | L2 | S2 | Proceed with Guardrails |
| 3 | Gastroesophageal reflux disease | L2 | S2 | Proceed with Guardrails |
| 4 | Peptic esophagitis | L3 | S1 | Research Question |
| 5 | Peptic ulcer disease | L4 | S1 | Hold |

Notably, **constipation** (Mg(OH)2's classic osmotic-laxative use) and **GERD** (two Phase 1 trials, NCT03065816 and NCT03069963, directly measuring antacid activity by scintigraphy/pH-metry) have comparably strong or arguably stronger direct evidence than esophagitis itself, and may warrant equal or higher priority in follow-up evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The acid-neutralizing mechanism is plausible for esophagitis and the evidence level is L2, but the only directly relevant trial is a terminated Phase 3 study of a different combination product, most literature covers magnesium hydroxide only as part of combination antacids, and the model's own prediction score (0.00%) is anomalously low and should not be treated as a confidence signal without validation.

**To proceed, the following is needed:**
- Extraction of actual NPRA/TFDA license and label text (currently blank for all sampled entries — DG001, Blocking)
- DrugBank/DrugBank API mechanism-of-action data (DG002, High)
- Formal safety labeling: key warnings, contraindications, and DDI data (currently all data gaps)
- Clarification/validation of the TxGNN scoring pipeline for this candidate, given the 0.00% score across all five ranked indications
- A focused safety assessment on hypermagnesemia risk (informed by PMID 38152602 and 9533062), especially for patients with renal impairment, before considering any monotherapy use in esophagitis
- Consider evaluating the constipation and GERD candidates (also L2, with more direct single-agent trial evidence) in parallel, as they may represent stronger near-term repurposing opportunities than esophagitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

