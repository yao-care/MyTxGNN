---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: From Hematologic/Myeloproliferative Disorders to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is a ribonucleotide reductase inhibitor whose approved indications in Malaysia are not captured in the current NPRA extract (see note below), but which is internationally established for myeloproliferative and sickle-cell hemoglobinopathies. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **20 publications** but **no registered clinical trials** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available NPRA license text (both license records are blank in this extract) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently a data gap (DG002). Based on established pharmacology, hydroxyurea inhibits ribonucleotide reductase, blocking conversion of ribonucleotides to deoxyribonucleotides and inducing S-phase arrest and replication stress. It is a long-standing antineoplastic/cytoreductive agent used in myeloproliferative neoplasms (e.g., CML, essential thrombocythemia) and in sickle cell disease (via fetal hemoglobin induction) — though the specific Malaysian-approved indication text was not retrievable in this data pull.

The repurposing rationale for breast carcinoma is mechanistic rather than clinical: hydroxyurea-induced replication stress can sensitize tumor cells to DNA-damage-response inhibitors (e.g., ATR inhibitors), and this pathway overlaps with replication-stress-avoidance mechanisms implicated in breast cancer progression (e.g., EYA4). Several preclinical studies also show hydroxyurea combined with sensitizing agents (valproic acid, novel RNR/ATR inhibitors) enhances DNA-repair inhibition in breast cancer cell lines, including BRCA1-deficient models.

However, this mechanistic plausibility has not been tested in a prospective breast-cancer-specific clinical trial. The strongest human-use evidence (a 1991 Phase I combination study and a 1994 high-dose consolidation cohort) predates modern breast cancer treatment standards and does not isolate hydroxyurea's independent efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | RCT (Phase I) | American Journal of Clinical Oncology | Sequential 5-FU/leucovorin followed by hydroxyurea (HALF regimen) tested in advanced GI and breast cancer patients |
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Cohort | Bone Marrow Transplantation | High-dose hydroxyurea added to cyclophosphamide/thiotepa consolidation with stem cell rescue in metastatic breast cancer |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | Novel compound enhances hydroxyurea sensitization in breast carcinoma via RPA2 hyperphosphorylation pathway |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Molecular Pharmacology | Novel ribonucleotide reductase inhibitor (class shared with hydroxyurea) inhibits DNA repair in BRCA1-defective breast cancer cells |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | British Journal of Cancer | ATR inhibitor (mechanistically linked to hydroxyurea-induced replication stress) evaluated in breast and ovarian cancer cell lines |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | Preclinical | Drug Research | Hydroxyurea-lipid conjugates designed to improve delivery and efficacy in breast cancer via PI3K/AKT/mTOR pathway targeting |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case Report | Case Reports in Hematology | Coexistent breast cancer and essential thrombocythemia (hydroxyurea-treated) — therapeutic management challenges |
| [28585003](https://pubmed.ncbi.nlm.nih.gov/28585003/) | 2017 | Case Report | Breast Cancer (Tokyo, Japan) | Secondary breast carcinoma arising after CML in complete remission on hydroxyurea + imatinib therapy |
| [26844848](https://pubmed.ncbi.nlm.nih.gov/26844848/) | 2016 | Preclinical | Cancer Biotherapy & Radiopharmaceuticals | Radiolabeling of hydroxyurea for potential in vitro/in vivo tumor imaging applications |

---

## Malaysia Market Information

License-level detail (product name, dosage form, manufacturer, indication text) is not available in the current NPRA data extract — both registered licenses have blank fields. Only the summary status is known: **2 licenses, market status "Marketed."**

---

## Cytotoxicity

Hydroxyurea is a conventional cytotoxic antineoplastic agent (ribonucleotide reductase inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; renal and hepatic function (standard for RNR-inhibitor class agents) |
| Handling Protection | Cytotoxic drug handling precautions required per institutional/regulatory protocol |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/NPRA warnings and contraindications are currently a **Blocking** data gap (DG001) — this must be resolved before any S1 safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials have tested hydroxyurea specifically in breast carcinoma; existing human-use evidence is a 1991 Phase I combination study and a 1994 consolidation cohort, both outside modern treatment context. Remaining support is preclinical/mechanistic (replication stress, DNA repair sensitization). Combined with a Blocking safety data gap (DG001), evidence is insufficient to advance past a research question.

**To proceed, the following is needed:**
- TFDA/NPRA product label — warnings, contraindications, myelosuppression/emetogenicity data (DG001, Blocking)
- DrugBank-confirmed mechanism of action (DG002)
- Malaysia license detail (product name, dosage form, approved indication text) — currently blank in source data
- If pursued, a prospective study design validating the PI3K/AKT/mTOR or RPA2/ATR-pathway sensitization signal in breast cancer

*Note: This evidence pack's own predictions include a stronger candidate — "sickle cell-hemoglobin C disease syndrome" (rank 3, evidence level L1, decision stage S3, "Proceed with Guardrails," 11 trials + 19 publications) — which may warrant its own dedicated evaluation report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

