---
layout: default
title: Methionine
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Methionine
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

# Methionine: From Unrecorded Original Indication to Acne (Disease)

## One-Sentence Summary

Methionine is a sulfur-containing essential amino acid marketed in Malaysia across 156 registered products, though the specific original indication text was not captured in this data pack.
The TxGNN model predicts it may be effective for **Acne (Disease)**, but this is currently supported only by **0 clinical trials** and **4 publications**, none of which directly test methionine as an acne treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA/NPRA license indication text was not returned in this data pack (156 licenses on file, none populated) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 156 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, methionine is a sulfur-containing amino acid metabolized via the transsulfuration pathway into homocysteine, then cysteine and glutathione — a route relevant to cellular antioxidant capacity.

No original indication text was retrievable from this data pack, so the relationship between methionine's established use(s) and acne cannot be directly assessed here. The 156 marketed registrations suggest it is a widely available amino acid/nutritional product in Malaysia, but the specific approved indications remain unconfirmed pending license detail retrieval.

The literature identified for this candidate does **not** study methionine treatment of acne. Instead, it links an unrelated drug (isotretinoin) to elevated homocysteine in cystic acne patients, and separately documents neutrophil/chemotactic abnormalities in inflammatory skin disease. This is, at best, an indirect association between sulfur-amino-acid metabolism and skin inflammation — not direct mechanistic or clinical support for methionine as an acne therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | International Journal of Dermatology | Patients on isotretinoin (not methionine) for cystic acne showed elevated plasma homocysteine, a methionine metabolite, linking the pathway to acne therapy side effects rather than efficacy |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case Report | BMJ Case Reports | Neonate with MTHFR mutation (affecting methionine/homocysteine metabolism) presented with neonatal acne among broader encephalopathy and dysmorphic features — an incidental association, not a treatment study |
| [3859500](https://pubmed.ncbi.nlm.nih.gov/3859500/) | 1985 | Basic Research | Journal of the American Academy of Dermatology | Case study of Sweet's syndrome with cystonodular acne showed altered neutrophil chemotactic activity; no methionine intervention studied |
| [3161955](https://pubmed.ncbi.nlm.nih.gov/3161955/) | 1985 | Basic Research | Journal of Investigative Dermatology | Study of neutrophil C5a responses across inflammatory skin diseases including acne conglobata; mechanistic, not methionine-specific |

---

## Malaysia Market Information

156 products are registered as marketed in Malaysia (NPRA market status: 已上市), but individual license details (authorization number, product name, dosage form, approved indication text) were not populated in this data pack and require separate retrieval.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature located for the acne prediction does not test methionine as an intervention — it is an indirect metabolic association drawn from a different drug's side-effect profile and unrelated basic-science studies. With no clinical trials and no direct mechanistic evidence, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Original indication and full license details (product name, dosage form, approved indication text) from TFDA/NPRA
- Mechanism of action (MOA) data confirming or refuting a plausible methionine–acne pathway
- Package insert warnings/contraindications (currently a Blocking data gap per DG001)
- A study that directly tests methionine (not isotretinoin or unrelated metabolic markers) in acne patients
- Note: other TxGNN candidates in this evidence pack — nuclear senile, cortical, mature, and diabetic cataract (ranks 4, 5, 8, 10) — carry stronger mechanistic literature support (L4, "Research Question") via glutathione/oxidative-stress pathways and may warrant earlier review priority than acne
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

