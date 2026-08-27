---
layout: default
title: Histidine
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 2
---

# Histidine
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

# Histidine: From Amino Acid Supplement to Predicted Gastroparesis

## One-Sentence Summary

Histidine is an essential amino acid marketed in Malaysia across 32 registered products, but the specific approved indication text was not captured in this dataset. The TxGNN model predicts a possible link to **Gastroparesis**, but this prediction currently has **zero supporting clinical trials and zero literature citations** — it is a pure algorithmic signal with no independent corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (approved indication text was not extracted for any of the 32 Malaysia licenses) |
| Predicted New Indication | Gastroparesis (disease) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 32 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for histidine in this evidence pack. Based on known biochemistry, histidine is the biosynthetic precursor of histamine (via L‑histidine decarboxylase), and histamine acts on H2 receptors to modulate gastrointestinal smooth muscle motility — giving a theoretical, indirect connection to gastric emptying / gastroparesis.

However, this link is speculative rather than established: the TxGNN score (0.9955) is a pure graph‑based prediction with **no supporting clinical trials, ICTRP trials, or PubMed literature** for the histidine–gastroparesis pair. Furthermore, the directionality of histamine's net effect on gastric emptying is not settled in the literature — some reports describe a prokinetic effect, others an inhibitory one — so even the proposed mechanism cannot be confidently signed as beneficial.

Notably, a second TxGNN-predicted indication for this drug (sclerosing cholangitis, not the primary focus of this report) is backed by real preclinical literature — but that literature actually points in the **opposite direction**: it shows that *blocking* histamine signaling (not supplementing its precursor) reduces biliary injury and fibrosis. This raises a broader caution about relying on histidine→histamine pathway reasoning alone as a basis for repurposing decisions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the histidine–gastroparesis pairing (0 hits from ClinicalTrials.gov and ICTRP).

---

## Literature Evidence

Currently no related literature available for the histidine–gastroparesis pairing (0 hits from PubMed).

---

## Supplementary Note: Second Predicted Indication (Sclerosing Cholangitis)

This evidence pack (candidate ID ending in "-multi") also carries a second, lower-ranked TxGNN prediction that is worth flagging alongside the primary one, because it has real supporting literature and an important caveat:

| Item | Content |
|------|------|
| Disease | Sclerosing cholangitis |
| TxGNN Score | 99.27% (rank 9734) |
| Evidence Level | L4 (8 PubMed citations, all preclinical/mechanistic or biomarker studies; no clinical trials) |

Multiple animal studies (PMIDs 27351144, 32054995, 35799467, 29601088) show that mast‑cell‑derived histamine *drives* biliary proliferation and fibrosis in primary sclerosing cholangitis (PSC) models, and that **blocking** H1/H2 receptors or knocking out histidine decarboxylase (the histidine→histamine enzyme) *reduces* biliary damage. This is a directionally contradictory signal: the mechanistic evidence supports *inhibiting* the histamine pathway as beneficial in PSC, not supplementing its precursor (histidine). This should be treated as a potential safety signal rather than a repurposing opportunity, and warrants explicit review before any further evaluation of histidine in hepatobiliary disease.

---

## Malaysia Market Information

Histidine holds 32 active registrations in Malaysia under "已上市" (marketed) status. License-level detail (authorization number, product name, dosage form, approved indication text) was not populated in the extracted dataset for this drug, so a per-product table cannot be presented without fabricating values.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack — DG001 flags TFDA/NPRA label warnings/contraindications as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary predicted indication (gastroparesis) is evidence level L5 — a model score with no supporting trials or literature at all. The secondary predicted indication (sclerosing cholangitis) has L4 mechanistic evidence, but that evidence points against, not toward, the biological plausibility of supplementing histidine. Neither indication currently meets the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action for histidine — currently a High-severity gap (DG002)
- Any real-world or preclinical evidence specific to histidine (not just downstream histamine) in gastric motility disorders
- Resolution of the directional contradiction seen in the sclerosing cholangitis literature before considering that indication further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

