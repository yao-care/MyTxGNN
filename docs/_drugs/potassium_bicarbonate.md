---
layout: default
title: Potassium Bicarbonate
parent: 僅模型預測 (L5)
nav_order: 564
evidence_level: L5
indication_count: 1
---

# Potassium Bicarbonate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Potassium Bicarbonate: From Electrolyte Replacement to Gastroduodenitis

## One-Sentence Summary

Potassium bicarbonate (DrugBank DB11098) is a potassium/electrolyte replacement and systemic alkalinizing agent, traditionally used to correct hypokalemia and metabolic acidosis.
The TxGNN model predicts it may be effective for **Gastroduodenitis**, but currently **no clinical trials** and **no publications** support this direction — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the current TFDA extract; known clinical use is as an electrolyte replacement / systemic alkalinizer for hypokalemia or metabolic acidosis |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Taiwan Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known pharmacology, potassium bicarbonate is a systemic electrolyte/alkalinizing agent — it is not formulated or established as a topical gastrointestinal drug.

The evidence pack's own mechanistic assessment is skeptical of this prediction: potassium bicarbonate's alkaline component could theoretically neutralize gastric acid and transiently relieve epigastric discomfort, but gastroduodenitis is primarily a mucosal inflammatory condition (commonly driven by *H. pylori* infection, NSAID use, or bile reflux). Potassium bicarbonate has no established anti-inflammatory, antimicrobial, or mucosal-protective mechanism to address that underlying pathology.

The high TxGNN score (99.72%) most likely reflects statistical co-occurrence in the knowledge graph between "potassium/electrolyte – acid-base balance – GI symptom" nodes, rather than a genuine, targeted pharmacological pathway. The mechanistic link should be considered weak and indirect until independently corroborated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

TFDA records show **4 registered licenses** for this drug, but license numbers, product names, dosage forms, manufacturers, and approved indication text are not available in the current data extract — these fields need to be populated from the TFDA source before they can be reported here.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently marked as data gaps — TFDA label warnings/contraindications are flagged as a **Blocking** data gap, item DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN score with no corroborating clinical trials or literature (Evidence Level L5), and the mechanistic rationale in the evidence pack itself is assessed as weak/indirect. A Blocking safety data gap (TFDA label warnings/contraindications) also prevents any S1 safety evaluation at this stage.

**To proceed, the following is needed:**
- TFDA package insert / label (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank — High-priority gap (DG002)
- Complete Taiwan license details (product names, dosage forms, approved indication text)
- Independent preclinical or mechanistic evidence linking potassium bicarbonate to gastroduodenitis before advancing beyond model prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

