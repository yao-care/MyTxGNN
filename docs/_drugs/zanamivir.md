---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 693
evidence_level: L5
indication_count: 2
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Zanamivir is a neuraminidase inhibitor whose evidence pack does not record a confirmed original indication or approved indication text, but its mechanism (blocking influenza virus release via viral surface glycoprotein inhibition) is well documented in the accompanying rationale.
> The TxGNN model predicts it may be effective for **Pyelonephritis**, a bacterial urinary tract infection,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in TFDA license text or `original_indications` field; evidence pack rationale identifies zanamivir as an anti-influenza neuraminidase inhibitor |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no supporting clinical trials or literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for zanamivir is marked as a data gap (`original_moa: [Data Gap]`), but the evidence pack's own rationale describes it as a **neuraminidase inhibitor** that acts exclusively on the influenza virus surface glycoprotein to block viral particle release — a purely antiviral mechanism.

Pyelonephritis, in contrast, is a **bacterial** upper urinary tract infection (most commonly caused by *E. coli*), driven by bacterial adhesion, invasion, and inflammatory pathways entirely unrelated to influenza viral neuraminidase activity. There is no known cross-reactivity, shared target, or overlapping pathway between viral neuraminidase inhibition and antibacterial activity.

The evidence pack explicitly assesses this link as **not mechanistically supported**: the high TxGNN similarity score is attributed to knowledge-graph embedding proximity rather than any real pharmacological or clinical relationship. This is corroborated by a second, lower-ranked prediction in the same pack (disorder of tyrosine metabolism, score 99.02%), where the only literature returned discusses influenza NA resistance mutations (H274Y/N294S) — topically irrelevant to a hereditary amino acid metabolism disorder, again indicating keyword/entity-matching artifacts rather than genuine repurposing signal. This pattern across both top predictions suggests the current run has a systematic false-positive issue for this drug rather than an isolated anomaly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not specified in evidence pack | Not specified in evidence pack | Not specified in evidence pack | Not specified in evidence pack |

*Note: `total_licenses` reports 1 registration, but the license record itself contains no populated fields (number, product name, dosage form, or indication text) in this evidence pack.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The evidence pack flags TFDA label warnings/contraindications (DG001) as a **Blocking** data gap — this alone prevents the candidate from entering initial safety screening (S1), independent of the efficacy evidence discussed above.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pyelonephritis) has no biologically plausible mechanistic link to zanamivir's known antiviral (neuraminidase-inhibiting) activity, no supporting clinical trials, and no supporting literature — the evidence pack itself classifies this as Evidence Level L5 with a "Hold" scoring recommendation. A second predicted indication in the same pack shows the same pattern (high score, irrelevant literature), suggesting the underlying signal is a graph-embedding artifact rather than a genuine repurposing candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the TFDA package insert for warnings/contraindications before any safety screening can begin
- Resolve DG002 (High): confirm zanamivir's mechanism of action via DrugBank API to formally document the mechanistic mismatch
- If this candidate is to be pursued further, independent confirmation of a plausible biological rationale (e.g., an off-target antibacterial or immunomodulatory effect) would be required, as none currently exists in the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

