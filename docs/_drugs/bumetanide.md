---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 1
---

# Bumetanide
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

# Bumetanide: From Loop-Diuretic Therapy (Edema) to Acute Pulmonary Heart Disease

## One-Sentence Summary

> Bumetanide is a potent loop diuretic historically used to manage fluid overload/edema associated with congestive heart failure, hepatic and renal disease, and acute pulmonary congestion.
> The TxGNN model predicts it may also be effective for **Acute Pulmonary Heart Disease** (acute cor pulmonale with right heart failure),
> with **3 clinical trials** and **5 publications** currently identified, though evidence quality is mixed (**Evidence Level L3**) and a critical safety data gap remains unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the current NPRA license text (fields empty); per literature (PMID 6391889), bumetanide is a loop diuretic historically used for oedema associated with congestive heart failure, hepatic/renal disease, and acute pulmonary congestion |
| Predicted New Indication | Acute Pulmonary Heart Disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal, structured mechanism-of-action record is not available for this drug in the current evidence pack (flagged as a High-severity data gap, DG002). However, the model's own repurposing rationale documents the underlying pharmacology: bumetanide is a potent loop diuretic that inhibits the NKCC2 (Na⁺-K⁺-2Cl⁻) co-transporter in the thick ascending limb of the loop of Henle, producing natriuresis and diuresis. This reduces circulating volume and cardiac preload — a mechanism directly relevant to volume-overload states.

Acute pulmonary heart disease (acute cor pulmonale) typically presents with acute right ventricular strain and systemic/pulmonary venous congestion. Since loop diuretics are already an established cornerstone of therapy for volume overload in heart failure — including the acute pulmonary congestion indication referenced in the older bumetanide literature (PMID 6391889) — extending this use to acute pulmonary heart disease is mechanistically plausible and represents an incremental extension of well-established loop-diuretic pharmacology rather than a novel mechanistic hypothesis.

That said, the trial evidence specifically testing bumetanide *in this context* is thin: the one Phase 4 trial designed to directly test bumetanide's acute hemodynamic effects in device-monitored heart-failure patients (NCT07375212) was withdrawn before enrolling any patients, and the largest related trial (NCT05580510) tests other agents (empagliflozin, sacubitril/valsartan) with bumetanide likely only as background therapy. The prediction should therefore be read as a plausible, mechanism-supported research hypothesis rather than a clinically validated new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Evaluates empagliflozin and sacubitril/valsartan in adult congenital heart disease patients with reduced-EF heart failure; bumetanide is likely only a background diuretic, not the primary intervention (Grade B relevance) |
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Designed to test whether a single 4mg intranasal bumetanide dose acutely reduces pulmonary artery pressure and blood volume in device-monitored (CardioMEMS/Cordella) heart-failure patients; high mechanistic relevance but withdrawn with zero enrollment, so no data were generated |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational study of seismocardiographic monitoring in heart failure patients; no drug intervention, only population overlap with bumetanide-treated patients (Grade C relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Clinical Study (uncontrolled, small-n) | British Journal of Clinical Pharmacology | IV bumetanide (25 µg/kg) in 24 patients with acute or chronic heart failure reduced cardiac index and pulmonary artery occluded pressure while increasing systemic arterial pressure and vascular resistance at rest |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | American Journal of Therapeutics | Reviews management of acute decompensated heart failure; most patients are effectively managed with diuretic agents as first-line therapy |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Comprehensive review of bumetanide pharmacodynamics/pharmacokinetics; confirms established use for oedema from CHF, hepatic/renal disease, and acute pulmonary congestion, with rapid onset (within 30 minutes) |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | The Annals of Pharmacotherapy | Comparative review of loop diuretics (including bumetanide) evaluating pharmacokinetics, safety, efficacy, and cost versus furosemide |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiology/Cohort | American Journal of Emergency Medicine | Describes epidemiology of heart-failure presentations to US emergency departments 2016–2023; provides background disease-burden context rather than direct drug evidence |

---

## Malaysia Market Information

NPRA records confirm **3 registered licenses** for bumetanide in Malaysia (market status: 已上市 / Marketed). However, the detailed registry fields — license number, product name, dosage form, manufacturer, and approved indication text — have not yet been extracted into this evidence pack and are currently blank for all 3 entries. This is a known data gap; sourcing the full NPRA product register entries is recommended before finalizing any regulatory-facing summary.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are all currently unavailable — this is tracked as a Blocking-severity data gap (DG001), since it prevents completion of the initial safety screening stage (S1). This must be resolved before any further clinical decision-making.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Blocking-severity data gap in TFDA/NPRA label warnings and contraindications (DG001) prevents completion of the mandatory initial safety screening (S1), and the clinical/literature evidence, while mechanistically coherent (L3 — driven mainly by older reviews and a small uncontrolled study), does not yet include a completed, dedicated trial confirming efficacy specifically for acute pulmonary heart disease; the one trial designed to test this directly (NCT07375212) was withdrawn before enrolling patients.

**To proceed, the following is needed:**
- Official NPRA/product insert data: key warnings, contraindications, and drug-drug interaction profile (resolves DG001, Blocking)
- Confirmed mechanism-of-action reference from DrugBank or equivalent authoritative source (resolves DG002, High)
- Complete NPRA license details (license numbers, product names, approved indication text) for the 3 existing registrations
- A dedicated, adequately powered clinical trial or registry study evaluating bumetanide specifically in acute pulmonary heart disease / acute cor pulmonale populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

