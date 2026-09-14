---
layout: default
title: Sulodexide
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 3
---

# Sulodexide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Sulodexide: From Venous/Thromboembolic Disease to Glanzmann Thrombasthenia

## One-Sentence Summary

Sulodexide is a glycosaminoglycan-based agent with antithrombotic, profibrinolytic, and vascular endothelial-protective properties, traditionally used in venous and vascular disorders. The TxGNN model predicts it may be relevant to **Glanzmann Thrombasthenia**, a rare inherited platelet function disorder, but this prediction is currently supported by **no clinical trials and no published literature**, and the drug's known pharmacology points in the opposite therapeutic direction from what this bleeding disorder requires.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current Malaysia registration data (known clinical use per pharmacological profile: venous disease, diabetic nephropathy, thrombosis-related vascular conditions) |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism of action data is not available in the Evidence Pack (flagged as a High-severity data gap). Based on the pharmacological description provided, sulodexide is a mixture of glycosaminoglycans (a fast-moving heparin-like fraction plus a slower-moving dermatan sulfate fraction) with **antithrombotic/anticoagulant, profibrinolytic, and blood-viscosity-lowering** effects, and it protects the vascular endothelial glycocalyx. Clinically it is used for venous disease and diabetic nephropathy — conditions related to thrombosis and vascular damage.

Glanzmann Thrombasthenia, by contrast, is a congenital bleeding disorder caused by a GPIIb/IIIa receptor defect that impairs platelet aggregation, producing a **bleeding tendency rather than a thrombotic one**. There is a direct mechanistic mismatch: an antithrombotic/anticoagulant-leaning drug is being proposed for a disorder whose treatment goal is to reduce bleeding, not promote further anticoagulation.

The most plausible explanation is that the TxGNN score reflects graph-level proximity between "platelet/coagulation" nodes in the knowledge graph rather than a genuine, directionally-correct pharmacological rationale. The same pattern applies to the other two ranked candidates (primary platelet release disorder, pseudo-von Willebrand disease), which are also bleeding disorders rather than thrombotic ones. This is an important caution rather than a confirmation of biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Sulodexide holds 2 active registrations in Malaysia (market status: Marketed), but authorization number, product name, dosage form, and approved indication text are not populated in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA package insert warnings and contraindications are flagged as a Blocking data gap (DG001) and must be obtained before any safety-related evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) with zero supporting clinical trials or literature, and the proposed mechanistic link is directionally inconsistent — sulodexide's antithrombotic profile does not logically support treatment of a congenital bleeding disorder like Glanzmann Thrombasthenia.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (DG002)
- Independent pharmacological or preclinical rationale reconciling the antithrombotic/bleeding-disorder mismatch before further investment
- Complete original approved-indication text from Malaysia license records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

