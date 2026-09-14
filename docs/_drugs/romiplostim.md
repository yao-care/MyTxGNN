---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 602
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia (ITP) to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim is a thrombopoietin receptor (TPO-R) agonist whose approved use is referenced within this evidence pack as immune thrombocytopenia (ITP); detailed original-indication text from the Malaysia registry record itself is not populated.
The TxGNN model predicts it may also be effective for **primary release disorder of platelets**, a mechanistic match with Romiplostim's core action of stimulating megakaryocyte-driven platelet production.
Currently only **1 clinical trial** (an observational cohort, not interventional) and **2 publications** (both review/mechanistic, tier 3) support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immune Thrombocytopenia (ITP) — referenced in evidence-pack rationale; NPRA license indication text not populated in source data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% (rank 7 among candidates) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (DrugBank MOA field) is flagged as a data gap in this pack. Based on the information available, however, the repurposing rationale for this candidate states that Romiplostim's core mechanism is stimulating megakaryocyte proliferation and differentiation to increase platelet production — i.e., it acts as a TPO receptor agonist.

"Primary release disorder of platelets" describes a disorder of platelet generation/release from megakaryocytes. This aligns directly with Romiplostim's known mode of action in its approved ITP use, where the drug boosts platelet counts by driving thrombopoiesis. The mechanistic overlap is therefore high in principle.

That said, the supporting evidence currently sits at the basic-science/mechanistic level (bone-marrow megakaryocytopoiesis literature) rather than at the level of interventional trials specifically targeting this disease label. The one available clinical trial is an observational cohort study on thrombosis risk factors in ITP patients, not a treatment trial — it establishes population overlap but not therapeutic efficacy for this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Observational cohort on thrombosis risk factors in immune thrombocytopenia (ITP); non-interventional, does not directly test Romiplostim efficacy for this disease label — population overlap only (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Reviews megakaryocytopoiesis and thrombopoiesis biology, including thrombopoietin (TPO) as the primary growth factor for the megakaryocyte lineage — mechanistic basis, not clinical trial data. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Mechanistic/Basic Study | Haematologica | Shows antiplatelet autoantibodies in ITP inhibit proplatelet formation and impair platelet production in vitro — supports the biological rationale for TPO-R agonist therapy but is not a clinical efficacy study. |

---

## Malaysia Market Information

The registry record confirms 1 active license (market status: Marketed), but the license number, product name, dosage form, and approved-indication text fields are not populated in the current data extract. Detailed authorization information needs to be pulled from the NPRA product registry directly.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (primary release disorder of platelets) is supported only by mechanistic/basic-science literature and one non-interventional observational trial — no direct interventional evidence exists yet for this specific disease label.
- Two Blocking/High-severity data gaps (package insert warnings & contraindications; detailed MOA) currently prevent this candidate from clearing the S1 safety pre-screen.

**To proceed, the following is needed:**
- NPRA package insert (warnings, contraindications) — currently a Blocking data gap
- DrugBank-sourced mechanism-of-action detail — currently a High-severity data gap
- Complete NPRA registration record (license number, product name, dosage form, full approved indication text)
- An interventional study (even early-phase) directly testing Romiplostim in a platelet-release-disorder population, rather than relying solely on ITP-adjacent mechanistic literature

*Note: a separate candidate in this same evidence pack, "platelet-type bleeding disorder" (rank 8), already reaches L1 evidence (Phase 3 RECITE trial and other Phase 3/4 studies) but substantially overlaps with Romiplostim's already-approved ITP-related use rather than representing a genuinely novel indication — it is not the primary subject of this report but may warrant its own evaluation if treated as a distinct label.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

