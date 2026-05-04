---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a broad-spectrum aminopenicillin antibiotic widely used to treat a range of bacterial infections, including respiratory tract, urinary tract, and skin infections.
The TxGNN model predicts it may be effective for **Laryngitis**, with **1 clinical trial** and **20 publications** currently identified in support of this direction.
However, this prediction requires careful interpretation: the overwhelming majority of laryngitis cases are viral in origin, and the mechanistic link applies only to specific, confirmed bacterial subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (detailed label text not available in this data pack) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Ampicillin is an aminopenicillin beta-lactam that exerts its bactericidal effect by binding to penicillin-binding proteins (PBPs) — the transpeptidase enzymes responsible for cross-linking bacterial cell wall peptidoglycan. This disrupts structural integrity and leads to osmotic lysis. Its spectrum of activity covers key Gram-positive organisms (e.g., *Streptococcus pyogenes*, *Enterococcus* spp., *Listeria monocytogenes*) and selected Gram-negative organisms that lack beta-lactamase (e.g., non-producing *Haemophilus influenzae*, *Neisseria meningitidis*).

Bacterial laryngitis, while representing a minority of all laryngitis cases, encompasses clinically serious conditions — acute epiglottitis (historically caused by *H. influenzae* type b), perilaryngeal and supraglottic abscesses (often involving Group A Streptococcus or mixed flora), and rare granulomatous infections such as actinomycosis. In these bacterial subtypes, beta-lactam antibiotics including Ampicillin have been used as part of standard-of-care management. The TxGNN knowledge graph likely captured this mechanistic and epidemiological connection.

