---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide: From Unrecorded Original Indication to Pulmonary Arterial Hypertension

## One-Sentence Summary

Nitric oxide (DrugBank DB00435) is already marketed in Malaysia, but its originally approved indication and mechanism of action are not captured in the regulatory data pulled for this evaluation. Among ten TxGNN-predicted indications in this pack, **Pulmonary Arterial Hypertension (PAH)** stands out with by far the strongest supporting evidence — **50 clinical trials** and **20 publications** retrieved — while five of the other top-scoring predictions (e.g., periodontal malformation syndrome, hypertrichosis) are explicitly flagged in the evidence review as knowledge-graph co-occurrence noise rather than real mechanistic signals. This report focuses on PAH as the credible repurposing candidate.

*Note: predicted_indications is ranked by raw TxGNN score, under which rank 1–5 are algorithmic noise (Evidence Level L5, recommendation "Hold"). PAH (rank 7) is presented here instead because it is the highest-quality candidate (L1 evidence) in the pack.*

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication or license text is present in the current regulatory data |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.41% (rank 8214 among candidate diseases) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this product is not available in the current data pull (DG002, High severity), and no original indication is on file either — this is itself a data gap that needs resolving before final sign-off.

That said, the mechanistic rationale for nitric oxide in PAH does not depend on this specific product's label — it is grounded in well-established pharmacology. Nitric oxide is an endogenous vasodilator, and PAH's core pathophysiology involves deficient endothelial NO synthesis/utilization. Current standard-of-care PAH therapies (PDE5 inhibitors such as sildenafil, and soluble guanylate cyclase stimulators such as riociguat) act downstream of exactly this NO–cGMP pathway. Inhaled NO is already used clinically for acute pulmonary vasoreactivity testing and for persistent pulmonary hypertension of the newborn, so this is a direct, clinically precedented mechanistic link rather than a speculative one.

