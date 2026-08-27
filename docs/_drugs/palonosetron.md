---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 530
evidence_level: L5
indication_count: 5
---

# Palonosetron
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

# Palonosetron: From Antiemetic (CINV/PONV) to Migraine Disorder

## One-Sentence Summary

Palonosetron is a selective 5-HT3 receptor antagonist originally used as an antiemetic for chemotherapy-induced and postoperative nausea and vomiting (CINV/PONV). The TxGNN model predicts it may be effective for **Migraine Disorder**, but the only literature currently available is a case report describing palonosetron *inducing* migraine-type headache as an adverse reaction — evidence that points against, not toward, the treatment hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced and postoperative nausea/vomiting (CINV/PONV) — based on known drug class; NPRA label text not available in current dataset |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap. Based on known pharmacology, palonosetron is a potent, long-acting selective 5-HT3 (serotonin) receptor antagonist, clinically established for preventing chemotherapy- and surgery-induced nausea and vomiting.

The TxGNN link to migraine plausibly reflects the fact that 5-HT3 receptors participate in pain signaling and trigeminovascular system activation — a pathway also implicated in migraine pathophysiology. In theory, this could support a bidirectional relationship (i.e., 5-HT3 blockade modulating migraine).

However, the only retrievable literature (PMID 21132477) points in the opposite direction: it is a case report of palonosetron **inducing** migraine-type headache as an adverse drug reaction, not evidence of therapeutic benefit. So while the mechanistic rationale has theoretical grounding, the sole piece of real-world evidence contradicts the repurposing hypothesis rather than supporting it.

*Note on other candidates:* Four additional TxGNN-ranked indications were reviewed (migraine with brainstem aura, migraine susceptibility, atrophoderma vermiculata, ulerythema ophryogenesis). None have any supporting clinical or case-level evidence, and the 20 "supporting" papers retrieved for the migraine-susceptibility candidate were found on review to be about epilepsy genetics/epileptogenesis — an apparent text-matching artifact, not real drug-disease evidence. All are scored Hold at evidence level L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report | Canadian Journal of Anaesthesia | Case report of palonosetron-induced migraine-type headache — an adverse reaction, not a therapeutic effect |

---

## Malaysia Market Information

NPRA registration data confirms palonosetron is marketed in Malaysia with **8 active registrations**, but detailed fields (license number, product name, dosage form, approved indication text) are not populated in the current dataset and require direct retrieval from NPRA product listings.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are currently unavailable — retrieving the NPRA product label is flagged as a Blocking data gap that must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence for this indication is a single case report describing palonosetron *causing* migraine-type headache — the opposite of the predicted therapeutic effect. Combined with the absence of any clinical trials and a Blocking gap in core safety data (warnings/contraindications), there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- NPRA product label (warnings, contraindications) — resolves DG001 (Blocking)
- DrugBank-confirmed mechanism of action — resolves DG002
- Complete Malaysia license/product detail (name, dosage form, approved indication text)
- Any mechanistic or preclinical study directly testing 5-HT3 antagonism in migraine models, to determine whether the case-report signal is an outlier or a real class effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

