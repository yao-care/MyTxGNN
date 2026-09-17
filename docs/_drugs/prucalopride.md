---
layout: default
title: Prucalopride
parent: Low Evidence (L4-L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Prucalopride
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Prucalopride: From Chronic Constipation to Hypoalphalipoproteinemia

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist used clinically for chronic constipation via gut prokinetic action (per mechanistic context noted elsewhere in this evidence pack). The TxGNN model's top-ranked prediction is **Hypoalphalipoproteinemia** (low HDL-cholesterol disorder), but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the model's own annotation explicitly notes no known biological link between 5-HT4 agonism and lipoprotein metabolism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Taiwan license text; chronic constipation noted as prucalopride's established clinical use elsewhere in this evidence pack |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for prucalopride is not available (DrugBank MOA lookup is an open data gap in this pack). Based on the pharmacological context referenced elsewhere in this evidence pack, prucalopride acts as a selective 5-HT4 receptor agonist and is used clinically to promote gut motility.

Hypoalphalipoproteinemia is a lipoprotein metabolism disorder characterized by low HDL-cholesterol, governed by pathways (e.g., LDL receptor, lipid transport, reverse cholesterol transport) that have no established connection to serotonergic gut motility signaling. The model's own repurposing rationale for this candidate states explicitly: *"5-HT4 受體致效劑與脂蛋白代謝、HDL 調控無已知機轉關聯，屬於缺乏生物學合理性之預測，無任何臨床或文獻證據支持"* (no known mechanistic link exists, and there is no supporting clinical or literature evidence). This is consistent with the score reflecting a graph-embedding association rather than a biologically grounded hypothesis, and with the L5 / Hold classification assigned by the scoring engine itself.

Two other candidates in this same prediction set — amyloidosis (rank 6) and primary amyloidosis (rank 9) — carry a more coherent mechanistic story (amyloid-related autonomic/GI dysmotility as a target for prokinetic symptom relief) and are backed by actual literature (L4, decision stage S1, "Research Question"). These may be more productive candidates for follow-up than the top-ranked but mechanistically unsupported hypoalphalipoproteinemia prediction.

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
| Not specified | Not specified | Not specified | Not specified |
| Not specified | Not specified | Not specified | Not specified |

Two active licenses are confirmed in the registry (total_licenses = 2, market_status = Marketed), but license number, product name, dosage form, and approved-indication text were not populated in this data pull.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are a documented Blocking-severity data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hypoalphalipoproteinemia) has no supporting clinical trials or literature (L5, evidence-model-only) and is explicitly flagged by the model's own rationale as lacking biological plausibility. Separately, TFDA label warnings/contraindications are a Blocking-severity data gap, meaning this candidate cannot even enter S1 safety screening regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — Blocking gap, required before any safety screening
- DrugBank mechanism-of-action data — needed for mechanistic-plausibility assessment
- Confirmed license text (product name, dosage form, approved indication) for the 2 Taiwan registrations
- Consider redirecting evaluation effort to the amyloidosis / primary amyloidosis candidates (rank 6 and 9) in this same prediction set, which have actual literature support and a more coherent mechanistic rationale
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

