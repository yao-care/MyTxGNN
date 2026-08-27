---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From Topical Analgesic (Rubefacient) Use to Migraine Disorder

## One-Sentence Summary

Camphor is a widely marketed OTC ingredient traditionally used as a topical rubefacient/counter-irritant (e.g., balms and liniments applied for muscular aches and headache relief). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is currently supported only by **0 clinical trials** and **5 loosely related publications** — most of which describe adverse effects or unrelated drugs rather than efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical analgesic / rubefacient (OTC liniments and balms); no TFDA/NPRA-registered indication text was returned in this data extract |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 297 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Camphor is not available in DrugBank. Based on available information, Camphor is a monoterpene ketone widely used as a topical rubefacient/counter-irritant in OTC liniments and balms (e.g., Tiger Balm–type products), where it is understood to activate and modulate TRP channels (TRPV1, TRPA1, TRPM8), producing a warming/cooling sensory effect similar to menthol.

This sensory mechanism plausibly explains the TxGNN association: camphor-menthol balms are commonly applied to the temples in folk and OTC self-care practice for symptomatic headache/migraine relief, which likely created a strong co-occurrence signal in the underlying knowledge graph.

However, this is a local, symptomatic counter-irritant mechanism — it does not engage the disease-modifying pathways targeted by modern migraine therapeutics (e.g., the CGRP receptor pathway). Furthermore, the supporting literature (below) contains signals suggesting camphor-containing products may *trigger or worsen* headache in some individuals, which weakens rather than strengthens the repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT | The Journal of Headache and Pain | Phase 3 RCT of erenumab (a CGRP-receptor monoclonal antibody, unrelated to Camphor) for chronic migraine prevention in Asian patients; surfaced by keyword overlap on "migraine," not Camphor-specific evidence |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review/Historical | Zeitschrift für Kinder- und Jugendpsychiatrie und Psychotherapie | Historical review of 1940s–50s neuropsychopharmacology; does not provide Camphor-specific efficacy data for migraine |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | 5 cases of cluster headache linked to toothpastes containing pro-convulsant essential oils; a safety/triggering signal, not efficacy evidence |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | 2 cases of cluster headache temporally associated with toothpaste containing camphor and eucalyptus oils; supports an adverse/triggering association rather than therapeutic benefit |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Case Report/Historical | Minerva Medica | Historical Italian-language report on therapy for "essential hemicrania"; abstract unavailable, content unverified |

---

## Safety Considerations

No structured TFDA/NPRA warning, contraindication, or drug-interaction data is currently available for Camphor (DDI query status: not found). Please refer to the package insert for safety information.

**Additional signals from literature (not part of the structured safety dataset, but relevant to this repurposing hypothesis):**
- An oral toxicology study in rats reported dose-dependent oxidative stress and histopathological tissue damage with edible camphor administration ([PMID 27955803](https://pubmed.ncbi.nlm.nih.gov/27955803/)).
- Multiple case reports describe camphor-containing topical/oral products triggering or worsening cluster headache and migraine-type symptoms ([PMID 35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/), [PMID 34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/)), consistent with camphor's known pro-convulsant potential at high exposure.

These findings should be treated as caution signals, not confirmatory safety data, until the formal TFDA label (warnings/contraindications) is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to L4 (case reports/series and one unrelated-drug RCT pulled in by keyword overlap); no Camphor-specific clinical trial or controlled study supports migraine efficacy. Critically, a **Blocking** data gap (TFDA warnings/contraindications not yet obtained) prevents the mandatory S1 safety screening, and the available literature leans toward a headache-triggering risk signal rather than therapeutic benefit — undermining rather than supporting the repurposing hypothesis at this stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- DrugBank MOA and DDI profile — currently a High-priority gap (DG002)
- Camphor-specific preclinical or clinical data testing a plausible anti-migraine mechanism (e.g., CGRP pathway or validated TRP-channel modulation with headache outcome measures)
- Re-curation of the literature evidence base to exclude keyword-collision results (e.g., the erenumab RCT) and to correctly classify adverse-effect case reports as safety signals rather than efficacy support
- Malaysia licence-level detail (product names, dosage forms, approved indication text) for the 297 registered products, which was not returned in this data extract
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

