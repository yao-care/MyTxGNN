---
layout: default
title: Moxonidine
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Moxonidine
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

# MOXONIDINE: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Moxonidine is a centrally-acting antihypertensive (marketed in Malaysia in 3 registered products); its specific NPRA-approved indication text was not retrievable in this data set. The TxGNN model's top-ranked prediction is **Hypotrichosis Simplex of the Scalp**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the model's own generated rationale flags it as lacking biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (specific approved-indication text not available in license records) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for moxonidine is marked as a data gap in the structured record. However, the evidence pack's own repurposing-rationale notes describe moxonidine as a centrally-acting I1-imidazoline receptor / α2-adrenergic receptor agonist that suppresses sympathetic outflow via the nucleus tractus solitarius — consistent with its known use as an antihypertensive.

For the top-ranked candidate, hypotrichosis simplex of the scalp, the pack's rationale explicitly states there is no known pharmacological link between central sympathetic inhibition and hair-follicle keratinization or growth-cycle regulation. The high TxGNN score appears to be an artifact of embedding similarity rather than a biologically grounded signal, and no clinical or literature evidence was found to support it.

By contrast, two lower-ranked candidates in this same evidence pack — malignant renovascular hypertension (rank 5) and malignant hypertensive renal disease (rank 6) — carry a stronger mechanistic case: they extend moxonidine's established antihypertensive mechanism (reduced sympathetic tone and plasma renin activity) to a more severe hypertensive phenotype within the same drug class, and were scored L4 / "Research Question" rather than Hold. These may warrant more attention than the nominal top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Moxonidine has 3 active registrations in the Malaysia (NPRA) database (market status: 已上市 / Marketed). License number, product name, dosage form, and approved-indication text were not returned for any of the 3 records in this data set.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (hypotrichosis simplex of the scalp) has no clinical trial, literature, or mechanistic support — the model's own rationale text identifies it as an embedding-similarity artifact rather than a biologically plausible repurposing signal.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action (MOA) from DrugBank or equivalent source
- If pursuing this program, consider redirecting evaluation toward the mechanistically plausible candidates in this same pack — malignant renovascular hypertension and malignant hypertensive renal disease (rank 5–6, L4/"Research Question") — which still require dedicated clinical or preclinical evidence but have a coherent pharmacological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

