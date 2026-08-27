---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 2
---

# Mupirocin
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

# Mupirocin: From Skin and Soft-Tissue Infections to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibiotic conventionally used to treat skin and soft-tissue infections such as impetigo. The TxGNN model predicts a possible new application in **Pleural Empyema**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (all NPRA license `approved_indication_text` fields are empty). Based on general pharmacological knowledge, mupirocin is indicated for skin/soft-tissue infections (e.g., impetigo). |
| Predicted New Indication | Pleural Empyema |
| TxGNN Prediction Score | 99.49% (KG rank 7,379) |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, mupirocin inhibits bacterial isoleucyl-tRNA synthetase and is active mainly against Gram-positive organisms, including *Staphylococcus aureus* (MRSA included) — the model's own rationale draws the same link.

For **Pleural Empyema**, the mechanistic connection is that empyema is commonly caused by *Staphylococcus* and *Streptococcus* species, which fall within mupirocin's antibacterial spectrum. However, this is a deep intrathoracic infection requiring systemic or intrapleural drug exposure, while mupirocin is currently only available as a topical formulation (skin/nasal) with minimal systemic absorption and rapid metabolism. This represents a substantial **translational gap between available dosage form and required route of administration**, not a mechanistic mismatch.

A second, lower-priority candidate was also flagged: **Punctate Epithelial Keratoconjunctivitis** (score 99.10%, KG rank 11,511), where some cases are bacterial or secondarily infected and a topical formulation is at least route-compatible with ophthalmic delivery — though no ocular-safe formulation of mupirocin currently exists, and this candidate likewise has zero supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Mupirocin holds **12 active registrations** in Malaysia (NPRA, market status: Marketed), confirming the drug is locally available. However, license-level detail (product names, dosage forms, manufacturers, approved indication text) was not returned in this evidence pack and cannot be tabulated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — flagged as a **Blocking** data gap, `DG001`, since it prevents entry into the S1 safety screening stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications sit at Evidence Level L5 — model prediction only, with no supporting clinical trials, literature, or ICTRP registrations. In addition, a Blocking data gap on TFDA/NPRA safety labeling (warnings/contraindications) prevents any preliminary safety assessment, and the leading candidate (pleural empyema) has a known dosage-form/route mismatch (topical-only product vs. an infection requiring systemic/intrapleural exposure).

**To proceed, the following is needed:**
- Package insert / full prescribing information from NPRA (resolves `DG001`, Blocking)
- Confirmed mechanism-of-action data from DrugBank (resolves `DG002`, High)
- Feasibility assessment of a systemic or intrapleural mupirocin formulation before pursuing the empyema indication
- If pursuing the keratoconjunctivitis candidate, evaluate whether existing excipients are safe for ocular use
- Targeted literature/trial search beyond ClinicalTrials.gov, ICTRP, and PubMed, given the current zero-hit result across all three sources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

