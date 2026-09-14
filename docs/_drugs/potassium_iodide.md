---
layout: default
title: Potassium Iodide
parent: 僅模型預測 (L5)
nav_order: 567
evidence_level: L5
indication_count: 2
---

# Potassium Iodide
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

# Potassium Iodide: From Unspecified Original Indication to Nasal Cavity Disease

## One-Sentence Summary

Potassium iodide (DrugBank DB06715) has 121 registered products in Malaysia, but its original approved indication is not recorded in the available registry data.
The TxGNN model predicts potential relevance to **Nasal Cavity Disease** (score 99.95%), with **0 clinical trials** and **4 case-report publications** — all describing fungal (mycotic) nasal/sinus infections rather than the broad TxGNN category itself, and mostly in veterinary settings.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available NPRA/registry data |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 121 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for potassium iodide. Based on the evidence collected, potassium iodide (as a saturated solution, SSKI) has a long traditional history as treatment for subcutaneous and mucosal fungal infections — notably sporotrichosis and mucormycosis (zygomycosis). Its mechanism is not fully elucidated, but is thought to involve direct antifungal activity from released iodine along with modulation of local inflammatory/immune responses.

The literature supporting this prediction describes a narrow clinical scenario — mycotic rhinitis and rhinofacial fungal infections (caused by organisms such as *Aspergillus fumigatus*, *Pseudallescheria boydii*, and *Pythium insidiosum*) — rather than "nasal cavity disease" as a broad category. This represents an **indirect mapping**: the TxGNN score reflects knowledge-graph-level similarity, while actual clinical support is limited to a specific fungal-infection subset of nasal disease, largely in veterinary case reports.

Because the mechanistic and disease-category link is narrow and indirect, and no interventional trials exist, this prediction should be interpreted as hypothesis-generating rather than clinically actionable at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case report | Journal de mycologie médicale | Successful potassium iodide treatment for rhinofacial pythiosis (oomycete infection) in sheep, causing nasal cavity and hard palate masses |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case report | Veterinary Research Communications | Mycotic rhinitis caused by *Aspergillus fumigatus* in a horse treated with topical clotrimazole plus oral potassium iodide |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case report | Journal of the American Veterinary Medical Association | *Pseudallescheria boydii* nasal cavity infection in a horse, treated with intranasal miconazole and intravenous sodium iodide |
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case report | Revista do Instituto de Medicina Tropical de São Paulo | Human case of nasofacial zygomycosis (mucormycosis) in Brazil showing rapid response to potassium iodide therapy |

---

## Malaysia Market Information

Malaysia has 121 registered products containing potassium iodide (market status: Marketed), but authorization numbers, product names, dosage forms, and approved indication text are not available in the current data extract.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is limited to four case reports (mostly veterinary), addressing a narrower fungal-rhinitis indication rather than the broad "nasal cavity disease" category predicted by TxGNN, with no clinical trials. A second predicted indication (acute laryngopharyngitis, score 99.95%) has no supporting clinical trials or literature at all and is also rated Hold — it will not be pursued further at this stage.
- Safety review cannot proceed: TFDA/NPRA package insert warnings and contraindications are a blocking data gap (DG001), and mechanism of action data is also missing (DG002).

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and drug interaction data for potassium iodide (blocking gap, DG001)
- Verified mechanism of action information (DG002)
- Clarification of which specific nasal/sinus condition (e.g., fungal rhinosinusitis) TxGNN's "nasal cavity disease" category corresponds to, and whether human (not just veterinary) evidence exists
- Malaysia-specific license and product details (currently unavailable despite 121 registrations)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

