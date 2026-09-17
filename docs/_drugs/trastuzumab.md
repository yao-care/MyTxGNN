---
layout: default
title: Trastuzumab
parent: High Evidence (L1-L2)
nav_order: 662
evidence_level: L1
indication_count: 10
---

# Trastuzumab
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
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

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab is a humanized anti-HER2 monoclonal antibody established for HER2-positive breast cancer. The TxGNN model predicts it may also be effective in **progesterone-receptor (PR) positive breast cancer**, with **36 clinical trials** and **20 publications** identified in the evidence pack supporting this direction — though the mechanistic link runs through HER2 status rather than PR status itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (referenced across evidence-pack rationale as trastuzumab's established indication; explicit TFDA label text not returned in this data pull) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (Marketed) |
| Number of Registrations | 18 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Trastuzumab is a humanized IgG1 monoclonal antibody targeting the extracellular domain of HER2/neu (ErbB2). Its established pharmacological action is to inhibit proliferation of tumor cells that overexpress HER2 and to mediate antibody-dependent cell-mediated cytotoxicity (ADCC) — as reflected consistently in the evidence pack's clinical-trial titles (e.g., NCT01785420: "trastuzumab... acts extracellularly on the erbB-2 receptor... a potent mediator of antibody-dependent cell-mediated cytotoxicity").

The predicted new indication, PR-positive breast cancer, is not a distinct disease target for trastuzumab — it is a clinically common **subgroup of the existing HER2-positive breast cancer population**. Roughly a third of HER2-positive breast cancers co-express hormone receptors (ER and/or PR), and trastuzumab combined with endocrine therapy (e.g., letrozole, fulvestrant) is already used in this "triple receptor" population, as shown in trials such as NCT00134680 and NCT02152943 and in the translational study on "triple-positive breast cancer" (PMID 31410192).

**Important caveat from the evidence pack's own mechanistic analysis:** trastuzumab's pharmacological target is HER2, not PR. PR positivity is a co-existing biomarker used for treatment stratification (e.g., adding endocrine therapy), not the driver of trastuzumab's efficacy. Efficacy prediction should therefore continue to rely primarily on HER2 status, with PR status used only as a stratification variable — a distinction the evidence pack flags explicitly across multiple candidate rationales.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole + trastuzumab in ErbB2-positive, ER and/or PR-positive metastatic breast cancer — directly tests the trastuzumab + endocrine therapy combination in the PR+ population |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | Withdrawn (enrollment 0) | 0 | Planned RCT of trastuzumab ± tamoxifen in ER/PR-positive, HER2/neu-positive stage IV breast cancer; withdrawn before enrollment |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus + trastuzumab + letrozole in hormone-receptor and HER2-positive advanced breast cancer |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Neratinib + endocrine therapy + trastuzumab in ER-positive, HER2-positive cancers |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | Randomized neoadjuvant trial of lapatinib + trastuzumab ± endocrine therapy in HER2-overexpressing breast cancer (evidence-pack grade B: directly relevant, not PR-specific by design) |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | Neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab without chemotherapy in HR+ (ER+ and/or PR+), HER2+ localized breast cancer (evidence-pack grade B; small n limits strength) |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Randomized double-blind trial of BCD-178 vs. Perjeta as neoadjuvant therapy for HER2-positive breast cancer, ER/PR-negative subgroup (evidence-pack grade A; note population is PR-negative, included for adjacency) |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Randomized adjuvant trial comparing chemotherapy alone vs. chemotherapy + trastuzumab in node-positive/high-risk HER2-low breast cancer |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3,436 | Randomized adjuvant AC→paclitaxel ± trastuzumab in HER2-overexpressing, node-positive or high-risk breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Randomized first-line comparison of taxane + lapatinib vs. taxane + trastuzumab in HER2-positive metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT (Tier 1) | The Lancet. Oncology | monarcHER phase 2 RCT: abemaciclib + trastuzumab ± fulvestrant vs. chemotherapy + trastuzumab in HR-positive, HER2-positive advanced breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT, 5-year follow-up (Tier 1) | The Lancet. Oncology | NeoSphere trial: neoadjuvant pertuzumab + trastuzumab improves pathological complete response in HER2-positive breast cancer |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II randomized trial: endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemotherapy in HR-positive/HER2-positive early breast cancer |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (biosimilar equivalence) | British Journal of Cancer | Phase 3 equivalence trial of pertuzumab biosimilar + trastuzumab + docetaxel in HER2-positive, ER/PR-negative breast cancer |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | Phase 3 RCT | The Lancet. Oncology | ExteNET trial: neratinib after trastuzumab-based adjuvant therapy in HER2-positive breast cancer |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Retrospective cohort | BMC Cancer | Trastuzumab + fulvestrant combination therapy in hormone-receptor and HER2-positive advanced breast cancer |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohort/Translational (Tier 2) | Theranostics | Molecular portraits and trastuzumab responsiveness of ER+, PR+, HER2+ ("triple-positive") breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase 2 trial | Annals of Oncology | WSG-ADAPT HER2+/HR- trial: de-escalation with neoadjuvant trastuzumab + pertuzumab ± paclitaxel |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review (Tier 3) | Breast (Edinburgh) | Clinical implications of intrinsic molecular subtypes of breast cancer, including hormone-receptor/HER2 interplay |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacological Research | Targeted and cytotoxic inhibitors used in breast cancer treatment, stratified by HER2/HR/ER/PR status |

---

## Malaysia Market Information

Malaysia records **18 registered trastuzumab products** (market status: already marketed). However, the license-level details returned in this data pull (authorization numbers, product names, dosage forms, approved indication text) were all blank, so a per-product table cannot be populated from the current data set. This should be treated as an open data gap requiring a fresh NPRA license-level query.

---

## Cytotoxicity

Trastuzumab is an antineoplastic agent (anti-HER2 targeted therapy), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (humanized anti-HER2 monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack's TFDA warnings/contraindications field and drug interaction (DDI) query both returned no usable data (DDI query status: not found, 0 interactions).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The candidate reaches evidence level L1 (multiple completed Phase 3 RCTs, e.g., NCT01275677, NCT00005970) and the PR-positive subgroup already appears as a stratification arm in several existing HER2-positive breast cancer trials (NCT00134680, NCT02689921). However, the underlying mechanism operates through HER2 overexpression, not PR positivity — guardrails should require HER2-status confirmation alongside PR status before this is treated as an independent indication.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a blocking data gap — DG001)
- Confirmed mechanism-of-action documentation from DrugBank (currently a high-severity data gap — DG002)
- HER2-status stratified outcome data for the PR-positive subgroup, to confirm the biomarker relationship is stratification rather than a new drug–target mechanism
- Malaysia license-level detail (product names, dosage forms, approved indication text) via a re-run NPRA query, since the current 18 registrations returned no usable fields
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

