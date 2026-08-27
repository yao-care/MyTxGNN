---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 7
---

# Desmopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Desmopressin: From Original Indication (Not Extracted) to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin (DrugBank DB00035) is a registered drug in Taiwan (7 TFDA licenses, market status "已上市"), though its labeled original indication text was not captured in this data extract. The TxGNN model's top-ranked prediction is efficacy in **congenital prothrombin deficiency**, but the supporting evidence — **1 clinical trial** (studying a different drug, emicizumab) and **4 publications** (none specifically addressing this disease) — does not substantiate the mechanistic pairing, and the evidence pack itself flags this as a likely **evidence mismatch**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA license indication text was not extracted for any of the 7 registrations (Data Gap DG001) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| Malaysia Market Status (TFDA/Taiwan data) | ✓ Marketed (已上市) |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for desmopressin is not available in the source record (`original_moa` is a flagged Data Gap, DG002). However, the evidence pack's own literature-derived rationale consistently describes desmopressin's established pharmacology: it is a vasopressin V2-receptor agonist that triggers release of endogenous von Willebrand factor (vWF) and Factor VIII from endothelial Weibel-Palade bodies, and enhances platelet adhesion. This mechanism underlies its accepted (including off-label) use in mild hemophilia A, von Willebrand disease, and certain platelet-release disorders — a pattern reflected across the literature attached to several of the other predicted indications in this evidence pack (e.g. PMID 36656570, PMID 21509710).

For congenital prothrombin (Factor II) deficiency specifically, this mechanism does not apply: prothrombin synthesis and activity are unrelated to the vWF/Factor VIII release pathway that desmopressin acts on. Consistent with this, the attached clinical trial (NCT04567511) studies emicizumab — not desmopressin — for mild hemophilia A, and the four literature citations concern acquired hemophilia A, combined Factor V/VIII deficiency, and general rational treatment of bleeding disorders, none of which directly address prothrombin deficiency. The evidence pack itself characterizes this as an "evidence mismatch": a high TxGNN score without a coherent mechanistic or clinical basis.

Two other candidates in this same evaluation batch show materially stronger alignment and may warrant separate follow-up: **primary release disorder of platelets** (rank 4, evidence level L3, decision stage S2, recommendation "Proceed with Guardrails") and **Glanzmann thrombasthenia** (rank 3, evidence level L3, decision stage S1, "Research Question"), both of which are directly supported by mechanism-relevant literature on desmopressin's known bleeding-time-shortening effects.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Studies Hemlibra (emicizumab) — not desmopressin — in mild hemophilia A. Relevance graded **C** (low): different drug, different indication than congenital prothrombin deficiency. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Diagnosis, aetiology, and treatment of acquired hemophilia A — not prothrombin deficiency. |
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | Rational treatment options for congenital bleeding disorders generally (hemophilia A, von Willebrand disease). |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki | Cesarean section management with Factor VIII replacement in combined Factor V/VIII deficiency — not prothrombin deficiency. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki | DDAVP administration in combined Factor V/VIII deficiency — not prothrombin deficiency. |

None of the above literature directly studies desmopressin in congenital prothrombin deficiency.

---

## Malaysia Market Information

License-level detail (authorization number, product name, dosage form, indication text) was not captured for any of the 7 TFDA registrations in this data extract — only the aggregate count and market status ("已上市") are available. Per Data Gap DG001, resolving this requires downloading and parsing the TFDA label PDFs directly.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings and contraindications for desmopressin were not available in this extract (Data Gap DG001, severity: Blocking) — this gap currently prevents the candidate from entering the S1 safety-evaluation stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for congenital prothrombin deficiency is high, but the attached clinical trial and literature evidence do not address this drug-disease pairing, and the underlying mechanism (vWF/Factor VIII release) has no established link to prothrombin synthesis or activity. This is assessed as a likely evidence mismatch rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety evaluation can begin
- DrugBank mechanism-of-action detail (DG002) to confirm or rule out any indirect pathway to prothrombin deficiency
- If this drug-disease pairing is to be pursued further, targeted literature/trial searches specific to desmopressin and Factor II deficiency (none currently exist in this pack)
- Consider prioritizing review of the same batch's stronger candidates instead — **primary release disorder of platelets** (S2, "Proceed with Guardrails") and **Glanzmann thrombasthenia** (S1, "Research Question") — which have direct mechanistic and literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

