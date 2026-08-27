---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is a nonsteroidal antiandrogen historically used in combined androgen blockade for (advanced) prostate cancer — a use extensively documented by trial data in this same evidence pack. The TxGNN model's top-ranked prediction points to **"Prostate Cancer/Brain Cancer Susceptibility"** (a genetic-susceptibility ontology node, not a clinical diagnosis), but currently **0 clinical trials** and **0 publications** support this specific pairing, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (advanced/metastatic — no TFDA/NPRA label text is available in this pack; use is confirmed indirectly via the 50 clinical trials retrieved under the related "male reproductive organ cancer" node) |
| Predicted New Indication | Prostate Cancer/Brain Cancer Susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is marked as a Data Gap in this evidence pack. However, literature attached to this drug elsewhere in the pack (PMID [8252497](https://pubmed.ncbi.nlm.nih.gov/8252497/), Labrie F, *Cancer*, 1993, "Mechanism of action and pure antiandrogenic properties of flutamide") confirms flutamide is a nonsteroidal, pure androgen-receptor antagonist used clinically in combined androgen blockade (with LHRH agonists) for prostate cancer — a use corroborated by dozens of Phase 2/3 trials also present in this pack.

The model's top-ranked candidate, however, is not a conventional new indication. "Prostate cancer/brain cancer susceptibility" combines a genetic-susceptibility ontology node with an unrelated cancer type that has no established link to androgen signaling. No clinical trials, ICTRP records, or PubMed literature were retrieved for this pairing (0/0/0), and the source annotation for this candidate itself flags it as a likely knowledge-graph label mismatch rather than a genuine mechanistic hypothesis, rather than a pharmacologically grounded lead.

Because flutamide's established mechanism (androgen receptor antagonism) does not extend in any documented way to brain tumour biology or hereditary cancer susceptibility, this specific top-ranked prediction does not currently meet the bar for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia records **1 registered license** for flutamide with market status **✓ Marketed**. However, license-level details (authorization number, product name, dosage form, approved indication text) are not available in this evidence pack.

---

## Cytotoxicity

Flutamide's original use in prostate cancer classifies it as antineoplastic, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (nonsteroidal antiandrogen; not conventional cytotoxic chemotherapy) |
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
The top-ranked prediction ("Prostate Cancer/Brain Cancer Susceptibility") has no supporting clinical trials, ICTRP records, or literature, and appears to be a knowledge-graph labeling artifact rather than a mechanistically grounded hypothesis (Evidence Level L5).

**To proceed, the following is needed:**
- TFDA/NPRA label data — warnings and contraindications (currently a Blocking data gap, DG001)
- DrugBank mechanism-of-action confirmation (DG002)
- Malaysia license details — product name, dosage form, full approved indication text
- If repurposing is still of interest, prioritize better-evidenced candidates already surfaced in this same TxGNN run instead of rank 1 — notably rank 6 "male reproductive organ cancer" (50 trials, 20 publications) and rank 4 "benign reproductive system neoplasm" (19 publications), both of which warrant their own separate scoring pass
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

