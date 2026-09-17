---
layout: default
title: Theophylline
parent: High Evidence (L1-L2)
nav_order: 644
evidence_level: L1
indication_count: 5
---

# Theophylline
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **5** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Theophylline: From Established Bronchodilator Therapy to Asthma (Confirmatory Signal)

## One-Sentence Summary

Theophylline is a long-established methylxanthine bronchodilator used for decades in asthma and COPD, though the current registry extract does not carry the exact approved indication text on file. The TxGNN model's top prediction points back to **Asthma** — the drug's own historical indication — supported by **48 clinical trials** and **20 publications** in the evidence pack, making this a confirmatory signal rather than a novel repurposing finding. The TxGNN score itself is reported as **0.00%**, which is anomalous given the volume of supporting evidence and should be verified against the source pipeline before this is used for prioritization.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in the current registry extract; theophylline is a long-established bronchodilator for asthma/COPD per decades of literature (e.g., PMID 8471184: "used in the treatment of asthma for over 50 years") |
| Predicted New Indication | Asthma (top-ranked; same disease category as established use — see caveat below) |
| TxGNN Prediction Score | 0.00% (score value as reported — recommend verifying, given the strength of supporting evidence) |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal MOA documentation is flagged as a data gap in this pack, but the evidence pack's own rationale field is informative: theophylline acts through **phosphodiesterase (PDE) inhibition combined with adenosine receptor antagonism**, producing bronchial smooth muscle relaxation and anti-inflammatory effects. This mechanistic basis underlies decades of standard clinical use in obstructive airway disease.

Importantly, the top-ranked predicted indication — asthma — is not a new therapeutic area for theophylline; it is the drug's own long-standing, well-documented indication (see literature evidence below, spanning 1983–2020). This means the finding should be read as the model **correctly recovering an already-established indication** rather than surfacing a genuinely novel repurposing opportunity. The evidence pack itself notes that a majority of the 48 matched clinical trials are not theophylline-specific interventions (e.g., trials of Symbicort, lebrikizumab, or biologics where theophylline appears only as a permitted background therapy) — the mechanistic and efficacy support is drawn mainly from the long-standing literature rather than from these trials directly.

Lower-ranked candidates (allergic asthma, bronchitis, pulmonary emphysema, intrinsic asthma) represent plausible mechanistic extensions of the same bronchodilator/anti-inflammatory action but carry progressively weaker direct evidence (L3–L5), with intrinsic asthma flagged as Hold (L5, S0) due to lack of subtype-specific data.

---

## Clinical Trial Evidence

