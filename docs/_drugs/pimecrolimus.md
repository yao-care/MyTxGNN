---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus (brand name: Elidel) is a topical calcineurin inhibitor originally developed and approved for the treatment of mild-to-moderate atopic dermatitis (eczema), offering a steroid-sparing anti-inflammatory option particularly suited for sensitive skin areas such as the face and neck.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
with **1 clinical trial** and **18 publications** currently supporting this direction, including 2 systematic reviews and 2 randomised controlled trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atopic Dermatitis (mild to moderate) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pimecrolimus is an ascomycin macrolactam derivative and a selective topical calcineurin inhibitor. Although detailed MOA data is not available from the DrugBank record in this Evidence Pack, published literature consistently describes its mechanism: pimecrolimus binds to macrophilin-12 (FKBP-12), inhibiting calcineurin phosphatase activity and thereby blocking NFAT-mediated transcription of pro-inflammatory cytokines — including IL-2, IL-4, and TNF-α — in T cells and mast cells. Crucially, unlike topical corticosteroids, pimecrolimus does not impair skin barrier function and carries no risk of cutaneous atrophy, making it particularly well-suited for chronic, long-term use on thin facial skin.

The biological rationale for repurposing to seborrheic dermatitis is compelling. Seborrheic dermatitis is now understood to involve a T-cell-mediated inflammatory cascade triggered by abnormal immune responses to the skin commensal yeast *Malassezia*. This Th1/Th2 dysregulation — characterised by elevated IL-2, IL-4, and interferon-γ in the lesional skin — maps directly onto the cytokine targets of pimecrolimus's calcineurin-inhibiting mechanism. Both atopic dermatitis and seborrheic dermatitis share overlapping immunological pathways: chronic skin inflammation mediated by activated T lymphocytes in sebum-rich regions prone to immune dysregulation.

