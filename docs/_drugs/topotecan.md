---
layout: default
title: Topotecan
parent: High Evidence (L1-L2)
nav_order: 658
evidence_level: L2
indication_count: 10
---

# Topotecan
{: .fs-9 }

Tahap bukti: **L2** | Indikasi diramal: **10** 
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

# Topotecan: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Topotecan is a topoisomerase I inhibitor whose established Malaysian market presence covers oncology use (2 NPRA-registered products), though the specific approved indication text was not available in this dataset. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **5 clinical trials** and **20 publications** currently supporting this direction — but the evidence is still largely preclinical/early-phase, placing this candidate at a hypothesis-generating "Research Question" stage rather than a treatment-ready one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available Malaysia registration records (both license entries are missing indication text — see Malaysia Market Information below) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (pipeline-labeled "Research Question" / decision stage S2 — hypothesis worth further dedicated study, not yet actionable) |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data for topotecan was not returned by DrugBank in this pack (data gap DG002), but the evidence pack's own repurposing rationale identifies the mechanism directly: **Topotecan is a Topoisomerase I inhibitor** that stabilizes the Top1–DNA cleavage complex, inducing double-strand DNA breaks. This is a broad-spectrum cytotoxic mechanism shared across many solid tumors — it is not breast-cancer-specific by design.

What makes the breast cancer signal noteworthy is a more targeted hypothesis layered on top of that general mechanism: recent preclinical work (PMID 40300683, 2025) identifies **TFDP1** as a driver of triple-negative breast cancer (TNBC) proliferation and proposes topotecan as a therapeutic agent against TFDP1-driven, MYC-associated tumor biology — a potential synthetic-lethality relationship rather than simple mechanistic overlap with topotecan's approved gynecologic-oncology indications.

Clinically, this is not an entirely novel idea — topotecan has been directly tested in breast cancer before (e.g., the CALGB Phase II trial, PMID 10362325, and the TIME high-dose regimen, NCT00006032), but those efforts date to the 1990s–2000s, showed modest or inconsistent activity, and one of the more targeted regimens was terminated. The newer TNBC/TFDP1 mechanistic angle is what currently sustains interest, but it has not yet been tested prospectively in patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan + ifosfamide/mesna + etoposide) followed by autologous stem cell rescue in metastatic breast cancer — the most directly relevant trial (Grade A), but terminated |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's-choice single-agent chemotherapy in platinum-sensitive relapsed ovarian cancer (gBRCA-mutated); topotecan's role is likely only as a comparator/background option (Grade B, relevance uncertain) |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib triplet vs. other combinations/standard chemo in platinum-resistant recurrent ovarian/peritoneal/fallopian cancer; topotecan appears only as one possible chemo backbone agent (Grade B) |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with multiple standard chemo/immunotherapy regimens (including topotecan) in advanced malignancies — a safety/dose-finding study, not a topotecan efficacy trial (Grade B) |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid drug-screening platform (SCORE) for refractory solid tumors; an ex vivo screening method, not a clinical efficacy trial (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase 2 clinical trial | American Journal of Clinical Oncology | CALGB Phase II trial of topotecan monotherapy in advanced breast cancer patients previously treated with one prior regimen |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | International Journal of Biological Macromolecules | TFDP1 drives TNBC development via senescence suppression; proposed as a therapeutic target for topotecan |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot clinical study | Onkologie | Topotecan as primary chemotherapy for breast cancer brain metastases — pilot study |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase 1/2 trial | British Journal of Cancer | Continuous infusional topotecan in advanced breast cancer and NSCLC — no evidence of increased efficacy over standard dosing |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase 2 trial | Journal of Clinical Oncology | Paclitaxel + topotecan with G-CSF support in stage IV breast cancer |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan + pazopanib combination shows potent efficacy in preclinical models of primary/late-stage metastatic TNBC |
| [27444351](https://pubmed.ncbi.nlm.nih.gov/27444351/) | 2016 | Preclinical | Phytomedicine | MHP-1 restores topotecan sensitivity and inhibits metastasis via EMT/TGF-β regulation in breast cancer cells |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacological Research | Daidzein enhances topotecan's anticancer effect and reverses BCRP-mediated drug resistance in breast cancer |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | Preclinical | Journal of Surgical Research | Quercetin's effect on topotecan cytotoxicity in MCF-7 and MDA-MB-231 breast cancer cells |
| [10930538](https://pubmed.ncbi.nlm.nih.gov/10930538/) | 2000 | Preclinical | Biochemical Pharmacology | BCRP/MXR/ABCP transporter expression characterized in topotecan-resistant breast carcinoma cell lines |

---

## Malaysia Market Information

NPRA records confirm **2 registered licenses** for topotecan (market status: Marketed), but this evidence pack does not include the license numbers, product names, dosage forms, or approved indication text for either entry — these fields were returned empty and require direct extraction from NPRA product records or the package insert.

---

## Cytotoxicity

Topotecan is a cytotoxic antineoplastic agent (topoisomerase I inhibitor, camptothecin derivative), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — topoisomerase I inhibitor (camptothecin derivative) |
| Myelosuppression Risk | High — dose-limiting myelosuppression is well documented for topotecan; e.g., a Phase 2 germ cell tumor trial in this evidence pack (PMID 8617580) reported median nadir leukocyte count 1.75 ×10⁹/L, neutrophil count 1.55 ×10⁹/L, hemoglobin 8.75 g/dL, and platelet count 20,500/mm³ |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (given the documented myelosuppression risk); renal and hepatic function per standard cytotoxic monitoring practice — Malaysia-specific label requirements not available in this dataset |
| Handling Protection | Standard cytotoxic drug handling precautions apply; confirm specific protocol against the local NPRA package insert once available |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack — flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis (Top1 inhibition with potential synthetic lethality in TFDP1/MYC-driven TNBC) is biologically plausible and supported by recent preclinical work, but direct clinical evidence in breast cancer is dated, mostly early-phase or preclinical, and the most disease-matched regimen (TIME) was terminated. The evidence pack itself scores this at decision stage S2 with a "Research Question" label — appropriate for further investigation, not for advancing toward clinical or regulatory action yet.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data — warnings, contraindications, DDIs (Blocking gap, DG001)
- Confirmed DrugBank MOA and drug category classification (DG002)
- Complete Malaysia product registration details (license numbers, product names, approved indication text) for both registered products
- A prospective trial specifically testing topotecan in TNBC/TFDP1-driven breast cancer, since existing breast cancer trials predate and do not test this specific mechanistic hypothesis
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

