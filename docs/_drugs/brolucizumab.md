---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Brolucizumab: From Neovascular Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Brolucizumab is an anti-VEGF-A single-chain antibody fragment (scFv) administered via intravitreal injection, originally approved for the treatment of neovascular (wet) age-related macular degeneration (AMD) and diabetic macular edema (DME). The TxGNN model predicts it may be effective for **Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies**, however there are currently **no clinical trials** and **no publications** supporting this direction, and mechanistic analysis indicates no plausible link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular age-related macular degeneration (wet AMD), diabetic macular edema (DME) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Brolucizumab (marketed as Beovu by Novartis) is a humanized single-chain variable fragment (scFv, ~26 kDa) that selectively binds and inhibits vascular endothelial growth factor A (VEGF-A). By blocking VEGF-A, it suppresses pathological angiogenesis and vascular permeability, which are hallmarks of neovascular AMD and diabetic macular edema. It is administered exclusively via intravitreal injection, resulting in minimal systemic exposure.

Mitochondrial oxidative phosphorylation disorders due to nuclear DNA anomalies are a group of inherited metabolic diseases caused by mutations in nuclear genes encoding components of the mitochondrial electron transport chain complexes I–V. These disorders result in impaired cellular energy production and primarily affect high-energy-demand tissues such as the brain, muscles, and heart. The pathophysiology is fundamentally distinct from VEGF-driven angiogenesis.

**This prediction lacks mechanistic plausibility.** There is no established direct regulatory relationship between VEGF signalling and mitochondrial respiratory chain function. Furthermore, brolucizumab is a large biologic molecule that, even if administered systemically, would be unable to penetrate the mitochondrial double membrane to reach the site of pathology. The mechanistic rationale provided in the evidence pack explicitly identifies this as a likely false positive from the knowledge graph. All four predicted indications for this drug share a similar pattern of weak or absent mechanistic rationale, suggesting these predictions represent noise rather than genuine repurposing opportunities.

## Clinical Trial Evidence

Currently no related clinical trials registered for brolucizumab in mitochondrial oxidative phosphorylation disorders, esophageal varices, or exocrine pancreatic insufficiency.

## Literature Evidence

Currently no related literature available for brolucizumab in any of the four predicted indications.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *(Registration number not available in data)* | Brolucizumab (Beovu) | Intravitreal injection | Neovascular (wet) age-related macular degeneration, diabetic macular edema |

> Note: License details (authorization number, local product name, dosage form text) were not populated in the source data. The information above is supplemented from publicly known registration data.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

**Known class-level safety signals for anti-VEGF intravitreal agents (for clinical reference):**
- Intraocular inflammation, including retinal vasculitis and retinal vascular occlusion (specific post-marketing signal for brolucizumab)
- Endophthalmitis (injection-related)
- Increased intraocular pressure
- Thromboembolic events (theoretical systemic risk)

## Additional Predicted Indications (Summary)

Since all four TxGNN predictions for brolucizumab share L5 evidence status and Hold recommendations, they are summarized below for completeness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Plausibility | Recommendation |
|------|---------------------|-------------|---------------|------------------------|----------------|
| 1 | Mitochondrial oxidative phosphorylation disorder (nuclear DNA) | 99.67% | L5 | None — no link between VEGF and mitochondrial respiratory chain | Hold |
| 2 | Esophageal varices without bleeding | 99.12% | L5 | Weak indirect — VEGF plays a role in portal hypertension, but intravitreal formulation cannot achieve systemic anti-VEGF levels | Hold |
| 3 | Esophageal varices with bleeding | 99.12% | L5 | Weak indirect — same as above, with additional safety concern that anti-VEGF impairs vascular repair during active bleeding | Hold |
| 4 | Exocrine pancreatic insufficiency | 99.07% | L5 | None — VEGF inhibition has no known relationship with pancreatic exocrine function; may theoretically worsen pancreatic perfusion | Hold |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications for brolucizumab lack clinical trial evidence, literature support, and — critically — mechanistic plausibility. Brolucizumab is a large biologic molecule formulated exclusively for intravitreal injection with minimal systemic bioavailability, making repurposing for systemic diseases fundamentally impractical without reformulation. The mechanistic analyses uniformly conclude that these predictions are likely false positives from the knowledge graph, with the strongest candidate (esophageal varices) still presenting insurmountable route-of-administration and safety barriers.

**To proceed, the following would be needed:**
- Independent validation of any mechanistic link between VEGF-A inhibition and mitochondrial oxidative phosphorylation (currently no evidence exists)
- Preclinical proof-of-concept studies demonstrating efficacy in relevant disease models
- Development of a systemic formulation with acceptable pharmacokinetics (for any non-ophthalmic indication)
- Comprehensive safety assessment, particularly regarding bleeding risk (for esophageal varices indications)
- Resolution of data gaps: detailed MOA documentation, package insert warnings and contraindications from NPRA

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

