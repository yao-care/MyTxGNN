---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 8
---

# Fluticasone Furoate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Fluticasone Furoate: From Asthma/COPD to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate (DB08906) is an inhaled corticosteroid (ICS) currently marketed in Malaysia in combination products (e.g. Relvar/Arnuity Ellipta) for asthma and COPD. The TxGNN model's top-ranked prediction is that it may also be effective for **Atopic Eczema**, but the supporting evidence base of **11 clinical trials** and **2 publications** consists almost entirely of the propionate ester (not furoate), so the finding remains a class-effect hypothesis rather than molecule-specific proof.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA license records (all 4 license entries have blank indication text); known approved uses of FF-containing combination products are asthma and COPD |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fluticasone furoate is not available (data gap, High severity). Based on what is present in this evidence pack, fluticasone furoate is an ICS marketed as combination products (Relvar/Breo Ellipta with vilanterol, and Arnuity Ellipta) approved for asthma and COPD, where it acts by suppressing airway inflammation. Topical corticosteroids as a drug class are also first-line treatment for atopic eczema, acting by suppressing local cutaneous inflammation — the same broad anti-inflammatory mechanism.

However, the mechanistic link here is a class-effect inference rather than molecule-specific evidence. Almost all of the clinical trials returned for atopic eczema studied **fluticasone propionate** (a different ester, e.g. Cutivate) in topical cream/ointment/lotion form — not fluticasone furoate. Fluticasone furoate itself is currently marketed only as a nasal spray and inhaler formulation; no furoate-specific topical skin trial was found. The prediction is therefore biologically plausible (steroid class-effect) but not yet supported by furoate-specific data, consistent with the evidence pack's own L2/"Research Question" scoring for this indication.

Notably, a separate TxGNN-predicted indication in this same evidence pack — **bronchitis/COPD** (rank 2) — is supported by direct fluticasone furoate evidence (RELVAR/Arnuity Ellipta trials) and reaches evidence level L1 with a "Proceed with Guardrails" recommendation. That indication represents a more direct, on-molecule extension of the drug's existing respiratory use and may warrant separate evaluation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Tacrolimus 0.1% ointment vs fluticasone 0.005% ointment in adults with moderate-severe atopic dermatitis with facial "red face" lesions |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Twice-weekly topical fluticasone propionate maintenance therapy to reduce relapse risk in children with mild-moderate AD |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of Cutivate (fluticasone propionate) lotion 0.05% effect on HPA axis in pediatric AD |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Tacrolimus 0.03% ointment vs fluticasone 0.005% ointment in children ≥2 years with moderate-severe AD |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Intermittent (twice-weekly) fluticasone propionate 0.05% cream vs daily moisturizer in stabilized pediatric AD |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | NA | Completed | 98 | Oral probiotic supplementation trial in children with AD (drug-unrelated comparator study) |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | SEAL study: proactive skin-barrier care plus fluticasone propionate cream vs reactive therapy to prevent AD/food allergy in infants |
| [NCT00426283](https://clinicaltrials.gov/study/NCT00426283) | Phase 2 | Completed | 42 | Swallowed high-dose fluticasone propionate vs placebo for eosinophilic esophagitis (non-cutaneous indication) |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | EpiCeram device vs mid-strength topical steroid (fluticasone propionate 0.05%) in pediatric AD |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Concomitant Elidel 1% cream + Cutivate (fluticasone propionate) 0.05% cream in severe AD lesions |

*Note: 1 additional trial (NCT03594565, a case series on skin reactions to glucose monitors) was excluded as not directly relevant to atopic eczema treatment.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews intranasal corticosteroid effects on the HPA axis in patients with allergic conditions including atopic dermatitis |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case Report | Indian J Otolaryngol Head Neck Surg | Case study of allergen immunotherapy use in a patient with autoimmune disease and atopic dermatitis |

## Malaysia Market Information

NPRA records show fluticasone furoate has 4 active marketing authorizations in Malaysia (market status: Marketed). However, the detailed license fields (authorization number, product name, dosage form, and approved indication text) are not populated in the current dataset and cannot be reported here.

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data are currently available in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that prevents initial safety screening (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (atopic eczema) is supported only by class-effect reasoning — nearly all cited trials studied fluticasone propionate, not the furoate ester actually under evaluation — placing it at evidence level L2 ("Research Question"). Combined with a Blocking-severity gap in safety/label data, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data for fluticasone furoate (High-severity gap, DG002)
- Complete Malaysia license details (authorization numbers, product names, approved indication text)
- Furoate-specific (not propionate) topical/dermatologic efficacy data for atopic eczema, if this indication is to be pursued further
- Consider evaluating the bronchitis/COPD prediction (rank 2) in parallel — it has direct furoate-specific evidence (L1, "Proceed with Guardrails") and may be a more actionable near-term candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