Two related PAH subtypes in this evidence pack — PAH associated with congenital heart disease (rank 8, L2) and PAH associated with connective tissue disease (rank 9, L3) — share the same NO-pathway rationale and are reasonable secondary research questions, though with thinner direct-intervention evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02725372](https://clinicaltrials.gov/study/NCT02725372) | Phase 3 | Terminated | 207 | Placebo-controlled RCT of pulsed inhaled NO vs. placebo in symptomatic PAH |
| [NCT01165047](https://clinicaltrials.gov/study/NCT01165047) | Phase 2 | Completed | 10 | GeNO Nitrosyl NO-delivery system; confirmed iNO reduces PVR in reversible PH |
| [NCT05757557](https://clinicaltrials.gov/study/NCT05757557) | Phase 1/2 | Completed | 136 | Perioperative NO-conditioning via plasma-chemical synthesis; selective pulmonary vasodilation, improved oxygenation |
| [NCT02436512](https://clinicaltrials.gov/study/NCT02436512) | Phase 3 | Withdrawn | 0 | EAGLE study: iNO-induced vasodilation as predictor of weaning from parenteral prostacyclin in WHO Group 1 PAH |
| [NCT02734953](https://clinicaltrials.gov/study/NCT02734953) | Phase 2 | Completed | 10 | Effects of iNO on invasively-derived pulmonary vascular resistance parameters in PAH |
| [NCT01728220](https://clinicaltrials.gov/study/NCT01728220) | Phase 2 | Completed | 159 | INHALE 1: dose-confirming RCT of pulsed iNO in WHO Group 3 PH associated with COPD |
| [NCT03267108](https://clinicaltrials.gov/study/NCT03267108) | Phase 3 | Terminated | 145 | REBUILD: dose-escalation RCT of pulsed iNO for PH associated with pulmonary fibrosis |
| [NCT02000856](https://clinicaltrials.gov/study/NCT02000856) | N/A | Completed | 15 | BEET PAH: crossover RCT of dietary nitrate (beetroot juice, NO donor pathway) in PAH |
| [NCT00527163](https://clinicaltrials.gov/study/NCT00527163) | N/A | Completed | 103 | NIH/Mali study on NO scavenging by plasma hemoglobin and hemolysis-associated PH in malaria |
| [NCT01185925](https://clinicaltrials.gov/study/NCT01185925) | Phase 2 | Completed | 32 | PDE5 inhibition (downstream of NO pathway) reverses exercise oscillatory breathing in chronic heart failure |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Overview of PAH diagnosis and treatment landscape |
| [33836637](https://pubmed.ncbi.nlm.nih.gov/33836637/) | 2021 | Review | J Cardiovasc Pharmacol Ther | Combination therapy in PAH targeting NO and prostacyclin pathways |
| [32442078](https://pubmed.ncbi.nlm.nih.gov/32442078/) | 2020 | Review | Curr Med Chem | NO pathway in PAH: pathomechanism, biomarkers, and drug targets |
| [23822809](https://pubmed.ncbi.nlm.nih.gov/23822809/) | 2013 | Review | Am J Respir Crit Care Med | NO deficiency and endothelial dysfunction as a driver of PAH pathogenesis |
| [20051913](https://pubmed.ncbi.nlm.nih.gov/20051913/) | 2010 | Review | J Hypertens | NO, oxidative stress, and inflammation in PAH |
| [40341051](https://pubmed.ncbi.nlm.nih.gov/40341051/) | 2025 | Review | Eur Respir J | Drugs targeting novel pathways (including NO) in PAH |
| [38054614](https://pubmed.ncbi.nlm.nih.gov/38054614/) | 2024 | Basic/Delivery | Small | Inhalable NO-releasing microsphere delivery systems for PAH treatment |
| [33773120](https://pubmed.ncbi.nlm.nih.gov/33773120/) | 2021 | RCT | Lancet Respir Med | REPLACE trial: switching to riociguat (NO-pathway) vs. PDE5i maintenance in PAH |
| [15194181](https://pubmed.ncbi.nlm.nih.gov/15194181/) | 2004 | Review | J Am Coll Cardiol | NO pathway and phosphodiesterase inhibitors in PAH |
| [39580019](https://pubmed.ncbi.nlm.nih.gov/39580019/) | 2025 | Meta-analysis | Nitric Oxide | NOS3 gene polymorphism and PAH risk — systematic review and meta-analysis |

## Malaysia Market Information

The evidence pack confirms the product is registered and marketed in Malaysia (`market_status: 已上市`, 1 license on file), but the license record itself contains no populated fields (license number, product name, dosage form, manufacturer, and approved indication text are all blank). No usable registration detail can be reported at this time — this should be pulled directly from the NPRA registry before the report is finalized.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and DDI data are not available in the current data pull — notably, the label warnings/contraindications gap (DG001) is flagged as **Blocking severity**, meaning the candidate cannot yet be advanced to a formal safety assessment stage (S1).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The PAH indication has strong (L1) mechanistic and clinical-trial support — including a completed Phase 1/2 study and a Phase 3 RCT — and reflects well-established NO-cGMP pathway pharmacology already used in related PH conditions. However, a Blocking-severity gap in TFDA/NPRA label safety data means this cannot be greenlit until basic safety information is confirmed.

**To proceed, the following is needed:**
- TFDA/NPRA product label — warnings and contraindications (Blocking gap, DG001)
- DrugBank mechanism-of-action detail (High priority gap, DG002)
- Complete Malaysia registration record (license number, product name, dosage form, approved indication text)
- Confirmation of this product's original approved indication(s), currently unrecorded
- Route-of-administration/delivery-system compatibility assessment for the inhaled formulation
- Secondary review of PAH-CHD (L2) and PAH-CTD (L3) as related research questions, and formal disposition (e.g., closure as noise) of the five L5 "Hold" predictions in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

