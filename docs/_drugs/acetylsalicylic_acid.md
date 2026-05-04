---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acetylsalicylic Acid: From Analgesic & Antiplatelet Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin, DB00945) is one of the world's oldest and most widely used medications, established for pain relief, fever reduction, anti-inflammatory effects, and cardiovascular protection through its irreversible COX inhibition and antiplatelet mechanism.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly basilar-type migraine) — a rare subtype involving brainstem-originating aura symptoms,
with **0 registered clinical trials** specific to this indication and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic, antipyretic, anti-inflammatory, and antiplatelet therapy (specific approved indication text not recorded in current regulatory dataset) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. However, aspirin's pharmacology is well-characterised from the broader literature: aspirin irreversibly acetylates serine residues on COX-1 (Ser529) and COX-2 (Ser516), blocking the conversion of arachidonic acid to prostaglandins and thromboxane A₂ (TXA₂). This dual mechanism — suppressing neuroinflammatory mediators (PGE₂, IL-1β) and irreversibly inhibiting platelet activation — is directly relevant to migraine pathophysiology, which involves sensitisation of the trigeminovascular system and release of CGRP and prostaglandins from perivascular trigeminal nerve terminals.

Migraine with brainstem aura is characterised by fully reversible aura symptoms attributable to brainstem dysfunction — diplopia, dysarthria, tinnitus, vertigo, and ataxia — before or during headache. The core mechanism involves cortical spreading depression (CSD) propagating into or originating from the brainstem, activating trigeminal nuclei (particularly the trigeminal nucleus caudalis in the pons) and triggering local neuroinflammation. Aspirin's upstream inhibition of PGE₂ synthesis and attenuation of CGRP-related sensitisation pathways in the trigeminovascular system provides a biologically plausible basis for modulating both the aura and headache phases. Additionally, the well-documented platelet hypothesis of migraine — wherein aberrant platelet serotonin release and TXA₂-mediated vasoconstriction contribute to CSD triggering — directly implicates aspirin's antiplatelet mechanism as a potential therapeutic lever.

Critically, a retrospective cohort study (PMID 25729594, n=203) directly evaluated low-dose aspirin as prophylaxis specifically for migraine with aura, and the 2015 American Headache Society evidence assessment (PMID 25600718) positions aspirin as a Level A/B agent for acute migraine management. A 2025 systematic review (PMID 39989443) further explored antithrombotic drugs — including aspirin — in migraine prevention. However, the "brainstem aura" subtype carries a higher vascular spasm risk than standard migraine with aura, and careful ischaemic risk evaluation is required before applying general migraine-with-aura evidence to this specific subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura and acetylsalicylic acid.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review (AHS) | *Headache* | Updated AHS evidence assessment of acute migraine pharmacotherapies; aspirin and aspirin-containing combinations rated as effective Level A agents for acute migraine, including migraine with aura |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | *Headache* | Systematic review of antithrombotic drugs (including aspirin) as migraine preventive medication; explored biological rationale and available clinical evidence for antiplatelet agents in migraine prevention |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | *Cephalalgia* | Double-blind double-dummy RCT (n=278, 17 centres): IV lysine acetylsalicylate 1.8 g vs sumatriptan 6 mg SC in acute migraine with or without aura; ASA demonstrated comparable acute efficacy to sumatriptan |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Cohort | *Curr Health Sci J* | Retrospective study (n=203 migraine-with-aura patients per ICHD-II criteria): 46.8% treated with low-dose ASA as prophylaxis; evaluated efficacy and tolerability over ≥4 months — most direct evidence for ASA in migraine with aura prevention |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | *Revue neurologique* | Comprehensive review of migraine with aura: cortical spreading depression as the pivotal mechanism underlying aura; ICHD-III diagnostic criteria and treatment overview including anti-inflammatory approaches |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | *Curr Pain Headache Rep* | Compared pathophysiology, epidemiology, and clinical implications of migraine with and without aura; higher cardiovascular/cerebrovascular risk in aura subtypes informs treatment selection and risk stratification |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Guideline Review | *FP Essentials* | AHA/ASA primary stroke prevention guidelines; migraine with aura recognised as a modifiable stroke risk factor, with aspirin discussed in context of vascular risk modification |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | *Heart* | Clopidogrel (antiplatelet) reduced migraine with aura episodes after transcatheter PFO closure; provides indirect support for the antiplatelet mechanism in modulating migraine with aura, including aura related to right-to-left shunt |
| [36657989](https://pubmed.ncbi.nlm.nih.gov/36657989/) | 2023 | Cohort Study | *Neurology* | Prepregnancy migraine phenotype and risk of adverse pregnancy outcomes; migraine with aura associated with distinct obstetric risk profile — relevant for treatment decision-making in reproductive-age women |
| [2701286](https://pubmed.ncbi.nlm.nih.gov/2701286/) | 1989 | Review | *Biomed Pharmacother* | Seminal 10-year review of the platelet hypothesis of migraine; foundational mechanistic basis for aspirin's potential in migraine via inhibition of platelet TXA₂ release and serotonin dysregulation |

---

## Malaysia Market Information

The Evidence Pack confirms **15 registered products** for acetylsalicylic acid in Malaysia, with a current market status of **Marketed (已上市)**. However, specific product details — including authorization numbers, brand names, dosage forms, manufacturers, and approved indication texts — were not retrieved in the current data query. Please consult the National Pharmaceutical Regulatory Agency (NPRA) product register directly for full product listings.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Specific consideration for this indication:** Migraine with brainstem aura (basilar-type migraine) involves a higher theoretical risk of vasospasm compared to common migraine with aura. Although aspirin is generally used in migraine management, patients with this specific subtype should be carefully evaluated for ischaemic and haemorrhagic risk before initiating antiplatelet prophylaxis. The interaction of aspirin with other vasoactive migraine medications (e.g., ergotamines, triptans) and the risk of gastrointestinal bleeding with long-term use are additional safety factors that require monitoring. Full warnings, contraindications, and drug interaction data should be retrieved from the NPRA-approved package insert to support a complete S1 safety evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple systematic reviews, one double-blind RCT for acute migraine (with or without aura), and a retrospective cohort study specifically evaluating low-dose aspirin in migraine-with-aura prophylaxis collectively provide Level 3 evidence (observational studies and systematic reviews); however, no clinical trial data exist specifically for the brainstem aura subtype, and the higher vascular risk profile of this rare subtype warrants a cautious, monitored approach before extrapolating from broader migraine-with-aura evidence.

**To proceed, the following is needed:**
- Dedicated prospective clinical trials or high-quality registry data specifically enrolling migraine with brainstem aura patients
- Retrieval of full MOA data from DrugBank API (currently a data gap) to strengthen mechanistic link analysis
- Download and parsing of NPRA-approved package insert PDF to complete the S1 safety evaluation (warnings, contraindications, key drug interactions)
- Retrieval of specific product registration details (authorization numbers, approved indications) from the NPRA register for all 15 registered products
- Vascular risk stratification protocol for patients with brainstem aura, given elevated ischaemic risk compared to standard migraine with aura
- Definition of the optimal dose regimen (acute vs. prophylactic low-dose) specific to this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

