---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 2
---

# Baricitinib
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

# Baricitinib: From Autoimmune Diseases to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Baricitinib is a selective JAK1/JAK2 inhibitor, originally approved for the treatment of autoimmune conditions such as rheumatoid arthritis and atopic dermatitis. The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, however there are currently **no clinical trials** and **no publications** supporting this direction. A secondary prediction for **Brachydactyly-Syndactyly Syndrome** similarly lacks supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune diseases (specific approved indication text not available in data) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Baricitinib is a selective Janus kinase (JAK) 1 and JAK2 inhibitor. By blocking JAK-STAT signalling, it suppresses the downstream inflammatory cascades driven by multiple cytokines (IL-6, IL-12, IL-23, IFN-γ, etc.). This mechanism has proven effective in rheumatoid arthritis, atopic dermatitis, alopecia areata, and was granted emergency use authorisation for COVID-19.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital disorder caused by mutations in developmental signalling pathways (SHH, PAX2, BMP), leading to structural malformations of the eye (microphthalmia with coloboma) and skeletal system (rhizomelic shortening). The mechanistic link between JAK-STAT inhibition and this developmental disorder is **extremely weak** — the disease arises from embryonic morphogenetic defects that are irreversible after birth, and JAK-STAT signalling is not a primary driver of the affected developmental pathways.

Although TxGNN assigned a high prediction score (99.94%), this likely reflects topological proximity in the knowledge graph rather than a genuine pharmacological rationale. The absence of any clinical trials, preclinical studies, or published literature further undermines the biological plausibility of this repurposing candidate. The secondary predicted indication (brachydactyly-syndactyly syndrome) shares a similar profile — a congenital skeletal malformation driven by BMP/GDF pathway mutations with no mechanistic connection to JAK inhibition.

## Clinical Trial Evidence

Currently no related clinical trials registered for Baricitinib in colobomatous microphthalmia-rhizomelic dysplasia syndrome.

## Literature Evidence

Currently no related literature available for Baricitinib in colobomatous microphthalmia-rhizomelic dysplasia syndrome.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| (Not available) | (Not available) | (Not available) | (Not available) |

*Note: Baricitinib has 2 registered products in Malaysia, but detailed registration information was not captured in the current data collection. Please consult the NPRA Quest database for complete product information.*

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack. As a JAK inhibitor, prescribers should generally be aware of risks including serious infections, thromboembolism, malignancy, and cardiovascular events as noted in the class-wide regulatory warnings for JAK inhibitors.

## Secondary Predicted Indication: Brachydactyly-Syndactyly Syndrome

| Item | Content |
|------|------|
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (Model prediction only) |
| Mechanistic Link | Very weak — disease driven by BMP/GDF pathway gene mutations (GDF5, HOXD13, BMPR1B); congenital skeletal malformation is irreversible post-birth |
| Clinical Trials | None |
| Literature | None |
| Recommended Decision | Hold |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are rare congenital developmental disorders with no mechanistic connection to JAK-STAT inhibition. Evidence level is L5 — there are zero clinical trials, zero publications, and the repurposing rationale from a biological perspective is extremely weak. These congenital structural malformations are irreversible after birth, making post-natal pharmacological intervention with a JAK inhibitor biologically implausible.

**To proceed, the following would be needed:**
- Preclinical evidence demonstrating JAK-STAT involvement in the pathogenesis of colobomatous microphthalmia-rhizomelic dysplasia syndrome
- Identification of any post-natal inflammatory or progressive component of the disease that could be amenable to JAK inhibition
- Completion of the Malaysia NPRA registration data (product names, dosage forms, approved indications)
- Detailed mechanism of action data from DrugBank
- Safety profile extraction from package insert (key warnings, contraindications, drug interactions)

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

