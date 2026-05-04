---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a peripherally-acting μ-opioid receptor agonist, widely used for the symptomatic management of acute and chronic diarrhea.
The TxGNN model predicts it may be effective for **Acute Contagious Conjunctivitis**, yet **no clinical trials** and **no publications** currently support this direction.
The mechanistic link between loperamide's intestinal opioid activity and ocular infection is unsubstantiated, and this prediction is assessed as a probable model false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diarrhea (registry indication data unavailable; based on known pharmacology) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Loperamide is a peripherally-acting μ-opioid receptor agonist that selectively binds to opioid receptors in the intestinal wall, reducing bowel motility, fluid secretion, and increasing anal sphincter tone. Its poor CNS penetration is intentional by design, making it a safe OTC antidiarrheal.

Acute contagious conjunctivitis is caused by bacterial or viral infection of the conjunctival epithelium and is managed primarily with topical antimicrobial or antiviral agents. While ocular tissues do express opioid receptors in small quantities, there is no established pharmacological mechanism by which loperamide's gut-restricted action would confer any antimicrobial, anti-inflammatory, or barrier-protective benefit in the eye.

The mechanistic analysis indicates this prediction most likely originates from co-morbidity associations between intestinal infections and ocular infections embedded within the knowledge graph, rather than a genuine drug–disease pharmacological relationship. This is a probable false positive from the TxGNN model, and no credible scientific rationale supports pursuing this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Product-level registration details (license numbers, product names, dosage forms, approved indications) were not returned in the current data extract. The NPRA regulatory query confirmed **10 registered loperamide products** in Malaysia with active market status. Full product details should be retrieved directly from the NPRA registry portal.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication — acute contagious conjunctivitis — is assessed as a probable model false positive with no supporting clinical trials, no published literature, and no plausible mechanistic link between loperamide's gut-selective opioid pharmacology and ocular infection (Evidence Level L5). Pursuing this direction would not be a productive use of development resources.

**To proceed with any repurposing evaluation, the following is needed:**

- **Retrieve MOA data**: Query DrugBank API (DB00836) to obtain full mechanism of action, pharmacodynamics, and pharmacokinetics data
- **Obtain NPRA product details**: Download Malaysia registry records for all 10 registered products, including licence numbers, approved indications, and dosage forms
- **Parse package insert**: Download and extract key warnings, contraindications, and precautions from the NPRA-approved prescribing information PDF
- **Re-evaluate alternative indications**: The Rank 4 prediction — **Gastroduodenitis** — carries a marginally more plausible mechanistic rationale (gastrointestinal opioid receptors, motility reduction) supported by 1 historical clinical study (PMID [3520142](https://pubmed.ncbi.nlm.nih.gov/3520142/)); this may be a more productive candidate for further screening, though evidence remains insufficient (L4) and warrants a dedicated safety review before advancing
- **Safety flag for Rank 2 (Amebic Dysentery)**: The existing literature explicitly documents loperamide-associated toxic megacolon risk in invasive intestinal infection — this indication should be formally flagged as contraindicated in any regulatory submission

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

