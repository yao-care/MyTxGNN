---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 5
---

# Betamethasone
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

# Betamethasone: From Inflammatory Conditions to Erythema Multiforme

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid widely used for various inflammatory, allergic, and autoimmune conditions across 97 registered products in Malaysia. The TxGNN model predicts it may be effective for **Erythema Multiforme (EM)**, with **17 clinical trials** and **20 publications** currently providing supporting or related evidence for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-inflammatory / immunosuppressive corticosteroid (broad dermatological, rheumatic, and allergic indications) |
| Predicted New Indication | Erythema Multiforme |
| TxGNN Prediction Score | 0.00% (rank 1) |
| Evidence Level | L3 — Observational studies and case series available |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 97 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Erythema multiforme (EM) is an acute, immune-mediated hypersensitivity reaction affecting the skin and mucous membranes, primarily driven by CD8+ cytotoxic T-cell attack on keratinocytes. The condition exists on a clinical spectrum that includes mild cutaneous EM minor at one end and the severe, life-threatening Stevens-Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN) at the other. The underlying immunopathology — T-cell activation, pro-inflammatory cytokine release, and keratinocyte apoptosis — is well-characterized.

Betamethasone, as a high-potency synthetic glucocorticoid, exerts its effects by suppressing T-cell activation, inhibiting the release of pro-inflammatory cytokines (IL-1, IL-6, TNF-α), and reducing keratinocyte apoptotic signalling. These mechanisms directly oppose the key pathological processes driving EM. In severe EM variants (SJS/TEN), topical betamethasone has already been reported in clinical use, particularly for ocular complications (PMID 37182731), lending real-world support to this mechanistic rationale.

However, a critical caveat exists: EM itself has been reported as an adverse reaction to betamethasone treatment (PMID 14206262), suggesting a paradoxical relationship. This bidirectional association — where the drug may both treat and occasionally trigger the condition — necessitates careful patient selection and monitoring. The mechanistic link is rated as moderate-to-strong, but the paradoxical induction risk must be factored into any clinical translation.

---

## Clinical Trial Evidence

