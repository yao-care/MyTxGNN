---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 2
---

# Laronidase
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

# Laronidase: From Mucopolysaccharidosis I (MPS I) to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase (recombinant human alpha-L-iduronidase) is the enzyme replacement therapy originally developed and approved (as Aldurazyme) for Mucopolysaccharidosis I (MPS I / Hurler-Scheie spectrum). The TxGNN model predicts high applicability to **lysosomal storage disease with skeletal involvement**, which mechanistically overlaps with the drug's own approved use, supported by **4 publications** and a 99.31% prediction score, though **no clinical trials specific to this exact label** are currently registered.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis I (MPS I / Hurler, Hurler-Scheie, Scheie syndromes) |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Laronidase is recombinant human alpha-L-iduronidase, an enzyme replacement therapy that supplies the enzyme missing in MPS I patients. MPS I arises from IDUA gene defects causing loss of alpha-L-iduronidase activity, which leads to accumulation of heparan sulfate and dermatan sulfate. This buildup drives multi-system disease, including skeletal dysplasia (dysostosis multiplex), joint contractures, and progressive organ damage.

The predicted indication — "lysosomal storage disease with skeletal involvement" — is not a distinct new disease but effectively describes the skeletal manifestation of MPS I itself, the condition laronidase was originally approved to treat. TxGNN has therefore recovered an already-validated, approved use rather than surfaced a novel repurposing signal: the mechanistic link is a direct 1:1 match (enzyme replacement for the exact deficient enzyme), which explains the very high prediction score.

Note: the structured `original_moa` field in DrugBank was flagged as a data gap; the mechanism described above is drawn from the supporting literature and the evidence pack's own mechanistic rationale rather than a DrugBank MOA record.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Overview of MPS I disease spectrum (Hurler, Scheie, Hurler-Scheie); diagnosis via urine GAG pattern and iduronidase enzyme assay |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Development profile of laronidase as recombinant alpha-L-iduronidase ERT for MPS-I, including orphan drug designation and early Phase I data |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Cohort | Pediatric Neurology | 6.5-year follow-up of ERT in attenuated MPS I (Scheie syndrome); patient showed disease progression despite treatment |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | Basic/mechanistic research | Biological & Pharmaceutical Bulletin | Demonstrated laronidase uptake into MPS I fibroblasts/osteoblasts mainly via mannose-6-phosphate receptors, with lysosomal processing |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is essentially certain (this is the drug's own approved indication), but the safety data required for a full S1 review — TFDA/NPRA label warnings and contraindications — is currently a blocking data gap, and no interaction data was found. A separate candidate signal for the same drug (Sanfilippo syndrome / MPS III) was also screened and rejected (**Hold**), since laronidase's target enzyme (alpha-L-iduronidase) is not deficient in that disease and no plausible pharmacological basis exists.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently blocking
- Structured mechanism-of-action data from DrugBank
- Complete Malaysia registration details (license number, product name, dosage form, approved indication text), which were blank in the current evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

