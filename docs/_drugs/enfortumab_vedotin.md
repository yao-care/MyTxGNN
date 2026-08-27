---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Enfortumab Vedotin: From Bladder Cancer (Nectin-4-Targeted ADC) to Leprosy

*Note: `taiwan_regulatory.licenses[].approved_indication_text` and `drug.original_indications` are empty in this evidence pack (data gap). "Bladder cancer" above is inferred from within-pack evidence — the literature entry and repurposing rationale repeatedly describe this drug as a Nectin-4-targeted ADC studied in bladder cancer — not from an external/registry source.*

## One-Sentence Summary

Enfortumab vedotin is an antibody-drug conjugate (ADC) targeting Nectin-4, delivering the microtubule inhibitor MMAE as its payload, used in the context of bladder cancer per the available literature reference. The TxGNN model's top prediction for repurposing is **Leprosy**, but the accompanying rationale explicitly states there is **no mechanistic link** between this ADC's cytotoxic mechanism and anti-leprosy treatment, and **0 clinical trials and 0 publications** support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in registry data (data gap); contextually associated with bladder cancer per in-pack literature |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action documentation is not available (`original_moa` is a flagged data gap, severity High). What can be established from the evidence pack itself is that enfortumab vedotin is an antibody-drug conjugate combining a Nectin-4-targeting antibody with MMAE (monomethyl auristatin E), a microtubule-polymerization inhibitor, delivering targeted cytotoxicity to Nectin-4-expressing tumour cells.

For the top-ranked prediction, **leprosy**, the model-generated rationale is explicit and negative: it states there is no known mechanistic relationship — the ADC's cytotoxic, anti-microtubule mode of action has no established role in treating mycobacterial infection, and Nectin-4 is not a recognized anti-leprosy drug target. This is corroborated by an empty evidence base (zero clinical trials, zero ICTRP trials, zero literature).

Reviewing the full ranked list reinforces this concern rather than resolving it: several other top-9 candidates (multiple endocrine neoplasia, cytomegalovirus infection, cerebral infarction, HIV, homozygous familial hypercholesterolemia) similarly have no mechanistic rationale and no evidence, and two candidates (infectious bovine rhinotracheitis, malignant catarrhal fever) are **veterinary, non-human diseases** with identical TxGNN scores — a pattern suggesting knowledge-graph ontology cross-contamination or embedding-space noise near this drug's node, rather than a genuine biological signal. The only candidate with any literature (candidiasis, rank 4) is supported by a single real-world pharmacovigilance (FAERS) study describing candidiasis as an **adverse-event signal** from ADC-related immunosuppression — not therapeutic evidence — and is itself explicitly flagged in the pack as a likely false positive from a "drug–adverse event–disease" co-occurrence pattern rather than a repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*(For context: across the full set of 9 top-ranked TxGNN candidates, only one — candidiasis, rank 4 — has any associated literature, and it is a pharmacovigilance safety-signal study, not efficacy evidence. See "Why is This Prediction Reasonable?" above.)*

## Malaysia Market Information

The evidence pack confirms the drug is marketed in Malaysia with 2 active registrations (NPRA), but license number, product name, dosage form, manufacturer, and approved-indication-text fields are all empty in this pack — detailed registration data is a gap requiring direct NPRA lookup.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC) with a cytotoxic microtubule-inhibitor payload (MMAE) directed at Nectin-4 |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this pack; retrieving the NPRA/manufacturer label is a blocking gap for any safety evaluation.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 9 top-ranked TxGNN predictions for this drug carry an "Hold" recommendation and L4–L5 evidence at best. The top candidate (leprosy) has an explicit no-mechanistic-link assessment and zero supporting studies; the ranked list additionally contains two veterinary/non-human disease entries, indicating likely knowledge-graph noise rather than a credible repurposing signal.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA label warnings and contraindications (blocking gap, DG001) before any safety-side evaluation can start
- Obtain a sourced mechanism-of-action document from DrugBank (DG002)
- Investigate the apparent knowledge-graph ontology contamination causing veterinary-disease predictions to rank alongside human indications, as this affects confidence in the entire candidate list for this drug
- If any candidate is pursued further, prioritize one with an actual mechanistic rationale and real evidence base — none of the current top 9 meet that bar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

