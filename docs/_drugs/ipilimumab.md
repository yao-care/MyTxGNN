---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ipilimumab: From Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Ipilimumab is an anti-CTLA-4 immune checkpoint inhibitor originally established for melanoma treatment. The TxGNN model predicts it may also be effective for **non-cutaneous melanoma** (e.g., uveal, mucosal subtypes), with **50 clinical trials** identified (10 assessed as directly relevant, including 2 completed Phase 3 studies) and **5 publications** currently supporting this direction. A second, much weaker signal — **choroideremia** — was also flagged by the model but shows no mechanistic, trial, or literature support and is treated separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma (cutaneous) — confirmed by drug-class rationale; structured NPRA license indication text not available in this evidence pack |
| Predicted New Indication | Non-Cutaneous Melanoma (uveal / mucosal melanoma) |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known drug class information, ipilimumab is an anti-CTLA-4 monoclonal antibody that blocks a T-cell inhibitory checkpoint, restoring antitumor immune activation. Its efficacy in cutaneous melanoma is well established and forms the pharmacological basis of its original approval.

Cutaneous and non-cutaneous melanoma (uveal, mucosal) share the same underlying tumor biology — melanocyte-derived malignancy with T-cell-mediated immune evasion — so the CTLA-4 blockade mechanism is directly applicable in principle. This is not really a cross-disease repurposing signal so much as a subgroup extrapolation: ipilimumab is already used clinically across melanoma subtypes.

The important caveat is that non-cutaneous subtypes — particularly uveal melanoma — are known to respond less robustly to CTLA-4/PD-1 blockade than cutaneous melanoma, due to differences in tumor mutational burden and immune microenvironment. The trial evidence below largely reflects general/cutaneous-predominant melanoma populations rather than non-cutaneous-specific cohorts, so the mechanistic plausibility is strong but the subtype-specific efficacy evidence is indirect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00324155](https://clinicaltrials.gov/study/NCT00324155) | Phase 3 | Completed | 681 | Pivotal MDX010-20 trial establishing ipilimumab + dacarbazine efficacy in melanoma; predominantly cutaneous population — supportive but not subtype-specific |
| [NCT02339571](https://clinicaltrials.gov/study/NCT02339571) | Phase 2/3 | Active, not recruiting | 600 | Nivolumab + ipilimumab ± sargramostim in unresectable stage III/IV melanoma; general population, mechanism-relevant |
| [NCT01783938](https://clinicaltrials.gov/study/NCT01783938) | Phase 2 | Completed | 138 | Sequential nivolumab + ipilimumab in advanced/metastatic melanoma; general population, moderately relevant |
| [NCT03068455](https://clinicaltrials.gov/study/NCT03068455) | Phase 3 | Completed | 1844 | Adjuvant nivolumab + ipilimumab vs. nivolumab after resection of stage IIIB-D/IV melanoma; cutaneous-predominant |
| [NCT01940809](https://clinicaltrials.gov/study/NCT01940809) | Phase 1 | Terminated | 15 | BRAF-MEK inhibition combined with CTLA-4/PD-1 blockade in BRAF-mutant melanoma; largely cutaneous, trial terminated |
| [NCT00972933](https://clinicaltrials.gov/study/NCT00972933) | Early Phase 1 | Completed | 59 | Neoadjuvant anti-CTLA-4 immunogenicity/biomarker study in resectable stage IIIB-C melanoma; cutaneous-predominant |
| [NCT07230613](https://clinicaltrials.gov/study/NCT07230613) | Phase 2 | Recruiting | 50 | Neoadjuvant intratumoral anti-CTLA-4 + anti-PD-1 in localized melanoma; subtype not specified |
| [NCT04401995](https://clinicaltrials.gov/study/NCT04401995) | Phase 2 | Completed | 9 | TLR9 agonist + nivolumab vs. nivolumab in stage IIIB/C/D melanoma; small sample, subtype unspecified |
| [NCT03752398](https://clinicaltrials.gov/study/NCT03752398) | Phase 1 | Completed | 198 | Dose-escalation of XmAb23104 ± ipilimumab in advanced solid tumors; general population |
| [NCT04133948](https://clinicaltrials.gov/study/NCT04133948) | Phase 1/2 | Completed | 44 | Domatinostat + nivolumab + ipilimumab neoadjuvant regimen in stage III cutaneous/unknown-primary melanoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Current Cancer Drug Targets | Systematic review of adjuvant melanoma trials (2000–2015); notes non-cutaneous melanoma is only ~5% of cases and mentions immunotherapy's evolving role |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discovery Medicine | Clinical update on anti-PD-1 antibodies alone or combined with ipilimumab as standard frontline therapy for advanced melanoma |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | Retrospective cohort comparing anti-PD-1 monotherapy vs. combination with ipilimumab across age groups in advanced melanoma |
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort/Expanded Access | The Medical Journal of Australia | Evaluates ipilimumab efficacy/tolerability in pretreated **cutaneous, uveal, and mucosal melanoma**, assessing response by subtype — directly relevant to the non-cutaneous prediction |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Case of metastatic melanoma with colonic involvement treated with immunotherapy; illustrates real-world use and immune-related GI toxicity |

---

## Malaysia Market Information

Ipilimumab has 1 registered authorization with Malaysia's NPRA (market status: Marketed). Detailed license number, product name, dosage form, and approved-indication text were not returned in this data extract and cannot be reported without risk of fabrication.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — immune checkpoint inhibitor (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — checkpoint inhibitors are not primarily myelosuppressive; the dominant toxicity pattern is immune-related adverse events (e.g., colitis, hepatitis, dermatitis, endocrinopathies) rather than bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests, thyroid/endocrine panel, CBC, and clinical monitoring for immune-related adverse events (colitis, hepatitis, dermatitis, hypophysitis/thyroiditis) |
| Handling Protection | Biologic monoclonal antibody infusion — not classic cytotoxic chemotherapy; follow institutional infusion and hazardous-drug handling protocols for biologics |

*Formal toxicity/warning data from the product label was not available (see data gap below) — please refer to the package insert warnings and precautions for confirmed details.*

---

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack flags this as a **Blocking** data gap (DG001: TFDA/NPRA label warnings and contraindications not yet retrieved), meaning a formal safety pre-screen (S1) cannot be completed until the label PDF is obtained and parsed. No drug interaction records were found in the current query.

---

## Other Predicted Indication (Screened Out)

The model also flagged **choroideremia** (TxGNN score 99.06%) as a candidate. This is an X-linked recessive retinal degeneration caused by CHM gene mutation / Rab escort protein-1 deficiency, with no known biological relationship to CTLA-4 blockade. No clinical trials or literature support this link, and the evidence level is L5 (model prediction only). This is assessed as likely algorithmic noise/false positive — **Decision: Hold**, no further action recommended.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for non-cutaneous melanoma)*

**Rationale:**
Ipilimumab's CTLA-4 blockade mechanism is directly validated in melanoma, including 2 completed Phase 3 trials, and is mechanistically applicable across cutaneous and non-cutaneous subtypes. However, direct subtype-specific (uveal/mucosal) efficacy evidence is limited, and known lower immunotherapy response rates in non-cutaneous melanoma warrant caution.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF for safety warnings and contraindications (DG001, blocking)
- Formal mechanism-of-action documentation (DG002)
- Subtype-specific (uveal/mucosal melanoma) efficacy and response-rate data
- Confirmation of registered indication text from NPRA license record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

