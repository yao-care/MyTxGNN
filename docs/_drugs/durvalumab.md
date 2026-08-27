---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

Using the report template's own instructions directly (no other skill matches — this is a self-contained report-writing task, not TxGNN pipeline engineering, and the evidence pack is already provided in full).

A few things worth flagging before the report: the evidence pack itself has significant gaps — `original_indications` is empty, `original_moa` is `[Data Gap]`, the single Malaysia license record has all fields blank, and the safety fields are all Data Gap / not_found. Per your instructions I won't guess at facts not in the pack (e.g., I won't assert a specific TFDA/NPRA-approved original indication that isn't in the data), but I will use the mechanistic class information ("anti-PD-L1 monoclonal antibody") that *is* explicitly present in the `repurposing_rationale.mechanistic_link` text, since that's sourced data, not invention.

---

# Durvalumab: From Existing Oncology Use to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 monoclonal antibody used in oncology, but this evidence pack does not contain a documented original indication (regulatory indication text is missing — see Data Gap DG001). The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**, an anatomical subtype of urothelial carcinoma, but this specific candidate currently has **0 clinical trials** and **0 publications** directly supporting it — the rationale is drawn entirely by analogy to the broader urothelial carcinoma tumor family.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in source data (approved indication text unavailable; see Data Gap DG001) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is not available for durvalumab in this evidence pack (Data Gap DG002). However, the repurposing rationale accompanying this candidate does identify durvalumab as an **anti-PD-L1 (programmed death-ligand 1) monoclonal antibody** — an immune checkpoint inhibitor. Urothelial carcinoma as a tumor family is characterized by relatively high PD-L1 expression and higher tumor mutational burden (TMB), both features generally associated with better response to checkpoint inhibition.

Prostatic urethra urothelial carcinoma is an anatomical subtype of urothelial carcinoma. Durvalumab already has a documented clinical development history in bladder/urothelial carcinoma more broadly — reflected in trials cited elsewhere in this evidence pack for related subtypes (e.g., NCT02812420 in muscle-invasive high-risk urothelial carcinoma, NCT03912818 in variant-histology bladder cancer). Mechanistically, extending to this specific anatomical location is a reasonable hypothesis by analogy.

That said, no clinical trial or literature record in this evidence pack evaluates durvalumab specifically in prostatic urethra urothelial carcinoma. The rationale is indirect — inferred entirely from evidence in the broader urothelial carcinoma category rather than from data specific to this subtype. Original indication and regulatory context for durvalumab are also not available in this dataset, which limits how confidently the "original → new indication" relationship can be assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available in current data extract | Not available | Not available | Not available (see Data Gap DG001) |

The regulatory record confirms durvalumab is marketed in Malaysia (1 registration on file), but the license number, product name, dosage form, and approved indication text were not populated in this data extract.

---

## Cytotoxicity

Durvalumab is an antineoplastic biologic (anti-PD-L1 immune checkpoint inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — checkpoint inhibitors as a class typically carry low direct myelosuppression risk compared to conventional chemotherapy; drug-specific toxicity data is not available in this evidence pack (Data Gap DG001) |
| Emetogenicity Classification | Low — checkpoint inhibitors as a class are generally minimally emetogenic |
| Monitoring Items | Immune-related adverse event monitoring (thyroid function, liver function tests, renal function, pulmonary and colitis symptoms); baseline and periodic CBC |
| Handling Protection | As a monoclonal antibody, durvalumab is generally not handled under conventional cytotoxic drug precautions, but institutional hazardous-drug handling policy (e.g., NIOSH-listed antineoplastic biologics) should be confirmed locally |

Please refer to the package insert warnings and precautions for drug-specific toxicity data, as this is not available in the current evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (prostatic urethra urothelial carcinoma) has only **L4** evidence — mechanism-level inference by analogy, with zero clinical trials or literature specific to this subtype.
- Data Gap DG001 (TFDA/NPRA package insert warnings and contraindications) is flagged as **Blocking**, meaning this candidate cannot yet enter S1 safety screening regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve DG001: obtain the Malaysia (NPRA) or reference regulatory package insert for durvalumab (warnings, contraindications) to unblock S1 safety review
- Resolve DG002: obtain a verified DrugBank mechanism-of-action record
- Complete the Malaysia license record (license number, product name, dosage form, approved indication text)
- Consider prioritizing research on other candidates in this same pack with stronger existing evidence — e.g., **endocervical carcinoma** (rank 6, evidence level L2, 2 trials including a completed Phase 1), **kidney pelvis sarcomatoid transitional cell carcinoma** (rank 2, L3), and **infiltrating bladder urothelial carcinoma sarcomatoid variant** (rank 3, L3) — as these have actual clinical trial support, unlike the headline prediction above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

