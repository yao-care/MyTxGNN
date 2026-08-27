---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a topical vitamin D3 analogue clinically established for the treatment of plaque psoriasis. The TxGNN model predicts it may also be effective for **Seborrheic Keratosis**, a hypothesis currently supported by **6 published studies** (no registered clinical trials yet) describing consistent clinical response and a plausible pro-apoptotic mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis (plaque psoriasis) — based on established pharmacology; not specified in the available NPRA registration text |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for calcipotriol is not available in the source dataset. Based on well-established pharmacological knowledge, calcipotriol is a synthetic vitamin D3 (calcitriol) analogue and a vitamin D receptor (VDR) agonist. Its proven efficacy in psoriasis comes from suppressing excessive keratinocyte proliferation while promoting keratinocyte differentiation and normal turnover.

Seborrheic keratosis (SK) is pathologically characterized by the same core process — benign but excessive accumulation of proliferating keratinocytes. This shared cellular target is the mechanistic bridge between the two indications: a drug that normalizes keratinocyte proliferation/differentiation in psoriatic plaques could plausibly do the same in SK lesions.

This is not purely theoretical. PMID 16043912 directly demonstrates that topical vitamin D3 analogues (including calcipotriol) induce **apoptosis** in SK ("senile wart") lesions, providing a specific mechanistic explanation rather than a generic extrapolation. Multiple independent case series, including a comparative study against standard cryosurgery (PMID 15090020), report consistent clinical regression with topical calcipotriol, which raises confidence in the TxGNN prediction beyond the score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative Clinical Trial (vs cryosurgery) | International Journal of Dermatology | Compared standard cryosurgery with topical calcipotriene, tazarotene, and imiquimod for seborrheic keratosis. |
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Prospective Clinical Study (case series, n=12) | The Australasian Journal of Dermatology | 12 patients with facial flat SK treated with 0.005% calcipotriol ointment for 3–8 months achieved complete lesion regression, with remission lasting 6–10 years. |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Clinical Study (mechanism: apoptosis) | The Journal of Dermatology | 116 senile warts (SK) treated with topical vitamin D3 (tacalcitol, calcipotriol, or maxacalcitol) for 3–12 months; 30.2% showed response, with apoptosis proposed as the mechanism. |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Clinical Study / Review | Clinical Calcium | Japanese-language update on topical vitamin D3 ointments (tacalcitol, calcipotriol, maxacalcitol) for treatment of senile warts (SK). |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Case Report | The Journal of Dermatology | A 35-year-old woman with keratosis lichenoides chronica (a seborrheic-dermatitis-like, therapy-resistant condition) showed marked response to calcipotriol ointment. |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Case Report / Clinical Vignette | JAAPA | Clinical vignette describing seborrheic keratosis as the diagnosis for a spotted, itchy shin rash (diagnostic teaching case, not a treatment study). |

---

## Malaysia Market Information

Calcipotriol is currently marketed in Malaysia with **6 active NPRA registrations** (Market Status: ✓ Marketed). Detailed product-level records (license numbers, brand names, dosage forms, and approved indication text) are not available in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The seborrheic keratosis prediction is backed by a specific, mechanistically-supported literature base (L3 — observational studies, including one comparative trial and a mechanism study demonstrating apoptosis induction), which is stronger than a pure model-score-only prediction. However, no registered clinical trials exist yet, and a **blocking data gap** in the drug's Malaysian label (warnings/contraindications) currently prevents completion of the mandatory S1 safety assessment.

**To proceed, the following is needed:**
- Resolve the blocking data gap: retrieve and parse the NPRA/TFDA package insert for calcipotriol to obtain warnings and contraindications (required before S1 safety sign-off)
- Obtain formal mechanism of action (MOA) documentation from DrugBank to complete the mechanistic-linkage review
- Complete license-level detail (product names, dosage forms, approved indication text) for the 6 existing Malaysia registrations
- Consider a small prospective/comparative trial in SK to move evidence from L3 toward L2, given no controlled trials currently exist
- Note: lower-ranked predicted indications (e.g., vulvitis, vulvar neoplasm) show mechanistically plausible but preliminary (L4) evidence and are not yet ready for advancement; several others (e.g., vulvovaginitis, bone Paget disease, breast fibrocystic disease) remain at L5/Hold with no supporting literature or trials, and one entry (bone Paget disease) may reflect a disease-entity mapping error that should be corrected before further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

