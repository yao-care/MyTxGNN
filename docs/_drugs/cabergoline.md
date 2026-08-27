---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 5
---

# Cabergoline
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

Using the provided Evidence Pack, I'll generate the drug repurposing evaluation report following the specified structure exactly.

# Cabergoline: From Hyperprolactinemia (Prolactinoma) to Pituitary Adenocarcinoma (Disease)

## One-Sentence Summary

> Cabergoline is a long-acting dopamine D2-receptor agonist whose established, evidence-rich use is the treatment of prolactin-secreting and other pituitary adenomas (hyperprolactinemia). The TxGNN model's top-ranked prediction for this drug is **Pituitary Adenocarcinoma (disease)**, but the supporting evidence is thin — **0 clinical trials** and only **3 tangentially related publications**, two of which do not actually describe the predicted disease. A closely related TxGNN node in the same evidence pack, "pituitary cancer" (rank 3), carries far stronger support (20 trials, 20 publications) and should be treated as the more actionable signal for this drug's pituitary-tumor repurposing story.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from the Malaysia (NPRA) registry (license record is unpopulated). Based on evidence-pack literature and trial descriptions, cabergoline's established use is treatment of hyperprolactinemia / prolactinoma and other prolactin-secreting pituitary adenomas. |
| Predicted New Indication | Pituitary Adenocarcinoma (disease) |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cabergoline is currently a documented data gap (DG002) in this evidence pack. However, the literature and clinical-trial evidence collected *within this pack* consistently describe cabergoline as a high-potency, long-acting dopamine D2-receptor agonist (with additional 5-HT2B activity). Through D2-receptor activation, cabergoline suppresses prolactin secretion and directly inhibits proliferation of D2-receptor-expressing pituitary tumor cells — this is its well-established mechanism in prolactinoma and, increasingly, in non-functioning pituitary adenomas (see e.g. PMID 38989697, PMID 31597135).

The predicted new indication, "Pituitary Adenocarcinoma (disease)," is organ- and mechanism-adjacent to cabergoline's original use: both involve tumors of the same gland and the same dopaminergic target pathway. On its face this makes the TxGNN prediction biologically plausible. However, the rationale attached to this specific node is explicit that the plausibility is largely inherited from a **different, closely related TxGNN node — "pituitary cancer" (rank 3 in this same pack)** — rather than from evidence specific to "pituitary adenocarcinoma" itself. Two of the three literature hits retrieved for this node are only tangentially connected (one describes pancreatic adenocarcinoma, the other an MEN1 gene variant case), meaning the *directly supporting* literature for this exact node is essentially a single case series. The mechanistic story is credible, but the direct evidentiary base for this exact disease label is weak.

