---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 5
---

# Chloramphenicol
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

# Chloramphenicol: From Broad-Spectrum Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Chloramphenicol is a broad-spectrum antibiotic with decades of established use against severe bacterial infections. The TxGNN model's top-ranked candidate indication is **Paratyphoid Fever**, supported by **0 registered clinical trials** and **20 literature records** — but the underlying evidence indicates this is a re-identification of a long-established classic use rather than a novel repurposing signal, and a **Blocking** data gap in TFDA/label safety information currently prevents formal safety screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from license data (all `approved_indication_text` fields empty); chloramphenicol is a well-established broad-spectrum antibiotic historically indicated for severe bacterial infections (e.g., typhoid fever, bacterial meningitis) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 0.00% (reported as 0.0 despite rank 1 — likely a pipeline/data population issue, not a true confidence value; flagged for source verification) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 12 |
| Recommended Decision | Hold (see Conclusion — overridden from the indication-level "Proceed with Guardrails" due to a Blocking safety data gap) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on known pharmacology, chloramphenicol is a broad-spectrum amphenicol-class antibiotic that inhibits bacterial protein synthesis (50S ribosomal subunit) and is bactericidal/bacteriostatic against a wide range of Gram-positive, Gram-negative, and intracellular organisms, including *Salmonella enterica* serovar Paratyphi.

Importantly, the evidence pack's own rationale for this candidate states that chloramphenicol is the **traditional standard therapy** for enteric fever (typhoid/paratyphoid), and explicitly flags this as an "已確立之經典用途，非探索性訊號" — i.e., **not a novel repurposing signal**, but a confirmation of an already well-documented historical indication. Supporting literature (e.g., PMID 36420914, a 2022 Cochrane review) notes that WHO currently recommends azithromycin, ciprofloxacin, or ceftriaxone as first-line therapy due to widespread resistance to older agents like chloramphenicol — meaning its clinical relevance today is largely as a historical/comparator or resource-limited-setting option rather than a genuine new-indication opportunity.

Mechanistically the link is sound, but the "prediction" value here is low: TxGNN appears to have surfaced a drug-disease pair that is already textbook-established rather than an unexplored hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [417191](https://pubmed.ncbi.nlm.nih.gov/417191/) | 1978 | RCT | J Trop Med Hyg | Comparative trial of co-trimoxazole vs. chloramphenicol in 91 typhoid/paratyphoid patients; co-trimoxazole effective, chloramphenicol used as active comparator |
| [8203854](https://pubmed.ncbi.nlm.nih.gov/8203854/) | 1994 | RCT | Antimicrob Agents Chemother | Randomized comparison of aztreonam vs. chloramphenicol (50 mg/kg/day) in 44 typhoid fever patients |
| [14072634](https://pubmed.ncbi.nlm.nih.gov/14072634/) | 1964 | RCT | Br Med J | Comparison of ampicillin and chloramphenicol in treatment of paratyphoid fever |
| [18843659](https://pubmed.ncbi.nlm.nih.gov/18843659/) | 2008 | Cochrane Review | Cochrane Database Syst Rev | Fluoroquinolones vs. other antibiotics (incl. chloramphenicol as historical comparator) for enteric fever |
| [18843701](https://pubmed.ncbi.nlm.nih.gov/18843701/) | 2008 | Cochrane Review | Cochrane Database Syst Rev | Azithromycin for uncomplicated typhoid/paratyphoid fever; comparator context includes chloramphenicol |
| [36420914](https://pubmed.ncbi.nlm.nih.gov/36420914/) | 2022 | Cochrane Review | Cochrane Database Syst Rev | Current WHO first-line agents are azithromycin, ciprofloxacin, ceftriaxone due to resistance to older drugs including chloramphenicol |
| [21975746](https://pubmed.ncbi.nlm.nih.gov/21975746/) | 2011 | Cochrane Review | Cochrane Database Syst Rev | Fluoroquinolones for enteric fever; WHO recommends fluoroquinolones in areas resistant to older first-line antibiotics |
| [6084470](https://pubmed.ncbi.nlm.nih.gov/6084470/) | 1984 | Cohort/Dosage study | Ann Trop Paediatr | 109 children with enteric fever: higher-dose chloramphenicol (100 mg/kg/24h) had lower treatment failure (24%) vs. lower dose (63%) |
| [11726293](https://pubmed.ncbi.nlm.nih.gov/11726293/) | 2001 | Retrospective cohort | J Travel Med | 10-year retrospective review of 41 enteric fever cases in a Parisian hospital, evaluating treatment trends |
| [35871037](https://pubmed.ncbi.nlm.nih.gov/35871037/) | 2022 | Retrospective cohort | J Formos Med Assoc | Clinical/microbiological features of 37 indigenous and imported enteric fever cases in Taiwan, 2010–2020 |

---

## Malaysia Market Information

Malaysia currently has **12 active marketing authorizations** for chloramphenicol (Market Status: ✓ Marketed). However, individual authorization numbers, product names, dosage forms, and approved indication texts were not returned by the current data source (all `licenses[]` entries are empty) and require a separate NPRA product-level lookup to populate.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** This is a Blocking data gap (DG001) — TFDA/label warnings, contraindications, and drug interaction data are all unavailable, which prevents the candidate from formally entering the S1 safety initial-review stage. Chloramphenicol is independently known (outside this evidence pack) to carry serious hematological risks (e.g., aplastic anemia, "gray baby syndrome"); these should be confirmed against the official label once available rather than assumed from general knowledge.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The indication-level scoring for paratyphoid fever (L2 evidence, decision stage S3) suggests "Proceed with Guardrails," but this is overridden at the drug level by a **Blocking** data gap (DG001: TFDA label warnings/contraindications unavailable), which the evidence pack itself flags as preventing entry into safety initial review (S1).
- The prediction also reflects an already-established classic indication rather than a novel repurposing signal, and current clinical guidelines have largely superseded chloramphenicol with newer agents for this indication due to resistance.

**To proceed, the following is needed:**
- TFDA label PDF (warnings, contraindications) — resolves DG001 (Blocking)
- DrugBank MOA data — resolves DG002
- Verification of the TxGNN score field (currently 0.0 for all 5 ranked candidates, which is inconsistent with a top-rank result)
- NPRA product-level license details (authorization numbers, product names, approved indication text)
- Clinical assessment of current relevance given resistance patterns and WHO's preference for azithromycin/ciprofloxacin/ceftriaxone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

