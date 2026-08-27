---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Multiple Myeloma/Ovarian Cancer to Hereditary Breast-Ovarian Cancer Syndrome

## One-Sentence Summary

> Melphalan is a bifunctional alkylating agent classically used for multiple myeloma and epithelial ovarian cancer. The TxGNN model predicts it may be effective for **Hereditary Breast-Ovarian Cancer Syndrome**, but this specific candidate currently has **zero clinical trials** and **zero publications** supporting it — the prediction rests entirely on a mechanistic hypothesis (DNA crosslinking in HR-deficient/BRCA-mutated cells) with no experimental confirmation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied registry data (TFDA/NPRA indication text was not captured); melphalan's internationally recognized indications are multiple myeloma and palliative treatment of epithelial ovarian cancer |
| Predicted New Indication | Hereditary Breast Ovarian Cancer Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for melphalan was not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic rationale captured alongside this prediction, melphalan is a bifunctional nitrogen mustard alkylating agent that forms DNA interstrand crosslinks. In cells with homologous recombination (HR) repair deficiency — such as those carrying BRCA1/2 mutations, which define hereditary breast-ovarian cancer syndrome — this crosslinking damage is theoretically harder to repair, creating a potential synthetic-lethal vulnerability. This is the same class of logic that underlies the clinical use of platinum agents and PARP inhibitors in BRCA-mutated cancers, and it plausibly explains why TxGNN assigned this candidate a very high score.

Melphalan already has an established history in ovarian malignancy broadly (including historical randomized comparisons against cisplatin-based regimens, and current use in high-dose conditioning regimens before stem cell transplant for various gynecologic and germ-cell tumors, per other candidates in this same evidence pack). Hereditary breast-ovarian cancer syndrome, however, is a genetic predisposition syndrome rather than a specific tumor type, and no clinical trial or publication in this dataset directly tests melphalan in that population. The mechanistic link is biologically coherent but entirely unvalidated for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

The NPRA registry data supplied for this evidence pack lists **2 active authorizations** for melphalan in Malaysia (market status: marketed), but license number, product name, dosage form, and approved-indication text were not populated in the source data — these fields will need to be retrieved directly from NPRA before further use.

---

## Cytotoxicity

Melphalan is a conventional cytotoxic chemotherapy agent (bifunctional alkylating agent, nitrogen mustard class), and all top predicted indications in this evidence pack are oncologic — this section therefore applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High — myelosuppression (neutropenia, thrombocytopenia) is the dose-limiting toxicity, particularly pronounced in high-dose/transplant-conditioning regimens |
| Emetogenicity Classification | Moderate at conventional oral/IV doses; high with high-dose conditioning regimens |
| Monitoring Items | CBC with differential and platelet count, renal function, hepatic function |
| Handling Protection | Requires standard cytotoxic/hazardous drug handling precautions |

Please refer to the package insert for drug-specific toxicity thresholds, as detailed institutional toxicity data was not available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate (Hereditary Breast-Ovarian Cancer Syndrome) is supported only by a TxGNN model score and a plausible but unvalidated mechanistic hypothesis — there is no clinical trial or literature evidence (L5), consistent with the pack's own S0/Hold scoring. In addition, TFDA/NPRA safety labeling (warnings and contraindications) is a **Blocking** data gap, meaning safety review cannot even begin at this stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a blocking gap
- DrugBank-sourced mechanism of action and toxicity profile — currently a high-severity gap
- Preclinical or case-level evidence specifically linking melphalan to HR-deficient/BRCA-mutated tumors before considering escalation beyond Hold
- If evidence generation is prioritized elsewhere in this pack, rank 8 (gonadal germ cell tumor, L2, "Research Question") has materially stronger existing evidence — a Phase 2 trial specifically in poor-prognosis relapsed germ-cell tumors — and may be a more productive candidate to advance first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

