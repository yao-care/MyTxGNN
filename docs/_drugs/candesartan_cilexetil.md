---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker (ARB) prodrug, a drug class established for the treatment of hypertension. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, but this direction is currently supported **only by the model's mechanistic score** — no clinical trials or literature specific to this indication have been identified, and a blocking data gap (missing TFDA/NPRA product label) prevents safety evaluation at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension *(general ARB drug-class indication; specific NPRA-approved label text is not available in this evidence pack — see Safety Considerations)* |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified for this indication) |
| Malaysia Market Status | ✓ Marketed (13 registrations) |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in this evidence pack (Data Gap DG002, High severity). Based on general pharmacological knowledge, candesartan cilexetil is an ester prodrug that is hydrolyzed to active candesartan, a selective angiotensin II type 1 (AT1) receptor antagonist. By blocking AT1 receptors, it inhibits renin-angiotensin-aldosterone system (RAAS)-mediated vasoconstriction and aldosterone secretion, and this mechanism underlies its established use for hypertension.

Malignant renovascular hypertension is pathophysiologically driven by excessive renin secretion secondary to renal artery stenosis, which in turn hyperactivates the RAAS pathway. Since ARBs directly interrupt this pathway, there is a plausible mechanistic rationale for candesartan's activity in renovascular hypertension in general, and ARBs already have an established clinical role in non-malignant renovascular hypertension.

However, the "malignant" subtype represents a hypertensive emergency, frequently accompanied by acute target-organ damage (retinopathy, acute kidney injury). Emergency management typically relies on intravenous antihypertensives rather than oral ARBs as first-line therapy, and in patients with bilateral renal artery stenosis, ARB use carries a recognized risk of precipitating acute renal function deterioration. Renal function and renal artery status should therefore be carefully assessed before candesartan is considered for long-term use in this population. This mechanistic plausibility, combined with the complete absence of direct clinical or literature evidence, is why the evidence level is rated L5 rather than higher.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Malaysia Market Information

NPRA registration records indicate **13 active licenses** for candesartan cilexetil in Malaysia, confirming the drug is currently marketed. However, this evidence pack does not include the underlying license details (authorization numbers, product names, dosage forms, or approved indication text) — all corresponding fields were returned empty by the data source. This is a data gap requiring direct retrieval from the NPRA product registry before license-level detail can be reported.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: retrieval of the TFDA/NPRA product label — including warnings, contraindications, and drug interaction data — is recorded as a **Blocking** data gap (DG001) in this evidence pack. This gap by itself prevents the candidate from entering the S1 safety initial-evaluation stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Malignant renovascular hypertension has a plausible RAAS-blockade mechanistic rationale but is supported by no clinical trials and no literature in the current evidence pack, placing it at evidence level L5. This alone would limit the candidate to a research question. More critically, the missing TFDA/NPRA product label (Data Gap DG001, Blocking) prevents any safety initial evaluation, and missing DrugBank mechanism-of-action data (Data Gap DG002, High) limits confidence in the mechanistic linkage. Given the emergency nature of the "malignant" phenotype and the known renal risk of ARBs in bilateral renal artery stenosis, proceeding without safety data would be inappropriate.

**To proceed, the following is needed:**
- TFDA/NPRA product label (warnings, contraindications, drug interactions) — resolves Blocking gap DG001
- DrugBank-confirmed mechanism of action — resolves High-severity gap DG002
- Complete NPRA license details (product names, dosage forms, approved indication text) for the 13 registered products
- Targeted literature/clinical trial search specific to ARB use in renovascular hypertension and renal artery stenosis populations
- Nephrology input on renal function and renal artery imaging criteria required before considering ARB use in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

