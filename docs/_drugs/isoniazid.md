---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 1
---

# Isoniazid
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line antituberculosis drug that inhibits mycolic acid synthesis in *Mycobacterium tuberculosis*. The TxGNN model predicts it may be effective for **Conjunctivitis**, but the supporting evidence — 1 clinical trial and 20 publications — largely reflects tuberculous/phlyctenular conjunctivitis (an ocular manifestation of TB already treated with standard anti-TB regimens) and isoniazid-induced ocular adverse effects, not a genuine new mechanistic indication for general conjunctivitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (per repurposing rationale; NPRA license indication text not available in current data extract) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, isoniazid is a first-line antituberculosis agent that inhibits mycolic acid synthesis in the mycobacterial cell wall; this mechanism has no direct pharmacological relationship to conjunctivitis.

The apparent link between isoniazid and conjunctivitis in the evidence base is explained by two confounded phenomena rather than a genuine new indication: (1) **tuberculous/phlyctenular conjunctivitis** is a rare ocular manifestation of TB that is already treated with standard anti-TB regimens including isoniazid — this is an extension of the existing TB indication, not a new one; and (2) isoniazid has documented **ocular adverse effects** (including drug-induced conjunctivitis), meaning some literature describes isoniazid *causing* ocular symptoms rather than treating them.

The high TxGNN score (99.36%) is most plausibly driven by a TB–conjunctivitis comorbidity edge in the knowledge graph rather than a true treatment signal, and mechanistically the prediction lacks support for conjunctivitis as a general (non-tuberculous) condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic adverse drug reaction rates between 3HP (rifapentine + isoniazid) and 1HP regimens for latent TB infection. This trial evaluates safety of an isoniazid-containing regimen and is **not related to conjunctivitis treatment** (relevance graded C / unrelated). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Systemic drugs causing ocular effects; notes isoniazid (and isotretinoin, sulfonamides, salicylates) among drugs **associated with causing** conjunctivitis, i.e. an adverse effect, not a treatment. |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Eskimos in Alaska — the most direct treatment-evidence in this set, but specific to TB-associated phlyctenular disease. |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case report | Annales d'oculistique | Local (topical) use of isoniazid in treatment of ocular tuberculosis. |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case report | Can J Ophthalmol | Conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case report | Cornea | Mycobacterium tuberculosis presenting as chronic red eye (conjunctival TB). |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case report | Oftalmologia | Phlyctenular keratoconjunctivitis and lymph node tuberculosis, 28 cases. |
| [4233886](https://pubmed.ncbi.nlm.nih.gov/4233886/) | 1968 | Case report | Arch Ophtalmol Rev Gen Ophtalmol | Tuberculosis of the bulbar conjunctiva. |

*Note: literature entries concerning BCG-related polyarthritis (unrelated drug/mechanism), rifampicin (drug mismatch), and toxic epidermal necrolysis (unrelated ADR) were excluded as not relevant to this indication.*

## Malaysia Market Information

License-level detail (authorization numbers, product names, dosage forms, indication text) is not available in the current NPRA data extract. The registry confirms **6 licensed products** with market status "Marketed."

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/NPRA warning and contraindication data, and DDI data, are currently unavailable — flagged as a Blocking data gap that must be resolved before any safety pre-assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between isoniazid and conjunctivitis is not supported by a plausible independent mechanism — the evidence base instead reflects TB-associated ocular disease (already covered by existing TB treatment) and isoniazid-induced ocular adverse effects. The single clinical trial identified is unrelated (safety comparison in latent TB treatment), and no RCT or systematic review supports isoniazid as a treatment for general conjunctivitis.

**To proceed, the following is needed:**
- Confirm whether the intended new indication is specifically "tuberculous/phlyctenular conjunctivitis" (a plausible extension of the existing TB indication) rather than general conjunctivitis
- Obtain TFDA/NPRA package insert warnings, contraindications, and DDI data (currently Blocking gap)
- Obtain confirmed mechanism of action documentation
- If pursuing the TB-conjunctivitis angle, seek dedicated clinical evidence beyond isolated case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

