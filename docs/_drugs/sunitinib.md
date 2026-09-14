---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From Renal Cell Carcinoma/GIST to Liposarcoma

## One-Sentence Summary

Sunitinib is an oral multi-targeted tyrosine kinase inhibitor established internationally for gastrointestinal stromal tumor (GIST), advanced renal cell carcinoma, and pancreatic neuroendocrine tumors. The TxGNN model predicts it may also be effective for **Liposarcoma**, with **3 clinical trials** and **9 publications** currently supporting this direction — though clinical response in this setting has historically been modest.

*Note: the current evidence pack has no populated NPRA license-level indication text and marks the structured original-indication/MOA fields as data gaps; the original-indication description above reflects internationally established labeling, not an extracted local regulatory record.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in NPRA license extract (all license fields empty); internationally labeled for GIST, advanced/metastatic renal cell carcinoma, and pancreatic neuroendocrine tumors |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, the structured mechanism-of-action field for sunitinib is marked as a data gap in this evidence pack. Based on well-established pharmacology, sunitinib is an oral multi-targeted TKI that inhibits VEGFR1-3, PDGFRα/β, KIT, and FLT3, blocking tumor angiogenesis and growth-factor signaling. This mechanism underlies its approved use in GIST and advanced renal cell carcinoma.

Liposarcoma — particularly the myxoid/round-cell subtype — is a rare soft-tissue sarcoma, and a subset of tumors display PDGFRβ expression with angiogenesis-dependent growth. This creates mechanistic overlap with sunitinib's established anti-angiogenic and anti-PDGFR activity, which is the rationale the evidence pack cites for the TxGNN prediction linking sunitinib to liposarcoma.

However, the evidence pack's own annotation cautions that clinical response rates for sunitinib in liposarcoma have historically been modest, and it is not a first-line agent for this indication — the mechanistic plausibility is real, but efficacy is limited relative to sunitinib's approved uses.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site trial of sunitinib malate in metastatic/unresectable soft tissue sarcoma, including leiomyosarcoma, liposarcoma, fibrosarcoma, and MFH; oral dosing days 1–28 of a 42-day cycle until progression or toxicity. |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing study of sunitinib in non-GIST sarcomas (including liposarcoma), evaluating anti-tumor activity via blockade of growth-related enzymes and tumor blood supply. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol studying regorafenib (a related small-molecule kinase inhibitor, not sunitinib itself) across sarcoma subtypes; cited as class-level mechanistic support only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase 2 trial | International Journal of Cancer | Single-institution Phase 2 study of sunitinib malate in relapsed/refractory soft tissue sarcoma, focused on leiomyosarcoma, liposarcoma, and MFH; evaluated safety and efficacy in these three histologies. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Reviews genetic, epigenetic, and transcriptomic alterations in liposarcoma to guide targeted-therapy selection; notes surgery remains mainstay while targeted options are limited. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Review of Anticancer Therapy | Surveys emerging medical therapies for adult soft tissue sarcoma, including subtype-specific chemosensitivity patterns. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Research | Reports long-lasting clinical benefit of sunitinib malate in a heavily pre-treated metastatic liposarcoma patient. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | N/A | American Journal of Surgical Pathology | Clinicopathologic analysis of 25 cases of myxoid inflammatory myofibroblastic sarcoma, a distinctive sarcoma type; general sarcoma-classification context. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | N/A | Magyar Onkologia | Discusses subtype-based medical treatment of soft tissue sarcomas, including targeted agents by histology. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | N/A | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma; evaluates predictive factors for sunitinib benefit in this related sarcoma subtype. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | N/A | Annals of Oncology | Discusses histology-driven therapy for soft tissue sarcomas, noting trabectedin's high activity specifically in myxoid liposarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | N/A | BMC Cancer | Protocol for the REGOSARC trial evaluating regorafenib (a related TKI) in advanced soft tissue sarcoma; angiogenesis-pathway rationale relevant to sunitinib's mechanism. |

---

## Malaysia Market Information

License-level details (authorization number, product name, dosage form, indication text) are not populated in the current dataset. NPRA records confirm Sunitinib holds **20 active marketing authorizations** in Malaysia with market status **已上市 (Marketed)**.

---

## Cytotoxicity

Please refer to the package insert warnings and precautions — DrugBank category, MOA, and toxicity data are not available in the current evidence pack to support a detailed cytotoxicity classification.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L2 (single dedicated Phase 2 trial population plus supportive literature), and the evidence pack itself flags sunitinib's response rate in liposarcoma as modest and non-first-line; the model score is high, but clinical evidence does not yet support active pursuit.

**To proceed, the following is needed:**
- TFDA/NPRA-sourced package insert (warnings, contraindications, DDI) to clear the current safety data gap
- DrugBank-sourced mechanism of action and drug category data
- Populated NPRA license records (product names, dosage forms, approved indication text) for the 20 existing registrations
- Liposarcoma-subtype-stratified efficacy data (particularly myxoid/round-cell) before considering further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

