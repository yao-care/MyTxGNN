---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Immunosuppression to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is a well-established immunosuppressive agent (purine antimetabolite) used to prevent organ transplant rejection and treat autoimmune conditions including inflammatory bowel disease. The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, however there are **0 clinical trials** and **0 publications** supporting this specific direction — this prediction lacks any mechanistic or clinical rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immunosuppression (specific approved indication text not available from NPRA records) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

**This prediction is not considered reasonable.** Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital developmental disorder involving ocular defects (colobomatous microphthalmia) and proximal limb bone dysplasia. The pathogenesis originates from abnormal gene regulation during embryonic development, resulting in irreversible structural defects formed before birth.

Azathioprine is a purine antimetabolite that is converted to 6-mercaptopurine in vivo, which subsequently inhibits purine synthesis and suppresses lymphocyte proliferation. This immunosuppressive mechanism targets the adaptive immune system — specifically T-cell and B-cell proliferation — and has no therapeutic relevance to congenital structural developmental defects.

The extremely high TxGNN score (99.99%) likely reflects a spurious pattern in the knowledge graph rather than a genuine pharmacological relationship. The complete absence of any clinical trial or literature evidence further confirms that this prediction does not warrant further investigation. Notably, the model also correctly identified azathioprine's well-established efficacy in inflammatory bowel disease (Rank 5, L1) and ulcerative colitis (Rank 9, L1), which are already approved indications — validating the model's ability to detect genuine drug-disease relationships while also demonstrating its tendency to generate false positives for unrelated conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered for azathioprine in colobomatous microphthalmia-rhizomelic dysplasia syndrome.

## Literature Evidence

Currently no related literature available for azathioprine in colobomatous microphthalmia-rhizomelic dysplasia syndrome.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Not available) | (Not available) | (Not available) | (Not available) |
| (Not available) | (Not available) | (Not available) | (Not available) |
| (Not available) | (Not available) | (Not available) | (Not available) |

> *Note: 3 registrations were identified in the NPRA database, but detailed product information (authorization number, product name, dosage form, approved indication) was not available at the time of data extraction.*

## Safety Considerations

Please refer to the package insert for safety information.

> *Note: Safety data including key warnings, contraindications, and drug-drug interactions were not available in the evidence pack. Given that azathioprine is a potent immunosuppressive agent with well-known risks including myelosuppression, hepatotoxicity, increased infection risk, and potential long-term malignancy risk, clinicians should consult the full prescribing information before use.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for colobomatous microphthalmia-rhizomelic dysplasia syndrome has no mechanistic basis. This is a congenital structural developmental syndrome caused by embryonic gene regulatory defects, and azathioprine's immunosuppressive mechanism has no therapeutic relevance to irreversible developmental abnormalities. The evidence level is L5 (model prediction only) with zero supporting clinical or preclinical evidence.

**To proceed, the following would be needed (though not recommended):**
- Any preclinical evidence suggesting immunomodulation plays a role in this syndrome
- Identification of an immune-mediated component in disease pathogenesis
- Case reports or observational data suggesting benefit

---

### Appendix: Notable Predictions with Existing Evidence

The TxGNN model also identified two indications for which azathioprine is **already an approved therapy**, confirming the model's capacity to detect validated drug-disease pairs:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Status |
|------|---------------------|-------------|----------------|--------|
| 5 | Inflammatory Bowel Disease | 99.52% | L1 | Already approved — not a repurposing candidate |
| 9 | Ulcerative Colitis | 99.33% | L1 | Already approved — not a repurposing candidate |

**IBD (Rank 5):** Supported by **50 clinical trials** (including multiple Phase 3 RCTs such as [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) with 508 patients and [NCT00098111](https://clinicaltrials.gov/study/NCT00098111)) and **20 publications** including reviews confirming 45+ years of clinical experience.

**Ulcerative Colitis (Rank 9):** Supported by **50 clinical trials** and **20 publications** including multiple Cochrane systematic reviews ([PMID 40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/), [PMID 27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/), [PMID 22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/)) and a meta-analysis ([PMID 19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/)).

The remaining novel predictions (Ranks 1–4, 6–8, 10) all received **Hold** recommendations due to lack of mechanistic rationale — most target congenital structural defects or primary immunodeficiencies where immunosuppression would be either irrelevant or potentially harmful (especially WHIM syndrome at Rank 4, which is a **mechanistic contraindication**).

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*

*Data cutoff: 2026-04-05 | Evidence Pack version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

