---
layout: default
title: Ammonium Chloride
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 5
---

# Ammonium Chloride
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

# Ammonium Chloride: From Expectorant/Acidifier to Pharyngitis

## One-Sentence Summary

Ammonium Chloride is a well-established compound pharmacologically known as an expectorant and systemic acidifying agent, commonly included in OTC cough and cold preparations.
The TxGNN model predicts it may be effective for **Pharyngitis**, however the prediction score stands at **0.00%** with **0 clinical trials** and **4 publications** of limited direct relevance supporting this direction.
This combination of near-zero model confidence and absent direct clinical evidence warrants a cautious hold before any further development steps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from regulatory records (pharmacologically known as expectorant and systemic acidifier) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 36 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Ammonium Chloride acts as an expectorant by stimulating bronchial gland secretion and increasing respiratory tract fluid volume, thereby reducing mucus viscosity and facilitating clearance of the airways. It also functions as a systemic acidifier by converting to urea and hydrochloric acid in the liver, lowering urinary and systemic pH.

Pharyngitis, common cold, and nasopharyngitis are all upper respiratory tract conditions that share overlapping symptomatic profiles — including throat irritation, mucosal inflammation, and excess mucus production — with which ammonium chloride's expectorant mechanism is broadly compatible. This biological plausibility is further supported by the fact that ammonium chloride is already a common active ingredient in numerous marketed OTC cough and cold preparations, lending indirect credibility to the TxGNN prediction.

However, the TxGNN score of 0.00% is a significant cautionary signal. This value suggests the knowledge graph model found very weak network-level connections between ammonium chloride and pharyngitis, and the evidence retrieved — consisting entirely of papers on structurally related but distinct quaternary ammonium compounds — does not fill this gap. The prediction should therefore be treated as hypothesis-generating rather than actionable at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The following publications were retrieved for ammonium chloride and pharyngitis. **Important caveat:** the papers retrieved describe quaternary ammonium compounds (benzalkonium chloride, benzoxonium chloride) rather than ammonium chloride itself; direct clinical evidence for ammonium chloride as a pharyngitis therapeutic is absent from this evidence pack.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [442769](https://pubmed.ncbi.nlm.nih.gov/442769/) | 1979 | Clinical | ZFA. Zeitschrift fur Allgemeinmedizin | Addresses therapy of acute inflammatory diseases of the mouth and pharyngeal space; abstract unavailable for detailed assessment |
| [3606702](https://pubmed.ncbi.nlm.nih.gov/3606702/) | 1987 | Clinical study | Arzneimittel-Forschung | Benzoxonium chloride (a quaternary ammonium compound, not ammonium chloride) gargle solutions significantly reduced buccopharyngeal bacterial count in healthy volunteers; 38 patients with sore throat showed safety and efficacy signal |
| [7818285](https://pubmed.ncbi.nlm.nih.gov/7818285/) | 1994 | Environmental/Epidemiological | Archives of Environmental Health | Pharyngitis and irritative symptoms observed after accidental exposure to a quaternary ammonium disinfectant via a school HVAC system; documents upper airway sensitivity to this compound class |
| [38622748](https://pubmed.ncbi.nlm.nih.gov/38622748/) | 2024 | Case report | Acta Veterinaria Scandinavica | Severe benzalkonium chloride intoxication in a cat; pharyngitis and oral ulcerations observed at ≤2% concentrations, illustrating mucosal irritation potential of quaternary ammonium compounds |

---

## Malaysia Market Information

Detailed product-level registration data was not populated in this evidence pack. The 36 registered products should be verified directly via the NPRA (National Pharmaceutical Regulatory Agency) public database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| (Not available in evidence pack — 36 registrations confirmed by NPRA query) | — | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information. Warnings, contraindications, and drug interaction data were all flagged as data gaps in this evidence pack and require retrieval from the NPRA product inserts before any safety assessment can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 0.00% indicates negligible model confidence for this repurposing direction, no registered clinical trials exist, and the retrieved literature addresses structurally related but distinct quaternary ammonium compounds rather than ammonium chloride itself — making this evidence pack insufficient to advance a repurposing claim.

**To proceed, the following is needed:**
- **[Blocking]** Download and parse NPRA product insert PDFs to obtain approved indications, warnings, and contraindications for the 36 registered products
- **[High]** Retrieve MOA data from DrugBank API (DB06767) to enable mechanistic link analysis
- Conduct a targeted PubMed search specifically for "ammonium chloride" AND "pharyngitis" or "upper respiratory tract infection" to identify any direct clinical literature not captured in this pack
- Clarify whether the TxGNN score of 0.00% reflects a genuine low-confidence prediction or a technical pipeline issue (e.g., missing node embedding for this drug)
- Review whether any of the 36 Malaysian registered products already carry an upper respiratory tract or cough/cold indication, which would reclassify this as a label-extension rather than repurposing scenario
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

