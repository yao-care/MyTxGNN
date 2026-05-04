---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety/Seizure Disorders to Insomnia

## One-Sentence Summary

Diazepam is a classic benzodiazepine, widely used for the treatment of anxiety disorders, muscle spasms, seizures, and alcohol withdrawal since its introduction as Valium® in 1963. The TxGNN model predicts it may be effective for **Insomnia (disease)**, with **24 clinical trials** and **18 publications** currently supporting this direction. Given diazepam's well-established GABA-A receptor-enhancing sedative-hypnotic mechanism, this prediction is pharmacologically intuitive, though its long half-life raises clinical suitability concerns.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorders, muscle spasms, seizures, alcohol withdrawal (specific approved indication text not available in dataset) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.99% (Rank #13) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diazepam acts as a positive allosteric modulator of the GABA-A receptor, binding to the benzodiazepine site and enhancing the inhibitory effect of gamma-aminobutyric acid (GABA) — the main inhibitory neurotransmitter in the central nervous system. This results in reduced neuronal excitability, producing anxiolytic, anticonvulsant, muscle relaxant, and **sedative-hypnotic** effects. The sedative-hypnotic property is directly relevant to insomnia treatment.

The relationship between diazepam's established indications (anxiety, seizures) and insomnia is pharmacologically straightforward: insomnia frequently co-occurs with anxiety, and the same GABAergic enhancement that reduces anxiety also promotes sleep onset and maintenance. In fact, benzodiazepines as a drug class have been used for insomnia treatment for decades. Diazepam specifically has been compared against newer hypnotics in RCTs (e.g., PMID 6113175, lormetazepam vs. diazepam in 100 insomnia patients), and is frequently used as a positive control in preclinical insomnia studies.

