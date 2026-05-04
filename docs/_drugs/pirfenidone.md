---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an oral antifibrotic agent approved for idiopathic pulmonary fibrosis (IPF), acting by inhibiting TGF-β1 and related fibrogenic cytokines to reduce fibroblast proliferation and collagen deposition. The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma** (Rank 1, score 99.71%), though currently **no clinical trials** or **supporting publications** directly evidence this direction. Notably, among all 10 evaluated predictions, **Fibroblastic Neoplasm (Rank 9)** represents the most mechanistically coherent candidate, backed by **6 preclinical and early-phase publications** — and is highlighted as a supplementary finding in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on published information, Pirfenidone is a broad-spectrum antifibrotic small molecule that inhibits TGF-β1, platelet-derived growth factor (PDGF), epidermal growth factor (EGF), and fibroblast growth factor (FGF) signaling. This results in reduced fibroblast proliferation, myofibroblast activation, and extracellular matrix accumulation — the hallmark pathological processes in IPF. Its efficacy in this setting has been established in multiple Phase 3 trials leading to regulatory approvals since 2014.

Extracutaneous mastocytoma is a rare mast cell tumor driven primarily by activating KIT mutations (most commonly D816V). Mast cell survival and proliferation are heavily dependent on KIT-mediated signaling rather than TGF-β pathways. Pirfenidone has no known direct inhibitory activity against KIT, making the mechanistic connection indirect at best. The high TxGNN prediction score most likely reflects the model detecting shared tumor microenvironment fibrosis features across mast cell neoplasms — a signal that is biologically plausible but not disease-specific.

Among all 10 predicted indications in this evidence pack, **Fibroblastic Neoplasm (Rank 9)** offers a more compelling biological rationale: fibroblastic tumors such as Dupuytren's disease and desmoid fibromatosis are directly driven by TGF-β1 signaling — the primary pharmacological target of Pirfenidone. However, two adverse event case reports from the literature describing fibroblastic lesion aggravation during Pirfenidone use introduce an important safety signal that must be reviewed before any oncology development is considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Extracutaneous Mastocytoma.

---

## Literature Evidence

Currently no related literature available for Extracutaneous Mastocytoma.

---

> **Supplementary Finding — Fibroblastic Neoplasm (Rank 9, Score 99.23%, Evidence Level L4):**
> This indication has the highest evidence density among all 10 predictions. The 6 supporting publications are summarised below.

### Supplementary Literature: Fibroblastic Neoplasm

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot Clinical Study | Am J Gastroenterology | Pilot evaluation of Pirfenidone in desmoid tumors arising in familial adenomatous polyposis; drug described as broad-spectrum antifibrotic blocking TGF-β1, PDGF, EGF, and FGF, with potential to prevent new fibrotic lesion formation |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In Vitro Study | BMC Musculoskelet Disord | Pirfenidone inhibited TGF-β1-mediated myofibroblast conversion and fascial contraction in Dupuytren's disease-derived fibroblasts; supports direct mechanistic relevance to fibroblastic proliferative disorders |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In Vitro Mechanistic Study | BMC Musculoskelet Disord | Pirfenidone suppressed both SMAD and non-SMAD TGF-β1 downstream pathways in Dupuytren's fibroblasts, broadening the mechanistic rationale beyond canonical signaling |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical / Formulation Study | Pharm Dev Technol | Injectable Pirfenidone formulation developed for local delivery to Dupuytren's nodules; in vitro data supports TGF-β-induced myofibroblast inhibition as proof of concept for targeted fibroblastic disease treatment |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case Report ⚠️ Adverse Signal | The Permanente Journal | Undifferentiated pleomorphic sarcoma reported following Pirfenidone use for IPF; authors note a potential oncologic adverse signal requiring long-term surveillance |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case Report ⚠️ Adverse Signal | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated during concomitant Pirfenidone and mycophenolate mofetil use in a systemic sclerosis patient; suggests possible paradoxical fibroblastic stimulation in certain contexts |

---

## Malaysia Market Information

The evidence pack records **3 active registrations** for Pirfenidone in Malaysia. Detailed product information — including registration numbers, brand names, dosage forms, and approved indication text — was not returned in this data pull and requires a follow-up query to the NPRA product database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Details not available in current data pull |

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Literature-Derived Safety Signal:** Two published case reports (PMID [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/), [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/)) describe fibroblastic or sarcomatous lesions arising or worsening during Pirfenidone use. While causality is unestablished, these signals are hypothesis-generating and should be formally reviewed through pharmacovigilance analysis before any oncology repurposing study is initiated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Extracutaneous Mastocytoma) has a high model score but zero supporting clinical or preclinical evidence, and the mechanistic link to Pirfenidone's TGF-β inhibitory mechanism is indirect. The prediction score likely reflects shared microenvironmental fibrosis features rather than a disease-specific connection, and the evidence base does not support proceeding to any development stage at this time.

**To reconsider this assessment or escalate Fibroblastic Neoplasm as the primary candidate, the following is needed:**

- **DG001 – Retrieve package insert:** Download and parse NPRA-registered Pirfenidone package inserts to obtain warnings, contraindications, and hepatotoxicity monitoring requirements, which are essential for any oncology safety evaluation
- **DG002 – Confirm MOA from DrugBank:** Retrieve the full mechanism of action profile (DB04951) to formalise the TGF-β inhibition rationale and identify any off-target activities relevant to KIT or PDGFR pathways
- **Regulatory data gap:** Retrieve the 3 Malaysia registration details (product names, dosage forms, indication text) from NPRA to complete market characterisation
- **Pharmacovigilance review:** Formally assess the two adverse oncologic signal case reports before any tumor-directed repurposing pathway is opened
- **Systematic review:** Commission or identify an existing systematic review on Pirfenidone in TGF-β-driven fibroblastic neoplasms (desmoid tumors, Dupuytren's disease) to establish whether L3-level evidence exists
- **Feasibility assessment:** If the pharmacovigilance review is reassuring, evaluate the scientific and regulatory feasibility of a Phase 1/2 exploratory trial in fibroblastic neoplasms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

