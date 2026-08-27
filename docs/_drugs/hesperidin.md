---
layout: default
title: Hesperidin
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 5
---

# Hesperidin
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

# Hesperidin: From Unspecified Original Indication to Myeloproliferative Neoplasm

## One-Sentence Summary

Hesperidin is a citrus-derived bioflavonoid marketed in Malaysia under 53 NPRA registrations; the specific approved indication text was not captured in this data pull, though bioflavonoids of this class are typically marketed for capillary fragility/vascular support. The TxGNN model predicts potential relevance to **myeloproliferative neoplasm**, but this is currently supported only by **0 clinical trials** and **2 preclinical (in silico/in vitro) publications**, with the mechanistic link explicitly noted as non-specific to known MPN pathophysiology (JAK2/CALR/MPL pathways).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not disclosed in NPRA registration records pulled (Hesperidin is a bioflavonoid commonly marketed OTC for capillary fragility/chronic venous insufficiency) |
| Predicted New Indication | Myeloproliferative Neoplasm |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 53 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Hesperidin in this evidence pack. Based on known information, Hesperidin is a citrus flavonoid glycoside (aglycone: hesperetin), commonly used in vascular-health and antioxidant supplement formulations; its efficacy in its typical use context is not itself supported by data in this pack, so the connection to a new oncologic/hematologic indication cannot be evaluated against a confirmed original indication.

The supporting literature for myeloproliferative neoplasm is indirect: one in silico study explores hesperetin-related scaffolds against the BCR kinase domain in chronic myeloid leukemia drug-resistance screening, and one 2025 in vitro study shows hesperetin (the aglycone, not hesperidin itself) modulates membrane progesterone receptor expression and reduces ROS in myeloid leukemia cell lines. Neither study addresses MPN-defining drivers (JAK2 V617F, CALR, MPL mutations), so the biological rationale is a generic antiproliferative/antioxidant extrapolation rather than a disease-specific mechanistic hypothesis.

Notably, a separate literature signal (PMID 14505793, rank 2 candidate) reports that rutinoside glycosylation at the C7 position — the exact structural feature that distinguishes hesperidin from its more active aglycone hesperetin — *attenuates* apoptosis-inducing activity in leukemia cells. This is a cautionary signal rather than supportive evidence, and it should temper enthusiasm for hesperidin (as opposed to hesperetin) specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40751800](https://pubmed.ncbi.nlm.nih.gov/40751800/) | 2025 | In Vitro | Medical Oncology (Northwood, London, England) | Hesperetin increased membrane progesterone receptor expression and reduced ROS in human myeloid leukemia cells |
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | In Silico | Asian Pacific Journal of Cancer Prevention (APJCP) | In silico drug-repurposing screen targeting the BCR kinase domain / Grb-2 interaction in chronic myeloid leukemia to address TKI resistance |

## Malaysia Market Information

License-level details (product names, dosage forms, manufacturers, and approved indication text) were not captured for the 53 NPRA registrations in this data pull. Market status is confirmed as **Marketed (已上市)** with a total of **53 registrations**, but no individual license records are available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. Note: this data pack flags a **Blocking** data gap for TFDA/NPRA label warnings and contraindications — this must be resolved before any safety assessment (S1 stage) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to two preclinical studies on the aglycone (hesperetin), not hesperidin itself, with no clinical trials and no mechanistic link specific to MPN pathophysiology. One available structure-activity study suggests hesperidin's glycosylation may actually *reduce* the relevant bioactivity compared to its aglycone, which weakens rather than supports the case for further investment at this time.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed original indication and DrugBank MOA data for Hesperidin
- Preclinical studies evaluating hesperidin (not just hesperetin) against MPN-relevant models (JAK2/CALR/MPL pathways)
- Clarification of whether the hesperidin formulations marketed in Malaysia are dosed/bioavailable at levels relevant to any oncologic effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

