---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 504
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran antibacterial internationally labeled for uncomplicated urinary tract infections (UTI); the specific approved-indication text in this market's regulatory record was not captured in this evidence pack. The TxGNN model ranks **Rheumatoid Arthritis** as its top predicted new indication (score 99.89%), but the supporting literature (12 PubMed records) consists almost entirely of case reports and reviews describing nitrofurantoin-*induced* adverse reactions (pulmonary fibrosis, hepatitis) in RA patients — not evidence of therapeutic benefit. No clinical trials exist for this pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (license text empty; TFDA label data flagged as a Blocking data gap — DG001). Internationally, Nitrofurantoin's established label indication is uncomplicated urinary tract infection (UTI). |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug (data gap). Nitrofurantoin's known pharmacology is that of a nitrofuran antibacterial: after bacterial nitroreductase activation it generates reactive intermediates that damage bacterial DNA and ribosomal proteins. There is no established immunomodulatory or anti-inflammatory mechanism that would explain an effect on rheumatoid synovitis or autoimmune disease activity.

Reviewing the 12 supporting publications shows the prediction is not mechanistically grounded: the majority describe nitrofurantoin (or other drugs) *causing* interstitial lung disease/pulmonary fibrosis, hepatotoxicity, or sialadenitis in patients who happen to have RA as a comorbidity or differential-diagnosis consideration — not nitrofurantoin treating RA. One record (PMID 31222078) specifically studies antibiotic exposure as a trigger for RA *flares* (a risk signal, not a benefit signal). This pattern is consistent with a co-occurrence artifact: nitrofurantoin and "rheumatoid arthritis" appear together in the literature mainly because clinicians differentiate drug-induced lung/liver injury from RA-associated disease in the same patients, not because of a treatment relationship.

Given this, the high TxGNN score most likely reflects textual/graph co-occurrence rather than a plausible repurposing hypothesis, and the evidence direction is arguably opposite to what a "new indication" would require.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Lists nitrofurantoin among drugs causing pulmonary fibrosis; notes RA itself is also a predisposing disease for lung fibrosis — an adverse-effect/comorbidity overlap, not a treatment link |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | General review of drug-induced interstitial lung disease listing nitrofurantoin (and minocycline) as causative antibiotics |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Studied whether antibiotic use *triggers* RA flares (n=31,992, CPRD GOLD) — a risk association, not evidence of therapeutic effect |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Describes poor prognosis of RA patients hospitalized for interstitial lung fibrosis; does not evaluate nitrofurantoin as therapy |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | Case of irreversible pulmonary fibrosis from methotrexate + nitrofurantoin interaction in an RA patient — an adverse drug interaction, not a benefit |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Autoimmune hepatitis differential diagnosis case; nitrofurantoin and RA both mentioned only as differential considerations for drug-induced liver injury |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Annales de dermatologie et de vénéréologie | Case of phenylbutazone-induced sialadenitis; nitrofurantoin mentioned only as another drug reported to cause sialadenitis |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Revue de pneumologie clinique | Gold-salt-induced pneumonitis case; compares BAL findings to those reported with methotrexate — nitrofurantoin not a treatment focus |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Unclassified | Acta Medica Scandinavica | No abstract available; title concerns nitrofurantoin therapy for bacteriuria (UTI), unrelated to RA |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Unclassified | Der Internist | No abstract available; title is a general synopsis on alveolitis/pulmonary fibrosis |

## Malaysia Market Information

This evidence pack records **1 registered license** with market status "已上市" (Marketed), but the license number, product name, dosage form, and approved-indication text fields were all empty in the source data — full registration details are not available and should be pulled directly from the NPRA product registry before use in any regulatory submission.

## Safety Considerations

Official safety fields (key warnings, contraindications, drug interactions) were not populated in this evidence pack (DG001, Blocking — TFDA/NPRA label PDF not yet parsed). Please refer to the package insert for safety information.

**Additional literature-derived signals worth flagging** (not from official label data, but surfaced by this evaluation's broader literature search across other predicted indications):
- Nitrofurantoin has documented case reports of *inducing* methemoglobinemia, particularly via photoactivation or in neonates ([PMID 3176031](https://pubmed.ncbi.nlm.nih.gov/3176031/), [930081](https://pubmed.ncbi.nlm.nih.gov/930081/), [5359411](https://pubmed.ncbi.nlm.nih.gov/5359411/)).
- Case-level evidence of nitrofurantoin-associated pulmonary fibrosis, especially in combination with methotrexate ([PMID 35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/)).
- Nitrofurantoin is conventionally contraindicated/used with caution in significant renal impairment (CrCl < 60 mL/min), relevant given one lower-ranked prediction (diabetic nephropathy) directly implicates renal function.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting literature for Rheumatoid Arthritis describes nitrofurantoin-induced adverse events (pulmonary fibrosis, hepatotoxicity) or RA-flare risk, not therapeutic benefit, and there is no plausible mechanistic link between nitrofurantoin's antibacterial mode of action and RA disease modification. No clinical trials exist. The evidence pack's own scoring (L5, S0) and recommendation already align with Hold.

**To proceed, the following is needed:**
- TFDA/NPRA label PDF parsing to close the Blocking safety data gap (DG001) before any S1 safety review
- DrugBank MOA data (DG002) to properly assess mechanistic plausibility
- A genuine RA-specific preclinical or translational rationale, since current literature evidence points in the opposite (harm) direction
- Confirmation this candidate should likely be deprioritized in favor of re-screening lower-noise predictions from this drug's candidate list, several of which (e.g., methemoglobinemia) are themselves inverse safety signals rather than repurposing opportunities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

