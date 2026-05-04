---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Apixaban: From Thromboembolic Prevention to Migraine Disorder

## One-Sentence Summary

Apixaban is a direct oral anticoagulant (Factor Xa inhibitor) approved in Malaysia for the prevention of stroke and systemic embolism in patients with atrial fibrillation, as well as treatment and prevention of deep vein thrombosis (DVT) and pulmonary embolism (PE).
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **1 clinical trial** and **4 publications** currently available — though the evidence is indirect and in some cases argues against Apixaban specifically.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Stroke/embolism prevention; DVT/PE treatment (licensed indication detail not retrieved in this data pull) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 25 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Apixaban is a selective, direct inhibitor of coagulation Factor Xa, blocking the conversion of prothrombin to thrombin and thereby suppressing clot formation. Although its approved use centres on thromboembolic conditions, the hypothesised link to migraine rests on three overlapping mechanisms: (1) **thrombin modulation** — thrombin has been proposed to facilitate cortical spreading depression (CSD), the electrophysiological substrate of migraine aura; (2) **PFO-mediated microembolism** — closure of a patent foramen ovale (PFO) has been associated with migraine reduction, and anticoagulation is one management strategy for cryptogenic stroke in PFO patients; (3) **antiphospholipid antibody syndrome (APS)** — patients with aPL positivity and refractory migraine appear to benefit from antithrombotic therapy.

However, the mechanistic case for Apixaban *specifically* is substantially weakened by the existing clinical literature. A directly relevant case report (PMID 28960288) documents a patient whose migraine with aura remitted completely on warfarin but returned within three weeks of switching to apixaban, resolving again only after warfarin was resumed. This suggests that the anti-migraine effect may depend on warfarin's broader pharmacological actions — including effects on Protein C/S and other vitamin K-dependent pathways — rather than Factor Xa inhibition alone.

Therefore, while the anticoagulant drug class carries biologically plausible associations with migraine, the translation of that signal to Apixaban as a class representative is not currently supported by direct positive evidence, and at least one head-to-head clinical observation actively contradicts this extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compares PFO closure vs. anticoagulants vs. antiplatelet therapy for secondary stroke prevention. Primary endpoint is stroke recurrence, **not migraine**. Anticoagulant used was not specified as Apixaban. Any migraine-related benefit would be incidental to PFO management. Relevance to Apixaban-specific migraine treatment is low (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Small Prospective Trial | *Lupus* | 75 patients with aPL antibodies and refractory migraine trialled antithrombotic therapy; a subset showed symptomatic improvement. Suggests anticoagulation may benefit a specific aPL-positive migraine subgroup, but Apixaban is not specifically evaluated. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | Reviews impact of DOACs on headache/migraine frequency and severity. Notes the literature is scarce and controversial; the role of Apixaban specifically is unclear. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | **Critical negative signal**: A 55-year-old woman had complete migraine with aura remission for 12 years on warfarin; symptoms returned within 3 weeks of switching to apixaban and resolved again upon resuming warfarin. Suggests Factor Xa inhibition alone is insufficient to replicate warfarin's anti-migraine effect. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolved with warfarin plus topiramate. No direct involvement of Apixaban; further supports the warfarin-specific rather than class-wide anticoagulation hypothesis. |

---

## Malaysia Market Information

Twenty-five product registrations for Apixaban are recorded with Malaysia's NPRA. Detailed product-level data (authorization numbers, brand names, dosage forms, and approved indication text) was not retrieved in this data pull and should be verified directly via the NPRA Product Registration database.

> **Action Required**: Retrieve full licence details from [NPRA Product Registration](https://www.npra.gov.my) to populate this table before regulatory submission or formulary review.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug-drug interactions) was not retrieved in this data pull.

> Please refer to the Apixaban package insert (e.g., Eliquis® prescribing information) for full safety information, including haemorrhagic risk, drug interactions (especially with strong CYP3A4/P-gp inhibitors), and contraindications in patients with active clinically significant bleeding or severe hepatic impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.02%), the available evidence does not support Apixaban as an effective treatment for migraine disorder. The only directly relevant clinical observation (PMID 28960288) demonstrates that the migraine-suppressing effect seen with warfarin was *not* reproduced by Apixaban, indicating a drug-specific rather than class-wide mechanism. The remaining literature is confined to low-tier case reports and one small retrospective study in an aPL-positive subgroup. Current evidence is insufficient to advance this candidate to the next screening stage.

**To proceed, the following is needed:**

- **Mechanism clarification**: Obtain full MOA data from DrugBank (DG002) to determine whether any Apixaban-specific pathway could plausibly modulate CSD or migraine pathophysiology independently of warfarin's vitamin K-dependent effects.
- **Safety profile**: Download and parse the TFDA/NPRA package insert PDF to complete the safety assessment (DG001 — currently Blocking for S1 safety screening).
- **Malaysia licence details**: Retrieve full NPRA registration data to confirm marketed formulations and approved indications.
- **Subgroup hypothesis**: If pursuing this indication further, focus on the aPL-positive refractory migraine subgroup (PMID 33402037) rather than unselected migraine, as this is the mechanistically coherent population for anticoagulant intervention.
- **Prospective clinical data**: A dedicated Phase 2 RCT comparing Apixaban to warfarin and placebo in aPL-positive migraine patients would be required to resolve the current uncertainty before any L2-level evidence can be claimed.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

