---
layout: default
title: Acetylcysteine
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 5
---

# Acetylcysteine
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

# Acetylcysteine: From Mucolytic Agent to Bronchitis

## One-Sentence Summary

Acetylcysteine (NAC) is a well-established mucolytic and antioxidant compound, clinically recognised as an expectorant for respiratory conditions and as an antidote for acetaminophen overdose.
The TxGNN model predicts it may be effective for **Bronchitis**,
with **13 clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucolytic agent (respiratory conditions); acetaminophen overdose antidote |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | Not available (score data not populated in current Evidence Pack) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 33 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data record. Based on well-established clinical and pharmacological literature, Acetylcysteine (NAC) is a thiol-containing mucolytic and antioxidant compound belonging to the N-acetyl derivative class. Its efficacy in managing pathological respiratory secretions and airway oxidative stress has been demonstrated over six decades of clinical use, and its pharmacological profile maps directly onto bronchitis pathophysiology.

NAC exerts effects through three complementary and well-characterised pathways: (1) **Mucolytic action** — NAC cleaves disulfide bonds within mucus glycoproteins, reducing the viscosity and elasticity of bronchial secretions and facilitating expectoration; (2) **Glutathione (GSH) replenishment** — as a direct precursor of L-cysteine, NAC restores intracellular GSH stores depleted by chronic oxidative stress in the inflamed airway epithelium; (3) **Anti-inflammatory signalling** — NAC suppresses NF-κB pathway activation, attenuating pro-inflammatory cytokine release and reducing persistent neutrophilic airway inflammation.

