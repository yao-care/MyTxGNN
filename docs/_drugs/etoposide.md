---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Established Oncology Indications to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a long-marketed cytotoxic chemotherapy agent in Malaysia (2 NPRA registrations); the specific original approved indication text is not available in the current data pack. The TxGNN model's top-ranked prediction is **well-differentiated fetal adenocarcinoma of the lung**, but this is currently supported by only **1 indirect case-report/review** and **no clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current Malaysia registration data (see Data Gap DG001) |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, DrugBank query pending). Based on information embedded in this evidence pack's own rationale entries, Etoposide is consistently identified as a **topoisomerase II inhibitor** used as a component of standard cytotoxic combination regimens (e.g., platinum-etoposide for small cell lung cancer, ifosfamide-etoposide for Ewing sarcoma and rhabdomyosarcoma). This confirms it belongs to the conventional cytotoxic chemotherapy class, even though a formal DrugBank MOA record has not yet been retrieved.

Well-differentiated fetal adenocarcinoma (WDFA) is a rare histologic subtype within the pulmonary blastoma family of lung tumors. Mechanistically, a topoisomerase II inhibitor could plausibly be applied to this tumor type by analogy with other pulmonary blastoma-family cases, where platinum-etoposide-class regimens have been used as adjuvant chemotherapy.

However, the single supporting literature reference is a case report of **classic biphasic pulmonary blastoma** — a related but histologically distinct entity — rather than WDFA itself, and the treatment described in that case used nedaplatin plus paclitaxel, not etoposide. The evidence pack's own rationale flags this explicitly: the title match is imprecise and the support is indirect, with no WDFA-specific clinical data. This is a case where TxGNN's high prediction score reflects a structural/mechanistic inference rather than an evidence-backed clinical signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case report/Review | The Journal of International Medical Research | Case report of classic biphasic pulmonary blastoma (a related pulmonary blastoma-family tumor, not WDFA itself); patient treated with nedaplatin plus paclitaxel as adjuvant chemotherapy, not etoposide. Notes no standard treatment guidelines exist for pulmonary blastoma due to rarity. |

## Malaysia Market Information

Etoposide is recorded as marketed in Malaysia with 2 total registrations; however, specific authorization numbers, product names, dosage forms, and approved indication text are not available in the current data pack (all fields blank in the source query). Remediation requires pulling full NPRA product listings.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor / epipodophyllotoxin class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
WDFA is an exceptionally rare tumor subtype, and the sole supporting literature item is an indirect case report of a related but distinct entity (classic biphasic pulmonary blastoma) that did not even use etoposide-based treatment. With no clinical trials and no WDFA-specific data, evidence is insufficient to move this candidate past a research hypothesis.

**To proceed, the following is needed:**
- WDFA-specific case series, registry data, or trial evidence involving etoposide-based regimens
- Completion of Data Gap DG001 (TFDA/NPRA label warnings and contraindications) and DG002 (confirmed DrugBank MOA)
- Full Malaysia license and approved-indication text for the 2 existing registrations
- Formal DDI and toxicity data to support a safety pre-screen (S1)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

