---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

# Bacitracin: From Superficial Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic widely used as a topical agent for superficial bacterial infections of the skin and eyes.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with a prediction score of 99.999%; however, **no clinical trials** and **no publications** currently directly support this specific indication, though strong mechanistic reasoning exists based on its established ophthalmic use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial bacterial infections (topical antibiotic — skin, eye, wound) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L4 — Mechanistic rationale based on existing ophthalmic use |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 27 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Bacitracin is a cyclic polypeptide antibiotic produced by *Bacillus subtilis* and *Bacillus licheniformis*. It works by interfering with bacterial cell wall synthesis, specifically by inhibiting the dephosphorylation of the C55-isoprenyl pyrophosphate lipid carrier, which is essential for peptidoglycan synthesis. This gives it potent activity against Gram-positive bacteria including *Staphylococcus* and *Streptococcus* species. Due to its nephrotoxicity when given systemically, it is used almost exclusively as a topical agent — in ointments for skin infections, wound care, and ophthalmic preparations.

Punctate epithelial keratoconjunctivitis (PEK) is an inflammatory condition of the cornea and conjunctiva characterised by scattered punctate epithelial erosions. While PEK can arise from viral, allergic, or environmental causes, a significant subset is driven by bacterial infection — particularly *Staphylococcus aureus*, *Moraxella*, and other Gram-positive organisms. Bacitracin ophthalmic ointment is already approved and widely used for superficial bacterial eye infections, placing it in direct therapeutic proximity to bacterial PEK.

The mechanistic link is straightforward: Bacitracin's antibacterial spectrum covers the common pathogens implicated in bacterial PEK, and the ointment vehicle provides an additional benefit of corneal surface lubrication and protection, which aids epithelial healing. This prediction essentially represents a clinical extension of Bacitracin's existing approved ophthalmic indication rather than a radical drug repurposing — strengthening the plausibility of the TxGNN model's prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered for the specific indication of punctate epithelial keratoconjunctivitis.

> **Note:** Although no trials target this exact indication, Bacitracin ophthalmic ointment has a long history of clinical use in bacterial eye infections, and PEK with a bacterial aetiology falls within its established therapeutic scope.

## Literature Evidence

Currently no related literature available for the specific combination of Bacitracin and punctate epithelial keratoconjunctivitis.

## Malaysia Market Information

Bacitracin has **27 registered products** in Malaysia. Detailed registration information (authorization numbers, product names, dosage forms, and approved indications) was not available in the current data extraction. Bacitracin products are typically available as:

- Topical ointments (skin)
- Ophthalmic ointments (eye)
- Combination products (e.g., with Polymyxin B, Neomycin)

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data are currently pending extraction from the NPRA database and product inserts. It is well-established that Bacitracin carries a risk of nephrotoxicity with systemic use, and topical application may rarely cause contact dermatitis or allergic reactions. Anaphylaxis has been reported in rare cases with topical Bacitracin.

## Other Predicted Indications of Interest

Beyond the top-ranked prediction, the TxGNN model identified several other potential indications. The most noteworthy are summarised below:

### Rank 4: Otitis Externa (Evidence Level L3)

| Item | Detail |
|------|--------|
| TxGNN Score | 99.969% |
| Recommendation | Proceed with Guardrails |
| Rationale | Bacitracin (often combined with Polymyxin B) is already used clinically for bacterial otitis externa. Gram-positive coverage plus ointment vehicle make it suitable for ear canal infections. |

**Literature supporting this indication:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Clinical Comparison | Eur Arch Otorhinolaryngol | 151-patient RCT comparing Polymyxin B + Bacitracin ointment alone vs. with hydrocortisone for acute otitis externa |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Clinical Study | Z Laryngol Rhinol Otol | Local treatment of inflammatory ear processes with Nebacetin (Bacitracin + Neomycin) |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Clinical Review | Md State Med J | Practical treatment of otitis externa |
| [4306877](https://pubmed.ncbi.nlm.nih.gov/4306877/) | 1969 | Clinical Review | Z Arztl Fortbild | Use of antibiotics in otologic practice |
| [165871](https://pubmed.ncbi.nlm.nih.gov/165871/) | 1975 | Clinical Study | Can Med Assoc J | Use of trimethoprim-sulfamethoxazole in external otitis |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | In vitro / Veterinary | Zentralbl Veterinarmed B | Susceptibility of bacterial isolates from chronic otitis externa to antibiotics including Bacitracin |

### Rank 2: Exposure Keratitis (Evidence Level L4)

| Item | Detail |
|------|--------|
| TxGNN Score | 99.991% |
| Recommendation | Proceed with Guardrails |
| Rationale | Bacitracin ophthalmic ointment is already part of standard clinical practice for exposure keratitis — providing both antibacterial prophylaxis against secondary infection and physical corneal lubrication/protection through the ointment base. |

### Indications Recommended as Hold

| Rank | Disease | TxGNN Score | Reason for Hold |
|------|---------|-------------|-----------------|
| 3 | Non-human animal disease | 99.970% | Not applicable to human medicine |
| 5 | Postinfectious vasculitis | 99.968% | No mechanistic link; topical agent cannot treat systemic vasculitis |
| 7 | Infective urethral stricture | 99.965% | Topical formulation cannot reach target; primary pathology is fibrosis, not infection |
| 8 | Post-infectious syndrome | 99.965% | Overly broad category; no anti-inflammatory or immunomodulatory activity |
| 9 | Infection-related HUS | 99.962% | Antibiotic use may worsen STEC-associated HUS; topical agent cannot treat systemic disease |
| 10 | Chagas cardiomyopathy | 99.961% | Caused by protozoan (*T. cruzi*); antibacterial agent has zero activity against parasites |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (punctate epithelial keratoconjunctivitis) is highly plausible because Bacitracin ophthalmic ointment is already approved and used for superficial bacterial eye infections — PEK with bacterial aetiology is a natural therapeutic extension. The otitis externa indication (rank 4) is supported by published clinical comparison data. Both represent low-risk expansions of existing clinical use rather than radical repurposing.

**To proceed, the following is needed:**
- Detailed mechanism of action data from DrugBank (currently a data gap)
- NPRA product insert safety information including warnings, contraindications, and precautions
- Extraction of detailed Malaysia registration data (authorization numbers, product names, dosage forms, approved indications) for the 27 registered products
- Clinical review to confirm that PEK indication is not already covered by existing approved ophthalmic indications (may be a labelling gap rather than true repurposing)
- For otitis externa: systematic review of existing evidence including the Mösges et al. 2007 clinical comparison study

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-09.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

