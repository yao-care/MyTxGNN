---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 488
evidence_level: L5
indication_count: 2
---

# Moclobemide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Moclobemide: From Depression to Agoraphobia

## One-Sentence Summary

Moclobemide is a reversible, selective MAO-A inhibitor (RIMA) established for the treatment of depression and social anxiety disorder. The TxGNN model predicts it may be effective for **Agoraphobia** (typically presenting as panic disorder with agoraphobia), with **12 publications** — including two randomized controlled trials — currently supporting this direction, though no clinical trials are registered for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression / Social Anxiety Disorder (based on drug class literature; TFDA registered indication text not available in this evidence pack) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap). Based on known pharmacological classification, moclobemide is a reversible inhibitor of monoamine oxidase A (RIMA), which increases synaptic concentrations of serotonin, norepinephrine, and dopamine — the accepted pharmacological basis for treating anxiety and panic-related disorders.

Agoraphobia is clinically and diagnostically closely linked to panic disorder, frequently co-occurring or classified jointly (panic disorder with agoraphobia). Most available literature studies moclobemide specifically in "panic disorder" rather than agoraphobia as an isolated diagnosis, making this an indirect but mechanistically coherent extension of its known anxiolytic/antidepressant activity rather than a novel therapeutic mechanism.

Two double-blind RCTs directly support efficacy in panic disorder with agoraphobia (comparing moclobemide against CBT and against clomipramine), reinforcing the plausibility of the TxGNN prediction even though no trial has targeted agoraphobia as a standalone endpoint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT | The British Journal of Psychiatry | Randomised placebo-controlled trial of moclobemide, CBT, and their combination in panic disorder with agoraphobia |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT | European Archives of Psychiatry and Clinical Neuroscience | Multicenter double-blind RCT: moclobemide 450mg/day vs clomipramine 150mg/day in panic disorder with/without agoraphobia (n=135) |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Cohort/RCT | Metabolic Brain Disease | SPECT comparison of citalopram vs moclobemide on resting brain perfusion in social anxiety disorder |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | Review | Clinical Neuropharmacology | Reversible MAO-A inhibitors (brofaromine, moclobemide) effective in panic disorder with fewer interactions than older MAOIs |
| [1498904](https://pubmed.ncbi.nlm.nih.gov/1498904/) | 1992 | Review | Clinical Neuropharmacology | Reversible MAO-A inhibitors in panic disorder |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Review | Dialogues in Clinical Neuroscience | Treatment guidelines for anxiety disorders including panic disorder/agoraphobia |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Review | Advances in Experimental Medicine and Biology | Current and novel psychopharmacological drugs for anxiety disorders including panic disorder/agoraphobia |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatrica Scandinavica Suppl. | Moclobemide shown effective vs multiple comparators (amitriptyline, imipramine, fluoxetine, etc.) across 4 placebo-controlled trials |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatrica Scandinavica Suppl. | MAOIs effective in controlled studies of panic disorder with agoraphobia, social phobia, and related conditions |
| [7892341](https://pubmed.ncbi.nlm.nih.gov/7892341/) | 1995 | Case Report | Psychiatrische Praxis | Treatment-refractory panic disorder with agoraphobia responded to combined imipramine + moclobemide + behavior therapy |

---

## Malaysia Market Information

Moclobemide is registered and marketed in Malaysia (1 active registration), but detailed license number, product name, dosage form, manufacturer, and approved indication text are not available in this evidence pack (data gap — requires NPRA product lookup).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/NPRA warnings, contraindications, and drug interaction data are marked as data gaps in this evidence pack — see below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two RCTs and a body of supporting review literature establish a mechanistically coherent link between moclobemide's MAO-A inhibition and panic disorder/agoraphobia, but no dedicated agoraphobia trial exists and safety documentation is currently missing — insufficient for an unconditional "Go" but too well-supported for "Hold."

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap — required before S1 safety assessment)
- Detailed mechanism of action (MOA) documentation from DrugBank
- Confirmed regulatory approved indication text and product details for the Malaysia registration
- Drug-drug interaction (DDI) data (currently not found)
- A prospective or retrospective study specifically targeting agoraphobia (rather than panic disorder broadly) as the primary endpoint

*Note: The second candidate indication, "benign paroxysmal torticollis of infancy" (TxGNN score 99.30%), has no literature or clinical trial support and no plausible mechanistic link — recommend Hold, likely a false-positive knowledge-graph prediction.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