The critical limitation, however, is that greater than 90% of clinical laryngitis is caused by viruses (parainfluenza, rhinovirus, influenza), for which Ampicillin has absolutely no therapeutic role. Additionally, beta-lactamase-producing strains are increasingly prevalent even among the bacterial pathogens associated with laryngeal infections, limiting the practical utility of unprotected Ampicillin monotherapy. The prediction is biologically plausible for a narrow bacterial subtype, but the TxGNN model has not distinguished between viral and bacterial laryngitis at the disease-ontology level.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing surveillance of CLAVAMOX® (Amoxicillin/Clavulanate) in Japanese pediatric patients with infections including laryngitis, tonsillitis, and bronchitis. The study drug is not Ampicillin; this trial provides indirect class-level evidence only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline Review | CoDAS | AGREE II quality assessment of clinical guidelines for laryngitis and pharyngitis management; provides evidence-based framework for antibiotic decision-making in laryngeal infections. |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Retrospective | Anaesthesia & Intensive Care | Review of 161 children with acute epiglottitis; documents 5 deaths and 45 complications, underscoring the severity of bacterial laryngeal disease and the necessity of antibiotic therapy. |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Case Series | Annals of Emergency Medicine | Three adult epiglottitis cases; highlights that bacterial laryngeal infection is underdiagnosed in adults and requires prompt antibiotic management. |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Retrospective | Western Journal of Medicine | Nine adult epiglottitis cases over 2 years; intubation required in 44% — reinforces antibiotic therapy as standard care for confirmed bacterial laryngeal infection. |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case Report/Review | Ann Otol Rhinol Laryngol | Historical review of spontaneous laryngeal abscess in the modern antibiotic era; connects beta-lactam antibiotic treatment to historical management of laryngeal suppurative infections. |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case Report | Auris Nasus Larynx | Laryngeal actinomycosis in a post-bone-marrow-transplant patient; infection resolved after prolonged penicillin-class antibiotic therapy — supports the mechanism of beta-lactams in rare bacterial laryngitis. |
| [8651625](https://pubmed.ncbi.nlm.nih.gov/8651625/) | 1996 | Case Series | Ann Otol Rhinol Laryngol | Laryngotracheal rhinoscleroma (*Klebsiella rhinoscleromatis*); early mucosal-stage disease responds to tetracycline but illustrates the broader concept of antibiotic therapy for chronic bacterial laryngeal infections. |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case Report | Auris Nasus Larynx | COVID-19 presenting as acute epiglottitis with necrotic laryngeal lesions; illustrates the importance of distinguishing infectious etiologies in laryngeal emergencies. |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Retrospective | Eur Arch Otorhinolaryngol | Microbiological analysis of neck and laryngeal abscesses in diabetic patients; highlights pathogen distribution and antibiotic selection, with beta-lactam sensitivity data for organisms relevant to laryngeal infections. |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | Case Report | Acta Otorrinolaringol Esp | Two cases of paraglottic laryngeal abscess — a rare but life-threatening entity requiring rapid antibiotic intervention; context for bacteria-targeted treatment of laryngeal suppuration. |

---

## Malaysia Market Information

A total of **18 Ampicillin product registrations** are confirmed in Malaysia (NPRA database, queried 2026-03-27). The drug is actively marketed. Detailed product names, dosage forms, manufacturers, and approved indication texts were not returned in this data pack's license records.

Please consult the [NPRA BPfarmasi portal](https://www.bpfarmasi.gov.my) directly for complete product-level information including registration numbers, dosage forms (capsule, powder for injection, oral suspension), and approved indications for each licensed product.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (flagged as data gaps requiring retrieval from the NPRA package insert PDF and DrugBank API).

> **Note for reviewers:** Two blocking data gaps have been identified:
> - **Package insert warnings/contraindications** (Severity: Blocking) — required before any S1 safety evaluation can proceed. Source: NPRA official website, method: download and parse package insert PDF.
> - **Mechanism of action data** (Severity: High) — affects mechanistic rationale analysis. Source: DrugBank API query for DB00415.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.97%), but the evidence level is L4 (preclinical/mechanism-level), and the clinical applicability is severely constrained by the fact that the vast majority of laryngitis is viral. No Ampicillin-specific clinical trial for laryngitis exists; the only identified trial studied a different compound (Amoxicillin/Clavulanate). The mechanistic link is valid only for confirmed bacterial subtypes (e.g., acute epiglottitis, laryngeal abscess with susceptible pathogens), which are distinct from the broad ICD entity "laryngitis." This prediction likely reflects a true biological connection at the pathogen level but is not actionable as a repurposing candidate without substantial additional refinement.

**To proceed, the following is needed:**

- **Resolve blocking data gap**: Obtain and parse the NPRA/TFDA package insert for Ampicillin to extract approved indications, warnings, and contraindications — prerequisite for any clinical safety evaluation.
- **Retrieve MOA data**: Query DrugBank API for DB00415 to formally document the mechanism of action and confirm spectrum of activity.
- **Refine the disease phenotype**: Narrow the indication from "laryngitis" (broad entity, >90% viral) to a specific bacterial subtype — e.g., *H. influenzae* epiglottitis, laryngeal actinomycosis, or supraglottic abscess caused by susceptible organisms — before assessing repurposing potential.
- **Assess resistance landscape**: Evaluate current regional prevalence of beta-lactamase-producing strains among pathogens causing laryngeal infections in Malaysia (e.g., via NPRA or MOH antimicrobial surveillance data), as resistance significantly limits the utility of unprotected Ampicillin.
- **Consider combination formulations**: Given widespread beta-lactamase production, evaluate whether Ampicillin-Sulbactam (rather than Ampicillin alone) would be the more appropriate repurposing candidate for bacterial laryngeal infections.
- **Cross-reference higher-ranked predictions**: The evidence pack contains 10 predicted indications; notably, **bacterial arthritis (Rank 8, L2 evidence, "Proceed with Guardrails")** and **chronic rhinosinusitis (Rank 4, L3, "Proceed with Guardrails")** show stronger clinical justification and may warrant prioritization over laryngitis for next-stage evaluation.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

