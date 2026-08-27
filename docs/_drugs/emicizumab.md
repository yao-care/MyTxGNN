---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

Using the evidence pack provided, I'm generating the drug repurposing evaluation report below. Note: among the 10 TxGNN-predicted indications in this evidence pack, only rank #5 ("acquired coagulation factor deficiency" — which maps to Acquired Haemophilia A) advanced past initial screening (S3, L1 evidence, "Proceed with Guardrails"); the other nine remain on Hold (S0) because their own mechanistic-link notes explicitly state the biology doesn't match emicizumab's mode of action, and none has supporting trials/literature. I've built the report around the evidence-supported candidate and appended a short note on the screened-out candidates for transparency.

---

# Emicizumab: From Congenital Haemophilia A to Acquired Haemophilia A

## One-Sentence Summary

> Emicizumab is a bispecific monoclonal antibody originally used to prevent bleeding episodes in patients with **congenital Haemophilia A** (with or without Factor VIII inhibitors).
> The TxGNN model predicts it may be effective for **Acquired Haemophilia A** (recorded in the knowledge graph as "acquired coagulation factor deficiency"),
> with **1 clinical trial** and **20 publications** — including three prospective Phase 2/3 studies and a formal working-group consensus statement — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Haemophilia A, with or without Factor VIII inhibitors *(based on internationally known indication for emicizumab; local NPRA licence text was not populated in this evidence pack)* |
| Predicted New Indication | Acquired Haemophilia A ("acquired coagulation factor deficiency") |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on publicly known pharmacology, emicizumab is a humanized bispecific IgG4 monoclonal antibody that simultaneously binds activated Factor IX (FIXa) and Factor X (FX), physically bridging them to restore the function of the intrinsic tenase complex — effectively mimicking the cofactor activity of activated Factor VIII (FVIIIa) without being a FVIII molecule itself.

Congenital Haemophilia A and Acquired Haemophilia A (AHA) are, at the coagulation-cascade level, the same functional lesion — insufficient FVIIIa cofactor activity in the intrinsic tenase complex — arising from two different causes: a genetic deficiency in congenital disease versus autoantibody-mediated neutralization of endogenous FVIII in AHA. Because emicizumab does not resemble native FVIII structurally, it is **not recognized or neutralized by anti-FVIII autoantibodies**, which is precisely the pathological driver of AHA.

