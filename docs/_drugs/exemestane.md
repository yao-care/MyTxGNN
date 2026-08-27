---
layout: default
title: Exemestane
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 7
---

# Exemestane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Exemestane: From Postmenopausal ER+ Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor whose established use — noted within this evidence pack's own analysis — is postmenopausal ER-positive breast cancer (the formal Malaysian label text was not retrievable; see Data Gaps below). The TxGNN model's top-ranked prediction for this drug is **Antithrombin Deficiency Type 2**, but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and the evidence pack's own rationale flags the signal as likely knowledge-graph noise rather than a genuine mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal ER+ breast cancer (per evidence-pack narrative; formal license indication text is a Blocking data gap — see DG001) |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for exemestane is not available in this evidence pack (`original_moa` is a data gap). Background information embedded in the pack's own rationale text describes exemestane as an irreversible steroidal aromatase inhibitor that lowers estrogen synthesis, used to treat postmenopausal ER-positive breast cancer.

Antithrombin Deficiency Type 2, however, is a hereditary *SERPINC1* gene defect affecting coagulation regulation. The evidence pack's own mechanistic assessment finds **no known pathway connecting aromatase/estrogen signaling to this coagulation disorder**, and notes the high TxGNN score most likely reflects the drug and disease co-occurring near other coagulation-disorder nodes in the knowledge graph, rather than a real pharmacological relationship.

In short: this is a case where a numerically high model score is not accompanied by mechanistic plausibility or any real-world evidence — exactly the profile the evidence pack itself labels as probable graph noise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Exemestane has **2 registered products** in Malaysia (`market_status`: 已上市 / Marketed), but the underlying license records in this evidence pack (license number, product name, dosage form, manufacturer, approved indication text) are all empty — this detail is not currently available from the data source and would need to be pulled directly from NPRA.

---

## Cytotoxicity

Exemestane's original indication involves breast cancer treatment, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/endocrine therapy (steroidal aromatase inhibitor) — non-cytotoxic, per the evidence pack's own background text |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (Antithrombin Deficiency Type 2) has zero clinical trials and zero literature support, and the evidence pack's own mechanistic review judges the TxGNN signal to be likely graph noise rather than a real drug-disease relationship.
- A Blocking data gap (DG001: TFDA/NPRA label warnings and contraindications) means this candidate cannot even proceed to the S1 safety pre-screen yet.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF (warnings, contraindications) — resolves DG001 (Blocking)
- DrugBank MOA data via API — resolves DG002 (High)
- Full Malaysia license records (license number, product name, dosage form, approved indication text) for the 2 registered products
- If continued repurposing evaluation is desired, note that rank 2 in this pack (amenorrhea, L4 evidence, 5 supporting publications) has more literature volume than rank 1 — though that literature describes amenorrhea as a *side effect* observed during ovarian-suppression therapy, not a treatment target, so it would need the same "is this causal or coincidental" scrutiny before advancing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

