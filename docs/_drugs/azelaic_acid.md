---
layout: default
title: Azelaic Acid
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 0
---

# Azelaic Acid
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

# Azelaic Acid: Dermatological Agent — No New Indication Predicted

## One-Sentence Summary

Azelaic Acid is a naturally occurring dicarboxylic acid commonly used in dermatology for the treatment of acne vulgaris and rosacea. The TxGNN model **did not generate any repurposing predictions** for this drug, meaning there are currently no computationally suggested new indications. Further data enrichment (mechanism of action, regulatory details) is needed before re-evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatological use (acne, rosacea — based on known pharmacology; specific approved indication text not available in dataset) |
| Predicted New Indication | **None** — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | **N/A** — no prediction to evaluate |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | **Hold** |

---

## Why Was No Prediction Generated?

Azelaic Acid (DrugBank ID: DB00548) is a dicarboxylic acid with known antibacterial, keratolytic, anti-inflammatory, and tyrosinase-inhibiting properties. It is primarily used as a topical agent for acne vulgaris, rosacea, and hyperpigmentation disorders.

The TxGNN model did not produce any repurposing candidates for this drug. Several factors may explain this:

1. **Topical-only use profile**: Azelaic Acid is predominantly used topically, which limits its systemic pharmacological interactions captured by the knowledge graph. TxGNN's drug–disease relationship network may not adequately represent topical-route-specific therapeutic effects.

2. **Missing mechanism of action data**: The MOA field is absent from the current dataset. Without explicit target–pathway annotations in the knowledge graph, the model's ability to infer novel disease associations is reduced.

3. **Limited knowledge graph connectivity**: If Azelaic Acid has few edges (drug–target, drug–disease, drug–drug) in the underlying knowledge graph, the graph neural network has insufficient signal to generate high-confidence predictions.

---

## Clinical Trial Evidence

No predicted indication exists; therefore, no targeted clinical trial search was performed.

---

## Literature Evidence

No predicted indication exists; therefore, no targeted literature search was performed.

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| *(Not available in dataset)* | *(Not available)* | *(Not available)* | *(Not available)* |

> **Note:** The NPRA query confirmed 2 registrations for Azelaic Acid in Malaysia, but detailed license information (authorization numbers, product names, dosage forms, approved indications) was not captured in the current dataset. Please consult the [NPRA Product Search](https://quest3plus.bpfk.gov.my/pmo/index.php) for complete registration details.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current dataset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not generate any repurposing predictions for Azelaic Acid. Without a candidate indication, there is no actionable repurposing hypothesis to evaluate at this time.

**To proceed, the following is needed:**

- **Mechanism of action (MOA) data** — Query DrugBank API to obtain target and pathway annotations, which will enrich Azelaic Acid's representation in the knowledge graph
- **Complete Malaysia regulatory details** — Retrieve full NPRA license information including product names, dosage forms, and approved indication text
- **Package insert safety data** — Obtain key warnings, contraindications, and precautions from the approved product labelling
- **Knowledge graph connectivity check** — Verify that Azelaic Acid (DB00548) exists as a node in the TxGNN knowledge graph (`data/kg.csv`) and assess its edge count; if absent or poorly connected, the drug cannot be effectively evaluated by the model
- **Re-run TxGNN prediction** after data enrichment to determine if new indications emerge

---

*This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

