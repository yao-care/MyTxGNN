---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: HER2-Positive Breast Carcinoma — Approved Indication Re-Identified, Not a Novel Repurposing Signal

## One-Sentence Summary

Pertuzumab (Perjeta) is a HER2-targeted monoclonal antibody; this evidence pack contains no captured record of its originally approved indication or mechanism of action (both flagged as data gaps).
The TxGNN model's top-ranked prediction is **HER2 Positive Breast Carcinoma** (score 99.97%), but the evidence pack's own rationale states this is **not a new hypothesis** — it is pertuzumab's existing, already-approved core indication, supported by **50 clinical trials queried** (10 shown) and **20 publications**, including landmark trials (CLEOPATRA, APHINITY, NeoSphere).
Ranks 2–5 are HER2+ breast cancer molecular-subtype labels (not independent new diseases), while ranks 6–10 are unrelated rare tumors with zero trials or literature — likely knowledge-graph noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this data pull (NPRA license fields empty; `original_indications` empty) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.97% (rank 830 in full candidate list) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 3 |
| Recommended Decision | Hold — pending data-gap remediation (see Conclusion) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned by DrugBank for this run (Data Gap DG002, High severity), and no original-indication text was captured from the Malaysia NPRA registration records either (all three license entries have empty fields). Based on what the evidence pack itself states, however, TxGNN's top-ranked prediction — HER2-positive breast carcinoma — is **not a genuinely novel hypothesis**: the pack's own `repurposing_rationale` for rank 1 explicitly notes that this is pertuzumab's core, already-approved use (marketed as Perjeta, given with trastuzumab and taxane/docetaxel chemotherapy to block HER2 dimerization). The knowledge-graph model appears to have re-identified an existing drug–disease edge rather than discovered a new one, and the pack recommends labeling it "approved use" rather than a repurposing candidate to avoid misleading interpretation.

This matters for the remaining ranked predictions too. Ranks 2–5 (progesterone-receptor-positive breast cancer, normal breast-like subtype, progesterone-receptor-negative breast cancer, luminal A/B breast cancer) are **not independent new indications** — they are molecular-subtype labels that already sit inside the broader HER2-positive breast cancer population pertuzumab is approved for. Their supporting trials are the same pertuzumab regimen trials (NeoSphere, DECRESCENDO, QL1209 biosimilar studies, etc.), stratified by hormone-receptor status rather than testing a distinct disease.

Only ranks 6–10 (ectomesenchymoma, malignant cutaneous granular cell skin tumor, HHV-8-related tumor, middle ear neuroendocrine tumor, prostatic urethra urothelial carcinoma) represent genuinely different disease entities. All five have **zero clinical trials and zero literature** in this pack, and their own rationale text describes them as likely knowledge-graph embedding noise rather than plausible biology — except prostatic urethra urothelial carcinoma, which the pack flags as having *some* biological plausibility (occasional HER2 overexpression in urothelial carcinoma) but currently no direct evidence.

## Clinical Trial Evidence

