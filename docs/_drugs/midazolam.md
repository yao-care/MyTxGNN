---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 484
evidence_level: L5
indication_count: 1
---

# Midazolam
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

# Midazolam: From Sedation/Anesthesia to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine most commonly used for procedural sedation, preoperative anxiolysis, and induction of anesthesia. The TxGNN model predicts it may also be effective for **Insomnia**, with **32 clinical trials** identified in the search (mostly related to sedation/sleep-quality contexts) and **11 publications**, including several older double-blind randomized trials that directly tested midazolam for sleep disorders. A blocking data gap remains: NPRA package-insert warnings and contraindications have not yet been retrieved, so full safety screening (S1) cannot be completed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Sedation / anesthesia induction (specific NPRA-approved indication text not captured in current dataset) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, midazolam is a short-acting benzodiazepine that acts as a positive allosteric modulator at the GABA-A receptor, enhancing inhibitory GABAergic neurotransmission to produce sedative, anxiolytic, amnestic, and hypnotic effects. It is primarily used for procedural sedation, preoperative anxiolysis, and induction of general anesthesia.

Because insomnia is fundamentally a disorder of sleep initiation and maintenance, and midazolam's core pharmacological action is hypnotic/sedative, the mechanistic rationale for repurposing toward insomnia is direct rather than incidental — other benzodiazepines in the same class (e.g., triazolam, temazepam) are already approved hypnotics. This shared mechanism plausibly explains the strong TxGNN score.

That said, most of the clinical trial evidence retrieved relates to procedural/perioperative sedation and sleep-quality outcomes in surgical or ICU settings, not to chronic primary insomnia as a standalone indication. The strongest direct evidence for an insomnia indication comes from a small set of older (1981–1990) double-blind randomized trials specifically testing oral midazolam in patients with sleep disorders.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam for postoperative pain in patients with sleep disturbance/anxiety undergoing laparoscopic colorectal cancer resection |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Compares postoperative sleep quality with IV dexmedetomidine vs. midazolam sedation for TURP |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | Compares sleep quality/quantity (24h polysomnography) between dexmedetomidine and midazolam in ICU patients |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Compares polysomnographic sleep stages between α2 agonist (dexmedetomidine) and GABA agonist (midazolam-class) sedation |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Sedation efficacy of dexmedetomidine vs. midazolam in critically ill ventilated children |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Completed | 23 | Dexmedetomidine vs. midazolam for facilitating extubation in ICU patients |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Phase 2 | Unknown | 60 | Compares dexmedetomidine, midazolam, and remifentanil for sedation in orthopedic surgery under regional anesthesia |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not yet recruiting | 195 | Oral melatonin vs. oral midazolam as premedication in children undergoing tonsillectomy |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Phase 2 | Recruiting | 110 | Internet-based CBT plus IV ketamine for suicidality in treatment-resistant depression, midazolam-controlled |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | NA | Completed | 178 | Effect of ketamine on sleep quality during colonoscopy sedation (midazolam used in standard sedation protocol) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Double-blind trial: midazolam 15mg vs. Vesparax in insomnia secondary to neuromuscular disease; midazolam was an effective hypnotic, better tolerated, no hangover effect |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Randomized, double-blind, parallel-group multicenter study of sleep, performance, and plasma levels with 14-day use of flurazepam vs. midazolam in chronic insomniacs |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Executive summary of the above multicenter 14-day flurazepam vs. midazolam trial in chronic insomniacs |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Clinical Trial | Arzneimittel-Forschung | Multi-center dose-finding pilot study of oral midazolam (10–30mg) in 75 hospitalized patients with mild-to-moderate insomnia |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | Review of insomnia pathophysiology, including hyperarousal state in primary insomnia |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | Review of clinical use of hypnotics (including benzodiazepines) and rationale for a variety of hypnotic options |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- TxGNN prediction is strong (99.74%) and is supported by several historical double-blind RCTs directly testing midazolam for sleep disorders/insomnia, giving mechanistic and empirical plausibility. However, NPRA package-insert warnings and contraindications are a **blocking** data gap — the candidate cannot pass initial safety screening (S1) without this information, particularly given midazolam's known respiratory depression and dependence risks in general use.

**To proceed, the following is needed:**
- NPRA/TFDA package insert warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Malaysia product license details (brand names, dosage forms, approved indication text) — current registry data is incomplete
- Formal drug-drug interaction (DDI) profile, since none was found in this pull
- Assessment of whether current midazolam formulations (injectable/procedural) are compatible with a chronic insomnia dosing regimen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

