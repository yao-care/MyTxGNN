---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Acetaminophen: From Pain Relief to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is one of the world's most widely used over-the-counter analgesics and antipyretics, indicated for the relief of mild-to-moderate pain and reduction of fever.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, with **0 clinical trials** and **20 publications** currently supporting this direction.
The available evidence consists primarily of RCTs and systematic reviews on acetaminophen in general migraine — indirect support for this specific subtype — placing overall evidence at **L3**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain relief and fever reduction (analgesic / antipyretic) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acetaminophen's central analgesic action is primarily attributed to inhibition of COX-3 (cyclooxygenase-3), which reduces prostaglandin synthesis within the central nervous system. Beyond COX-3, it modulates descending pain control pathways — notably the periaqueductal grey (PAG) region of the brainstem — a structure critical for endogenous pain suppression. It is important to note that formal MOA data is not yet confirmed for this specific application; the mechanistic rationale presented here is based on indirect inference from its established central analgesic profile.

Migraine with brainstem aura is a distinct migraine subtype in which aura symptoms originate from the brainstem itself, manifesting as dysarthria, vertigo, tinnitus, diplopia, or ataxia. The underlying pathophysiology involves aberrant activation of the trigeminal nucleus caudalis and the brainstem reticular formation. Because acetaminophen acts directly on brainstem pain circuitry via the PAG and descending modulatory pathways, there is a plausible neuroanatomical and pharmacological basis for its efficacy in this subtype.

In broader clinical practice, acetaminophen is already endorsed as a first-line agent for mild-to-moderate migraine attacks — and is the preferred analgesic during pregnancy when NSAIDs and triptans are contraindicated. Extending this recommendation to the brainstem aura subtype is therefore a refinement of an existing indication rather than a wholly novel application, though direct mechanistic and clinical validation for this specific subtype is still lacking.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acetaminophen specifically in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT | *Archives of Internal Medicine* | Randomised, double-blind, placebo-controlled population-based study demonstrating efficacy and safety of acetaminophen monotherapy in acute migraine treatment |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT | *Archives of Neurology* | Three double-blind, placebo-controlled trials confirming acetaminophen + aspirin + caffeine combination effectively relieves migraine headache pain |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT | *Clinical Therapeutics* | Pooled analysis of 3 randomised placebo-controlled trials showing acetaminophen + aspirin + caffeine is effective for menstruation-associated migraine |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative Study | *Headache* | Head-to-head comparison of isometheptene/dichloralphenazone/acetaminophen vs sumatriptan for mild-to-moderate migraine with or without aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review / Clinical Guideline | *Headache* | American Headache Society updated evidence assessment of pharmacotherapies for acute migraine; positions acetaminophen within the treatment hierarchy |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Systematic Review | *Cureus* | Review of abortive and prophylactic migraine therapies in pregnancy; highlights acetaminophen as the primary safe acute treatment option |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Narrative Review | *Handbook of Clinical Neurology* | Covers status migrainosus — a severe complication of migraine with or without aura lasting >72 hours — and current treatment approaches |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | *Neurologic Clinics* | Confirms acetaminophen as first-line symptomatic treatment for headache in pregnancy, including migraine; discusses safety profile across trimesters |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | *Cureus* | Comprehensive review of migraine management during pregnancy and breastfeeding, including safety profiles and dosing considerations for analgesics |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | *Neurology International* | Overview of ubrogepant for acute migraine; contextualises acetaminophen and NSAIDs as standard first-line options for mild-to-moderate migraine attacks |

---

## Malaysia Market Information

Acetaminophen is confirmed as **marketed** in Malaysia with **5 registered products**. Detailed licence records (licence numbers, product names, dosage forms, and approved indication texts) are not available in the current dataset.

To retrieve full registration details, please consult the [NPRA Product Registration database](https://www.npra.gov.my/).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acetaminophen is a well-established analgesic with robust evidence for general migraine management and a highly favourable safety profile, making its application to migraine with brainstem aura a clinically reasonable extension. However, no clinical trials have been conducted specifically for this subtype, and the mechanistic link remains indirect inference requiring formal validation.

**To proceed, the following is needed:**
- Identify or design a prospective observational study or pilot RCT targeting patients with migraine with brainstem aura treated with acetaminophen
- Retrieve formal MOA data from DrugBank API (DG002) to confirm the COX-3 / brainstem PAG pathway hypothesis
- Download and parse the NPRA package insert PDF (DG001) to identify any contraindications or warnings relevant to this use case
- Assess drug-drug interaction profile, particularly with concurrent migraine prophylaxis agents (e.g., beta-blockers, valproate, topiramate)
- Engage a neurologist specialising in headache disorders to review clinical feasibility and define appropriate patient selection criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

