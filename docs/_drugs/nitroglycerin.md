---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 505
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Nitroglycerin is a nitrate vasodilator classically used for angina pectoris and hypertensive emergencies (regulatory indication text was not returned in this data pull). The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with **13 clinical trials** and **20 publications** currently supporting this direction, though none are completed pivotal Phase 3 trials specific to this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from this NPRA data pull (license indication text empty); classically indicated for angina pectoris / hypertensive emergencies |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this candidate in the current data pull. Based on the supporting literature itself (Divakaran & Loscalzo, *JACC* 2017, PMID 29096811), nitroglycerin is an organic nitrate that is enzymatically converted to nitric oxide (NO), which activates guanylate cyclase, raises intracellular cGMP, and relaxes vascular smooth muscle. This is the same mechanism underlying its established use in angina and acute pulmonary edema.

Because pulmonary vascular smooth muscle responds to the same NO–cGMP pathway as systemic and coronary vasculature, the mechanistic extension from angina/vasospasm control to pulmonary vasodilation is pharmacologically plausible. This is reinforced by decades of small clinical studies using inhaled/nebulized or IV nitroglycerin to acutely lower pulmonary artery pressure across multiple pulmonary hypertension etiologies — congenital heart disease, persistent pulmonary hypertension of the newborn (PPHN), post-cardiac-surgery pulmonary hypertension, and COPD-related pulmonary hypertension.

Nitroglycerin's known short duration of action, tolerance development, and need for continuous/nebulized dosing (rather than oral formulation for pulmonary hypertension) are practical considerations that mechanistic plausibility alone does not resolve, and would need to be addressed before any Malaysia-specific development plan.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | NA | Completed | 80 | Nebulized nitroglycerin as adjuvant therapy improved echocardiographic and clinical parameters in persistent pulmonary hypertension of the newborn (PPHN) |
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | NA | Completed | 20 | Nebulized nitroglycerin evaluated as a vaso-reactivity testing agent in pulmonary arterial hypertension |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Compared nebulized PGI2 (epoprostenol) vs. nebulized nitroglycerin for managing pulmonary hypertension after valve replacement surgery |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | High- vs. low-dose IV nitroglycerin in sympathetic crashing acute pulmonary edema (SCAPE) |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | Nitroglycerin vs. furosemide guided by lung ultrasound in acute heart failure |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Acute effect of nitroglycerin infusion on cyclosporine-induced hypertension after cardiac transplantation |
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | IV L-citrulline (NO-pathway precursor) vs. placebo in children undergoing cardiopulmonary bypass, relevant to pulmonary pressure control |
| [NCT05373108](https://clinicaltrials.gov/study/NCT05373108) | Phase 4 | Completed | 19 | Endothelin-1 and vasomotor function assessment in cardiac allograft vasculopathy — mechanistically relevant to pulmonary/coronary vasomotor regulation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | European Journal of Pediatrics | Nebulized nitroglycerin improved echocardiographic/clinical parameters vs. control in 80 newborns with PPHN |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT | Journal of Cardiothoracic and Vascular Anesthesia | Compared dobutamine + nitroglycerin vs. milrinone for perioperative pulmonary hypertension management in mitral valve surgery |
| [39549131](https://pubmed.ncbi.nlm.nih.gov/39549131/) | 2024 | Systematic Review/NMA | Clinical Drug Investigation | Network meta-analysis comparing pulmonary vasodilator therapies (including nitroglycerin) for perioperative pulmonary hypertension in mitral valve replacement surgery |
| [29096811](https://pubmed.ncbi.nlm.nih.gov/29096811/) | 2017 | Review | Journal of the American College of Cardiology | Comprehensive review of nitroglycerin's NO-donor mechanism and cardiovascular therapeutic roles |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Review | Cardiology in the Young | Review of nitroglycerin inhalation for acute pulmonary arterial hypertension in children with congenital heart disease |
| [16429888](https://pubmed.ncbi.nlm.nih.gov/16429888/) | 2005 | Review | Texas Heart Institute Journal | Review of pharmacologic management of systemic and pulmonary hypertension in cardiac surgery patients |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Clinical Study | Annals of Internal Medicine | Nitroglycerin increased cardiac index 40%, decreased pulmonary vascular resistance 40%, and reduced mean pulmonary artery pressure in 9 patients with chronic pulmonary hypertension |
| [14508317](https://pubmed.ncbi.nlm.nih.gov/14508317/) | 2003 | Clinical Study | Anesthesiology | Nitroglycerin inhalation improved postoperative hemodynamics in pulmonary hypertension patients undergoing mitral valve replacement |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical Study | Bulletin Européen de Physiopathologie Respiratoire | Sublingual nitroglycerin/isosorbide dinitrate reduced pulmonary arterial pressure and vascular resistance in COPD-related pulmonary hypertension |
| [31250045](https://pubmed.ncbi.nlm.nih.gov/31250045/) | 2019 | Clinical Study | European Journal of Clinical Pharmacology | ALDH2 polymorphism influenced the vasodilatory response to nitroglycerin in infants with congenital heart disease and pulmonary arterial hypertension |

---

## Malaysia Market Information

NPRA confirms 3 active registrations under marketed status for nitroglycerin, but license-level details (authorization number, product name, dosage form, approved indication text) were not returned in this data pull and require direct retrieval from the NPRA product registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A substantial and mechanistically coherent body of small clinical studies, one RCT, and a network meta-analysis support nitroglycerin's acute pulmonary-vasodilatory effect across several pulmonary hypertension etiologies (PPHN, post-cardiac-surgery, COPD-related), but no completed pivotal Phase 3 RCT exists for a formal pulmonary hypertension indication, and safety/regulatory data for the Malaysia-registered products is currently missing.

**To proceed, the following is needed:**
- NPRA product label / prescribing information (key warnings, contraindications, drug interactions) — currently blocking (DG001)
- Confirmed mechanism-of-action reference from DrugBank or the product label (DG002)
- Full license-level product data for the 3 Malaysia registrations (brand names, dosage forms, approved indication text)
- A focused Phase 2/3 trial or updated systematic review targeting a specific pulmonary hypertension subtype (e.g., PPHN or post-cardiac-surgery pulmonary hypertension) to consolidate the existing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

