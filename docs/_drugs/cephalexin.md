---
layout: default
title: Cephalexin
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 5
---

# Cephalexin
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

# Cephalexin: From Bacterial Infections to Streptococcal Pneumonia

## One-Sentence Summary

Cephalexin is a first-generation oral cephalosporin antibiotic long used against susceptible bacterial infections. The TxGNN model lists **Streptococcal Pneumonia** as its top associated indication, but the prediction carries a **0% score** and the evidence pack's own mechanistic analysis identifies this as an existing antibacterial-spectrum use rather than a novel repurposing signal — supported by **0 clinical trials** and **20 literature references**, mostly older reviews and small comparator studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this data pull (Cephalexin is a first-generation cephalosporin antibiotic for susceptible bacterial infections) |
| Predicted New Indication | Streptococcal Pneumonia |
| TxGNN Prediction Score | 0% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 26 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, Cephalexin inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs), giving it direct antibacterial activity against susceptible gram-positive organisms, including *Streptococcus pneumoniae*.

This is the key caveat for this candidate: the evidence pack's own mechanistic rationale explicitly states that streptococcal pneumonia falls **within cephalexin's existing antibacterial spectrum rather than a cross-mechanism repurposing hypothesis** ("此為抗菌譜內用途而非跨機轉再利用"). The TxGNN score of 0.0 — identical across all five predicted indications in this pack — provides no computational novelty signal to support a genuine repurposing claim.

The same pattern holds across the other four candidates in this pack: *streptococcal infection* (L2, "既有適應症延伸使用") and *staphylococcus aureus infection* (L1, "非跨機轉假說") are both explicitly labeled as on-spectrum extensions rather than new indications, while *infectious otitis media* and *arthropathy* have weak or mismatched mechanistic support. None of the five candidates in this evidence pack represents a strong novel repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [799997](https://pubmed.ncbi.nlm.nih.gov/799997/) | 1976 | RCT (small, old) | J Int Med Res | Randomized double-blind comparison of cephradine vs. cephalexin in 162 children with bacterial infections, including lobar pneumonia and skin infections |
| [4284](https://pubmed.ncbi.nlm.nih.gov/4284/) | 1976 | RCT (small, old) | Curr Ther Res Clin Exp | Comparison of cephradine and cephalexin in respiratory and urinary tract infections |
| [4248663](https://pubmed.ncbi.nlm.nih.gov/4248663/) | 1970 | Review | Med Clin North Am | General review of cephalexin pharmacology and clinical use |
| [3803252](https://pubmed.ncbi.nlm.nih.gov/3803252/) | 1986 | RCT (comparator: cefaclor, not cephalexin arm) | Drugs | 103 gold-miners with pneumococcal pneumonia treated with cefadroxil vs. cefaclor; 94% clinical cure in both arms — cephalexin not a study arm |
| [3752972](https://pubmed.ncbi.nlm.nih.gov/3752972/) | 1986 | Animal model | Antimicrob Agents Chemother | Rat lung-infection model: cefadroxil ~8x more effective than cephalexin at reducing viable streptococci at infection site |
| [44908](https://pubmed.ncbi.nlm.nih.gov/44908/) | 1979 | Cohort (cefaclor, not cephalexin) | Postgrad Med J | 60 patients with pneumonia/bronchitis treated with cefaclor; cephalexin not the study drug |
| [5556191](https://pubmed.ncbi.nlm.nih.gov/5556191/) | 1971 | Pending classification | Postgrad Med J | "Treatment of pneumonia in childhood with cephalexin" — title directly relevant, abstract not retrieved |
| [4404851](https://pubmed.ncbi.nlm.nih.gov/4404851/) | 1972 | Pending classification | Scand J Infect Dis | "Cephalexin therapy of lower respiratory tract, soft tissue and bone infections" |
| [4931110](https://pubmed.ncbi.nlm.nih.gov/4931110/) | 1970 | Pending classification | La Prensa Med Mex | Cephalexin monohydrate in 120 children with respiratory infections; clinical, bacteriological and hematic/hepatic/renal tolerance data |
| [4642154](https://pubmed.ncbi.nlm.nih.gov/4642154/) | 1972 | Pending classification | Am Fam Physician | General review titled "Pneumonia" |

---

## Malaysia Market Information

Detailed authorization records (product name, dosage form, manufacturer, approved indication text) were not populated in this data pull — all fields returned blank. NPRA query log confirms **26 active registrations** for Cephalexin as of the data cutoff, with overall market status "已上市" (Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: NPRA/TFDA package insert warnings and contraindications are flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any safety-stage evaluation (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 0.0 provides no computational novelty signal, and the evidence pack's own mechanistic rationale confirms that streptococcal pneumonia falls within cephalexin's existing antibacterial spectrum rather than representing a genuine repurposing hypothesis. No clinical trials directly test cephalexin for this indication, and a Blocking data gap on regulatory warnings/contraindications prevents even an initial safety screen.

**To proceed, the following is needed:**
- NPRA/TFDA package insert warnings and contraindications (Blocking gap, DG001)
- DrugBank mechanism-of-action detail (DG002)
- A trial or controlled study evaluating cephalexin itself (not comparator cephalosporins) specifically for streptococcal pneumonia
- Reassessment of whether this and the other four predicted indications in this pack should be reclassified as label-consistent uses rather than repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

