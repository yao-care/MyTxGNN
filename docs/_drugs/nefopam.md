---
layout: default
title: Nefopam
parent: 僅模型預測 (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: From General Analgesia to Postoperative Pain Control in Lumbar Spinal Stenosis Surgery

## One-Sentence Summary

> Nefopam is a non-opioid, centrally acting analgesic already marketed in Malaysia for general pain control.
> Among the TxGNN model's predictions, the only candidate supported by actual clinical evidence is **Lumbar Spinal Stenosis** — specifically as an adjunct for postoperative pain and dysesthesia after spine surgery —
> backed by **1 randomized controlled trial** and **3 publications** (one of which is a serious safety signal, not efficacy evidence).

**Note on ranking:** TxGNN's top 9 predictions (immature/mature/diabetic/senile cataract subtypes, etc.) all scored ~99.98% with zero supporting trials or literature. The evidence pack itself flags these as a knowledge-graph clustering artifact — nine near-identical cataract subtypes scoring almost identically, with no plausible mechanistic link between a monoamine-reuptake analgesic and lens pathology. This report therefore treats **Lumbar Spinal Stenosis (rank 10)** — the only prediction with real trial/literature support — as the substantive candidate, and excludes the cataract cluster from further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General analgesia (non-opioid centrally acting analgesic) — specific NPRA-approved label text not available in source data |
| Predicted New Indication | Lumbar Spinal Stenosis (postoperative pain/dysesthesia control) |
| TxGNN Prediction Score | 99.97% (rank 803 among all candidates) |
| Evidence Level | L3 (single RCT + case report + cohort study; no completed Phase 2/3 RCT registered for this specific indication) |
| Malaysia Market Status | Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Nefopam is a centrally acting monoamine reuptake inhibitor (serotonin/norepinephrine/dopamine), clinically known for analgesic and anti-shivering/anti-tremor effects. Detailed formal mechanism-of-action documentation was not available in this evidence pack (flagged as a Blocking-severity data gap), but the repurposing rationale attached to the top literature-backed candidate describes this mechanism consistently across sources.

The link to lumbar spinal stenosis is not disease-modifying — nefopam does not act on the pathology of spinal canal narrowing itself. Rather, it is already used off-label/adjunctively in multimodal postoperative analgesia protocols following spine surgery, including decompression for lumbar spinal stenosis, by modulating pain signaling at the spinal cord/brainstem level. This is a **symptomatic perioperative pain-control use**, not a treatment for the underlying stenosis.

This distinction matters for decision-making: the evidence supports "nefopam as a postoperative analgesic adjunct in LSS surgery patients," not "nefopam treats lumbar spinal stenosis." The recommendation and any future development plan should be scoped accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for this indication. (The supporting RCT below was identified through PubMed as a journal-published trial, not a registry entry.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | RCT | Journal of Clinical Medicine | Double-blind RCT (n=73) in LSS spine surgery patients: intraoperative nefopam 20 mg reduced postoperative dysesthesia and pain, improved satisfaction vs. saline control |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Cohort | Zhurnal Voprosy Neirokhirurgii im. N.N. Burdenko | Compared multimodal analgesia regimens (incl. nefopam) in spinal stenosis surgery patients; assessed effect on failed back surgery syndrome rate |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Case Report | Journal of Korean Neurosurgical Society | **Safety signal**: status epilepticus in a 71-year-old LSS surgery patient following IV nefopam among a multi-drug analgesic regimen |

---

## Malaysia Market Information

Nefopam is recorded as **marketed** in Malaysia with **1 registered license**, but the source data does not include the license number, product name, dosage form, or approved indication text for this registration — these fields were returned blank by NPRA and could not be populated here.

---

## Safety Considerations

Formal label-derived warnings, contraindications, and drug interaction data were not available for this drug (flagged as a Blocking-severity data gap — this also means a formal S1 safety pre-assessment cannot be completed). Please refer to the package insert for safety information.

**Additional signal from literature (not label data):** one case report ([PMID 25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/)) describes status epilepticus temporally associated with IV nefopam administration in a spine-surgery patient receiving concurrent analgesics. This is a single case within a polypharmacy context and does not establish causality, but it should be tracked explicitly given nefopam's known seizure-risk class signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature-supported candidate (lumbar spinal stenosis) is backed by a single moderate-sized RCT (n=73) showing symptomatic postoperative benefit, not disease-modifying efficacy, and a documented seizure-risk safety signal. Critically, the formal NPRA label (warnings/contraindications) is a Blocking data gap, so the mandatory S1 safety pre-assessment cannot yet be completed.

**To proceed, the following is needed:**
- NPRA product label/insert (warnings, contraindications) — resolves DG001, required before any S1 safety sign-off
- Confirmed mechanism-of-action documentation from DrugBank — resolves DG002
- Larger/replication RCT data specifically in LSS postoperative pain, ideally with seizure/neuropsychiatric adverse event monitoring
- Explicit scoping decision: pursue as "postoperative analgesic adjunct in spine surgery" (symptomatic use) rather than "treatment for lumbar spinal stenosis" (disease-modifying), to avoid overstating the indication
- DDI review, since current DDI query returned no data (not confirmed absence of interactions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