Selected from 48 matched trials, prioritizing studies where theophylline is a direct study intervention or comparator:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00252785](https://clinicaltrials.gov/study/NCT00252785) | Phase 3 | Completed | 340 | Symbicort Turbuhaler 160/4.5µg vs Pulmicort + Theolong (theophylline) tablet in Japanese asthma patients |
| [NCT00000578](https://clinicaltrials.gov/study/NCT00000578) | Phase 3 | Completed | N/A | NHLBI Asthma in Pregnancy Trial (ATPT): RCT of inhaled beclomethasone vs theophylline in moderate asthma during pregnancy |
| [NCT00756418](https://clinicaltrials.gov/study/NCT00756418) | Phase 4 | Completed | 84 | Montelukast vs theophylline added to inhaled corticosteroid in pediatric bronchial asthma |
| [NCT00119496](https://clinicaltrials.gov/study/NCT00119496) | Phase 2/3 | Completed | 79 | Theophylline reverses corticosteroid resistance in asthmatic smokers; compared with rosiglitazone + ICS |
| [NCT01132781](https://clinicaltrials.gov/study/NCT01132781) | Phase 2 | Completed | 28 | Effect of theophylline in patients with allergic rhinitis (comorbid airway disease with asthma) |
| [NCT02023554](https://clinicaltrials.gov/study/NCT02023554) | N/A | Completed | 40 | PK drug-interaction study: effect of azithromycin on steady-state theophylline plasma levels (Chinese population) |
| [NCT01684683](https://clinicaltrials.gov/study/NCT01684683) | Phase 4 | Completed | 100 | Efficacy and safety of 24-week theophylline treatment in non-cystic fibrosis bronchiectasis |
| [NCT04789499](https://clinicaltrials.gov/study/NCT04789499) | Phase 2 | Completed | 51 | Intranasal theophylline (PDE inhibitor) for COVID-19-related anosmia/dysgeusia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8471184](https://pubmed.ncbi.nlm.nih.gov/8471184/) | 1993 | Review | Drug Safety | Theophylline used in asthma for 50+ years; reviews risk/benefit balance versus newer bronchodilators |
| [8614425](https://pubmed.ncbi.nlm.nih.gov/8614425/) | 1996 | Review | New England Journal of Medicine | Established clinical review of theophylline's role in asthma management |
| [2010095](https://pubmed.ncbi.nlm.nih.gov/2010095/) | 1991 | Review | Geriatrics | Theophylline's changing role and controversies in asthma and COPD |
| [7589387](https://pubmed.ncbi.nlm.nih.gov/7589387/) | 1995 | Review | European Respiratory Journal | Theophylline and selective PDE inhibitors as anti-inflammatory agents in bronchial asthma |
| [9756184](https://pubmed.ncbi.nlm.nih.gov/9756184/) | 1998 | Review | Clin Exp Allergy | Theophylline's effects on airway inflammation beyond bronchodilation |
| [1735811](https://pubmed.ncbi.nlm.nih.gov/1735811/) | 1992 | Cohort/Clinical study | Journal of Pediatrics | Safety and efficacy of theophylline in children with asthma |
| [11775391](https://pubmed.ncbi.nlm.nih.gov/11775391/) | 2001 | Review | Allergy and Asthma Proceedings | Theophylline decreases airway inflammation and accelerates eosinophil apoptosis at low doses |
| [32094104](https://pubmed.ncbi.nlm.nih.gov/32094104/) | 2020 | Review | Respiratory Medicine | Theophylline remains widely prescribed for asthma/COPD in resource-limited settings; anti-inflammatory and corticosteroid-resistance-reversing effects |
| [19479396](https://pubmed.ncbi.nlm.nih.gov/19479396/) | 1997 | Review | Medizinische Klinik | Combination of inhaled corticosteroid plus theophylline at least as effective as doubling ICS dose |
| [3315274](https://pubmed.ncbi.nlm.nih.gov/3315274/) | 1987 | Review | Chronobiology International | Sustained-release theophylline and unequal (evening-weighted) dosing for nocturnal asthma |

---

## Malaysia Market Information

Malaysia market status is **✓ Marketed** with **8 registered licenses** on file, but the registry extract in this evidence pack does not contain populated license numbers, product names, dosage forms, or indication text for these entries — this data needs to be pulled directly from the NPRA registry before market-facing claims can be made.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Theophylline has a deep base of literature and multiple Phase 3 trials supporting bronchodilator/anti-inflammatory efficacy in asthma, justifying an L1 evidence level. However, this "prediction" largely reconfirms theophylline's own established indication rather than identifying a genuinely new use, and the reported TxGNN score (0.00%) is inconsistent with the volume of supporting evidence — both points need resolution before this candidate is treated as a repurposing opportunity. Safety data (warnings, contraindications, DDI) is entirely unavailable and is a blocking gap for any S1 safety pass.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA package insert warnings and contraindications (DG001, blocking)
- Retrieve formal DrugBank MOA documentation (DG002)
- Verify the TxGNN score of 0.00% against the source scoring pipeline — likely a data/normalization anomaly given L1 evidence
- Populate the 8 Malaysia license records (product name, dosage form, approved indication text)
- Clarify with the review team whether "asthma" as the top-ranked candidate should be reclassified as a validation/QA case rather than a repurposing candidate, given it matches theophylline's own historical indication
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

