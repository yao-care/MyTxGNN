---
layout: default
title: Streptokinase
parent: Low Evidence (L4-L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Streptokinase
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Streptokinase: From Thrombolytic Therapy to Myocardial Infarction

## One-Sentence Summary

Streptokinase is a bacterial-derived fibrinolytic (thrombolytic) enzyme. The TxGNN model's top prediction for this drug is **Myocardial Infarction**, supported by **20 historical publications** — however, this predicted indication substantially overlaps with streptokinase's long-established classical clinical use as a thrombolytic in acute MI, so it should be read as evidence *confirmation* rather than a novel repurposing signal. No structured clinical trials are registered for this specific pairing, and Malaysia (NPRA) label/safety data for this candidate is currently a blocking gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — NPRA license record field is currently blank (see Safety Considerations) |
| Predicted New Indication | Myocardial Infarction |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 (multiple historical randomized controlled trials in literature) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is not available for this candidate (data gap). Based on general pharmacological knowledge, streptokinase is a **fibrinolytic/thrombolytic enzyme**: it forms a complex with plasminogen that catalyzes conversion of plasminogen to plasmin, which in turn degrades fibrin and dissolves intravascular thrombi.

Myocardial infarction is caused by acute coronary artery thrombosis; a thrombolytic that clears the occlusive clot and restores coronary flow is mechanistically directly applicable to this condition. Consistent with this, the literature evidence set is dominated by studies (from the 1970s–1990s) evaluating exactly this use — reperfusion therapy for acute MI.

**Important caveat**: this is not really a "new" indication being discovered — thrombolysis for acute MI is streptokinase's classical, decades-old primary clinical application. The TxGNN score here most likely reflects the model recovering a well-known drug–disease association embedded in its training knowledge graph, rather than surfacing a genuinely novel repurposing opportunity. This should be weighed heavily when interpreting the "Go/Hold" recommendation below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP both returned 0 results for Streptokinase × myocardial infarction; the supporting evidence predates the modern trial-registry era, which is consistent with the literature dates below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4934187](https://pubmed.ncbi.nlm.nih.gov/4934187/) | 1971 | RCT | British Medical Journal | European Working Party multicentre trial; 730 evaluable MI patients randomized to streptokinase vs. heparin. |
| [481511](https://pubmed.ncbi.nlm.nih.gov/481511/) | 1979 | RCT | New England Journal of Medicine | Controlled trial in 512 stratified AMI patients at 11 European centers; 24-hour streptokinase infusion vs. glucose significantly reduced 6-month mortality (p<0.01) in medium/high-risk groups. |
| [2888018](https://pubmed.ncbi.nlm.nih.gov/2888018/) | 1987 | RCT | New England Journal of Medicine | Double-blind trial, 219 patients with AMI <4h from onset; IV streptokinase (1.5 MU) vs. placebo; primary endpoint left ventricular function. |
| [3312370](https://pubmed.ncbi.nlm.nih.gov/3312370/) | 1987 | Review | Journal of the American College of Cardiology | Review of randomized trials of intracoronary and intravenous streptokinase for AMI, including Western Washington and Netherlands trials. |
| [8028463](https://pubmed.ncbi.nlm.nih.gov/8028463/) | 1994 | Meta-analysis / Decision analysis | Medical Decision Making | Combined meta-analysis and decision analysis of cost-effectiveness of IV streptokinase by infarct location and likelihood of infarction. |
| [21070617](https://pubmed.ncbi.nlm.nih.gov/21070617/) | 2012 | Review | Cardiovascular Therapeutics | Reviews streptokinase's discovery and demonstrated mortality benefit in AMI, and later tissue plasminogen activators (alteplase, reteplase, tenecteplase). |
| [10172727](https://pubmed.ncbi.nlm.nih.gov/10172727/) | 1995 | Review | Journal of Interventional Cardiology | European Working Party streptokinase trials and European Cooperative Study Group alteplase trials in AMI. |
| [7895344](https://pubmed.ncbi.nlm.nih.gov/7895344/) | 1995 | Review | Circulation | Discusses optimal AMI management requiring early, complete reperfusion. |
| [3815914](https://pubmed.ncbi.nlm.nih.gov/3815914/) | 1987 | Case report | Clinical Cardiology | 45-year-old man developed a second (anterior) MI during apparently successful streptokinase therapy for an initial inferolateral MI. |
| [8005961](https://pubmed.ncbi.nlm.nih.gov/8005961/) | 1993 | Review | Journal of the Association of Physicians of India | Discussion of streptokinase use in acute MI. |

---

## Malaysia Market Information

The NPRA record confirms **1 active registration** with market status "Marketed," but the specific license number, product name, dosage form, and approved-indication text fields are currently blank in the underlying record (data gap — see DG001). These fields need to be populated from the official NPRA product insert before market-detail claims can be made.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug–drug interaction data are all currently unavailable — DG001, Blocking severity — and must be obtained from the official NPRA/manufacturer package insert before any safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The efficacy evidence for streptokinase in myocardial infarction is strong (multiple historical RCTs), but this largely reflects the drug's already-established classical use rather than a novel repurposing signal, limiting the value of pursuing it as a "new indication" candidate.
- More critically, TFDA/NPRA label data (warnings, contraindications, DDI) is a **Blocking** data gap that prevents even an initial (S1) safety evaluation — the candidate cannot progress until this is resolved.

**To proceed, the following is needed:**
- Obtain and parse the official NPRA package insert (warnings, contraindications, interactions) to close DG001
- Retrieve DrugBank MOA/classification data to close DG002
- Confirm streptokinase's actual approved indication text on the Malaysia label, to determine whether MI is already covered (making this a label-expansion/confirmation exercise, not true repurposing)
- Deprioritize the low-evidence downstream candidates already flagged Hold/L5 in this pack (e.g., hemoglobinopathy, partial 16p deletion), which appear to be knowledge-graph artifacts rather than plausible signals
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

