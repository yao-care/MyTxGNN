---
layout: default
title: Fusidic Acid
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 5
---

# Fusidic Acid
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

# Fusidic Acid: From Staphylococcal Infection to Ornithosis

## One-Sentence Summary

Fusidic Acid (DrugBank DB02703) is a long-established antistaphylococcal antibiotic marketed in Malaysia under 38 registrations. The TxGNN model's top-ranked new indication, **Ornithosis** (psittacosis), carries a **prediction score of 0%** and is supported by **0 clinical trials** and **0 publications** — the model output itself flags this as a weak, unsupported association rather than a promising repurposing lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no non-empty `approved_indication_text` in the 5 license records provided) |
| Predicted New Indication | Ornithosis |
| TxGNN Prediction Score | 0% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 38 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged in the evidence pack as a High-severity data gap). Based on general pharmacological knowledge, fusidic acid inhibits bacterial protein synthesis by blocking elongation factor G (EF-G)-mediated ribosomal translocation, and its established antibacterial activity is concentrated against Gram-positive organisms, particularly *Staphylococcus aureus*.

Ornithosis (psittacosis) is caused by *Chlamydia psittaci*, an obligate intracellular pathogen structurally and mechanistically distant from the Gram-positive bacteria fusidic acid is known to target. The standard treatment class for this pathogen is tetracyclines, not fusidic acid. The evidence pack's own mechanistic rationale for this candidate explicitly states the link is weak, with no clinical or literature support identified.

Across all five TxGNN-ranked candidates in this pack (ornithosis, superior limbic keratoconjunctivitis, cholera, gastrointestinal anthrax, typhus), every prediction score is 0%, every evidence level is L5, and every recommendation is Hold. Only "gastrointestinal anthrax" (rank 4) has a plausible mechanistic rationale (Gram-positive *Bacillus anthracis* falls within fusidic acid's known spectrum), but even that candidate has zero supporting trials or literature. This pattern indicates the model output for this drug is currently exploratory only, not evidence-backed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked indication (Ornithosis).

*Note: two PubMed records were retrieved for the lower-ranked "cholera" candidate (PMID [31762145](https://pubmed.ncbi.nlm.nih.gov/31762145/), a structural/basic-science study of chloramphenicol acetyltransferases in *Vibrio*, and PMID [15950082](https://pubmed.ncbi.nlm.nih.gov/15950082/), a molecular epidemiology study of *Shigella dysenteriae*), but neither directly studies fusidic acid treatment of cholera, and both are Tier 3 (basic science/epidemiology, not clinical efficacy) evidence.*

## Malaysia Market Information

NPRA records show 38 total registrations with active marketed status, but individual authorisation details (registration number, product name, dosage form, approved indication text) were not populated in this evidence pack — all 5 sampled license records contain empty fields. This should be resolved before any regulatory-facing use of this report.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are flagged as data gaps in this evidence pack — notably DG001, a Blocking-severity gap on TFDA/NPRA label warnings and contraindications, which prevents safety pre-screening.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Ornithosis) has a 0% TxGNN score, L5 evidence (model prediction only), no clinical trials, no literature, and an explicitly weak mechanistic rationale. All four other ranked candidates in this pack share the same pattern. There is currently no basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Complete license/indication text for the 38 Malaysia registrations (all 5 sampled records were empty)
- If this candidate is to be pursued further, targeted literature/preclinical search specifically on fusidic acid activity against *Chlamydia psittaci* (none found to date)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

