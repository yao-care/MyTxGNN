---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 544
evidence_level: L5
indication_count: 2
---

# Phenylalanine
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

# Phenylalanine: From Unspecified Indication to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine (DrugBank DB00120) is an essential amino acid marketed in Malaysia under 35 registrations, but its approved indication text was not captured in the available registry data.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, with **no clinical trials** and only **4 tangentially related publications** currently identified — none of which studied phenylalanine as a therapeutic intervention for this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (all 5 extracted license records have blank indication text) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed (已上市) |
| Number of Registrations | 35 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for phenylalanine in this evidence pack. What is known is that phenylalanine is an essential amino acid and metabolic precursor of tyrosine — it is not a drug with a defined pharmacological mechanism targeting a specific disease pathway.

There is no established causal or mechanistic link between phenylalanine and the immune/fibrotic pathology underlying sclerosing cholangitis. The identified literature is incidental rather than supportive: one study (PMID 15790420) measured plasma tyrosine as a fatigue biomarker in cholangitis patients (an association, not an intervention); another (PMID 32025163) profiled serum metabolomics in cholangiocarcinoma for biomarker discovery; and two older papers (PMID 8000512, PMID 2103382) concern *formyl-methionyl-leucyl-phenylalanine (fMLP)*, a bacterial chemotactic peptide that merely contains a phenylalanine residue — structurally related but pharmacologically unrelated to phenylalanine itself.

The high TxGNN score (0.994) reflects topological similarity within the knowledge graph rather than mechanistic or clinical evidence. Given the absence of any direct study of phenylalanine in sclerosing cholangitis, this prediction should be treated as a hypothesis-generation signal only, not a repurposing candidate with supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined plasma tyrosine levels and their association with fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; identifies an amino-acid/fatigue association, not a phenylalanine intervention |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | Journal of Clinical and Experimental Hepatology | Serum metabolomic/mass-spectrometry profiling to find biomarkers for cholangiocarcinoma vs. benign hepatobiliary disease; no phenylalanine treatment involved |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal model | Journal of Gastroenterology | Rat colitis model: rectal administration of the bacterial peptide fMLT (which contains a phenylalanine residue) induced small duct cholangitis — a mechanistic curiosity, not evidence for phenylalanine as a treatment |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Other | Journal of Gastroenterology and Hepatology | Describes enterohepatic circulation of bacterial chemotactic F-met-oligopeptides in humans; unrelated to therapeutic use of phenylalanine |

## Malaysia Market Information

35 product registrations are on record, but the extracted regulatory dataset did not include license numbers, product names, dosage forms, or indication text for any of the 5 sampled entries — this section cannot be populated from the current evidence pack and requires re-extraction from the source registry.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN topological score (L5 evidence) with no supporting clinical trials and no literature that directly studies phenylalanine as a treatment for sclerosing cholangitis; the identified publications are biomarker or unrelated-peptide studies. There is currently no mechanistic or clinical rationale to advance this candidate.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for phenylalanine from DrugBank
- TFDA/NPRA label warnings, contraindications, and approved indication text (currently blocking, per data gap DG001)
- Any preclinical or mechanistic study directly linking phenylalanine metabolism to cholangitis/biliary fibrosis before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

