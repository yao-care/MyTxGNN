---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a guanosine nucleoside analog originally developed and marketed for chronic hepatitis B (HBV) treatment, acting by inhibiting the HBV reverse transcriptase. The TxGNN model's top-ranked prediction flags **chronic hepatitis C virus infection** as a candidate new indication (score 99.98%), but the underlying evidence — **40 clinical trials** and **20 publications** — consists almost entirely of HBV trials and HBV/HCV coinfection management studies, not direct HCV treatment evidence. The evidence pack itself flags this prediction as a likely knowledge-graph artifact rather than a genuine pharmacological signal (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis B virus infection *(inferred from evidence-pack rationale text; the structured TFDA label field was empty — see Data Gap DG001)* |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from DrugBank in this evidence pack (Data Gap DG002). Based on what is documented in the accompanying clinical-trial and literature evidence, however, entecavir is a cyclopentyl guanosine analog that inhibits the HBV reverse transcriptase across all three steps of viral DNA synthesis (priming, negative-strand synthesis, positive-strand synthesis). This mechanism is specific to hepadnaviruses (HBV) — it is not a broad-spectrum antiviral mechanism.

Hepatitis C virus, by contrast, is a flavivirus that replicates via an RNA-dependent RNA polymerase (NS5B), a completely different enzymatic target. The evidence pack's own repurposing rationale explicitly notes this mismatch: *"Entecavir…僅抑制HBV反轉錄酶，對HCV（黃病毒科，以NS5B RNA依賴性RNA聚合酶複製）無直接藥理作用機轉"* — there is no known direct pharmacological mechanism connecting entecavir to HCV.

The TxGNN model's very high score for this candidate is most plausibly explained by **"guilt-by-association" inflation**: HBV and HCV frequently co-occur in the same patients and in the same clinical literature (coinfection management, DAA-triggered HBV reactivation studies, dual-hepatitis reviews), which creates dense graph connectivity between entecavir and HCV-related disease nodes without reflecting a real treatment effect. Consistent with this, essentially all of the "supporting" clinical trials for this candidate are actually entecavir-for-HBV trials, or studies of HBV management in HCV/HBV-coinfected patients — not trials of entecavir as HCV therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Evaluates nucleos(t)ide analogue prophylaxis (incl. entecavir) to prevent HBV reactivation in HCV/HBV-coinfected patients receiving DAA therapy for hepatitis C — entecavir treats the HBV component, not HCV itself |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studies direct-acting antivirals for HCV/HBV coinfection; entecavir role limited to managing the HBV component during anti-HCV treatment |
| [NCT01037166](https://clinicaltrials.gov/study/NCT01037166) | Phase 2 | Completed | 84 | Japan study of entecavir antiviral activity in lamivudine-incomplete-responder chronic hepatitis B patients — HBV indication, not HCV |
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | QL-007 combined with entecavir or tenofovir in chronic hepatitis B — an HBV combination study, unrelated to HCV |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys plus entecavir vs entecavir alone for HBeAg-negative chronic hepatitis B — HBV trial |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Drug-drug interaction/PK study of ritonavir combination with entecavir or tenofovir in healthy subjects — not an efficacy trial |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Entecavir vs adefovir in chronic hepatitis B with hepatic decompensation — core HBV registration-type evidence |
| [NCT02881008](https://clinicaltrials.gov/study/NCT02881008) | Phase 1/2 | Completed | 48 | Myrcludex B vs entecavir in HBeAg-negative chronic hepatitis B |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Arabinoxylan rice bran (MGN-3/Biobran) for hepatocellular carcinoma and hepatitis B/C infection; entecavir not the primary study intervention |
| [NCT07267208](https://clinicaltrials.gov/study/NCT07267208) | Phase 2 | Not yet recruiting | 82 | Entecavir orally disintegrating tablet conversion in stable liver transplant patients with chronic hepatitis B |

**None of the retrieved trials directly test entecavir as a treatment for hepatitis C.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort/Observational | Viruses | Examines HCV reactivation in anti-HCV antibody-positive chronic hepatitis B patients undergoing nucleos(t)ide analogue (incl. entecavir) therapy for HBV |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World J Gastroenterol | Reviews HBV/HCV/alcohol as causes of hepatocellular carcinoma; general background, not entecavir-HCV efficacy |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Overview of chronic hepatitis B and C treatment landscape as separate diseases |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Reviews antiviral medications for hepatitis B and C and renal effects; lists entecavir among HBV-specific agents |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Management of viral hepatitis B and C in children — separate disease management |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Pract Res Clin Gastroenterol | Fibrosis in chronic viral hepatitis; entecavir discussed only in the HBV context |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Management of hepatitis B/C before and after transplantation; entecavir cited for HBV prophylaxis |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in HBV/HCV coinfection treatment; entecavir addresses the HBV component only |
| [39351520](https://pubmed.ncbi.nlm.nih.gov/39351520/) | 2024 | Review/Commentary | World J Hepatol | General commentary on metabolomics in liver disease diagnostics |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review (pending) | Biomedicines | Overview of chronic viral hepatitis (B, C, D) therapies; entecavir discussed under HBV suppressive therapy |

**No RCT or direct clinical study evaluates entecavir as an HCV antiviral treatment.**

---

## Safety Considerations

Please refer to the package insert for safety information. *(TFDA warnings, contraindications, and drug-drug interaction data were not available in this evidence pack — Data Gap DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for entecavir–HCV is very high, but every retrieved clinical trial and literature source supports entecavir's *existing* HBV indication or its use in managing the HBV component of HBV/HCV coinfection — none demonstrates direct antiviral activity against HCV. The prediction is mechanistically implausible (HBV reverse transcriptase inhibitor vs. HCV NS5B RNA polymerase target) and is best explained as a graph-association artifact rather than a genuine repurposing signal.

Separately, note that this same evidence pack's rank-2 candidate ("hepatitis B virus infection," L1 evidence, 1 large Phase 3 RCT plus extensive Phase 2–4 data) is very likely **entecavir's own existing approved indication being mis-flagged as "new"** — a downstream effect of the `original_indications` field being empty in the source data (Data Gap). This should be corrected at the data-pipeline level before further scoring.

**To proceed, the following is needed:**
- TFDA/NPRA label data (warnings, contraindications) to close Data Gap DG001
- Confirmed DrugBank mechanism-of-action record to close Data Gap DG002
- Backfill of the `original_indications` field so already-approved indications are not re-surfaced as novel repurposing candidates
- If HCV repurposing is still of interest, a literature/mechanism search specifically for entecavir activity against HCV NS5B or host antiviral pathways, since no such evidence exists in the current pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

