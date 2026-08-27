---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

Using the provided Evidence Pack, I selected the strongest, most actionable predicted indication for the headline analysis. A quick note on that judgment call before the report: the JSON contains 7 TxGNN-predicted indications for calcitriol, ranked by raw model score — but rank #1 ("obsolete vitamin D deficiency") is explicitly flagged in its own rationale as an ontology artifact with **no supporting trials/literature and Hold status (L5/S0)**. The strongest evidence-backed candidate is actually **rank #7, "hereditary hypophosphatemic rickets"** (L2, decision stage S2, "Proceed with Guardrails," with a Phase 4 trial and a Grade-A direct-evidence Phase 1 calcitriol monotherapy trial). I built the report around that candidate rather than blindly following list order, since a score-ranked #1 with zero evidence would produce a misleading report.

---

# Calcitriol: From Hypocalcemia/Secondary Hyperparathyroidism to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

> Calcitriol (active vitamin D3, DrugBank DB00136) is an established therapy for disorders of calcium/phosphate homeostasis such as hypocalcemia and secondary hyperparathyroidism.
> Among several TxGNN-predicted indications in this evidence pack, **Hereditary Hypophosphatemic Rickets** stands out as the most actionable candidate,
> supported by **7 clinical trials** (including a direct Phase 4 and an Early Phase 1 calcitriol-specific trial) and **20 publications**, several of which report decades of direct clinical experience using calcitriol in this exact disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in NPRA registration text in this evidence pack (all `approved_indication_text` fields were empty). Based on general pharmacological knowledge, calcitriol is used for hypocalcemia and secondary hyperparathyroidism of chronic kidney disease, and for hypoparathyroidism. |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets (incl. X-linked hypophosphatemia, XLH) |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available in this evidence pack. Based on known pharmacology, calcitriol is the biologically active metabolite of vitamin D3 (1,25-dihydroxyvitamin D3), and it acts by binding the vitamin D receptor (VDR) to increase intestinal calcium/phosphate absorption and regulate renal tubular calcium handling. Its efficacy in managing hypocalcemia and secondary hyperparathyroidism is well established, and mechanistically it is directly applicable to disorders of impaired endogenous calcitriol synthesis.

Hereditary hypophosphatemic rickets — most commonly X-linked hypophosphatemia (XLH) caused by PHEX gene mutations — leads to excess circulating FGF23, which suppresses renal 1α-hydroxylase activity and renal phosphate reabsorption. The net effect is chronic hypophosphatemia **combined with inappropriately low or normal (rather than compensatorily elevated) endogenous calcitriol levels**. This is not a peripheral or coincidental link: exogenous calcitriol replacement, together with phosphate supplementation, was the international standard of care for XLH for decades before the FGF23-targeting biologic burosumab became available. The mechanistic rationale is therefore direct — calcitriol replaces a metabolite whose endogenous synthesis is pathologically suppressed in this exact disease — rather than a speculative cross-disease inference.

