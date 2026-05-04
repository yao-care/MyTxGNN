---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
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

# Alfacalcidol: From Renal Osteodystrophy to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol (1α-hydroxycholecalciferol) is a synthetic active vitamin D analog widely used for calcium-phosphate metabolic disorders, including renal osteodystrophy and various forms of hypoparathyroidism.
The TxGNN model predicts it may be effective for **Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion**, with a prediction score of **99.61%**; however, the evidence for this specific genetic subtype currently rests on mechanistic reasoning rather than dedicated clinical trials or publications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal osteodystrophy; calcium-phosphate metabolic disorders (individual product data not available from regulatory records) |
| Predicted New Indication | Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 — Mechanistic evidence; no dedicated clinical trials or publications identified |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alfacalcidol is a pro-drug that undergoes hepatic 25-hydroxylation to yield calcitriol (1,25-dihydroxycholecalciferol) — the biologically active form of vitamin D. Crucially, this hepatic activation pathway does **not** depend on renal 1α-hydroxylase, the enzyme whose activity is tightly controlled by parathyroid hormone (PTH). Detailed mechanism of action data from DrugBank was not retrievable for this analysis, but alfacalcidol's pharmacology is well established in the scientific literature.

In familial isolated hypoparathyroidism due to impaired PTH secretion, the root defect is insufficient PTH production from the parathyroid glands (caused by mutations in the *PTH* gene, *GCM2*, or related secretory machinery). Without adequate PTH signalling, renal 1α-hydroxylase activity falls, calcitriol synthesis drops, and patients develop chronic hypocalcaemia accompanied by neuromuscular irritability, tetany, and seizure risk. By supplying a ready-to-activate vitamin D precursor that bypasses this renal bottleneck entirely, alfacalcidol directly addresses the downstream metabolic deficit regardless of PTH status.

The repurposing logic is especially compelling because alfacalcidol is already the standard of care for other PTH-deficient states — post-surgical hypoparathyroidism, autoimmune hypoparathyroidism, and pseudohypoparathyroidism. Familial isolated hypoparathyroidism shares the identical downstream metabolic lesion (insufficient active vitamin D), making the mechanistic fit essentially complete (★★★★★). The primary gap is the absence of studies specifically enrolling patients with this rare, genetically confirmed subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for familial isolated hypoparathyroidism due to impaired PTH secretion.

---

## Literature Evidence

Currently no related literature available specifically for familial isolated hypoparathyroidism due to impaired PTH secretion.

> **Context note:** Supporting literature exists for closely related conditions sharing the same PTH-deficiency mechanism. Notably, 20 publications were identified for Dahlberg-Borer-Newcomer syndrome (HDR syndrome, also characterised by hypoparathyroidism), and 8 publications for renal tubular acidosis with alfacalcidol use — both providing indirect mechanistic support. Key examples from adjacent evidence are listed below for reference.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28993435](https://pubmed.ncbi.nlm.nih.gov/28993435/) | 2017 | Case Series | *Endocrine Connections* | Active vitamin D analogue is standard management for hypocalcaemia in children with hypoparathyroidism; intercurrent illness can destabilise calcium homeostasis, requiring dose adjustment |
| [31968342](https://pubmed.ncbi.nlm.nih.gov/31968342/) | 2020 | Clinical Study | *American Journal of Nephrology* | Patients with permanent post-surgical hypoparathyroidism require high calcium supplementation with vitamin D (including alfacalcidol) to maintain serum calcium; highlights hypercalcaemia risk as key monitoring point |
| [32580149](https://pubmed.ncbi.nlm.nih.gov/32580149/) | 2020 | Registry Study | *Endocrine Connections* | Russian registry of chronic hypoparathyroidism patients; active vitamin D derivatives including alfacalcidol are the principal treatment modality |
| [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) | 2001 | Case Report | *Internal Medicine (Tokyo)* | Alfacalcidol as part of a regimen achieving rapid bone mineralisation improvement in a patient with renal tubular acidosis type 1 and osteomalacia |
| [6893175](https://pubmed.ncbi.nlm.nih.gov/6893175/) | 1980 | Clinical Study | *Contributions to Nephrology* | 1α-OH-VD₃ (alfacalcidol) was 200–250 times more potent than vitamin D₂ in correcting calcium malabsorption in Fanconi syndrome; plasma calcitriol rose rapidly after administration |
| [6262039](https://pubmed.ncbi.nlm.nih.gov/6262039/) | 1981 | Review | *Drugs* | Comprehensive pharmacological review establishing alfacalcidol's role among active vitamin D compounds; efficacy in hypoparathyroidism explicitly reviewed |

---

## Malaysia Market Information

Individual product authorisation details were not available in the Evidence Pack for the 16 registered products. Alfacalcidol is confirmed as currently marketed in Malaysia with 16 active registrations.

For current product listings, refer to the [NPRA Drug Registration Database](https://npra.gov.my).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note:** Although formal safety data was not retrievable for this report, active vitamin D analogs carry well-recognised risks of **hypercalcaemia** and **hypercalciuria**, which are particularly relevant when used in hypoparathyroid patients requiring long-term supplementation. A monitoring protocol should be established before any clinical use. Package insert download and parsing is listed as a required next step.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alfacalcidol's PTH-independent mechanism of action maps directly onto the metabolic deficit caused by impaired PTH secretion, making this a scientifically compelling repurposing candidate. The absence of dedicated evidence for this specific genetic subtype reflects the disease's rarity, not a mechanistic mismatch — the drug is already standard of care in phenotypically identical conditions.

**To proceed, the following is needed:**

- **Safety data**: Download and parse the NPRA-approved package insert to extract contraindications, warnings (especially hypercalcaemia, hypercalciuria, renal calculi), drug interactions, and dose adjustment guidance
- **MOA confirmation**: Retrieve full mechanism of action data from DrugBank (DB01436) to formalise the pharmacological rationale for regulatory and clinical submissions
- **Evidence generation**: Initiate a case series or patient registry study enrolling individuals with genetically confirmed familial isolated hypoparathyroidism on alfacalcidol therapy; partner with rare endocrine disease networks (e.g., EUHYPO, Hypoparathyroidism Association)
- **Monitoring protocol**: Define calcium, phosphate, urinary calcium, PTH (if measurable), and renal function monitoring intervals — weekly during dose-titration phase, transitioning to monthly once stable
- **Regulatory pathway**: Consult NPRA regarding off-label prescribing documentation or orphan drug designation options for this rare endocrine condition (estimated prevalence < 1:100,000)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

