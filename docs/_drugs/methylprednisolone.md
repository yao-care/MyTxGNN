---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 481
evidence_level: L5
indication_count: 5
---

# Methylprednisolone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Methylprednisolone: From Corticosteroid-Responsive Inflammatory Conditions to Erythema Multiforme

## One-Sentence Summary

Methylprednisolone is a systemic glucocorticoid broadly used for inflammatory, allergic, and autoimmune conditions; the specific NPRA-approved indication text is not captured in this evidence pack. The TxGNN model ranks **Erythema Multiforme** as its top predicted new indication, supported by **2 directly relevant clinical trials** and **10+ relevant publications**, including a Cochrane systematic review on the SJS/TEN spectrum — but a blocking gap in TFDA/NPRA safety-label data currently prevents a full safety assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in NPRA license records (all 5 sampled license entries are blank); methylprednisolone's known general indication class is corticosteroid-responsive inflammatory/allergic/autoimmune conditions |
| Predicted New Indication | Erythema Multiforme |
| TxGNN Prediction Score | 0.00% (raw score recorded as 0.0 — appears to be a data capture issue; treat rank position #1, not the score magnitude, as the directional signal) |
| Evidence Level | L3 (systematic review + observational evidence) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known pharmacology, methylprednisolone is a synthetic glucocorticoid with broad anti-inflammatory and immunosuppressive activity, widely used across corticosteroid-responsive conditions; its efficacy in these settings has been proven for decades.

Erythema multiforme (EM) is a T-cell–mediated hypersensitivity mucocutaneous reaction. Systemic glucocorticoids, including methylprednisolone, are commonly used clinically to control inflammation in severe forms (EM major). Mechanistically this is a reasonable extension of methylprednisolone's established immunosuppressive action. However, EM sits on a disease spectrum with Stevens-Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN), and the systematic-review evidence for systemic interventions (including corticosteroids) across this spectrum is of relatively weak quality with inconsistent conclusions — which tempers confidence in the prediction despite biological plausibility.

---

## Clinical Trial Evidence

Note: the evidence pack's clinical-trials query returned 14 results for "erythema multiforme," but most (e.g., prostate cancer abiraterone trials, an SBRT trial, vitiligo studies) are keyword-mismatched and not clinically relevant. Only the following are directly relevant:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06266221](https://clinicaltrials.gov/study/NCT06266221) | Phase 3 | Not yet recruiting | 96 | RCT comparing a short systemic corticosteroid regimen to placebo in the acute established phase of severe erythema multiforme |
| [NCT06119490](https://clinicaltrials.gov/study/NCT06119490) | Early Phase 1 | Recruiting | 30 | Two-arm, open-label study evaluating methylprednisolone combined with JAK inhibitors (baricitinib/tofacitinib) for toxic epidermal necrolysis (EM-spectrum disease) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35274741](https://pubmed.ncbi.nlm.nih.gov/35274741/) | 2022 | Cochrane Systematic Review | Cochrane Database Syst Rev | Reviews systemic interventions (including glucocorticoids) for SJS/TEN/overlap syndrome; notes an unmet need to establish efficacy of these therapies |
| [9039508](https://pubmed.ncbi.nlm.nih.gov/9039508/) | 1997 | Prospective comparative study | Eur J Pediatr | 16 children with EM major (Stevens-Johnson): early IV methylprednisolone bolus (4 mg/kg/day) vs. supportive care only — early corticosteroid use associated with better outcomes |
| [26281815](https://pubmed.ncbi.nlm.nih.gov/26281815/) | 2015 | Review | J Emerg Med | General clinical review of erythema multiforme presentation and management |
| [8566721](https://pubmed.ncbi.nlm.nih.gov/8566721/) | 1995 | Review | Allergy Proc | Virus-induced EM/SJS; discusses acyclovir plus corticosteroid management strategy |
| [37832081](https://pubmed.ncbi.nlm.nih.gov/37832081/) | 2023 | Case Report | Medicine | Sintilimab (PD-1 inhibitor)-induced EM drug eruption in colon cancer treatment |
| [38962048](https://pubmed.ncbi.nlm.nih.gov/38962048/) | 2024 | Case Report | Int Cancer Conf J | Pembrolizumab-induced severe EM major; steroid ointment ineffective, systemic disease progressed |
| [7919560](https://pubmed.ncbi.nlm.nih.gov/7919560/) | 1994 | Case Report | Ann Pharmacother | Ampicillin-induced EM with hypersensitivity myocarditis |
| [16164723](https://pubmed.ncbi.nlm.nih.gov/16164723/) | 2005 | Review/Case series | J Eur Acad Dermatol Venereol | Lupus erythematosus associated with EM-like lesions (Rowell's syndrome) |
| [12370143](https://pubmed.ncbi.nlm.nih.gov/12370143/) | 2002 | Case Report | Eur J Dermatol | Dimorphic exanthema with EM major features from pyrazolone derivatives |
| [21909214](https://pubmed.ncbi.nlm.nih.gov/21909214/) | 2011 | Case Report | Ann Dermatol | Neonatal erythema multiforme, an extremely rare presentation |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were returned in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication has plausible mechanistic rationale and L3-level evidence (a Cochrane systematic review plus supportive clinical and case literature), but a **Blocking** data gap (DG001: missing TFDA/NPRA package insert warnings/contraindications) prevents this candidate from completing even the S1 safety initial screening stage — this must be resolved before any Go/Guardrails decision can be made.
- The TxGNN score value itself appears incompletely captured (0.0 across all ranked candidates), so the ranking should be treated as directional only, not as a calibrated confidence measure.

**To proceed, the following is needed:**
- Retrieve and parse the Malaysia NPRA product insert(s) for methylprednisolone to resolve DG001 (key warnings, contraindications)
- Obtain detailed mechanism-of-action data from DrugBank to resolve DG002
- Monitor completion of NCT06266221 (Phase 3 RCT, EM major, expected completion 2027) as the pivotal efficacy signal
- Track NCT06119490 (methylprednisolone + JAK inhibitors in TEN) for spectrum-disease safety/efficacy data
- Populate complete Malaysia license records (product name, dosage form, approved indication text) — current records for all sampled licenses are blank despite 7 total registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

