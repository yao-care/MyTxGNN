---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 519
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

> Omalizumab (Xolair) is a recombinant humanized anti-IgE monoclonal antibody originally established for moderate-to-severe allergic asthma. The TxGNN model's top-ranked prediction points to **Bronchitis**, but the evidence pack's own analysis flags this as a likely disease-ontology mismatch — the linked trials and literature are almost entirely about asthma, not bronchitis itself. Only **2 clinical trials** and **8 publications** are currently associated with this specific candidate, and none directly demonstrate efficacy in bronchitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic Asthma (Omalizumab's established indication; detailed Malaysia NPRA label text is not available in this data pack) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this pack. Based on known information, Omalizumab is a humanized anti-IgE monoclonal antibody that binds free serum IgE, blocking its interaction with the high-affinity FcεRI receptor on mast cells and basophils, thereby reducing the downstream allergic inflammatory cascade. This mechanism is well established in allergic (IgE-mediated) asthma.

For the specific candidate here — **bronchitis** — the evidence pack itself flags a significant caveat: the mechanistic link is characterized as weak and likely reflects **disease-ontology mislabeling** rather than a genuine repurposing signal. The associated trials and literature predominantly involve asthma patients (including eosinophilic bronchitis as a comorbid feature of asthma, or chronic bronchitis discussed only in the context of asthma-COPD overlap), rather than bronchitis as a standalone target. Only one literature entry (a case report on plastic bronchitis after bronchial thermoplasty) addresses bronchitis directly, and it is not a treatment-efficacy study. Given this, any anti-inflammatory rationale for bronchitis is indirect, inferred from symptom overlap between asthma and chronic bronchitis rather than a distinct pharmacological target.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of QGE031 (ligelizumab, an anti-IgE antibody) as add-on therapy in Chronic Spontaneous Urticaria; not bronchitis-specific, actually targets a different allergic population (relevance graded C) |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Investigated whether adding omalizumab allows prednisone dose reduction in patients with asthma **and** eosinophilic bronchitis; very small sample (n=11), asthma is the primary condition (relevance graded C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Not classified | Expert Opinion on Pharmacotherapy | Discusses smoking-induced airway diseases (chronic bronchitis, emphysema, ACO) as comorbidities in asthma; drug treatment for these overlap patients remains uncertain |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui (Japanese J. Anesthesiology) | Preoperative management review covering bronchial asthma/chronic bronchitis; mentions omalizumab as an option for severe allergic asthma, not bronchitis specifically |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Single case of plastic bronchitis occurring after bronchial thermoplasty — not an omalizumab efficacy study |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Not classified | Postepy Dermatologii i Alergologii | Omalizumab in older patients with severe allergic asthma-COPD overlap |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Not classified | Clinical Reviews in Allergy & Immunology | Review of omalizumab's approval and post-approval experience in moderate-to-severe persistent asthma |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Not classified | Current Medical Research and Opinion | Pooled safety analysis of omalizumab in children with allergic (IgE-mediated) asthma |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Not classified | Revue des Maladies Respiratoires | French expert review on adult asthma exacerbations; general asthma management, not bronchitis-specific |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Not classified | Allergologia et Immunopathologia | General review of monoclonal antibody use in pediatrics, including allergic disease |

## Malaysia Market Information

Detailed authorization records (license numbers, product names, dosage forms, approved indication text) are not available in this data pack. Only the following is confirmed: Omalizumab is marketed in Malaysia (✓ Marketed) with **7 total registrations**.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis candidate carries only L4 evidence (mechanism/preclinical-level, no dedicated confirmatory trials), and the evidence pack's own analysis identifies this as a likely disease-ontology mislabeling — the underlying trials and literature are predominantly asthma studies, not bronchitis-specific. There is no direct clinical evidence supporting efficacy in bronchitis itself.

**To proceed, the following is needed:**
- TFDA/NPRA label warnings and contraindications (currently a Blocking data gap preventing S1 safety screening)
- Confirmed mechanism of action documentation (DrugBank query)
- A bronchitis-specific (not asthma-comorbid) clinical trial or mechanistic study before this candidate can advance past S0

*Note: This same evidence pack contains other candidates for omalizumab with stronger support — notably atopic eczema (L3, S2, Research Question) and obstructive lung disease/COPD (L3, S1) — which may warrant separate evaluation if a broader repurposing review is desired.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

