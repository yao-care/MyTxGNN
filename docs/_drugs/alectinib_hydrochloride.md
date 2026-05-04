---
layout: default
title: Alectinib Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 0
---

# Alectinib Hydrochloride
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

# Alectinib Hydrochloride: From ALK+ Non-Small Cell Lung Cancer to [No Repurposing Predictions Generated]

## One-Sentence Summary

Alectinib Hydrochloride is an ALK/RET tyrosine kinase inhibitor with an established indication in ALK-positive non-small cell lung cancer (NSCLC), and is confirmed as a marketed product in Malaysia with 1 registered licence.
However, the current Evidence Pack contains **no TxGNN-generated repurposing predictions** for this compound, as key upstream data — including the DrugBank ID, approved indication text, and safety information — were not successfully retrieved.
A full drug repurposing evaluation **cannot be completed** until these data gaps are resolved and the prediction pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in current data (known from background: ALK-positive NSCLC) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Background and Data Status

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, alectinib is an orally administered, selective ALK (Anaplastic Lymphoma Kinase) and RET kinase inhibitor. Its efficacy in ALK-positive NSCLC has been well established through pivotal Phase 3 trials (e.g., ALEX, J-ALEX, ALESIA), demonstrating superior progression-free survival compared to crizotinib, including activity against CNS metastases.

The TxGNN knowledge graph prediction step did not produce any candidate repurposing indications in the current run. This is most likely attributable to the unresolved `drugbank_id: null` field — the DrugBank ID is required as a node identifier in the knowledge graph, and its absence prevents TxGNN from computing similarity scores against disease nodes.

Once the DrugBank mapping is restored (DB ID: DB11363 for alectinib) and the pipeline is re-executed, biologically plausible repurposing candidates may include other ALK-driven malignancies such as anaplastic large cell lymphoma (ALCL), inflammatory myofibroblastic tumour (IMT), and neuroblastoma — all of which overexpress or harbour ALK fusions. However, these candidates must be formally scored by TxGNN before evaluation can proceed.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective ALK/RET tyrosine kinase inhibitor (second-generation) |
| Myelosuppression Risk | Low to moderate; anaemia and neutropenia reported but less frequent than conventional cytotoxics |
| Emetogenicity Classification | Low (oral agent; nausea reported in ~18% of patients) |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST/bilirubin), renal function, pulmonary function, ECG (QTc), CPK (myalgia/rhabdomyolysis risk) |
| Handling Protection | Oral solid dosage form; standard handling precautions for oral targeted therapies apply; avoid crushing capsules without containment |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings and contraindications are listed as data gaps in the current Evidence Pack (DG001: Severity — Blocking). No drug-drug interaction data was retrieved (query status: not_found). Full safety evaluation is blocked until the product insert is retrieved and parsed.

---

## Malaysia Market Information

The Evidence Pack confirms **1 active registration** with market status **✓ Marketed (已上市)**. However, all licence record fields (licence number, product name, dosage form, manufacturer, and approved indication text) were returned as empty strings and could not be populated in this report.

> **Action required:** Query the NPRA Product Registration database directly at [https://www.npra.gov.my](https://www.npra.gov.my) using the search term "ALECTINIB" to retrieve the full registration record and approved indication text.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction pipeline did not generate any TxGNN repurposing candidates for alectinib, most likely due to a missing DrugBank ID that prevents the drug from being located as a node in the knowledge graph. Without scored predictions, no evidence-based repurposing evaluation can be conducted.

**To proceed, the following is needed:**

- **[Critical — DG001]** Retrieve the Malaysian product insert (PI/SmPC) from the NPRA database to populate approved indication, warnings, and contraindications
- **[Critical — DG002]** Resolve `drugbank_id: null` — confirmed DrugBank ID is **DB11363**; update the mapping table and re-run `scripts/run_kg_prediction.py`
- **[Critical]** Re-run the full TxGNN prediction pipeline after DrugBank mapping is restored; expected repurposing candidates include ALK-driven tumours beyond NSCLC
- **[High]** Populate the licence record fields (product name, dosage form, approved indication) from NPRA to complete the regulatory section
- **[High]** Once predictions are available, collect clinical trial (ClinicalTrials.gov / ICTRP) and PubMed literature evidence for the top-ranked predicted indication before re-generating this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

