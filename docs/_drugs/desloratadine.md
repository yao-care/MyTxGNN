---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 5
---

# Desloratadine
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

# Desloratadine: From Allergic Conditions to Pharyngitis (Predicted)

## One-Sentence Summary

Desloratadine is a second-generation H1-antihistamine already marketed in Malaysia (23 registrations); its original approved indications are not available in this evidence pack's structured registry data. The TxGNN model's top-ranked candidate predicts a possible effect on **Pharyngitis**, but the **4 literature citations** supporting this pairing actually describe allergic rhinitis, chronic urticaria, or a different drug — not pharyngitis — indicating a likely data/label mismatch rather than genuine supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (all 5 license records in this pack have blank indication text; see Malaysia Market Information below) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0% (score field shows 0.0 for all 5 candidates in this pack — likely unpopulated rather than a true low score) |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 23 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, desloratadine is a peripherally-selective, second-generation H1-histamine receptor antagonist and the active metabolite of loratadine, generally used for histamine-mediated allergic conditions.

Pharyngitis is predominantly infectious or non-specific inflammatory in origin rather than histamine-mediated, so H1-receptor blockade has no established mechanistic pathway for treating it directly. The evidence pack's own rationale confirms this: none of the supporting literature actually studies pharyngitis. Instead, the cited papers address perennial allergic rhinitis, chronic idiopathic urticaria, or a related but different drug (levocetirizine). This points to a data/label mismatch in how this candidate's evidence was tagged, rather than a genuine mechanistic or clinical signal for pharyngitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12642846](https://pubmed.ncbi.nlm.nih.gov/12642846/) | 2003 | RCT | J Allergy Clin Immunol | Studies desloratadine efficacy/safety in **perennial allergic rhinitis**, not pharyngitis |
| [11277962](https://pubmed.ncbi.nlm.nih.gov/11277962/) | 2001 | RCT | Int J Dermatol | Randomized placebo-controlled trial of desloratadine in **chronic idiopathic urticaria**, not pharyngitis |
| [12962522](https://pubmed.ncbi.nlm.nih.gov/12962522/) | 2003 | Review | Drugs | General review of desloratadine efficacy across allergic disorders (rhinitis, urticaria); no pharyngitis data |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Reviews **levocetirizine** (a different drug) in allergic rhinitis/urticaria; not desloratadine, not pharyngitis |

None of the above literature directly supports a desloratadine–pharyngitis link; all four are mismatched to allergic-disease topics or a different drug.

---

## Malaysia Market Information

Detailed license-level data (authorization number, product name, dosage form, indication text) was not retrieved for this evidence pack — all 5 sampled license records are blank. The registry confirms desloratadine is **marketed** in Malaysia with **23 total registrations**, but per-product detail requires a follow-up NPRA data pull.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/NPRA label warnings and contraindications for this drug were not successfully retrieved (data gap DG001, severity: **Blocking**) — this must be resolved before any S1 safety pre-screening can proceed, regardless of indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature evidence tagged to this candidate does not actually pertain to pharyngitis — it describes allergic rhinitis, chronic urticaria, or a different drug — and there is no mechanistic basis (H1-blockade is not relevant to typically infectious/non-specific pharyngitis) or clinical trial support. Evidence level is L4 with no clinical trials, and a Blocking data gap on TFDA safety labeling further prevents progression.

**To proceed, the following is needed:**
- Retrieve and verify TFDA/NPRA package insert warnings and contraindications (DG001, Blocking)
- Obtain confirmed mechanism-of-action data from DrugBank (DG002)
- Re-verify why pharyngitis-tagged literature does not match the topic — correct the evidence-disease mapping before re-scoring this candidate
- Complete per-license Malaysia registry detail (product names, dosage forms, indication text)

**Note on other candidates in this evidence pack:** This pack contains 4 additional predicted indications for desloratadine. Of these, **allergic urticaria** (rank 4) has the strongest evidence (L1, decision stage S3, "Proceed with Guardrails") — but the pack's own rationale notes this is an already-approved labeled use of desloratadine rather than a novel repurposing candidate. The remaining candidates (papillary conjunctivitis, vasomotor rhinitis, common cold) all carry Hold recommendations due to absent or weak evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

