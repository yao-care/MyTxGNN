---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is a next-generation anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor, originally approved for the treatment of ALK-positive metastatic non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this specific indication, placing this at the lowest evidence level (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive metastatic non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Brigatinib (brand name ALUNBRIG™) is a next-generation small molecule tyrosine kinase inhibitor that primarily targets anaplastic lymphoma kinase (ALK). It also exhibits inhibitory activity against additional kinases including ROS1, FLT3, EGFR (including T790M mutant), and IGF-1R. It was first approved by the US FDA in April 2017 for ALK-positive metastatic NSCLC, and its first-line efficacy was established through the landmark Phase 3 ALTA-1L trial demonstrating superior progression-free survival over crizotinib. Detailed mechanism of action data was not available in the Evidence Pack, but based on extensive published literature, brigatinib's primary mechanism involves potent and selective inhibition of ALK kinase activity, blocking downstream oncogenic signalling pathways (RAS/MAPK, PI3K/AKT, JAK/STAT).

Gingival fibromatosis is a benign condition characterised by progressive, non-neoplastic fibrous overgrowth of gingival tissue. It can be hereditary (caused by mutations in genes such as SOS1 or HGF) or drug-induced (commonly by calcium channel blockers, cyclosporin, or phenytoin). The pathophysiology involves excessive collagen deposition by gingival fibroblasts, driven by growth factor signalling (particularly TGF-β and CTGF pathways) rather than kinase-driven oncogenic proliferation.

The mechanistic link between ALK inhibition and gingival fibromatosis is weak. There is no established evidence that ALK signalling plays a role in gingival fibroblast proliferation or collagen overproduction. While TxGNN assigned a high prediction score (99.89%), this likely reflects topological proximity in the knowledge graph rather than a true pharmacological rationale. The absence of any clinical trials, case reports, or preclinical studies linking brigatinib (or any ALK inhibitor) to gingival fibromatosis further underscores the speculative nature of this prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered for brigatinib in gingival fibromatosis.

## Literature Evidence

Currently no related literature available for brigatinib in gingival fibromatosis.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details pending) | — | — | ALK-positive NSCLC |
| (Details pending) | — | — | ALK-positive NSCLC |
| (Details pending) | — | — | ALK-positive NSCLC |

> *Note: 3 registrations are recorded in the NPRA database, but detailed product information (authorization numbers, product names, dosage forms, and approved indication text) was not available in the current data extract.*

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low to moderate — lymphopenia and anaemia reported; severe myelosuppression uncommon compared to conventional cytotoxics |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, hepatic transaminases (ALT/AST), lipase/amylase, serum creatinine, blood glucose, blood pressure; pulmonary function (risk of early-onset pulmonary events/ILD) |
| Handling Protection | Standard precautions for oral antineoplastic agents; no cytotoxic spill kit required for intact tablets, but broken/crushed tablets should be handled with gloves per institutional guidelines |

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

**Known class-level safety signals from published literature include:**
- **Interstitial lung disease (ILD) / Pneumonitis**: Early-onset pulmonary events (within 7 days of initiation) reported in clinical trials; dose escalation strategy (90 mg × 7 days → 180 mg) was implemented to mitigate this risk
- **Hypertension**: Treatment-emergent hypertension reported in ALTA-1L; blood pressure monitoring recommended
- **Hepatotoxicity**: Elevations in ALT/AST observed; periodic liver function monitoring advised
- **Tumour lysis syndrome (TLS)**: A fatal case of brigatinib-induced TLS has been reported in the literature (PMID: 34987411)
- **Visual disturbances**: Blurred vision and other visual symptoms reported

## Additional Predicted Indications Overview

Given that the top-ranked prediction (gingival fibromatosis) lacks mechanistic rationale, a summary of all 10 predicted indications is provided below for completeness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Plausibility | Recommendation |
|------|---------------------|-------------|----------------|--------------------------|----------------|
| 1 | Fibromatosis, gingival | 99.89% | L5 | None — no ALK pathway involvement | Hold |
| 2 | Fibroma of lung | 99.86% | L5 | None — benign tumour, no ALK activation | Hold |
| 3 | Hamartoma of lung | 99.85% | L5 | None — HMGA2-driven, not ALK | Hold |
| 4 | Lung hilum carcinoma | 99.85% | L4 | **Conditional** — if ALK+ NSCLC subtype, brigatinib already has Phase 3 evidence | Research Question |
| 5 | Lung benign neoplasm | 99.85% | L5 | None — benign tumours lack ALK activation | Hold |
| 6 | IBMPFD (VCP-related) | 99.84% | L5 | None — VCP gene mutation, unrelated to ALK | Hold |
| 7 | Lung germ cell tumour | 99.84% | L4 | Weak — ALK not a common driver in GCTs | Hold |
| 8 | Pulmonary sulcus neoplasm | 99.84% | L4 | **Conditional** — Pancoast tumour is NSCLC; if ALK+, existing evidence applies | Research Question |
| 9 | Junctional epidermolysis bullosa | 99.83% | L5 | None — structural protein defect, unrelated to kinase signalling | Hold |
| 10 | Leukomelanoderma syndrome | 99.83% | L5 | None — rare genetic developmental syndrome | Hold |

**Notable finding**: The most scientifically interesting signal for brigatinib repurposing does **not** appear in the TxGNN top-10 list but is present in the literature evidence: **NF2-related schwannomatosis**. A Phase 2 trial published in *The New England Journal of Medicine* (PMID: [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/)) demonstrated that brigatinib causes tumour shrinkage in NF2-deficient schwannomas and meningiomas through inhibition of multiple tyrosine kinases (not ALK), representing a genuine mechanistically validated repurposing opportunity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication (gingival fibromatosis) lacks any mechanistic rationale linking ALK inhibition to the pathophysiology of gingival fibrous overgrowth. There are zero clinical trials and zero publications supporting this specific drug–disease pair. The remaining predictions are similarly unsupported, with the partial exception of anatomical subtypes of NSCLC (lung hilum carcinoma, Pancoast tumour), for which brigatinib's existing ALK-positive NSCLC indication already applies conditionally. The high TxGNN scores (>99.8%) across all predictions likely reflect the drug's strong connectivity within the knowledge graph rather than true therapeutic potential for these specific conditions.

**To proceed, the following is needed:**
- Obtain detailed mechanism of action data from DrugBank to assess off-target kinase activity that might be relevant to non-oncologic conditions
- Retrieve package insert safety information (key warnings, contraindications) from NPRA to complete the safety profile
- Investigate the NF2-schwannomatosis signal further — this represents the most promising repurposing lead supported by Phase 2 clinical evidence (NEJM 2024), though it was not captured in the TxGNN prediction ranking
- For lung hilum carcinoma and pulmonary sulcus neoplasm, no additional action is needed — these are anatomical subtypes of NSCLC already covered by the existing ALK-positive NSCLC indication
- Consider whether TxGNN model retraining or feature engineering could improve specificity for distinguishing benign from malignant conditions

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

