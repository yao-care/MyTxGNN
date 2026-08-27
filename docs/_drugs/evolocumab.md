---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Evolocumab: From Hypercholesterolemia to Symptomatic Form of Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab (Repatha) is a PCSK9-inhibiting monoclonal antibody originally used to lower LDL-cholesterol and reduce cardiovascular risk in hypercholesterolemia. The TxGNN model predicts it may be effective for **symptomatic form of hemophilia in female carriers**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and no known biological mechanism links the two conditions.

*Note: This evidence pack contains 6 TxGNN-predicted candidate indications for evolocumab (ranks 1–6, scores 99.08–99.82%), all rated L5 evidence / Hold. This report focuses on the top-ranked candidate; the other five (familial apolipoprotein C-II deficiency, thrombocytopenic purpura, factor XI deficiency, hemophilia A with vascular abnormality, and a non-specific ontology node "disease of catalytic activity") carry the same evidence status.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in the current TFDA/NPRA license extract (fields blank in Evidence Pack). Publicly available labeling identifies evolocumab as indicated to reduce LDL-C and cardiovascular risk in adults/adolescents with hypercholesterolemia (including HeFH/HoFH) and to reduce major adverse cardiovascular events in at-risk adults. |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Evolocumab is a fully human IgG2 monoclonal antibody against PCSK9. It binds circulating PCSK9 and prevents it from binding the LDL receptor (LDLR), blocking PCSK9-mediated LDLR degradation. This allows more LDLR to recycle to the hepatocyte surface, increasing LDL-C clearance from the blood.

Symptomatic hemophilia in female carriers is a coagulation-factor disorder (reduced Factor VIII or IX activity due to skewed X-inactivation), governed by an entirely different biological pathway than lipid metabolism. The evidence pack's own rationale explicitly flags this: *"血友病屬凝血因子路徑疾病，與 PCSK9/LDL 受體路徑無已知機轉關聯，未查得任何生物學合理性佐證"* (hemophilia is a coagulation-pathway disease with no known mechanistic link to the PCSK9/LDLR pathway, and no biological plausibility evidence was found).

In other words, this candidate arises purely from the knowledge-graph's statistical association (TxGNN embedding similarity), not from a pharmacologically grounded rationale. Unlike cases where a shared organ system or pathway justifies a repurposing hypothesis, PCSK9 inhibition and coagulation-factor deficiency have no established biological connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Evolocumab holds 2 active registrations in Malaysia (market status: ✓ Marketed). The Evidence Pack's license records for authorization number, product name, dosage form, and approved indication text are currently blank — this is a data-collection gap (see DG001, listed as Blocking severity), not an absence of registration.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(DG001 flags that TFDA/NPRA label warnings and contraindications have not yet been retrieved — this is a Blocking-severity gap for any S1 safety review of this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, decision stage S0) with zero supporting clinical trials or literature, and the documented mechanistic rationale itself states there is no known biological link between PCSK9/LDLR pathway modulation and coagulation-factor pathway disorders. Evidence is insufficient to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank-sourced MOA confirmation for the regulatory file (currently only externally verified, not in the pack)
- Any preclinical or mechanistic literature specifically testing PCSK9 pathway involvement in coagulation/hemophilia biology
- If no such mechanistic or clinical signal emerges, this candidate should remain closed rather than progress to evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

