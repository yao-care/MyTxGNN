---
layout: default
title: Clofazimine
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Clofazimine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clofazimine: From Leprosy (Hansen's Disease) to Pneumocystosis

## One-Sentence Summary

Clofazimine is a riminophenazine antimycobacterial agent, established in leprosy multidrug therapy and multidrug-resistant tuberculosis regimens.
The TxGNN model predicts it may be effective for **Pneumocystosis**, with a prediction score of **99.90%**, but **0 clinical trials** and **0 publications** currently support this direction, and the model's own mechanistic rationale flags the prediction as likely a knowledge-graph co-occurrence artifact rather than a true pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy (Hansen's disease) / MDR-TB — based on established pharmacological knowledge of clofazimine; not confirmed by NPRA license text in this Evidence Pack (all 4 license records have blank indication fields — see Data Gap DG001) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, clofazimine is a riminophenazine compound whose established mechanism involves DNA binding, reactive oxygen species (ROS) induction, and inhibition of the K+ channel/phospholipase A2 pathway — an antimycobacterial and immunomodulatory profile used against *M. leprae* and *M. tuberculosis*.

*Pneumocystis jirovecii*, the causative organism of pneumocystosis, is a fungus with cell wall composition and metabolic pathways substantially different from mycobacteria. There is no documented antifungal activity for clofazimine that would mechanistically support this prediction. The evidence pack's own rationale for this ranking states that the high TxGNN score likely reflects graph proximity between clofazimine and pneumocystosis through a shared "opportunistic infection in immunocompromised populations" node cluster, rather than a genuine pharmacological relationship — and explicitly rates the credibility of this link as low.

Two lower-ranked candidates were also generated: **malaria** (99.60%, rank 6229) has a somewhat more plausible theoretical basis — clofazimine's lipophilicity, membrane penetration, and ROS-induction mechanism overlap conceptually with oxidative-stress-based antimalarial mechanisms, and the rationale notes prior literature reports of in vitro antiplasmodial activity, though this evidence pack's own PubMed/ClinicalTrials/ICTRP searches returned zero hits — suggesting an evidence-collection gap rather than a true absence of literature, and warranting a targeted follow-up search. **Gastrin secretion abnormality** (99.57%, rank 6584) has no known mechanistic basis and is assessed as likely graph noise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Malaysia Market Information

Four authorizations are on record with Malaysia's NPRA (total_licenses = 4), but product-level details (license number, product name, dosage form, approved indication text) are not populated in this Evidence Pack — this is a data gap requiring direct NPRA lookup to resolve.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this Evidence Pack — DG001, Blocking severity — and could not be retrieved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pneumocystosis) is unsupported by any clinical trial or literature evidence, and this Evidence Pack's own mechanistic analysis assesses the graph-derived link as low-credibility co-occurrence rather than genuine pharmacology. Additionally, TFDA/NPRA warning and contraindication data is a Blocking-severity gap, which prevents the case from entering the S1 safety pre-screening stage regardless of indication.

**To proceed, the following is needed:**
- NPRA/TFDA package insert (warnings, contraindications) — resolves Blocking Data Gap DG001, required before any S1 safety assessment
- DrugBank mechanism-of-action detail — resolves High-severity Data Gap DG002
- Confirmed NPRA license text for the 4 existing Malaysia registrations (license number, product name, dosage form, approved indication)
- If pursuing the malaria candidate instead of pneumocystosis: a targeted external literature search for in vitro/in vivo antiplasmodial data on clofazimine, since this evidence pack's automated search found none despite the rationale citing prior reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

