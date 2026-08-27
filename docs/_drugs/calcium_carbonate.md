---
layout: default
title: Calcium Carbonate
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 5
---

# Calcium Carbonate
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

Using the evidence pack as provided (no fabrication of missing regulatory fields), here is the report:

---

# Calcium Carbonate: From Calcium Supplementation to Nephrocalcinosis

## One-Sentence Summary

> Calcium carbonate (DrugBank DB06724) is a widely marketed compound generally used as a calcium supplement, antacid, and phosphate binder, though the specific NPRA-approved indication text is not available in the current data extract.
> The TxGNN model nominally ranks **Nephrocalcinosis** as its top predicted association, but the prediction carries a **TxGNN score of 0.00%** and **0 supporting clinical trials** — the 20 retrieved publications largely describe calcium carbonate **causing** hypercalcemia/nephrocalcinosis as an adverse reaction, not treating it, suggesting this is a reversed safety signal rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from NPRA license extract (all license fields blank in source data); calcium carbonate is generally known as a calcium supplement / antacid / phosphate binder |
| Predicted New Indication | Nephrocalcinosis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 348 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap — DG002). Based on general pharmacological knowledge, calcium carbonate acts by dissociating into calcium and carbonate ions in the gastrointestinal tract, where it neutralizes gastric acid, supplements elemental calcium, and binds dietary phosphate in the gut lumen.

However, the evidence gathered for this candidate does **not** support a therapeutic rationale for nephrocalcinosis. Nephrocalcinosis is the pathological deposition of calcium salts in renal tissue — mechanistically, this is the *opposite* of what a repurposing candidate should demonstrate. The literature base is dominated by reports of calcium carbonate **inducing** hypercalcemia, medullary nephrocalcinosis, and milk-alkali syndrome, particularly with excessive or prolonged intake (e.g., PMID 9203205, PMID 2507975, PMID 885714, PMID 36146999). The single publication evaluating a genuine protective mechanism against oxalate-driven nephrocalcinosis (PMID 23228382) studied **lanthanum carbonate**, a different phosphate-binding compound, and cannot be directly extrapolated to calcium carbonate.

Combined with a TxGNN prediction score of 0.00 (i.e., no meaningful positive model signal) and zero clinical trials directly testing calcium carbonate for nephrocalcinosis, this candidate should be interpreted as a **drug-safety signal** (calcium carbonate as a cause of nephrocalcinosis) rather than a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9203205](https://pubmed.ncbi.nlm.nih.gov/9203205/) | 1997 | Case Report | Pediatric Nephrology | Severe hypercalcemia, renal failure, and medullary nephrocalcinosis secondary to calcium carbonate ingestion — direct adverse-reaction report |
| [885714](https://pubmed.ncbi.nlm.nih.gov/885714/) | 1977 | Case Report | Israel Journal of Medical Sciences | Renal tubular acidosis and focal tubular calcification from excessive calcium carbonate ingestion (milk-alkali syndrome) |
| [2507975](https://pubmed.ncbi.nlm.nih.gov/2507975/) | 1989 | Cohort/Safety Study | Nephrology Dialysis Transplantation | 68 children with chronic renal failure on calcium carbonate; 47 hypercalcemia episodes in 29 patients over ~20 months follow-up |
| [36146999](https://pubmed.ncbi.nlm.nih.gov/36146999/) | 2022 | Case Series | J Royal College of Physicians of Edinburgh | Two adult cases of hypercalcemia and acute kidney injury from prolonged self-medication with OTC calcium compounds |
| [8906632](https://pubmed.ncbi.nlm.nih.gov/8906632/) | 1996 | Animal Study | J Nutritional Science and Vitaminology | Compared calcium gluconate vs. calcium carbonate on magnesium utilization and nephrocalcinosis in magnesium-deficient rats |
| [7965206](https://pubmed.ncbi.nlm.nih.gov/7965206/) | 1994 | Animal Study | The Journal of Nutrition | Dietary calcium chloride vs. calcium carbonate in cats — calcium carbonate associated with higher urinary pH and kidney calcium deposition |
| [8967338](https://pubmed.ncbi.nlm.nih.gov/8967338/) | 1996 | Basic Science/Physiology | American Journal of Physiology | Modeled ion supersaturation along the rat nephron; calcium carbonate/phosphate supersaturation predicted in the loop of Henle |
| [5493536](https://pubmed.ncbi.nlm.nih.gov/5493536/) | 1970 | Animal Study | Clinical Science | Examined urinary pH, citrate, magnesium, and calcium in diet/acetazolamide-induced nephrocalcinosis in rats |
| [14531797](https://pubmed.ncbi.nlm.nih.gov/14531797/) | 2003 | Comparative Animal Study | Kidney International | Sevelamer associated with less nephrocalcinosis than calcium carbonate in long-term uremic rat model, despite similar phosphate control |
| [23228382](https://pubmed.ncbi.nlm.nih.gov/23228382/) | 2013 | Animal Study (different drug) | The Journal of Urology | Lanthanum carbonate (not calcium carbonate) inhibits intestinal oxalate absorption and prevents nephrocalcinosis after oxalate loading in rats |

---

## Malaysia Market Information

Calcium carbonate is currently **marketed in Malaysia** with **348 total NPRA registrations**. However, the license-level fields (authorization number, product name, dosage form, approved indication text) returned by the current NPRA data extract are blank for all sampled entries, so a detailed product-level breakdown cannot be presented at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/NPRA label warnings and contraindications for this drug are flagged as a Blocking-severity data gap — DG001 — and drug interaction data returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this candidate is 0.00, no clinical trials support calcium carbonate for nephrocalcinosis, and the retrieved literature predominantly describes calcium carbonate as a **cause** of hypercalcemia/nephrocalcinosis rather than a treatment for it — indicating this is likely a reversed or spurious association rather than a genuine repurposing signal. This is compounded by a Blocking-severity gap in safety/label data (DG001) and missing mechanism-of-action data (DG002).

**To proceed, the following is needed:**
- TFDA/NPRA label PDF retrieval and parsing for warnings and contraindications (DG001, Blocking)
- DrugBank mechanism-of-action query to support/refute mechanistic plausibility (DG002, High)
- Original NPRA license indication text (current extract returned blank fields despite 348 registrations)
- A re-evaluation of whether "nephrocalcinosis" should be treated as a repurposing candidate at all, given the directionality issue identified in the literature, or reclassified as a pharmacovigilance signal instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

