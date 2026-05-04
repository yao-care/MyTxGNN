---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Adenosine
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

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Adenosine is an endogenous purine nucleoside widely used in clinical practice as an antiarrhythmic agent — primarily for acute termination of paroxysmal supraventricular tachycardia (PSVT) and pharmacological cardiac stress testing.

The TxGNN model's top clinically valid predicted indication is **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, an inherited arrhythmia syndrome causing fatal ventricular arrhythmias triggered by adrenergic stimulation.

Currently, **1 Phase 2a clinical trial** (evaluating AGP100, an adenosine-pathway agent) and **13 publications** provide indirect mechanistic and clinical support for this repurposing direction.

> **Note on Rank 1 Prediction:** The highest-ranked TxGNN prediction ("obsolete bundle branch block", score 99.94%) carries an obsolete disease ontology label with zero supporting evidence; mechanistic rationale also does not support a direct adenosine effect on bundle branch conduction. This term has been set aside. CPVT (TxGNN rank 2, score 99.42%) is treated as the primary evaluation target in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Paroxysmal supraventricular tachycardia (PSVT); pharmacological cardiac stress testing |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured data source. Based on established pharmacological knowledge, Adenosine is an endogenous purine nucleoside that exerts its cardiac effects primarily through A1 adenosine receptors on the AV node and sinus node. Binding to A1 receptors activates Gi proteins, which suppress adenylyl cyclase activity, thereby reducing intracellular cyclic AMP (cAMP) and downstream protein kinase A (PKA) activity. This antiadrenergic cascade slows AV nodal conduction and forms the basis of its established use in terminating PSVT.

CPVT is driven by a mechanistically convergent but genetically distinct pathway: mutations in RyR2 (cardiac ryanodine receptor) or CASQ2 (calsequestrin-2) render the sarcoplasmic reticulum susceptible to catecholamine-triggered Ca²⁺ overload. During adrenergic stress, rising cAMP causes PKA to hyperphosphorylate RyR2, SR Ca²⁺ leaks into the cytoplasm, and delayed afterdepolarisations (DADs) trigger life-threatening bidirectional ventricular tachycardia. Adenosine's suppression of cAMP via A1–Gi signalling directly counteracts this cascade — placing it mechanistically upstream of the central CPVT arrhythmia trigger. Furthermore, ATP — adenosine's immediate precursor and a closely related purinergic ligand — has been shown to interact directly with the CPVT mutation-associated central domain of RyR2 (PMID 23747301), suggesting a possible channel-stabilising effect that is independent of cAMP modulation.

The strongest direct clinical observation supporting this hypothesis is a 2008 case report (PMID 18313614) in which intravenous ATP terminated bidirectional VT in a genetically confirmed CPVT patient. While this remains a single case, the convergence of (1) adenosine's antiadrenergic mechanism, (2) direct ATP–RyR2 binding data, and (3) an ongoing Phase 2a trial targeting the adenosine signalling axis in CPVT collectively indicate biological plausibility. The primary limitation is the absence of any prospective trial using Adenosine itself, and the pharmacokinetic challenge that adenosine's ultra-short intravenous half-life (~10 seconds) is poorly suited to the chronic oral prophylaxis that CPVT management requires.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | PACE-CPVT trial: evaluates safety, tolerability, and exploratory efficacy of AGP100 — a novel agent acting on the adenosine signalling pathway — in CPVT patients. Addresses the unmet need of patients who remain symptomatic on current therapy during exercise or emotional stress. Results expected by June 2027. |

