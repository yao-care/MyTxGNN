---
layout: default
title: Hexetidine
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Hexetidine
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

# Hexetidine: From Topical Oral/Vaginal Antisepsis to Interventricular Septum Aneurysm

## One-Sentence Summary

Hexetidine is a topical antiseptic used on oral and vaginal mucosa, with no established systemic pharmacology. The TxGNN model's top prediction for this drug is **Interventricular Septum Aneurysm**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags no plausible biological pathway connecting a topical antimicrobial to cardiac septal pathology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical oral/vaginal mucosal antisepsis (official TFDA/NPRA indication text not populated in source data) |
| Predicted New Indication | Interventricular Septum Aneurysm |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for hexetidine is not currently available in DrugBank (data gap DG002, High severity). Based on the information present in this evidence pack, hexetidine functions as a topical antimicrobial applied to oral and vaginal mucosa, with no meaningful systemic absorption and no known cardiac pharmacological target.

The predicted new indication — interventricular septum aneurysm — is a structural cardiac abnormality. The rationale provided alongside the prediction explicitly states there is no explainable biological pathway linking a locally-acting, non-absorbed antiseptic to cardiac septal disease. This pattern is consistent across all of hexetidine's top 10 TxGNN predictions in this pack: congenital heart defects (pulmonary valve disease, Laubry-Pezzi syndrome), craniofacial/genetic syndromes (orofacial clefting, Pierre Robin syndrome, chromosome 22q/7q deletions, Jeune syndrome), and one rare metabolic disorder — none of which share a plausible pharmacological target with hexetidine's known antimicrobial mechanism.

This suggests the current top-ranked predictions are driven by knowledge-graph embedding proximity rather than a testable pharmacological hypothesis, and should be treated as exploratory model output only, not as a repurposing lead ready for evidence review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*Note: among the top 10 predictions, only rank 6 ("disorder of fucoglycosan synthesis") returned literature (2 PubMed records), but both papers concern hexetidine's already-known use as an oral antiplaque/decontamination antiseptic — they do not address the predicted rare metabolic disease and are considered a label-mapping mismatch rather than supporting evidence.*

## Malaysia Market Information

NPRA records confirm 1 active registration for hexetidine (market status: 已上市 / Marketed), but the license number, product name, dosage form, and approved indication text fields are not populated in the current data source and require retrieval from the NPRA product registry.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (interventricular septum aneurysm) has no clinical trial or literature support and no plausible mechanistic link per the evidence pack's own assessment, placing it at evidence level L5 / decision stage S0. Compounding this, safety review cannot proceed because TFDA/NPRA label warnings and contraindications are a Blocking-severity data gap (DG001).

**To proceed, the following is needed:**
- Retrieve the TFDA/NPRA package insert (warnings, contraindications) — required before any S1 safety screening (DG001, Blocking)
- Retrieve hexetidine's MOA from DrugBank (DG002)
- Complete the NPRA license record (license number, product name, dosage form, approved indication text)
- Re-evaluate lower-ranked candidates with actual clinical/literature support (e.g., rank 6) for label-mapping accuracy before considering any indication in this list further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