However, a critical caveat exists: diazepam's long half-life (20–100 hours for the parent compound, with the active metabolite desmethyldiazepam reaching up to 200 hours) makes it suboptimal for primary insomnia treatment compared to shorter-acting benzodiazepines (e.g., triazolam, temazepam) or non-benzodiazepine hypnotics (e.g., zolpidem). Residual daytime sedation, psychomotor impairment, and cognitive decline with long-term use (PMID 35228700) are significant concerns. This explains why current guidelines generally prefer shorter-acting agents for insomnia despite the mechanistic soundness of the prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, not recruiting | 260 | Evaluates blinded hypnotic tapering + CBTI for enhancing hypnotic discontinuation rates, indirectly addressing diazepam's role in insomnia management |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Placebo-controlled double-blind multicenter study investigating Ramelteon combination use for dose reduction of BZD/non-BZD hypnotics in chronic insomnia |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort assessing risk/benefit of hypnotic agents (including BZD) for sleep disorders among elderly in Taiwan |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Examined role of tapering pace and patient traits on hypnotic (BZD/BZRA) discontinuation in insomnia sufferers |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | RCT evaluating ACT psychotherapy for optimal BZD withdrawal in hypnotic-dependent insomnia patients |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel mechanism for helping older adults discontinue use of sleeping pills (including BZD hypnotics) |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Phase 1 | Completed | 12 | Investigated selective GABA modulator AZD7325 as potential successor to diazepam for insomnia/anxiety with fewer side effects |
| [NCT07417813](https://clinicaltrials.gov/study/NCT07417813) | N/A | Recruiting | 121 | Observational study of lemborexant (dual orexin receptor antagonist) for insomnia in psychiatric disorder patients — a newer mechanism alternative to BZD |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | N/A | Completed | 131 | Prospective RCT comparing remimazolam vs. propofol + midazolam for general anaesthesia; sedative-hypnotic BZD mechanism evaluation |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Evaluating Adepsique® (amitriptyline + perphenazine + diazepam combination) for chronic tinnitus; includes diazepam as component |

> **Note:** Most trials study BZD tapering/discontinuation in insomnia patients rather than directly evaluating diazepam as an insomnia treatment, reflecting the current clinical trend of moving away from long-acting BZDs for sleep.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Lormetazepam 1 mg vs. diazepam 5 mg in 100 insomnia patients; lormetazepam significantly superior in reducing sleep onset time and improving sleep quality |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorg Chem | Comprehensive review of GABA-A receptor modulators; diazepam as classic PAM for epilepsy, anxiety, insomnia, with noted sedation/tolerance side effects |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Animal study | Nat Neurosci | Long-term diazepam enhances microglial spine engulfment via TSPO, impairing cognitive performance — key safety concern for chronic insomnia use |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clinical evidence | Cell Mol Biol Lett | Long-term BZD (including diazepam) and Z-drug use for insomnia exacerbates breast cancer risk — important long-term safety signal |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharm | Meta-analysis of tranquilization therapy in elderly patients; evaluates dose, outcomes, and adverse effects across tranquilizer types |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Review of triazolam's hypnotic properties, noting shorter half-life advantage over diazepam, nitrazepam, flurazepam for insomnia |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Systematic Review | Front Pharmacol | Suanzaoren formulae for insomnia; diazepam used as positive comparator in multiple RCTs, confirming its recognized hypnotic activity |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Animal study | Food Funct | Goat/cow milk effects on insomnia mouse model; diazepam (DZP) served as positive control, validating its sedative-hypnotic benchmark status |
| [40347763](https://pubmed.ncbi.nlm.nih.gov/40347763/) | 2025 | Animal study | J Pharm Biomed Anal | Yiyin Anshen Granule sedative-hypnotic effects with diazepam as standard positive control in PCPA-induced insomnia model |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Animal study | Zhongguo Zhongyao Zazhi | Ziziphi Spinosae Semen extracts on CUMS-induced insomnia; diazepam 2 mg/kg as positive control group |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Data unavailable) | — | — | Detailed registration data not available in the current dataset |

> **Note:** Diazepam has 8 registered licenses in Malaysia with marketed status confirmed. Specific product names, dosage forms, and authorized indications require retrieval from the NPRA database.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Important general considerations for diazepam (based on established drug class knowledge):**
> - **Dependence and withdrawal risk**: Benzodiazepines carry significant risk of physical and psychological dependence, particularly with prolonged use for insomnia
> - **Cognitive impairment**: Long-term use associated with microglial-mediated dendritic spine engulfment and cognitive decline (PMID 35228700)
> - **Daytime sedation**: Long half-life (parent + active metabolites up to 200 hours) causes residual next-day impairment
> - **Fall risk in elderly**: Increased risk of falls and fractures, especially in older adults
> - **Respiratory depression**: Risk when combined with opioids, alcohol, or other CNS depressants

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of diazepam for insomnia is pharmacologically sound — GABA-A receptor enhancement is the core mechanism shared by most classical sedative-hypnotics. The prediction essentially validates diazepam's well-recognized but off-label sedative-hypnotic activity. One published RCT (PMID 6113175) directly tested diazepam in insomnia patients, and diazepam is routinely used as a positive control in preclinical insomnia studies. However, current clinical guidelines do **not** recommend diazepam as a first-line insomnia treatment due to its long half-life, accumulation risk, dependence liability, and cognitive impairment with chronic use. Shorter-acting alternatives (temazepam, zolpidem) or dual orexin receptor antagonists (lemborexant, suvorexant) are preferred.

**To proceed, the following is needed:**
- Retrieve complete NPRA registration data (product names, dosage forms, approved indications)
- Obtain detailed mechanism of action (MOA) data from DrugBank (DrugBank ID mapping)
- Retrieve package insert safety data (key warnings, contraindications, drug interactions)
- Comparative benefit-risk analysis against current first-line insomnia therapies available in Malaysia
- Assessment of route compatibility (oral, injectable formulations available vs. required)
- Regulatory pathway review for potential label expansion in Malaysia (if not already indicated for insomnia)

---

## Additional Predicted Indications Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Link |
|------|---------|-------------|----------------|----------------|------------------|
| 1 | Insomnia | 99.99% | L2 | Proceed with Guardrails | Strong — GABA-A sedative-hypnotic effect |
| 2 | Cauda equina syndrome | 99.99% | L5 | Hold | Weak — muscle relaxant only; cannot address structural compression |
| 3 | Alcohol withdrawal delirium | 99.98% | L1 | Proceed with Guardrails | Strong (core indication) — cross-tolerance with ethanol; first-line treatment |
| 4 | Sleep disorder (initiating/maintaining) | 99.97% | L5 | Hold | Strong mechanism but no evidence; long half-life problematic |
| 5 | Anxiety | 99.97% | L1 | Proceed with Guardrails | Core indication — original design target since Valium® (1963) |
| 6 | ADHD, inattentive type | 99.97% | L5 | Hold | Adverse — GABAergic sedation worsens attention/cognition |
| 7 | Antidepressant type abuse | 99.95% | L4 | Hold | Paradoxical — BZD itself has abuse potential |
| 8 | Barbiturate abuse | 99.95% | L4 | Research Question | Partial — cross-tolerance for harm reduction, not treatment |
| 9 | Hallucinogen abuse | 99.95% | L4 | Research Question | Indirect — acute agitation management only |
| 10 | Specific developmental disorder | 99.95% | L5 | Hold | Weak/harmful — may disrupt neurodevelopment |

> **Key Insight:** Indications #3 (alcohol withdrawal delirium) and #5 (anxiety) are effectively **validated core indications** for diazepam, demonstrating the TxGNN model's ability to correctly identify established drug-disease relationships. Indication #1 (insomnia) represents a mechanistically sound but clinically nuanced repurposing candidate where drug selection within the BZD class matters significantly.

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