Importantly, the off-label use of pimecrolimus 1% cream for seborrheic dermatitis is already well-documented in the dermatology literature. Multiple independent systematic reviews confirm that pimecrolimus is effective and well-tolerated, with efficacy comparable to topical antifungals (ketoconazole) and superior safety versus topical corticosteroids for long-term facial application. This convergence of mechanistic plausibility and accumulated clinical evidence makes the TxGNN prediction highly credible rather than speculative.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | A 4-week randomised double-blind active-comparator controlled study directly designed to evaluate Elidel (pimecrolimus) for the treatment of seborrheic dermatitis. This is the most directly relevant registered trial for this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review | Cureus | Systematic review of RCTs evaluating the efficacy and safety of pimecrolimus in facial seborrheic dermatitis; reviews calcineurin inhibitors as a key treatment category alongside antifungals and corticosteroids. |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review | Expert Review of Clinical Pharmacology | Systematic review of RCTs of pimecrolimus 1% cream for seborrheic dermatitis vs corticosteroids, antimycotics, and placebo; concludes pimecrolimus is well-tolerated and effective with comparable efficacy to comparators. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | American Journal of Clinical Dermatology | Systematic review of topical treatments for facial seborrheic dermatitis; reviews the role of antifungals, keratolytics, and corticosteroids, with calcineurin inhibitors discussed as an emerging treatment category. |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clinical and Experimental Dermatology | Randomised blinded trial directly comparing pimecrolimus 1% cream vs sertaconazole 2% cream in facial seborrhoeic dermatitis; addresses long-term management of this chronic relapsing condition. |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT | Irish Journal of Medical Science | RCT comparing sertaconazole 2% cream versus pimecrolimus 1% cream in seborrheic dermatitis; provides direct comparative efficacy data for this indication. |
| [23441238](https://pubmed.ncbi.nlm.nih.gov/23441238/) | 2013 | Clinical Study | Journal of Clinical and Aesthetic Dermatology | Review and clinical discussion of topical pimecrolimus 1% as a calcineurin inhibitor alternative for seborrheic dermatitis, particularly for long-term use where topical corticosteroid side effects are a concern. |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-Label Study | American Journal of Clinical Dermatology | Open-label study of pimecrolimus 1% cream in resistant facial seborrheic dermatitis; demonstrates effectiveness and tolerability in cases where standard treatments have failed. |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | International Journal of Clinical Practice | Comprehensive mechanistic review of pimecrolimus in dermatology, covering its selective T-cell and mast-cell targeting and its applications beyond atopic dermatitis, including seborrheic dermatitis. |
| [19255921](https://pubmed.ncbi.nlm.nih.gov/19255921/) | 2009 | Clinical Study | Journal of Dermatological Treatment | Prospective study on pimecrolimus experience in seborrheic dermatitis with close follow-up; documents cure and remission times and side-effect profile, confirming increasing off-label use. |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Clinical Study | Journal of Dermatological Treatment | Open randomised prospective comparative study of topical pimecrolimus 1% cream vs topical ketoconazole 2% cream in seborrheic dermatitis; provides head-to-head efficacy data against the antifungal standard of care. |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | Pimecrolimus (1 registered product) | Topical Cream (1% cream, Elidel class) | Detailed indication text not recorded in current regulatory dataset; registration confirmed active (已上市) |

> **Note:** The Malaysia NPRA query confirmed 1 active registration for pimecrolimus. Detailed product name, license number, and approved indication text require verification directly from the NPRA product database or the registered package insert.

---

## Safety Considerations

Detailed package insert warnings, contraindications, and drug interaction data were not captured in this Evidence Pack. Based on established pharmacology and published literature, the following are clinically relevant safety considerations for pimecrolimus:

- **Black Box Warning (FDA):** Long-term safety of topical calcineurin inhibitors, including pimecrolimus, has not been established. Use should be limited to second-line therapy; long-term continuous use should be avoided. A theoretical risk of malignancy (skin cancer, lymphoma) was identified in post-market surveillance, though a 2023 systematic review and meta-analysis (*Lancet Child & Adolescent Health*, PMID 36370744) found no statistically significant increase in cancer risk.
- **Application Site Reactions:** Burning, stinging, and pruritus at application site are the most common adverse effects, particularly on initial application.
- **Alcohol Flush Reaction:** Concurrent alcohol ingestion may cause transient facial flushing and skin irritation at application sites.
- **Infection Risk:** Pimecrolimus reduces local immune surveillance; caution is warranted in patients with active skin infections, including tinea (risk of tinea incognito with atypical presentation).
- **Contraindications:** Known hypersensitivity to pimecrolimus or any excipient; Netherton's syndrome; generalised erythroderma.

Please verify the complete contraindication list and current warnings in the registered Malaysian package insert (jururawat/SmPC).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The use of pimecrolimus for seborrheic dermatitis is mechanistically well-grounded and supported by multiple systematic reviews, two direct RCTs, and a completed Phase 2 trial (NCT00403559). The calcineurin inhibitor mechanism directly addresses the T-cell-mediated inflammatory pathology of seborrheic dermatitis, and the drug's established safety advantage over topical corticosteroids (no skin atrophy, suitable for long-term facial use) represents a clinically meaningful advantage for this chronic, recurrent condition affecting the face and scalp.

**To proceed, the following is needed:**

- **Confirm Malaysia registered indication:** Retrieve the approved indication text from the NPRA-registered package insert to determine whether seborrheic dermatitis is already covered or constitutes a true off-label use in Malaysia.
- **Obtain full safety data:** Download and parse the registered Malaysian SmPC/package insert to complete the warning and contraindication profile (currently blocking for formal safety assessment).
- **Dosage form verification:** Confirm that the currently registered product in Malaysia is pimecrolimus 1% cream (the formulation studied in all relevant trials), and that topical application route is covered.
- **Pharmaco-economic assessment:** Evaluate cost-competitiveness vs. ketoconazole and low-potency topical corticosteroids, which are the current standard of care in Malaysia for seborrheic dermatitis.
- **Regulatory pathway review:** Determine whether a label extension application to NPRA is required or whether the current broad dermatitis indication encompasses seborrheic dermatitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

