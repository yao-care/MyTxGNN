---
layout: default
title: Sofosbuvir
parent: Medium Evidence (L3)
nav_order: 623
evidence_level: L3
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Tahap bukti: **L3** | Indikasi diramal: **8** 
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

# Sofosbuvir: From Chronic Hepatitis C Virus (HCV) Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide analog NS5B polymerase inhibitor developed for chronic hepatitis C virus (HCV) infection. The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**, with **50 clinical trials** and **19 publications** currently retrieved as supporting context — though on closer review, only a small number of these directly test sofosbuvir (or its fixed-dose combinations) against HBV itself, and the underlying mechanism is biologically debatable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (based on established pharmacology cited throughout the evidence pack; NPRA registry text itself is not populated — see Malaysia Market Information) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sofosbuvir is a prodrug that is metabolized intracellularly to its active triphosphate, GS-461203, which is misincorporated by the HCV NS5B RNA-dependent RNA polymerase (RdRp), causing chain termination of the viral RNA. This mechanism is well validated for HCV, where sofosbuvir-based regimens (often combined with ledipasvir, velpatasvir, or daclatasvir) are the current standard of care.

HBV, however, is a DNA virus that replicates via reverse transcriptase (RT), not RdRp. Structurally, sofosbuvir's known target has no direct counterpart in the HBV replication cycle, so a straightforward "same enzyme, same drug" rationale does not hold the way it does for other RdRp-dependent RNA viruses (e.g., HEV or flaviviruses, seen elsewhere in this evidence pack). The TxGNN association more likely reflects the frequent clinical co-occurrence of HCV and HBV (shared risk factors, common coinfection, shared trial populations) rather than a validated shared molecular target.