**Important distinction:** the strong body of trial evidence in this evidence pack (20 trials, largely Phase 2–4, several completed RCTs) is for pituitary **adenomas** — predominantly prolactinomas and non-functioning pituitary adenomas, which are typically benign — not for pituitary **carcinoma**, a rare, more aggressive malignant entity. Any recommendation should be careful not to conflate adenoma-level efficacy evidence with a claim of efficacy against true pituitary carcinoma.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for "Pituitary Adenocarcinoma (disease)" specifically (`clinical_trials` = 0 in this node's evidence).

*Note: a closely related node in this same evidence pack, "pituitary cancer," has 20 associated trials — see "Related TxGNN Candidates" below for context.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case series/Retrospective | Endocrine Practice | Long-term octreotide or cabergoline management in a patient with ectopic ACTH hypersecretion; corticotropin response described in a single case. |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case report (not directly relevant — pancreatic adenocarcinoma) | Revista Española de Enfermedades Digestivas | Patient with pre-existing pituitary adenoma on cabergoline later diagnosed with duodenal infiltration by pancreatic adenocarcinoma; cabergoline is incidental to the case, not the treatment focus. |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case report (indirect — MEN1 syndrome) | Medicine | Atypical MEN1 case with a variant of uncertain pathogenicity; relevance to cabergoline/pituitary adenocarcinoma is indirect (via MEN1-associated pituitary tumors). |

---

## Malaysia Market Information

The NPRA registry confirms cabergoline is marketed in Malaysia (1 registration), but the underlying license record fields (authorization number, product name, dosage form, approved indication text) are currently empty in this evidence pack. Detailed registration information could not be extracted and should be sourced directly from the NPRA product registry before this data point is relied upon.

---

## Related TxGNN Candidates in This Evidence Pack

This evidence pack scored five TxGNN-predicted indications for cabergoline. For context, since they share overlapping biology, they are summarized here (not a substitute for the sections above, which are scoped to the top-ranked candidate):

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Pituitary Adenocarcinoma (disease) | 99.06% | L3 | Research Question | Subject of this report; direct literature largely tangential |
| 2 | Progeria–short stature–pigmented nevi syndrome | 99.06% | L5 | Hold | Zero trials/literature; no plausible mechanistic link established |
| 3 | Pituitary cancer | 99.04% | L1 | Proceed with Guardrails | 20 trials (several completed Phase 2/3 RCTs) + 20 publications, including systematic review/meta-analysis and clinical guidelines; strongest evidence in the pack, but predominantly for adenoma (prolactinoma/NFPA), not true carcinoma |
| 4 | Cerebral palsy, spastic quadriplegic | 99.02% | L5 | Hold | Zero trials/literature; theoretical dopaminergic link only |
| 5 | Glaucoma | 99.01% | L4 | Hold | Literature is contradictory — case reports and reviews describe cabergoline as a **cause** of drug-induced angle-closure glaucoma, not a treatment; risk signal, not a repurposing opportunity |

This distribution suggests the TxGNN score alone (all five candidates cluster around 99%) is not discriminating here — evidence level varies from L1 to L5 across candidates with nearly identical scores, underscoring the need for evidence-based triage rather than score-based ranking alone.

---

## Safety Considerations

Please refer to the package insert for safety information (formal safety fields — key warnings, contraindications, drug interactions — are all data gaps in this evidence pack; DG001 flags this as a **Blocking** gap that prevents this candidate from entering the S1 safety pre-assessment stage).

For awareness, the literature *within this evidence pack* (not the official label) repeatedly raises safety signals relevant to cabergoline as a class of ergot-derived dopamine agonist that should be tracked once formal label data is obtained:
- Valvular heart disease / cardiac valve regurgitation with chronic use (PMID 25732645; NCT00460616)
- Impulse control disorders (up to reported prevalence of ~60% in one screening study) (PMID 41619686)
- Drug-induced bilateral angle-closure glaucoma (PMID 21347189; PMID 25943730)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for cabergoline — Pituitary Adenocarcinoma (disease) — has no supporting clinical trials and only tangential literature support (L3, "Research Question" stage), so it does not yet warrant advancement. Separately, the mandatory Malaysia (NPRA) label data (warnings/contraindications) is a **Blocking** data gap (DG001), meaning no candidate for this drug — including the more evidence-rich "pituitary cancer" node — can formally clear the S1 safety pre-assessment until that data is obtained.

**To proceed, the following is needed:**
- Retrieve the NPRA product label/insert (warnings, contraindications, DDI) to close the Blocking gap (DG001) and enable S1 safety pre-assessment
- Obtain confirmed mechanism-of-action documentation from DrugBank to close DG002
- Disambiguate the disease scope: clarify whether "pituitary adenocarcinoma" in this workflow is intended to capture benign pituitary adenoma (where evidence is strong, per the related rank-3 node) or true malignant pituitary carcinoma (where evidence remains essentially absent)
- If the intent is the adenoma/prolactinoma indication, re-evaluate using the rank-3 "pituitary cancer" evidence base (L1, 20 trials including completed Phase 2/3 RCTs and a systematic review/meta-analysis), which is markedly stronger than the rank-1 node scored here
- Complete NPRA license record details (authorization number, approved indication text, dosage form) currently missing from the registry extract
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

