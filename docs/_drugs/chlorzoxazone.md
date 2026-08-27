---
layout: default
title: Chlorzoxazone
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 9
---

# Chlorzoxazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Chlorzoxazone: From Skeletal Muscle Spasm to Migraine Disorder

## One-Sentence Summary

Chlorzoxazone is a centrally-acting skeletal muscle relaxant historically used for musculoskeletal spasm and pain (detailed label indication text is not available in the current data source — see Data Gaps below). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is currently supported only by **0 clinical trials** and **3 literature items**, all indirect/mechanistic rather than chlorzoxazone-specific.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skeletal muscle spasm relief (based on known drug classification; formal label/indication text not available — see DG001) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for chlorzoxazone is not available (DrugBank MOA field flagged as a High-severity data gap). Based on known information, chlorzoxazone is a centrally-acting skeletal muscle relaxant, and the literature retrieved for this candidate converges on a specific mechanistic hypothesis: chlorzoxazone acts as a Ca²⁺-dependent K⁺ channel (SK/BK) activator, and in animal models this class of activator alleviates cerebellar ataxia caused by enhanced CaV2.1 (P/Q-type calcium channel, *CACNA1A* gene) currents.

*CACNA1A* mutations are also the known genetic cause of familial hemiplegic migraine and migraine with brainstem aura, which creates an indirect pharmacological link between chlorzoxazone's ion-channel activity and migraine pathophysiology. However, this connection is drawn from preclinical ataxia models and general vestibular-disorder reviews — none of the retrieved literature tests chlorzoxazone directly in migraine patients or migraine animal models. The relationship between the original muscle-relaxant use and the predicted migraine indication is therefore mechanistic-hypothesis-level, not clinically demonstrated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Review | Journal of Neurology | Overview of pharmacotherapy for cerebellar and central vestibular disorders; discusses K⁺-channel modulation relevant to nystagmus control, not chlorzoxazone-specific |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Deutsches Ärzteblatt International | Treatment and natural course of peripheral/central vertigo; notes vestibular migraine accounts for 11.4% of vertigo syndromes |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Preclinical | Journal of Neuroscience | In *Cacna1a*(S218L) mutant mice, Ca²⁺-dependent K⁺-channel activators alleviate cerebellar ataxia from enhanced CaV2.1 currents — mechanistic basis for the chlorzoxazone/migraine hypothesis, not a migraine study itself |

---

## Malaysia Market Information

One registration is on file (market status: 已上市 / Marketed), but the current data extract does not include the license number, product name, dosage form, or approved indication text for this registration — these fields need to be pulled from the NPRA source record directly.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** The TFDA/NPRA label warnings and contraindications for chlorzoxazone are flagged as a **Blocking** data gap (DG001) — this data must be obtained before any formal S1 safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest evidence available for the top-ranked candidate (migraine disorder, L4) consists only of preclinical and review-level literature built around a shared *CACNA1A* gene pathway — no study tests chlorzoxazone in migraine directly, and there are no clinical trials. Combined with a Blocking gap on label safety data, there is not yet enough evidence to move past the research-question stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert — warnings and contraindications (DG001, Blocking)
- DrugBank-confirmed mechanism of action (DG002, High)
- Direct preclinical or clinical evidence linking chlorzoxazone (not just the CACNA1A pathway analogy) to migraine
- Malaysia license/product detail verification (license number, dosage form, approved indication text)

*Side note: among the other TxGNN candidates for this drug, rheumatoid arthritis (rank 9, L3, decision stage S2) has comparatively stronger evidence — case-series use of chlorzoxazone combinations in rheumatic/musculo-articular disease dating to the 1960s–70s — and may warrant a separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