(For predicted indication rank 1: HER2 Positive Breast Carcinoma; 10 of 50 queried trials shown, prioritized by relevance grade and Phase 3/completed status)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03199885](https://clinicaltrials.gov/study/NCT03199885) | Phase 3 | Completed | 190 | Taxane/trastuzumab/pertuzumab ± atezolizumab as first-line therapy for HER2+ metastatic breast cancer |
| [NCT01120184](https://clinicaltrials.gov/study/NCT01120184) | Phase 3 | Completed | 1,095 | MARIANNE: T-DM1 + pertuzumab vs. T-DM1 + placebo vs. trastuzumab + taxane, first-line HER2+ advanced/metastatic breast cancer |
| [NCT02402712](https://clinicaltrials.gov/study/NCT02402712) | Phase 3 | Completed | 418 | Safety/tolerability of subcutaneous Herceptin + IV Perjeta + docetaxel in HER2+ metastatic breast cancer |
| [NCT02896855](https://clinicaltrials.gov/study/NCT02896855) | Phase 3 | Completed | 243 | China RCT: pertuzumab + trastuzumab + docetaxel vs. placebo + trastuzumab + docetaxel, untreated HER2+ metastatic breast cancer |
| [NCT02586025](https://clinicaltrials.gov/study/NCT02586025) | Phase 3 | Completed | 329 | Asia-Pacific RCT: pertuzumab neoadjuvant + adjuvant vs. placebo in early/locally advanced HER2+ breast cancer |
| [NCT04858529](https://clinicaltrials.gov/study/NCT04858529) | Phase 3 | Unknown | 774 | neoCARHP: TCHP vs. THP neoadjuvant regimens compared for pCR in HER2+ breast cancer |
| [NCT04514419](https://clinicaltrials.gov/study/NCT04514419) | Phase 3 | Active, not recruiting | 408 | HS627 (biosimilar) vs. reference pertuzumab, neoadjuvant HER2+ breast cancer |
| [NCT06057610](https://clinicaltrials.gov/study/NCT06057610) | Phase 3 | Active, not recruiting | 868 | SHR-A1811 ± pertuzumab vs. trastuzumab + pertuzumab + docetaxel in HER2+ recurrent/metastatic breast cancer |
| [NCT03742986](https://clinicaltrials.gov/study/NCT03742986) | Phase 2 | Completed | 8 | Nivolumab + neoadjuvant chemotherapy in inflammatory breast cancer (pertuzumab not primary arm) |
| [NCT02605915](https://clinicaltrials.gov/study/NCT02605915) | Phase 1 | Completed | 98 | Atezolizumab + T-DM1 or + trastuzumab/pertuzumab: safety and PK in HER2+ breast cancer |

## Literature Evidence

(10 of 20 publications shown, RCTs prioritized)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23602601](https://pubmed.ncbi.nlm.nih.gov/23602601/) | 2013 | RCT | Lancet Oncology | CLEOPATRA — overall survival results, pertuzumab + trastuzumab + docetaxel in first-line HER2+ metastatic breast cancer |
| [23704196](https://pubmed.ncbi.nlm.nih.gov/23704196/) | 2013 | RCT | Annals of Oncology | TRYPHAENA — cardiac safety of neoadjuvant pertuzumab + trastuzumab with anthracycline-containing/free chemo |
| [29175149](https://pubmed.ncbi.nlm.nih.gov/29175149/) | 2018 | RCT | Lancet Oncology | KRISTINE — neoadjuvant trastuzumab/pertuzumab/chemo vs. T-DM1 + pertuzumab in HER2+ breast cancer |
| [33357420](https://pubmed.ncbi.nlm.nih.gov/33357420/) | 2021 | RCT | Lancet Oncology | FeDeriCa — non-inferiority of fixed-dose subcutaneous pertuzumab/trastuzumab vs. IV formulation |
| [33539215](https://pubmed.ncbi.nlm.nih.gov/33539215/) | 2021 | RCT | J Clin Oncol | APHINITY 6-year follow-up — adjuvant pertuzumab + trastuzumab improves invasive disease-free survival |
| [39612919](https://pubmed.ncbi.nlm.nih.gov/39612919/) | 2025 | RCT | Lancet Oncology | HELEN-006 — de-escalated weekly nab-paclitaxel vs. docetaxel/carboplatin, both with trastuzumab + pertuzumab |
| [22153890](https://pubmed.ncbi.nlm.nih.gov/22153890/) | 2012 | Cohort/RCT | Lancet Oncology | NeoSphere — neoadjuvant pertuzumab + trastuzumab ± docetaxel, efficacy and safety |
| [27939064](https://pubmed.ncbi.nlm.nih.gov/27939064/) | 2017 | Review | Lancet | HER2-positive breast cancer overview; pertuzumab approval basis (improved pCR with trastuzumab) |
| [32721042](https://pubmed.ncbi.nlm.nih.gov/32721042/) | 2020 | Review | Cancer | Novel HER2-targeted therapies for HER2+ metastatic breast cancer, including pertuzumab and ADCs |
| [38875362](https://pubmed.ncbi.nlm.nih.gov/38875362/) | 2024 | Review | Medicine | HER2/PI3K/AKT pathway review, context for trastuzumab/pertuzumab mechanism |

## Other TxGNN-Ranked Predictions (Ranks 2–10)

| Rank | Predicted Disease | Evidence Level | Recommendation | Note |
|------|------|------|------|------|
| 2 | Progesterone-receptor positive breast cancer | L2 | Proceed with Guardrails | Hormone-receptor subgroup within existing HER2+ population, not a distinct disease |
| 3 | Normal breast-like subtype of breast carcinoma | L4 | Research Question | No literature; trials are general HER2+ populations, not subtype-specific |
| 4 | Progesterone-receptor negative breast cancer | L2 | Proceed with Guardrails | Same as rank 2; PR status affects magnitude of pertuzumab benefit (PMID 37723497) |
| 5 | Breast tumor luminal A or B | L4 | Research Question | Luminal tumors are mostly HER2-negative; weak overlap, no direct literature |
| 6 | Ectomesenchymoma | L5 | Hold | Zero trials, zero literature; no known HER2 mechanism |
| 7 | Malignant cutaneous granular cell skin tumor | L5 | Hold | Zero trials, zero literature; no known HER2 mechanism |
| 8 | Human herpesvirus 8-related tumor | L5 | Hold | Viral pathogenesis, unrelated to HER2 pathway |
| 9 | Middle ear neuroendocrine tumor | L5 | Hold | Zero trials, zero literature; rare tumor, no HER2 link |
| 10 | Prostatic urethra urothelial carcinoma | L5 | Research Question | Biologically plausible (HER2 overexpression reported in some urothelial carcinoma) but zero direct evidence for pertuzumab |

## Malaysia Market Information

NPRA registration confirms **3 active licenses** and marketed status ("已上市"), but license-level fields (authorization number, product name, dosage form, approved indication text) were all returned empty in this data pull — this is not the same as zero registrations, just missing field-level detail that needs re-query.

## Cytotoxicity

Pertuzumab is an antineoplastic agent (HER2-directed monoclonal antibody used in breast cancer treatment), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody — not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI queries all returned no data in this evidence pack — DG001, Blocking severity.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two data gaps block a sound safety/regulatory judgment on this candidate package: TFDA/NPRA label warnings and contraindications are entirely missing (Blocking severity), and mechanism-of-action data is absent (High severity). More importantly, the top-ranked "prediction" (HER2-positive breast carcinoma) is, by the evidence pack's own analysis, pertuzumab's existing approved indication rather than a new repurposing opportunity — so this run does not yet surface a genuine, evidence-supported new-use candidate. Ranks 6–10 are unsupported (zero trials/literature) except rank 10, which is a plausible but entirely unevidenced research question.

**To proceed, the following is needed:**
- Retrieve NPRA package insert (warnings, contraindications, DDI) to close the blocking safety gap
- Retrieve DrugBank MOA and drug categories to confirm targeted-therapy classification and enable proper cytotoxicity/monitoring guidance
- Re-run the KG mapping to exclude pertuzumab's already-approved indication (and its HR-status subtypes) from the "candidate" list, so future outputs isolate genuinely novel hypotheses
- If prostatic urethra urothelial carcinoma is to be pursued as a research question, commission a targeted literature/trial search specifically for anti-HER2 therapy in HER2-overexpressing urothelial carcinoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

