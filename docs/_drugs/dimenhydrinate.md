---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Dimenhydrinate: From Motion Sickness/Antiemetic to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is a first-generation antihistamine widely used for the prevention and treatment of motion sickness, nausea, and vomiting. The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **1 pharmacokinetic publication** currently supporting this direction but **no clinical trials** registered. Notably, the drug's active moiety — diphenhydramine — is already clinically used for urticaria, making this a formulation-level repurposing rather than a novel mechanistic hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness, nausea, vomiting (licence detail pending) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (Preclinical / mechanism-level studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dimenhydrinate is a 1:1 salt combination of **diphenhydramine** (a first-generation H1 receptor antagonist) and **8-chlorotheophylline** (a mild stimulant added to counteract drowsiness). After oral administration, it dissociates to release diphenhydramine as the pharmacologically active moiety. Diphenhydramine competitively blocks histamine H1 receptors on vascular endothelial cells, smooth muscle, and sensory nerve endings.

Allergic urticaria is driven by mast cell degranulation, which releases histamine that acts on H1 receptors to cause vasodilation, increased vascular permeability, pruritus, and wheal formation. H1 receptor antagonism directly interrupts this pathological cascade and is the pharmacological basis for first-line urticaria treatment. Indeed, diphenhydramine (marketed as Benadryl) is already widely used off-label and on-label for acute urticaria across many markets.

The key distinction here is that **dimenhydrinate as a specific formulation** has not been approved with an urticaria indication — its regulatory labels are limited to motion sickness and antiemetic use. However, since the active component is identical to a drug already proven effective in urticaria, this prediction reflects a **formulation-level repurposing opportunity** with a strong mechanistic rationale. Current treatment guidelines favour second-generation antihistamines (e.g. cetirizine, loratadine) due to fewer sedative side effects, which would position dimenhydrinate as a potential rescue or acute-care option rather than maintenance therapy.

---

## Clinical Trial Evidence

Currently no clinical trials registered for dimenhydrinate in allergic urticaria on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic Study | Veterinary Dermatology | Compared diphenhydramine PK after oral/IV diphenhydramine and oral dimenhydrinate in dogs. Found dimenhydrinate may produce superior oral absorption of diphenhydramine. Assessed pharmacodynamic effect on histamine-induced wheal formation, confirming anti-wheal activity relevant to urticaria pathophysiology. |

---

## Malaysia Market Information

Dimenhydrinate has **15 active registrations** in Malaysia. However, detailed licence information (registration numbers, product names, dosage forms, and approved indication text) was not available in the current data extraction. Further details should be obtained from the NPRA database.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** The following data gaps have been identified and should be resolved before proceeding:
> - **Package insert warnings and contraindications** — Source: NPRA / TFDA official website (Severity: Blocking)
> - **Detailed mechanism of action (MOA)** — Source: DrugBank API (Severity: High)
>
> **General considerations for first-generation H1 antihistamines** (based on class-level knowledge):
> - **CNS depression**: Drowsiness, sedation, impaired psychomotor performance
> - **Anticholinergic effects**: Dry mouth, urinary retention, blurred vision, constipation
> - **Use caution in**: Elderly patients, patients with glaucoma, prostatic hyperplasia, or asthma
> - **Drug interactions**: Additive CNS depression with alcohol, benzodiazepines, opioids, and other sedating medications

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between dimenhydrinate (via its active moiety diphenhydramine) and allergic urticaria is well-established — H1 receptor antagonism directly addresses the core histamine-mediated pathology. While no clinical trials specifically test dimenhydrinate for urticaria, the active ingredient diphenhydramine is already a recognised treatment. The main barrier is regulatory (formulation-specific indication) rather than scientific.

**To proceed, the following is needed:**
- **Resolve safety data gaps**: Obtain full package insert warnings and contraindications from the NPRA database (currently blocking S1 safety assessment)
- **Head-to-head positioning analysis**: Compare dimenhydrinate against second-generation antihistamines (cetirizine, loratadine) for urticaria to define its clinical niche (e.g. acute/rescue setting vs. maintenance)
- **Formulation & dose evaluation**: Determine whether existing marketed dosage forms and strengths are appropriate for urticaria dosing regimens
- **Regulatory pathway assessment**: Evaluate whether a label extension for an existing registration or a new submission is more feasible in the Malaysian context
- **Clinical evidence generation**: Consider a pilot pharmacodynamic study (wheal-and-flare suppression) in human subjects to support the repurposing application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

