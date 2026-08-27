---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a fibrate-class lipid-regulating agent, clinically established for treating hypertriglyceridemia and mixed dyslipidemia. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this direction is currently supported only by **animal-model and case-report literature (4 publications)**, with no registered clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidemia / hypertriglyceridemia (fibrate class; detailed NPRA-approved indication wording not captured in this evidence pack) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (preclinical / mechanistic studies only) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold (flagged internally as "Research Question" stage — S1) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gemfibrozil is a fibrate-class **PPAR-α agonist**, clinically used to lower triglycerides and raise HDL-C in dyslipidemia. Mechanistically, PPAR-α activation has documented anti-inflammatory and immunomodulatory effects beyond lipid metabolism, which is the pharmacological basis for the TxGNN prediction linking it to rheumatoid arthritis (RA).

The supporting literature is class-level rather than drug-specific in most cases. One study (PMID 30074417) directly tested gemfibrozil combined with a reduced steroid dose in a rat adjuvant-induced arthritis (AIA) model, showing efficacy comparable to full-dose steroid alone. A related study on bezafibrate — a pan-PPAR agonist in the same drug class — showed attenuation of experimental RA via PPAR-γ–dependent modulation of inflammatory pathways (PMID 41207105), lending indirect mechanistic support.

However, no human clinical trials for gemfibrozil in RA have been identified, and the evidence base remains confined to animal models, case reports, and cross-class mechanistic analogy. This keeps the finding at the "research question" stage rather than a clinically actionable repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal model (rat AIA) | Modern Rheumatology | Gemfibrozil + reduced-dose prednisolone gave a similar disease-management outcome as full-dose steroid in a rat adjuvant-induced arthritis model |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical/animal (bezafibrate, class analog) | International Immunopharmacology | Pan-PPAR agonist bezafibrate attenuates experimental RA via PPAR-dependent modulation of inflammatory pathways, emphasizing PPAR-γ activity |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical/mechanistic (EAE model, non-RA) | Journal of Immunology | Myelin basic protein priming reduces Foxp3 expression in T cells via nitric oxide — general Treg/autoimmune mechanism, not RA-specific |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Case report (unrelated finding) | American Journal of Clinical Dermatology | Review of palmar erythema causes; tangential relevance, not a treatment study |

---

## Malaysia Market Information

Gemfibrozil is marketed in Malaysia with 8 active NPRA registrations, but this evidence pack does not include the individual license details (authorization numbers, product names, dosage forms, or approved indication text) — these fields came back blank from the source query and would need to be re-pulled from NPRA.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack (flagged internally as a **Blocking** data gap — DG001), meaning a full safety pre-assessment cannot yet be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (PPAR-α/γ anti-inflammatory activity) is plausible, but current evidence for gemfibrozil in RA is limited to one rat AIA model, cross-class analogy (bezafibrate), and a tangentially related case report — no human trials exist. Combined with a blocking gap in TFDA/NPRA safety labeling data, this candidate is not ready to advance past the research-question stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, blocking)
- DrugBank-confirmed mechanism of action (DG002)
- NPRA license details (authorization numbers, product names, approved indication text) for the 8 Malaysia registrations
- A prospective (at minimum Phase 2) clinical study in RA patients, since existing evidence is entirely preclinical
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

