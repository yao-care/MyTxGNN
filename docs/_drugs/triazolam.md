---
layout: default
title: Triazolam
parent: 僅模型預測 (L5)
nav_order: 668
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Triazolam: From Insomnia to Insomnia — A Confirmatory Signal

## One-Sentence Summary

Triazolam is a short-acting triazolobenzodiazepine long used clinically as a hypnotic for insomnia. The TxGNN model predicts it is effective for **Insomnia (Sleep Disorder, Initiating and Maintaining Sleep)** — a signal that, per the underlying rationale, reflects the drug's *existing* approved use rather than a genuinely novel repurposing hypothesis. The prediction is backed by **20 publications** (including a major clinical practice guideline and two systematic reviews/meta-analyses), though **no dedicated clinical trials** for this specific prediction are currently registered.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (per repurposing rationale — described as the drug's existing, long-established approved use; not separately confirmed in the registry record) |
| Predicted New Indication | Insomnia (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Triazolam is a triazolobenzodiazepine that acts at the benzodiazepine binding site on the GABA-A receptor, positively and allosterically enhancing inhibitory GABAergic neurotransmission to produce sedative/hypnotic effects. This mechanism directly underlies its established clinical use for insomnia (difficulty initiating and maintaining sleep).

Because the predicted indication and the drug's real-world therapeutic use are the same condition, this case is best understood not as a novel drug-repurposing hypothesis but as a **model-confirmed validation** of triazolam's known clinical role. The evidence pack explicitly frames this as a compilation of existing clinical practice evidence rather than a new mechanistic leap.

Note: a structured mechanism-of-action (MOA) field for the drug record itself is currently unavailable (data gap); the mechanistic description above is drawn from the repurposing rationale rather than a dedicated MOA source.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical Practice Guideline | J Clin Sleep Med | AASM guideline on pharmacologic treatment of chronic insomnia in adults, evaluating individual hypnotic drugs including benzodiazepines |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Systematic Review/Meta-analysis | Psychiatry Clin Neurosci | Efficacy/safety of sleep medication classes (incl. benzodiazepines) as add-on therapy for MDD with insomnia symptoms |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic Review/Network Meta-analysis | Sleep | Comparative efficacy and safety of hypnotics for insomnia in older adults |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs & Aging | Recommendations for pharmacological management of insomnia in elderly patients |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Review | Minerva Medica | Overview of insomnia disorder diagnosis and management |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clinical Therapeutics | Safety and efficacy of sleep medicines in older adults |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Comparative Review | Ann Pharmacother | Comparison of zolpidem vs. triazolam on efficacy and safety |
| [10533351](https://pubmed.ncbi.nlm.nih.gov/10533351/) | 1999 | Review | J Am Pharm Assoc | Overview of pharmacologic and nonpharmacologic management of insomnia |
| [1679317](https://pubmed.ncbi.nlm.nih.gov/1679317/) | 1991 | Review | Ann Acad Med Singap | Review of hypnotic drug treatment for insomnia, including benzodiazepines |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | Pharmacology of benzodiazepine hypnotics, including triazolam's historical role |

---

## Malaysia Market Information

Malaysia registration is confirmed (1 license on file), but detailed product-level information (license number, product name, dosage form, approved indication text) is not currently populated in the dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Literature evidence is strong and consistent (a clinical practice guideline plus two systematic reviews/meta-analyses supporting benzodiazepine hypnotics, including triazolam, for insomnia), but this reflects confirmation of an existing use rather than a novel indication, and a blocking safety data gap (product leaflet warnings/contraindications) prevents completion of the initial safety screen.

**To proceed, the following is needed:**
- TFDA/regulatory leaflet data — warnings and contraindications (blocking; source: official regulatory site, method: retrieve and parse product leaflet PDF)
- Mechanism-of-action data for the drug record itself (source: DrugBank API query)
- Malaysia product-level registration details (license number, product name, dosage form, approved indication text)
- Clarification of whether this candidate should be scoped as "confirmatory evidence review" rather than a standard repurposing pipeline, given the predicted and existing indications overlap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

