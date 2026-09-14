---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 5
---

# Pretomanid
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

# Pretomanid: From Extensively Drug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

> Pretomanid is a nitroimidazooxazine antimycobacterial, approved as part of the BPaL (Bedaquiline-Pretomanid-Linezolid) regimen for extensively drug-resistant (XDR) and treatment-intolerant/nonresponsive multidrug-resistant (MDR) pulmonary tuberculosis. The TxGNN model predicts it may be effective for **Candidiasis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's known mechanism (mycobacterial cell-wall/mycolic acid synthesis inhibition and hypoxia-dependent activation) has no established relevance to fungal pathogens — the prediction should be treated as a likely knowledge-graph artifact rather than a genuine repurposing lead.

*(Note: `taiwan_regulatory.licenses[0].approved_indication_text` in the evidence pack is blank; the original indication above is inferred from literature within the same evidence pack, e.g. PMID 41263908.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Extensively drug-resistant tuberculosis (XDR-TB), as part of the BPaL regimen |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available for this evidence pack. Based on contextual information captured elsewhere in the pack, pretomanid's known antimycobacterial activity relies on two pathways specific to mycobacteria: inhibition of mycolic acid (cell wall) biosynthesis, and a nitro-imidazole activation mechanism that depends on mycobacterial-specific enzymes active under hypoxic conditions.

Candidiasis is caused by *Candida* species, which are fungi with a fundamentally different cell wall composition (chitin/glucan, not mycolic acid) and no known dependency on the hypoxia-activation pathway pretomanid exploits. There is no structural, taxonomic, or pharmacological overlap between the original indication (mycobacterial infection) and the predicted indication (fungal infection) that would support a plausible mechanistic link.

Given the absence of any supporting clinical trials or literature, and the lack of a coherent mechanistic rationale, the high TxGNN score most likely reflects an indirect knowledge-graph connection (e.g., shared comorbidity or co-prescription nodes with other anti-infectives) rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia market status indicates the product is **marketed** with **1** registered license. However, the registration number, product name, dosage form, and approved indication text for this license were not populated in the source data — no further detail can be reported without accessing the primary NPRA record.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and a formal drug-interaction (DDI) check are not available in the current data set (DDI query returned no results).

**Additional flagged signal (not from the formal safety fields, but noted elsewhere in this evidence pack):** the rationale for two other TxGNN-predicted candidates (coronary artery disease, myocardial ischemia) references a known QT-prolongation risk for pretomanid. This should be verified against the official label before any further clinical consideration.

---

## Other TxGNN-Predicted Indications (Not Further Assessed Above)

This evidence pack is a multi-candidate pull (`TW-DB05154-multi`) covering 5 predicted indications, all currently at **Hold**:

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|------|------|
| 2 | Leprosy | 99.27% | L4 | Has 3 clinical trials + 9 publications, but PMID 17005816 directly demonstrates *M. leprae* is **naturally resistant** to pretomanid (PA-824) — a mechanistic refutation, not just an evidence gap. |
| 3 | Coronary artery disease | 99.25% | L5 | No trials/literature; conflicts with pretomanid's known QT-prolongation risk. |
| 4 | Myocardial ischemia | 99.17% | L5 | Same rationale as above. |
| 5 | Anomalous left coronary artery from the pulmonary artery (ALCAPA) | 99.08% | L5 | Structural congenital anomaly requiring surgery; no drug-treatable mechanism. |

None of the five candidates in this pack currently clears even a preliminary mechanistic screen.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (candidiasis) has no supporting clinical or literature evidence and no plausible mechanistic basis. Across the full candidate set in this pack, the best-evidenced candidate (leprosy) is directly contradicted by a dedicated antimicrobial-susceptibility study, and the remaining candidates conflict with a known cardiac safety signal or are non-pharmacologically treatable. This is a case where high TxGNN scores are not corroborated by mechanism or evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) from DrugBank or primary literature — currently a High-severity data gap (DG002)
- If any candidate is pursued further, targeted literature/trial searches specific to that indication, since automated queries for candidiasis, coronary artery disease, myocardial ischemia, and ALCAPA returned zero results
- Verification of the QT-prolongation signal referenced in the rationale text against the official label before considering any cardiac-adjacent indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

