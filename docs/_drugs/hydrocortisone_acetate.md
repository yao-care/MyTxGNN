---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 5
---

# Hydrocortisone Acetate
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

# Hydrocortisone Acetate: From Topical Anti-Inflammatory Corticosteroid Use to Erythema Multiforme

## One-Sentence Summary

Hydrocortisone Acetate is a corticosteroid (glucocorticoid receptor agonist) already marketed in Malaysia with 34 registrations, though the specific original indication text was not returned in this data extract. The TxGNN model ranks **Erythema Multiforme** as its top predicted new indication, but the evidence behind this prediction is essentially absent — a TxGNN score of **0.00%**, **0 relevant clinical trials**, and only **1 case report**, which actually describes hydrocortisone-containing ear drops *causing* erythema multiforme rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available NPRA license extract (all `approved_indication_text` fields empty); pharmacologically a topical/systemic corticosteroid used for inflammatory conditions |
| Predicted New Indication | Erythema Multiforme |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 34 |
| Recommended Decision | Hold |

> ⚠ **Note on candidate selection**: This candidate pack contains 5 KG-predicted indications for Hydrocortisone Acetate. Erythema Multiforme is ranked #1 but has the weakest and most contradictory evidence of the set. By contrast, rank #2 (**Hemorrhoid**) has **Evidence Level L1**, multiple completed Phase 2 RCTs directly testing hydrocortisone acetate, and a recommendation of **"Proceed with Guardrails"** — reflecting an already-established clinical use rather than a novel repurposing signal. Decision-makers reviewing this candidate should be aware the top-ranked TxGNN output is not the strongest evidence-backed option in this pack.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on information present elsewhere in this evidence pack, Hydrocortisone Acetate acts as a glucocorticoid receptor agonist, and topical/rectal formulations are established for suppressing inflammatory mediators and reducing vascular permeability and edema (as reflected in its established use in hemorrhoid and ocular surface inflammation products).

For Erythema Multiforme specifically, however, this mechanistic rationale does not translate into supportive evidence. Erythema multiforme is itself an immune-mediated hypersensitivity reaction, often triggered by drugs or infections — and the single literature record retrieved for this pairing documents hydrocortisone acetate (as an ingredient in Gentisone HC ear drops) as the **cause** of a case of erythema multiforme, not as a treatment. No clinical trial in the retrieved set tests hydrocortisone acetate as a therapy for erythema multiforme; all four trials returned are off-target (unrelated drugs/diseases, graded "C" for relevance).

In short, the mechanistic plausibility that exists for hydrocortisone acetate's anti-inflammatory effects does not extend to this specific prediction — the available evidence points in the opposite direction (adverse reaction) rather than supporting therapeutic benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02153762](https://clinicaltrials.gov/study/NCT02153762) | NA | Completed | 41 | Application-order study of Locoid Lipocream (hydrocortisone **butyrate**, not acetate) and Hylatopic Plus in atopic dermatitis — unrelated drug salt and indication (Grade C) |
| [NCT00332163](https://clinicaltrials.gov/study/NCT00332163) | Phase 2 | Completed | 95 | Prophylactic vs. reactive treatment of EGFR-inhibitor–related skin toxicity in metastatic colorectal cancer patients — not hydrocortisone acetate, not EM (Grade C) |
| [NCT05468372](https://clinicaltrials.gov/study/NCT05468372) | Phase 2 | Recruiting | 50 | Amphotericin B vs. posaconazole for pulmonary mucormycosis — unrelated to hydrocortisone acetate or EM (Grade C) |
| [NCT01650194](https://clinicaltrials.gov/study/NCT01650194) | Phase 2 | Completed | 60 | Enzalutamide plus abiraterone acetate in metastatic prostate cancer — unrelated (Grade C) |

None of the retrieved trials directly test hydrocortisone acetate for erythema multiforme; all are graded C (low relevance / knowledge-graph noise).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696380](https://pubmed.ncbi.nlm.nih.gov/10696380/) | 1999 | Case Report | The Journal of Laryngology and Otology | A 4-year-old girl developed erythema multiforme after topical aural application of Gentisone HC drops (hydrocortisone acetate 1% + gentamicin) for post-grommet otorrhoea — reported as an **adverse drug reaction**, not a treatment effect |

---

## Malaysia Market Information

NPRA records confirm the product is marketed with **34 total registrations**, but detailed per-license fields (authorization number, product name, dosage form, approved indication) were not populated in this data extract and cannot be reported here without fabricating values.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this data extract — DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for this indication is effectively zero, evidence level is L5 (no supportive studies), and the only literature identified documents hydrocortisone acetate **causing** erythema multiforme as a hypersensitivity reaction — evidence that runs counter to, not in support of, the proposed therapeutic use.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a blocking data gap — DG001)
- Verified mechanism of action data (DG002)
- Any genuine preclinical or mechanistic evidence for corticosteroid benefit in erythema multiforme, distinct from the single contradictory adverse-event case report
- Consider redirecting evaluation effort to the **Hemorrhoid** candidate in this same pack (rank 2, Evidence Level L1, multiple completed Phase 2 RCTs, "Proceed with Guardrails"), which represents a substantially stronger and already clinically established signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

