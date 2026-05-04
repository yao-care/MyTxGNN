---
layout: default
title: Azithromycin Dihydrate
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Azithromycin Dihydrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Azithromycin Dihydrate: Drug Repurposing Evaluation Report

## One-Sentence Summary

Azithromycin dihydrate is a macrolide antibiotic widely used for the treatment of bacterial infections, with 39 registrations currently active in Malaysia. The TxGNN model has **not generated any predicted new indications** for this drug at this time, and critical data gaps (mechanism of action, safety profile) remain unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (license indication text not provided) |
| Predicted New Indication | **None** — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions, no supporting studies) |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 39 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not produced any repurposing predictions for Azithromycin Dihydrate. This may be due to one or more of the following reasons:

1. **Missing DrugBank ID mapping**: The evidence pack shows `drugbank_id: null`. Without a valid DrugBank identifier, the drug cannot be properly located within the TxGNN knowledge graph, which relies on DrugBank nodes to establish drug–disease relationships. The query log indicates a DrugBank search was performed and returned 1 result, but this mapping was not successfully integrated into the evidence pack.

2. **Incomplete mechanism of action data**: Detailed MOA data is not available in this evidence pack. Azithromycin is widely known as a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. Beyond its antimicrobial activity, azithromycin has documented immunomodulatory and anti-inflammatory properties, which have driven investigation in conditions such as chronic obstructive pulmonary disease (COPD), cystic fibrosis, and COVID-19. However, without MOA data formally linked in the knowledge graph, the model cannot leverage these mechanistic connections.

3. **Data integration gap**: The approved indication text for all 39 Malaysian registrations is empty, meaning the pipeline could not extract the original therapeutic context needed for indication-based reasoning.

---

## Clinical Trial Evidence

Currently no predicted indication is available; therefore, no targeted clinical trial search was conducted.

---

## Literature Evidence

Currently no predicted indication is available; therefore, no targeted literature search was conducted.

---

## Malaysia Market Information

The NPRA database returned 39 registrations for Azithromycin Dihydrate; however, detailed licence information (authorization numbers, product names, dosage forms, and approved indications) was not captured in this evidence pack.

| Item | Content |
|------|------|
| Total Registrations | 39 |
| Product Details | Not available — license data fields are empty |

> **Note:** To complete this section, the NPRA Quest database (https://quest3plus.bpfk.gov.my/) should be re-queried to retrieve full product registration details.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not generate any repurposing predictions for Azithromycin Dihydrate. This is primarily attributable to the missing DrugBank ID mapping and the absence of approved indication text, which together prevent the knowledge graph from establishing the drug's position in the disease–drug network. No evaluation of repurposing potential can proceed until these foundational data gaps are resolved.

**To proceed, the following is needed:**

1. **Resolve DrugBank mapping** — Query the DrugBank API for "Azithromycin" (DB00207) and link it to the evidence pack. The query log confirms a match exists but was not integrated.
2. **Re-extract NPRA licence data** — Re-query the NPRA Quest database to populate authorization numbers, product names, dosage forms, and approved indication text for all 39 registrations.
3. **Obtain MOA data** — Retrieve the mechanism of action from DrugBank (macrolide antibiotic; 50S ribosomal subunit inhibitor; immunomodulatory properties).
4. **Obtain safety profile** — Download and parse the package insert (PIL) from NPRA to extract key warnings, contraindications, and drug interactions.
5. **Re-run TxGNN prediction** — Once DrugBank ID and indication data are integrated, re-execute the KG and DL prediction pipeline to generate repurposing candidates.

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

