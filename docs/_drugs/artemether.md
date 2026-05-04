---
layout: default
title: Artemether
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: From Malaria Treatment to Acquired Angioedema

## One-Sentence Summary

Artemether is a well-established artemisinin-based sesquiterpene lactone endoperoxide, recognised globally as a first-line component of artemisinin-based combination therapy (ACT) for the treatment of malaria, including uncomplicated and severe *Plasmodium falciparum* malaria.
The TxGNN model predicts it may be effective for **Acquired Angioedema**, with a prediction score of **99.90%**; however, **no clinical trials or supporting publications** have been identified for this specific new indication, rendering the current evidence base insufficient to support clinical translation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (artemisinin-based combination therapy, ACT) |
| Predicted New Indication | Acquired Angioedema |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for artemether is not available in the Evidence Pack. Based on established pharmacological knowledge, artemether is an artemisinin derivative activated by ferrous iron (Fe²⁺) within the parasite food vacuole. Cleavage of the endoperoxide bridge generates carbon-centred free radicals and reactive oxygen species (ROS), which alkylate and damage critical parasitic proteins — including PfATP6 (a sarco/endoplasmic reticulum Ca²⁺-ATPase) and heme polymerase — directly killing *Plasmodium falciparum* erythrocytic-stage parasites. This mechanism is tightly coupled to the iron-rich intraparasitic environment and forms the molecular basis of its antimalarial efficacy.

Acquired angioedema is mechanistically distinct: it is primarily caused by deficiency or functional impairment of C1 esterase inhibitor (C1-INH), leading to uncontrolled activation of the contact system, excessive bradykinin generation, and episodic submucosal and subcutaneous oedema. There is no established pharmacological bridge between artemether's known mode of action (iron-dependent ROS generation and parasite protein alkylation) and the C1-INH/bradykinin axis that drives acquired angioedema.

Some in vitro evidence for artemisinin class compounds — not specifically artemether — suggests partial NF-κB inhibitory activity and anti-complement effects, which could theoretically modulate inflammatory cascades. However, these findings remain entirely preclinical, involve different molecular entities, and have not been extended to C1-INH-pathway or bradykinin-system studies. The high TxGNN score (0.9990) most likely reflects over-generalised connectivity between immune and inflammatory nodes within the knowledge graph, rather than a biologically specific mechanistic signal for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acquired angioedema.

---

## Literature Evidence

Currently no related literature available for acquired angioedema.

---

## Malaysia Market Information

Artemether has **4 registered products** on file with the National Pharmaceutical Regulatory Agency (NPRA) Malaysia. Detailed product information — including product names, dosage forms, manufacturers, and approved indication text — is not available in the current dataset. This information should be retrieved directly from the NPRA product search portal for a complete regulatory assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Key warnings, contraindications, and drug interaction data were not retrievable from the current data sources (classified as data gaps in this Evidence Pack). It is recommended to obtain the full prescribing information from the NPRA-approved product monograph prior to any clinical planning.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high prediction score (99.90%) to acquired angioedema, this confidence is unsupported by any clinical trial data or peer-reviewed literature, and no plausible direct mechanistic link exists between artemether's established pharmacology and the C1-INH/bradykinin-mediated pathophysiology of acquired angioedema. The high score most likely reflects knowledge graph over-generalisation across immune-inflammation nodes, and does not constitute actionable biological evidence.

**To proceed, the following would be needed:**

- **Mechanistic feasibility studies**: In vitro experiments to evaluate artemether's effect on C1-INH activity, bradykinin generation, or contact system activation
- **Preclinical model data**: Animal studies using C1-INH-deficient models (e.g., *Serping1*-knockout mice) to assess any oedema-modifying activity
- **Detailed MOA data**: Full DrugBank and literature review for artemether's pharmacology, including any immunomodulatory or anti-complement properties
- **Safety package**: Package insert warnings, contraindications, and DDI data from NPRA-approved product monograph
- **Malaysia regulatory detail**: Complete NPRA product registration records (product names, dosage forms, approved indications for all 4 registered products)
- **Mechanistic rationale refinement**: If in vitro data emerges, a formal mechanistic hypothesis linking artemether to bradykinin or complement pathway modulation must be developed before progressing to human studies

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

