---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is a classic organic nitrate vasodilator, traditionally used for angina pectoris and congestive heart failure. The TxGNN model predicts it may also be effective for **Pulmonary Hypertension**, and unlike several other TxGNN-flagged candidates for this drug (e.g., alopecia, hypotrichosis), this indication is backed by **20 published studies**, though no dedicated randomized controlled trials or registered clinical trials for this specific indication were found.

*Note: This evidence pack lists 10 TxGNN-predicted indications for ISDN. The top-ranked candidate by raw score (alopecia) has zero supporting evidence and is explicitly flagged by the model rationale as speculative ("純屬 TxGNN 嵌入相似性預測"). Pulmonary hypertension (rank 4) is the only candidate reaching L3 evidence with a substantive literature base, so this report focuses on it.*

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris / congestive heart failure (classical use; Malaysia NPRA license text not available — data gap) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (Observational studies, no RCTs specific to this indication) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack (data gap). Based on known pharmacology, isosorbide dinitrate is an organic nitrate that is metabolized to release nitric oxide (NO), causing smooth muscle relaxation and vasodilation — the same mechanism underlying its established use in angina and heart failure.

Since pulmonary vascular smooth muscle responds to the same NO/cGMP pathway, ISDN can lower mean pulmonary arterial pressure, particularly in post-capillary pulmonary hypertension (e.g., due to left heart disease). This mechanistic overlap between its cardiovascular original use and pulmonary vasculature is what likely drives the TxGNN prediction.

However, the mechanistic link comes with important caveats reflected in the evidence: ISDN's vasodilation is non-selective, and in pre-capillary pulmonary hypertension it can reduce cardiac output and systemic blood pressure, worsen ventilation/perfusion mismatch, and is subject to nitrate tolerance with chronic use. Current pulmonary arterial hypertension (PAH) treatment guidelines do not recommend non-selective nitrates as standard therapy, which is why this prediction sits at a "Research Question" stage rather than a stronger evidence tier.

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension specifically (ClinicalTrials.gov, ICTRP, and regional registries returned zero results for this drug-disease pair).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19620510](https://pubmed.ncbi.nlm.nih.gov/19620510/) | 2009 | RCT | Hypertension (Dallas) | Fixed-dose ISDN/hydralazine improved diastolic function and LV remodeling in hypertension-induced diastolic heart failure |
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | Cohort | Heart and Vessels | Bolus ISDN reduced mean pulmonary arterial pressure in PH patients with cardiopulmonary comorbidities, with caution needed for pre- vs. post-capillary overlap |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | Cohort | Acta Anaesthesiol Scand | ISDN showed pulmonary vascular effects in end-stage cardiomyopathy patients undergoing heart transplant evaluation |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Cohort | Bull Eur Physiopathol Respir | Sublingual ISDN acutely decreased pulmonary arterial pressure and cardiac output in COPD-related PH, but did not reduce pulmonary vascular resistance (unlike nitroglycerin) |
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | Cohort | Clin Pharmacol Ther | Randomized, double-blind study of oral ISDN vs. placebo in COPD patients with pulmonary hypertension |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | Cohort (rat model) | Exp Ther Med | Intratracheal ISDN improved pulmonary artery pressure and ventricular remodeling in a rat post-MI heart failure model |
| [2498122](https://pubmed.ncbi.nlm.nih.gov/2498122/) | 1989 | Animal/Preclinical | Exp Mol Pathol | Compared ISDN with prednisolone, indomethacin, and elastase in monocrotaline-induced PH rat model |
| [39398794](https://pubmed.ncbi.nlm.nih.gov/39398794/) | 2024 | Cohort (epidemiological) | Cureus | Descriptive study of PH burden and treatment strategies in hemodialysis-dependent ESRD patients |
| [29377691](https://pubmed.ncbi.nlm.nih.gov/29377691/) | 2018 | Review (medicinal chemistry) | J Med Chem | Describes a novel NO-donor hybrid molecule (using isosorbide mononitrate) designed for pulmonary vasodilation in PAH rats |
| [6861502](https://pubmed.ncbi.nlm.nih.gov/6861502/) | 1983 | Cohort (portal hypertension, not PH) | Crit Care Med | ISDN reduced portal pressure but also lowered systemic arterial pressure — illustrates the non-selective hypotensive risk relevant to PH use |

## Malaysia Market Information

Malaysia NPRA records show **3 registered licenses** for isosorbide dinitrate (market status: Marketed), but detailed license-level data — license numbers, product names, dosage forms, and approved indication text — is not available in the current evidence pack (data gap).

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug-drug interaction data for this drug are not currently available in the evidence pack — this is flagged as a **Blocking** data gap (DG001), meaning a formal safety pre-screen (S1) cannot yet be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is limited to observational/cohort and preclinical studies (L3) with no RCTs or registered clinical trials specific to pulmonary hypertension, and the mechanism carries known risks (systemic hypotension, V/Q mismatch, nitrate tolerance) that current PAH guidelines weigh against non-selective nitrate use.
- Core safety data (warnings, contraindications, DDIs) is entirely missing, which blocks the standard S1 safety pre-screen required before any advancement decision.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (resolve DG001)
- Confirmed mechanism of action data from DrugBank (resolve DG002)
- A prospective or controlled study targeting the specific PH subpopulation shown most responsive in the literature (post-capillary PH with cardiopulmonary comorbidities, per the 2025 Kashimura et al. cohort)
- Malaysia-specific license and approved-indication text to confirm current labeled use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

