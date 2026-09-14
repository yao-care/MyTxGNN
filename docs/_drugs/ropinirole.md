---
layout: default
title: Ropinirole
parent: 僅模型預測 (L5)
nav_order: 604
evidence_level: L5
indication_count: 10
---

# Ropinirole
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

# Ropinirole: From Parkinson's Disease to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

Ropinirole is a non-ergoline dopamine D2/D3 receptor agonist globally indicated for Parkinson's disease and restless legs syndrome (RLS). The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, currently supported by **0 clinical trials** and **8 publications**, most of which are case reports and reviews from RLS–ADHD comorbid populations rather than trials targeting ADHD directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease / Restless Legs Syndrome (global indications; Malaysia-specific approved indication text not available in this data pack) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (marked as a Data Gap). Based on established pharmacological knowledge, Ropinirole is a non-ergoline dopamine D2/D3 receptor agonist whose efficacy in Parkinson's disease and restless legs syndrome is well established.

ADHD is mechanistically associated with reduced dopaminergic transmission in prefrontal-striatal circuits, so a D2/D3 agonist is theoretically plausible as a modulator of ADHD symptoms. However, the literature currently supporting this signal comes almost entirely from patients with **comorbid RLS and ADHD** (e.g., a pediatric case where ropinirole improved both restless-legs/periodic-limb-movement symptoms and ADHD symptoms), not from trials designed to treat ADHD's core symptoms directly.

This means the mechanistic rationale is real but indirect — the current evidence base reflects a secondary/comorbidity observation rather than a targeted therapeutic hypothesis, which is why the evidence level remains L4 (preclinical/mechanistic) rather than higher.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | Case Report | Pediatric Neurology | 6-year-old with ADHD + RLS/PLMS showed significant improvement in both ADHD symptoms and sleep disruption after ropinirole treatment |
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Review | Sleep | Reviews the RLS–ADHD association and proposes a shared dopaminergic mechanism supporting common pharmacologic treatment |
| [18052582](https://pubmed.ncbi.nlm.nih.gov/18052582/) | 2007 | Case Report | J Clin Psychiatry | Ropinirole used to treat aripiprazole-induced tardive akathisia (unrelated to ADHD; dopaminergic mechanism relevant) |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General overview of restless legs syndrome epidemiology and diagnostic criteria; no ADHD-specific data |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | Preclinical | J Neuropathol Exp Neurol | A11-lesioned, iron-deprived mouse model of RLS; supports a dopamine–iron pathophysiology link theoretically relevant to RLS/ADHD overlap |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | RCT (Parkinson's disease population) | Clinical Neuropharmacology | 11-week comparison of piribedil vs. pramipexole/ropinirole on vigilance in Parkinson's disease with daytime sleepiness; not ADHD-specific |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Receptor Pharmacology | Pharmacological Research | Studies D4 receptor/α2A-adrenoceptor heteromers implicated in ADHD pathophysiology; does not directly test ropinirole |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | Case Report (Safety) | Cornea | Corneal edema reported in patients exposed to systemic dopaminergic agents; safety signal, not efficacy evidence |

**Note:** None of the identified literature is a clinical trial directly testing ropinirole for ADHD's core symptoms; most evidence derives from RLS–ADHD comorbid case reports and dopaminergic mechanism studies.

---

## Malaysia Market Information

NPRA records confirm **4 active marketed authorizations** for Ropinirole in Malaysia, but this data pull did not return the underlying license number, product name, dosage form, or approved-indication text fields for any of them — these details should be sourced directly from NPRA product registration records before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Package insert warnings/contraindications (DG001) are flagged as a **Blocking** data gap in this evidence pack — this data must be obtained before the drug can enter a formal S1 safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NPRA package-insert safety data required for even a preliminary (S1) safety screen is currently missing (Blocking data gap), and the ADHD signal itself rests only on case reports and mechanistic reviews (L4) from RLS–ADHD comorbid patients — not on any completed clinical trial targeting ADHD. Additionally, 9 of the 10 TxGNN-ranked candidates for this drug (e.g., faciodigitogenital syndrome, X-linked myopia, Charcot-Marie-Tooth disease) show zero supporting evidence and no plausible dopaminergic mechanism, indicating substantial noise in this model run that warrants caution in weighting the ADHD score itself.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) to clear the Blocking data gap
- DrugBank-confirmed mechanism of action (DG002)
- A prospective or retrospective study directly assessing ropinirole in ADHD (not just comorbid RLS populations)
- Safety monitoring plan addressing known dopamine-agonist risks (e.g., impulse-control disorders such as gambling, noted in adjacent literature) if pursued in a psychiatric population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