This mechanistic independence from FVIII-inhibitor status is why emicizumab can restore haemostasis in AHA patients regardless of autoantibody titre, making it one of the mechanistically best-supported repurposing candidates identified for this drug — a conclusion echoed in the pack's own rationale: *"the disease corresponds substantively to Acquired Haemophilia A, where autoantibodies against FVIII cause functional FVIII deficiency; emicizumab's FIXa/FX bridging mechanism directly bypasses the inhibited FVIII and is unaffected by antibody interference, making it one of the most mechanistically plausible candidates for this indication."*

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | Recruiting | 3,000 | ATHN Transcends — a multicenter natural-history cohort registry tracking safety, effectiveness, and real-world treatment practice across non-neoplastic haematologic disorders, including acquired coagulation factor deficiencies. Provides descriptive/real-world safety signal rather than direct interventional efficacy data for emicizumab (evidence grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3 (single-arm, open-label) | J Thromb Haemost | First prospective, multicenter Phase 3 study of emicizumab prophylaxis specifically in patients with Acquired Haemophilia A. |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2/3 (GTH-AHA-EMI) | Lancet Haematology | Open-label, single-arm study showing emicizumab protects AHA patients from bleeding and allows immunosuppression to be deferred during the first 12 weeks. |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 final analysis (AGEHA) | Thrombosis and Haemostasis | Final AGEHA study results, including IST-ineligible patients, confirming a favourable benefit-risk profile for long-term emicizumab prophylaxis in AHA. |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus/Guideline (GTH-AHA Working Group) | Hämostaseologie | Formal working-group consensus recommendations on the use of emicizumab in Acquired Haemophilia A. |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Narrative Review | J Thromb Haemost | Overview of AHA epidemiology, pathophysiology, and management in "the emicizumab era." |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Real-world Cohort (US multicenter) | Blood Advances | Retrospective data on 62 AHA patients treated off-label with emicizumab across 12 US haemophilia treatment centers. |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohort (2-year follow-up) | Blood Advances | Sustained survival benefit and postponed immunosuppression in AHA patients followed up after the GTH-AHA-EMI study. |
| [38562115](https://pubmed.ncbi.nlm.nih.gov/38562115/) | 2024 | Review | Haemophilia | Reviews recent advances in managing AHA, acquired von Willebrand syndrome, and chronic liver disease-related coagulopathy, noting emicizumab prophylaxis benefit in AHA. |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review (opinion) | Blood Transfusion | Discusses pros and cons of emicizumab as a new approach to preventing and treating bleeding in AHA. |
| [39401737](https://pubmed.ncbi.nlm.nih.gov/39401737/) | 2025 | Case Study | J Thromb Haemost | Detailed evaluation of anti-emicizumab (anti-drug) antibodies observed in a minority of AHA patients treated with emicizumab. |

---

## Malaysia Market Information

NPRA registration confirms **✓ Marketed** status with **2 active licences**. Detailed licence numbers, product names, dosage forms, and approved indication text were not populated in this evidence pack and require direct retrieval from NPRA before further regulatory assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple prospective Phase 2/3 studies (GTH-AHA-EMI, AGEHA) and a formal working-group consensus statement support emicizumab's efficacy and mechanistic suitability in Acquired Haemophilia A, and its FIXa/FX-bridging mechanism directly addresses the FVIII-inhibitor-driven pathology of AHA. However, this evidence base originates largely from off-label/registry use in other regulatory jurisdictions, so local (Malaysia) regulatory and safety documentation is still required before advancing further.

**To proceed, the following is needed:**
- NPRA licence detail (product names, dosage forms, approved indication text) — currently blank in the evidence pack
- Formal package insert data: key warnings, contraindications, and drug interactions (flagged as a **Blocking** data gap, DG001) — this must be resolved before any S1 safety assessment
- DrugBank-sourced mechanism-of-action documentation (High-severity data gap, DG002)
- Review of emicizumab's known thrombotic microangiopathy risk profile when co-administered with bypassing agents (e.g., aPCC), given AHA patients often require bypassing therapy for acute bleeds
- Local health authority guidance on off-label AHA use and any reimbursement pathway

---

### Other TxGNN-Predicted Indications (Held)

For completeness, this evidence pack screened 10 TxGNN-predicted indications for emicizumab. The remaining nine were held at the earliest screening stage (S0, L5 — model prediction only, no supporting evidence) because their own mechanistic assessments found no plausible link to emicizumab's FIXa/FX-bridging mode of action:

- **Pseudo-von Willebrand disease** and **Glanzmann thrombasthenia** — platelet receptor/glycoprotein defects, not coagulation-factor deficiencies
- **Primary platelet release disorder** and **bleeding diathesis due to a collagen receptor defect** — platelet activation/adhesion signalling defects
- **Scott syndrome** — platelet membrane phospholipid-scramblase defect
- **Hemorrhagic disorder due to constitutional thrombocytopenia** and **fetal/neonatal alloimmune thrombocytopenia** — platelet quantity or immune-destruction disorders, not factor-pathway defects
- **Thrombotic thrombocytopenic purpura** — a *thrombotic* (not bleeding) disorder; increasing thrombin generation here is a theoretical safety concern rather than a therapeutic opportunity and should be flagged as a caution, not pursued
- **"Flood factor deficiency"** — likely a knowledge-graph node-naming artifact with no recognized clinical correlate; requires source-data verification before any evaluation

None of these nine require further action at this time beyond periodic re-screening as new evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