> **Note:** No clinical trials directly studying betamethasone for erythema multiforme were identified. The trials below involve betamethasone or related potent corticosteroids in dermatological or EM-spectrum conditions (SJS/TEN), providing indirect supportive evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT03331523](https://clinicaltrials.gov/study/NCT03331523) | Phase 3 | Completed | 643 | Generic calcipotriene/betamethasone dipropionate topical suspension vs Taclonex® for scalp psoriasis. Demonstrates large-scale safety of topical betamethasone in inflammatory skin disease. |
| [NCT03731091](https://clinicaltrials.gov/study/NCT03731091) | Phase 3 | Completed | 494 | Generic calcipotriene/betamethasone dipropionate foam vs Enstilar® for plaque psoriasis. Confirms topical betamethasone efficacy and tolerability. |
| [NCT01422434](https://clinicaltrials.gov/study/NCT01422434) | Phase 3 | Completed | 676 | LEO 90105 ointment (calcipotriol + betamethasone dipropionate) vs monotherapy in Japanese psoriasis vulgaris patients. Large-scale safety data in Asian population. |
| [NCT02319616](https://clinicaltrials.gov/study/NCT02319616) | Phase 1/2 | Withdrawn | 0 | Clobetasol 0.05% ointment for TEN — directly on the EM/SJS/TEN spectrum. Unfortunately withdrawn with no data generated. |
| [NCT05185258](https://clinicaltrials.gov/study/NCT05185258) | Phase 4 | Active, not recruiting | 12 | Enstilar® (calcipotriol/betamethasone) and NB-UVB therapy investigating residual disease memory in psoriatic skin. Explores corticosteroid effects on immune memory. |
| [NCT00820950](https://clinicaltrials.gov/study/NCT00820950) | Phase 2 | Completed | 29 | Ruxolitinib phosphate cream dose-escalation study in plaque psoriasis. Provides comparative context for topical anti-inflammatory agents. |
| [NCT03880357](https://clinicaltrials.gov/study/NCT03880357) | Phase 1 | Completed | 485 | Bioequivalence study of betamethasone-containing product for scalp psoriasis. Large-scale tolerability data. |
| [NCT03395132](https://clinicaltrials.gov/study/NCT03395132) | Phase 3 | Terminated | 68 | Fusidic acid/betamethasone cream (Fucicort®) in clinically infected atopic dermatitis/eczema. Terminated early but relevant to infected inflammatory skin conditions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [37182731](https://pubmed.ncbi.nlm.nih.gov/37182731/) | 2023 | Clinical Study / Case Series | Am J Ophthalmol | Topical betamethasone treatment of SJS/TEN with ocular involvement in the acute phase. Demonstrates direct clinical use of betamethasone in the EM-spectrum. |
| [40500649](https://pubmed.ncbi.nlm.nih.gov/40500649/) | 2025 | Review | Allergol Int | Updates on ocular manifestations and treatment of SJS/TEN. Confirms importance of early topical steroid intervention for ocular complications. |
| [38795750](https://pubmed.ncbi.nlm.nih.gov/38795750/) | 2024 | Cohort / National Study | Am J Ophthalmol | National survey in Japan on SJS/TEN ocular sequelae incidence and prognostic factors (2016–2018 vs 2005–2007). Evidence of improving prognosis with treatment advances. |
| [14206262](https://pubmed.ncbi.nlm.nih.gov/14206262/) | 1964 | Case Report (Adverse Event) | Br J Clin Pract | **Critical safety signal:** EM occurring *during* betamethasone treatment for pruritus vulvae and neurodermatitis. Documents paradoxical EM induction. |
| [1068978](https://pubmed.ncbi.nlm.nih.gov/1068978/) | 1976 | Review | Int Dent J | Corticosteroids in oral mucosal diseases, including betamethasone valerate 0.1 mg for oral EM. Reports efficacy when administered during prodromal phase. |
| [26297574](https://pubmed.ncbi.nlm.nih.gov/26297574/) | 2015 | Protocol | Trials | RCT protocol for topical clobetasol in TEN treatment. Supports rationale for potent topical corticosteroids in the EM-SJS-TEN spectrum. |
| [2011350](https://pubmed.ncbi.nlm.nih.gov/2011350/) | 1991 | Open Trial | Oral Surg Oral Med Oral Pathol | Clobetasol propionate in adhesive paste for chronic oral vesiculoerosive diseases, including EM patients. 4 chronic EM patients showed improvement. |
| [32105227](https://pubmed.ncbi.nlm.nih.gov/32105227/) | 2020 | Case Report | Gen Dent | Fluconazole-induced EM in immunocompetent patient. Provides pathophysiology context and treatment approach for drug-induced EM. |
| [37854261](https://pubmed.ncbi.nlm.nih.gov/37854261/) | 2023 | Case Report | Clin Case Rep | EM provoked by radiotherapy in a 63-year-old patient. Disseminated erythematous lesions treated with corticosteroid-based approach. |
| [22082897](https://pubmed.ncbi.nlm.nih.gov/22082897/) | 2011 | Case Report | Intern Med (Tokyo) | Severe obliterative bronchitis associated with SJS. Betamethasone was directly administered as primary treatment for SJS. |

---

## Malaysia Market Information

> Betamethasone has **97 registered products** and is actively marketed in Malaysia. Detailed license-level data (authorization numbers, product names, dosage forms, and approved indications) was not available in the current data extract. Below is a summary of known status:

| Item | Content |
|------|---------|
| Total Registrations | 97 |
| Market Status | Marketed |
| Common Dosage Forms | Topical cream/ointment, injection, oral tablet, eye drops (based on global betamethasone formulations) |
| Primary Approved Indications | Anti-inflammatory and immunosuppressive conditions (dermatological, rheumatic, allergic, and ophthalmic indications) |

---

## Safety Considerations

> Detailed safety data (key warnings, contraindications, and drug interactions) was not available in the current data extract. Please refer to the package insert for comprehensive safety information.

**Known class-level considerations for potent glucocorticoids:**
- Prolonged use may cause skin atrophy, striae, telangiectasia (topical), and adrenal suppression (systemic)
- Immunosuppression increases infection risk
- **Paradoxical EM induction** has been documented during betamethasone treatment (PMID 14206262) — requires vigilant monitoring
- Systemic absorption from extensive topical application or occlusive dressings may cause hypothalamic-pituitary-adrenal (HPA) axis suppression

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between betamethasone's immunosuppressive properties and EM's immune-mediated pathology is moderate-to-strong. Literature evidence directly supports use of betamethasone in the SJS/TEN spectrum (severe EM variants), and corticosteroids are already used off-label for oral and ocular EM manifestations. However, the absence of EM-specific clinical trials and the documented paradoxical EM induction by betamethasone warrant a cautious approach.

**To proceed, the following is needed:**
- **Mechanism of action (MOA) data**: Obtain detailed betamethasone MOA from DrugBank to strengthen mechanistic rationale
- **Package insert safety data**: Download and parse the full prescribing information from NPRA for key warnings, contraindications, and drug interactions
- **Targeted literature review**: Systematic review of corticosteroid use specifically in EM minor (non-SJS/TEN) to distinguish evidence from the broader EM-SJS-TEN spectrum
- **Paradoxical risk assessment**: Formal evaluation of the incidence and risk factors for corticosteroid-induced EM, to develop patient exclusion criteria
- **Route-of-administration analysis**: Determine which betamethasone formulations (topical, oral, injectable, ophthalmic) are most appropriate for different EM presentations
- **Prospective observational study design**: Plan a pilot observational study or case registry for betamethasone in moderate-to-severe EM to generate direct clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

