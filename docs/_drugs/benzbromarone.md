---
layout: default
title: Benzbromarone
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 1
---

# Benzbromarone
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

# Benzbromarone: From Hyperuricemia/Gout to Renal Hypouricemia

## One-Sentence Summary

Benzbromarone is a uricosuric agent (URAT1 inhibitor) originally used for the treatment of hyperuricemia and gout.
The TxGNN model predicts it may be effective for **Renal Hypouricemia**, with **0 clinical trials** and **20 publications** identified—however, mechanistic analysis indicates this is a **contra-indicated false positive**: the drug would worsen, not treat, the predicted condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia / Gout (license detail unavailable) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L5 — Model prediction only; no therapeutic clinical evidence |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** ⛔ (Mechanistic contradiction) |

## Why is This Prediction Reasonable?

**Short answer: it is not.** While the TxGNN model assigns a high confidence score (99.07%), deeper mechanistic analysis reveals this prediction is a classic false positive driven by pathway association without regard to therapeutic directionality.

Benzbromarone is a potent inhibitor of URAT1 (urate transporter 1, encoded by the *SLC22A12* gene). Its pharmacological action blocks uric acid reabsorption in the renal proximal tubule, thereby promoting urinary uric acid excretion. This mechanism makes it effective for treating **hyperuricemia** and **gout**, where the therapeutic goal is to *lower* serum urate by *increasing* renal urate clearance.

Renal hypouricemia, by contrast, is an inherited disorder caused by **loss-of-function mutations** in URAT1 (*SLC22A12*) or GLUT9 (*SLC2A9*). Patients already have defective urate reabsorption, resulting in excessive urinary urate excretion and dangerously low serum urate levels. Administering benzbromarone—a drug that further inhibits the very transporter that is already dysfunctional—would **exacerbate** the condition rather than treat it. The TxGNN model correctly identified that benzbromarone and renal hypouricemia share the URAT1 pathway, but it **cannot distinguish between "treats via this pathway" and "acts on the same pathway in the wrong direction."** This is a well-recognized limitation of knowledge graph–based drug repurposing models.

## Clinical Trial Evidence

Currently no related clinical trials registered for benzbromarone in the treatment of renal hypouricemia.

## Literature Evidence

Twenty publications were identified; however, none describe therapeutic use of benzbromarone for renal hypouricemia. Instead, benzbromarone appears exclusively as a **diagnostic pharmacological probe** used to characterize urate transport defects. The most relevant publications are summarized below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Comprehensive review of hypouricemia for rheumatologists; classifies aetiologies and discusses URAT1/GLUT9 mutations. Benzbromarone mentioned as diagnostic tool only. |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Observational/Molecular | J Am Soc Nephrol | Sequenced SLC22A12 in 32 renal hypouricemia patients; established that URAT1 mutations cause the disorder. Benzbromarone used in tubular transport analysis. |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Preclinical/Mechanistic | J Am Soc Nephrol | Characterised mouse URAT1 homologue (RST); benzbromarone inhibited RST-mediated urate transport in Xenopus oocytes, confirming URAT1 inhibition mechanism. |
| [18670416](https://pubmed.ncbi.nlm.nih.gov/18670416/) | 2008 | Pharmacological Study | Am J Hypertens | Demonstrated losartan's uricosuric action via URAT1 inhibition in hypertensive patients; contextualises benzbromarone's mechanism alongside other URAT1 inhibitors. |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case Report | Am J Kidney Dis | Two siblings with hereditary renal hypouricemia and exercise-induced ARF; URAT1 mutation (W258X) identified. Benzbromarone used only in diagnostic workup. |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Pharmacological Study | Nephron | Analysed uric acid transport in Fanconi syndrome with marked renal hypouricemia using pyrazinamide and benzbromarone as pharmacological probes. |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Case Series | Clin Nephrol | Patient with recurrent exercise-induced ARF and renal hypouricemia; benzbromarone/pyrazinamide tests used to localise the tubular transport defect. |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case Report | Acta Paediatr | Recurrent exercise-induced ARF in renal hypouricemia; benzbromarone/pyrazinamide test suggested defective presecretory reabsorption. |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case Series | J Pediatr | Four children with hereditary renal hypouricemia; pyrazinamide and benzbromarone did not affect clearance ratios, consistent with severe transport defects. |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case Report/Mechanistic | Nephron | Young man with isolated renal urate transport defect; urate clearance further increased after benzbromarone, confirming drug worsens the phenotype. |

> **Key observation:** In multiple case reports (PMIDs 3380222, 8863890, 4009341), benzbromarone administration **increased** urate clearance in hypouricemic patients—i.e., it made the condition worse. This directly confirms the mechanistic contraindication.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Detail unavailable) | — | — | — |

*Note: One registration is recorded in Malaysia (market status: marketed), but detailed license information was not retrieved. Benzbromarone is internationally recognised as a uricosuric agent indicated for hyperuricemia and gout.*

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack.

> **Important note specific to this prediction:** Benzbromarone carries a known risk of **hepatotoxicity** (the reason it was withdrawn in several European markets). Additionally, in patients with renal hypouricemia, use of benzbromarone could theoretically precipitate **exercise-induced acute renal failure** by further increasing urinary uric acid excretion and promoting intratubular urate crystal deposition.

## Conclusion and Next Steps

**Decision: Hold ⛔**

**Rationale:**
This prediction represents a **mechanistic false positive**. The TxGNN model detected a strong association between benzbromarone and renal hypouricemia via the shared URAT1 pathway, yielding a high prediction score (99.07%). However, the drug's pharmacological action (URAT1 inhibition → increased urate excretion) is **diametrically opposed** to what renal hypouricemia patients need (restored urate reabsorption → decreased urate excretion). Published case reports confirm that benzbromarone worsens urate clearance in these patients. This candidate should not proceed to any further evaluation stage.

**This case highlights an important limitation of knowledge graph–based repurposing models:** pathway-level association does not equate to therapeutic applicability. Directional pharmacological reasoning must be applied as a post-prediction filter.

**No further action is recommended for this candidate.** Instead, the following model improvement is suggested:
- Incorporate **directionality annotations** (agonist/antagonist, gain-of-function/loss-of-function) into the TxGNN knowledge graph to reduce contra-indicated false positives
- Flag candidates where the drug's MOA targets the same transporter/receptor implicated in the disease's loss-of-function aetiology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

