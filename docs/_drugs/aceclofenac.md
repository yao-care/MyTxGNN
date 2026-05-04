---
layout: default
title: Aceclofenac
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# Aceclofenac: From Inflammatory Pain to Osteoarthritis

## One-Sentence Summary

Aceclofenac is an oral NSAID (phenylacetic acid derivative) used for the symptomatic treatment of inflammatory pain and rheumatic conditions including joint disease, low back pain, and periarthritis.
The TxGNN model predicts it may be effective for **Osteoarthritis**, with **5 clinical trials** and **20 publications** currently supporting this direction—including a 2017 meta-analysis of randomised controlled trials directly confirming its efficacy in knee OA.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current NPRA registration data (globally used for inflammatory pain and rheumatic conditions) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank records in this Evidence Pack. Based on extensively published pharmacological literature, Aceclofenac is a phenylacetic acid derivative that inhibits both COX-1 and COX-2 enzymes, thereby suppressing prostaglandin E2 (PGE2) synthesis and reducing the expression of pro-inflammatory mediators—including IL-1β, TNF-α, and matrix metalloproteinases (MMPs)—within synovial tissue and cartilage. These are the core inflammatory pathways driving joint pain and structural deterioration in osteoarthritis.

What distinguishes Aceclofenac from other NSAIDs in the context of osteoarthritis is evidence of additional chondroprotective activity. Research published in the *British Journal of Pharmacology* (PMID: 11090115) demonstrated that Aceclofenac—unlike diclofenac—promotes proteoglycan and hyaluronan synthesis in osteoarthritic human cartilage, suggesting a disease-modifying potential beyond symptom relief. A major metabolite, 4'-hydroxy aceclofenac, also suppresses production of pro-collagenase (MMP-1) and pro-stromelysin (MMP-3) in rheumatoid synovial cells (PMID: 10807502), reinforcing its role in slowing joint matrix degradation.

