---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Musculoskeletal Inflammation to Osteoarthritis Susceptibility

## One-Sentence Summary

Piroxicam is an oxicam-class NSAID with an extended half-life enabling once-daily dosing, well established for managing pain and inflammation in rheumatic and musculoskeletal conditions.
The TxGNN model predicts it may have utility in **Osteoarthritis Susceptibility** — specifically as a potential early or preventive intervention in genetically predisposed individuals — with **no registered clinical trials** and **2 publications** currently supporting this specific direction.
Closely related predictions for **Rheumatoid Arthritis** (Rank 2) and **Osteoarthritis** (Rank 3) carry substantially stronger Level 1 evidence, providing important contextual support for the biological plausibility of the overall prediction cluster.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Approved indication text not available from current regulatory dataset (Piroxicam is an NSAID indicated for musculoskeletal pain and inflammation) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.9994% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on established pharmacology, Piroxicam inhibits cyclooxygenase (COX) enzymes — both COX-1 and COX-2 — thereby reducing the biosynthesis of prostaglandins, particularly prostaglandin E₂ (PGE₂). This mechanism accounts for its well-documented analgesic, anti-inflammatory, and antipyretic effects across a range of rheumatic conditions.

The prediction linking Piroxicam to **osteoarthritis susceptibility** is mechanistically plausible in principle: PGE₂ is a key mediator of articular cartilage degradation and synovial inflammation in OA pathogenesis. In theory, sustained COX inhibition could attenuate cartilage-destructive inflammatory signalling in individuals genetically predisposed to OA — such as those carrying GDF5 polymorphisms, which are associated with reduced cartilage formation capacity. However, this represents a qualitatively different clinical application from symptomatic OA treatment: it implies a preventive or disease-modifying role in pre-symptomatic individuals, for which no dedicated clinical trial evidence currently exists.

It is important to contextualise this prediction within the broader TxGNN output. Piroxicam's established efficacy in **symptomatic osteoarthritis** (Rank 3, L1 evidence, multiple RCTs) and **rheumatoid arthritis** (Rank 2, L1 evidence, multiple RCTs) strongly validates the COX-PGE₂ mechanistic link to inflammatory joint disease. The TxGNN model appears to extend this association to the upstream susceptibility phenotype, but the leap from symptom management to genetic predisposition prevention remains speculative and requires dedicated prospective study designs that have not yet been conducted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for osteoarthritis susceptibility with Piroxicam.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28497473](https://pubmed.ncbi.nlm.nih.gov/28497473/) | 2017 | Cochrane Overview | The Cochrane Database of Systematic Reviews | Systematic overview of topical analgesics (including Piroxicam formulations) for acute and chronic pain conditions including osteoarthritis of the hand and knee; supports the broader evidence base for Piroxicam in OA-spectrum disease |
| [3142593](https://pubmed.ncbi.nlm.nih.gov/3142593/) | 1988 | RCT (GI Protection) | BMJ (Clinical Research Ed.) | Controlled trial evaluating ranitidine prophylaxis against gastroduodenal damage in patients receiving NSAIDs including Piroxicam; provides safety context relevant to any consideration of long-term preventive NSAID use in susceptible populations |

---

## Malaysia Market Information

Eight Piroxicam product registrations are confirmed active on the Malaysian NPRA register. Detailed product-level information — including authorisation numbers, product names, dosage forms, and approved indication text — was not returned in the current dataset and requires direct retrieval from the NPRA official portal.

| Item | Detail |
|------|--------|
| Total Registrations Confirmed | 8 products |
| Market Status | Marketed (已上市) |
| Full Product Details | Retrieve from [NPRA Product Registration Search](https://www.npra.gov.my/index.php/en/product-registration) |

---

## Safety Considerations

Please refer to the package insert for full safety information, as detailed warnings and contraindications were not available in the current evidence pack.

As a non-selective NSAID, Piroxicam carries well-recognised class-related risks that are particularly relevant when evaluating any long-term or preventive use in an OA susceptibility context:

- **Gastrointestinal risk**: The 1988 BMJ RCT included in this evidence pack specifically investigated GI mucosal protection strategies for Piroxicam users, underscoring that upper GI ulceration and bleeding are a primary safety concern, especially in prolonged use.
- **Cardiovascular risk**: NSAIDs, particularly non-selective COX inhibitors, carry dose- and duration-dependent cardiovascular event risk, which is especially significant for any preventive indication targeting asymptomatic individuals.
- **Renal risk**: Impaired renal prostaglandin synthesis may compromise renal haemodynamics, particularly in elderly or hypertensive populations.
- **Drug interactions**: A completed Phase 4 clinical trial (NCT00631514, n=88) in the broader evidence set directly evaluated the interaction between Piroxicam and antihypertensive agents, confirming the potential to blunt blood pressure control — a clinically important consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score of 99.9994%, the evidence supporting Piroxicam specifically for **osteoarthritis susceptibility** — as a preventive or disease-modifying intervention in genetically at-risk individuals — is currently limited to mechanistic hypothesis (L4). No clinical trials have been conducted to address this specific preventive indication, and the long-term safety profile of NSAID prophylaxis in asymptomatic populations has not been characterised.

**To proceed, the following is needed:**
- Prospective studies evaluating COX inhibitors in OA-susceptible populations (e.g., GDF5 polymorphism carriers or individuals with radiological pre-OA signs)
- Long-term safety characterisation of preventive NSAID use in asymptomatic subjects, particularly regarding GI, cardiovascular, and renal endpoints
- Detailed MOA data from DrugBank to formally characterise Piroxicam's COX-1/COX-2 selectivity profile and off-target pharmacology
- Full NPRA package insert to confirm Malaysian-approved indications, warnings, and contraindications
- Pharmacoeconomic assessment comparing preventive NSAID therapy against current OA risk stratification and management guidelines in Malaysia

---

**Adjacent high-priority predictions with immediately actionable evidence:**

| Indication | TxGNN Rank | Evidence Level | Recommendation |
|------------|-----------|----------------|----------------|
| Rheumatoid Arthritis | #2 | L1 | Proceed with Guardrails |
| Osteoarthritis | #3 | L1 | Proceed with Guardrails |
| Arthropathy | #10 | L2 | Proceed with Guardrails |

These closely related indications share Piroxicam's core COX-inhibition mechanism, are supported by multiple completed RCTs and systematic reviews, and represent more immediately actionable opportunities for label expansion or formal registration in Malaysia. In particular, if Piroxicam's current Malaysian product registrations do not explicitly include OA or RA indications, these represent the highest-priority repurposing targets to pursue.

---

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any clinical application. YMYL content — all findings should be interpreted by qualified healthcare professionals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

