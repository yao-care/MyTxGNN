---
layout: default
title: Mycophenolic Acid
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Mycophenolic Acid
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

# Mycophenolic Acid: From Transplant Rejection Prophylaxis to Hemoglobinopathy

## One-Sentence Summary

Mycophenolic acid (the active moiety of mycophenolate mofetil) is an established immunosuppressant used to prevent solid organ transplant rejection.
The TxGNN model predicts a possible association with **Hemoglobinopathy**, but the underlying evidence shows the drug is used as a **graft-versus-host disease (GVHD) prophylaxis agent during hematopoietic stem cell transplantation (HSCT)** for conditions like thalassemia and sickle cell disease — not as a direct treatment for the blood disorder itself — with **27 clinical trials** and **9 publications** currently supporting this indirect association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of organ (renal/cardiac/hepatic) transplant rejection *(NPRA license indication text not available in current data pull; based on known pharmacology)* |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the registry pull (data gap), but the evidence pack's mechanistic analysis indicates mycophenolic acid is a selective, reversible inhibitor of inosine monophosphate dehydrogenase (IMPDH). By blocking de novo guanine nucleotide synthesis, it selectively suppresses T- and B-lymphocyte proliferation — the pharmacological basis for its approved use as an anti-rejection immunosuppressant in organ transplantation.

The link to "hemoglobinopathy" does not reflect a disease-modifying effect on the blood disorder itself. Instead, allogeneic HSCT is a potentially curative procedure for severe hemoglobinopathies (thalassemia major, sickle cell disease), and mycophenolate mofetil is a standard component of the GVHD-prophylaxis regimen given alongside calcineurin inhibitors after transplant. In this sense, the same immunosuppressive mechanism that prevents organ-transplant rejection is being repurposed to prevent graft-versus-host reactions in HSCT for hemoglobinopathy — a related but mechanistically indirect application, not a primary therapy for the hematologic disease.

Because MMF is a supportive/adjunct medication in these trials rather than the study's primary intervention, the strength of the "repurposing" signal is weaker than it appears from the TxGNN score alone — this is reflected in the L3 (observational/cohort-level) evidence grade rather than a higher tier.

---

## Clinical Trial Evidence

*Note: In nearly all trials below, mycophenolate mofetil (MMF) is a component of the standard GVHD-prophylaxis regimen (alongside a calcineurin inhibitor ± other agents) rather than the primary study intervention.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04009525](https://clinicaltrials.gov/study/NCT04009525) | Phase 4 | Completed | 823 | Multicenter study evaluating allo-HSCT efficacy for thalassemia major; MMF likely part of standard GVHD prophylaxis, not the primary intervention |
| [NCT02342145](https://clinicaltrials.gov/study/NCT02342145) | Phase 4 | Completed | 205 | Randomized study of basiliximab for acute GVHD prevention after unrelated allo-HSCT in thalassemia major |
| [NCT03924401](https://clinicaltrials.gov/study/NCT03924401) | Phase 2 | Active, not recruiting | 30 | Extended abatacept combined with tacrolimus + MMF to prevent acute/chronic GVHD in pediatric non-malignant hematologic disease HSCT |
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Abatacept added to cyclosporine + MMF as GVHD prophylaxis in pediatric unrelated HSCT for non-malignant disease |
| [NCT02867800](https://clinicaltrials.gov/study/NCT02867800) | Phase 1 | Completed | 24 | Abatacept added to standard GVHD prophylaxis (calcineurin inhibitor + methotrexate) in pediatric sickle cell HSCT |
| [NCT02776202](https://clinicaltrials.gov/study/NCT02776202) | Phase 2 | Unknown | 15 | HLA-identical sibling bone marrow transplant with reduced-intensity conditioning for severe sickle cell disease |
| [NCT01050855](https://clinicaltrials.gov/study/NCT01050855) | Phase 2 | Active, not recruiting | 75 | Reduced-intensity conditioning regimen evaluating engraftment and toxicity in non-malignant disorders |
| [NCT06872333](https://clinicaltrials.gov/study/NCT06872333) | Phase 2 | Recruiting | 62 | Allogeneic HSCT for high-risk hemoglobinopathies and other red-cell transfusion-dependent disorders |
| [NCT05736419](https://clinicaltrials.gov/study/NCT05736419) | Phase 2 | Recruiting | 24 | Pre-transplant immune suppression with haploidentical HCT for sickle cell disease or β-thalassemia |
| [NCT03171831](https://clinicaltrials.gov/study/NCT03171831) | Phase 4 | Unknown | 30 | Safety and efficacy of haploidentical HSCT for thalassemia major |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Cohort/Case series | Transplantation and Cellular Therapy | MMF used to boost immunosuppression for declining mixed chimerism after HSCT in thalassemia |
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Retrospective/Dosing study | Eur J Drug Metab Pharmacokinet | Population PK-based off-label MMF dosing recommendations for pediatric thalassemia HSCT patients |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Cohort | Biol Blood Marrow Transplant | Alternative-donor HSCT with post-transplant cyclophosphamide for non-malignant disorders including hemoglobinopathies |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Cohort | Biol Blood Marrow Transplant | Unrelated-donor HSCT with post-transplant cyclophosphamide + tacrolimus/MMF for GVHD prophylaxis in severe sickle cell disease |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Cohort (Phase I) | Biol Blood Marrow Transplant | Unrelated umbilical cord blood transplant for sickle cell disease after reduced-intensity conditioning |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Cohort | Biol Blood Marrow Transplant | Stable long-term donor engraftment following reduced-intensity HCT for sickle cell disease |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Cohort/Risk factor analysis | Hematology (Amsterdam) | Risk factors for pure red cell aplasia following major ABO-incompatible allo-HSCT |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case report (safety signal, not efficacy) | J Perinatology | Neonatal anemia and hydrops fetalis reported after maternal MMF use during pregnancy — safety signal, relevant to contraindication assessment rather than efficacy |
| [15126382](https://pubmed.ncbi.nlm.nih.gov/15126382/) | 2004 | Historical/mechanistic (low direct relevance) | Genetics | General genetics/medicine commentary; tangential to the hemoglobinopathy indication |

---

## Malaysia Market Information

Malaysia registration status shows **5 active licenses (✓ Marketed)**, but authorization numbers, product names, dosage forms, and approved-indication text were not returned in the current NPRA data pull — this is tracked separately as a data gap requiring a direct NPRA lookup, and is not fabricated here.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data were not available in this data pull. Note: obtaining TFDA/NPRA label warnings and contraindications is flagged as a **Blocking** data gap (DG001) — it must be resolved before this candidate can proceed to initial safety screening (S1). One safety-relevant signal was found in the literature review: a case report of neonatal anemia and hydrops fetalis following maternal MMF use during pregnancy (PMID 17180133), which should be incorporated into the formal safety review once label data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association is supported mainly by MMF's role as a standard GVHD-prophylaxis component in HSCT for hemoglobinopathies, not as a direct treatment for the disease itself — evidence level is L3 (cohort/observational), and a Blocking-severity data gap on TFDA/NPRA safety warnings and contraindications prevents entry into initial safety screening (S1).

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data from DrugBank (High-priority gap, DG002)
- Complete Malaysia license/authorization details (license numbers, product names, approved indication text)
- A mechanistic re-assessment clarifying whether this candidate should be scoped as "MMF for hemoglobinopathy" or more precisely as "MMF for GVHD prophylaxis in HSCT for hemoglobinopathy," since these represent different clinical claims
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

