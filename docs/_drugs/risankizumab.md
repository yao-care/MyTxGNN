---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

Using the drug-repurposing report template directly (no other skill fits this task — it's a fixed-format writing job from a supplied Evidence Pack, not a coding/build task).

# Risankizumab: From Plaque Psoriasis to Dermatitis (Atopic Dermatitis)

## One-Sentence Summary

Risankizumab is an anti-IL-23p19 monoclonal antibody originally developed and approved for **plaque psoriasis and related psoriatic diseases** (the license text itself was not captured in this data batch, but this is corroborated by the literature and clinical-trial evidence inside this pack). The TxGNN model predicts activity in the broader **Dermatitis** category — most credibly **atopic dermatitis** — supported by **7 clinical trials** and **18 publications**, though the disease label mixes several unrelated skin conditions of very different evidence quality. **A Blocking data gap in TFDA/NPRA safety labeling (warnings/contraindications) currently prevents a full safety pre-screen (S1).**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis (and related psoriatic disease) — *NPRA license indication text not captured in this batch; inferred from literature/trial evidence in this pack* |
| Predicted New Indication | Dermatitis (evidence concentrates on Atopic Dermatitis) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data was not available in the drug record itself, but the literature evidence collected in this pack fills the gap: risankizumab is described (PMID 38266061, PMID 31098898) as a humanized IgG1 monoclonal antibody that selectively binds the p19 subunit of interleukin-23 (IL-23), blocking downstream Th17-pathway inflammation. This is the mechanism underlying its approved use in plaque psoriasis, psoriatic arthritis, generalized pustular/erythrodermic psoriasis, and Crohn's disease.

The "dermatitis" prediction bundles several distinct conditions under one label: atopic dermatitis (Th2/Th22-dominant with some Th17 contribution), erythrodermic psoriasis and acrodermatitis continua of Hallopeau (both IL-23/Th17-driven, i.e. mechanistically close to the approved indication), and lichen planus (T-cell mediated, more distal mechanism). Only the atopic dermatitis component has direct interventional evidence — a completed Phase 2, placebo-controlled RCT (NCT03706040 / PMID 36588137) — making it the credible sub-signal within this otherwise noisy label. IL-23 blockade in AD is a genuine but mechanistically weaker rationale than in psoriasis, since AD pathogenesis is more Th2/Th22-centered; the RCT result should be treated as the primary evidence rather than the mechanistic argument alone.

Several other rank-listed diseases under this same TxGNN score band (neonatal dermatomyositis, acrodermatitis chronica atrophicans, severe nonproliferative diabetic retinopathy, hydroa vacciniforme) have **zero clinical or literature evidence** and mechanistically implausible links (infectious, VEGF-driven, or EBV-lymphoproliferative etiologies) — these are very likely model noise and are not part of the credible signal here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomized, placebo-controlled, double-blind study of risankizumab in adult/adolescent moderate-to-severe atopic dermatitis. Direct AD efficacy/safety evidence (relevance grade B: title truncated, needs manual confirmation of exact indication mapping). |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Head-to-head vs. apremilast in moderate plaque psoriasis — not dermatitis-specific, listed here due to shared query bucket (grade B). |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | RCT of risankizumab in genital/scalp psoriasis subpopulations (grade B) — psoriasis variant, not primary dermatitis evidence. |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Multi-center observational biomarker study profiling 6 immune-mediated skin diseases including AD; non-interventional (grade C). |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completed | 240 | Taiwan observational cohort on chronic plaque psoriasis durability of response; not dermatitis (grade C). |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective pharmacogenetic study on biologic survival in cutaneous psoriasis; not efficacy evidence (grade C). |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice drug-delivery feasibility study spanning AD and psoriasis; not yet recruiting, non-efficacy (grade C). |

**Note:** Only NCT03706040 is a direct interventional trial in atopic dermatitis. The remaining 6 trials are predominantly psoriasis-focused or non-interventional and were captured under the broad "dermatitis" query — they support drug safety familiarity but not the new-indication signal itself.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2, randomized, double-blind, placebo-controlled trial of risankizumab in moderate-to-severe atopic dermatitis; rationale based on IL-23/IL-22 blockade alongside Th2/Th22 involvement. Primary direct evidence. |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Systematic review | American Journal of Clinical Dermatology | Systemic therapy options, including IL-23 inhibitors, for erythrodermic psoriasis — a severe psoriasis variant sometimes captured under "dermatitis." |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Systematic review | Inflammopharmacology | Reviews IL-inhibitor (including IL-23) effects, both therapeutic and paradoxical, in lichen planus. |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/small molecules (including risankizumab) for pediatric AD, psoriasis, alopecia areata, and hidradenitis suppurativa. |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review (drug profile) | Drugs | "Risankizumab: First Global Approval" — confirms original approval basis (psoriasis vulgaris, PsA, generalized pustular/erythrodermic psoriasis in Japan; later USA/Canada/EU). |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opinion on Biological Therapy | Reviews emerging biologics, including risankizumab, for pediatric atopic dermatitis. |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Reappraises systemic immunomodulators, including IL-23 inhibitors, for psoriasis and eczema management context. |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Case series | International Journal of Dermatology | Effectiveness/safety of combined dupilumab + risankizumab in patients with concomitant AD and psoriasis. |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Case series | Experimental Dermatology | Retrospective single-center experience of risankizumab in patients with prior erythrodermic psoriasis. |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case report | Journal of Dermatological Treatment | Acrodermatitis continua of Hallopeau successfully and rapidly treated with risankizumab in an elderly patient. |

**Note:** Multiple additional case reports describe *paradoxical eczematous eruptions* occurring during risankizumab treatment for psoriasis (PMID 33185530, 36939506, 33368238, 37014149, 41645692) — these are adverse-event reports, not efficacy evidence, and are relevant to the Safety section rather than the repurposing rationale.

---

## Malaysia Market Information

NPRA records confirm **4 marketing authorizations** for Risankizumab in Malaysia (market status: Marketed), but authorization number, product name, dosage form, and approved-indication text were not populated for any of the 4 license entries in this data batch. This field-level extraction gap should be closed by re-querying NPRA before finalizing any regulatory submission.

---

## Safety Considerations

Please refer to the package insert for safety information. *(No key warnings, contraindications, or drug–drug interaction data were retrievable in this batch — TFDA/NPRA label extraction for warnings/contraindications is flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The atopic-dermatitis sub-signal has genuine L2 evidence (one completed Phase 2 placebo-controlled RCT: NCT03706040 / PMID 36588137), but the broader "dermatitis" label mixes in mechanistically weak or evidence-free conditions (neonatal dermatomyositis, acrodermatitis chronica atrophicans, hydroa vacciniforme, etc.) that should not be advanced.
- A **Blocking** data gap (DG001: TFDA/NPRA package-insert warnings/contraindications) currently makes it impossible to complete the mandatory S1 safety pre-screen, which overrides the otherwise-promising efficacy signal.

**To proceed, the following is needed:**
- Download and parse the TFDA/NPRA package insert for warnings, contraindications, and DDI data (DG001, Blocking)
- Confirm MOA via DrugBank API to formalize the mechanistic rationale beyond literature-derived description (DG002, High)
- Re-extract NPRA license-level fields (authorization number, product name, dosage form, approved indication text) — all 4 entries are currently blank
- Disambiguate the "dermatitis" label to isolate atopic dermatitis as the standalone candidate, separate from psoriasis-variant and case-report-only sub-conditions
- Discard rank 2–6, 8–10 candidates (all L5/S0/Hold, zero trials or literature) pending independent re-validation
- Note for data hygiene: rank 7 ("psoriasis") is not a new indication — it is risankizumab's existing approved indication and should be excluded from repurposing scoring in future runs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

