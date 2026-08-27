---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 532
evidence_level: L5
indication_count: 6
---

# Pantoprazole
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

# Pantoprazole: From Gastroesophageal Reflux Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

> Pantoprazole is a proton pump inhibitor (PPI) internationally established for treating acid-related gastrointestinal conditions such as GERD and erosive esophagitis.
> The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
> with **3 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current NPRA registration data (pantoprazole's internationally recognized indications include GERD and erosive esophagitis — see note below) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 30 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a data gap). Based on evidence from the literature pack, pantoprazole is a proton pump inhibitor that binds irreversibly and specifically to the gastric H⁺/K⁺-ATPase ("proton pump") on the parietal cell, thereby reducing gastric acid secretion (PMID 19938880, 9017763).

Peptic ulcer disease and acid-related conditions such as GERD and H. pylori-associated gastritis share the same underlying pathophysiology — excess or unbuffered gastric acid damaging the gastrointestinal mucosa. Since acid suppression is the central therapeutic principle for both, pantoprazole's core mechanism is directly applicable to active peptic ulcer disease.

This is reinforced by the fact that pantoprazole is already one of the most extensively studied PPIs in peptic ulcer management, including H. pylori eradication triple therapy and prevention/treatment of ulcer bleeding, which is reflected in the large body of clinical trial and publication evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled trial comparing ilaprazole vs. pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors predicting poor stigmata fading or early rebleeding after endoscopic hemostasis and high-dose PPI infusion, to guide second-look endoscopy selection |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the effect of various PPIs (including pantoprazole) on platelet aggregation and clopidogrel antiplatelet interaction in patients undergoing PCI with dual antiplatelet therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective randomized study comparing intermittent vs. continuous pantoprazole infusion for preventing peptic ulcer rebleeding after endoscopic therapy |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole + amoxicillin + azithromycin/clarithromycin regimens for H. pylori eradication in duodenal ulcer |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Comparison of three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Prospective RCT showing pantoprazole infusion as adjuvant therapy after endoscopic treatment improves outcomes in peptic ulcer bleeding |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole's mechanism (irreversible proton pump binding) and favorable drug-interaction profile |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | Review of PPI mechanism of action and superiority over H2RAs in acid-related disease control |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Review | Am J Gastroenterol | Network meta-analysis comparing P-CAB vs. PPI (including pantoprazole) efficacy in severe (Grade C/D) esophagitis |
| [10983736](https://pubmed.ncbi.nlm.nih.gov/10983736/) | 2000 | Review | Drugs | Comparative review of esomeprazole vs. other PPIs including pantoprazole in GERD/erosive esophagitis healing |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical | Inflammopharmacology | Rat model study of pantoprazole combined with mesenchymal stem cells on gastric ulcer healing, oxidative stress and apoptosis pathways |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Cohort | Hepatogastroenterology | Comparison of lansoprazole vs. pantoprazole efficacy in active duodenal ulcer treatment and H. pylori eradication |

---

## Malaysia Market Information

Pantoprazole holds **30 active NPRA product registrations** and is confirmed **Marketed** in Malaysia. However, individual authorization numbers, product names, dosage forms, and approved indication text are not available in the current dataset — this has been logged as a Blocking data gap (requires downloading and parsing NPRA product label PDFs).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (flagged as a Blocking data gap that must be resolved before the safety review stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and directly supported by L1-level evidence (Phase 3 RCT plus a substantial literature base) for pantoprazole's acid-suppressive effect in active peptic ulcer disease. However, a Blocking data gap on NPRA label warnings/contraindications means this candidate cannot yet clear the S1 safety pre-screen, so progression must be gated on closing that gap.

**To proceed, the following is needed:**
- NPRA product label (warnings, contraindications, DDI) — download and parse from NPRA official source
- DrugBank mechanism of action data via API query
- Individual NPRA license/product details (currently only aggregate count of 30 is known)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

