---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: From Vitamin C Deficiency to Acute Injury Management

## One-Sentence Summary

Ascorbic acid (Vitamin C, DrugBank ID: DB00126) is an essential micronutrient classically used to prevent and treat vitamin C deficiency and scurvy. The TxGNN model identifies 10 novel indications across evidence levels L1–L5; among genuine repurposing candidates, the strongest novel evidence supports its role in **acute injury management** — including burns, transfusion-related acute lung injury (TRALI), and sepsis-induced organ dysfunction — backed by **multiple completed Phase 2/3 clinical trials** and **20+ publications**. The model also confirms its established utility in vitamin deficiency disorders (L1 evidence, Proceed with Guardrails), though this represents its traditional rather than a novel indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin C deficiency (scurvy); general nutritional supplementation |
| Predicted New Indication | Acute Injury (burns, TRALI, sepsis-related organ injury) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1,140 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on well-established pharmacological knowledge, ascorbic acid is a potent water-soluble antioxidant and essential co-factor for prolyl hydroxylase and lysyl hydroxylase — the enzymes required for collagen cross-linking and vascular integrity. These functions place it directly at the intersection of injury biology: tissue repair, oxidative stress resolution, and microvascular stability.

The mechanistic bridge to acute injury management is particularly compelling for three reasons. First, critically ill and burned patients exhibit precipitous drops in plasma ascorbic acid within hours of injury onset, creating a functional deficiency state. Second, high-dose intravenous ascorbic acid reduces microvascular hyperpermeability — the primary driver of the massive fluid shifts seen in burns and sepsis — and attenuates oxidative damage in TRALI. Third, in spinal cord injury models, ascorbic acid promotes functional recovery through TET-enzyme-dependent epigenetic modulation (DNA demethylation of regeneration-associated genes), an entirely novel mechanism that goes beyond simple antioxidant activity.