That said, this is not purely a false-positive knowledge-graph link: one dedicated Phase 2 open-label study (NCT03312023, matched to publication PMID 36045503) tested ledipasvir/sofosbuvir for 12 weeks in **HBV-monoinfected** subjects and reported a modest decline in HBsAg — a real, if preliminary, empirical signal. The proposed rationale for that effect is retrospective observation of HBsAg reduction in HBV/HCV-coinfected patients treated with LDV/SOF, hypothesized to extend to HBV-monoinfected patients; the exact mechanism (host immune modulation vs. any off-target antiviral effect) is not established. Given this ambiguity, mechanistic plausibility for this indication should be regarded as unconfirmed rather than strong.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label study of ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; primary/secondary endpoints were decline in HBsAg and HBV DNA from baseline — the most directly relevant trial for this indication. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2, Phase 3 | Completed | 23 | Prospective study of incidence, morbidity, and predisposing factors for HBV reactivation during direct-acting antiviral treatment of HCV/HBV coinfected patients. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | Ledipasvir/sofosbuvir FDC for 12 weeks in genotype 1/2 HCV patients coinfected with HBV (Taiwan); primary aim is HCV efficacy/safety, HBV status monitored as coinfection. |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL regimen combined with prophylactic TAF for HCV/HBV coinfected patients in China, evaluating prevention of HBV reactivation during HCV treatment. |
| [NCT02010255](https://clinicaltrials.gov/study/NCT02010255) | Phase 2 | Completed | 334 | Ledipasvir/sofosbuvir FDC + ribavirin in HCV patients with advanced liver disease or post-liver transplant; HBV not a specific study focus (background HCV trial). |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | Sofosbuvir + velpatasvir in treatment-naive chronic HCV; included for background only, no HBV-specific endpoint. |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | Comparison of ABT-493/ABT-530 vs. sofosbuvir+daclatasvir in genotype 3 HCV; drug-overlap match only, not HBV-related. |
| [NCT01826981](https://clinicaltrials.gov/study/NCT01826981) | Phase 2 | Completed | 359 | Sofosbuvir-containing regimens for chronic HCV; drug-overlap match only, not HBV-related. |

*Note: Of the 50 trials retrieved for this indication, the large majority are HCV treatment trials matched only because sofosbuvir was a study drug; they are not designed to test efficacy against HBV. The table above prioritizes the studies with genuine HBV relevance.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT (Phase 2) | Journal of Medical Virology | Open-label Phase 2 pilot of ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; reported modest HBsAg decline, hypothesis-generating rather than confirmatory. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans. Royal Soc. Tropical Med. Hyg. | Sofosbuvir/daclatasvir-based therapy in chronic HCV and HCV/HBV coinfected patients in Egypt; treatment target is HCV. |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort (108-week follow-up) | Clinical Infectious Diseases | Ledipasvir/sofosbuvir in HCV/HBV coinfected patients in Taiwan; tracked HBV reactivation through 108 weeks post-treatment. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | Journal of Clinical Gastroenterology | Risk of HBV reactivation among patients treated with ledipasvir-sofosbuvir for HCV — a safety signal, not an efficacy signal. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohort | Journal of Viral Hepatitis | HBV reactivation in cancer patients receiving DAAs for HCV in HBV/HCV coinfection — safety signal. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir and ribavirin — safety signal. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment in HCV-HBV coinfected patients. |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Review / epidemiological modeling | Lancet Gastroenterology & Hepatology | Global prevalence and care cascade of HBV — background epidemiology, not drug-specific. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Antiviral medications for HBV and HCV and their effects on kidney function — general background. |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatrica | Treatment of hepatitis B and C in children — general background. |

*Note: The majority of the retrieved literature discusses HBV reactivation risk during sofosbuvir-based HCV treatment in coinfected patients — this is a safety concern in the opposite clinical direction from the repurposing hypothesis, and is reflected in Safety Considerations below.*

---

## Malaysia Market Information

NPRA registration records list 6 active licenses under "Marketed" status, but the license number, product name, dosage form, manufacturer, and approved indication text fields are not populated in the current data source. A detailed authorization table cannot be produced until this registry data gap is resolved (see Conclusion and Next Steps).

---

## Safety Considerations

Official TFDA/NPRA key warnings, contraindications, and drug interaction data are not available in the current data source (flagged as a **Blocking** data gap — see Conclusion). Please refer to the package insert for official safety information.

**Literature-derived safety signal (not from official labeling):** Multiple cohort studies and case reports in the evidence pack (PMID 29334502, 33523503, 33031326, 31632097, 34864948) independently describe **HBV reactivation** occurring in HBV/HCV-coinfected patients during or after sofosbuvir-based DAA treatment for HCV. This is a clinically important consideration precisely because the repurposing candidate under evaluation is HBV infection itself — any protocol exploring sofosbuvir for HBV should explicitly account for this reactivation literature rather than treat it as unrelated background.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The proposed mechanism is not well supported — HBV replicates via reverse transcriptase, not the RdRp that sofosbuvir targets in HCV — and only one small (n=21), non-randomized Phase 2 pilot (NCT03312023 / PMID 36045503) directly tests sofosbuvir-based therapy against HBV, showing a modest, non-confirmatory HBsAg decline.
- A **Blocking** data gap exists: TFDA/NPRA label warnings and contraindications are unavailable, which prevents this candidate from entering the S1 safety pre-assessment stage at all.
- Literature otherwise associated with this indication predominantly documents HBV *reactivation* risk during sofosbuvir-based HCV treatment — a safety signal running counter to the repurposing hypothesis that should be resolved before further evaluation.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA package insert warnings and contraindications (resolves the Blocking data gap, DG001)
- Obtain confirmed DrugBank/original manufacturer MOA data (DG002)
- Confirm or refute the mechanistic basis for anti-HBV activity (e.g., is the reported HBsAg effect host-immune-mediated rather than direct antiviral?)
- Monitor for publication of full results from NCT03312023 (currently only pilot-stage data available)
- Formally assess the HBV reactivation safety literature as part of any future benefit-risk review for this indication
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

