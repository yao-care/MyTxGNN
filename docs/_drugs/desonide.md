---
layout: default
title: Desonide
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Desonide
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

# Desonide: From Corticosteroid-Responsive Dermatoses to Atopic Eczema

## One-Sentence Summary

> Desonide is a low-potency (Class VI) topical corticosteroid generally used for corticosteroid-responsive dermatoses.
> The TxGNN model predicts it is effective for **Atopic Eczema**, a use for which desonide already carries substantial direct clinical support —
> **9 clinical trials** and **20 publications** are available, several using desonide itself in atopic dermatitis populations.

*Note: This evidence pack's TFDA/NPRA license fields (product name, dosage form, approved-indication text) were returned blank, so the "original indication" below is derived from desonide's well-established pharmacological class rather than a specific label extract.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Corticosteroid-responsive dermatoses (topical low-potency corticosteroid class; specific TFDA/NPRA label text not provided in this evidence pack) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 35 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Desonide is a low-potency (Class VI) topical corticosteroid. Its anti-inflammatory action is thought to work through inhibition of the phospholipase A2 / arachidonic acid pathway and suppression of pro-inflammatory cytokine release, reducing epidermal inflammation. This mechanism maps directly onto the immune-inflammatory pathology underlying atopic eczema (atopic dermatitis).

Importantly, this is not a novel repurposing signal in the strict sense: atopic eczema/dermatitis is already a well-established, approved use for desonide in multiple markets. Several of the supporting trials and publications use desonide products (Desonide Gel/Hydrogel/Cream/Foam, e.g. Desonate™) directly in pediatric and adult atopic dermatitis populations, which is why the evidence level here is graded L1 rather than a purely speculative L4/L5 mechanistic extrapolation.

Detailed drug-level mechanism-of-action data (structured MOA field) was not available in this evidence pack (flagged as a data gap), but the mechanistic rationale above is derived from the repurposing evidence and is consistent with the established pharmacology of low-potency topical corticosteroids.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00690833](https://clinicaltrials.gov/study/NCT00690833) | Phase 4 | Completed | 41 | Efficacy of Desonide (Desonate™) Gel 0.05% in younger and older subjects with atopic dermatitis; direct drug-indication-population match. |
| [NCT02732314](https://clinicaltrials.gov/study/NCT02732314) | Phase 4 | Completed | 53 | 13-week randomized, double-blind study of new topical corticosteroid formulations (desonide-class) in atopic dermatitis, SCORAD >16. |
| [NCT00828412](https://clinicaltrials.gov/study/NCT00828412) | Phase 4 | Completed | 100 | Multicenter pilot comparing EpiCeram skin barrier emulsion vs. Desonide Cream 0.05% (twice daily) in pediatric moderate atopic dermatitis. |
| [NCT02286700](https://clinicaltrials.gov/study/NCT02286700) | Phase 3 | Unknown | 42 | Double-blind active-control study comparing amino acid moisturizing cream vs. Desonide Cream in mild-to-moderate atopic dermatitis/eczema. |
| [NCT03386032](https://clinicaltrials.gov/study/NCT03386032) | Phase 3 | Completed | 65 | 8-week atopic dermatitis treatment study evaluating an experimental cream via SCORAD; drug identity not fully confirmed as desonide. |
| [NCT01779258](https://clinicaltrials.gov/study/NCT01779258) | Phase 3 | Completed | 347 | Emollients (not desonide) for flare prevention in pediatric atopic dermatitis maintenance therapy. |
| [NCT01467362](https://clinicaltrials.gov/study/NCT01467362) | Phase 3 | Completed | 251 | Emollient efficacy on xerosis in children with atopic dermatitis; vehicle-controlled, not a corticosteroid trial. |
| [NCT03397979](https://clinicaltrials.gov/study/NCT03397979) | N/A | Completed | 63 | Bathing-frequency comparison (soak-and-seal) alongside topical corticosteroid use in pediatric atopic dermatitis. |
| [NCT07295678](https://clinicaltrials.gov/study/NCT07295678) | N/A | Not yet recruiting | 44 | Medical device (non-steroidal cream) evaluated alongside dermocorticoids for atopic dermatitis; not a desonide drug trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17373176](https://pubmed.ncbi.nlm.nih.gov/17373176/) | 2007 | RCT | J Drugs Dermatol | Safety and efficacy of desonide hydrogel 0.05% in pediatric atopic dermatitis, including children under 2 years. |
| [7601950](https://pubmed.ncbi.nlm.nih.gov/7601950/) | 1995 | RCT | J Am Acad Dermatol | Long-term multicenter comparison of 0.05% desonide vs. 1% hydrocortisone ointment in pediatric atopic dermatitis. |
| [12121395](https://pubmed.ncbi.nlm.nih.gov/12121395/) | 2002 | RCT | Australas J Dermatol | Desonide 0.05% lotion (Desowen) vs. vehicle for facial atopic/seborrhoeic dermatitis: efficacy, tolerance, cosmetic acceptability. |
| [10930856](https://pubmed.ncbi.nlm.nih.gov/10930856/) | 2000 | RCT | Ann Dermatol Venereol | Micronised desonide cream 0.1% vs. betamethasone dipropionate cream in childhood atopic dermatitis, including cortisol monitoring. |
| [31551225](https://pubmed.ncbi.nlm.nih.gov/31551225/) | 2019 | RCT | Pak J Pharm Sci | Mucopolysaccharide polysulfate ointment combined with desonide ointment for infantile eczema. |
| [18301804](https://pubmed.ncbi.nlm.nih.gov/18301804/) | 2008 | Review | Drugs Today | Review of desonide foam 0.05%, effective vs. vehicle in mild-to-moderate atopic dermatitis (pediatric and adult). |
| [31424707](https://pubmed.ncbi.nlm.nih.gov/31424707/) | 2019 | Review | J Drugs Dermatol | Review of topical corticosteroid foams, including desonide-class agents. |
| [20514788](https://pubmed.ncbi.nlm.nih.gov/20514788/) | 2010 | Cohort | J Drugs Dermatol | Adherence and early efficacy program for desonide hydrogel in atopic dermatitis patients. |
| [18638631](https://pubmed.ncbi.nlm.nih.gov/18638631/) | 2008 | Cohort | J Am Acad Dermatol | Safety of desonide foam 0.05% in children as young as 3 months. |
| [35986531](https://pubmed.ncbi.nlm.nih.gov/35986531/) | 2023 | Preclinical/PK-PD | Curr Drug Deliv | Desonide nanoemulsion gel for improved transdermal delivery: pharmacodynamic and safety evaluation. |

---

## Malaysia Market Information

Malaysia (NPRA) currently lists **35 registered licenses** for Desonide-containing products with market status "✓ Marketed." However, individual license-level details (registration numbers, product names, dosage forms, and approved-indication text) were not populated in this evidence pack and cannot be tabulated here.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — flagged as a Blocking data gap, DG001 — and are needed before this candidate can complete initial safety screening.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atopic eczema is supported by direct clinical evidence — including desonide-specific Phase 3/4 trials and multiple RCTs — because this is effectively an existing, well-characterized use of desonide rather than a novel mechanistic leap. However, the absence of structured safety-label data (warnings/contraindications/DDI) prevents a full "Go" determination at this time.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, contraindications, and DDI data (DG001, Blocking)
- Structured drug-level mechanism-of-action (MOA) data from DrugBank or equivalent (DG002)
- Individual Malaysia license details (product names, dosage forms, indication text) to confirm marketed formulations match the studied dosage forms (gel/hydrogel/foam/cream)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

