---
layout: default
title: Abiraterone Acetate
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Abiraterone Acetate: From Prostate Cancer to [Awaiting TxGNN Prediction]

## One-Sentence Summary

Abiraterone acetate is a CYP17A1 inhibitor indicated for metastatic castration-resistant prostate cancer (mCRPC), registered in Malaysia under 11 authorizations.
However, **the TxGNN prediction pipeline has not yet generated new indication candidates** for this drug — `predicted_indications` is empty.
Without a prediction output, this report serves as a **data completeness audit** prior to full repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC) *(from general knowledge; NPRA indication text not retrieved)* |
| Predicted New Indication | Not yet generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | **Hold** — critical data gaps block evaluation |

---

## Why is This Prediction Reasonable?

No TxGNN prediction is currently available for Abiraterone Acetate (`predicted_indications: []`). A mechanistic rationale for repurposing cannot be constructed without a target indication.

Currently, detailed mechanism of action data has not been retrieved from DrugBank. Based on publicly available knowledge, Abiraterone Acetate irreversibly inhibits **CYP17A1** (17α-hydroxylase/C17,20-lyase), a key enzyme in androgen biosynthesis in the testes, adrenal glands, and within prostate tumour tissue itself. This androgen-depletion mechanism drives its efficacy in hormone-sensitive and castration-resistant prostate cancer.

Once the TxGNN prediction pipeline is executed and a new indication candidate is identified, the mechanistic bridge between CYP17A1 inhibition and the predicted disease can be evaluated here.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available. Clinical trial evidence cannot be displayed.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available. Literature evidence cannot be displayed.

---

## Malaysia Market Information

The NPRA query returned **11 registered licenses**, but individual license details (authorization number, product name, dosage form, approved indication text) were not populated in this Evidence Pack. Please re-run the data extraction with full field retrieval.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* | *(Not retrieved)* |

> ⚠️ **11 registrations confirmed** via NPRA query (2026-03-27), but individual record details require a follow-up extraction pass.

---

## Cytotoxicity

Abiraterone Acetate is an antineoplastic agent (androgen biosynthesis inhibitor for prostate cancer).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Hormonal / CYP17A1 inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low (non-cytotoxic mechanism; myelosuppression not a primary concern) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT/AST/bilirubin), serum potassium, blood pressure, fluid retention, serum testosterone and PSA |
| Handling Protection | Standard oncology handling precautions; does not typically require cytotoxic drug handling protocols under most institutional guidelines, but confirm per local SOPs |

---

## Safety Considerations

Please refer to the package insert for safety information.

> The Evidence Pack carries **DG001 (Blocking)**: NPRA/TFDA package insert warnings and contraindications have not been retrieved. This gap must be resolved before any safety-gated decision can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The two most critical inputs for a repurposing evaluation — TxGNN predicted indications and safety/MOA data — are both absent. Proceeding without them would yield an uninformative risk assessment.

**To proceed, the following is needed:**

- [ ] **\[DG001 — Blocking\]** Retrieve NPRA/TFDA package insert: download the PDF and parse warnings, contraindications, and special population data
- [ ] **\[DG002 — High\]** Query DrugBank API for `ABIRATERONE ACETATE` to obtain DrugBank ID, confirmed MOA, drug categories, and toxicity data
- [ ] **Re-run TxGNN prediction pipeline** — `predicted_indications` is empty; execute KG + DL prediction steps and populate the Evidence Pack
- [ ] **Re-extract NPRA license details** — 11 registrations exist but individual record fields (product name, dosage form, indication text) were not captured; re-query with full field mapping
- [ ] Once predictions are available, re-generate this report with a target indication and evidence tables
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