Osteoarthritis is characterised by progressive cartilage degradation, chronic synovial inflammation, and persistent joint pain—all pathways directly addressed by Aceclofenac's pharmacological profile. The TxGNN model's high prediction score (99.92%) is consistent with substantial global clinical evidence: Aceclofenac is already approved for osteoarthritis in multiple countries including India, South Korea, Spain, and several EU member states. This prediction therefore reflects a strong translational opportunity to formally evaluate or confirm the OA indication within Malaysia's regulatory framework.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02682524](https://clinicaltrials.gov/study/NCT02682524) | Phase 4 | Completed | 191 | Multicenter, randomized, double-blinded Phase IV RCT directly comparing Aceclofenac with pelubiprofen CR in knee OA patients; evaluates both efficacy and safety over 4 weeks—highest-relevance trial for this prediction |
| [NCT00647517](https://clinicaltrials.gov/study/NCT00647517) | Phase 4 | Completed | 60 | Taiwan-based Phase 4 trial assessing add-on Tramadol to COX-2 NSAID (including Aceclofenac) in OA and inflammatory arthritis; directly involves Aceclofenac as the NSAID backbone |
| [NCT00635349](https://clinicaltrials.gov/study/NCT00635349) | Phase 4 | Completed | 143 | Multicenter RCT comparing tramadol/acetaminophen maintenance versus NSAID maintenance in knee OA after initial combination therapy; supports NSAID class—including Aceclofenac—as an effective OA maintenance strategy |
| [NCT03911570](https://clinicaltrials.gov/study/NCT03911570) | N/A | Completed | 108 | Retrospective 6-month comparative study evaluating crystalline glucosamine sulfate added to conventional OA therapy in patients with concomitant knee and primary hand OA; provides relevant OA treatment context |
| [NCT04170218](https://clinicaltrials.gov/study/NCT04170218) | N/A | Unknown | 405 | Multicentric French observational study assessing quality-of-care indicators for knee/hip OA in elderly patients; describes the real-world OA management landscape and unmet care needs |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28293447](https://pubmed.ncbi.nlm.nih.gov/28293447/) | 2017 | Meta-Analysis of RCTs | European Journal of Rheumatology | Meta-analysis of RCTs confirming Aceclofenac's efficacy for pain relief, functional improvement, and safety in OA versus comparator NSAIDs and analgesics; highest-level evidence in this dataset |
| [24639945](https://pubmed.ncbi.nlm.nih.gov/24639945/) | 2014 | RCT | Knee Surgery & Related Research | 4-week multicenter RCT of Aceclofenac controlled-release in chronic knee OA; demonstrates significant analgesic efficacy and an acceptable safety profile |
| [21277837](https://pubmed.ncbi.nlm.nih.gov/21277837/) | 2011 | RCT | The Journal of Pain | 6-week double-blind multicentric RCT (n=285) comparing Aceclofenac-CR once daily vs conventional Aceclofenac twice daily in knee OA; both formulations effective for pain intensity and functional outcomes |
| [32991606](https://pubmed.ncbi.nlm.nih.gov/32991606/) | 2020 | RCT | PLoS ONE | Phase IV non-inferiority RCT comparing pelubiprofen CR vs Aceclofenac 200 mg/day in symptomatic knee OA over 4 weeks; confirms Aceclofenac as the active comparator standard in the field |
| [16709320](https://pubmed.ncbi.nlm.nih.gov/16709320/) | 2006 | RCT | Current Medical Research and Opinion | Double-blind Indian RCT comparing Aceclofenac vs Diclofenac in OA; Aceclofenac demonstrates equivalent efficacy with superior GI tolerability—relevant for Asian patient populations |
| [20387351](https://pubmed.ncbi.nlm.nih.gov/20387351/) | 2009 | RCT/Comparative | JNMA | Head-to-head RCT comparing Aceclofenac vs Nabumetone in OA; evaluates comparative efficacy and GI tolerability |
| [8608684](https://pubmed.ncbi.nlm.nih.gov/8608684/) | 1995 | RCT | Clinical Rheumatology | Large multicentre 12-week double-blind RCT (n=397) comparing Aceclofenac 100 mg BD vs Diclofenac 50 mg TID in knee OA; equivalent clinical efficacy demonstrated at end point |
| [34876850](https://pubmed.ncbi.nlm.nih.gov/34876850/) | 2021 | Narrative Review | Journal of Pain Research | Comprehensive review of Aceclofenac's analgesic and anti-inflammatory properties in musculoskeletal disorders; summarises OA, RA, and ankylosing spondylitis evidence across global populations |
| [11511027](https://pubmed.ncbi.nlm.nih.gov/11511027/) | 2001 | Review | Drugs | Comprehensive reappraisal of Aceclofenac use in pain and rheumatic disease; OA efficacy confirmed as comparable to diclofenac, piroxicam, and naproxen in multiple double-blind trials |
| [11523298](https://pubmed.ncbi.nlm.nih.gov/11523298/) | 2001 | Review | Revue Medicale de Liege | Critical review of Aceclofenac's role in chronic OA; highlights effects on inflammatory mediators, PGE2 inhibition, and cartilage remodelling beyond classical NSAID action |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Not available) | (Not available) | (Not available) | (Not available) |

> **Note:** One Aceclofenac product is confirmed as marketed in Malaysia (NPRA query returned 1 result). However, the product name, dosage form, manufacturer, and approved indication text were not available in the current data extract. Full product details should be retrieved directly from the [NPRA official registry](https://www.npra.gov.my/) or by downloading the product package insert PDF.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important data gap:** Package insert warnings and contraindications for the Malaysian-registered Aceclofenac product were not retrievable in this Evidence Pack. Retrieval from the NPRA official website is required before clinical deployment to identify local-specific safety requirements, particularly regarding GI, cardiovascular, and renal risk categories per NPRA labelling standards.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aceclofenac in osteoarthritis is supported by multiple completed Phase 4 RCTs and a meta-analysis of randomised controlled trials meeting Level 1 (L1) evidence standards. Its established approval for OA across multiple international jurisdictions substantially de-risks this repurposing pathway in Malaysia, and the TxGNN model's high prediction score (99.92%) is fully consistent with the mechanistic and clinical evidence base.

**To proceed, the following is needed:**
- Retrieve full NPRA registration record (product name, dosage form, currently approved indication text) to determine whether an OA indication extension is required or already covered under the existing Malaysia licence
- Obtain mechanism of action data from DrugBank API (DrugBank ID currently unresolved) to complete the mechanistic rationale for any regulatory submission
- Download and review the Malaysian product package insert from the NPRA official website to identify local warnings, contraindications, and drug interactions (currently a blocking data gap)
- Evaluate GI and cardiovascular risk profile specifically for the Malaysian patient population, particularly elderly patients and those with common Southeast Asian comorbidities (hypertension, diabetes, chronic kidney disease)
- Design a post-marketing surveillance plan for long-term safety monitoring should OA be formally listed as an approved indication in Malaysia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

