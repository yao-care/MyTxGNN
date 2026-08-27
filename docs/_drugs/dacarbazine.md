---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 1
---

# Dacarbazine
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

# Dacarbazine: From Established Oncology Indications to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine is an alkylating chemotherapy agent already marketed in Taiwan, with established use in cancers such as melanoma, Hodgkin lymphoma, and soft tissue sarcoma. The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm**, but this prediction is currently supported by **no clinical trials and no literature**, and rests solely on knowledge-graph similarity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extracted from Taiwan license data (license text unavailable); known established uses include melanoma, Hodgkin lymphoma, and soft tissue sarcoma |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, dacarbazine is an alkylating agent that acts through DNA methylation to inhibit tumour cell proliferation, and it is clinically established for melanoma, Hodgkin lymphoma, and soft tissue sarcoma.

The histological and tumour-biology overlap between these approved indications and upper aerodigestive tract neoplasms (predominantly squamous cell carcinomas of the head and neck, larynx, and esophagus) is limited. Without confirmed mechanism-of-action data, the biological rationale for extending dacarbazine to this indication cannot be independently verified at this time.

The TxGNN score of 99.26% reflects knowledge-graph embedding similarity only — it is not derived from mechanistic or clinical validation, and should be interpreted as a hypothesis-generating signal rather than evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Malaysia Market Information

Dacarbazine holds 2 registered licenses in Taiwan (market status: marketed), but detailed license fields (product name, dosage form, manufacturer, approved indication text) are not populated in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard cytotoxic drug handling precautions apply; please refer to institutional protocols |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no supporting clinical trials or literature, no confirmed mechanism-of-action data linking dacarbazine to upper aerodigestive tract neoplasms, and a blocking gap in TFDA label/safety data — the prediction currently rests on knowledge-graph similarity alone (L5, decision stage S0).

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking safety review
- Confirmed mechanism of action data from DrugBank or primary literature
- Targeted clinical trial and PubMed searches for dacarbazine in head/neck, laryngeal, or esophageal cancer
- Complete Taiwan license detail fields (product name, dosage form, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

