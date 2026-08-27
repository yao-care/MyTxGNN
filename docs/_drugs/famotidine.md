---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 5
---

# Famotidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Famotidine: From Peptic Ulcer Disease / GERD to Hyperinsulinism

## One-Sentence Summary

Famotidine is a histamine H2-receptor antagonist long established for acid-related gastrointestinal conditions (peptic ulcer disease, GERD/erosive esophagitis) — this is inferred from the evidence pack itself, where famotidine repeatedly appears as the standard comparator drug in these conditions, since Malaysia registration and original-indication fields were not populated in this dataset. TxGNN's top-ranked candidate, **Hyperinsulinism**, has a prediction score of **0%** and is supported by **0 clinical trials** and **0 publications**; the reviewer's own annotation flags it as likely database-matching noise with no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in registry data; famotidine is a well-established H2-receptor antagonist used for peptic ulcer disease and GERD/erosive esophagitis (inferred from its role as reference comparator throughout this evidence pack) |
| Predicted New Indication | Hyperinsulinism |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | 已上市 (Marketed) |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap in this evidence pack). Based on known pharmacology, famotidine acts as a selective histamine H2-receptor antagonist on parietal cells, reducing gastric acid secretion — a mechanism with no established connection to insulin secretion regulation.

The evidence pack's own mechanistic annotation for this candidate states directly: famotidine's H2-antagonism acts on gastric acid secretion and has no known mechanistic relationship to hyperinsulinism, and with a TxGNN score of 0.0 this pairing is most likely database-matching noise rather than a genuine repurposing signal.

Because the TxGNN score is 0 across all five candidates in this pack (including the better-evidenced ones below), the score field itself may not be reliably populated for this run — this should be verified against the raw model output before further use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Malaysia registry (NPRA) records 15 approved product licenses for Famotidine with market status "已上市" (Marketed). Individual license numbers, product names, dosage forms, and approved indication text were not populated in this evidence pack and would need to be pulled directly from NPRA records to complete this table.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Hyperinsulinism) has zero supporting trials, zero literature, a 0% model score, and an explicitly flagged absence of mechanistic plausibility — this does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed original approved indication text and DrugBank MOA data
- Verification of the TxGNN scoring pipeline, since all five candidates in this evidence pack returned a score of 0.0
- If hyperinsulinism is to be pursued further, a targeted literature/preclinical search specifically on H2-receptor antagonism and insulin secretion pathways, since none currently exists in this pack

**Note on other candidates in this evidence pack:** This dataset also contained four additional candidates — esophagitis, gastric ulcer, duodenal ulcer (each rank L1/S3, "Proceed with Guardrails," backed by multiple completed Phase 3 RCTs and dozens of publications), and gastrin secretion abnormality (L5/Hold, no evidence). However, the rationale text for esophagitis, gastric ulcer, and duodenal ulcer explicitly states these already reflect famotidine's established, approved-level indications rather than novel repurposing hypotheses — they are not "new" uses in the repurposing sense, which is why Hyperinsulinism (the nominal rank-1, genuinely novel candidate) was used as this report's headline despite its weak evidence. If the goal is to identify a viable repurposing candidate rather than document existing use, none of the five candidates in this pack currently qualifies — this evidence pack does not yet contain a credible new-indication signal for Famotidine.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

