---
layout: default
title: Lidocaine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 0
---

# Lidocaine Hydrochloride
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

# Lidocaine Hydrochloride: From Local Anesthesia/Antiarrhythmia — No Active Repurposing Prediction Available

## One-Sentence Summary

Lidocaine Hydrochloride is a well-established voltage-gated sodium channel blocker, widely used as a local anesthetic and antiarrhythmic agent across numerous clinical settings.
The current Evidence Pack contains **no TxGNN-generated repurposing predictions** for this compound, likely due to upstream data gaps in the processing pipeline.
With 19 registered products in Malaysia and zero predicted indications on record, this candidate requires pipeline remediation before a formal repurposing assessment can be conducted.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia; ventricular arrhythmia (based on established clinical knowledge; no approved indication text retrieved) |
| Predicted New Indication | N/A — no predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only; no actual studies linked) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

---

## Background: What Is This Drug?

Although no TxGNN prediction is available, the following context is provided for completeness.

Lidocaine Hydrochloride belongs to the Class Ib antiarrhythmic and aminoethylamide local anesthetic families. Its primary mechanism involves **blocking voltage-gated sodium channels (Nav1.x)**, thereby inhibiting the initiation and propagation of action potentials in excitable tissues including neurons and cardiomyocytes. This dual action underpins its widespread use in:

- **Local/regional anesthesia**: infiltration, nerve block, epidural, and topical anesthesia
- **Antiarrhythmia**: acute management of ventricular tachycardia and ventricular fibrillation

The sodium channel blocking mechanism has historically been explored in additional therapeutic contexts — including neuropathic pain, certain inflammatory conditions, and perioperative analgesia — making it a pharmacologically interesting repurposing candidate in principle. However, **this report cannot proceed with a formal repurposing analysis** because the TxGNN prediction pipeline returned no scored indications for this drug.

---

## Malaysia Market Information

The Malaysia NPRA database returned **19 registered products** for Lidocaine Hydrochloride. However, the current Evidence Pack did not retrieve individual registration details (authorization numbers, product names, dosage forms, or approved indication text) for any of the 19 entries. A follow-up query against the NPRA database is required to populate this table.

> **Note:** 19 active registrations confirm substantial market presence. Lidocaine products are expected to include injectable solutions (1%/2%), topical gels/sprays, and combination preparations.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The current Evidence Pack contains no retrieved warnings, contraindications, or drug–drug interaction data. Key areas to investigate prior to any repurposing study include: cardiovascular toxicity (bradycardia, hypotension, heart block), CNS toxicity (seizures, confusion), hypersensitivity reactions, and interactions with other antiarrhythmics or CYP1A2/CYP3A4 substrates.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline returned zero repurposing candidates for Lidocaine Hydrochloride, and critical upstream data — including the DrugBank ID, MOA details, approved indication text, and safety warnings — are absent. Without a scored prediction and complete drug profile, a repurposing evaluation cannot be formally initiated.

**To proceed, the following is needed:**

- **Resolve DrugBank ID** — Query DrugBank by INN "lidocaine" to retrieve the canonical `DB00281` record and populate MOA, categories, and toxicity data
- **Retrieve NPRA license details** — Re-query NPRA for all 19 registration records to obtain authorization numbers, dosage forms, and approved indication text
- **Retrieve TFDA package insert** — Download and parse the PDF to extract warnings, contraindications, and dosage information (Data Gap DG001)
- **Re-run TxGNN prediction pipeline** — Once drug mapping is confirmed (DrugBank ID resolved), re-execute the KG and DL prediction steps to generate scored repurposing candidates
- **Verify input data integrity** — Check whether the empty `original_indications` array caused the prediction pipeline to skip this compound entirely, and correct the upstream loader if so
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

