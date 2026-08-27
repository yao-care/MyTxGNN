---
layout: default
title: Ethanol
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 2
---

# Ethanol
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

# Ethanol: From Antiseptic/Disinfectant Use to Migraine Disorder

## One-Sentence Summary

Ethanol (DrugBank DB00898) is a widely used topical antiseptic/disinfectant and pharmaceutical solvent; the evidence pack does not provide a verified NPRA-approved indication text for the Malaysian market. The TxGNN model predicts a possible role in **Migraine Disorder** with a high score (99.29%), but this direction is **not supported by the underlying evidence** — the 32 clinical trials and 20 publications retrieved either are unrelated to ethanol or explicitly identify alcohol as a migraine **trigger**, not a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiseptic/disinfectant, pharmaceutical solvent (general known use — NPRA licence indication text was not returned in this evidence pack) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only; no supporting clinical/observational evidence for a therapeutic effect) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ethanol is not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge, ethanol is a CNS depressant and enzyme/receptor modulator (e.g., GABA-A potentiation, NMDA inhibition) used clinically mainly as a topical antiseptic, solvent/preservative, and antidote for toxic alcohol poisoning — none of which have an established mechanistic link to migraine prevention or treatment.

Critically, the collected evidence points in the **opposite direction** from the TxGNN prediction. A mechanistic study (PMID 37101198) shows that ethanol's metabolite acetaldehyde activates the CGRP receptor and TRPA1 pathway on Schwann cells, inducing migraine-like periorbital allodynia in mice — i.e., ethanol *promotes* migraine-type pain rather than relieving it. Multiple reviews (PMID 36373782, 41305669, 18231712) confirm that alcohol is a well-recognized migraine **trigger** in roughly a third of migraine patients, not a therapeutic agent.

The high TxGNN score most likely reflects a knowledge-graph artifact: ethanol and migraine co-occur frequently in the literature because of their well-documented *trigger/comorbidity* relationship, which the model may have misclassified as a *treatment* relationship. This should be treated as a caution flag rather than confirmation of a genuine repurposing opportunity.

---

## Clinical Trial Evidence

None of the retrieved trials involve ethanol as a migraine treatment. The following are the reviewed (Grade C) trials surfaced by the search — all judged unrelated or only coincidentally co-occurring with the search terms:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05351086](https://clinicaltrials.gov/study/NCT05351086) | Phase 1 | Completed | 26 | PUR3100 safety/PK study, unrelated to ethanol |
| [NCT06517446](https://clinicaltrials.gov/study/NCT06517446) | N/A | Recruiting | 48 | VR-based vestibular rehabilitation, non-pharmacological, unrelated to ethanol |
| [NCT07207603](https://clinicaltrials.gov/study/NCT07207603) | N/A | Enrolling by invitation | 1000 | Cardiovascular risk cohort study, not a migraine treatment trial |
| [NCT05454826](https://clinicaltrials.gov/study/NCT05454826) | N/A | Completed | 26 | Cold application + relaxation exercises for migraine, non-pharmacological |
| [NCT07297901](https://clinicaltrials.gov/study/NCT07297901) | N/A | Enrolling by invitation | 30 | App-based breathing/biofeedback program, non-pharmacological |
| [NCT02810015](https://clinicaltrials.gov/study/NCT02810015) | Phase 2 | Unknown | 40 | Botulinum toxin for temporo-myofascial disorder, unrelated to ethanol |
| [NCT06197542](https://clinicaltrials.gov/study/NCT06197542) | N/A | Completed | 54 | Manual therapy techniques for migraine, unrelated to ethanol |
| [NCT03757208](https://clinicaltrials.gov/study/NCT03757208) | N/A | Completed | 113 | Preoperative carbohydrate loading, unrelated to migraine or ethanol |
| [NCT06263920](https://clinicaltrials.gov/study/NCT06263920) | N/A | Recruiting | 360 | Late-onset epilepsy/stroke/dementia cohort, unrelated to ethanol |
| [NCT00109083](https://clinicaltrials.gov/study/NCT00109083) | Phase 2 | Completed | 300 | RWJ-333369 dose-ranging RCT for migraine prophylaxis — an unrelated investigational drug, not ethanol |

**No trial in the evidence pack tests ethanol as a migraine therapy.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | Comprehensive review of the alcohol–migraine relationship; alcohol is consistently reported as a headache trigger, not a therapeutic agent |
| [41305669](https://pubmed.ncbi.nlm.nih.gov/41305669/) | 2025 | Review | Nutrients | Reviews alcohol as a trigger for migraine and tension-type headache; pathophysiology unclear, no therapeutic role identified |
| [18231712](https://pubmed.ncbi.nlm.nih.gov/18231712/) | 2008 | Review | J Headache Pain | MEDLINE review confirms alcohol as a recognized migraine trigger in ~1/3 of patients |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Preclinical/Mechanistic | J Biomed Sci | Ethanol's metabolite acetaldehyde activates CGRP receptor/TRPA1 on Schwann cells, producing migraine-like allodynia in mice — mechanistic evidence ethanol worsens, not relieves, migraine-type pain |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | Cohort/Survey | Aerosp Med Hum Perform | Observational study of migraine history in military pilots; not related to ethanol treatment |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetic Association | Headache | ADH2 gene polymorphism and migraine risk; alcohol-metabolism genetics, not treatment evidence |
| [36674807](https://pubmed.ncbi.nlm.nih.gov/36674807/) | 2023 | Genetic Association | Int J Mol Sci | LAG3/CD4 gene variants and migraine risk; unrelated to ethanol pharmacology |
| [29299688](https://pubmed.ncbi.nlm.nih.gov/29299688/) | 2018 | Genetic Association | J Neural Transm | GABA receptor gene polymorphisms and migraine risk; unrelated to ethanol |
| [31792366](https://pubmed.ncbi.nlm.nih.gov/31792366/) | 2020 | Genetic Association | Pharmacogenomics J | NOS3 gene polymorphism and migraine risk; unrelated to ethanol |
| [8681169](https://pubmed.ncbi.nlm.nih.gov/8681169/) | 1996 | Review | Rev Neurol | Reviews dietary migraine triggers including alcoholic beverages; supports alcohol as a trigger, not a treatment |

**Overall pattern: every substantive publication frames alcohol/ethanol as a migraine trigger or metabolic risk-modifier — none support a therapeutic effect.**

---

## Malaysia Market Information

The evidence pack confirms 11 NPRA registrations exist for ethanol (market status: Marketed), but license-level details (registration number, product name, dosage form, manufacturer, approved indication text) were not returned by the query and cannot be reported here without fabrication.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data were returned for ethanol in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but every piece of retrieved clinical and literature evidence contradicts the predicted direction — alcohol/ethanol is consistently documented as a migraine **trigger**, and one mechanistic study shows it actively promotes migraine-like pain via CGRP/TRPA1 signaling. No clinical trial in the evidence pack tests ethanol as a migraine treatment. Combined with the blocking absence of safety/label data (DG001) and mechanism-of-action data (DG002), there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (DG001, blocking — required before any S1 safety screen)
- Verified mechanism of action data from DrugBank (DG002)
- Any primary research (if it exists) specifically testing ethanol as a migraine therapeutic, rather than as a trigger or comorbidity factor
- License-level NPRA registration details (product names, dosage forms, approved indication text) for the 11 Malaysian registrations
- A re-review of the TxGNN knowledge-graph edge underlying this prediction, given the strong contradicting mechanistic and epidemiological signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

