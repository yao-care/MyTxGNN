---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

> Captopril is an ACE inhibitor originally used to treat hypertension (the specific NPRA-approved indication text is not available in the current registry extract). The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, a use already implicit in captopril's core RAAS-blocking mechanism, with **0 clinical trials** and **20 publications** currently identified, none of which are randomized controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor class; specific NPRA-approved indication text not available — see Data Gaps) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, captopril is an ACE (angiotensin-converting enzyme) inhibitor; its efficacy in hypertension is well established, and mechanistically it is directly applicable to malignant renovascular hypertension.

Captopril blocks the renin-angiotensin-aldosterone system (RAAS) activation that drives renovascular hypertension caused by renal artery stenosis or renin-secreting tumors. This is not a novel mechanism but rather captopril's core pharmacological action — in fact, "captopril renography" is itself a standard diagnostic tool that exploits this exact mechanism to identify renovascular hypertension, which indicates the pharmacological basis for this use is already clinically established rather than purely theoretical.

Because malignant renovascular hypertension is mechanistically a more severe subset of the hypertension captopril is already indicated for, the TxGNN prediction is consistent with decades of clinical use of ACE inhibitors in renin-mediated hypertensive states, though most supporting evidence here is diagnostic/observational rather than treatment-outcome RCT data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Clinical concepts review of renovascular hypertension; discusses treatment strategies directed at the renin-angiotensin mechanism. |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | The Journal of Pediatrics | Review of malignant hypertension. |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Cohort (animal) | Japanese Heart Journal | Characterizes neurohormonal (renin/angiotensin/catecholamine) changes in benign vs. malignant phases of Goldblatt renovascular hypertension. |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Cohort/Clinical observation | Biulleten' Vsesoiuznogo Kardiologicheskogo Nauchnogo Tsentra AMN SSSR | Use of captopril in stable and malignant-course arterial hypertension. |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical study | Clinical Science | Captopril-induced rise in plasma renin activity (>14 ng/h/ml) reliably identified untreated renovascular hypertension in 43/44 patients. |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Case Report | Klinische Wochenschrift | Severe renovascular hypertension (neurofibromatosis, bilateral renal artery stenosis) treated with captopril after patient refused surgery. |
| [1436350](https://pubmed.ncbi.nlm.nih.gov/1436350/) | 1992 | Case Report | Nephron | Captopril administration enhanced renin secretion while improving blood pressure in a patient with severe secondary hypertension. |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report/Review | Clinical Nephrology | Two cases of neurofibromatosis-associated renovascular hypertension; captopril used both diagnostically and therapeutically. |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Case Report/Review | Endocrinology and Metabolism Clinics of North America | Renin-secreting tumors; blood pressure drops during converting-enzyme (captopril) treatment. |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | Captopril renal scintigraphy case illustrating diagnostic use and limitations in malignant hypertension. |

---

## Malaysia Market Information

NPRA registry data confirms **6 registered licenses** for captopril with market status "Marketed," but the current extract does not include license numbers, product names, dosage forms, or approved indication text for any of the individual registrations (all fields returned blank). This is a data gap requiring direct NPRA lookup before market-level details can be reported.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available in the evidence pack (NPRA label not yet retrieved/parsed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and clinically self-evident (captopril's RAAS-blocking action is the same mechanism exploited diagnostically via captopril renography for renovascular hypertension), but supporting literature is limited to case reports, small cohorts, and diagnostic studies rather than treatment RCTs, and no clinical trials are currently registered for this specific indication — consistent with the assigned L3 evidence level and S2 decision stage.

**To proceed, the following is needed:**
- NPRA product label (仿单) with warnings/contraindications — **Blocking**, required before any safety (S1) assessment can begin
- DrugBank mechanism-of-action data — **High priority**, needed to confirm and formalize the mechanistic rationale
- Complete NPRA license-level details (product names, dosage forms, approved indication text) for the 6 marketed registrations
- Confirmation of original approved indication text, since none of the current license records populated this field
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

