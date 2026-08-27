---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 5
---

# Cabotegravir
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

Using the drug-repurposing evaluation report format specified in the prompt to produce the report from the supplied Evidence Pack.

# Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), used clinically for the treatment and pre-exposure prophylaxis (PrEP) of HIV-1 infection. The TxGNN model predicts a possible association with **Rheumatoid Arthritis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and mechanistic review indicates the score is more likely a knowledge-graph artifact than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (treatment / PrEP) — based on known drug identity; formal NPRA label indication text not yet extracted |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Cabotegravir in this evidence pack. Based on known information, Cabotegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), part of the same pharmacological class as dolutegravir and bictegravir, and its efficacy in HIV-1 treatment and prevention is well established. No anti-inflammatory, anti-TNF, IL-6 pathway, or broader immunomodulatory mechanism has been reported for this drug class that would plausibly explain an effect on rheumatoid arthritis.

Rheumatoid arthritis is a chronic autoimmune/inflammatory joint disease driven by cytokine pathways (TNF-α, IL-6, JAK-STAT) that are mechanistically unrelated to viral integrase inhibition. The high TxGNN score most likely reflects indirect graph connections — for example, shared nodes around HIV-associated immune activation or autoimmune comorbidities in the underlying knowledge graph — rather than a direct pharmacological relationship between the drug and the disease.

Given the complete absence of supporting clinical trials or literature (0/0), and no plausible biological rationale, this prediction should be treated as an unconfirmed model output rather than an actionable repurposing lead at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Cabotegravir holds **2 active registrations** in Malaysia (NPRA status: 已上市 / Marketed). However, the detailed registration fields (authorization number, product name, dosage form, and approved indication text) could not be extracted from the current data source and require follow-up retrieval from the NPRA product registry before they can be reported here.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Extraction of the NPRA/TFDA label warnings and contraindications for Cabotegravir is currently blocked (see data gap below) and could not be completed for this evaluation.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid arthritis) — along with all other top-5 TxGNN predictions for this drug — has no clinical trial or literature support and no plausible mechanistic link to integrase inhibition; the repurposing rationale itself flags these as likely knowledge-graph noise rather than genuine signals. In addition, a **Blocking** data gap (missing NPRA/TFDA label warnings and contraindications) currently prevents even a baseline safety review, so this candidate cannot proceed regardless of the efficacy signal strength.

**To proceed, the following is needed:**
- NPRA/TFDA product label (warnings, contraindications) — required to clear the Blocking data gap (DG001) before any safety evaluation
- Detailed mechanism of action data from DrugBank — required to resolve the High-severity data gap (DG002) and support mechanistic review
- Complete NPRA registration details (license numbers, product names, dosage forms, approved indication text) for the 2 existing Malaysia registrations
- If the rheumatoid arthritis hypothesis is pursued further: preclinical or mechanistic evidence establishing a plausible immunomodulatory pathway, followed by a renewed search for clinical trials and literature
- Given that none of the top 5 TxGNN-predicted indications for this drug show mechanistic plausibility or evidentiary support, consider re-evaluating this candidate's priority or revisiting the underlying model output before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

