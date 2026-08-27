---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 5
---

# Caffeine
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

# Caffeine: From Analgesic Adjuvant / CNS Stimulant to Headache Disorder

## One-Sentence Summary

Caffeine (DrugBank DB00201) is marketed in Malaysia across 10 registered products and is broadly recognized as a CNS stimulant and analgesic adjuvant. Of the five candidate indications screened in this evidence pack, **Headache Disorder** (including migraine and tension-type headache) is the strongest-supported new indication, backed by **4 completed Phase 3/4 clinical trials** (the largest enrolling 1,889 patients) and roughly **20 relevant publications**, earning the highest evidence rating (L2) among all candidates evaluated for this drug.

> Note: This evidence pack also screened caffeine against pharyngitis, vasomotor rhinitis, common cold, and nasopharyngitis. Those candidates returned only weak or tangential evidence (L3–L5, "Hold") and are not the focus of this report — see the closing note for details.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the current NPRA license dataset (approved indication text was not extracted for any of the 10 records). Caffeine is generally recognized as a CNS stimulant / analgesic adjuvant. |
| Predicted New Indication | Headache Disorder (migraine, tension-type headache) |
| TxGNN Prediction Score | Not available — the model score field returned 0.0 across all candidates in this dataset (likely an unpopulated data field); the qualitative evidence rating below is used instead |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data from DrugBank was not available in this dataset (flagged as data gap DG002). Based on established pharmacology captured in the evidence pack's own repurposing rationale, caffeine acts as an **adenosine receptor (A1/A2A) antagonist**. This produces cerebral vasoconstriction and potentiates the analgesic effect of NSAIDs and acetaminophen on the prostaglandin pathway — the long-standing pharmacological basis for caffeine's inclusion in OTC combination analgesics (e.g., acetaminophen/aspirin + caffeine).

Because the original NPRA-approved indication text was not captured for any of caffeine's 10 Malaysian licenses, a direct "original indication → new indication" comparison cannot be made from this dataset. However, caffeine's well-documented role as an analgesic adjuvant is mechanistically continuous with headache/migraine treatment: it is already a component of several internationally marketed fixed-dose headache products (e.g., acetaminophen+aspirin+caffeine, ibuprofen+caffeine, rizatriptan+caffeine).

