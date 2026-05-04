---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Azithromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Azithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Azithromycin is a widely used macrolide antibiotic originally indicated for various bacterial infections (respiratory, skin, sexually transmitted infections, etc.). The TxGNN model's top-ranked prediction suggests it may be effective for **Hyperamylasemia**, however there are currently **no clinical trials** and **no publications** supporting this direction, making this a model-only prediction (L5). Among all 10 predicted indications, **Septicemic Plague** (Rank 9) presents the strongest mechanistic rationale and is the only candidate recommended for advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (respiratory tract, skin, sexually transmitted infections) |
| Predicted New Indication (Rank 1) | Hyperamylasemia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 46 |
| Recommended Decision | **Hold** |

---

## All Predicted Indications Overview

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------|-------------|----------------|--------|--------------|----------------|
| 1 | Hyperamylasemia | 99.81% | L5 | 0 | 0 | Hold |
| 2 | Polyclonal hyperviscosity syndrome | 99.81% | L5 | 0 | 0 | Hold |
| 3 | Congenital analbuminemia | 99.79% | L5 | 0 | 0 | Hold |
| 4 | Punctate epithelial keratoconjunctivitis | 99.78% | L4 | 0 | 1 | Research Question |
| 5 | Blood group incompatibility | 99.70% | L5 | 0 | 0 | Hold |
| 6 | Premalignant hematological system disease | 99.64% | L5 | 0 | 0 | Hold |
| 7 | Monoclonal gammopathy | 99.61% | L4 | 0 | 7 | Research Question |
| 8 | Haematological disease with acquired peripheral neuropathy | 99.56% | L5 | 0 | 0 | Hold |
| 9 | **Septicemic plague** | **99.52%** | **L3** | **0** | **5** | **Proceed with Guardrails** |
| 10 | Congenital hematological disorder | 99.40% | L4 | 4 | 2 | Research Question |

> **Key finding**: 6 out of 10 predictions are rated L5 (model-only) with a "Hold" recommendation. The most actionable candidate is **Septicemic Plague** (Rank 9), the only prediction rated "Proceed with Guardrails".

---

## Why is This Prediction Reasonable?

### Rank 1: Hyperamylasemia — Not Reasonable

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Azithromycin is a macrolide antibiotic that binds to the 50S ribosomal subunit of susceptible bacteria, inhibiting bacterial protein synthesis. It has additional immunomodulatory and anti-inflammatory properties that are increasingly recognized in clinical practice.

Hyperamylasemia (elevated serum amylase levels) is a laboratory abnormality most commonly associated with pancreatitis, parotitis, and other conditions affecting the pancreas or salivary glands. It is not considered an independent therapeutic target but rather a biochemical marker of underlying disease processes.

**Critical concern**: Published literature reports that azithromycin may actually *induce* pancreatitis, which consequently leads to hyperamylasemia as an adverse drug reaction. This strongly suggests the TxGNN model has detected a drug-disease *association* that represents a causal adverse effect rather than a therapeutic relationship. This prediction is likely a **model false positive** where the direction of causality is reversed.

### Rank 9: Septicemic Plague — Strong Mechanistic Support

Azithromycin, as a broad-spectrum macrolide antibiotic, has demonstrated in vitro activity against *Yersinia pestis* (the causative agent of plague). CDC guidelines already list macrolides as an alternative therapy for plague. The mechanism is clear and direct: azithromycin binds the *Y. pestis* 50S ribosomal subunit, inhibiting bacterial protein synthesis. This represents the most mechanistically coherent repurposing candidate in this analysis.

### Rank 4: Punctate Epithelial Keratoconjunctivitis — Reasonable

Azithromycin ophthalmic solution (AzaSite® 1%) is already FDA-approved for bacterial conjunctivitis. The macrolide's anti-inflammatory properties may reduce punctate epithelial inflammation, and it has demonstrated activity against ocular surface microorganisms including *Encephalitozoon* species. This represents a route-compatible and mechanistically sound extension of existing use.

### Rank 7: Monoclonal Gammopathy — Preclinical Support

