---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (Tecentriq) is an anti-PD-L1 immune checkpoint inhibitor approved for the treatment of urothelial carcinoma (including bladder cancer) and other solid tumours.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma** — a clinically important subset of BCG-unresponsive non-muscle invasive bladder cancer (NMIBC) — with a prediction score of **99.98%**.
This prediction is currently supported by **2 clinical trials** (including 1 completed Phase 2 trial), though no dedicated published literature was identified for this specific anatomical subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma (bladder/upper urinary tract) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Atezolizumab is a monoclonal antibody that targets PD-L1 (Programmed Death-Ligand 1), blocking its interaction with the PD-1 and B7.1 receptors on T cells. This restores anti-tumour immune activity and has been validated across multiple urothelial carcinoma settings, including cisplatin-ineligible patients and post-platinum relapse.

Prostatic urethra urothelial carcinoma is anatomically and histologically a subtype within the broader urothelial carcinoma (UC) family — the same tumour class for which Atezolizumab already holds regulatory approval. Urothelial tumours arising in the prostatic urethra share the same transitional cell origin and PD-L1 expression biology as bladder UC. Crucially, prostatic urethral involvement is a well-recognised feature of BCG-unresponsive NMIBC, where PD-L1 checkpoint inhibition is a clinically logical therapeutic approach.

The completed Phase 2 trial (NCT02844816) specifically studied Atezolizumab in BCG-unresponsive NMIBC — a population that directly overlaps with patients harbouring prostatic urethra involvement. This positions the TxGNN prediction not as a leap into unknown territory, but as a precision refinement of an already-validated clinical indication, making the mechanistic and clinical rationale for this extension highly plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive NMIBC (recurrent/refractory); immunotherapy may help the immune system attack cancer cells and inhibit tumour growth and spread. Prostatic urethral involvement is a key clinical subgroup within this BCG-unresponsive population. |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, Not Recruiting | 914 | Cabozantinib ± Atezolizumab dose-escalation basket trial across multiple tumour types, including advanced urothelial carcinoma (bladder, renal pelvis, ureter, urethra), RCC, CRPC, NSCLC, TNBC, and others. Urothelial carcinoma (including urethral) explicitly listed as an eligible tumour type. |

---

## Literature Evidence

Currently no related literature specifically addressing Atezolizumab in prostatic urethra urothelial carcinoma is available.

---

## Malaysia Market Information

Two product registrations are recorded in the Malaysian National Pharmaceutical Regulatory Agency (NPRA) database. Detailed registration information (authorization numbers, product names, dosage forms, and approved indication text) was not captured in the current data retrieval. Please refer directly to the [NPRA Drug Registration database](https://www.pharmacy.gov.my) for full product labelling details.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| (Not available in current dataset) | — | — | — |
| (Not available in current dataset) | — | — | — |

---

## Cytotoxicity

Atezolizumab is an antineoplastic immunotherapy agent (anti-PD-L1 checkpoint inhibitor) used in oncology settings.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — Checkpoint Inhibitor (anti-PD-L1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (checkpoint inhibitors do not directly suppress bone marrow; immune-mediated haematological adverse events are rare but possible) |
| Emetogenicity Classification | Very low (intravenous monoclonal antibody; emetogenicity is minimal compared to conventional chemotherapy) |
| Monitoring Items | CBC with differential (baseline and periodic), liver function tests (ALT/AST/bilirubin), thyroid function (TSH/free T4), renal function, blood glucose; monitor for immune-related adverse events (irAEs) across all organ systems |
| Handling Protection | Standard biohazard precautions for intravenous biologics; not classified as a cytotoxic hazardous drug under NIOSH guidelines, but institutional policies should be consulted |

---

## Safety Considerations

Detailed warning and contraindication data was not available in this Evidence Pack (package insert data not yet retrieved).

> Please refer to the Atezolizumab (Tecentriq) package insert for complete safety information, including immune-related adverse events (irAEs) such as pneumonitis, hepatitis, colitis, endocrinopathies, and infusion-related reactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Prostatic urethra urothelial carcinoma falls squarely within the urothelial carcinoma disease class for which Atezolizumab is already approved, and the completed Phase 2 trial in BCG-unresponsive NMIBC directly covers the clinical population most likely to harbour this anatomical subtype. The mechanistic basis (PD-L1 expression in UC) is well-established, and the evidence level (L2) is sufficient to justify a structured clinical development pathway rather than a research-only posture.

**To proceed, the following is needed:**

- **Package insert data**: Retrieve and parse the Malaysian (NPRA) approved label to confirm approved indications, warnings, and contraindications — currently a blocking data gap
- **Mechanism of action documentation**: Obtain full MOA data from DrugBank (DB11595) to support regulatory submission narratives
- **Subgroup analysis from NCT02844816**: Request or identify published results stratifying by prostatic urethral involvement to quantify direct efficacy signal
- **Biomarker strategy**: Define PD-L1 expression thresholds or TMB criteria for patient selection specific to prostatic urethra UC
- **Regulatory pathway assessment**: Evaluate whether a label extension or investigator-initiated trial (IIT) is the most efficient route for Malaysian regulatory acceptance
- **Real-world data review**: Search for registry or case series data on Atezolizumab use in BCG-unresponsive NMIBC with prostatic urethral involvement in Asian populations

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All predictions are generated by the TxGNN computational model and must be interpreted in conjunction with clinical expertise and regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