> No clinical trial directly testing Adenosine itself in CPVT was identified. AGP100's results will provide critical pathway-level validation but cannot be directly extrapolated to Adenosine as a repurposed agent.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | Heart Rhythm | ATP terminates bidirectional VT in a confirmed CPVT patient — the only direct clinical observation linking the adenosine/ATP axis to CPVT suppression |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Basic Science | Biochim Biophys Acta | ATP binds directly to the CPVT mutation-associated central domain of RyR2, suggesting a channel-stabilising effect independent of cAMP modulation |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Clinical Review | Europace | ESC/HRS/APHRS/LAHRS consensus on pharmacological provocation testing in cardiac electrophysiology; establishes adenosine's diagnostic role in inherited arrhythmia syndromes |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Basic Science | Cardiovasc Res | PDE2A/PDE4B gene therapy prevents HF and arrhythmias by improving subcellular cAMP compartmentation — mechanistically supports cAMP reduction (adenosine's downstream effect) as a therapeutic target in CPVT |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | In vitro (Human Organoid) | J Physiol | Human cardiac-neural microtissue model reveals CPVT involves sympathetic neurons, reinforcing adrenergic-axis targets and broadening the therapeutic rationale for antiadrenergic agents |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Basic Science | Commun Biol | TECRL deficiency in CPVT causes mitochondrial dysfunction, contextualising disease heterogeneity and identifying potential non-responder subgroups for any repurposing strategy |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Observational | Heart Rhythm | EPS study in CPVT with RyR2 mutation demonstrates postpacing abnormal repolarisation; mechanistic support for DAD-based arrhythmia triggers targeted by adenosine |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Basic Science | Sci Transl Med | RyR2 stabiliser (rycal S36) reduces SR Ca²⁺ leak and improves survival in animal HF/arrhythmia models — convergent evidence that RyR2 stabilisation is a valid CPVT therapeutic strategy |
| [23858002](https://pubmed.ncbi.nlm.nih.gov/23858002/) | 2013 | Basic Science | J Gen Physiol | Calsequestrin regulation of RyR2 in CPVT pathophysiology — mechanistic rationale for why reducing PKA-mediated RyR2 hyperphosphorylation (adenosine's downstream effect) could suppress Ca²⁺ leak |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Classification and management framework for idiopathic and structurally normal-heart ventricular tachycardias including CPVT; contextual background for adenosine's established role in VT discrimination |

---

## Malaysia Market Information

Malaysia NPRA records confirm 2 registered products for Adenosine (market status: Marketed). However, detailed product-level data — including registration numbers, product names, dosage forms, manufacturers, and approved indication text — was not recoverable from the current data extract. A supplementary NPRA database lookup is required.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — (pending retrieval) | — | — | Supplementary NPRA query required |
| — (pending retrieval) | — | — | Supplementary NPRA query required |

---

## Safety Considerations

Detailed package insert warnings and contraindications were not available in the current evidence pack. Based on the established pharmacological class profile, the following are well-recognised clinical safety considerations for Adenosine:

- **Transient but significant cardiovascular effects**: Bradycardia, AV block (including transient complete heart block), hypotension; expected given the mechanism but require monitoring
- **Respiratory**: Bronchoconstriction; use with caution or avoid in asthma and reactive airways disease
- **Pharmacokinetic interactions**: Methylxanthines (theophylline, aminophylline, caffeine) competitively antagonise adenosine receptors and may negate therapeutic effect; dipyridamole potentiates adenosine's effects and requires dose reduction or is contraindicated
- **Route restriction**: Currently only approved for intravenous administration; the ultra-short half-life (~10 seconds) limits oral repurposing potential for chronic indications such as CPVT

> For complete and current safety information, please download and review the approved product monograph from NPRA or the relevant product manufacturer. Package insert PDF retrieval is classified as a Blocking data gap for formal safety assessment (DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Adenosine in CPVT is biologically coherent — its A1–Gi–cAMP–PKA axis directly targets the molecular trigger of CPVT arrhythmias, and a single case report demonstrates that the closely related purine ATP can terminate CPVT-induced bidirectional VT. However, the current evidence base reaches only L4 (basic science and mechanistic studies plus one case report), and Adenosine's intravenous-only, ultra-short-acting pharmacokinetic profile poses a fundamental barrier to use as a chronic prophylactic agent in CPVT.

**To proceed, the following is needed:**

- **Targeted literature review**: Systematic search specifically for adenosine or ATP use in CPVT or other inherited arrhythmia syndromes; identify any additional clinical observations beyond PMID 18313614
- **Pharmacokinetic feasibility assessment**: Evaluate whether modified-release adenosine formulations, adenosine receptor agonists (e.g., A1-selective agonists), or pro-drug strategies could overcome the duration-of-action barrier for a chronic CPVT indication
- **Mechanistic validation study**: In vitro or murine RyR2-mutant CPVT model directly testing adenosine (not only ATP or AGP100) on DAD frequency, VT inducibility, and SR Ca²⁺ leak
- **NPRA package insert retrieval**: Download approved Malaysian product monograph PDF and extract key warnings and contraindications to complete safety assessment (resolves DG001 — currently Blocking)
- **DrugBank MOA documentation**: Complete formal MOA profile via DrugBank API query (resolves DG002 — currently High severity)
- **Monitor PACE-CPVT trial (NCT07263139)**: AGP100 Phase 2a results (expected June 2027) will significantly validate or invalidate the adenosine-pathway hypothesis in CPVT and should gate any further investment in this repurposing direction
- **CPVT subtype stratification**: Clarify whether the RyR2 versus CASQ2 mutation subtype modifies the expected adenosine response, given differing upstream mechanisms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

