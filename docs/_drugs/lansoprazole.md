---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 2
---

# Lansoprazole
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

# Lansoprazole: From Peptic Ulcer Disease/GERD to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI), a drug class established for peptic ulcer disease, GERD, and acid-related gastrointestinal conditions. The TxGNN model predicts potential relevance to **Duodenogastric Reflux**, but this direction is currently supported by **0 clinical trials** and only **2 publications** — and one of those publications actually points to a safety risk rather than a therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the current registration data. (Lansoprazole is a proton pump inhibitor generally indicated for peptic ulcer disease, GERD, and H. pylori eradication.) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

*Note: A second candidate, duodenal obstruction (Evidence Level L4, also recommended Hold), was evaluated in the same pack but is not the primary focus of this report.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Lansoprazole is part of the proton pump inhibitor (PPI) class, and its efficacy in acid-related gastrointestinal indications has been proven. Mechanistically, PPIs suppress gastric acid secretion, which could theoretically reduce the acid-related mucosal irritation caused by reflux of duodenal contents (bile, pancreatic enzymes) into the stomach — the basis for TxGNN's prediction.

However, the only directly relevant literature identified (a rat model study, PMID 15052437) found the opposite effect: Lansoprazole *promoted* gastric carcinogenesis associated with duodenogastric reflux, rather than mitigating it. This is a potential risk signal, not a therapeutic signal, and directly contradicts the mechanistic hypothesis. No clinical trials currently exist to test efficacy in this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Preclinical (rat model) | Gastric Cancer | Lansoprazole promoted gastric carcinogenesis in rats with duodenogastric reflux — a risk signal, opposite to the therapeutic hypothesis |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General review of PPI clinical use and pharmacokinetics (peptic ulcer, H. pylori, GERD, NSAID-induced GI lesions, Zollinger-Ellison syndrome); not specific to duodenogastric reflux |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the only mechanistically direct evidence (a rat carcinogenesis study) suggests risk rather than benefit, and there are zero clinical trials in this indication. Evidence Level L5 (model prediction only) does not support moving forward.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Confirmed mechanism of action from DrugBank (currently a High-severity data gap)
- Preclinical or clinical data resolving the conflicting signal from the rat carcinogenesis study before further development is considered
- If pursued, dedicated clinical studies specifically evaluating Lansoprazole in duodenogastric reflux (none currently exist)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

