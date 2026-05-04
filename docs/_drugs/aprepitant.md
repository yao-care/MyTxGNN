---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant (brand name: Emend) is a Neurokinin-1 (NK1) receptor antagonist approved for the prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV). The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, a rare renal tubular disorder of water regulation, with a prediction score of **99.97%**. However, **no supporting clinical trials or published literature** were identified for this specific indication, placing this at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (CINV); post-operative nausea and vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 — Model prediction only; no supporting clinical or preclinical studies identified |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Aprepitant is a selective, high-affinity antagonist of the human Substance P / Neurokinin-1 (NK1) receptor. Substance P is a neuropeptide widely distributed across the central and peripheral nervous systems. By blocking the NK1 receptor, Aprepitant interrupts Substance P-mediated signalling cascades — including the emetic reflex arc in the brainstem — which is the mechanistic basis for its anti-emetic effect in chemotherapy patients.

The mechanistic bridge to Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is biologically indirect. NSIAD is a rare X-linked condition caused by gain-of-function mutations in the V2 vasopressin receptor gene (*AVPR2*), rendering renal collecting duct cells constitutively responsive to vasopressin signals regardless of actual circulating vasopressin (ADH) levels. This leads to persistent, inappropriate water retention and hyponatraemia. The NK1/Substance P system has been shown to modulate vasopressin secretion from the posterior pituitary, and NK1 receptors are expressed in hypothalamic nuclei that regulate fluid homeostasis. Blocking Substance P-driven vasopressin stimulation theoretically could attenuate excessive water retention.

However, a critical limitation applies: because NSIAD originates from a constitutively active, ligand-independent AVPR2 mutation, reducing Substance P-mediated upstream vasopressin stimulation may have minimal downstream impact on the mutant receptor. The TxGNN model's high score likely reflects graph-level connectivity between "NK1 signalling," "vasopressin axis," and "renal water handling" nodes in the biomedical knowledge graph, rather than validated pharmacological interaction. No experimental data — animal, cellular, or clinical — currently supports this predicted repurposing.

> **Note:** Formal mechanism of action (MOA) data was not retrieved from DrugBank in this pipeline run (Data Gap DG002). The mechanistic reasoning above is based on published pharmacology literature and is provided for interpretive context only.

---

## Clinical Trial Evidence

Currently no clinical trials related to Aprepitant in Nephrogenic Syndrome of Inappropriate Antidiuresis have been registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

Currently no published literature linking Aprepitant to Nephrogenic Syndrome of Inappropriate Antidiuresis is available.

---

## Malaysia Market Information

8 product registrations are confirmed with the National Pharmaceutical Regulatory Agency (NPRA) Malaysia. Detailed registration records (authorization numbers, product names, dosage forms, and approved indication text) were not returned in the current data query. The market status is confirmed as **Marketed**.

> To retrieve full registration details, please query the NPRA product search portal directly at: https://www.npra.gov.my/

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug-drug interaction records) were not retrieved in this pipeline run.

> Please refer to the approved Aprepitant (Emend®) package insert for complete safety information, including its well-documented CYP3A4 inhibition profile (moderate inhibitor), interactions with warfarin, oral contraceptives, dexamethasone, and other CYP3A4 substrates, as well as contraindications in patients receiving pimozide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns Aprepitant a very high score (99.97%) for NSIAD, likely driven by knowledge graph connectivity through the vasopressin/fluid regulation axis; however, the mechanistic link is indirect and biologically uncertain given the constitutive nature of NSIAD's AVPR2 mutations. With zero supporting clinical trials, zero published literature on this combination, and outstanding formal data gaps in MOA and safety documentation, there is currently no empirical basis to progress beyond a computational hypothesis.

**To proceed, the following is needed:**

- **Preclinical mechanistic study:** Determine whether NK1 antagonism measurably reduces vasopressin secretion *in vivo*, and whether this translates to any reduction in water retention in AVPR2 gain-of-function animal models (e.g., NSIAD knock-in mice)
- **BBB and renal penetration data:** Confirm whether Aprepitant achieves pharmacologically relevant concentrations in hypothalamic nuclei and renal collecting ducts at clinically approved doses
- **DrugBank MOA retrieval:** Complete Data Gap DG002 to formally document the NK1/Substance P mechanism for pipeline records
- **NPRA license detail retrieval:** Complete full extraction of the 8 Malaysia registrations (authorization numbers, dosage forms, approved indications) for a complete regulatory profile
- **TFDA/package insert safety parsing:** Complete Data Gap DG001 to enable formal safety screening before any clinical translation discussion
- **Expert consultation:** Seek input from a nephrologist specialising in rare renal tubular disorders to assess the biological plausibility of this repurposing hypothesis before committing resources to a wet-lab programme

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. This content is generated by an AI-assisted pipeline and should be reviewed by qualified medical and pharmaceutical professionals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

