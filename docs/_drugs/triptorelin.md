---
layout: default
title: Triptorelin
parent: 僅模型預測 (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

Using the evidence pack as provided (no coding needed for this task—straight report authoring per the fixed template).

# Triptorelin: From Precocious Puberty to Hypertrichosis

## One-Sentence Summary

Triptorelin is a GnRH agonist already used clinically for precocious puberty (confirmed within this evidence pack by strong Phase 3 trial data under a different candidate entry). The TxGNN model's top-ranked new signal is **Hypertrichosis (disease)**, but this prediction is supported by only **1 tangentially related case report** and **0 clinical trials**, and the reviewers' own annotation flags it as likely model noise rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Precocious puberty (GnRH agonist; confirmed in this evidence pack's rationale notes — Malaysia license indication text was not returned) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Triptorelin is not available in this evidence pack. Triptorelin is known to work as a GnRH agonist, chronically suppressing pituitary LH/FSH release — a mechanism with no established link to hair follicle growth regulation.

The only literature record returned for this candidate (PMID 41822646) does not actually study Triptorelin's effect on hypertrichosis. It describes a transgender woman on **ciclosporin**, estradiol, and triptorelin who developed generalised hypertrichosis attributed to the ciclosporin, with triptorelin only present as a concurrent background medication. There is no causal or mechanistic claim in this source connecting Triptorelin itself to hair growth.

Given the absence of any clinical trials, any disease-specific mechanistic hypothesis, and a single case report that does not actually implicate the drug, this candidate should be treated as a likely knowledge-graph false positive rather than a credible repurposing lead — consistent with the model's own evidence-level scoring (L5) and Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case report | Cureus | Describes ciclosporin-induced generalised hypertrichosis in a transgender woman concurrently receiving triptorelin and estradiol; the hypertrichosis is attributed to ciclosporin, not to triptorelin — the drug appears only as background co-medication. |

---

## Malaysia Market Information

Triptorelin is recorded as marketed in Malaysia with 6 total registrations, but the evidence pack did not return license numbers, product names, dosage forms, or approved indication text for any of the entries — no market license table can be produced from the current data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Hypertrichosis prediction rests on a top TxGNN score but zero supportive clinical trials and one case report that does not actually implicate Triptorelin in hair growth — this is evidence level L5 (model prediction only), and the underlying mechanistic story (GnRH-axis suppression → hypertrichosis) has no established basis.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently missing — flagged as a blocking gap)
- Confirmed mechanism of action data (currently missing — high-severity gap)
- Malaysia license details (product names, dosage forms, approved indication text) to characterize current marketed use
- A specific, testable mechanistic hypothesis linking GnRH agonism to hair follicle biology before any further evidence collection is warranted
- If this candidate remains of interest, dedicated literature/trial searches specifically querying "Triptorelin AND hypertrichosis/hirsutism" mechanisms rather than relying on the single incidental case report currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

