---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 1
---

# Dapsone
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

# Dapsone: From Leprosy / Dermatitis Herpetiformis to Pneumocystosis

*Note: The evidence pack's Taiwan/Malaysia regulatory license records contain no populated original-indication text (data gap DG001), so "Leprosy / Dermatitis Herpetiformis" above reflects Dapsone's well-established general indications rather than a value extracted from this pack.*

## One-Sentence Summary

Dapsone is a sulfone-class antibacterial classically indicated for leprosy (Hansen's disease) and dermatitis herpetiformis; the TFDA label detail needed to confirm this locally is currently missing from the evidence pack (data gap DG001). The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis pneumonia)**, a prediction that aligns with dapsone's established off-label/guideline-based use as PCP prophylaxis — but the pack currently contains **0 matched clinical trials** and **0 matched publications** for this specific pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in evidence pack (TFDA license text blank — see DG001); generally known as leprosy / dermatitis herpetiformis |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 (per source scoring — see rationale below; note zero trials/literature were indexed in this pack) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002 — High severity gap). Based on known pharmacology, Dapsone is a sulfonamide analog that inhibits dihydropteroate synthase in *Pneumocystis jirovecii*, the same mechanistic target as sulfamethoxazole. This places dapsone squarely in the established antifolate pathway used against this organism.

Clinically, dapsone (alone or combined with pyrimethamine) is already a recognized alternative for Pneumocystis pneumonia (PCP) prophylaxis and treatment in patients who cannot tolerate trimethoprim-sulfamethoxazole (TMP-SMX), and is included in CDC/NIH/IDSA opportunistic infection guidelines. In other words, this is not a novel repurposing hypothesis generated purely from graph inference — it reflects existing clinical practice that the TxGNN model has independently recovered, which is a strong internal-consistency signal for the prediction.

The high TxGNN score (99.73%) is therefore consistent with prior mechanistic and guideline evidence, even though this specific evidence pack did not return matching entries from ClinicalTrials.gov, ICTRP, or PubMed for the dapsone–pneumocystosis pairing (see Clinical Trial and Literature sections below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Malaysia Market Information

Dapsone holds **2 registrations** with market status "Marketed," but the evidence pack's license records (authorization number, product name, dosage form, approved indication) are blank for both entries — this is consistent with data gap DG001 (TFDA label/warning extraction not yet completed). Populated license details are needed before this table can be produced.

## Safety Considerations

Please refer to the package insert for safety information.

Note: Key warnings, contraindications, and drug-interaction data are all currently unavailable in this evidence pack (DG001, severity: Blocking — "cannot proceed to S1 safety screening"). This is a hard blocker for any safety-based go/no-go assessment, independent of the efficacy evidence above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic and guideline-based rationale for dapsone in pneumocystosis is sound and reflects existing clinical practice, but a Blocking data gap (TFDA label warnings/contraindications, DG001) prevents any safety screening, and this pack independently indexed zero clinical trials or publications for the specific pairing.

**To proceed, the following is needed:**
- TFDA product label (warnings/contraindications) to close DG001 and unblock S1 safety review
- Mechanism of action documentation from DrugBank to close DG002
- Populated Malaysia license details (product name, dosage form, approved indication text)
- Targeted literature search for dapsone PCP-prophylaxis guideline citations (CDC/NIH/IDSA) to substantiate the L2 evidence rating with primary sources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

