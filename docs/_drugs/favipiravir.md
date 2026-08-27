---
layout: default
title: Favipiravir
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 3
---

# Favipiravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Favipiravir: From Antiviral Therapy to Hemophagocytic Syndrome Associated with an Infection

## One-Sentence Summary

Favipiravir is a broad-spectrum antiviral (RNA-dependent RNA polymerase inhibitor); its originally approved indication is not recorded in the available Malaysia registry extract.
The TxGNN model predicts it may be effective for **Hemophagocytic Syndrome Associated with an Infection**,
currently supported only by **2 review-type publications** and **no clinical trials**, indicating an early-stage mechanistic hypothesis rather than validated clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current registry records |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 (preclinical/mechanism-level literature only) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not formally on file (DrugBank MOA field is a data gap), but supporting evidence within this evidence pack characterizes favipiravir as a broad-spectrum RNA-dependent RNA polymerase (RdRp) inhibitor with antiviral activity against SFTS virus (severe fever with thrombocytopenia syndrome virus) and Heartland virus — both bunyaviruses.

Infections with these viruses are a recognized trigger for infection-associated hemophagocytic lymphohistiocytosis (HLH). The underlying logic is therefore indirect: suppressing viral replication upstream may reduce the trigger for hemophagocytic activation, rather than favipiravir directly modulating the hemophagocytic/immune-activation pathway itself (e.g., IFN-γ, JAK-STAT signaling).

This distinction matters for interpretation — the TxGNN score of 99.41% reflects a knowledge-graph-level connection between "favipiravir → antiviral → SFTS/Heartland virus → HLH," not direct clinical evidence that favipiravir treats hemophagocytic syndrome as an outcome. It should be read as a research hypothesis rooted in treating the upstream infection, not a validated indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30098914](https://pubmed.ncbi.nlm.nih.gov/30098914/) | 2018 | Review | Journal of Infection and Chemotherapy | Reviews pathophysiology of severe fever with thrombocytopenia syndrome (SFTS), a bunyavirus infection, and discusses development of specific antiviral therapy against SFTSV. |
| [38399689](https://pubmed.ncbi.nlm.nih.gov/38399689/) | 2024 | Review | Microorganisms | Reviews Heartland virus disease, a tick-borne bunyavirus infection with symptoms including fever, leukopenia and thrombocytopenia — an underreported emerging infection. |

## Malaysia Market Information

Malaysia registry data confirms the product is marketed with 1 registered license, but detailed particulars (license number, product name, dosage form, approved indication text) are not populated in the current data extract.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/NPRA label warnings and contraindications are flagged as a **Blocking** data gap — DG001 — pending retrieval of the official product label.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to mechanism-level review literature (L4) with no clinical trials, and the mechanistic link is indirect — favipiravir would act on the upstream viral trigger, not the hemophagocytic pathway itself. Critically, TFDA/NPRA safety label data is a Blocking gap (DG001), which prevents even a baseline safety assessment (S1) from being completed. The two lower-ranked predictions in this pack (malignancy-associated HLH; a mitochondrial Complex IV deficiency) lack any supporting mechanism or literature and are separately flagged Hold.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications) — resolves DG001
- Confirmed mechanism-of-action documentation from DrugBank — resolves DG002
- Original approved indication text for this product (currently missing from the registry extract)
- Case reports or preclinical data directly linking favipiravir treatment to hemophagocytic syndrome outcomes, rather than upstream viral-infection reviews alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

