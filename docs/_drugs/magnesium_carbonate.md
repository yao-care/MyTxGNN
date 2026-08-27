---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

# Magnesium Carbonate: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium carbonate (DrugBank DB09481) is a long-established antacid compound; formal original-indication text is not available in the current Malaysia NPRA licensing data, but its acid-neutralizing pharmacology is well known. The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **0 clinical trials** and **4 supporting publications** (three RCTs, one analytical study) currently identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA licensing records provided (all `approved_indication_text` fields are empty); commonly used pharmacologically as an antacid for hyperacidity/dyspepsia |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 34 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known pharmacology, magnesium carbonate is a base/antacid compound that reacts with hydrochloric acid in the stomach to neutralize gastric acid and raise intragastric pH; it has long been used clinically for hyperacidity, dyspepsia, and as a component of combination antacid products.

Active peptic ulcer disease is fundamentally an acid-related mucosal injury — the ulcer bed is exposed to gastric acid, which impairs healing and drives symptoms. Since antacids reduce acid exposure at the ulcer surface, there is a direct and long-recognized mechanistic link between magnesium-based antacids and peptic ulcer management, predating the era of H2-blockers and proton pump inhibitors.

This mechanistic plausibility is reinforced by the retrieved literature: several controlled trials from the 1980s directly evaluated antacid regimens (including magnesium-containing formulations) in patients with active duodenal and prepyloric ulcers, generally showing healing rates comparable to (though sometimes below) H2-antagonists such as cimetidine. This supports a real, if historically dated, evidence base rather than a purely computational artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | 12-week double-blind trial in 72 patients with duodenal/prepyloric ulcers comparing cimetidine, antacid/anticholinergic combination, and placebo; 3-week healing rates were 67% (cimetidine) and 50% (antacid), both significantly better than placebo |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scandinavian Journal of Gastroenterology. Supplement | Companion report evaluating antacid/anticholinergic vs. cimetidine vs. placebo in active prepyloric and duodenal ulcers |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | 80 patients with active duodenal ulcer received antacid tablets (1.1 g, four times daily) alongside high- or low-fiber diets; ulcer healing occurred in 67.5% vs. 60% of patients respectively, confirming antacid efficacy independent of fiber intake |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro/analytical study | Medicine and Pharmacy Reports | Evaluated the acid-neutralizing capacity (ANC) and other physicochemical properties of marketed antacid products |

---

## Malaysia Market Information

Detailed per-license information (license number, product name, dosage form, approved indication text) was not returned in the current evidence pack — all five sampled license records contain empty fields. NPRA data confirms the drug is **marketed** in Malaysia with **34 total registrations**, but a data pull for the specific license details is required before this table can be completed.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The evidence pack flags TFDA/NPRA package-insert warnings and contraindications (DG001) as a **Blocking**-severity data gap — this information must be obtained before the candidate can proceed to the S1 safety review stage.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction is mechanistically well-grounded (acid neutralization directly addresses ulcer pathophysiology) and is supported by multiple historical RCTs (L2 evidence) demonstrating antacid efficacy in active peptic ulcer healing. However, mechanism-of-action data and TFDA/NPRA safety warnings are currently missing, and no indication-specific clinical trials have been identified, so the candidate should advance cautiously rather than proceed unconditionally.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001 — Blocking; required to complete the S1 safety review)
- Formal mechanism of action documentation from DrugBank or product labeling (DG002)
- Confirmed original indication text from complete NPRA license records (current sample records are empty)
- Detailed Malaysia licensing information (license numbers, product names, dosage forms, manufacturers) for the 34 registered products
- Consideration of whether the largely pre-1990 RCT evidence base warrants a contemporary confirmatory study, given that antacids have since been superseded by H2-blockers/PPIs as first-line ulcer therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

