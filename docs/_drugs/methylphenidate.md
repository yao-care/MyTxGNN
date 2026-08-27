---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 4
---

# Methylphenidate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Methylphenidate: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

> Methylphenidate is a dopamine/norepinephrine reuptake inhibitor long used to treat Attention-Deficit/Hyperactivity Disorder (ADHD).
> TxGNN's top-ranked prediction for this drug is **Faciodigitogenital Syndrome (Aarskog Syndrome)**, a rare FGD1-gene skeletal developmental disorder,
> but this candidate is currently supported by **zero clinical trials** and **zero publications** — the model's own rationale flags it as likely knowledge-graph noise rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) — inferred from clinical evidence within this pack (e.g. NCT04647500); formal NPRA label text was not retrievable |
| Predicted New Indication | Faciodigitogenital Syndrome (Aarskog Syndrome) |
| TxGNN Prediction Score | 99.998% (rank 84 among all predictions) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed（已上市） |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data is flagged as a data gap in this pack (DG002). Based on the mechanistic notes embedded in TxGNN's own rationale text, methylphenidate acts primarily as a dopamine/norepinephrine reuptake inhibitor, increasing prefrontal cortical catecholaminergic signaling — the basis for its established use in ADHD.

Faciodigitogenital syndrome (Aarskog syndrome) is a genetic connective-tissue/skeletal developmental disorder caused by FGD1 mutations, affecting facial, digital, and genital morphogenesis through Rho-GTPase signaling pathways unrelated to monoamine transporters. There is no known pathophysiological overlap between this condition and methylphenidate's catecholaminergic mechanism.

The evidence pack's own repurposing rationale for this candidate explicitly states there is no identifiable mechanistic link, and attributes the unusually high TxGNN score to likely co-occurrence noise or indirect node relationships in the knowledge graph rather than a biologically grounded signal. This candidate should be treated as a model artifact pending manual review of the underlying knowledge-graph path, not as a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

NPRA records confirm 11 active registrations for methylphenidate in Malaysia (market status: 已上市), but individual license details (authorization number, product name, dosage form, approved indication text) were not returned by the data source and are not available to populate a per-license table at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no mechanistic rationale, no clinical trial evidence, and no literature support — the drug's own evidence pack explicitly characterizes the high TxGNN score as probable knowledge-graph noise rather than a genuine signal. This does not meet the threshold for further investment.

**To proceed, the following is needed:**
- Manual review of the TxGNN knowledge-graph path connecting methylphenidate to faciodigitogenital syndrome, to rule out a spurious node connection
- Formal DrugBank MOA data (DG002)
- TFDA/NPRA package insert warnings and contraindications (DG001, blocking — required before any S1 safety screening)
- Complete per-license Malaysia registration details (authorization numbers, indications)

**Note:** Two lower-ranked candidates in this pack — "specific developmental disorder" (rank 3, L2/S3, Proceed with Guardrails) and "dysthymic disorder" (rank 4, L4/S1) — carry substantially stronger clinical/literature support and may warrant separate evaluation, though the rank-3 candidate overlaps heavily with methylphenidate's existing ADHD indication and is not a novel repurposing target.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

