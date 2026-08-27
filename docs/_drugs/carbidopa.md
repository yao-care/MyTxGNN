---
layout: default
title: Carbidopa
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 5
---

# Carbidopa
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

# Carbidopa: From Parkinson's Disease to Parkinsonian Disorder

## One-Sentence Summary

Carbidopa is a peripheral dopa-decarboxylase (DDC) inhibitor used together with levodopa as standard therapy for Parkinson's disease. The TxGNN model's top-ranked prediction is **Parkinsonian Disorder**, supported by **50 clinical trials** and **19 publications** — but this term is essentially an ontology-level synonym of Parkinson's disease itself, meaning the "prediction" largely re-confirms carbidopa's already-established indication rather than surfacing a genuinely new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, used in combination with levodopa (drawn from the evidence pack's mechanistic rationale; the formal NPRA license indication text is not available — see caveat below) |
| Predicted New Indication | Parkinsonian Disorder |
| TxGNN Prediction Score | 0.00% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 12 |
| Recommended Decision | Proceed with Guardrails |

**Important caveat:** The TxGNN score for every predicted indication in this pack (ranks 1–5) is 0.0%, and the evidence pack's own rationale for rank 1 explicitly flags that "Parkinsonian Disorder" and "Parkinson Disease" (rank 4) are the same standard indication under different ontology labels, not independent candidates. This is not a typical repurposing case.

## Why is This Prediction Reasonable?

Carbidopa is a peripheral dopa-decarboxylase (DDC) inhibitor. It does not cross the blood-brain barrier and has no central activity on its own; instead, it blocks the conversion of levodopa to dopamine in peripheral tissues. This reduces peripheral side effects (e.g., nausea, cardiovascular effects) and increases the amount of levodopa reaching the central nervous system, where it is converted to dopamine to relieve parkinsonian motor symptoms.

Because this mechanism is the basis of carbidopa's original, well-established use alongside levodopa for Parkinson's disease, the "prediction" that carbidopa is relevant to Parkinsonian Disorder is mechanistically sound but not novel — it reflects decades of standard clinical practice rather than a new therapeutic hypothesis. The knowledge graph appears to have generated two nearly identical top entries (ranks 1 and 4) for what is clinically the same disease concept.

Formal MOA documentation (`original_moa`) is flagged as a data gap (DG002, High severity) in this evidence pack; the mechanistic description above is derived from the rationale text embedded in the model's own scoring output, not from a structured DrugBank MOA field.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00143026](https://clinicaltrials.gov/study/NCT00143026) | Phase 4 | Completed | 184 | Carbidopa/levodopa/entacapone effect on quality of life (PDQ-8) in PD patients with minimal motor fluctuations |
| [NCT00360568](https://clinicaltrials.gov/study/NCT00360568) | Phase 3 | Completed | 62 | 12-month open-label safety/efficacy of levodopa-carbidopa intestinal gel in levodopa-responsive PD |
| [NCT00199407](https://clinicaltrials.gov/study/NCT00199407) | Phase 3 | Completed | 230 | Fixed-dose, double-blind, placebo-controlled trial of istradefylline added to levodopa/carbidopa in advanced PD with motor complications |
| [NCT01766258](https://clinicaltrials.gov/study/NCT01766258) | Phase 2 | Completed | 117 | ODM-101 (new LD/CD/entacapone combination) vs. standard Stalevo in PD with end-of-dose motor fluctuations |
| [NCT00880620](https://clinicaltrials.gov/study/NCT00880620) | Phase 3 | Completed | 381 | Placebo-controlled trial of three IPX066 (extended-release CD/LD) doses in PD |
| [NCT01227655](https://clinicaltrials.gov/study/NCT01227655) | Phase 3 | Completed | 427 | BIA 9-1067 add-on to levodopa/DDCI (carbidopa or benserazide) for wearing-off phenomenon |
| [NCT06596876](https://clinicaltrials.gov/study/NCT06596876) | Phase 3 | Recruiting | 450 | HRG2010 vs. sustained-release carbidopa-levodopa in PD with motor fluctuations |
| [NCT04750226](https://clinicaltrials.gov/study/NCT04750226) | Phase 3 | Active, not recruiting | 118 | Open-label extension evaluating 24-hour ABBV-951 (levodopa/carbidopa phosphate) exposure in advanced PD |
| [NCT01411137](https://clinicaltrials.gov/study/NCT01411137) | Phase 3 | Completed | 43 | Conversion study from CD-LD extended/immediate release to IPX066, with open-label extension safety follow-up |
| [NCT06765668](https://clinicaltrials.gov/study/NCT06765668) | Phase 4 | Recruiting | 220 | Real-world efficacy and safety of CREXONT (carbidopa/levodopa extended-release capsules) in PD |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25449210](https://pubmed.ncbi.nlm.nih.gov/25449210/) | 2015 | Review | Movement Disorders | Comprehensive review of levodopa pharmacokinetics/pharmacodynamics, including carbidopa's role as a decarboxylase inhibitor |
| [30566307](https://pubmed.ncbi.nlm.nih.gov/30566307/) | 2017 | Review | Nihon Rinsho | Overview of current anti-parkinsonian drug options, including levodopa/carbidopa formulations (e.g., intestinal gel) |
| [30361296](https://pubmed.ncbi.nlm.nih.gov/30361296/) | 2019 | Cohort | J Neurol Neurosurg Psychiatry | REIN-PD trial: behavioral/impulse-control changes after switching from dopamine agonists to levodopa/carbidopa |
| [8787797](https://pubmed.ncbi.nlm.nih.gov/8787797/) | 1995 | PK modeling study | Biol Pharm Bull | Pharmacokinetic model of oral levodopa clarifying carbidopa's effect on levodopa disposition |
| [9316692](https://pubmed.ncbi.nlm.nih.gov/9316692/) | 1994 | Clinical study | Clinical Neuropharmacology | PK and clinical efficacy of controlled-release levodopa/carbidopa 25/100 in untreated PD patients |
| [3403218](https://pubmed.ncbi.nlm.nih.gov/3403218/) | 1988 | Clinical study | Italian Journal of Neurological Sciences | Peripheral pharmacokinetics of levodopa/carbidopa and relation to the on-off phenomenon |
| [9235023](https://pubmed.ncbi.nlm.nih.gov/9235023/) | 1997 | Clinical study | Neurologia | Multicenter double-blind comparison of standard vs. slow-release levodopa/carbidopa formulations |
| [477187](https://pubmed.ncbi.nlm.nih.gov/477187/) | 1979 | Case series | Clinical Science | Niacin depletion observed in PD patients treated with levodopa plus benserazide or carbidopa |
| [31032135](https://pubmed.ncbi.nlm.nih.gov/31032135/) | 2019 | Case report | Case Reports in Psychiatry | Attempted suicide in a PD patient on VIM-DBS and high-dose carbidopa-levodopa; raises psychiatric safety signal |
| [40579361](https://pubmed.ncbi.nlm.nih.gov/40579361/) | 2025 | Preclinical (rat model) | Journal of Pharmacy and Pharmacology | Neuroprotective mechanisms of vitamin E vs. levodopa/carbidopa in rotenone-induced PD model |

## Safety Considerations

Please refer to the package insert for safety information. (No TFDA/NPRA warnings, contraindications, or drug-interaction data are currently available in this evidence pack — resolving this is flagged as a **Blocking** data gap, see below.)

## Conclusion and Next Steps

**Decision: Hold (pending clarification), with existing standard-of-care use continuing under guardrails**

**Rationale:**
The evidence base for carbidopa in Parkinson's disease/parkinsonian disorder is extensive and mature (L1, 50 trials, 19 publications) — but this is because it is confirming carbidopa's **existing, decades-old core indication**, not a novel repurposing signal. The pack's own rationale explicitly notes ranks 1 and 4 are duplicate ontology labels for the same disease, and all five predicted indications carry a TxGNN score of 0.0%, which undermines confidence in the ranking itself. Treat this candidate as a data-quality/ontology artifact rather than a genuine new-indication opportunity; ranks 2, 3, and 5 (juvenile-onset/atypical parkinsonism subtypes) have little to no supporting evidence (L4–L5) and should remain on Hold.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the actual TFDA/NPRA package insert for warnings and contraindications before any safety-stage (S1) evaluation can proceed
- Resolve DG002: source a structured DrugBank MOA record rather than relying on narrative rationale text
- Correct/investigate the TxGNN scoring pipeline — a uniform 0.0% score across all five candidates suggests a normalization or export issue that should be fixed before this candidate set is used for prioritization
- Deduplicate "Parkinsonian Disorder" and "Parkinson Disease" at the ontology level so future runs don't double-count the same known indication as two separate repurposing candidates
- If genuine novel indications are the goal, re-run prediction excluding the drug's own labeled disease class to surface true candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

