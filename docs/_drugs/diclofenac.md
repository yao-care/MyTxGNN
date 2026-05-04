---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From Anti-inflammatory/Analgesic to Osteoarthritis Susceptibility

## One-Sentence Summary

Diclofenac is a widely used non-steroidal anti-inflammatory drug (NSAID), primarily indicated for pain relief and inflammation in rheumatic and musculoskeletal conditions. The TxGNN model predicts it may be effective for **Osteoarthritis Susceptibility**, with **1 clinical trial** and **5 publications** currently supporting this direction. Notably, the closely related indications of "osteoarthritis" (Rank 2) and "arthropathy" (Rank 7) are already approved uses of diclofenac, making the "susceptibility" (preventive) angle the only genuinely novel prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anti-inflammatory, analgesic (rheumatic diseases, musculoskeletal pain, osteoarthritis, rheumatoid arthritis) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 81 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Diclofenac is a phenylacetic acid derivative that inhibits cyclooxygenase (COX-1 and COX-2) enzymes, thereby reducing the synthesis of prostaglandins (particularly PGE2) that mediate inflammation, pain, and fever. It is one of the most widely prescribed NSAIDs globally, with well-established efficacy in osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, and various acute pain conditions. Its mechanism directly targets the inflammatory cascade that drives joint pain and swelling in degenerative and inflammatory arthropathies.

The distinction between the predicted indication — "osteoarthritis susceptibility" — and the already-approved indication of osteoarthritis treatment is critical. "Susceptibility" refers to the pre-disease genetic and biological predisposition to develop osteoarthritis, rather than the symptomatic disease itself. While COX inhibition effectively manages established OA symptoms (pain, swelling, stiffness), there is currently **no evidence** that chronic NSAID use can prevent OA onset in genetically susceptible individuals. In fact, the well-documented cardiovascular, gastrointestinal, and renal risks of long-term NSAID use make diclofenac a poor candidate for preventive use in asymptomatic populations.

The TxGNN model likely generated this prediction due to the strong pharmacological overlap between diclofenac and OA treatment. However, the model may not adequately distinguish between therapeutic and preventive applications. The 8 additional predicted indications (Ranks 3–6, 8–10) are rare genetic skeletal or dermatological disorders (e.g., pseudoachondroplasia, brachyolmia, hypotrichosis) for which COX inhibition has no plausible mechanistic rationale, further suggesting that the model is capturing broad anti-inflammatory associations rather than specific repurposing opportunities.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04402047](https://clinicaltrials.gov/study/NCT04402047) | N/A | Unknown | 108 | Electroacupuncture vs topical diclofenac sodium gel for hand OA; a treatment comparison study rather than a prevention/susceptibility study. Evidence value limited due to unknown status. |

Only 1 clinical trial was identified for the specific "osteoarthritis susceptibility" indication. This trial evaluates diclofenac as a treatment for established hand OA, not as a preventive intervention for susceptible individuals. No trials specifically addressing OA prevention with diclofenac were found.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28497473](https://pubmed.ncbi.nlm.nih.gov/28497473/) | 2017 | Cochrane Overview | Cochrane Database Syst Rev | Overview of topical analgesics for acute and chronic pain including OA; confirms diclofenac efficacy for OA symptom management |
| [38183573](https://pubmed.ncbi.nlm.nih.gov/38183573/) | 2024 | Model-Based Meta-Analysis | Pain Ther | Supports combination of acetaminophen and topical diclofenac in OA pain via complementary mechanisms; focuses on treatment not prevention |
| [30860559](https://pubmed.ncbi.nlm.nih.gov/30860559/) | 2019 | Cohort Study | JAMA | Tramadol vs NSAIDs (including diclofenac) mortality comparison in OA patients; highlights safety concerns of long-term use |
| [14575648](https://pubmed.ncbi.nlm.nih.gov/14575648/) | 2003 | Review (Toxicology) | Toxicol Appl Pharmacol | Diclofenac-induced liver injury as idiosyncratic toxicity paradigm; raises safety concerns for chronic preventive use |
| [3142593](https://pubmed.ncbi.nlm.nih.gov/3142593/) | 1988 | RCT (Safety) | BMJ | Ranitidine prophylaxis for NSAID-induced gastroduodenal damage; underscores GI risk with chronic diclofenac use |

All identified literature addresses diclofenac use in **established** osteoarthritis or its safety profile. No publications specifically investigate the prevention of OA onset in susceptible populations.

## Malaysia Market Information

Diclofenac is marketed in Malaysia with **81 registered products**. Specific registration details (authorization numbers, product names, dosage forms, and approved indications) were not available in the evidence pack. Given the large number of registrations, diclofenac is widely available across multiple dosage forms (oral tablets, topical gels, patches, injections, suppositories) from numerous manufacturers.

## Safety Considerations

Please refer to the package insert for safety information.

As a well-characterized NSAID, diclofenac's safety profile is extensively documented in the literature. Key concerns for any long-term or preventive use would include:

- **Cardiovascular risk**: Increased risk of myocardial infarction and stroke with prolonged use
- **Gastrointestinal toxicity**: Ulceration, bleeding, and perforation risk
- **Hepatotoxicity**: Rare but serious idiosyncratic liver injury (onset typically >1–3 months)
- **Renal impairment**: Risk of nephrotoxicity with chronic use
- **Drug interactions**: Significant interactions with anticoagulants, antihypertensives, lithium, methotrexate, and other NSAIDs

These risks strongly argue against repurposing diclofenac as a preventive agent in asymptomatic populations with OA susceptibility.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of diclofenac for "osteoarthritis susceptibility" conflates treatment efficacy with preventive potential. While diclofenac is a proven first-line therapy for established osteoarthritis (already an approved indication), there is no clinical evidence supporting its use to prevent OA development in genetically susceptible individuals. The well-known cardiovascular, GI, hepatic, and renal risks of chronic NSAID use make this an unfavorable risk–benefit profile for preventive application. The remaining novel predictions (Ranks 3–6, 8–10) are rare genetic disorders with no mechanistic rationale for COX inhibition.

**To proceed, the following is needed:**
- Preclinical evidence demonstrating that COX inhibition can modify OA disease initiation (not just symptom management)
- Epidemiological studies evaluating whether chronic NSAID users have lower OA incidence
- Risk–benefit analysis for long-term diclofenac use in asymptomatic populations
- Identification of biomarkers that could define a target population where preventive benefit outweighs known NSAID risks
- DrugBank ID confirmation and detailed MOA data to close existing data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

