---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is a selective endothelin type A (ETA) receptor antagonist, approved for the treatment of pulmonary arterial hypertension (PAH) and currently marketed in Malaysia under 2 registered products.
The TxGNN model's top-ranked prediction suggests it may be relevant to **Pulmonary Arteriovenous Malformation (PAVM)**, through an indirect mechanistic pathway involving HHT-associated PAH and ETA receptor cross-talk with the BMP/ALK1 signalling axis.
This direction is currently supported by **0 clinical trials** and **1 case report**, placing it at an early exploratory stage only — while separately, evidence for several PAH subtypes (CHD-PAH, CTD-PAH, HIV-PAH) in this same pack reaches L1–L2 and warrants independent evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (PAH) |
| Predicted New Indication | Pulmonary Arteriovenous Malformation (PAVM) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Ambrisentan is a selective ETA receptor antagonist that inhibits endothelin-1 (ET-1)-mediated pulmonary vasoconstriction and vascular smooth muscle proliferation. Its selectivity for ETA over ETB receptors is considered pharmacologically advantageous, as ETB mediates vasodilatory and natriuretic effects that may be preserved during treatment.

Pulmonary arteriovenous malformations (PAVMs) are structural arteriovenous communications within the lung, most commonly (>70%) occurring as a manifestation of hereditary haemorrhagic telangiectasia (HHT) — an autosomal dominant disorder caused by loss-of-function mutations in *ALK1* (*ACVRL1*) or *ENG*. A clinically important minority of HHT patients develops concurrent pulmonary arterial hypertension, creating an overlap syndrome. Research has demonstrated that ET-1 can suppress BMP/ALK1 pathway signalling and drive vascular remodelling, suggesting that ETA blockade might theoretically attenuate this suppression in HHT-associated vascular dysregulation.

However, the mechanistic link is indirect. PAVM itself is a structural defect arising from impaired BMP/ALK1-driven vascular development — its formation is not primarily ET-1-driven. Any potential benefit of Ambrisentan would be confined to managing the PAH component in HHT patients who develop both conditions simultaneously, and would not be expected to prevent, regress, or structurally modify the arteriovenous malformation itself. The TxGNN high score most likely reflects ontological proximity between PAVM (as an HHT feature) and PAH-related nodes in the knowledge graph, rather than a direct drug–disease mechanistic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ambrisentan in pulmonary arteriovenous malformation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World Journal of Clinical Cases | Reports a rare case of HHT complicated by PAH; describes clinical presentation, management strategy, and family genetic analysis. Highlights the diagnostic and therapeutic challenge of this co-occurrence. No direct Ambrisentan efficacy data for PAVM are provided. |

---

## Malaysia Market Information

Malaysia NPRA records confirm **2 registered products** for Ambrisentan (market status: Marketed). Detailed registration data — including license numbers, product names, dosage forms, manufacturers, and approved indication text — are not available in the current dataset.

> For complete registration details, please consult the NPRA Product Registration database directly.

---

## Safety Considerations

> Please refer to the NPRA-approved package insert for full safety information. Detailed warning and contraindication data are not available in the current evidence pack and must be obtained from the prescribing information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for PAVM (99.41%) most likely reflects knowledge graph artefact — specifically, the topological proximity between PAVM/HHT disease nodes and PAH-related nodes — rather than a clinically actionable drug–disease relationship. PAVM is a structural lesion not driven by ET-1 signalling, and the available evidence is limited to a single indirect case report with no Ambrisentan-specific data.

**To proceed, the following is needed:**
- **Mechanistic validation:** Preclinical studies in HHT animal models (e.g., *ALK1*/*ENG* heterozygous knockout mice) to evaluate whether ETA antagonism modifies PAH severity or PAVM progression
- **Refine the research question:** Redirect focus to the specific sub-population of HHT patients with concurrent PAH (not PAVM alone), where the mechanistic rationale is more direct
- **Obtain complete safety data:** Retrieve NPRA package insert to address the blocking data gap (DG001: warnings and contraindications)
- **Obtain MOA data:** Query DrugBank API to address DG002 and enable full mechanistic analysis
- **Confirm registration details:** Retrieve approved indication text from NPRA to characterise the licensed scope in Malaysia

---

## Supplementary: Additional High-Evidence Predicted Indications

> The evidence pack covers 10 TxGNN-predicted indications. The top-ranked prediction (PAVM, L4) has limited evidence. The following indications in the same pack carry substantially stronger evidence and merit independent evaluation.

| Rank | Indication | TxGNN Score | Evidence Level | Clinical Trials | Literature | Recommendation |
|------|-----------|-------------|---------------|-----------------|------------|----------------|
| 2 | PAH associated with Congenital Heart Disease (CHD-PAH) | 99.37% | **L2** | 9 trials (1 completed Phase 3b, 2 Phase 2) | 18 publications | **Proceed with Guardrails** |
| 3 | PAH associated with Connective Tissue Disease (CTD-PAH) | 99.30% | **L2** | 3 trials (2 completed Phase 2/4) | 19 publications (incl. 2 meta-analyses) | **Proceed with Guardrails** |
| 4 | PAH associated with HIV infection (HIV-PAH) | 99.30% | **L1** | 1 completed Phase 3 RCT (HIV-PAH population) | 4 publications | **Proceed with Guardrails** |
| 5 | PAH associated with Chronic Haemolytic Anaemia | 99.30% | L4 | None | None | Hold |
| 6 | PAH associated with Schistosomiasis | 99.30% | L4 | None | None | Hold |
| 7–10 | Periodontal syndrome / Hypotrichosis / Hypertrichosis / Dandy-Walker syndrome | 99.1–99.2% | L5 | None | Unrelated literature | Hold — likely KG artefacts |

**Key observation for CHD-PAH (Rank 2):** The mechanistic pathway is the most directly supported — chronic left-to-right shunting → persistent pulmonary endothelial shear stress → ET-1 upregulation → ETA-mediated vascular remodelling (Eisenmenger physiology). This is the most biologically direct alignment with Ambrisentan's ETA antagonism. A Phase 3b study in 134 Chinese PAH patients (NCT01808313, including CHD-PAH subgroup) has been completed.

**Key observation for CTD-PAH (Rank 3):** Ambrisentan is already included in international guidelines (ESC/ERS) and licensed in several jurisdictions for CTD-PAH, particularly systemic sclerosis-associated PAH. The AMBITION trial CTD-PAH subgroup analysis and multiple Phase 2/4 studies provide L2-level evidence for initial combination therapy (Ambrisentan + Tadalafil). This may represent a label-extension opportunity in Malaysia rather than a novel repurposing.

**Key observation for HIV-PAH (Rank 4):** A completed Phase 3, multicentre, double-blind, placebo-controlled crossover RCT (NCT00709956) enrolled 64 HIV-PAH patients. While this trial evaluated iloprost as the primary intervention, it represents the highest-quality trial evidence available for this patient population and validates the feasibility of controlled studies in HIV-PAH. ERA-specific data (including Ambrisentan background therapy) are available within this dataset.

> ⚠️ **Disclaimer:** All findings are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All clinical use should refer to the NPRA-approved prescribing information and applicable Malaysia regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

