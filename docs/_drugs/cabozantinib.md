---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

Using the Evidence Pack, I found an important interpretive nuance in the data itself: `predicted_indications[0]` (liposarcoma) is the highest TxGNN-scored *new* signal, but the evidence for `rank 2` (clear cell renal carcinoma) explicitly notes in its own `repurposing_rationale` that this is very likely cabozantinib's **already-approved indication** (confirmed by a post-marketing surveillance trial, NCT04804813), not a genuine new repurposing discovery. I built the report around the template-mandated `predicted_indications[0]` (Liposarcoma) as instructed, and flagged this distinction where it matters for correct interpretation, without fabricating any data not present in the pack (drug MOA, license details, and safety fields are genuine gaps per `meta.data_gaps` DG001/DG002).

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-target tyrosine kinase inhibitor (VEGFR2/MET/AXL/RET) already marketed and used for advanced **renal cell carcinoma** — confirmed within this evidence pack by a completed post-marketing drug-use surveillance study (NCT04804813). The TxGNN model's top-ranked *new* signal predicts potential efficacy in **Liposarcoma**, currently supported by **1 clinical trial** and **1 publication**, representing an early, hypothesis-generating stage of evidence rather than a validated indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (inferred from marketed-drug surveillance data within this evidence pack; TFDA/NPRA label indication text itself is a data gap — see DG001) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed, drug-label-sourced mechanism of action data is not available for cabozantinib in this evidence pack (flagged as data gap DG002, High severity). However, the evidence pack's own repurposing rationale fields describe cabozantinib as a multi-target tyrosine kinase inhibitor acting on **VEGFR2, MET, AXL, and RET** — a mechanism consistent with its established, marketed use in renal cell carcinoma (supported here by the completed Japanese post-marketing surveillance study NCT04804813, "Drug Use Surveillance for Cabometyx Tablets 'Renal Cell Carcinoma'").

The link to liposarcoma follows from tumor biology shared across renal cell carcinoma and soft tissue sarcomas: both are angiogenesis-dependent tumor types, and VEGFR-targeted TKIs (e.g., pazopanib) are already approved for soft tissue sarcoma (STS). Cabozantinib's additional MET/AXL inhibition is proposed to potentially overcome the VEGFR-TKI resistance mechanisms seen in sarcomas (MET/AXL upregulation is a known escape pathway).

Importantly, the current supporting trial (NCT05836571) is a **broad "soft tissue sarcoma" umbrella study**, not a liposarcoma-specific design, and no liposarcoma subgroup results have been published yet. This means the mechanistic rationale is biologically plausible but has not yet been demonstrated specifically in liposarcoma patients — consistent with the L2 evidence level and "Research Question" recommendation assigned to this prediction.

**Note on Interpretation:** This evidence pack's rank-2 prediction, "clear cell renal carcinoma" (score 99.80%), is explicitly annotated in its own rationale as almost certainly cabozantinib's *existing approved indication* rather than a new repurposing signal (supported by 48 trials, 20 publications, multiple completed Phase 3 RCTs including METEOR and CheckMate 9ER, and post-approval surveillance data). It should not be read as a novel repurposing opportunity — Liposarcoma (rank 1) is the more genuinely novel signal, albeit with much thinner evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomized Phase 2 trial comparing immunotherapy (ipilimumab + nivolumab) alone vs. in combination with cabozantinib in advanced soft tissue sarcoma (liposarcoma is one of the eligible histologies, not a dedicated cohort); tests whether adding a multi-kinase TKI improves immune-mediated tumor control. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 | American Journal of Clinical Oncology | Phase 1 study of neoadjuvant cabozantinib combined with radiation therapy in extremity soft tissue sarcomas; establishes preliminary safety of concurrent cabozantinib + RT, an approach previously limited by concerns over fistula/perforation risk. |

---

## Malaysia Market Information

Cabozantinib is currently marketed in Malaysia with **3 registered product licenses**. However, license numbers, product names, dosage forms, manufacturers, and approved indication text for these registrations are not yet populated in this evidence pack — this is tracked as data gap **DG001** (Blocking severity), pending retrieval and parsing of the NPRA/TFDA product label (PDF).

---

## Cytotoxicity

*(Included because cabozantinib is an antineoplastic agent — it is used for renal cell carcinoma and belongs to the targeted multi-kinase inhibitor class.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR2 / MET / AXL / RET multi-kinase inhibitor) |
| Myelosuppression Risk | Not specified in current evidence pack — please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not specified in current evidence pack — please refer to the package insert warnings and precautions |
| Monitoring Items | Not specified in current evidence pack — please refer to the package insert warnings and precautions |
| Handling Protection | Not specified in current evidence pack — please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (All key warnings, contraindications, and drug-interaction data are currently unavailable in this evidence pack — this is tracked as data gap **DG001**, Blocking severity, meaning safety review cannot yet proceed past initial screening.)

---

## Conclusion and Next Steps

**Decision: Research Question (Hold for further evidence generation)**

**Rationale:**
The liposarcoma signal rests on a single, still-ongoing, non-liposarcoma-specific Phase 2 trial and one Phase 1 safety-focused publication — insufficient to support clinical action. This is compounded by a Blocking-severity gap in TFDA/NPRA safety labeling (DG001), which by itself prevents the candidate from entering initial safety assessment (S1) regardless of efficacy evidence maturity.

**To proceed, the following is needed:**
- NPRA/TFDA package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- DrugBank-confirmed mechanism of action — currently a High-severity gap (DG002)
- Liposarcoma-specific subgroup results from NCT05836571 (active, not recruiting; expected completion 2026-05-15)
- Complete Malaysia license-level details (product names, dosage forms, approved indication text) for the 3 existing registrations
- Clarification that the "clear cell renal carcinoma" signal in this same evidence pack reflects an already-approved use, so it is not mistaken for a second repurposing opportunity in downstream decision-making
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

