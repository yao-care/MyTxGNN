---
layout: default
title: Guaiacol
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 2
---

# Guaiacol
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

# Guaiacol: From Historical Expectorant Use to Acute Laryngopharyngitis

## One-Sentence Summary

Guaiacol (DrugBank DB11359) is a phenolic compound registered in Malaysia under 2 marketing authorizations; the exact approved indication text is not available in the current registry extract. The TxGNN model's top prediction suggests potential relevance to **Acute Laryngopharyngitis**, but this is currently supported by **0 clinical trials and 0 publications** — a model-only signal. A secondary prediction, **Nasal Cavity Disease**, has weaker but non-zero support: **1 clinical trial** (on the related compound guaifenesin) and **1 literature review**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current registry data (approved indication text not populated in either license record) |
| Predicted New Indication | Acute Laryngopharyngitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for guaiacol is not currently available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological background, guaiacol is a phenolic compound historically associated with mild antiseptic and expectorant properties, and is chemically the parent structure of guaifenesin (guaiacol glyceryl ether), a well-established mucolytic/expectorant agent.

The rationale linking guaiacol to acute laryngopharyngitis is purely topological (TxGNN knowledge-graph prediction, score 0.9957) — no clinical trial or published study on guaiacol itself for this indication currently exists in the evidence base. The theoretical basis (mild mucosal effects on upper respiratory inflammation) is plausible but unverified.

A related, better-supported signal exists for **Nasal Cavity Disease**: guaifenesin — sharing the guaiacol core structure — has demonstrated expectorant/mucolytic effects in a completed Phase 2 pediatric trial for chronic rhinitis. Because this evidence comes from a structural analog rather than guaiacol itself, and guaiacol's own MOA is a confirmed data gap, this mechanistic link is of moderate strength and requires validation before it can be extrapolated to guaiacol directly.

---

## Clinical Trial Evidence — Acute Laryngopharyngitis (Primary Prediction)

Currently no related clinical trials registered.

## Literature Evidence — Acute Laryngopharyngitis (Primary Prediction)

Currently no related literature available.

---

## Secondary Prediction: Nasal Cavity Disease (Score 99.51%, Rank 7149, Evidence Level L4)

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | Randomized, placebo-controlled pilot trial of oral guaifenesin (guaiacol derivative, not guaiacol itself) for pediatric chronic rhinitis; evaluated nasal symptom relief via SN-5 survey. Rated Grade B relevance — same chemical family, not the same molecule. |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review | American Journal of Rhinology | Review of sinusitis management in adult cystic fibrosis patients; general sinonasal disease context, not guaiacol-specific. |

---

## Malaysia Market Information

Guaiacol holds 2 marketing authorizations in Malaysia (market status: Marketed), but the license number, product name, dosage form, manufacturer, and approved indication text fields are not populated in the current registry extract. This information should be sourced directly from NPRA product listings before proceeding further.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/NPRA package insert warnings, contraindications, and drug interaction data are not yet available in this evidence pack — retrieval of the product insert is flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold** (for the primary prediction, Acute Laryngopharyngitis)

**Rationale:**
The top-ranked prediction (Acute Laryngopharyngitis) is supported only by the TxGNN model score with zero clinical trials or literature — insufficient to advance past initial screening. The secondary prediction (Nasal Cavity Disease) shows a more promising evidence trail, but the trial evidence is for guaifenesin rather than guaiacol itself, and MOA/safety data for guaiacol remain unconfirmed.

**To proceed, the following is needed:**
- Guaiacol package insert (warnings, contraindications) from TFDA/NPRA — currently a Blocking gap
- Confirmed mechanism of action for guaiacol from DrugBank or primary literature
- Malaysia license details (product names, approved indication text) for the 2 existing registrations
- If pursuing the Nasal Cavity Disease lead: literature or trial data specific to guaiacol (not just guaifenesin) to confirm the mechanistic extrapolation is valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

