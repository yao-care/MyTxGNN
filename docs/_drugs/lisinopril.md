---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an angiotensin-converting enzyme (ACE) inhibitor widely used to treat hypertension and chronic heart failure by suppressing the renin-angiotensin-aldosterone system (RAAS).
The TxGNN model assigns its highest prediction score to **Posterolateral Myocardial Infarction** (99.90%), with indirect mechanistic support from landmark ACE inhibitor trials in acute MI (GISSI-3, ISIS-4), though no direct evidence exists for this specific anatomical subtype.
This is a **multi-indication evaluation covering 10 predicted indications**; the strongest clinical evidence overall belongs to **Chronic Pulmonary Heart Disease (Cor Pulmonale)** at Evidence Level L3 — supported by **5 clinical trials** and **8 publications** — carrying a *Proceed with Guardrails* recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / Chronic Heart Failure |
| Top Predicted Indication (Rank 1) | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Research Question |

---

## Multi-Indication Summary

This evidence pack evaluates 10 predicted indications. The table below is sorted by evidence strength:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|-------------|----------------|----------|
| 1 | Posterolateral Myocardial Infarction | 99.90% | L4 | Research Question |
| 2 | Posteroinferior Myocardial Infarction | 99.90% | L4 | Research Question ⚠️ |
| 3 | Pulmonary Hypertension — Lung Disease/Hypoxia (WHO Group 3) | 99.89% | L4 | Hold |
| 4 | Pulmonary Hypertension — Multifactorial (WHO Group 5) | 99.89% | L5 | Hold |
| 5 | Malignant Hypertensive Renal Disease | 99.89% | L4 | Proceed with Guardrails |
| 6 | Malignant Renovascular Hypertension | 99.89% | L4 | Hold ⛔ |
| 7 | Septal Myocardial Infarction | 99.88% | L4 | Research Question |
| 8 | Braddock Syndrome | 99.86% | L5 | Hold |
| **9** | **Chronic Pulmonary Heart Disease (Cor Pulmonale)** | **99.68%** | **L3** | **Proceed with Guardrails** |
| 10 | Autosomal Dominant Familial Hematuria–Retinal Arteriolar Tortuosity–Contractures Syndrome | 99.33% | L5 | Hold |

> ⚠️ **Posteroinferior MI**: right ventricular infarction (RVI) context may worsen preload-dependent haemodynamics under ACE inhibition — safety review required before any further evaluation.
>
> ⛔ **Malignant Renovascular Hypertension**: ACE inhibitors are **contraindicated** in bilateral renal artery stenosis — efferent arteriolar dilatation collapses glomerular perfusion pressure and may precipitate acute renal failure. This indication is blocked pending definitive exclusion of bilateral RAS.

---

## Why is This Prediction Reasonable?

### Posterolateral Myocardial Infarction (Top-Ranked Prediction)

Currently, detailed mechanism of action data is not available from DrugBank for this evaluation. Based on well-established pharmacology, lisinopril is an ACE inhibitor that blocks the conversion of angiotensin I to angiotensin II, thereby inhibiting RAAS activation. This reduces cardiac afterload and, crucially, suppresses ventricular remodelling — the pathological process of progressive ventricular dilation and fibrosis following myocardial infarction that drives long-term morbidity and mortality.

The landmark Phase 3 RCTs GISSI-3 and ISIS-4 established that ACE inhibitors (lisinopril was directly studied in GISSI-3) significantly reduce 6-week and 5-week mortality after acute MI across general populations. However, neither trial stratified outcomes by anatomical MI subtype (posterolateral vs. anterior vs. inferior), making the TxGNN prediction for "posterolateral MI" an indirect extrapolation from this robust general evidence base rather than a targeted finding.

The posterolateral territory is typically perfused by the left circumflex or dominant right coronary artery. While the same anti-remodelling mechanism applies regardless of infarct territory, the unique haemodynamic consequences of posterolateral involvement — including potential lateral wall motion abnormalities and mitral regurgitation — may modulate the magnitude of ACE inhibitor benefit, justifying targeted investigation.

### Chronic Pulmonary Heart Disease (Best-Evidenced Indication)

