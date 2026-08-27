---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 5
---

# Imiglucerase
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase is a recombinant glucocerebrosidase enzyme-replacement therapy, historically established for Gaucher disease. The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**, but this pack finds **0 clinical trials** and only **2 tangential review articles**, and the evidence pack's own mechanistic analysis flags the prediction as a likely false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (identified from evidence-pack literature; Malaysia license/indication text not available in this data pack) |
| Predicted New Indication | Hurler syndrome (MPS I) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on the literature captured in this pack, imiglucerase is a recombinant glucocerebrosidase used in enzyme replacement therapy (ERT), substituting for the deficient enzyme in Gaucher disease, whose accumulated substrate is glucosylceramide.

Hurler syndrome (MPS I) is caused by deficiency of a *different* enzyme, alpha-L-iduronidase, which breaks down dermatan/heparan sulfate — a distinct substrate with no direct overlap with glucocerebrosidase activity. Both conditions fall under the broad "lysosomal storage disease" category and are treated with the same ERT *modality*, which is likely why the two diseases sit close together in embedding space, but there is no enzyme-specific reason to expect imiglucerase to be active in MPS I.

The evidence pack's own repurposing rationale for this candidate explicitly flags this as a probable category-clustering artifact rather than a genuine pharmacological signal, and this same substrate mismatch applies to the other LSD candidates in this pack (Scheie syndrome, cholesteryl ester storage disease). The two remaining candidates (benign adrenal neoplasm, ichthyosis syndrome) have no identifiable mechanistic link at all.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | Proceedings of the National Academy of Sciences | Overview of PET imaging for enzyme replacement therapy across LSDs (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); does not report imiglucerase efficacy data specific to Hurler syndrome |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of ERT history across lysosomal storage diseases, tracing imiglucerase (Cerezyme) development for Gaucher disease; does not address Hurler syndrome use |

Both citations are general ERT-class reviews that mention imiglucerase and Hurler syndrome in the same survey context, not studies evaluating imiglucerase as a Hurler syndrome treatment.

## Malaysia Market Information

Detailed authorization records (license number, product name, dosage form, indication text) are not populated in this data pack. Market status is confirmed as Marketed, with 1 registration on file.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/NPRA warning and contraindication data is flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety evaluation (S1) can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack's own mechanistic analysis identifies the top candidate (Hurler syndrome) as a likely artifact of lysosomal-storage-disease category clustering rather than a true enzyme-specific signal, and this pattern repeats across the other MPS/LSD candidates. No clinical trials exist for any of the five predicted indications, and literature support is limited to general ERT-class reviews rather than disease-specific evidence.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Expert pharmacology review to determine whether the TxGNN LSD-category clustering reflects a genuine signal or a modeling artifact
- If pursued, preclinical rationale specific to alpha-L-iduronidase pathway crossover before any clinical evidence generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

