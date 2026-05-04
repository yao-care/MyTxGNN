---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dextromethorphan: From Cough Suppression to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan (DXM) is a widely used antitussive (cough suppressant) with NMDA receptor antagonist and sigma-1 receptor agonist properties. The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **1 clinical trial** currently listed, though direct evidence for this specific indication remains limited. No relevant publications were identified at the time of data cutoff.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough suppression (antitussive) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 45 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, dextromethorphan is a multitarget drug primarily used as a cough suppressant. Its key pharmacological actions include **NMDA receptor antagonism**, **sigma-1 receptor agonism**, and **serotonin reuptake inhibition**. These diverse receptor activities give DXM a broader pharmacological profile than a typical antitussive agent.

DXM has been widely used for upper respiratory symptom relief, particularly cough suppression associated with colds and upper airway irritation. Nasal cavity disease—encompassing conditions affecting the nasal passages such as mucosal inflammation and congestion—shares anatomical and pathophysiological overlap with upper respiratory conditions where DXM is already clinically employed. The sigma-1 receptor agonist activity of DXM may confer anti-inflammatory effects that could help modulate nasal mucosal inflammation. Additionally, NMDA receptor antagonism may regulate neurogenic inflammation in the nasal cavity, a mechanism implicated in chronic rhinosinusitis and other nasal inflammatory conditions.

The prediction is mechanistically plausible given DXM's established role in upper respiratory care, its potential anti-inflammatory properties through sigma-1 receptors, and the anatomical proximity of its traditional therapeutic targets to the nasal cavity. Furthermore, DXM is increasingly being investigated for indications beyond cough suppression (e.g., the DXM/bupropion combination for major depressive disorder), demonstrating that its pharmacological versatility extends well beyond its original antitussive use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter, randomized, double-blind, placebo-controlled trial evaluating DXM/bupropion sustained-release tablets in Chinese adult patients with major depressive disorder (MDD). |

> **Note:** The listed clinical trial investigates dextromethorphan in combination with bupropion for major depressive disorder, not nasal cavity disease directly. Its relevance to the predicted indication is indirect—it reflects the expanding clinical investigation of DXM beyond its traditional antitussive role, but does not constitute direct evidence for nasal cavity disease.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

Dextromethorphan has **45 registered products** in Malaysia with a market status of **Marketed**. Detailed individual license information (authorization numbers, product names, dosage forms, and approved indications) was not available in the evidence pack at the time of this report.

> Detailed registration records should be obtained from NPRA (National Pharmaceutical Regulatory Agency) for a complete regulatory assessment.

---

## Safety Considerations

> Please refer to the package insert for safety information.

---

## Additional Predicted Indications

Beyond the primary prediction, the TxGNN model also identified the following candidate indications for dextromethorphan:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 2 | Acute Laryngopharyngitis | 99.98% | L4 | Hold |
| 3 | Faucial Diphtheria | 99.36% | L5 | Hold |
| 4 | Trigeminal Autonomic Cephalalgia | 99.32% | L5 | Research Question |
| 5 | Cervical Disc Degenerative Disorder | 99.30% | L5 | Research Question |
| 6 | Allergic Urticaria | 99.25% | L5 | Hold |

**Key observations:**
- **Acute laryngopharyngitis** (Rank 2) is closely related to DXM's established upper respiratory use, though no clinical trials or literature were found for this specific indication.
- **Trigeminal autonomic cephalalgia** and **cervical disc degenerative disorder** (Ranks 4–5) represent pain-related indications where DXM's NMDA antagonism may have mechanistic relevance. NMDA receptor antagonists (e.g., ketamine) have documented roles in chronic pain and headache management.
- **Faucial diphtheria** (Rank 3) and **allergic urticaria** (Rank 6) have weak mechanistic links to DXM's known pharmacological targets and are recommended for hold.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dextromethorphan has a well-established safety profile with extensive market availability (45 registrations in Malaysia). The mechanistic rationale linking its sigma-1 and NMDA receptor activities to nasal mucosal inflammation is plausible, and its longstanding use in upper respiratory symptom management provides a clinical foundation. However, direct clinical evidence for nasal cavity disease is absent, warranting a cautious approach.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data from DrugBank (current data gap DG002)
- NPRA package insert review for safety warnings and contraindications (current data gap DG001)
- Expanded literature search using related terms (rhinitis, nasal inflammation, sinonasal disease, chronic rhinosinusitis)
- Identification of preclinical or pilot studies targeting nasal cavity inflammatory conditions with NMDA antagonists or sigma-1 agonists
- Drug-drug interaction profiling for commonly co-administered nasal/respiratory medications (e.g., intranasal corticosteroids, antihistamines)
- Assessment of appropriate dosage form and route of administration for nasal cavity disease (oral vs. topical nasal delivery)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

