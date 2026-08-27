---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
---

# Budesonide
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

Using the provided report template, I'll assemble the Evaluation Report directly from the Evidence Pack (no additional tool calls or skills are needed for this — it's a pure data-to-narrative writing task).

# Budesonide: From Inhaled Corticosteroid Therapy to Asthma (Indication Confirmation)

## One-Sentence Summary

Budesonide is a locally-acting synthetic glucocorticoid already marketed in Malaysia as an inhaled/oral corticosteroid. The TxGNN model's top-ranked association points to **Asthma**, but the evidence and rationale supplied indicate this is Budesonide's **already-approved core indication** rather than a genuinely novel repurposing candidate, supported by roughly **50 clinical trials** and **20 publications** in the underlying dataset (top 10 of each shown below). This candidate is best read as a **confirmatory validation signal** — the report also flags where the model's other four ranked associations (IBD, allergic asthma, intrinsic asthma, Crohn's disease) fall on the novelty spectrum.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from the current NPRA license data (all 5 sampled license records have blank `approved_indication_text`). Budesonide is a well-characterized glucocorticoid marketed for respiratory (asthma) and gastrointestinal (IBD) indications globally. |
| Predicted New Indication | Asthma |
| TxGNN Prediction Score | 0.00% *(see caveat below — this value appears to be a data placeholder rather than a genuine confidence score, since it is reported as 0.0 despite being ranked #1)* |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 34 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Budesonide is not available in the structured DrugBank feed (Data Gap DG002). Based on known pharmacology, Budesonide is a non-halogenated synthetic glucocorticoid with high topical anti-inflammatory potency and extensive first-pass hepatic metabolism, which gives it a favorable local-to-systemic activity ratio. This property underlies its two major clinical applications: inhaled/nebulized use for airway inflammation (asthma) and pH/time-release oral or rectal formulations for gastrointestinal inflammation (Crohn's disease, ulcerative colitis, microscopic colitis).

For the top-ranked candidate in this evidence pack, the supplied mechanistic rationale explicitly states: *"Budesonide is a potent, locally-acting ICS that suppresses airway eosinophilic infiltration, mucosal edema, and cytokine release via the glucocorticoid receptor — this is the standard anti-inflammatory mechanism for asthma. This is Budesonide's core already-approved indication, not a novel prediction candidate; the mechanistic link is direct and clinically validated."* In other words, this particular TxGNN output is confirming an established use rather than surfacing a new therapeutic hypothesis — the large body of Phase 3 evidence below reflects decades of approved-indication research, not exploratory repurposing data.

For context, the same evidence pack's other ranked associations vary in novelty: inflammatory bowel disease (rank 2) and Crohn's disease (rank 5) are also already-approved uses of Budesonide's ileal-release formulation (Entocort EC); allergic asthma (rank 3) overlaps substantially with the approved asthma indication; only intrinsic (non-allergic) asthma (rank 4) reflects a genuinely under-studied phenotype-specific question, supported mainly by older, small-scale literature (evidence level L3, decision stage "Research Question"). This distinction matters for prioritizing any follow-up work.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | Completed | 1,600 | Symbicort (budesonide/formoterol) SMART regimen vs. conventional best-practice treatment for persistent asthma over 26 weeks |
| [NCT05202262](https://clinicaltrials.gov/study/NCT05202262) | Phase 3 | Completed | 645 | VATHOS: 24-week trial of budesonide/formoterol MDI vs. budesonide MDI and open-label Symbicort Turbuhaler in inadequately controlled asthma |
| [NCT00509028](https://clinicaltrials.gov/study/NCT00509028) | Phase 3 | Completed | 241 | Long-term (48-week) safety/efficacy of budesonide Turbuhaler in Japanese children with bronchial asthma |
| [NCT00646529](https://clinicaltrials.gov/study/NCT00646529) | Phase 3 | Completed | 175 | SAPLING: 6-month safety comparison of Symbicort vs. Pulmicort Turbuhaler in asthmatic children aged 6–11 |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2,091 | 12-month multinational trial comparing Symbicort SMART vs. Symbicort + terbutaline as-needed in patients ≥16 years |
| [NCT04609904](https://clinicaltrials.gov/study/NCT04609904) | Phase 3 | Completed | 2,187 | Efficacy/safety of budesonide/glycopyrronium/formoterol vs. Symbicort in adults/adolescents with severe inadequately-controlled asthma |
| [NCT00646594](https://clinicaltrials.gov/study/NCT00646594) | Phase 3 | Completed | 1,200 | 7-month comparison of Symbicort pMDI (fixed/adjustable) vs. Advair in subjects ≥12 years with asthma |
| [NCT00252824](https://clinicaltrials.gov/study/NCT00252824) | Phase 3 | Completed | 1,000 | 26-week comparison of Symbicort single-inhaler therapy vs. conventional stepwise treatment in adolescents/adults with persistent asthma |
| [NCT01803555](https://clinicaltrials.gov/study/NCT01803555) | Phase 3 | Completed | 605 | 12-week efficacy/safety of budesonide/formoterol Spiromax vs. Symbicort Turbohaler in persistent asthma |
| [NCT01360021](https://clinicaltrials.gov/study/NCT01360021) | Phase 3 | Completed | 214 | 12-week comparison of Symbicort breath-actuated MDI vs. pressurized MDI formulations in adult/adolescent asthmatics |

*Note: the underlying dataset contains ~50 asthma-related trials in total; the 10 above were prioritized for graded relevance ("A"), completed Phase 3 status, and enrollment size.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | As-needed inhaled budesonide-formoterol as an alternative to conventional maintenance strategies in mild asthma |
| [37003355](https://pubmed.ncbi.nlm.nih.gov/37003355/) | 2023 | RCT | Chest | DENALI trial: albuterol-budesonide pMDI in mild-to-moderate asthma, confirming each component's contribution to efficacy |
| [11687183](https://pubmed.ncbi.nlm.nih.gov/11687183/) | 2001 | Cochrane Review/Meta-analysis | Cochrane Database Syst Rev | Systematic review of inhaled budesonide for chronic asthma in children and adults |
| [32237004](https://pubmed.ncbi.nlm.nih.gov/32237004/) | 2020 | Review | Respirology | Synthesis of asthma-control data from budesonide/formoterol maintenance-and-reliever trials |
| [38527278](https://pubmed.ncbi.nlm.nih.gov/38527278/) | 2024 | Expert Consensus/Review | J Asthma | Thailand expert consensus on nebulized budesonide use for asthma and COPD, stable and exacerbation stages |
| [16162021](https://pubmed.ncbi.nlm.nih.gov/16162021/) | 2005 | Review | Drugs | Review of budesonide inhalation suspension for asthma treatment in infants and children |
| [38889078](https://pubmed.ncbi.nlm.nih.gov/38889078/) | 2024 | Meta-analysis | J Asthma | Meta-analysis of aerosolized budesonide inhalation effects on respiratory symptoms and inflammatory markers in asthma |
| [27381656](https://pubmed.ncbi.nlm.nih.gov/27381656/) | 2016 | Mechanistic Review | Pulm Pharmacol Ther | Molecular and cellular mechanisms underlying budesonide's therapeutic effects in asthma |
| [17983258](https://pubmed.ncbi.nlm.nih.gov/17983258/) | 2007 | Review | Drugs | Review of budesonide/formoterol as combined maintenance-and-reliever inhalation therapy in asthma |
| [19032229](https://pubmed.ncbi.nlm.nih.gov/19032229/) | 2008 | Review | Allergy | Review of budesonide/formoterol maintenance-and-reliever therapy in moderate-to-severe asthma per GINA guidelines |

*Note: the underlying dataset contains 20 asthma-related publications in total; the 10 above were prioritized as RCTs and meta-analyses first, then reviews by recency and relevance.*

## Malaysia Market Information

NPRA records confirm Budesonide is **marketed in Malaysia with 34 total licenses**, but the license-level fields returned in the current query (license number, product name, dosage form, manufacturer, approved indication text) are all blank for the 5 sampled records. No usable authorization table can be presented from this dataset at this time. A re-query of the NPRA product registry (or direct lookup on the NPRA QUEST database) is needed to populate authorization numbers, product/brand names, dosage forms, and label indication text before this section can be completed.

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were queried but returned no usable results — DDI query status: not found, 0 interactions on file. This is flagged as a Blocking data gap (DG001) for full safety assessment; see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical trial and literature base for Budesonide in asthma is extensive and mature (evidence level L1, multiple completed Phase 3 RCTs), but this reflects confirmation of an already-approved indication rather than a novel repurposing opportunity — the supplied mechanistic rationale itself states this is not a new prediction candidate. The "guardrail" designation is therefore driven less by efficacy uncertainty and more by two Blocking/High-severity data gaps that prevent a complete safety and regulatory sign-off: missing NPRA label warnings/contraindications (DG001, Blocking) and missing structured mechanism-of-action data (DG002, High).

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, precautions, contraindications) — required before Stage 1 safety screening can be completed (Blocking)
- Structured mechanism-of-action data via DrugBank API query (High priority)
- Complete NPRA license-level detail (authorization numbers, product names, dosage forms, approved indication text) for the 34 registered products — current extract returned blank fields
- Clarification of the TxGNN score field, which reads 0.00% despite being the #1-ranked candidate — likely a pipeline/export artifact rather than a true confidence value
- If further repurposing research is desired, prioritize the intrinsic (non-allergic) asthma phenotype (rank 4, evidence level L3, "Research Question" stage) as the more genuinely exploratory candidate in this set, rather than the already-approved asthma/IBD/Crohn's disease associations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