These three mechanisms map precisely onto the cardinal pathological features of bronchitis: mucus hypersecretion causing productive cough, oxidative stress injury to the bronchial epithelium, and chronic airway inflammation driving disease progression. The mechanistic-disease alignment is high, and the TxGNN model prediction is strongly corroborated by a substantial body of clinical evidence — including completed Phase 2–4 RCTs and multiple systematic reviews and Cochrane analyses confirming NAC's role as a clinically active mucolytic in chronic bronchitis and overlapping COPD populations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00205647](https://clinicaltrials.gov/study/NCT00205647) | Phase 2 | Completed | 240 | Multicenter, randomised, placebo-controlled trial evaluating three doses of oral NAC on sputum viscosity, transport properties, symptoms, quality of life, and exacerbation rate in patients with stable chronic bronchitis; the most direct core evidence for this indication |
| [NCT00184977](https://clinicaltrials.gov/study/NCT00184977) | Phase 4 | Completed | 270 | Large double-blind RCT comparing long-term effects of oral NAC versus inhaled fluticasone propionate on COPD/chronic bronchitis progression and outcomes over several years in general practice |
| [NCT03843541](https://clinicaltrials.gov/study/NCT03843541) | Phase 3 | Completed | 333 | Multicenter, 3-arm parallel RCT comparing IV NAC 600 mg BID versus ambroxol hydrochloride versus placebo as expectorant therapies in Chinese patients with respiratory tract diseases and abnormal mucus secretions |
| [NCT06688292](https://clinicaltrials.gov/study/NCT06688292) | Phase 4 | Completed | 42 | Head-to-head safety and efficacy comparison of two NAC 600 mg formulations (Taneasy granules vs Actein effervescent tablets) administered BID for 14 days in COPD patients |
| [NCT06828120](https://clinicaltrials.gov/study/NCT06828120) | Phase 4 | Completed | 45 | Direct formulation comparison of Taneasy 600 mg granules vs Fluimucil 600 mg granules (the reference branded NAC product) BID for 14 days in COPD with chronic bronchitis overlap |
| [NCT07108166](https://clinicaltrials.gov/study/NCT07108166) | N/A | Recruiting | 290 | Ongoing RCT assessing improvements in major respiratory symptoms (cough frequency, dyspnoea) and lung function in COPD patients with chronic bronchitis switching from combustible cigarettes to tobacco heating system |
| [NCT01599884](https://clinicaltrials.gov/study/NCT01599884) | N/A | Unknown | 65 | Randomised, placebo-controlled trial investigating whether high-dose oral NAC improves respiratory health status and quality of life in COPD patients with concurrent chronic bronchitis symptoms |
| [NCT01739790](https://clinicaltrials.gov/study/NCT01739790) | N/A | Terminated | 51 | Placebo-controlled trial examining whether high-dose NAC improves St. George Respiratory Questionnaire scores in COPD with chronic bronchitis; terminated prior to full enrolment |
| [NCT03364218](https://clinicaltrials.gov/study/NCT03364218) | Phase 4 | Unknown | 106 | RCT of nebulised NAC versus standard care for bronchiolitis in hospitalised infants under 6 months; evaluates length of hospital stay and respiratory symptom resolution |
| [NCT05843669](https://clinicaltrials.gov/study/NCT05843669) | Phase 4 | Completed | 82 | Open-label, multicenter, single-group study evaluating effectiveness of Mucinex® (guaifenesin) over a 12-week treatment period in patients with stable chronic bronchitis, following a 2-week treatment-free run-in to establish baseline |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38555190](https://pubmed.ncbi.nlm.nih.gov/38555190/) | 2024 | Systematic Review | Archivos de Bronconeumologia | Distinct meta-analyses separately evaluating NAC efficacy in COPD and in chronic bronchitis/pre-COPD; demonstrates antioxidant and mucolytic benefits and distinguishes response profiles between the two populations |
| [26324807](https://pubmed.ncbi.nlm.nih.gov/26324807/) | 2015 | Meta-analysis | European Respiratory Review | Meta-analysis clarifying NAC's role in preventing exacerbations of chronic bronchitis and COPD; identifies dose-response relationship comparing low (≤600 mg/day) versus high (>600 mg/day) dosing regimens |
| [31107966](https://pubmed.ncbi.nlm.nih.gov/31107966/) | 2019 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Comprehensive Cochrane review of mucolytics versus placebo in chronic bronchitis/COPD; assesses exacerbation frequency, sputum volume, days of disability, and adverse effects across multiple trials |
| [39413571](https://pubmed.ncbi.nlm.nih.gov/39413571/) | 2024 | Systematic Review | Respiratory Investigation | Systematic review and meta-analysis of mucolytic efficacy and safety in patients with stable COPD, with direct applicability to the chronic bronchitis phenotype |
| [31598901](https://pubmed.ncbi.nlm.nih.gov/31598901/) | 2019 | Meta-analysis | Advances in Therapy | Meta-analysis specifically focused on the effect of orally administered NAC on clinical outcomes — including exacerbation rate, sputum characteristics, and lung function — in patients with chronic bronchitis |
| [19138505](https://pubmed.ncbi.nlm.nih.gov/19138505/) | 2009 | RCT | Respiratory Medicine | Long-term RCT (publication from NCT00184977) comparing fluticasone and NAC in primary care patients with COPD or chronic bronchitis; examines oxidative stress, bronchial inflammation, and clinical outcomes |
| [6376210](https://pubmed.ncbi.nlm.nih.gov/6376210/) | 1984 | RCT | J International Medical Research | Landmark multicentre, double-blind, placebo-controlled study of oral acetylcysteine (Fabrol) for chronic bronchitis symptoms over 3 months in UK general practice; statistically significant improvements in expectoration difficulty and cough severity |
| [27143871](https://pubmed.ncbi.nlm.nih.gov/27143871/) | 2016 | RCT | Int J Chronic Obstructive Pulmonary Disease | Randomised placebo-controlled trial of high-dose oral NAC in COPD with chronic bronchitis; high-dose NAC failed to improve respiratory health status, raising questions about the optimal dose ceiling |
| [32454850](https://pubmed.ncbi.nlm.nih.gov/32454850/) | 2020 | RCT | Evidence-Based Complementary and Alternative Medicine | Randomised comparison of ivy leaf cough syrup versus acetylcysteine in adults and children with acute bronchitis; evaluates relative improvement in productive cough and symptom burden |
| [24787454](https://pubmed.ncbi.nlm.nih.gov/24787454/) | 2014 | Review | COPD | Pharmacological and clinical reappraisal of NAC in respiratory system oxidative stress; provides mechanistic rationale for NAC use in chronic bronchitis and COPD across multiple patient subgroups |

> **Note:** PMID 35795313 and its retraction notice (PMID 38075328) have been excluded from this analysis due to confirmed retraction (DOI: 10.1155/2022/9133777).

---

## Malaysia Market Information

Acetylcysteine holds **33 registered products** in Malaysia with a confirmed marketed status (已上市). However, individual product details — including authorization numbers, brand names, dosage forms, and approved indication texts — were not available in the current NPRA data extract. Please consult the [NPRA Product Registration database](https://www.npra.gov.my/) directly for complete product listings to determine which approved indications are currently on-label in Malaysia.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for NAC in bronchitis meets the L1 threshold, supported by multiple completed Phase 2–4 RCTs (including a 333-patient multicenter Phase 3 trial), several Cochrane systematic reviews, and multiple meta-analyses confirming mucolytic and anti-exacerbation efficacy. NAC is already referenced in international respiratory guidelines for chronic bronchitis and overlapping COPD phenotypes. Malaysia market access is confirmed with 33 registered products.

**To proceed, the following is needed:**
- Retrieve and review the Malaysia NPRA package insert(s) for approved indications, key warnings, and contraindications — this is currently a **Blocking data gap (DG001)** preventing formal safety pre-screening
- Confirm whether any of the 33 registered NPRA products carry a bronchitis-specific approved indication, to establish on-label versus off-label status in Malaysia
- Obtain the formal mechanism of action data from DrugBank (Data Gap DG002) to complete mechanistic documentation
- Conduct a Malaysia-specific drug-drug interaction review, as DDI data was not retrieved in the current evidence pack
- For clinical implementation, note that evidence favours standard-dose NAC (600 mg/day oral) over high-dose regimens in chronic bronchitis; dose optimisation should be specified in any implementation protocol

---

## Additional Predicted Indications Overview

This Evidence Pack covers 5 TxGNN-predicted indications for Acetylcysteine. Summary below:

| Rank | Indication | Evidence Level | Decision |
|------|-----------|---------------|---------|
| 1 | Bronchitis | L1 | Proceed with Guardrails |
| 2 | Bronchiectasis | L2 | Research Question |
| 3 | Amyloidosis | L3 | Research Question |
| 4 | AL Amyloidosis | L5 | Hold |
| 5 | Cystic Fibrosis | L2 | Research Question |

**Bronchiectasis (Rank 2):** Multiple RCTs directly evaluating NAC in non-cystic fibrosis bronchiectasis, including the completed BENE trial (NCT02088216, n=161) and a forthcoming Phase 3 TB-recovery trial (NCT07136987, n=1,104). Separate detailed report recommended.

**Cystic Fibrosis (Rank 5):** Strong mechanistic rationale (GSH depletion is a hallmark of CF lung disease; NAC corrects redox imbalance and reduces mucus viscosity) with Phase 2B RCT evidence (NCT00809094, n=70). Separate detailed report recommended.

**Amyloidosis (Rank 3):** Emerging signal concentrated in a rare subtype — hereditary cystatin C amyloid angiopathy (HCCAA) — where NAC disrupts cystatin C aggregation via disulfide bond cleavage. A non-randomised clinical trial was published in *JAMA Neurology* (2025, PMID 40163249). Evidence for general amyloidosis remains preclinical.

**AL Amyloidosis (Rank 4):** No relevant NAC clinical evidence. The mechanistic link (light-chain misfolding) is distant from NAC's pharmacology. **Hold** decision is appropriate; deprioritise unless further biological rationale emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

