---
layout: default
title: Norethisterone
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 1
---

# Norethisterone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Norethisterone: From Hormonal Contraception/Menstrual Regulation to Amenorrhea

## One-Sentence Summary

> Norethisterone (DB00717) is a 19-nortestosterone-derived progestin generally used in hormonal contraception and menstrual cycle regulation; the specific Malaysian/Taiwan-registered indication text was not retrievable in this data pull.
> The TxGNN model predicts it may be effective for **Amenorrhea**, with a **99.60%** prediction score, supported by **8 clinical trials** and **~20 publications**.
> However, the underlying evidence suggests this may reflect a **drug-causes-disease** association (norethisterone inducing amenorrhea as a side effect / add-back component) rather than a genuine treatment signal, and evidence strength is only L3.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available data (no `approved_indication_text` retrieved from registry; norethisterone is generally known as a progestin used in contraception/menstrual disorders) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 (per evidence pack scoring) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on known pharmacology, norethisterone is a synthetic progestin that binds the progesterone receptor and is primarily used to induce endometrial withdrawal bleeding, delay menses, and support contraceptive regimens — a mechanism that is, if anything, **opposite in direction** to treating amenorrhea (absence of menstruation).

The supporting evidence largely reflects this ambiguity. Of the 8 clinical trials retrieved, most (LIBERTY 1, LIBERTY 2, LIBERTY EXTENSION, NCT03751124) use **relugolix** (a GnRH antagonist) as the primary agent, with norethindrone acetate included only as low-dose "add-back" therapy to offset estrogen-deficiency side effects (e.g., bone density loss) — amenorrhea/bleeding reduction in these trials is driven by relugolix's suppression of ovulation, not by norethisterone itself. The remaining trials (elagolix studies, BG2109) do not involve norethisterone at all.

The evidence pack's own `repurposing_rationale.mechanistic_link` flags this explicitly: the high TxGNN score (0.996) may reflect a **drug–disease co-occurrence/side-effect association** (long-term progestin or combined oral contraceptive use causing amenorrhea) rather than a validated therapeutic relationship. This directional ambiguity should be resolved before any further development effort.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Phase 3 | Completed | 388 | LIBERTY 1: relugolix ± low-dose estradiol/norethindrone acetate (NETA) add-back vs placebo for heavy menstrual bleeding in uterine fibroids; amenorrhea a secondary outcome. NETA is an add-back component, not the primary agent. |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Phase 3 | Completed | 382 | LIBERTY 2: identical design/regimen to LIBERTY 1, confirmatory Phase 3 RCT. |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Phase 3 | Completed | 477 | LIBERTY EXTENSION: open-label, long-term (28-week) safety/efficacy extension of relugolix + estradiol/NETA. |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Phase 3 | Completed | 229 | Randomized withdrawal study of relugolix + estradiol + norethindrone acetate, up to 104 weeks, in uterine fibroid patients. |
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Phase 3 | Unknown | 312 | BG2109 (not norethisterone) ± add-back therapy for heavy menstrual bleeding; status unclear, drug identity for add-back not confirmed. |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2 | Completed | 571 | Elagolix ± add-back vs placebo for heavy menstrual bleeding in uterine fibroids; primary agent is elagolix, not norethisterone. |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | Completed | 271 | Elagolix vs placebo proof-of-concept for uterine bleeding/fibroid volume; no direct norethisterone involvement. |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | N/A | Recruiting | 111 | Ultrasound observational study of fibroid morphology during relugolix/estradiol/norethisterone treatment; descriptive imaging study, not an efficacy trial. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863160](https://pubmed.ncbi.nlm.nih.gov/37863160/) | 2024 | RCT | American Journal of Obstetrics and Gynecology | Relugolix + estradiol + NETA (LIBERTY Long-Term Extension) improved fibroid-associated heavy menstrual bleeding in Black/African American women over 52 weeks; NETA is add-back, not primary driver. |
| [41489365](https://pubmed.ncbi.nlm.nih.gov/41489365/) | 2026 | Secondary analysis | Biology of Reproduction | WHICH trial secondary study: compared DMPA-IM vs norethisterone enanthate (NET-EN) on HPO axis; DMPA-IM associated with more amenorrhea than NET-EN, suggesting NET-EN is *less* amenorrhea-inducing among injectables. |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | Phase I trial | Contraception | Phase I trial of norethisterone enanthate (NEN) and norethisterone acetate (NET) in 20 women; reports amenorrhea/spotting as menstrual-disorder side effects during contraceptive use. |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PLoS One | WHICH randomized trial comparing DMPA-IM and NET-EN effects on estradiol levels and menstrual/psychological/behavioral measures relevant to HIV risk. |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstetrics and Gynecology | Reviews oral GnRH antagonists (co-administered with steroid hormones, e.g., norethindrone) for uterine leiomyoma management. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Review of combination injectable contraceptives, including bleeding-pattern changes (e.g., amenorrhea) as a known effect. |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Earlier Cochrane review of combination injectable contraceptives, same topic as above. |
| [2975377](https://pubmed.ncbi.nlm.nih.gov/2975377/) | 1988 | Review | The Practitioner | General review of injectable contraception. |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Review | Pediatric Clinics of North America | Overview of hormonal contraception principles for adolescent care. |
| [12317413](https://pubmed.ncbi.nlm.nih.gov/12317413/) | 1987 | Review | Current Therapeutics | General review of oral contraceptives. |

## Malaysia Market Information

License-level detail (authorization numbers, product names, dosage forms, approved indication text) was not returned in this data pull — all 7 registered license records have empty fields. Only the aggregate figures are confirmed: **7 total licenses**, market status **已上市 (Marketed)**. Full license detail should be re-queried from the source registry before this is used in decision-making.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — flagged as Blocking data gap DG001, TFDA label warnings/contraindications not yet retrieved.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale itself questions the direction of the TxGNN association — most supporting trials use norethisterone/NETA only as an add-back component to a different primary drug (relugolix), and clinical literature indicates norethisterone-containing regimens are more plausibly linked to *causing* amenorrhea (as a contraceptive side effect) than treating it. Combined with L3 evidence and a Blocking safety data gap (DG001), this does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (resolve DG001, currently blocking safety review)
- Confirmed mechanism of action data (resolve DG002)
- A targeted literature/trial search restricted to norethisterone as monotherapy (not as GnRH-antagonist add-back) for amenorrhea treatment, to clarify whether a genuine treatment signal exists
- Malaysia/Taiwan license-level indication text (currently empty across all 7 records) to establish the true original indication baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

