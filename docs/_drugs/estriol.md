---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 1
---

# Estriol
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

# Estriol: From Menopausal Hormone Therapy to Amenorrhea

## One-Sentence Summary

Estriol is a low-potency natural estrogen historically used in menopausal hormone therapy (vaginal/urogenital atrophy, vasomotor symptoms); the specific Malaysia-registered indication text was not captured in this data pull.
The TxGNN model predicts it may be effective for **Amenorrhea** — specifically functional hypothalamic amenorrhea (FHA) — but the supporting evidence is thin: **0 directly relevant clinical trials** (the 3 retrieved trials involve a different drug, estetrol) and only **1 small pilot RCT** plus supporting reviews among 13 retrieved publications.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the Malaysia registry data provided (license record fields are blank); estriol is generally used for menopausal/urogenital estrogen therapy |
| Predicted New Indication | Amenorrhea (functional hypothalamic amenorrhea) |
| TxGNN Prediction Score | 99.18% (rank 10,684 among all predictions) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for estriol is not available in this evidence pack. Based on known pharmacology, estriol is a weak-affinity, short-acting estrogen; its established efficacy is in menopausal estrogen replacement, and mechanistically this same estrogen-receptor activity is plausible in other hypoestrogenic states.

Functional hypothalamic amenorrhea (FHA) is one such state: chronic psychosocial/metabolic stress suppresses pulsatile GnRH release, reducing LH/FSH and producing a hypoestrogenic, amenorrheic condition. Low-dose estrogen exposure has been proposed to modulate the hypothalamic-pituitary axis and help re-trigger positive-feedback LH secretion in FHA patients — this is the specific mechanistic link cited in the evidence pack.

Two important caveats limit how far this rationale extends. First, it only addresses the hypoestrogenic/hypothalamic subtype of amenorrhea — it has no mechanistic bearing on uterine, chromosomal, or other non-hypoestrogenic causes. Second, the supporting clinical data measures a surrogate endpoint (LH pulsatility), not the actual clinical outcome of restored menstrual cycles, so the causal chain from "modulates LH" to "treats amenorrhea" remains unproven.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1015 | Trial of **estetrol (E4)**/drospirenone combined oral contraceptive for postmenopausal vasomotor symptoms — not estriol; appears to be a drug-name mismatch (estetrol ≠ estriol) and does not address amenorrhea |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1570 | Same estetrol/drospirenone contraceptive series, vasomotor-symptom endpoint; same mismatch issue, not relevant to estriol or amenorrhea |
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn | 0 | Photobiomodulation for postmenopausal vulvovaginal atrophy; trial withdrawn with zero enrollment, unrelated to estriol or amenorrhea |

⚠️ None of the three retrieved trials constitute direct evidence for estriol in amenorrhea. Two are confounded with estetrol (a distinct, related estrogen used in oral contraceptives) and the third was withdrawn before enrolling any subjects. Effectively, **there is no usable clinical trial evidence** for this indication at present.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | RCT (pilot, crossover) | Fertility and Sterility | Estriol administration modulated LH secretion in women with functional hypothalamic amenorrhea — the only direct estriol/amenorrhea clinical evidence found, but a small pilot with a surrogate (hormonal) endpoint |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | Biomedicines | Reviews low-dose estrogens as neuroendocrine modulators in FHA, discussing the mechanistic basis for triggering positive-feedback LH release |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Cohort | Medicinski pregled | Effects of estro-progestagen therapy on lipid/hormonal profiles in premature primary ovarian failure (a hypergonadotropic amenorrhea) |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observational (TCM) | Zhong xi yi jie he za zhi | Traditional Chinese Medicine observational study on gonadal function changes in amenorrhea/oligomenorrhea; not estriol-specific |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | Clinical Obstetrics and Gynecology | General review of neoplasia risk and hormonal contraception; background relevance only |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Case report/Review | British Journal of Psychiatry | Anorexia nervosa review, noting associated amenorrhea; not an estriol treatment study |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Case report | American Journal of Obstetrics and Gynecology | Gynecologic/endocrine effects following medroxyprogesterone in pregnancy; not estriol |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case report | Lancet | Endocrine findings in two patients with premature ovarian failure |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | Methods paper | Die Medizinische Welt | Radioimmunoassay methodology for LH, FSH, progesterone, estrone, estradiol and estriol; lab-methods reference only |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Review (mechanism) | Journal of Clinical Endocrinology and Metabolism | Historical review of anti-ovulatory compound mechanisms |

## Malaysia Market Information

The NPRA registry indicates 1 registered license for estriol with market status "已上市" (Marketed), but the license number, product name, dosage form, and approved indication text were not captured in this evidence pack (all fields blank). This is flagged as data gap **DG001** (Blocking) — resolving it requires downloading and parsing the actual product label/insert from the regulatory source.

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack — DDI query returned zero results, and warnings/contraindications are recorded as data gaps.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a plausible but narrow mechanism (estrogen modulation of LH in one amenorrhea subtype, FHA) supported by a single small pilot crossover RCT with a surrogate endpoint, not restored menses. The three retrieved clinical trials do not actually support estriol in this indication (drug-name mismatch with estetrol, or withdrawn). Combined with a Blocking data gap on TFDA/NPRA safety labeling (DG001) that prevents a proper S1 safety screen, and a High-severity gap on mechanism of action (DG002), the evidence is not yet sufficient to proceed.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the actual Malaysia product label for warnings, contraindications, and confirmed approved indication text
- Resolve DG002: obtain estriol's mechanism-of-action detail from DrugBank
- A clinical trial search specifically re-verified for estriol (not estetrol) to confirm whether any real trials exist in amenorrhea
- A larger, adequately powered RCT with a clinical endpoint (resumption of menstrual cycles), not just LH secretion, to validate the FHA mechanistic hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

