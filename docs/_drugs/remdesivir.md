---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 588
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is a nucleotide analogue antiviral prodrug most widely known for treating COVID-19 (SARS-CoV-2 infection). The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, but this pairing currently has **0 clinical trials** and **0 publications** supporting it — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COVID-19 (SARS-CoV-2 infection) — based on the drug's publicly known global indication; NPRA license indication text is not available in this evidence pack |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known information, remdesivir is a nucleotide analogue prodrug that inhibits the viral RNA-dependent RNA polymerase (RdRp), and its clinical use has centered on RNA viral infections — principally COVID-19, with earlier investigational use in Ebola virus disease.

Multiple Endocrine Neoplasia is a hereditary endocrine tumour syndrome driven by germline mutations in genes such as *RET* or *MEN1*, involving tumour-suppressor/oncogene pathways in endocrine tissue. This is mechanistically unrelated to viral RNA replication, and there is no known pharmacological pathway connecting an RdRp inhibitor to MEN pathogenesis.

Given the absence of any clinical trials or literature linking remdesivir to MEN, and the lack of a plausible mechanistic rationale, this prediction is most likely a knowledge-graph artifact — possibly arising from indirect graph paths (e.g., shared "infection–oncology comorbidity" nodes) rather than a genuine pharmacological signal. The high TxGNN score alone is not sufficient grounds to pursue this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The NPRA record indicates the drug is marketed in Malaysia with 1 registered licence; however, detailed licence number, product name, dosage form, and approved indication text are not available in the current evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Multiple Endocrine Neoplasia) has no supporting clinical trials or literature, and no plausible mechanistic link to remdesivir's known antiviral (RdRp-inhibitory) activity — the evidence level is L5 (model prediction only), consistent with a likely false-positive knowledge-graph connection.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action data from DrugBank
- Any preclinical or case-level evidence specifically linking remdesivir to endocrine tumour pathways, before further investment in this candidate
- Note: the #2-ranked candidate (HIV infectious disease) in this evidence pack has more attached trials/literature, but on review those records are actually COVID-19 studies mismapped to the HIV disease label — this indicates a broader disease-mapping data quality issue in the pipeline that should be corrected before re-scoring other candidates for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

