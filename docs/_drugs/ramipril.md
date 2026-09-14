---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Hypertension to Ischemic Stroke Susceptibility

## One-Sentence Summary

Ramipril is a long-established ACE inhibitor originally used to treat **hypertension** (and, per existing outcome trials, to reduce cardiovascular/stroke risk in high-risk patients). The TxGNN model's top-ranked new signal points to **"obsolete susceptibility to ischemic stroke,"** but this term carries **no independent clinical trials or literature** and its own rationale flags it as a likely duplicate/obsolete ontology node overlapping with stroke-related terms that are already part of Ramipril's established use — so it is not yet a genuine, actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from drug class and cross-references in the evidence pack; TFDA/NPRA indication text not yet retrieved) |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Ramipril is not available in this evidence pack. Based on known pharmacology, Ramipril is an angiotensin-converting enzyme (ACE) inhibitor: it blocks conversion of angiotensin I to angiotensin II, reducing vasoconstriction and aldosterone release. This mechanism is well established for blood pressure control and, per the HOPE trial and related outcome data captured elsewhere in this evidence pack, also reduces cardiovascular death, myocardial infarction, and stroke in high-risk patients — an effect mechanistically consistent with reduced vascular resistance and endothelial protection.

However, the specific top-ranked term "obsolete susceptibility to ischemic stroke" is not supported by any drug-specific clinical trial or literature evidence — the query log confirms zero results across ClinicalTrials.gov, ICTRP, and PubMed for this exact term. The evidence pack's own rationale is explicit that this label may be an overlapping or deprecated node in the underlying disease ontology relative to "stroke disorder" and "cerebrovascular disorder," which appear separately in this same prediction set with strong, direct Phase 3/4 trial support (e.g., HOPE, ONTARGET). In other words, the mechanistic story for *stroke risk reduction* is credible for Ramipril, but the specific node being scored here is likely redundant with — rather than independent evidence for — those better-supported terms.

Because of this ambiguity, the prediction should be treated as a data-quality question first, and a pharmacological hypothesis second, until the ontology overlap is resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Detailed licence-level data (authorisation number, product name, dosage form, indication text) was not returned for this drug in the current evidence pack — all fields in the source records are blank. What is confirmed: Ramipril is **marketed in Malaysia** under **8 registered product licences**. Licence-level details should be pulled directly from NPRA QUEST3+ before this candidate proceeds further.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate carries only model-prediction-level evidence (L3) with zero corroborating trials or literature, and the rationale itself suggests it may be a duplicate/obsolete ontology node rather than a distinct clinical entity — it should not be advanced as a repurposing hypothesis until that is clarified. (Note: other candidates in this evidence pack — "hypertensive disorder," "cerebrovascular disorder," and "stroke disorder" — already carry L1 evidence via HOPE/ONTARGET, but these reflect Ramipril's *existing* approved use and outcome benefit rather than a new indication.)

**To proceed, the following is needed:**
- Clarify whether "obsolete susceptibility to ischemic stroke" is a distinct disease entity or a deprecated/duplicate node relative to "stroke disorder" and "cerebrovascular disorder" in the underlying ontology
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap — DG001)
- DrugBank mechanism-of-action data (High-severity data gap — DG002)
- Malaysia licence-level details (product names, dosage forms, approved indication text) from NPRA QUEST3+
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