A second, bidirectional mechanistic link strengthens this candidate: caffeine **withdrawal** is itself a recognized trigger of headache, meaning both chronic caffeine intake patterns and acute caffeine dosing are clinically entangled with headache pathophysiology — a relationship reflected across the literature evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02183688](https://clinicaltrials.gov/study/NCT02183688) | Phase 3 | Completed | 1889 | RCT confirming the combination rationale of ASA + paracetamol + caffeine vs. ASA + paracetamol and the individual agents in headache patients |
| [NCT01755702](https://clinicaltrials.gov/study/NCT01755702) | Phase 2/3 | Terminated | 66 | Fast-absorbing paracetamol + caffeine vs. placebo and OTC paracetamol/ibuprofen for episodic tension-type headache; terminated early (reason not captured in dataset) |
| [NCT01248468](https://clinicaltrials.gov/study/NCT01248468) | Phase 4 | Completed | 752 | Aspirin + acetaminophen + caffeine (AAC) vs. sumatriptan vs. placebo for acute migraine |
| [NCT00471952](https://clinicaltrials.gov/study/NCT00471952) | Phase 3 | Completed | 50 | Rizatriptan (Maxalt) 10mg alone vs. combined with caffeine 75mg for acute migraine attacks |
| [NCT01080677](https://clinicaltrials.gov/study/NCT01080677) | Phase 2 | Completed | 60 | Dose-ranging safety/efficacy study of caffeine + propranolol for acute migraine |
| [NCT02115269](https://clinicaltrials.gov/study/NCT02115269) | N/A (real-world) | Completed | 759 | Indomethacin + prochlorperazine + caffeine (IndoProCaf) effervescent tablets for acute migraine/tension-type headache in routine practice (Ukraine/Kazakhstan) |
| [NCT01629329](https://clinicaltrials.gov/study/NCT01629329) | Phase 4 | Terminated | 93 | Acetaminophen + aspirin + caffeine vs. IV prochlorperazine for acute migraine in the ED (non-inferiority design) |
| [NCT03951649](https://clinicaltrials.gov/study/NCT03951649) | Phase 4 | Completed | 62 | Occipital nerve block vs. oral acetaminophen + caffeine for acute headache treatment in pregnancy |
| [NCT01172405](https://clinicaltrials.gov/study/NCT01172405) | Phase 3 | Unknown | 144 | Ibuprofen + caffeine vs. ibuprofen alone for headache attacks (efficacy and tolerability) |
| [NCT07022496](https://clinicaltrials.gov/study/NCT07022496) | Phase 4 | Recruiting | 120 | Oral caffeine (from green tea) to abort acute migraine attacks; currently enrolling |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39371383](https://pubmed.ncbi.nlm.nih.gov/39371383/) | 2024 | RCT | Iranian Journal of Medical Sciences | Randomized double-blind trial showing acetaminophen + caffeine reduced incidence of post-dural-puncture headache after spinal anesthesia for cesarean section |
| [32731623](https://pubmed.ncbi.nlm.nih.gov/32731623/) | 2020 | Review | Nutrients | Comprehensive review of caffeine's dual role in migraine — both as a trigger and as an adjunct treatment |
| [25728949](https://pubmed.ncbi.nlm.nih.gov/25728949/) | 2017 | Review | Neurologia | Chronic caffeine use can promote cortical hyperexcitability worsening primary headache, while acute/intermittent use provides analgesic-adjuvant benefit |
| [33974014](https://pubmed.ncbi.nlm.nih.gov/33974014/) | 2021 | Review | JAMA | Clinical review of headache diagnosis and management, situating caffeine-containing analgesic combinations within standard care |
| [40378325](https://pubmed.ncbi.nlm.nih.gov/40378325/) | 2025 | Review | American Family Physician | Current migraine prophylaxis guidance, including analgesic-overuse thresholds relevant to caffeine-combination products |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Guideline | Annals of Internal Medicine | 2023 VA/DoD clinical practice guideline for headache management, referencing combination analgesics |
| [32449944](https://pubmed.ncbi.nlm.nih.gov/32449944/) | 2020 | Review | Headache | Systematic review of dietary/nutritional migraine triggers and treatments, including caffeine's dual role |
| [26677204](https://pubmed.ncbi.nlm.nih.gov/26677204/) | 2016 | Review | Practical Neurology | Overview of caffeine's neurological effects — improved alertness/mood balanced against migraine and sleep disturbance risk |
| [34865666](https://pubmed.ncbi.nlm.nih.gov/34865666/) | 2022 | Review | Psychological Medicine | Explores the relationship between ADHD, headache, and caffeine use |
| [15448977](https://pubmed.ncbi.nlm.nih.gov/15448977/) | 2004 | Review | Psychopharmacology | Foundational review validating caffeine-withdrawal headache as a clinically significant syndrome — relevant to dosing/discontinuation guardrails |

---

## Malaysia Market Information

NPRA registry data confirms caffeine is currently marketed in Malaysia across **10 registrations**, but line-item details (license number, product name, dosage form, manufacturer, approved indication text) were not captured in this dataset — all five sampled license records returned blank fields. This is logged as a **Blocking** data gap (DG001) and must be resolved (via TFDA/NPRA package-insert retrieval) before any regulatory-facing use of this report.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data were available in this dataset (DDI query status: not found, 0 interactions returned). Retrieval of the official package insert is flagged as a **Blocking** data gap (DG001) and is required before this candidate can advance past initial safety screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Headache disorder is supported by 4 completed Phase 3/4 trials (including a 1,889-patient RCT) and a consistent body of review-level literature establishing caffeine's mechanistic and clinical role as an analgesic adjuvant — the strongest evidence profile (L2) of any candidate in this evidence pack. However, nearly all supporting trials test caffeine as part of a **fixed-dose combination** (with acetaminophen, aspirin, ibuprofen, or triptans) rather than as monotherapy, and core safety/regulatory data (package insert, contraindications, DDIs, confirmed original indication) are currently missing.

**To proceed, the following is needed:**
- Official NPRA-approved indication text and package insert (warnings, contraindications, DDIs) — currently a Blocking gap (DG001)
- Structured DrugBank mechanism-of-action data — currently a High-priority gap (DG002)
- Clarification of whether the repositioning claim should target caffeine monotherapy or caffeine-as-adjuvant within combination products, since almost all trial evidence is combination-based
- Review of termination/withdrawal/suspension reasons for NCT01755702, NCT01629329, NCT01426971, and NCT02582996 before those trials are counted as fully supportive evidence
- If a broader-indication strategy is desired, note that pharyngitis, vasomotor rhinitis, common cold, and nasopharyngitis were also screened in this pack but returned only weak/indirect evidence (L3–L5) and are recommended for **Hold**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

