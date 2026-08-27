---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin: From Acute Myeloid Leukemia to Acute Lymphoblastic/Lymphocytic Leukemia

## One-Sentence Summary

Daunorubicin is a classic anthracycline cytotoxic agent, established in clinical practice primarily for induction therapy of acute myeloid leukemia (AML). The TxGNN model's top-ranked prediction points to **Acute Lymphoblastic/Lymphocytic Leukemia (ALL)**, with 50 clinical trials retrieved from the query, several of which (grade A relevance) explicitly use daunorubicin-based induction protocols — though a substantial share of the retrieved trial pool actually concerns doxorubicin, not daunorubicin, and no literature was returned. Because the evidence pack's `original_indications` field is empty, this prediction may represent confirmation of an existing approved use rather than a genuinely novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myeloid leukemia (based on established pharmacological/clinical knowledge; specific approved indication text not returned in this evidence pack — see Data Gaps) |
| Predicted New Indication | Acute Lymphoblastic/Lymphocytic Leukemia (ALL) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ 已上市 (Marketed) |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on established pharmacological knowledge, Daunorubicin belongs to the anthracycline antibiotic class, acting as a DNA intercalator and topoisomerase II inhibitor that induces double-strand breaks and cytotoxicity in rapidly dividing cells. Its efficacy in AML induction has been proven for decades, and mechanistically this class of agents is broadly applicable across acute leukemias, since ALL and AML share the underlying vulnerability of rapidly proliferating blast cells to DNA-damaging cytotoxics.

Importantly, the repurposing rationale attached to this candidate notes that daunorubicin is already a long-standing component of standard ALL induction/consolidation regimens (e.g., VDLP-type and PETHEMA/LAL-family protocols), rather than a newly hypothesized use. Several of the highest-relevance trials (graded "A") are Spanish PETHEMA LAL-Ph-2000 and LAL-BR/2001 protocols, and one trial (NCT01990807) explicitly names daunorubicin in its consolidation arm. This suggests the empty `original_indications` field is more likely a data-collection gap than evidence that ALL is truly unapproved — this should be verified against the TFDA/DrugBank label before treating the candidate as a novel indication.

A caution: the majority of the 50 retrieved trials for this indication actually describe doxorubicin-based regimens (e.g., hyper-CVAD, DA-EPOCH), which are pharmacologically related but not the same drug. This substantially dilutes the apparent size of the evidence base and should be accounted for in any downstream scoring.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9,350 | Large COG standard-risk B-ALL/localized B-LLy trial; risk-adapted chemotherapy including anthracycline induction (Grade A relevance — daunorubicin is a common COG regimen component). |
| [NCT00526305](https://clinicaltrials.gov/study/NCT00526305) | Phase 4 | Completed | 100 | LAL-Ph-2000 (PETHEMA, Spain): treatment protocol for Philadelphia-positive ALL; this protocol family conventionally uses daunorubicin rather than doxorubicin (Grade A). |
| [NCT00526175](https://clinicaltrials.gov/study/NCT00526175) | Phase 4 | Completed | 150 | LAL-BR/2001 (PETHEMA): low-risk ALL consolidation intensified with high-dose methotrexate; same protocol family as above, daunorubicin-based (Grade A). |
| [NCT01990807](https://clinicaltrials.gov/study/NCT01990807) | Phase 4 | Unknown | 20 | Philadelphia-negative high-risk childhood ALL: induction with idarubicin, consolidation explicitly includes daunorubicin + vincristine + L-asparaginase + dexamethasone. |
| [NCT02269579](https://clinicaltrials.gov/study/NCT02269579) | Phase 2 | Withdrawn (enrollment 0) | 0 | Pharmacokinetic study of CPX-351 (liposomal cytarabine:daunorubicin) in acute leukemias/MDS with hepatic impairment; trial did not proceed to enrollment. |
| [NCT00198978](https://clinicaltrials.gov/study/NCT00198978) | Phase 4 | Completed | 377 | GMALL Elderly 1/2003: dose-reduced chemotherapy for elderly ALL patients; anthracycline-based backbone but drug not specifically confirmed as daunorubicin (Grade B). |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6,136 | International collaborative COG/pediatric protocol comparing combination chemotherapy regimens for childhood ALL; anthracycline component not yet confirmed as daunorubicin-specific. |
| [NCT02883049](https://clinicaltrials.gov/study/NCT02883049) | Phase 3 | Active, not recruiting | 5,949 | COG high-risk B-ALL trial evaluating dasatinib addition for Ph-like TKI-sensitive mutations; large confirmatory trial, drug-specificity to daunorubicin not yet reviewed. |

## Literature Evidence

Currently no related literature available (PubMed query for Daunorubicin + acute lymphoblastic/lymphocytic leukemia returned 0 results as of the 2026-03-26 data cutoff).

## Malaysia Market Information

NPRA records indicate Daunorubicin is currently marketed in Malaysia with 3 registered product licenses. However, this evidence pack did not return the underlying license details (license numbers, product names, dosage forms, manufacturers, or approved indication text) — this is a data gap that should be filled from NPRA's product registry before regulatory submission planning.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Anthracycline class — DNA intercalator / topoisomerase II inhibitor) |
| Myelosuppression Risk | High — anthracyclines as a class cause significant dose-limiting neutropenia and thrombocytopenia (based on established pharmacological knowledge; drug-specific toxicity data not present in this evidence pack) |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | CBC with differential, cardiac function (LVEF/echocardiography — cumulative-dose cardiotoxicity risk), liver and renal function, infusion site monitoring (vesicant/extravasation risk) |
| Handling Protection | Yes — must follow cytotoxic drug handling and disposal regulations; vesicant precautions required during administration |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data were all flagged as data gaps in this evidence pack — see Data Gap DG001, which is classified as Blocking and must be resolved before safety review can proceed.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ALL prediction is supported by L1-level evidence (multiple completed/active Phase 3 trials), and several of the highest-relevance trials use daunorubicin-based regimens consistent with existing clinical practice. However, the original indication is not confirmed in this data pack, a large share of the retrieved trial evidence is confounded by doxorubicin (a related but distinct drug), and safety/label data is entirely missing (Blocking gap DG001).

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — resolves Blocking gap DG001
- DrugBank mechanism-of-action confirmation — resolves gap DG002
- Verification of whether ALL is already an approved indication for Daunorubicin (to distinguish label-extension confirmation from true repurposing)
- Malaysia license detail records (license numbers, product names, dosage forms, approved indication text)
- Re-review of clinical trial relevance grading to exclude doxorubicin-mismatched trials from the daunorubicin evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

