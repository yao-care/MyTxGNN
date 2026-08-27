---
layout: default
title: Ferrous Fumarate
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 5
---

# Ferrous Fumarate
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

# Ferrous Fumarate: From Iron-Deficiency Anemia to Acne

## One-Sentence Summary

> Ferrous fumarate is a generic oral iron salt (DrugBank DB14491) conventionally used to treat and prevent iron-deficiency anemia, though the specific NPRA-approved indication text was not captured in this evidence pack. The TxGNN model's top-ranked prediction is **Acne**, but this evidence pack contains **0 clinical trials** and **8 publications**, and the literature review finds the supporting studies are almost entirely about oral contraceptives, not iron supplementation — the mechanistic case is currently unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (all 5 NPRA license records returned blank `approved_indication_text`); ferrous fumarate is a well-known generic oral iron salt indicated for iron-deficiency anemia |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 0.00% (note: all 5 ranked predictions in this pack show an identical 0.0 score — likely a data population issue, not a true differentiator) |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 152 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on general pharmacological knowledge, ferrous fumarate is a simple ferrous iron salt used to replenish iron stores and correct hemoglobin synthesis deficits — its established use is in iron-deficiency and microcytic anemias, not dermatology.

There is no known pharmacological pathway linking iron repletion to acne pathogenesis (which is primarily driven by androgen-stimulated sebum production, follicular hyperkeratinization, and *C. acnes* colonization). Reviewing the underlying evidence for this candidate, 7 of the 8 cited publications discuss oral contraceptives (estrogen/progestin combinations) and their antiandrogenic effect on acne — a completely different drug class and mechanism from an iron salt. This pattern is consistent with a keyword/co-occurrence mismatch in the source database (e.g., "iron" and "anemia" co-occurring with contraceptive studies, or combined oral contraceptive products that historically included iron in placebo/inert pills) rather than a genuine pharmacological signal.

The one loosely iron-related paper (PMID 1974991) reports that patients with recurrent *furunculosis* (a bacterial skin infection, not acne) had low serum iron, and that iron supplementation resolved the infection — this describes iron **deficiency** predisposing to infection, which is not evidence that iron **supplementation treats acne**. Overall, the mechanistic rationale for this specific candidate is weak to absent based on currently available evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16371290](https://pubmed.ncbi.nlm.nih.gov/16371290/) | 2006 | Review | Contraception | Reviews oral contraceptive (estrogen/progestin) regimens for acne treatment — unrelated to iron supplementation |
| [9678128](https://pubmed.ncbi.nlm.nih.gov/9678128/) | 1996 | RCT (unrelated drug class) | Eur J Contracept Reprod Health Care | Compares triphasic oral contraceptive pills for contraceptive efficacy and cycle control — unrelated to ferrous fumarate |
| [2289388](https://pubmed.ncbi.nlm.nih.gov/2289388/) | 1990 | Comparative trial (unrelated drug class) | Contraception | Compares cycle control across low-dose oral contraceptive formulations — unrelated to iron |
| [16904419](https://pubmed.ncbi.nlm.nih.gov/16904419/) | 2006 | Cohort (unrelated drug class) | Contraception | Investigates whether St. John's Wort interferes with the antiandrogenic/acne effect of oral contraceptives — unrelated to iron |
| [14596626](https://pubmed.ncbi.nlm.nih.gov/14596626/) | 2003 | Validation study (QoL questionnaire) | PharmacoEconomics | Validates an acne-specific quality-of-life questionnaire used in an oral-contraceptive trial — no drug efficacy data |
| [1863941](https://pubmed.ncbi.nlm.nih.gov/1863941/) | 1991 | Phase IV study (unrelated drug class) | Clinical Therapeutics | Postmarketing study of a low-dose triphasic oral contraceptive's cycle-control performance — unrelated to iron |
| [1974991](https://pubmed.ncbi.nlm.nih.gov/1974991/) | 1990 | Case series/Preliminary report | Lancet | Patients with recurrent furunculosis (skin infection, not acne) had low serum iron; iron supplementation resolved the infection — direction is "iron deficiency → infection risk," not "iron treats acne" |
| [14158432](https://pubmed.ncbi.nlm.nih.gov/14158432/) | 1964 | Case series (historic, unrelated) | Svenska Läkartidningen | Historic survey of peroral gestagen/estrogen treatment (no abstract available) — unrelated to iron |

**Note:** None of the above literature provides direct evidence that ferrous fumarate treats acne; 7/8 papers concern an unrelated drug class (oral contraceptives).

---

## Malaysia Market Information

License records show 152 total registrations, but the sampled entries in this evidence pack returned no license number, product name, dosage form, or indication text — the field values were empty. Full registration details should be queried directly from the NPRA QUEST3+ database.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: DG001 — TFDA/NPRA package insert warnings and contraindications are marked Blocking for safety pre-screening (S1) and have not yet been obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- TxGNN score and evidence level (L5) indicate model prediction only, with no supporting clinical trials.
- The cited literature is predominantly about an unrelated drug class (oral contraceptives), suggesting the association may be a database keyword mismatch rather than a genuine signal; no plausible mechanistic link between iron repletion and acne has been identified.

**To proceed, the following is needed:**
- Verify the TxGNN scoring pipeline — all 5 ranked candidates in this pack show an identical 0.0 score, which should be investigated before this candidate is compared against others.
- Obtain confirmed DrugBank MOA data (DG002) to properly assess mechanistic plausibility.
- Obtain the NPRA package insert (warnings/contraindications, DG001 — Blocking) before any S1 safety pre-screening can proceed.
- Given the weak evidence for this candidate, consider prioritizing this drug's other TxGNN-ranked candidates instead — **microcytic anemia** (rank 2, L1, "Proceed with Guardrails," 1 completed Phase 3 RCT) and **deficiency anemia** (rank 3, extensive trial/literature base) are mechanistically coherent with iron supplementation and much better supported by this same evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

