---
layout: default
title: Phenol
parent: 僅模型預測 (L5)
nav_order: 542
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Phenol: From Topical Keratolytic/Antiseptic Use to Acne Keloid

## One-Sentence Summary

Phenol (DrugBank DB03255) is a well-established topical caustic/keratolytic agent long used in dermatology for chemical peeling and keratotic lesion treatment; formal NPRA-registered indication text was not retrievable for this evaluation. Of 8 TxGNN-predicted new indications reviewed, only **Acne Keloid** is supported by actual literature evidence (4 publications), while the other 7 candidates (including the top-ranked TxGNN score) have no corroborating trials or literature and remain at Hold status. This report focuses on the Acne Keloid candidate as the only evidence-backed direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from NPRA license records (all 5 sampled license entries have blank indication text; drug's original_indications field is empty). Based on general pharmacological knowledge, phenol is used as a topical caustic/keratolytic agent (e.g., chemical peeling, keratotic lesion ablation). |
| Predicted New Indication | Acne Keloid |
| TxGNN Prediction Score | 99.94% (rank 1255 of predictions) |
| Evidence Level | L3 (literature-only; no registered clinical trials) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 30 |
| Recommended Decision | Proceed with Guardrails |

**Note on other candidates:** 7 of the 8 TxGNN-predicted indications for phenol (acrodermatitis chronica atrophicans, secondary childhood interstitial lung disease, neonatal dermatomyositis, amyopathic dermatomyositis, hydroa vacciniforme familial, severe nonproliferative diabetic retinopathy, dry eye syndrome) have no phenol-specific supporting evidence — the trials/literature retrieved for those queries concern unrelated drugs (hydroxychloroquine, fenofibrate, aspirin, antimuscarinics, etc.). All are scored L4–L5 with a Hold recommendation and are not discussed further here.

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for phenol is not available in this evidence pack (DG002, High severity data gap). However, phenol's action as a protein coagulant is well documented in the dermatologic literature captured here: at controlled concentrations it denatures/coagulates surface keratin and dermal protein in a depth-dependent manner, which is the basis of its established clinical use in chemical peeling ("phenol peel").

Acne keloid (keloidal scarring secondary to acne, including keloidal folliculitis) involves excess/abnormal collagen deposition and post-inflammatory hyperpigmentation following inflammatory acne lesions. Chemical peeling with phenol is already used clinically to resurface acne-scarred skin, promote controlled protein coagulation, and stimulate collagen remodeling — a mechanism directly relevant to keloidal/scarring acne sequelae rather than a purely speculative TxGNN association.

This gives the Acne Keloid candidate a genuine mechanistic rationale, distinguishing it from the other 7 predicted indications, none of which have any plausible mechanistic or evidentiary link to phenol's known pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) | 2007 | Case series | The Journal of Dermatology | Modified phenol peel (Exoderm) evaluated in Asian patients for facial wrinkles, acne scars and related skin problems; modification aimed to reduce classic phenol-peel side effects (hypopigmentation, hypertrophic scarring, keloid) while retaining efficacy. |
| [16164153](https://pubmed.ncbi.nlm.nih.gov/16164153/) | 2005 | Review | Cutis | Reviews acne treatment considerations in ethnic/darker skin, noting increased risk of post-inflammatory hyperpigmentation and keloid scarring following acne lesions; discusses topical retinoid/hydroquinone as PIH standard and keloid management approaches. |
| [866280](https://pubmed.ncbi.nlm.nih.gov/866280/) | 1977 | Review | Postgraduate Medicine | General review of dermatoses more common in Black patients, including pigmentary abnormalities and keloidal folliculitis associated with inflammatory skin disease and hair-related conditions. |
| [4278481](https://pubmed.ncbi.nlm.nih.gov/4278481/) | 1974 | Case series | Fortschritte der Medizin | Case series on scalp disease treatment using "Crino-Kaban" preparation; abstract text not available in source data. |

---

## Malaysia Market Information

NPRA records show phenol is marketed under **30 total registrations**, but the license-level detail fields (authorization number, product name, dosage form, approved indication text) were not populated in this evidence pack for any of the 5 sampled entries — full label/registration data needs to be pulled directly from NPRA before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not retrievable in this evidence pack — DG001 flags this as a Blocking gap for safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acne Keloid is the only one of 8 TxGNN-predicted indications with a genuine mechanistic basis (phenol's established use in chemical peeling for acne scarring) and supporting literature, though evidence is limited to case series/reviews with no controlled trials — insufficient for a full Go, but too plausible to Hold outright.

**To proceed, the following is needed:**
- NPRA package insert / label data (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Formal mechanism-of-action documentation from DrugBank or manufacturer data (DG002)
- Complete license-level registration details (product names, dosage forms, approved indication text) for the 30 Malaysia registrations
- Prospective or comparative clinical data specifically evaluating phenol peel for acne-related keloidal scarring, since current evidence is limited to case series and general reviews
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

