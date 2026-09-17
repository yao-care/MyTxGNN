---
layout: default
title: Temozolomide
parent: High Evidence (L1-L2)
nav_order: 639
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **2** 
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

# Temozolomide: From Unrecorded Original Indication to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide (DrugBank DB00853) is an orally administered alkylating agent marketed in Malaysia under 5 registrations, though the specific approved indication text was not captured in this evidence pack. The TxGNN model predicts it may be effective for **Adult Astrocytic Tumour**, a prediction already strongly corroborated by real-world oncology practice, with **2 clinical trials** and **10+ prioritized publications** (including multiple completed Phase 3 RCTs) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — TFDA/NPRA license records did not include approved indication text (data gap) |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from the standard drug reference is not available in this evidence pack (flagged as a High-severity data gap). Based on the reviewer's mechanistic assessment, temozolomide is an oral imidazotetrazine alkylating agent that crosses the blood-brain barrier and induces tumour cell apoptosis via DNA methylation at the O6-guanine position — a mechanism well documented in the oncology literature as the pharmacological basis for treating astrocytic tumours.

Although the original approved indication text for the Malaysian registrations could not be extracted (likely a data-collection gap in the TFDA/NPRA source rather than an actual absence of an approved use), the supporting clinical and literature evidence is unambiguous: temozolomide combined with radiotherapy (the Stupp protocol) is already the internationally recognized standard of care for glioblastoma and other high-grade astrocytic tumours. This means the TxGNN prediction is not identifying a novel mechanistic hypothesis so much as confirming an already well-established clinical use — which explains the very high prediction score (99.36%) and the L1 evidence tier.

Given this, the primary evaluation task is less about efficacy plausibility and more about closing the administrative/regulatory data gaps (original indication text, package insert warnings) so this established use can be formally documented against the Malaysian registration.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomized comparison of temozolomide alone vs. PCV (procarbazine, lomustine, vincristine) in recurrent WHO Grade III/IV astrocytic tumours |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib) combined with temozolomide and radiotherapy in newly diagnosed glioblastoma; primarily a safety/PK study of the combination, not TMZ monotherapy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark EORTC-NCIC trial establishing concomitant + adjuvant temozolomide with radiotherapy as standard of care for newly diagnosed glioblastoma |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | 5-year follow-up of the EORTC-NCIC trial confirming durable survival benefit of temozolomide + radiotherapy |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 trial: dose-dense temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Randomized trial of bevacizumab added to standard temozolomide + radiotherapy in newly diagnosed glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumor-Treating Fields plus maintenance temozolomide vs. temozolomide alone in glioblastoma |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | RCT | J Neurooncol | Concurrent radiotherapy plus temozolomide followed by 13-cis-retinoic acid maintenance in anaplastic astrocytic gliomas |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 Phase 3 trial: lomustine-temozolomide combination vs. standard temozolomide in MGMT-methylated glioblastoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG Oncology BN007 Phase II/III trial of dual immune checkpoint blockade in MGMT-unmethylated glioblastoma (temozolomide-containing standard arm) |
| [41345097](https://pubmed.ncbi.nlm.nih.gov/41345097/) | 2025 | Phase Ib/II trial | Nat Commun | GEINO 1602 trial: glasdegib added to standard temozolomide + radiotherapy (Stupp regimen) in newly diagnosed glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Overview of glioblastoma and other primary adult brain malignancies, including current treatment standards |

## Malaysia Market Information

License detail records (product name, dosage form, manufacturer, approved indication text) were not captured for any of the 5 registered temozolomide products in this evidence pack — only the aggregate count and "Marketed (Marketed)" status are on file. Detailed license extraction is required before this table can be populated.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) — based on the drug's DNA-methylating mechanism |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence is strong — multiple completed Phase 3 RCTs (including the landmark Stupp EORTC-NCIC trial and its 5-year follow-up) establish temozolomide as a de facto standard therapy for astrocytic tumours, supporting the L1 evidence tier. However, a Blocking-severity data gap on TFDA package insert warnings/contraindications (DG001) prevents a complete Stage 1 safety review, so the candidate cannot yet advance to unconditional Go.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the Blocking data gap before safety sign-off
- DrugBank-sourced mechanism of action and drug categories — currently unavailable, needed for formal MOA documentation
- Original approved indication text for the 5 Malaysian license entries — needed to confirm whether astrocytic tumour use is already covered under the existing registration or requires a label update
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