Several other TxGNN-predicted indications in this pack (e.g., familial isolated hypoparathyroidism, Dahlberg-Borer-Newcomer syndrome/pseudohypoparathyroidism) share the same underlying logic — restoring active vitamin D signaling downstream of a PTH- or FGF23-driven synthesis defect — reinforcing that this is a coherent pharmacological class of repurposing candidates rather than a single outlier prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, not recruiting | 20 | **[Direct evidence]** Calcitriol monotherapy (without phosphate) in children/adults with XLH; evaluates effect on serum phosphate, skeletal mineralization, kidney calcification risk, and growth. |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | **[Direct evidence]** Compares high- vs low-dose active vitamin D (calcitriol) combined with neutral phosphate in children with XLH; aims to establish optimal weight-based calcitriol dosing. |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, not recruiting | 27 | Evaluates INZ-701 (a novel agent, not calcitriol) in ENPP1 deficiency; included as indirect background on the broader hypophosphatemic-rickets treatment landscape. |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Observational cohort characterizing inappropriate FGF23 secretion in hospitalized hypophosphatemia patients; natural-history/background data, not an interventional calcitriol trial. |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn (enrollment 0) | 0 | Intended to study cinacalcet (not calcitriol) as add-on therapy for familial hypophosphatemic rickets; explicitly notes that high-dose phosphate + calcitriol is the current standard treatment. Background reference only. |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and sclerostin in kidney stone formers; disease-mechanism background, not an interventional trial. |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not yet recruiting | 65 | ³¹P-MRS methodology study measuring ATP concentration in phosphate diabetes (including XLH); imaging/biomarker methodology, not a drug trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical study | The New England Journal of Medicine | In 11 children with vitamin D-resistant rickets, calcitriol (0.25–1 µg/day) raised serum calcitriol above normal, increased intestinal phosphate absorption, and reduced phosphate supplementation needs versus phosphate or ergocalciferol alone. |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical study | The Journal of Clinical Investigation | High-dose calcitriol (68.2±10 ng/kg/day) plus phosphorus healed coexistent osteomalacia in X-linked hypophosphatemic rickets, which conventional vitamin D + phosphate therapy alone failed to resolve. |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Cohort | Calcified Tissue International | Bone mineral measurements in 17 children with familial hypophosphatemic rickets following calcitriol + phosphate therapy, tracking axial/appendicular bone mineral density over time. |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort | Pediatric Endocrinology Reviews | Height data from 127 XLH patients across 49 centers; discusses spontaneous growth and the effect of early calcitriol + phosphate therapy versus untreated natural history. |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | The Lancet | Comprehensive review of XLH pathophysiology (PHEX/FGF23 axis) and management, noting decreased calcitriol synthesis as a core driver of disease and a rationale for active vitamin D replacement. |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcified Tissue International | Updated review of XLH diagnosis and therapy, covering conventional calcitriol/phosphate treatment alongside newer FGF23-targeted biologics. |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Hormone Research in Paediatrics | Historical and mechanistic review of rickets, vitamin D, and calcium/phosphate metabolism, including active vitamin D metabolite therapy. |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Review | Arquivos Brasileiros de Endocrinologia & Metabologia | Reviews hereditary/acquired hypophosphatemic conditions sharing impaired renal phosphate reabsorption and inappropriately low/normal calcitriol, causing rickets/osteomalacia. |
| [31392510](https://pubmed.ncbi.nlm.nih.gov/31392510/) | 2020 | Review | Pediatric Nephrology | Reviews mineralization defects in hypophosphatemic rickets driven by FGF23 excess and reduced renal phosphate reabsorption. |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Cohort/Case report | Journal of Bone and Mineral Research | Case of an infant with hypophosphatemic rickets and short stature, illustrating diagnostic work-up (TmP/GFR, FGF23) and clinical presentation. |

---

## Malaysia Market Information

Calcitriol holds **7 active NPRA registrations** in Malaysia with overall market status **✓ Marketed**. However, the evidence pack's `taiwan_regulatory.licenses` array did not contain populated authorization numbers, product names, dosage forms, or approved-indication text for any of the 7 entries — this data was not captured during collection and should be pulled directly from the NPRA product registration database (QUEST3+) before finalizing any regulatory submission.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings` and `safety.contraindications` were both returned as data gaps, and the DDI query returned no results. This is flagged as a **Blocking** data gap — see Conclusion below — because calcitriol carries well-known class risks such as hypercalcemia/hypercalciuria that require monitoring, and this evidence pack does not yet contain the source data to substantiate that.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanistic link is strong and non-speculative: hereditary hypophosphatemic rickets (XLH) involves FGF23-driven suppression of endogenous calcitriol synthesis, and exogenous calcitriol + phosphate was the long-standing standard of care before biologic therapies existed. This is corroborated by a direct Phase 4 dosing trial (NCT03820518) and a Grade-A Early Phase 1 monotherapy trial (NCT03748966), plus multiple decades-old clinical studies directly using calcitriol in this disease.
- However, the drug-level safety dossier (key warnings, contraindications) is currently marked as a **Blocking** data gap in this pack, and NPRA licensing details (indication text, dosage forms) are also incomplete. Neither prevents moving forward with guardrails, but both must be resolved before any safety sign-off (S1 stage).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap, DG001) — required before this candidate can pass initial safety screening (S1).
- Detailed mechanism of action (MOA) data from DrugBank (High-priority gap, DG002) — needed to formalize the mechanistic-relevance write-up beyond general pharmacological knowledge.
- Complete NPRA license records (authorization numbers, product names, approved indication text, dosage forms) for the 7 registered products.
- A dedicated literature/trial reconciliation for the other TxGNN candidates flagged as "Research Question" (renal tubular acidosis, familial isolated hypoparathyroidism) — these share the same mechanistic class and may be worth a manual literature search given the apparent evidence-collection gap noted in their rationales.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

