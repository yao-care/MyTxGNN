---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
---

# Milrinone
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

# Milrinone: From Acute Decompensated Heart Failure to Headache Disorder (Reversible Cerebral Vasoconstriction Syndrome)

## One-Sentence Summary

Milrinone is a PDE3-inhibitor inotrope/vasodilator used short-term for acute decompensated heart failure and cardiogenic shock. Among 10 TxGNN-predicted indications, the four highest-scoring hits (alopecia, hypotrichosis simplex, congenital hypotrichosis milia, diffuse alopecia areata) are flagged by the evidence pack itself as likely embedding-space artifacts — **zero supporting trials or literature**, all scored "Hold." The only candidate with real, if narrow, clinical support is **Headache Disorder**, driven specifically by case-report evidence for milrinone reversing vasospasm in Reversible Cerebral Vasoconstriction Syndrome (RCVS), with **1 loosely-matched trial** and **3 case reports** (L3).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute decompensated heart failure / cardiogenic shock (short-term IV inotropic support) — TFDA/NPRA-specific indication text is a data gap in this pack |
| Predicted New Indication | Headache Disorder (specifically: RCVS-associated headache) |
| TxGNN Prediction Score | 99.46% (rank 7,623 of candidates) |
| Evidence Level | L3 (case reports/case series only) |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision | Research Question |

*Note: predicted_indications[0] (alopecia, 99.91%) was not used as the headline — its own rationale explicitly calls it "疑為 embedding 空間鄰近性造成的假陽性" with no clinical trials, no literature, and a Hold recommendation. Rank 6 (congestive heart failure, L1) was also excluded from the headline because it is milrinone's *existing* approved use, not a repurposing candidate — its own rationale states "此為已建立用途而非新穎再利用."*

## Why is This Prediction Reasonable?

Milrinone is a phosphodiesterase-3 (PDE3) inhibitor that raises intracellular cAMP in cardiac and vascular smooth muscle, producing positive inotropy and vasodilation (an "inodilator"). This mechanism is well established for cardiac use, but it also gives milrinone direct cerebral-artery vasodilating properties when delivered intra-arterially.

Reversible Cerebral Vasoconstriction Syndrome (RCVS) is a rare neurological disorder defined by multifocal, reversible constriction of cerebral arteries that classically presents as recurrent thunderclap headache. Because milrinone dilates vascular smooth muscle, it has been used off-label as an intra-arterial rescue therapy to reverse the vasospasm driving RCVS symptoms — this is the specific and mechanistically coherent link behind the "headache disorder" prediction, not a general antimigraine or analgesic effect.

This mechanism is narrow: it applies to vasospasm-driven secondary headache (RCVS), not to primary headache disorders like migraine or tension headache — a distinction the underlying evidence pack itself flags. Notably, the single clinical trial linked to this prediction (NCT06205758) is a milrinone-vs-levosimendan cardiogenic shock trial with no connection to headache, graded "C" (likely a data-linkage error) — the actual support comes entirely from the literature below.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06205758](https://clinicaltrials.gov/study/NCT06205758) | N/A | Unknown | 1600 | Compares milrinone vs. levosimendan as initial inotrope in acute/advanced heart failure with renal insufficiency — **not related to headache**; included in the evidence pack as a low-relevance (grade C) match, likely a data-linkage artifact. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18647181](https://pubmed.ncbi.nlm.nih.gov/18647181/) | 2009 | Case report | Headache | Intra-arterial milrinone used to treat RCVS after a patient failed oral calcium channel blockers and developed focal neurological deficits. |
| [25440342](https://pubmed.ncbi.nlm.nih.gov/25440342/) | 2015 | Case series | J Stroke Cerebrovasc Dis | Describes a diagnostic approach for RCVS (thunderclap headache + reversible segmental vasoconstriction); milrinone referenced in the treatment context. |
| [34784343](https://pubmed.ncbi.nlm.nih.gov/34784343/) | 2021 | Case report | Am J Case Rep | RCVS in the setting of eclampsia, responding to milrinone infusion. |

## Malaysia Market Information

NPRA records confirm Milrinone holds **1 active registration** in Malaysia with market status "已上市 (Marketed)." License number, product name, dosage form, and the approved indication text were not captured in this data pull — this is recorded as **Data Gap DG001 (Blocking)** in the evidence pack and must be resolved before any safety review can proceed.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data were not available in this evidence pack — DG001, severity: Blocking.)

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence is limited to three case reports/series (L3) supporting a mechanistically specific but narrow use — intra-arterial milrinone for RCVS-driven headache — not general headache disorders. The one linked clinical trial is unrelated to headache, and the underlying safety data (warnings/contraindications) needed for any S1 safety gate is a **Blocking** data gap.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/NPRA package insert for warnings, contraindications, and DDI data
- Resolve DG002 (High): confirm MOA via DrugBank API rather than relying on rationale-text inference
- Clarify route of administration required for RCVS efficacy (published cases use intra-arterial infusion — standard IV/oral milrinone formulations may not replicate this effect)
- Seek a dedicated RCVS case series or registry data beyond the 3 existing case reports to raise evidence level above L3
- Separately re-triage rank 1–4 (alopecia/hypotrichosis cluster) and rank 7–9 (migraine cluster) predictions — evidence pack already recommends Hold with no further action pending new trial/literature signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

