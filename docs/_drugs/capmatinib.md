---
layout: default
title: Capmatinib
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 2
---

# Capmatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Capmatinib: From NSCLC (MET Exon 14 Skipping) to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib is a selective MET (c-Met/HGF receptor) tyrosine kinase inhibitor originally approved for non-small cell lung cancer (NSCLC) harboring MET exon 14 skipping mutations.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this direction is currently supported only by **0 clinical trials** and **1 indirectly related publication** (a general kinase-inhibitor review, not RA-specific).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NSCLC with MET exon 14 skipping mutation (derived from mechanism description; TFDA/NPRA license indication text not available in current data pull) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for capmatinib is currently a data gap (DG002). Based on the available mechanistic description, capmatinib is a selective MET (c-Met/HGF receptor) tyrosine kinase inhibitor, approved for NSCLC driven by MET exon 14 skipping mutations.

The c-Met/HGF signaling pathway has been discussed in preclinical literature as playing a potential role in rheumatoid arthritis synovial fibroblast proliferation and pannus (invasive synovial tissue) formation. This offers a theoretical, mechanism-level rationale for exploring MET inhibition in RA.

However, this link is a class-level inference — it applies broadly to kinase inhibitors with MET activity rather than being derived from capmatinib-specific data. No clinical trials, case reports, or capmatinib-specific preclinical studies in RA currently exist to support this prediction; it originates from the TxGNN model score alone.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | General review of FDA-approved protein kinase inhibitors (2021 update); mentions capmatinib within the broader kinase-inhibitor class but does not address rheumatoid arthritis specifically |

## Malaysia Market Information

NPRA records show **2 registered licenses** for capmatinib (market status: Marketed), but license number, product name, dosage form, and approved indication text are not available in the current data pull.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective MET/c-Met tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, Stage S0) with no capmatinib-specific clinical, case-report, or preclinical evidence for rheumatoid arthritis — only a class-level mechanistic hypothesis. A blocking data gap (DG001: TFDA/NPRA label warnings and contraindications) also prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications) to clear the S1 safety gate (DG001, blocking)
- Confirmed DrugBank mechanism-of-action record for capmatinib (DG002)
- Capmatinib-specific preclinical or case-level evidence linking MET inhibition to RA disease activity
- Complete license/product details (name, dosage form, indication text) for the 2 Malaysia registrations

*Note: A second candidate, brachydactyly-syndactyly syndrome (TxGNN score 99.03%), was also screened for capmatinib but excluded from this report — no known biological mechanism connects MET inhibition to this congenital limb malformation syndrome, and no supporting trials or literature exist.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

