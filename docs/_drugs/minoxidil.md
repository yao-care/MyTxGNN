---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

# Minoxidil: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Minoxidil was originally developed as an oral vasodilator for severe/refractory hypertension, and its topical form is already an approved treatment for androgenetic alopecia.
The TxGNN model's top-ranked new prediction is **Hypotrichosis Simplex of the Scalp**, a rare hereditary hair-loss disorder,
but this direction is currently supported only by **3 case-report publications** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe hypertension (oral, historical first approval); topical minoxidil is separately already approved for androgenetic alopecia. NPRA license-level indication text was not captured in this evidence pack (see note below). |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query flagged as a High-severity data gap). Based on known information, minoxidil is a K⁺-channel opener class vasodilator; its efficacy in hypertension has long been proven, and its topical/oral hair-growth-promoting effect (prolonging the anagen phase, increasing follicular blood flow) is already an established, separately approved use for androgenetic alopecia.

Hypotrichosis simplex of the scalp is a rare monogenic (CDSN gene, autosomal dominant) disorder of hair follicle development and cycling, distinct in etiology from androgenetic alopecia but phenotypically similar (reduced hair density/length). The evidence pack's own repurposing rationale for this candidate states: "遺傳性頭皮單純性稀毛症屬毛囊發育/週期異常，minoxidil 促進毛囊生長之機轉理論上可緩解症狀" — i.e., minoxidil's follicle-stimulating mechanism is theoretically applicable, since it targets the hair growth cycle rather than the disease's specific genetic cause.

Because the underlying defect in hypotrichosis simplex is structural/genetic rather than vascular or androgen-driven, minoxidil is unlikely to be curative; the mechanistic link is plausible but indirect, and this is consistent with the current evidence being limited to individual case reports rather than controlled studies.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case report (oral minoxidil + growth factors) | Dermatologic Therapy | Treatment of hereditary hypotrichosis simplex of the scalp using oral minoxidil combined with growth factors (abstract not available). |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case report (botanical extracts + minoxidil) | Frontiers in Genetics | Familial case (8-year-old male) of CDSN-mutation hypotrichosis simplex treated with a combination of botanic extracts and minoxidil; notes lack of definitive effective treatments for this disease. |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case report (PRP + topical minoxidil) | Journal of Dermatological Treatment | 14-year-old patient with hereditary hypotrichosis simplex successfully treated with combined platelet-rich plasma injection and topical minoxidil 2%. |

## Malaysia Market Information

NPRA records show **15 total registrations** for Minoxidil in Malaysia (market status: Marketed), but individual license details (authorization numbers, product names, dosage forms, approved indication text) were not captured in this evidence pack and require direct retrieval from the NPRA registry.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/NPRA label warnings and contraindications are a documented Blocking data gap — see Conclusion.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for minoxidil in hypotrichosis simplex of the scalp is limited to three case reports (Tier 3, no controlled trials), placing it at evidence level L4/decision stage S1. Separately, TFDA label safety data (warnings, contraindications) is flagged as a **Blocking** data gap, which by itself prevents this candidate from entering the S1 safety initial assessment regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap, DG001)
- DrugBank mechanism-of-action data (High-priority gap, DG002)
- Individual NPRA license details (product names, dosage forms, approved indication text) for the 15 registered Malaysia licenses
- Larger case series or a controlled study specific to hypotrichosis simplex of the scalp, since current evidence is anecdotal and confounded by co-administered treatments (growth factors, PRP, botanical extracts)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