A key in vitro study (PMID 23546223) demonstrated that macrolide antibiotics, including azithromycin, can block autophagy flux and sensitize myeloma cells to bortezomib via endoplasmic reticulum stress-mediated CHOP induction. While scientifically intriguing, the therapeutic gap from MGUS to multiple myeloma treatment is substantial, and no clinical evidence exists.

### Rank 10: Congenital Hematological Disorder — Partial Support

Within this broad category, the most specific evidence comes from sickle cell disease (SCD): azithromycin's anti-inflammatory properties may reduce vaso-occlusive crises, and its antimicrobial activity may prevent infection-triggered acute chest syndrome. Two directly relevant clinical trials (NCT02630394, NCT02960503) were designed but subsequently withdrawn, possibly due to recruitment difficulties rather than safety concerns.

---

## Clinical Trial Evidence

### Rank 1: Hyperamylasemia

Currently no related clinical trials registered.

### Rank 10: Congenital Hematological Disorder (Most Trial Activity)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | Pilot study of azithromycin prophylaxis for acute chest syndrome in sickle cell disease. Designed to evaluate macrolide anti-inflammatory actions for ACS prevention. Withdrawn before enrollment. |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy to improve FEV1 in adults with sickle cell disease. Aimed to leverage azithromycin's immunomodulatory effects on SCD pulmonary complications. Withdrawn before enrollment. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Large PK/PD observational study of understudied drugs in children. Azithromycin may be among studied drugs but is not the primary focus. |
| [NCT04294641](https://clinicaltrials.gov/study/NCT04294641) | Phase 2 | Completed | 10 | Study of ibrutinib for chronic GVHD. Azithromycin is not the primary study drug; weak relevance to congenital hematological disorders. |

> **Note**: Both azithromycin-focused SCD trials (NCT02630394, NCT02960503) were withdrawn without enrollment. This pattern suggests practical barriers (recruitment, funding) rather than safety signals, but warrants investigation before initiating new trials.

---

## Literature Evidence

### Rank 1: Hyperamylasemia

Currently no related literature available.

### Rank 9: Septicemic Plague (Strongest Mechanistic Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro study | Antimicrob Agents Chemother | In vitro susceptibility of 78 *Y. pestis* strains tested against 14 antimicrobials. Notably, azithromycin showed **poor activity** against all strains — a critical counter-finding to the mechanistic hypothesis. |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Animal study | Antibiotiki i Khimioterapiia | Demonstrated high efficacy of azithromycin in experimental brucellosis treatment, with rapid normalization of bactericidal and energy systems in peripheral blood cells. Azithromycin was the most active agent tested. |
| [10628822](https://pubmed.ncbi.nlm.nih.gov/10628822/) | 2000 | Conference review | J Med Microbiol | Review of tropical/exotic infections including MDR *S. typhi* and emerging resistance patterns. Discusses fluoroquinolone and cephalosporin resistance in endemic areas. |
| [19392866](https://pubmed.ncbi.nlm.nih.gov/19392866/) | 2009 | Systematic Review | Aliment Pharmacol Ther | Systematic review of travellers' diarrhoea epidemiology and clinical features. Indirect relevance to azithromycin as an antimicrobial for enteric infections. |
| [31778198](https://pubmed.ncbi.nlm.nih.gov/31778198/) | 2019 | Review | Mil Med | Review of DoD biomedical response to STIs including *N. gonorrhoeae*. Highlights increasing antibiotic resistance and need for surveillance. Tangential relevance. |

> **Critical finding**: PMID 8540736 reports that azithromycin showed **poor in vitro activity** against *Y. pestis*. This directly contradicts the mechanistic rationale and significantly weakens the septicemic plague repurposing hypothesis despite the overall L3 evidence rating.

### Rank 7: Monoclonal Gammopathy

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | Preclinical/In vitro | Int J Oncol | **Key study**: Macrolide antibiotics (including azithromycin) block autophagy flux and sensitize myeloma cells to bortezomib via ER stress-mediated CHOP induction. Combined AZM + BZ enhanced cytotoxicity in U266, IM-9 and RPMI8226 cell lines. |
| [18355359](https://pubmed.ncbi.nlm.nih.gov/18355359/) | 2008 | Review | Clin Exp Dermatol | Review of subcorneal pustular dermatosis (Sneddon-Wilkinson disease) over 50 years. SCPD is associated with monoclonal gammopathy. Indirect relevance. |
| [33389938](https://pubmed.ncbi.nlm.nih.gov/33389938/) | 2020 | Case Report | Turk J Ophthalmol | *Bartonella henselae* neuroretinitis in POEMS syndrome with Castleman disease. Azithromycin used for infection in context of monoclonal gammopathy. |
| [22825522](https://pubmed.ncbi.nlm.nih.gov/22825522/) | 2012 | Case Report | Tumori | Azithromycin 500 mg/day used adjunctively for ONJ in a multiple myeloma patient receiving bisphosphonates. Supportive/antimicrobial role only. |
| [32708858](https://pubmed.ncbi.nlm.nih.gov/32708858/) | 2020 | Case Report | Medicina | COVID-19 in a patient with cryoglobulinemic MPGN. Azithromycin used as part of COVID treatment, not for the gammopathy itself. |

### Rank 4: Punctate Epithelial Keratoconjunctivitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult diagnosed by metagenomic deep sequencing. Demonstrates azithromycin-susceptible ocular pathogens in keratoconjunctivitis. |

### Rank 10: Congenital Hematological Disorder

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of antibiotics for preventing LRTI in high-risk children ≤12 years. Relevant to prophylactic use in children with congenital hematological conditions predisposing to infections. |
| [34471086](https://pubmed.ncbi.nlm.nih.gov/34471086/) | 2021 | Case Report | Am J Case Rep | Immune thrombocytopenia in a SARS-CoV-2 positive infant treated with megadose methylprednisolone. Azithromycin mentioned in COVID treatment context, tangential relevance. |

---

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Not available) | — | — | — |

*46 registrations were identified in the NPRA database for Azithromycin, confirming widespread market availability in Malaysia. However, detailed license information (authorization numbers, product names, dosage forms, approved indications) was not included in this evidence pack. Azithromycin is generally registered for bacterial infections of the respiratory tract, skin and soft tissue, and sexually transmitted infections.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (identified as a blocking data gap, DG001). Safety assessment cannot proceed to Stage 1 until NPRA package insert data is obtained and analysed. Known class-level concerns for macrolides include QT prolongation, hepatotoxicity, and Clostridioides difficile-associated diarrhoea.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (hyperamylasemia) lacks any supporting evidence and is likely a model false positive — azithromycin is more likely to *cause* hyperamylasemia than treat it. Among all 10 predicted indications, 6 are rated L5 (model-only) with no mechanistic rationale. The most promising candidate, **septicemic plague** (Rank 9), has mechanistic plausibility but is critically undermined by in vitro data showing poor azithromycin activity against *Y. pestis* (PMID 8540736). The **monoclonal gammopathy** direction (Rank 7) has intriguing preclinical data on autophagy blockade but is far from clinical application. Overall, no prediction in this pack reaches a confidence level sufficient for clinical advancement.

**To proceed, the following is needed:**
- **[Blocking]** Obtain NPRA package insert data (warnings, contraindications, DDI) to enable safety evaluation (DG001)
- **[High]** Obtain detailed mechanism of action data from DrugBank (DG002)
- **[For Septicemic Plague]** Reconcile conflicting evidence: CDC guideline support vs. poor in vitro activity (PMID 8540736); determine MIC breakpoints for clinical relevance
- **[For Monoclonal Gammopathy]** Evaluate whether the in vitro autophagy-blocking effect (PMID 23546223) translates to clinically achievable drug concentrations
- **[For Congenital Hematological Disorder/SCD]** Investigate reasons for withdrawal of NCT02630394 and NCT02960503 before designing new trials
- **[For Punctate Epithelial Keratoconjunctivitis]** Assess existing AzaSite® ophthalmic data for potential label extension feasibility

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

