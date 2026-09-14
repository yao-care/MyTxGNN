---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: From Moderate-to-Severe Pain to Osteoarthritis

> **Note on ranking**: TxGNN's single highest-scored candidate is *"osteoarthritis susceptibility"* (rank #1, 99.9985%) — this KG node represents a genetic susceptibility locus, not a treatable clinical indication, and carries no supporting efficacy evidence (only one unrelated mortality-safety paper). This report therefore evaluates the top **clinically actionable** candidate, **osteoarthritis** (rank #2, 99.9945%), which is where essentially all the clinical trial and literature evidence in this pack actually concentrates.

## One-Sentence Summary

Tramadol is a centrally-acting opioid analgesic long used for moderate to severe pain. The TxGNN model additionally scores **Osteoarthritis** very highly among candidate indications, and this direction is already backed by **50 clinical trials** and **20 publications** in the evidence pack — including multiple completed Phase 3 RCTs of tramadol itself in knee/hip OA and Cochrane-level systematic reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe pain (opioid analgesic) — Malaysia-specific licensed indication text not available in this data set |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 34 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action documentation is not available in the regulatory data supplied. Based on well-established pharmacology, tramadol is a weak mu-opioid receptor agonist that also inhibits serotonin and norepinephrine reuptake (an SNRI-like effect), giving it a dual mechanism: opioid-receptor-mediated analgesia plus activation of descending monoaminergic pain-inhibition pathways.

Tramadol's original use is analgesia for moderate-to-severe pain of varied etiology, and osteoarthritis (OA) pain is one of the most common chronic pain conditions this mechanism is already applied to clinically. The proposed "new" indication is therefore not a mechanistic leap — it is a direct extension of tramadol's core pharmacology to a specific, high-prevalence pain population.

