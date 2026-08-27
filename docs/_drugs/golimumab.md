---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 5
---

# Golimumab
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

# Golimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

> Golimumab is a fully human anti-TNF-α monoclonal antibody used for rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis.
> The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
> with **3 clinical trials** and **6 publications** currently identified, though none directly trial golimumab for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (per literature evidence in this pack; NPRA license text was not returned) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Malaysia Market Status | Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, golimumab is a fully human anti-TNF-α monoclonal antibody (part of the anti-TNF biologic class), its efficacy in rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis has been proven, and mechanistically may be applicable to rheumatoid vasculitis.

Rheumatoid vasculitis is a severe extra-articular manifestation of long-standing, seropositive rheumatoid arthritis, driven in part by TNF-α-mediated vascular inflammation. One of the identified publications (PMID 29075910) explicitly notes that the incidence of rheumatoid vasculitis has declined since the introduction of biologic DMARDs, including anti-TNF-α agents — golimumab's own drug class. Two further publications (PMID 22999907, Takayasu's arteritis; PMID 23252659, Behçet's disease-associated uveitis) describe anti-TNF/golimumab use in other vasculitis-related autoimmune conditions, lending mechanistic plausibility.

However, none of the identified clinical trials enrolled patients specifically for rheumatoid vasculitis — they are general RA observational studies, an immune-mediated-disease risk registry, and a peri-operative management trial. The supporting literature is dominated by case reports rather than controlled studies, so this remains a mechanism-and-case-level signal rather than a clinically validated indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of RoActemra/Actemra (tocilizumab, not golimumab) in RA patients with inadequate response to DMARDs/biologics — general RA practice-pattern data, not vasculitis-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Registry study of incident immune-mediated inflammatory disease (IMID) risk in patients on biologics/immunosuppressants for a single IMID |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Assesses rheumatologic flares and complications in rheumatology patients (on immunosuppressants) undergoing shoulder arthroplasty — perioperative management, not a treatment trial for vasculitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatology International | Case of pyoderma gangrenosum/pyogenic arthritis presenting as severe sepsis in an RA patient on golimumab; notes rheumatoid vasculitis incidence has declined since biologic anti-TNF agents were introduced |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (36 RCTs) | International Journal of Molecular Sciences | Golimumab and other anti-TNF agents similarly reduce joint destruction in RA vs. methotrexate |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Observational | Seminars in Arthritis and Rheumatism | Frequency, causes, and RA treatment considerations in patients with end-stage renal disease |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Update on biologic therapies (including anti-TNF) for autoimmune/rheumatologic diseases |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of Takayasu's arteritis occurring under anti-TNF therapy — relevant to anti-TNF/vasculitis interplay but a cautionary, not supportive, signal |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocular Immunology and Inflammation | Behçet disease-associated uveitis successfully treated with golimumab |

---

## Malaysia Market Information

NPRA records show **2 registered licenses** for golimumab with market status "Marketed," but this evidence pack did not return license number, product name, dosage form, manufacturer, or approved-indication text for either registration — these fields came back empty from the data source and are not fabricated here.

---

## Safety Considerations

TFDA/NPRA label warnings, contraindications, and drug-interaction data were not retrieved in this evidence pull (flagged as a **Blocking** data gap, DG001) — this must be resolved before any safety-stage (S1) evaluation. Please refer to the package insert for safety information in the interim.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (DG001: TFDA/NPRA label warnings/contraindications) prevents the mandatory S1 safety initial assessment, regardless of indication-evidence strength.
- Evidence specific to rheumatoid vasculitis is limited to case reports and non-specific RA/IMID trials — no direct RCT — placing this candidate at L4.

**To proceed, the following is needed:**
- NPRA product label (warnings/contraindications) — resolves DG001
- DrugBank/other MOA detail — resolves DG002
- License-level product name, dosage form, and approved-indication text for the 2 Malaysia registrations
- A search for registry or case-series data on golimumab specifically in rheumatoid vasculitis, beyond the isolated case reports identified here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

