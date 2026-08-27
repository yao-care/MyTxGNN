---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 2
---

# Nimodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nimodipine: From Cerebral Vasospasm Prevention to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a dihydropyridine calcium channel blocker whose established clinical use is preventing cerebral vasospasm after aneurysmal subarachnoid hemorrhage. The TxGNN model predicts a possible link to **Homozygous Familial Hypercholesterolemia (HoFH)**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the pack's own mechanistic review finds no plausible pharmacological connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in registry data; known clinical use is prevention of cerebral vasospasm following subarachnoid hemorrhage |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not retrievable from the queried DrugBank record. Based on known pharmacology, nimodipine is a highly lipophilic dihydropyridine calcium channel blocker acting on L-type Ca²⁺ channels in vascular smooth muscle, and its only established indication is cerebral vasospasm prophylaxis after subarachnoid hemorrhage.

HoFH pathophysiology is driven by homozygous loss-of-function mutations in the LDL receptor (LDLR) gene, impairing hepatic LDL clearance — a pathway with no known interaction with L-type calcium channel signaling. The evidence pack's own mechanistic review concludes that the high TxGNN score (0.993) likely reflects topological proximity between vascular/cardiovascular nodes in the knowledge graph rather than a genuine pharmacological relationship.

A second candidate, nephrogenic syndrome of inappropriate antidiuresis (NSIAD, score 0.991), was also predicted. NSIAD arises from gain-of-function mutations in the AVPR2 (V2 vasopressin receptor), acting through the renal collecting-duct cAMP pathway. While calcium and cAMP signaling can theoretically cross-talk, no direct evidence supports CCBs modulating V2 receptor activity or treating this disorder. Both candidates therefore represent high-confidence model outputs without corresponding mechanistic or clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Nimodipine has 2 active NPRA registrations, but authorization numbers, product names, dosage forms, and approved indication text were not captured in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. TFDA/NPRA labeled warnings and contraindications for nimodipine could not be retrieved (flagged as a Blocking data gap, DG001), so no S1 safety screening can be completed at this time. No drug-drug interaction data was found (query returned zero results).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications sit at evidence level L5 / decision stage S0 — high TxGNN scores with zero corroborating clinical trials or literature, and the pack's own mechanistic analysis finds no plausible pharmacological link between L-type calcium channel blockade and either LDLR-driven HoFH or AVPR2-driven NSIAD.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism-of-action data from DrugBank or primary literature
- Any preclinical or mechanistic studies linking CCB activity to lipid metabolism (HoFH) or V2-receptor/cAMP signaling (NSIAD)
- Re-screen for clinical trials/literature periodically, as current searches returned no hits for either indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

