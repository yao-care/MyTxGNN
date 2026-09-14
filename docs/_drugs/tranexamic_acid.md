---
layout: default
title: Tranexamic Acid
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
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

# Tranexamic Acid: From Heavy Menstrual Bleeding to Amenorrhea — A Contradictory Signal

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic agent whose established clinical role is *reducing* excessive menstrual bleeding (menorrhagia/abnormal uterine bleeding), not inducing or treating absence of menstruation. The TxGNN model predicts a link to **Amenorrhea**, but this evidence pack contains **no supporting clinical trials** and only **2 review-type publications**, neither of which studies this indication directly. The predicted direction appears pharmacologically opposite to the drug's known effect, and is flagged in this pack as a likely knowledge-graph artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in TFDA license text on file; per the evidence pack's own rationale notes, tranexamic acid is an antifibrinolytic used to control/reduce heavy menstrual bleeding and other hemorrhagic conditions |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, tranexamic acid is a plasminogen/plasmin inhibitor (antifibrinolytic) whose proven clinical effect is to **reduce** excessive uterine bleeding — the opposite physiological direction from amenorrhea (absence of menstruation).

The evidence pack itself raises this concern directly: the high TxGNN score (0.99) most likely reflects graph proximity between the "amenorrhea" node and "menstrual bleeding / abnormal uterine bleeding (AUB)" nodes in the knowledge graph, rather than a causal or therapeutic relationship. In other words, the model may be picking up on the fact that tranexamic acid is strongly associated with menstrual-bleeding-related disease concepts in general, without correctly distinguishing "treats bleeding" from "causes absence of bleeding."

Because the original MOA data is missing, this mechanistic conflict cannot be independently cross-checked or resolved from this pack alone. It should be treated as an unresolved contradiction, not as supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Evidence-based review of pharmacological therapies for **abnormal uterine bleeding** (i.e., treating excess bleeding, not amenorrhea); does not address tranexamic acid for amenorrhea specifically |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | Journal of Oncology Pharmacy Practice | Systematic approach to menses **prophylaxis and suppression** in pre-menopausal hematologic cancer patients undergoing treatment-associated cytopenias; discusses menstrual suppression strategies broadly, not amenorrhea as a treated indication for this drug |

Neither publication provides direct evidence for tranexamic acid as a treatment for amenorrhea; both concern management of menstrual bleeding, reinforcing the mechanistic conflict noted above.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA warning/contraindication data for this drug is an outstanding **Blocking**-severity data gap (DG001) — safety evaluation (Stage S1) cannot proceed until this is resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (amenorrhea) runs contrary to tranexamic acid's known pharmacological effect of reducing menstrual bleeding, and no clinical trial evidence exists to support it — the two available publications concern managing bleeding, not treating its absence. Combined with missing MOA and safety data, this candidate does not currently meet the bar to advance past initial screening (decision stage S0).

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Drug mechanism of action data from DrugBank (DG002, High)
- Independent mechanistic or clinical rationale explaining how an antifibrinolytic could plausibly treat amenorrhea, to rule out a knowledge-graph proximity artifact
- Detailed TFDA license/product records (license number, product name, dosage form, approved indication text), which were not returned in this pack despite 10 registrations on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

