---
layout: default
title: Ampicillin Trihydrate
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 0
---

# Ampicillin Trihydrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Ampicillin Trihydrate: Repurposing Evaluation (No TxGNN Prediction Available)

## One-Sentence Summary

Ampicillin Trihydrate is a broad-spectrum aminopenicillin antibiotic, widely used to treat bacterial infections including respiratory tract infections, urinary tract infections, and meningitis.
The current Evidence Pack contains **no TxGNN-predicted new indications** for this drug — the prediction pipeline has not yet been run or returned results for this candidate.
Without a predicted indication, a formal repurposing evaluation cannot be completed at this time; **this report documents current data availability and identifies the gaps that must be resolved before proceeding.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum antibiotic: respiratory, urinary tract, CNS, GI) |
| Predicted New Indication | Not available — no TxGNN prediction returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (prediction pipeline not executed) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | **Hold** — critical data gaps must be resolved first |

---

## Drug Background

Ampicillin Trihydrate is the stable trihydrate salt form of ampicillin, a broad-spectrum beta-lactam antibiotic of the aminopenicillin subclass. It has been in clinical use since the 1960s and remains on the WHO Essential Medicines List.

**Mechanism of Action (from general knowledge — DrugBank query pending):**
Ampicillin exerts bactericidal activity by irreversibly binding to penicillin-binding proteins (PBPs) located on the inner membrane of bacterial cell walls. This inhibits the transpeptidase enzyme responsible for peptidoglycan cross-linking, thereby disrupting cell wall synthesis and ultimately causing bacterial cell lysis. Its aminobenzyl side chain provides extended gram-negative coverage compared to earlier penicillins.

> ⚠️ **Data Gap DG002 (High):** Formal MOA data has not been retrieved from DrugBank for this Evidence Pack. The description above is based on established pharmacological knowledge and should be verified against the DrugBank API record before formal reporting.

**Established Indications:**
Ampicillin is approved for infections caused by susceptible organisms, including:
- Upper and lower respiratory tract infections (*Haemophilus influenzae*, *Streptococcus pneumoniae*)
- Urinary tract infections (*E. coli*, *Enterococcus faecalis*)
- Gastrointestinal infections (*Salmonella*, *Shigella*)
- Bacterial meningitis, endocarditis, and septicemia

---

## TxGNN Prediction Status

The `predicted_indications` field in the Evidence Pack is **empty**. This means one of the following scenarios has occurred:

| Possible Cause | Recommended Action |
|---|---|
| Prediction pipeline was not executed for this drug | Run `scripts/run_kg_prediction.py` with Ampicillin Trihydrate as input |
| DrugBank ID mapping failed (DrugBank ID is `null`) | Resolve DrugBank ID mapping; canonical ID is **DB00415** (ampicillin) |
| Drug name normalisation mismatch | Check if "AMPICILLIN TRIHYDRATE" normalises correctly to the KG node |
| No significant repurposing signal above threshold | Review prediction threshold settings |

Until a TxGNN prediction is available, the core sections of this report (clinical trial evidence, literature evidence, mechanism rationale) cannot be populated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a repurposing target — no predicted indication available.

---

## Literature Evidence

Currently no related literature available — no predicted indication to search against.

---

## Malaysia Market Information

The Evidence Pack confirms **9 active registrations** in Malaysia; however, all individual licence detail fields (licence number, product name, dosage form, manufacturer, approved indication) were returned as empty strings in the current data pull.

> ⚠️ Detailed licence records must be retrieved from the NPRA portal before this section can be completed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---|---|---|---|
| (9 licences confirmed) | Details not available in current data pack | — | — |

**Recommended action:** Re-query NPRA with the `MAL` licence number range or retrieve the full registration detail via the NPRA product search API to populate this table.

---

## Safety Considerations

> ⚠️ **Data Gap DG001 (Blocking):** TFDA/NPRA package insert warnings and contraindications have not been retrieved. This gap is classified as **Blocking** and prevents completion of the S1 safety pre-screening stage.

Please refer to the approved package insert for full safety information. Key areas to retrieve include:
- Hypersensitivity / anaphylaxis warnings (cross-reactivity with cephalosporins)
- Contraindications in penicillin-allergic patients
- Renal dose adjustment requirements
- Drug interactions (anticoagulants, oral contraceptives, allopurinol, bacteriostatic antibiotics)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline has not returned any repurposing candidates for Ampicillin Trihydrate, and two critical data gaps (package insert safety data and DrugBank MOA) remain unresolved. A formal repurposing evaluation cannot be conducted without a predicted indication target.

**To proceed, the following is needed:**

1. **Resolve DrugBank ID mapping** — Confirm the canonical DrugBank ID (`DB00415` for ampicillin) and re-run the KG prediction pipeline to generate `predicted_indications`.
2. **Retrieve package insert data (DG001 — Blocking)** — Download the NPRA/TFDA package insert PDF and parse warnings, contraindications, and drug interaction data.
3. **Retrieve MOA from DrugBank (DG002 — High)** — Query the DrugBank API to obtain structured pharmacology and mechanism data.
4. **Populate NPRA licence details** — Re-query NPRA to retrieve full licence records (product names, dosage forms, approved indications) for all 9 registrations.
5. **Re-run evidence collection** — Once a predicted indication is available, execute the ClinicalTrials.gov and PubMed collectors to populate the evidence tables.
6. **Re-issue this report** — After the above steps, re-generate the Evidence Pack (target version v5) and produce a complete evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

