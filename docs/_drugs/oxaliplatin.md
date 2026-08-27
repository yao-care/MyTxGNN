---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 524
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a third-generation platinum-based cytotoxic agent, most widely known as a backbone of colorectal cancer chemotherapy regimens (e.g., FOLFOX).
The TxGNN model predicts it may also be effective for **Malignant Pleural Mesothelioma**,
with **5 clinical trials** and **20 publications** currently supporting this direction.

*Note: The evidence pack did not contain TFDA/NPRA license text specifying the locally approved indication, so "Colorectal Cancer" above reflects oxaliplatin's well-established original indication rather than pack-sourced regulatory text.*

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (general drug knowledge; local license indication text not available in evidence pack) |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 9 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not available in this evidence pack (marked as a High-severity data gap). Based on the drug-repurposing rationale attached to this prediction, oxaliplatin is a third-generation platinum compound that works by forming DNA inter-strand and intra-strand cross-links, inhibiting DNA replication and transcription and inducing apoptosis. This cytotoxic mechanism has broad activity across multiple solid tumor types, not just its original indication.

Colorectal cancer and malignant pleural mesothelioma (MPM) are pharmacologically connected through this shared cytotoxic mechanism. When combined with agents like gemcitabine (nucleotide synthesis inhibitor) or raltitrexed (thymidylate synthase/antifolate inhibitor), oxaliplatin's DNA cross-linking is mechanistically complementary — the combination pairs DNA-synthesis suppression with direct DNA damage. Multiple Phase 2 single-arm trials have already demonstrated activity of these oxaliplatin combinations in MPM, representing a form of repurposing already tested in clinical practice, though not yet confirmed by a Phase 3 RCT.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin + gemcitabine as first- or second-line therapy in pleural/peritoneal mesothelioma; core direct evidence for this drug-disease pair |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib (Velcade) + oxaliplatin (Eloxatin) in previously treated pleural/peritoneal mesothelioma |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1000 | International registry of Pressurized IntraPeritoneal/IntraThoracic Aerosol Chemotherapy (PIPAC/PITAC) for malignant pleural/peritoneal disease; not oxaliplatin-specific, indirect relevance |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | Dose-escalation study of NX-1607 (CBL-B inhibitor) in advanced malignancies including MPM cohort; investigational drug unrelated to oxaliplatin |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Neoadjuvant cadonilimab + chemotherapy in gastroesophageal junction/gastric cancer; disease mismatch, low relevance |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase 2 trial | Tumori | Pilot study of oxaliplatin + raltitrexed in inoperable MPM, following earlier signal of activity in a Phase 1 study |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 trial (multicenter) | Clinical Lung Cancer | Multicenter trial of gemcitabine + oxaliplatin (25 patients) evaluating activity in MPM |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 trial | Journal of Clinical Oncology | Raltitrexed + oxaliplatin in 70 chemo-naive/pretreated diffuse MPM patients |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase 2/retrospective | J Occup Med Toxicol | Gemcitabine ± oxaliplatin in pemetrexed-pretreated MPM patients; efficacy/safety observational data |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 trial | Lung Cancer | Vinorelbine + oxaliplatin as first-line therapy in untreated MPM |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 trial | Lung Cancer | Raltitrexed-oxaliplatin as second-line MPM therapy; trial closed early due to no objective responses |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Institutional review | European Journal of Cancer | Institut Gustave Roussy 9-year experience across 7 chemo/chemo-immunotherapy trials in mesothelioma, including raltitrexed-oxaliplatin |
| [26526504](https://pubmed.ncbi.nlm.nih.gov/26526504/) | 2015 | Review | Cancer Treatment Reviews | Reviews therapeutic landscape of MPM, noting pemetrexed-platinum as standard first-line care |
| [12601280](https://pubmed.ncbi.nlm.nih.gov/12601280/) | 2003 | Review | Current Opinion in Oncology | Summarizes chemotherapy trial outcomes in MPM, including raltitrexed-oxaliplatin combinations |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sciences | Reviews immunomodulatory effects of chemo agents including oxaliplatin, to inform combination with immune checkpoint blockade in MPM |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum-based agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions; cytotoxic drug handling regulations generally apply to platinum agents |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 single-arm trials and a substantial literature base (20 publications) support oxaliplatin-based combinations' activity in MPM, but no Phase 3 RCT confirms efficacy, and this candidate's Evidence Level is L2. Critically, TFDA warning/contraindication data is a **Blocking** data gap that must be resolved before any safety-stage (S1) review can proceed.

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — currently blocking (DG001)
- Confirmed DrugBank mechanism-of-action detail — currently a High-severity gap (DG002)
- Local (Malaysia/Taiwan) approved indication text from license records, which was empty in this evidence pack
- Route-of-administration compatibility assessment (currently marked "pending" in the evidence pack)
- Ideally, a randomized Phase 3 trial or systematic review/meta-analysis to move beyond L2 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

