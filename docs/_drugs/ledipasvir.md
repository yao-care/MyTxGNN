---
layout: default
title: Ledipasvir
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Ledipasvir
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

# Ledipasvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Ledipasvir is the NS5A-inhibitor component of the Ledipasvir/Sofosbuvir (Harvoni) fixed-dose combination, originally developed and approved for chronic hepatitis C virus (HCV) infection.
The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**,
with **21 clinical trials** and **20 publications** currently retrieved for this pairing — though on review, most of this evidence concerns HBV reactivation safety during HCV treatment rather than deliberate HBV therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) Infection (as part of Ledipasvir/Sofosbuvir combination) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, ledipasvir is an NS5A inhibitor and is marketed only as part of the Ledipasvir/Sofosbuvir (Harvoni) fixed-dose combination; its efficacy in chronic HCV infection is well established and it has no independent regulatory approval outside this combination.

HCV and HBV are both hepatotropic viruses that share transmission routes and frequently co-occur in the same patient population, which is almost certainly why the TxGNN model surfaced this link — the knowledge graph likely encodes strong co-occurrence between ledipasvir, HCV treatment trials, and HBV-coinfected patient cohorts.

However, the mechanistic case is weak on closer inspection. Ledipasvir's target (HCV NS5A protein) has no known structural or functional homolog in HBV, and HBV replicates via a reverse-transcriptase mechanism unrelated to HCV's RNA-dependent RNA polymerase pathway. The bulk of the retrieved evidence is actually safety surveillance — studies monitoring HBV reactivation risk in HCV/HBV-coinfected patients undergoing HCV treatment — rather than trials designed to test ledipasvir as an HBV therapy. The one exception, a small open-label Phase 2 pilot (NCT03312023 / PMID 36045503, n=21), directly tested ledipasvir/sofosbuvir in HBV mono-infected subjects and reported only a modest HBsAg decline, which may be attributable to sofosbuvir rather than ledipasvir.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Only trial designed directly for HBV-infected subjects; open-label, 12-week LDV/SOF, assessed HBsAg/HBV DNA decline (Grade A relevance) |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Unknown | 21 | HARVONI in HCV-associated indolent B-cell lymphoma; title suggests possible HDV (HBsAg+) population, not standard HBV monoinfection (Grade B) |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | HCV/HBV coinfection study; primary endpoint is HCV response, HBV reactivation is a secondary observation (Grade B) |
| [NCT02219685](https://clinicaltrials.gov/study/NCT02219685) | Phase 2 | Completed | 40 | Double-blind, placebo-controlled RCT on cerebral metabolism/neurocognition in HCV; rigorous design but small and not HBV-focused (Grade B) |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | LDV/SOF in HCV genotype 1/2 patients coinfected with HBV in Taiwan; treats HCV, HBV is a coinfection covariate (Grade C) |
| [NCT01826981](https://clinicaltrials.gov/study/NCT01826981) | Phase 2 | Completed | 359 | Sofosbuvir-containing regimens for chronic HCV; HBV not a treatment target (Grade C) |
| [NCT02010255](https://clinicaltrials.gov/study/NCT02010255) | Phase 2 | Completed | 334 | LDV/SOF + ribavirin in advanced liver disease/post-transplant HCV patients |
| [NCT01457768](https://clinicaltrials.gov/study/NCT01457768) | N/A | Completed | 570 | Long-term registry for HCV patients who failed to achieve SVR; observational, not HBV-directed |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV patients; unrelated to HBV |
| [NCT02421211](https://clinicaltrials.gov/study/NCT02421211) | Phase 2 | Completed | 41 | Pharmacokinetic interaction study between simeprevir and ledipasvir in HCV patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT/Phase 2 | Journal of Medical Virology | Only dedicated HBV-monoinfection trial; LDV/SOF produced modest HBsAg/HBV DNA decline at Week 12 |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort (reactivation risk) | Journal of Clinical Gastroenterology | Examined HBV reactivation risk during LDV/SOF treatment for HCV |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort | Clinical Infectious Diseases | Taiwan HCV/HBV coinfection cohort, 108-week posttreatment follow-up on HBV reactivation |
| [27486112](https://pubmed.ncbi.nlm.nih.gov/27486112/) | 2016 | Cohort (safety) | Clinical Infectious Diseases | Taiwan/Korea trial cohort; no evidence of HBV reactivation among 103 previously HBV-infected patients |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohort (cancer patients) | Journal of Viral Hepatitis | HBV reactivation risk during DAA treatment in cancer patients with HBV/HCV coinfection |
| [27367295](https://pubmed.ncbi.nlm.nih.gov/27367295/) | 2016 | Pilot study | Antiviral Therapy | Pilot study of LDV/SOF suppressing HCV in HBV-coinfected patients |
| [29174546](https://pubmed.ncbi.nlm.nih.gov/29174546/) | 2018 | Prospective cohort | Gastroenterology | Risks and outcomes of HBV reactivation during LDV/SOF treatment of HCV in HBV-infected patients |
| [28294955](https://pubmed.ncbi.nlm.nih.gov/28294955/) | 2018 | Case report/Cohort | Antiviral Therapy | HBV reactivation in chronic hepatitis C patients during LDV/SOF treatment |
| [28585404](https://pubmed.ncbi.nlm.nih.gov/28585404/) | 2017 | Cohort | Hepatology Research | Japanese prospective cohort on frequency/factors of HBV reactivation during all-oral DAA treatment |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | Journal of Viral Hepatitis | Low incidence of HBV reactivation in chronic HCV patients receiving DAA therapy |

---

## Malaysia Market Information

Malaysia NPRA records show **1 active registration** for ledipasvir with market status "已上市" (Marketed). However, the specific license number, product name, dosage form, manufacturer, and approved indication text were not available in this evidence pack and require direct lookup from the NPRA product registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for ledipasvir's activity against HBV is weak — its target has no known HBV homolog — and the supporting evidence is dominated by HBV-reactivation safety surveillance in HCV-treated coinfected patients rather than trials designed to test HBV efficacy. The single direct HBV-efficacy trial (NCT03312023, n=21) is too small to support progression, and the underlying safety label data (warnings/contraindications) needed for even a preliminary safety screen (S1) is currently missing — a Blocking-severity data gap.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap; required before any S1 safety screening)
- Detailed mechanism of action data for ledipasvir (currently a High-severity data gap affecting mechanistic assessment)
- A larger, controlled trial specifically targeting HBV monoinfection to confirm or refute the modest HBsAg reduction signal seen in NCT03312023
- Malaysia-specific license and approved-indication details from the NPRA registry
- Clarification of whether NCT03261349's target population is true HBV monoinfection or hepatitis delta virus (HDV), which would materially change the interpretation of that trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