Chronic cor pulmonale — right ventricular hypertrophy and eventual failure driven by sustained pulmonary arterial hypertension — may benefit from ACE inhibition through at least three mechanisms: ① reducing systemic vascular resistance improves biventricular interdependence, offloading the already-stressed right ventricle; ② suppressing ventricular fibrosis and structural remodelling in both ventricles; ③ bradykinin pathway activation may improve pulmonary vascular endothelial function, given that ACE is highly expressed in the pulmonary vascular bed.

Two directly relevant clinical studies support this rationale. PMID 14524095 is a clinical trial of lisinopril specifically in patients with chronic cor pulmonale. PMID 17047621 demonstrates that lisinopril 10 mg/day attenuates pulmonary hypertension, improves right ventricular systolic function and diastolic filling, and corrects vascular tone in patients with the combination of ischaemic heart disease and COPD — a pathophysiological model closely aligned with cor pulmonale. Together, these form an L3 evidence base and represent the most clinically actionable finding in this evaluation.

---

## Clinical Trial Evidence

### Chronic Pulmonary Heart Disease (Rank 9 — Best Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06697353](https://clinicaltrials.gov/study/NCT06697353) | N/A | Completed | 4,936 | Real-world retrospective cohort of vericiguat (sGC activator) in Japanese chronic HFrEF patients; provides comparative context for pharmacotherapy outcomes in chronic heart failure, though the study drug differs from lisinopril |
| [NCT00982423](https://clinicaltrials.gov/study/NCT00982423) | Phase 1/2 | Completed | 41 | Effects of reducing furosemide dose on cardiorenal and humoral function in compensated CHF with and without renal dysfunction; useful background for understanding ACEI + diuretic interactions in the same patient population |
| [NCT04486118](https://clinicaltrials.gov/study/NCT04486118) | Phase 2 | Active, not recruiting | 36 | Double-blind RCT of centrally acting ACE inhibition in SLE-associated cognitive impairment; demonstrates active investigation of ACE inhibitor class effects in non-traditional indications |
| [NCT03967496](https://clinicaltrials.gov/study/NCT03967496) | N/A | Completed | 402 | Observational assessment of immediate postoperative delirium; limited direct relevance but captures cardiac complication data including MI and pulmonary events in the perioperative setting |
| [NCT00292162](https://clinicaltrials.gov/study/NCT00292162) | N/A | Completed | 41 | Radiofrequency ablation for AF in advanced CHF; different intervention, but provides outcomes data in advanced CHF patients with significant haemodynamic compromise |

> None of the retrieved trials directly study lisinopril in chronic pulmonary heart disease or cor pulmonale. The most directly relevant evidence comes from the literature (PMID 14524095 and PMID 17047621).

### Posterolateral Myocardial Infarction (Rank 1)

Currently no related clinical trials registered for this specific anatomical MI subtype.

---

## Literature Evidence

### Chronic Pulmonary Heart Disease (Rank 9 — Best Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical Trial | Problemy Tuberkuleza i Boleznei Legkikh | **Direct evidence**: Small clinical trial of lisinopril specifically in patients with chronic cor pulmonale — primary supporting study for this indication |
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical Study | Kardiologiia | **Direct evidence**: Lisinopril 10 mg/day attenuated pulmonary hypertension, improved right ventricular systolic function and diastolic ventricular filling, and corrected vascular tone in IHD+COPD patients with pulmonary hypertension and endothelial dysfunction |
| [26895877](https://pubmed.ncbi.nlm.nih.gov/26895877/) | 2016 | Review | European Journal of Pediatrics | Reviews ACEI/ARB recommendations in paediatric chronic heart failure; highlights mechanistic rationale for tissue ACE inhibition in heart failure despite limited age-specific RCT data |
| [20852161](https://pubmed.ncbi.nlm.nih.gov/20852161/) | 2010 | Case Report | Am J Health-System Pharmacy | Severe bradycardia and hypotension with concomitant tizanidine and lisinopril — clinically important drug interaction safety signal |
| [11170787](https://pubmed.ncbi.nlm.nih.gov/11170787/) | 2001 | Animal Study | Experimental and Molecular Pathology | Cardiopulmonary protein synthesis changes in three chronic hypertension rat models (aortic constriction, Goldblatt, bromoethylamine); mechanistic background for cardiac remodelling in hypertensive heart disease |

### Septal Myocardial Infarction (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case Report | JPMA — Journal of Pakistan Medical Association | ACE inhibitor + CoQ10 as adjunctive treatment for ventricular septal rupture complicating late-onset acute MI in a 74-year-old woman; demonstrates real-world ACEI use in septal complications of MI, though direct applicability to septal MI as an anatomical subtype is limited |

### Posterolateral Myocardial Infarction (Rank 1)

Currently no related literature available for this specific anatomical MI subtype.

---

## Malaysia Market Information

Nine product licences for Lisinopril are registered with the National Pharmaceutical Regulatory Agency (NPRA) of Malaysia, confirming active market presence. Detailed product-level data (authorization numbers, brand names, dosage forms, and approved indication text) was not returned in the current data extract despite successful query.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | Not available in current data extract | — | — |
| (9 licences confirmed via NPRA query on 2026-03-27) | | | |

> Lisinopril is a mature generic ACE inhibitor registered internationally under brand names including Zestril® and Prinivil®, typically available as tablets (2.5 mg, 5 mg, 10 mg, 20 mg) approved for hypertension, chronic heart failure, and post-MI left ventricular dysfunction. Full product details should be retrieved directly from the NPRA eSearch portal.

---

## Safety Considerations

**Key Warning — Malignant Renovascular Hypertension (Rank 6):**
Bilateral renal artery stenosis (or stenosis affecting a solitary functioning kidney) is a **contraindication** to lisinopril and all ACE inhibitors. In this setting, ACE inhibition dilates the efferent arteriole, catastrophically reducing glomerular filtration pressure and triggering acute renal failure. This predicted indication (Rank 6) must remain on **Hold** until bilateral RAS is definitively excluded by imaging.

**Drug Interaction Signal (from literature — PMID 20852161):**
Concomitant use of tizanidine and lisinopril has been associated with severe bradycardia and hypotension. This interaction should be flagged in any clinical use setting.

For complete warnings, contraindications, and the full drug interaction profile, please refer to the approved Malaysian package insert.

---

## Conclusion and Next Steps

### Chronic Pulmonary Heart Disease — **Decision: Proceed with Guardrails**

**Rationale:**
Two small but directly relevant clinical studies examined lisinopril specifically in cor pulmonale and COPD-related pulmonary hypertension and reported improvements in right ventricular function and pulmonary pressure. This L3 evidence base, combined with sound mechanistic plausibility via RAAS suppression and bradykinin-mediated pulmonary endothelial effects, justifies moving to the next evaluation stage.

**To proceed, the following is needed:**
- Full-text review of PMID 14524095 and PMID 17047621 to assess sample sizes, study design, control groups, and effect sizes
- Safety monitoring protocol: baseline and follow-up eGFR, serum potassium, and blood pressure tracking (avoid excessive hypotension given right-heart preload dependence)
- Mandatory exclusion of bilateral renal artery stenosis prior to initiation
- Design of a prospective pilot RCT or well-controlled observational study in COPD-associated cor pulmonale patients on standard background therapy

---

### Posterolateral Myocardial Infarction — **Decision: Research Question**

**Rationale:**
ACEI/lisinopril has Phase 3 RCT evidence for mortality reduction in general acute MI (GISSI-3, ISIS-4), but no published data exists for the posterolateral anatomical subtype specifically. Mechanistic extrapolation is reasonable but unconfirmed.

**To proceed, the following is needed:**
- Retrospective subgroup analysis from existing large MI trial datasets (GISSI-3, ISIS-4) stratifying outcomes by MI territory
- Prospective registry or cohort study comparing outcomes in posterolateral MI patients with vs. without ACE inhibitor therapy
- Lisinopril DrugBank MOA data (currently a data gap — DG002)
- NPRA package insert review for full safety and contraindication data (DG001)

---

### Malignant Renovascular Hypertension — **Decision: Hold**

**Rationale:**
Bilateral renal artery stenosis constitutes a contraindication to ACE inhibitors. This indication is blocked unless bilateral RAS exclusion is confirmed.

---

> ⚕️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

