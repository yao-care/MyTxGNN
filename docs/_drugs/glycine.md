---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 5
---

# Glycine
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

# Glycine: From Unspecified Original Indication to Pharyngitis

## One-Sentence Summary

Glycine (DrugBank DB00145) is a simple amino acid with no original indication recorded in the current data pack. The TxGNN model's top-ranked prediction is **Pharyngitis**, but the prediction score is **0.00%** and none of the associated clinical trials or literature directly study glycine for this condition — the supporting evidence is currently keyword-matched noise rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current records (no license text or MOA available) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 209 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for glycine. Glycine is a small, non-essential amino acid and inhibitory neurotransmitter, widely marketed as an injectable irrigation/infusion solution, nutritional supplement, and pharmaceutical excipient — but no original indication text could be extracted from the 209 Malaysia registrations on file, and no combination/class context is recorded to anchor a mechanistic rationale.

The TxGNN score for pharyngitis is 0.0, meaning the knowledge-graph model itself found no meaningful support for this link — it appears only because it was ranked first among low-confidence candidates. The seven associated publications cover antibacterial compound discovery, psoriasis models, roxadustat renal anemia trials, glyphosate poisoning, and Group A Streptococcus carriage genetics; only one paper (PMID 1112054, 1975) is even topically adjacent, reporting glycine as one of many free amino acids measured in human tonsillar tissue — a biochemical background finding, not evidence of therapeutic effect. Overall, there is no coherent mechanistic bridge between glycine's known pharmacology and pharyngitis treatment based on the evidence gathered so far.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03656198](https://clinicaltrials.gov/study/NCT03656198) | Phase 4 | Completed | 546 | Studies non-specific effects of **rabies vaccine** on common infectious disease incidence; does not test glycine — flagged as a keyword mismatch (relevance grade C). |
| [NCT04678830](https://clinicaltrials.gov/study/NCT04678830) | Phase 2 | Completed | 56 | Evaluates **leronlimab** for prolonged COVID-19 symptoms; unrelated to glycine or pharyngitis (relevance grade C). |

Neither trial provides direct evidence for glycine in pharyngitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1112054](https://pubmed.ncbi.nlm.nih.gov/1112054/) | 1975 | Cohort | Clinical Chemistry | Measured free amino acids (including glycine) in human tonsillar tissue — indirect biochemical background only, not a treatment study. |
| [32493693](https://pubmed.ncbi.nlm.nih.gov/32493693/) | 2020 | RCT | J Am Soc Nephrol | Roxadustat vs. darbepoetin alfa for CKD anemia on hemodialysis; not related to glycine or pharyngitis. |
| [31891449](https://pubmed.ncbi.nlm.nih.gov/31891449/) | 2020 | RCT | Ther Apher Dial | Oral roxadustat for CKD anemia; unrelated (likely a drug-matching artifact). |
| [26283331](https://pubmed.ncbi.nlm.nih.gov/26283331/) | 2015 | Review | Infection and Immunity | Sensor kinase mutation linked to Group A Streptococcus carriage after acute pharyngitis; genomics study, not a glycine treatment study. |
| [38043864](https://pubmed.ncbi.nlm.nih.gov/38043864/) | 2024 | Review | Journal of Proteomics | Antibacterial mechanism of compound TMC-154 against *S. pyogenes*; unrelated to glycine. |
| [34603060](https://pubmed.ncbi.nlm.nih.gov/34603060/) | 2021 | Review | Frontiers in Pharmacology | Herbal extract (*Pithecellobium clypearia*) mechanism in a psoriasis mouse model, with historical use for pharyngitis; not a glycine study. |
| [23291146](https://pubmed.ncbi.nlm.nih.gov/23291146/) | 2013 | Review | Forensic Science International | Case series of **glyphosate** (herbicide) acute poisoning; unrelated to glycine — likely a name-similarity mismatch. |

None of these publications constitute direct evidence of glycine's efficacy in pharyngitis.

## Malaysia Market Information

Taiwan/NPRA regulatory records show **209 total registrations** with market status "已上市" (Marketed), but the license-level fields (registration number, product name, dosage form, manufacturer, indication text) returned empty for all sampled entries in this evidence pack. No usable per-product table can be presented until license records are re-queried.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available; TFDA label warnings/contraindications are flagged as a **blocking** data gap in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for pharyngitis is 0.0 with no supporting mechanism, and all associated clinical trials and nearly all literature are keyword mismatches rather than genuine glycine-pharyngitis evidence — this does not meet even L4 threshold, let alone support progression.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (currently blocking further safety review)
- Verified mechanism of action (MOA) data from DrugBank or primary literature
- Corrected/re-run evidence search with tighter drug-name disambiguation (current results are contaminated by glyphosate, roxadustat/daprodustat, and unrelated vaccine trials)
- Complete license-level records (product name, dosage form, approved indication text) for the 209 Malaysia registrations
- If pursuing further, evaluate the more evidence-backed but confounded **common cold** candidate (rank 4, L3/S1) separately, noting glycine's role there is likely as a zinc-stabilizing excipient rather than the active moiety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