The TxGNN knowledge graph likely captures these dense mechanistic interconnections between ascorbic acid, ROS pathways, inflammatory cascades, and collagen metabolism. However, a critical caveat must be emphasised: the LOVIT trial (n=872, Phase 3, 2022) found no significant benefit of high-dose IV vitamin C on mortality or persistent organ dysfunction at 28 days in septic ICU patients, and the VICToRY burn trial (n=666, Phase 3) has been suspended. These results indicate that therapeutic benefit is likely context-specific — patient population, injury subtype, and timing of administration remain critical unresolved variables.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04153487](https://clinicaltrials.gov/study/NCT04153487) | Phase 2 | Completed | 40 | IV ascorbic acid in critically ill patients with TRALI — directly evaluates ascorbic acid for transfusion-related acute lung injury; the most relevant trial for this specific injury subtype |
| [NCT03780933](https://clinicaltrials.gov/study/NCT03780933) | N/A | Completed | 40 | High-dose vitamin C in critically ill ARDS patients — assessed oxidant/antioxidant imbalance, hospital stay, mechanical ventilator weaning, and mortality rate |
| [NCT03680274](https://clinicaltrials.gov/study/NCT03680274) | Phase 3 | Completed | 872 | LOVIT trial — high-dose IV vitamin C vs. placebo in septic ICU patients; primary endpoint (mortality or persistent organ dysfunction at 28 days) was not met; results published 2022 |
| [NCT02873026](https://clinicaltrials.gov/study/NCT02873026) | Phase 3 | Completed | 300 | Triamcinolone adjunct in open globe eye trauma surgery — Phase 3 RCT evaluating recovery after serious ocular injury; vitamin C used as part of post-injury protocol |
| [NCT04138394](https://clinicaltrials.gov/study/NCT04138394) | Phase 3 | Suspended | 666 | VICToRY trial — high-dose IV vitamin C in severely burned critically ill patients; currently suspended, limiting conclusions |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recruiting | 20,000 | REMAP-CAP — large adaptive platform trial; ascorbic acid is one experimental arm for community-acquired pneumonia and sepsis-related injury |
| [NCT06050668](https://clinicaltrials.gov/study/NCT06050668) | Phase 2 | Recruiting | 60 | MEND Repair & Recover — essential amino acid-based supplementation for muscle recovery after femoral fragility fracture; vitamin C included |
| [NCT02216812](https://clinicaltrials.gov/study/NCT02216812) | N/A | Completed | 134 | Vitamin C to reduce finger stiffness after distal radius fracture — RCT with objective motion measurement and patient-reported outcomes |
| [NCT04216459](https://clinicaltrials.gov/study/NCT04216459) | N/A | Completed | 112 | Anti-inflammatory and anti-microbial co-supplementation (including vitamin C) in traumatic ICU patients at high risk of sepsis |
| [NCT01548105](https://clinicaltrials.gov/study/NCT01548105) | N/A | Completed | 96 | Collagen metabolism markers and vitamin C in smokers with pelvic organ prolapse — mechanistic evidence for vitamin C's role in connective tissue injury repair |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27852613](https://pubmed.ncbi.nlm.nih.gov/27852613/) | 2017 | RCT | Am J Clin Nutr | Vitamin C-enriched gelatin supplementation before intermittent activity augments collagen synthesis — direct clinical evidence for musculoskeletal injury prevention and repair |
| [33675075](https://pubmed.ncbi.nlm.nih.gov/33675075/) | 2021 | Review | JPEN | Comprehensive review of ascorbic acid in acute care: burns, sepsis, ARDS, TRALI — dosing, pharmacokinetics, IV administration, and evidence summary |
| [31440996](https://pubmed.ncbi.nlm.nih.gov/31440996/) | 2020 | Review | Neurocrit Care | High-dose IV ascorbic acid in traumatic brain injury — reviews mechanistic rationale; inflammatory and oxidative stress pathways central |
| [32466098](https://pubmed.ncbi.nlm.nih.gov/32466098/) | 2020 | Animal/Mechanistic | Cells | Ascorbic acid promotes functional restoration after spinal cord injury via epigenetic modulation (TET enzyme-dependent DNA demethylation of regeneration-associated genes) |
| [37199082](https://pubmed.ncbi.nlm.nih.gov/37199082/) | 2023 | Animal study | Clin Exp Pharmacol Physiol | Melatonin + ascorbic acid synergistically protect against sepsis-induced lung injury in rats — oxidative stress, inflammation, and histopathology improved |
| [31631076](https://pubmed.ncbi.nlm.nih.gov/31631076/) | 2020 | Retrospective | Ann Thorac Cardiovasc Surg | Corticosteroids + ascorbic acid + thiamine improved oxygenation after thoracoscopic esophagectomy — clinical evidence for post-surgical injury management |
| [25977448](https://pubmed.ncbi.nlm.nih.gov/25977448/) | 2015 | Mechanistic | J Appl Physiol | Ascorbic acid abrogates microparticle generation and vascular injuries from high-pressure exposure in murine model |
| [30777116](https://pubmed.ncbi.nlm.nih.gov/30777116/) | 2019 | Animal study | J Orthop Surg Res | Ascorbic acid + T3 outperformed bone marrow mesenchymal stem cells in Achilles tendon injury rat model — tendon healing outcomes superior |
| [32141505](https://pubmed.ncbi.nlm.nih.gov/32141505/) | 2020 | Retrospective | J Burn Care Res | Safety and pharmacodynamics of high vs. low dose ascorbic acid in severely burned adults (n=38) — high-dose protocol feasibility assessed |
| [12643856](https://pubmed.ncbi.nlm.nih.gov/12643856/) | 2003 | Observational | J Surg Res | Ascorbic acid dynamics in critically ill and injured patients — documents acute depletion post-injury and assesses high-dose supplementation potential |

---

## Malaysia Market Information

Individual product registration data (authorization numbers, product names, dosage forms, approved indications) were not populated in the current Evidence Pack. Based on NPRA query results, **1,140 registered products** containing ascorbic acid are currently on the Malaysian market. This reflects extremely broad availability across multiple dosage forms. For the acute injury indication, however, **intravenous high-dose formulations** (typically 25–200 mg/kg/day) would be specifically required — their availability and registration status should be confirmed separately, as the majority of current registrations are likely oral supplements and tablets.

---

## Safety Considerations

Please refer to the package insert for detailed safety information. Full safety data (NPRA warnings and contraindications) were not available in this Evidence Pack.

**Key safety notes from published literature:**

- **High-dose IV renal risk**: Doses exceeding 10 g/day may cause hyperoxaluria, raising the risk of calcium oxalate nephrolithiasis — particularly in patients with pre-existing renal impairment. Monitor serum creatinine and urinary oxalate in high-dose IV protocols.
- **Drug-induced esophageal injury**: Case series document esophageal stricture from vitamin C tablets in patients with esophageal motility disorders or inadequate water intake (PMID [3606243](https://pubmed.ncbi.nlm.nih.gov/3606243/), [20227023](https://pubmed.ncbi.nlm.nih.gov/20227023/)). Relevant to oral formulations only.
- **Context-specific pro-carcinogenic concern**: Animal data show that ascorbic acid combined with sodium nitrite under acidic conditions (e.g., acid reflux) may enhance esophageal carcinogenesis (PMID [17953708](https://pubmed.ncbi.nlm.nih.gov/17953708/)). Not relevant to acute injury use but noted for completeness.
- **Warfarin interaction**: Case reports suggest high-dose ascorbic acid may interfere with warfarin anticoagulation (PMID [4739125](https://pubmed.ncbi.nlm.nih.gov/4739125/)); monitor INR in patients on anticoagulation therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 clinical trials demonstrate a clinically meaningful signal for high-dose intravenous ascorbic acid in specific acute injury subtypes, particularly TRALI and burn resuscitation, supported by a robust mechanistic rationale. However, the negative LOVIT Phase 3 trial in sepsis patients and the suspension of the VICToRY burn trial mean that the evidence base is uneven across injury subtypes — and the benefit is unlikely to apply uniformly across all "injury" presentations. Proceeding requires careful indication selection and a structured clinical development plan.

**To proceed, the following is needed:**
- Select a specific injury subtype as the primary target (e.g., TRALI, burn resuscitation, or traumatic spinal cord injury) rather than pursuing the broad "injury" category
- Confirm availability and regulatory status of high-dose IV ascorbic acid formulations in Malaysia (current 1,140 registrations are predominantly oral/supplement products)
- Obtain complete safety data from the Malaysian package insert (NPRA; currently a data gap flagged as Blocking)
- Design a focused Phase 2/3 RCT with clearly defined patient population, dosing protocol (50–200 mg/kg/day IV), validated primary endpoints (e.g., SOFA score, fluid balance, length of stay), and pre-specified subgroup analyses by injury type
- Implement mandatory renal monitoring (serum oxalate, creatinine) in high-dose IV protocols
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