This is corroborated by external evidence: both the American Academy of Orthopaedic Surgeons and the American College of Rheumatology/Arthritis Foundation guidelines already list tramadol as a treatment option for knee OA, and multiple completed Phase 3 RCTs (several with >500–1900 enrolled patients) and Cochrane systematic reviews have directly evaluated tramadol's efficacy and safety in OA. In effect, TxGNN has re-discovered a use that is already substantially validated in the literature — which strengthens confidence in the model's signal but also means the "novelty" of this repurposing candidate is limited; the value here is closer to formal indication expansion / evidence consolidation than genuine off-label discovery.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04504812](https://clinicaltrials.gov/study/NCT04504812) | Phase 3 | Completed | 1,937 | Large effectiveness trial of sequenced pain-management strategies (including opioid pathway) for knee OA pain |
| [NCT00833794](https://clinicaltrials.gov/study/NCT00833794) | Phase 3 | Completed | 1,028 | Tramadol HCl Once-a-Day vs placebo: analgesic efficacy, safety, and clinical benefit in OA |
| [NCT00348452](https://clinicaltrials.gov/study/NCT00348452) | Phase 3 | Completed | 1,000 | Dose-ranging RCT of tramadol HCl ER (100/200/300mg) vs celecoxib vs placebo in knee/hip OA |
| [NCT00832416](https://clinicaltrials.gov/study/NCT00832416) | Phase 3 | Completed | 565 | Four-arm dose-response RCT: tramadol OAD 100/200/300mg vs placebo for knee OA pain |
| [NCT00852917](https://clinicaltrials.gov/study/NCT00852917) | Phase 3 | Completed | 552 | Same dose-response design with 7-day follow-up extension |
| [NCT00950651](https://clinicaltrials.gov/study/NCT00950651) | Phase 3 | Completed | 431 | Double-blind, double-dummy RCT comparing tramadol HCl/Contramid® once-daily vs tramadol HCl SR twice-daily in knee OA |
| [NCT00833911](https://clinicaltrials.gov/study/NCT00833911) | Phase 3 | Completed | 392 | Open-label long-term (6–12 month) safety study of tramadol HCl OAD 300mg in knee OA |
| [NCT00912015](https://clinicaltrials.gov/study/NCT00912015) | Phase 3 | Completed | 238 | Extension protocol + open-label long-term safety follow-up of tramadol OAD (up to 400mg) |
| [NCT01063842](https://clinicaltrials.gov/study/NCT01063842) | Phase 4 | Completed | 250 | Titration vs fixed-dose tramadol/acetaminophen (Ultracet) tolerability in Korean OA patients |
| [NCT01019265](https://clinicaltrials.gov/study/NCT01019265) | Phase 4 | Completed | 170 | Head-to-head RCT: buprenorphine transdermal patch vs oral tramadol SR in moderate-severe OA pain |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31132298](https://pubmed.ncbi.nlm.nih.gov/31132298/) | 2019 | Cochrane Review | Cochrane Database Syst Rev | Updated Cochrane review of tramadol for OA pain and disability |
| [34251756](https://pubmed.ncbi.nlm.nih.gov/34251756/) | 2023 | Systematic Review / Network Meta-Analysis | Arthritis Care & Research | Efficacy and safety of tramadol for knee/hip OA across RCTs |
| [17343302](https://pubmed.ncbi.nlm.nih.gov/17343302/) | 2007 | Meta-Analysis | J Rheumatology | Tramadol for OA: systematic review and meta-analysis of analgesic effectiveness and safety |
| [16856101](https://pubmed.ncbi.nlm.nih.gov/16856101/) | 2006 | Cochrane Review | Cochrane Database Syst Rev | Original Cochrane review establishing tramadol's OA evidence base |
| [31908149](https://pubmed.ncbi.nlm.nih.gov/31908149/) | 2020 | Guideline | Arthritis Care & Research | 2019 ACR/Arthritis Foundation guideline for OA management (hand, hip, knee) |
| [22563589](https://pubmed.ncbi.nlm.nih.gov/22563589/) | 2012 | Guideline | Arthritis Care & Research | ACR 2012 recommendations for pharmacologic/non-pharmacologic OA therapy |
| [30860559](https://pubmed.ncbi.nlm.nih.gov/30860559/) | 2019 | Cohort (safety/mortality) | JAMA | Association of tramadol with all-cause mortality among OA patients — safety signal requiring caution |
| [39420382](https://pubmed.ncbi.nlm.nih.gov/39420382/) | 2024 | Systematic Review / Meta-Analysis | Advances in Rheumatology | Tramadol vs codeine: all-cause mortality and cardiovascular risk in OA, propensity-matched cohorts |
| [38103456](https://pubmed.ncbi.nlm.nih.gov/38103456/) | 2024 | Systematic Review / Meta-Analysis | Int J Orthopaedic and Trauma Nursing | Tramadol use and hip fracture risk in OA patients |
| [40095377](https://pubmed.ncbi.nlm.nih.gov/40095377/) | 2025 | Systematic Review (post-marketing safety) | Drugs | Post-marketing surveillance safety review of anti-OA medications including tramadol |

---

## Malaysia Market Information

Malaysia (NPRA) records show Tramadol as **marketed** with **34 total registrations**, but license-level detail (registration numbers, product names, dosage forms, manufacturers, approved indication text) was not returned by the source query in this evidence pack — all fields were blank. This is a data gap that needs to be closed via a direct NPRA registration lookup before finalizing formulation/route assumptions.

---

## Safety Considerations

Please refer to the package insert for safety information. No usable warnings, contraindications, or drug-drug interaction data were returned in this evidence pack (DDI query status: not found, 0 interactions). Note this overlaps with **DG001** (TFDA/NPRA package insert warnings/contraindications, severity: Blocking) — this gap currently blocks formal S1 safety screening and must be resolved before any clinical guardrails can be specified. Independently of this data gap, published literature above already flags tramadol-specific safety signals in OA populations (all-cause mortality, hip fracture risk, cardiovascular risk vs codeine) that should inform any monitoring plan.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Osteoarthritis is supported by evidence level L1 — multiple large, completed Phase 3 RCTs directly testing tramadol in knee/hip OA, plus Cochrane systematic reviews and ACR/AAOS clinical guidelines that already recommend tramadol as an OA treatment option. However, a Blocking-severity data gap (TFDA/NPRA warnings and contraindications, DG001) prevents completion of the safety pre-screen, and published safety literature (mortality, fracture risk) warrants guardrails rather than an unconditional Go.

**To proceed, the following is needed:**
- Resolve DG001: retrieve and parse the Malaysia (NPRA) package insert PDF for warnings/contraindications
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Obtain complete NPRA license-level detail (product names, dosage forms, manufacturers, approved indication text) — currently blank
- Formal DDI query against a validated interaction database (current query returned no results)
- Given the extensive existing RCT/guideline base, prioritize a rapid evidence-synthesis (rather than new trials) plus local regulatory/safety confirmation as the fastest path to decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

